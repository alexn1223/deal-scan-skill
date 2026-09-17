---
name: deal-scan
description: Research one startup deal in parallel — company and filings, people, product and market, competitors — returned as a dossier in which every line carries a verbatim quote and a live URL. Use when checking out a company before or during a deal.
---

# deal-scan

Research on one company, run as four researchers working at once and assembled into a
sourced dossier. You are the orchestrator: you fix the scope, write the briefs, dispatch,
and assemble. You do not do the research yourself.

One company per run.

## The line

This skill collects and cites. It does not judge.

It may state what a source says, who said it, and when. It may state that two sources
disagree, and show both. It may state that something was searched for and not found, and
name where it looked.

It may never say a company is good, risky, credible, promising, concerning, legitimate or
a scam. It may never say whether to invest, meet, pass or proceed. A disagreement between
sources is reported as a disagreement, never resolved. A missing document is reported as
absent from the sources searched, never as evidence of absence.

If asked "so is this a good deal?", give the refusal in `references/refusal.md`.

## What it produces

    dossier.md     the readable document — every line a quote and a link
    findings.json  the same content structured, one record per claim
    gaps.md        what could not be resolved, and where it was looked for

`gaps.md` is not optional. Silence about a missing thing reads as absence of a problem.

## How a run works

    1. Scope        you establish the field and the countries, and read them back
    2. Dispatch     four researchers, in one message, working concurrently
    3. Assemble     you merge what returns, run the gate, write the three files

### 1. Scope comes first, and it is yours

Competitors cannot be researched before the field is settled, so this step is not
delegated and not skipped. Spend two or three browses on the company's own site, then
write down:

- **The field** — one line, built from the company's own self-description, quoted.
- **The countries** — where the customers and the revenue are, which is not necessarily
  where the company is registered or where the team sits. Evidence: site languages and
  currencies, the currency on the pricing page, customers named or described, job post
  locations, region-specific channels and integrations, regulatory regimes the company
  names.

Both are the scan's **working definition**, labelled as such, never written as a fact
about the company. **Read both back to the user and wait.** A wrong field produces four
wrong briefs; correcting it here costs one message instead of a whole run.

### 2. Dispatch four researchers in one message

Issue all four in a single response, or they run one after another instead of at once.

| Agent | Covers |
|---|---|
| **company** | Legal existence and filings, digital footprint, funding history, and the on-chain block when the deal has a contract |
| **people** | Founders and team, titles, prior roles checked against those employers, profile and account ages |
| **product** | Pricing, named customers and whether the customer says so back, repositories, job boards, app listings, and how the field is sized by third parties |
| **competitors** | The three rings, including a search in the local language of each country in scope |

Each brief is written from `references/agent-briefs.md`, which holds the full collection
list, the return contract and the constraints for each. A brief is **self-contained**:
the researcher has none of this conversation, so the target, the URL, the agreed field
and countries, the source classes and the return shape all go into the brief itself.

The four surfaces are disjoint by design, so the researchers do not need each other and
do not share state.

### 3. Assemble

Merge the four returns into one `findings.json`, then run the gate. Where two researchers
returned the same claim from different sources, keep both sources on one claim — that is
what the `sources` array is for. Where they disagree, set `conflict: true` and show both.
Never resolve a disagreement.

## Every researcher verifies its own citations

This is the part that does not bend.

A browse tool answers a prompt **about** a page; it returns a model's paraphrase. In
testing it supplied a URL that returned 404 and quotes that were not on the page. So each
researcher, before returning anything, runs

    python3 scripts/fetch_verify.py --findings <its own findings> --write

and returns **only** claims whose sources came back `verified`. A paraphrased quote is
fixed by the researcher that drafted it, while it still has the page in context. A quote
that cannot be made to verify is dropped, and the item moves to that researcher's gaps
list.

The script exists because fetching is not as simple as it looks, and each of these was
found by running it, not by reasoning about it:

- **A 200 does not mean the page exists.** Single-page apps answer 200 for absent paths
  and ship their own "not found" text inside every page bundle, so neither the status code
  nor a content marker can be trusted. The script control-probes each host with a
  deliberately random path and treats a byte-identical response as dead.
- **A fetch has three outcomes.** `found`, `not-found`, and `blocked`. Bot protection, a
  paywall or a login wall is `blocked`, and recording it as `not-found` is a lie: the
  information exists and was not reached.
- **Markup and data need different handling.** Stripping HTML tags from a JSON body
  carrying source code deleted more than half an explorer response, including the string
  under verification.
- **The best self-description lives in an attribute.** A company's own meta description is
  the cleanest statement of what it does, and it sits inside a tag, so the script hoists
  `<title>` and every `<meta content="…">` before tags are removed.

## Source classes

Every source carries one, assigned from the domain. See `references/source-classes.md`.

| Class | What it proves |
|---|---|
| `registry` | An official body recorded it |
| `primary-self` | The company **said** it — never that it is true |
| `primary-third` | A counterparty said it about them — the strongest ordinary class |
| `press` | A publication reported it |
| `aggregator` | A third-party database holds it |
| `social` | A profile asserts it |
| `archive` | A capture or certificate log recorded it at a date |

The highest-value findings are two-sided, never single lookups: the company names an
investor — does that investor's own site list them? The site claims a headcount — what
does its company profile say? A founder claims a prior role — does that employer say so?
Every brief tells its researcher to pair sources deliberately.

## Competitors are three rings

The competitors brief asks three questions in order, each answered separately with its
own count and named list. A ring with nothing in it is reported as a count of zero
against the sources searched, never as silence.

- **Ring 1 — is anyone doing the same thing?** A customer could switch and have the same
  job done the same way. Usually shortest, sometimes empty, and an empty ring 1 is a real
  finding worth stating plainly.
- **Ring 2 — is anyone competing for the same customer?** Same buyer, same budget,
  different mechanism. Where the substitute the company does not think of as a competitor
  lives: the spreadsheet, the agency, the in-house build, and the platform it integrates
  with.
- **Ring 3 — is anyone operating in the same field?** Widest, and in practice never empty.

Ring assignment is a judgement, so it is shown rather than asserted: every entry carries
both quotations it was placed on — the target's own description of what it does, and the
competitor's own description.

**An empty ring 3 fails the run.** Every field has other people working in it, so nobody
in ring 3 means the field was drawn wrongly in step 1, not that the company has no
competitors. Redraw the field and dispatch the competitors brief again.

Size is a cited number, never a label. "Raised $340M, per Crunchbase" is checkable; "the
largest" is not, and the ban list refuses it.

## The gate

After assembling, and regardless of what the researchers reported:

    python3 scripts/validate_output.py --findings findings.json --dossier dossier.md

Nine rules, listed in `references/output-contract.md`: every claim sourced, every source
classed, timestamped and verified, both ban lists clear of anything you wrote yourself,
a populated gaps file, every quotation in the dossier traceable to `findings.json`, the
disclaimer present, and the competitor rings well formed.

Ban lists apply to what the skill writes, never to quotations. A source may say anything;
quoting it is reporting. Writing the same word yourself is a verdict.

A run that fails the gate does not ship.

## Refusals

Asked whether to invest, whether the team is strong, whether the valuation is fair,
whether the market is attractive, or whether anything is a red flag: give the refusal in
`references/refusal.md` and offer to dispatch a researcher for more sources instead.

This is desk research from public sources at one moment in time. It is not legal due
diligence, not an audit, not a background check, and not advice.
