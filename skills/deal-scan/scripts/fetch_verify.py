#!/usr/bin/env python3
"""Re-fetch every cited URL and prove the quoted string is actually there.

Three things this does that a naive checker does not:

1. Control probe. A single-page app answers HTTP 200 for a URL that does not exist,
   and ships its own "not found" text inside the bundle of every page, so neither the
   status code nor a content marker can be trusted. For each host we first fetch a
   deliberately random path, fingerprint the response, and treat any later page whose
   fingerprint matches it as dead.

2. Three outcomes. found / not-found / blocked. Bot protection and paywalls are not
   absence of information and are not recorded as such.

3. Exact matching against raw bytes. Never against a summariser's paraphrase.

Standard library only. Exit 0 if every source verified, 1 otherwise.
"""

import argparse
import gzip
import hashlib
import html
import json
import random
import re
import string
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 deal-scan/1.0"
TIMEOUT = 25
PAUSE = 0.4

BLOCK_STATUS = {401, 402, 403, 407, 429, 451}
BLOCK_MARKERS = (
    "enable javascript and cookies",
    "just a moment",
    "checking your browser",
    "cf-browser-verification",
    "access denied",
    "are you a robot",
    "captcha",
    "subscribe to continue",
    "this content is for subscribers",
)

_SCRIPT = re.compile(r"<(script|style|noscript)\b[^>]*>.*?</\1>", re.I | re.S)
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_META = re.compile(r"<meta\b[^>]*?content=([\"'])(.*?)\1[^>]*>", re.I | re.S)
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def is_markup(text, ctype=""):
    """Only treat a body as HTML when it really is one.

    Stripping tags from JSON that carries source code is destructive: a Solidity
    body containing `a < b` and a later `>` looks like a tag to the regex, and in
    testing that deleted 281,684 of 515,784 characters of an explorer response —
    including the string being verified. Tag handling is opt-in, not the default.
    """
    if "json" in ctype.lower():
        return False
    if "html" in ctype.lower() or "xml" in ctype.lower():
        return True
    head = text.lstrip()[:400].lower()
    if head.startswith(("{", "[")):
        return False
    return "<html" in head or "<!doctype html" in head or "<body" in head


def normalise(raw, markup=True):
    """Comparable text. Tags and entities are handled only for real markup."""
    text = raw
    if markup:
        # Hoist <title> and every <meta content="..."> before tags are removed.
        # A company's own meta description is its cleanest self-description, and it
        # lives inside an attribute — which tag stripping would otherwise delete,
        # making the one string most worth quoting impossible to verify.
        hoisted = [m.group(1) for m in _TITLE.finditer(text)]
        hoisted += [m.group(2) for m in _META.finditer(text)]
        text = _SCRIPT.sub(" ", text)
        text = _TAG.sub(" ", text)
        text = " ".join(hoisted) + " " + text
        text = html.unescape(text)
    return _WS.sub(" ", text).strip()


def fetch(url):
    """Return (status, text, error). Never raises."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en,uk;q=0.8,de;q=0.6",
        "Accept-Encoding": "gzip",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                try:
                    body = gzip.decompress(body)
                except OSError:
                    pass
            charset = resp.headers.get_content_charset() or "utf-8"
            ctype = resp.headers.get("Content-Type", "")
            return resp.status, body.decode(charset, errors="replace"), None, ctype
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return exc.code, body, None, exc.headers.get("Content-Type", "") if exc.headers else ""
    except Exception as exc:
        return None, "", f"{type(exc).__name__}: {exc}", ""


def fingerprint(text, markup=True):
    norm = normalise(text, markup)
    return {"len": len(norm), "sha": hashlib.sha256(norm.encode()).hexdigest()[:16]}


def host_profile(host_url, cache):
    """Fingerprint an absent path AND the root, once per host.

    A client-rendered app serves one identical shell for every path, including
    absent ones — so on such a host the control probe cannot tell a live page
    from a dead one, and naively treating "matches control" as dead condemns
    the real homepage. Probing the root settles which world we are in: if the
    root is byte-identical to a deliberately absent path, the host is an SPA
    and its control probe is uninformative rather than damning.
    """
    parts = urlparse(host_url)
    host = parts.netloc
    if host in cache:
        return cache[host]
    nonce = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
    probe = f"{parts.scheme}://{host}/zzz-deal-scan-{nonce}"
    status, text, err, ctype = fetch(probe)
    control = None if err or not text else fingerprint(text, is_markup(text, ctype))
    time.sleep(PAUSE)

    spa = False
    if control:
        rs, rt, rerr, rct = fetch(f"{parts.scheme}://{host}/")
        time.sleep(PAUSE)
        if not rerr and rt:
            spa = fingerprint(rt, is_markup(rt, rct))["sha"] == control["sha"]

    cache[host] = {"control": control, "spa": spa}
    return cache[host]


def looks_blocked(status, text):
    if status in BLOCK_STATUS:
        return True
    low = text[:4000].lower()
    return any(marker in low for marker in BLOCK_MARKERS)


def verify_source(src, cache):
    url = src.get("url", "")
    quote = src.get("quote", "")
    if not url:
        return {"outcome": "invalid", "detail": "source has no url"}
    if not quote:
        return {"outcome": "invalid", "detail": "source has no quote"}

    prof = host_profile(url, cache)
    control, spa = prof["control"], prof["spa"]
    is_root = urlparse(url).path in ("", "/")
    status, text, err, ctype = fetch(url)
    time.sleep(PAUSE)
    markup = is_markup(text, ctype)

    if err:
        return {"outcome": "unreachable", "detail": err}
    if looks_blocked(status, text):
        return {"outcome": "blocked", "status": status,
                "detail": "bot protection, paywall or login wall"}
    if status and status >= 400:
        return {"outcome": "not-found", "status": status}

    fp = fingerprint(text, markup)
    if control and fp["sha"] == control["sha"] and not (spa or is_root):
        return {"outcome": "soft-404", "status": status,
                "detail": f"byte-identical to control probe ({fp['len']} chars)"}

    page = normalise(text, markup)
    want = _WS.sub(" ", html.unescape(quote) if markup else quote).strip()
    if want.lower() in page.lower():
        result = {"outcome": "verified", "status": status, "chars": fp["len"],
                  "body": "markup" if markup else "data"}
    if spa:
        result["liveness"] = ("undetermined — client-rendered host serves one "
                              "shell for every path, so a dead sub-path cannot "
                              "be distinguished from a live one")
    return result

    # Quote absent. Report the longest prefix that IS present, to show how far it got.
    best = 0
    for end in range(len(want), 20, -10):
        if want[:end].lower() in page.lower():
            best = end
            break
    return {"outcome": "quote-not-found", "status": status,
            "detail": f"matched first {best} of {len(want)} chars"}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--write", action="store_true",
                    help="write verification results back into the findings file")
    args = ap.parse_args()

    with open(args.findings, encoding="utf-8") as fh:
        doc = json.load(fh)

    claims = doc.get("claims", [])
    cache, tally, failures = {}, {}, []
    checked = 0

    for claim in claims:
        for src in claim.get("sources", []):
            result = verify_source(src, cache)
            src["verification"] = result
            src["verified_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            outcome = result["outcome"]
            tally[outcome] = tally.get(outcome, 0) + 1
            checked += 1
            mark = "ok  " if outcome == "verified" else "FAIL"
            print(f"  {mark} {outcome:<16} {src.get('url','')[:78]}")
            if outcome != "verified":
                failures.append((claim.get("id", "?"), src.get("url", ""), result))

    if args.write:
        doc.setdefault("run", {})["verified_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with open(args.findings, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=2, ensure_ascii=False)

    print(f"\n{checked} sources across {len(claims)} claims")
    for outcome in sorted(tally):
        print(f"  {outcome:<16} {tally[outcome]}")

    if failures:
        print(f"\n{len(failures)} source(s) did not verify. Each must be corrected,")
        print("or its claim moved to gaps.md. Unverified sources do not ship.")
        return 1
    print("\nAll sources verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
