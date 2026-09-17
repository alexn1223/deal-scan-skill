#!/usr/bin/env python3
"""Render dossier.md and gaps.md from findings.json.

The dossier is a rendering of findings.json, never a separate document. Every
quotation it prints comes from a source record, which is what lets rule R7 run
the check in the other direction: a quotation in the dossier with no matching
record fails the run.

The renderer writes scaffold text and copies field values; it never paraphrases,
never adds a connective, and never comments. Standard library only.
"""

import argparse
import json
import os
import sys
from urllib.parse import urlparse

SECTIONS = [
    ("existence",   "Identity and filings"),
    ("footprint",   "Digital footprint"),
    ("funding",     "Funding history"),
    ("people",      "People"),
    ("scope",       "Operating scope"),
    ("traction",    "Product and traction"),
    ("market",      "Market"),
    ("competitors", "Competitors"),
    ("web3",        "On-chain"),
]
RINGS = {1: "Ring 1 — does the same thing",
         2: "Ring 2 — competes for the same customer",
         3: "Ring 3 — operates in the same field"}


def cite(src):
    dom = urlparse(src["url"]).netloc or src["url"]
    return f"> {src['quote']} — [{dom}]({src['url']})"


def render_claim(claim):
    out = []
    classes = sorted({s.get("source_class", "?") for s in claim.get("sources", [])})
    label = " · ".join(f"`{c}`" for c in classes)
    flag = " · **sources disagree**" if claim.get("conflict") else ""
    out.append(f"**{claim['statement']}** · {label}{flag}")
    for src in claim.get("sources", []):
        out.append(cite(src))
    out.append("")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--gaps", required=True)
    ap.add_argument("--disclaimer")
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    disc_path = args.disclaimer or os.path.join(here, "..", "references", "disclaimer.md")
    with open(args.findings, encoding="utf-8") as fh:
        doc = json.load(fh)
    run, claims, gaps = doc["run"], doc["claims"], doc.get("gaps", [])

    by_block = {}
    for c in claims:
        by_block.setdefault(c["block"], []).append(c)

    L = [f"# Deal scan — {run['target']}", ""]
    L.append(f"`branch: {run['branch']}` · `tier {run['tier']}` · `{run.get('started_at','')[:10]}` "
             f"· `{run.get('fetch_count','?')} fetches` · `{len(claims)} claims` "
             f"· `{sum(len(c['sources']) for c in claims)} verified sources`")
    L += ["", "Every line below is a quotation from a source, with that source linked. "
              "Nothing here is a judgement.", ""]

    for block, title in SECTIONS:
        items = by_block.get(block)
        if not items:
            continue
        L.append(f"## {title}")
        L.append("")
        if block == "competitors":
            for ring in (1, 2, 3):
                inring = [c for c in items if c.get("ring") == ring]
                L.append(f"### {RINGS[ring]} · {len(inring)} found")
                L.append("")
                for c in inring:
                    L += render_claim(c)
        else:
            for c in items:
                L += render_claim(c)

    conflicts = [c for c in claims if c.get("conflict")]
    L += ["## Disagreements", ""]
    if conflicts:
        for c in conflicts:
            L.append(f"- {c['statement']}")
        L.append("")
    else:
        L += ["None recorded among the claims above.", ""]

    kinds = {}
    for g in gaps:
        kinds[g["kind"]] = kinds.get(g["kind"], 0) + 1
    L += ["## Could not find", "",
          f"{len(gaps)} items, in `{os.path.basename(args.gaps)}`: "
          + ", ".join(f"{v} {k}" for k, v in sorted(kinds.items())) + ".", ""]

    with open(disc_path, encoding="utf-8") as fh:
        L += ["## Disclaimer", "", fh.read().strip(), ""]

    with open(args.dossier, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    G = [f"# Could not find — {run['target']}", "",
         "Three kinds, and they are not the same thing. `not-found` means searched with no "
         "match. `blocked` means the source exists and could not be reached. `not-checkable` "
         "means no public source of this kind exists for this jurisdiction.", ""]
    for kind in ("blocked", "not-checkable", "not-found"):
        items = [g for g in gaps if g["kind"] == kind]
        if not items:
            continue
        G += [f"## {kind}", ""]
        for g in items:
            G.append(f"**{g['item']}**")
            G.append("")
            G.append("Searched: " + "; ".join(g.get("searched", [])) + ".")
            G.append("")
    with open(args.gaps, "w", encoding="utf-8") as fh:
        fh.write("\n".join(G))

    print(f"wrote {args.dossier} ({len(L)} lines) and {args.gaps} ({len(gaps)} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
