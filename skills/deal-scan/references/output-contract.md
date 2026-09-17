# Output contract

Human-readable mirror of what the run writes and what `scripts/validate_output.py`
checks. Documentation only; the scripts do not read this file.

`findings.json` is assembled by the orchestrator from what the four researchers return.
Each researcher has already run `fetch_verify.py` over its own set, so every source
arriving here carries a `verification` block reading `verified`; the orchestrator's gate
re-checks that rather than trusting it. Where two researchers returned the same claim
from different sources, the sources merge onto one claim. Where they disagree, the claim
carries `conflict: true` and both sides stand.

## Three files

| File | Contents |
|---|---|
| `dossier.md` | The readable document |
| `findings.json` | The same content structured, per `schema/findings.schema.json` |
| `gaps.md` | What could not be resolved, and where it was looked for |

`findings.json` is the source of truth. `dossier.md` is a rendering of it, and rule R7
enforces that: a quotation appearing in the dossier that is not in `findings.json` fails
the run.

## Two kinds of text, and only two

Every line of `dossier.md` is either a **verbatim quotation** — a Markdown blockquote,
prefixed `> ` — or **skill-authored scaffold**: headings, labels, table cells,
connective text.

The ban lists apply to authored text and never to quotations. A source may say anything;
quoting it is reporting, not asserting. The skill using the same word in its own voice is
a verdict, and fails.

The disclaimer section is exempt from both, and is reproduced verbatim from
`references/disclaimer.md`.

## Section order

1. **Header** — target, branch, tier, date, fetch count
2. **Identity & funding**
3. **Cross-checks** — claims confirmed or contradicted by a `primary-third` source
4. **People**
5. **Digital footprint**
6. **Traction**
7. **Market**
8. **Operating scope** — the field and the countries, labelled as the scan's working definition
9. **Competitors**
10. **Web3** — present only on the web3 branch
11. **Disagreements** — every claim with `conflict: true`, both sides shown
12. **Could not find** — a pointer into `gaps.md`
13. **Disclaimer** — verbatim

A block that yielded nothing keeps its heading and carries gap entries. Dropping the
heading hides the fact that nothing was found.

## How a claim renders

    **<statement>** · `<source_class>`
    > "<quote>" — [<domain>](<url>)

A claim with several sources carries several quote lines. A claim with `conflict: true`
renders under a "N sources disagree" label with every source shown and no resolution.

## The ten rules

| Rule | Requirement |
|---|---|
| R1 | Every claim carries at least one source |
| R2 | Every source carries `url`, `quote`, `fetched_at`, `source_class` |
| R3 | `source_class` is one of the seven in `references/source-classes.md` |
| R4 | Every source verified by `fetch_verify.py` with outcome `verified` |
| R5 | Neither ban list appears in skill-authored text |
| R6 | `gaps.md` exists, is populated, and labels entries `not-found` / `blocked` / `not-checkable` |
| R7 | Every dossier quotation traces to a source in `findings.json` |
| R8 | The disclaimer section is present |
| R9 | Every competitor claim carries a ring of 1, 2 or 3, and ring 3 is not empty |
| R10 | A quotation inside a `statement` also appears in one of that claim's own sources |

R10 exists because the ban lists exempt quotations, and a quotation inside a statement is
indistinguishable from the skill's own voice unless it can be traced. List C in
`references/ban-list.md` handles the other half of the same problem: phrases such as
*persons with significant control* are statutory names that happen to contain a banned
word, and are blanked out before either list runs.

`scripts/render_dossier.py` writes `dossier.md` and `gaps.md` from `findings.json`, which
is what makes R7 meaningful — the dossier is a rendering, never a parallel document.

R9 deserves a note too. Ring 3 — anyone operating in the same field — is never
legitimately empty, so a run that finds nobody there has almost certainly defined the
field wrongly in the scope block rather than discovered a company with no competitors.
The rule fails the run and points back at the scope definition. R9 is skipped entirely
when the competitor block was not run, so a partial scan is not punished for it.

R6 deserves a note. A scan that resolved everything is a scan that did not look hard
enough — every real company has something the public record does not carry. An empty
gaps file fails.

## Verification outcomes

`fetch_verify.py` assigns one per source. Only `verified` ships.

| Outcome | Meaning |
|---|---|
| `verified` | The quoted string appears at the URL, on a page that is not the control fingerprint |
| `quote-not-found` | Page live, quotation absent — usually a paraphrase that got through drafting |
| `soft-404` | HTTP 200, but byte-identical to a deliberately random path on the same host |
| `blocked` | Bot protection, paywall or login wall. **Information exists and was not reached** |
| `not-found` | Genuine 4xx |
| `unreachable` | DNS, TLS or timeout failure |
