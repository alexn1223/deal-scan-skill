# How to use deal-scan

## What to supply

At minimum, **one identifier**: a company name, or a URL. More is better and cheaper:

| You have | Give it | Why it helps |
|---|---|---|
| Website | the URL | Anchors every other lookup |
| Legal entity name | exact spelling | Registry search is exact-match |
| Jurisdiction | country | Picks the right registry immediately |
| Founder names | as spelled | Halves the people block |
| Contract address | `0x…` + chain | Triggers the web3 branch |
| Deck or one-pager | upload it | Claims from it get checked against public sources |

Nothing from an uploaded deck enters the dossier as fact. It becomes a set of claims to
go verify, and each one ends up confirmed by a public source, contradicted by one, or in
`gaps.md`.

## What a run costs

A scan is roughly 22–28 fetches and covers every block. On a Free claude.ai account that
is a real fraction of the message budget, so the scan is bounded deliberately and stops.

A deep pass runs only when you ask for one, by section:

    deep competitors
    deep founders
    deep registry

Each appends to the dossier under the same rules.

## Reading the output

Every line carries a class. The one to watch is `primary-self` — it establishes that the
company **said** something, not that it is so. A claim carrying only `primary-self`
sources is unconfirmed by definition, however plausible it reads.

Where two sources disagree, both are shown and neither is resolved. That is deliberate.

`gaps.md` distinguishes three things, and they are not the same:

- **not found** — searched, named sources, no match
- **blocked** — the source exists and could not be reached (bot protection, paywall, login)
- **not checkable** — no public source of this kind exists for this jurisdiction

## What it will not do

Tell you whether to invest, whether the team is strong, whether the valuation is fair, or
whether anything is a red flag. Ask and you get the refusal in `references/refusal.md`.
The skill will offer to go find more sources instead, which is the only thing it can
honestly do about an uncertain question.
