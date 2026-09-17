#!/usr/bin/env python3
"""Decide whether a dossier is allowed to exist.

Eight rules. Any failure means the run does not ship: either fix the dossier, or move
the offending claim into gaps.md where unsourced statements belong.

Run scripts/fetch_verify.py first — rule R4 reads the verification results it writes.

Standard library only. Exit 0 if every rule passes, 1 otherwise.
"""

import argparse
import json
import os
import re
import sys

CLASSES = {"registry", "primary-self", "primary-third", "press",
           "aggregator", "social", "archive"}
REQUIRED_SOURCE_FIELDS = ("url", "quote", "fetched_at", "source_class")
GAP_KINDS = {"not-found", "blocked", "not-checkable"}
_WS = re.compile(r"\s+")


def load_ban_list(path):
    """Read List A, List B, and an optional List C of exemptions."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    blocks = re.findall(r"```(.*?)```", text, re.S)
    if len(blocks) not in (2, 3):
        raise SystemExit(f"ban-list.md must hold 2 or 3 fenced blocks, found {len(blocks)}")
    lists = []
    for block in blocks:
        entries = [ln.strip() for ln in block.splitlines()
                   if ln.strip() and not ln.strip().startswith("#")]
        lists.append(entries)
    while len(lists) < 3:
        lists.append([])
    return lists[0], lists[1], lists[2]


QUOTED = re.compile(
    # Only unambiguous quotation delimiters. A bare ' is an apostrophe far more
    # often than a quote mark -- "Horizons' own site" is not a quotation, and
    # treating it as one produced 17 false positives on real agent output.
    r'"([^"]{15,})"'
    r"|\u201c([^\u201d]{15,})\u201d"
    r"|\u00ab([^\u00bb]{15,})\u00bb"
    r"|\u2018([^\u2019]{15,})\u2019"
)


def quoted_spans(text):
    return [g for m in QUOTED.finditer(text) for g in m.groups() if g]


def strip_exempt(text, exemptions):
    """Blank out terms of art before the ban lists see the text."""
    for phrase in exemptions:
        text = re.compile(re.escape(_WS.sub(" ", phrase)), re.I).sub(" ", text)
    return text


def compile_entry(entry):
    if " " in entry:
        return re.compile(re.escape(_WS.sub(" ", entry)), re.I)
    return re.compile(rf"\b{re.escape(entry)}\b", re.I)


def authored_text(dossier):
    """Everything the skill wrote itself: not blockquotes, not the disclaimer."""
    lines, out, in_disclaimer = dossier.splitlines(), [], False
    for line in lines:
        stripped = line.strip()
        if re.match(r"^#{1,6}\s+disclaimer\b", stripped, re.I):
            in_disclaimer = True
            continue
        if in_disclaimer and stripped.startswith("#"):
            in_disclaimer = False
        if in_disclaimer or stripped.startswith(">"):
            continue
        out.append(line)
    return "\n".join(out)


def blockquotes(dossier):
    return [_WS.sub(" ", ln.strip().lstrip(">").strip())
            for ln in dossier.splitlines() if ln.strip().startswith(">")]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--gaps")
    ap.add_argument("--ban-list")
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    ban_path = args.ban_list or os.path.join(here, "..", "references", "ban-list.md")
    gaps_path = args.gaps or os.path.join(os.path.dirname(args.dossier), "gaps.md")

    with open(args.findings, encoding="utf-8") as fh:
        doc = json.load(fh)
    with open(args.dossier, encoding="utf-8") as fh:
        dossier = fh.read()

    claims = doc.get("claims", [])
    failures = []

    def fail(rule, message):
        failures.append(f"{rule}  {message}")

    # R1 — every claim carries at least one source.
    for claim in claims:
        if not claim.get("sources"):
            fail("R1", f"claim {claim.get('id','?')!r} has no source: "
                       f"{claim.get('statement','')[:70]!r}")

    # R2/R3 — source records are complete and classed.
    for claim in claims:
        for i, src in enumerate(claim.get("sources", [])):
            where = f"claim {claim.get('id','?')} source {i}"
            for field in REQUIRED_SOURCE_FIELDS:
                if not src.get(field):
                    fail("R2", f"{where} missing {field!r}")
            cls = src.get("source_class")
            if cls and cls not in CLASSES:
                fail("R3", f"{where} has unknown source_class {cls!r}")

    # R4 — every source verified by fetch_verify.py.
    for claim in claims:
        for src in claim.get("sources", []):
            outcome = (src.get("verification") or {}).get("outcome")
            if outcome is None:
                fail("R4", f"claim {claim.get('id','?')} source not verified — "
                           "run fetch_verify.py first")
            elif outcome != "verified":
                fail("R4", f"claim {claim.get('id','?')} source {outcome}: "
                           f"{src.get('url','')[:60]}")

    # R5 — ban lists, on skill-authored text only.
    list_a, list_b, list_c = load_ban_list(ban_path)
    authored = strip_exempt(_WS.sub(" ", authored_text(dossier)), list_c)
    for label, entries in (("A", list_a), ("B", list_b)):
        for entry in entries:
            match = compile_entry(entry).search(authored)
            if match:
                start = max(0, match.start() - 40)
                fail("R5", f"list {label} term {entry!r} in authored text: "
                           f"…{authored[start:match.end() + 40].strip()}…")

    # R6 — gaps file exists, is populated, and distinguishes the three kinds.
    if not os.path.exists(gaps_path):
        fail("R6", f"no gaps file at {gaps_path} — it is not optional")
    else:
        with open(gaps_path, encoding="utf-8") as fh:
            gaps = fh.read()
        if len(gaps.strip()) < 40:
            fail("R6", "gaps file is empty; a scan that resolved everything is a scan "
                       "that did not look")
        if not any(kind in gaps for kind in GAP_KINDS):
            fail("R6", f"gaps file must label entries with one of {sorted(GAP_KINDS)}")

    # R7 — every blockquote in the dossier traces to a source in findings.json.
    known = {_WS.sub(" ", s.get("quote", "")).strip().lower()
             for c in claims for s in c.get("sources", [])}
    for quote in blockquotes(dossier):
        if len(quote) < 15:
            continue
        if not any(quote.lower() in k or k in quote.lower() for k in known):
            fail("R7", f"quoted in dossier but absent from findings.json: {quote[:70]!r}")

    # R10 — a quotation inside a statement must be in that claim's own sources,
    # and is exempt from the ban lists. Quoting a source is reporting; the same
    # words written in the skill's own voice are a verdict, and without this the
    # two are indistinguishable to the scanner.
    for claim in claims:
        st = claim.get("statement", "")
        own = " ".join(_WS.sub(" ", s.get("quote", ""))
                       for s in claim.get("sources", [])).lower()
        for span in quoted_spans(st):
            span_n = _WS.sub(" ", span).strip()
            if span_n.lower() not in own:
                fail("R10", f"claim {claim.get('id','?')} quotes {span_n[:50]!r} in its "
                            "statement, but no source of that claim carries it — put the "
                            "quotation in sources, or drop the quotation marks")

    # R9 — competitor rings. Skipped entirely when the block was not run.
    comp = [c for c in claims if c.get("block") == "competitors"]
    if comp:
        rings = []
        for claim in comp:
            ring = claim.get("ring")
            if ring not in (1, 2, 3):
                fail("R9", f"competitor claim {claim.get('id','?')!r} carries no ring "
                           f"(got {ring!r}); every entry is 1, 2 or 3")
            else:
                rings.append(ring)
        if rings and 3 not in rings:
            fail("R9", "ring 3 is empty. Every field has other people working in it, so "
                       "this is evidence the field in the scope block was drawn wrongly "
                       "— redraw it and search again. It is not a company without "
                       "competitors.")

    # R8 — disclaimer present.
    if not re.search(r"^#{1,6}\s+disclaimer\b", dossier, re.I | re.M):
        fail("R8", "dossier has no Disclaimer section")

    if failures:
        print(f"FAILED — {len(failures)} problem(s)\n")
        for line in failures:
            print(f"  {line}")
        print("\nFix each, or move the claim to gaps.md. A dossier that fails does "
              "not ship.")
        return 1

    sources = sum(len(c.get("sources", [])) for c in claims)
    print(f"PASSED — {len(claims)} claims, {sources} verified sources, 10/10 rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
