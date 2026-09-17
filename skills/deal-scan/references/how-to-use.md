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

## How a run goes

**First you get a scope, and you are asked to confirm it.** The skill spends a couple of
browses on the site and comes back with two lines — the field it thinks the company is
in, and the countries it thinks the customers are in, both labelled as a working
definition rather than a fact. Correct either one. A wrong field sends four researchers
after the wrong competitors, and fixing it at that point costs one message.

**Then four researchers run at once**, on disjoint ground:

| Researcher | Looks for |
|---|---|
| company | Registry and filings, domain and site history, funding history, on-chain if there is a contract |
| people | Founders, titles, prior roles checked against those employers |
| product | Pricing, customers, repositories, job boards, and how the field is sized |
| competitors | Ring 1, ring 2, ring 3 — including a search in each country's own language |

Each one verifies its own quotations before reporting, so a paraphrase is fixed by the
researcher that wrote it rather than surviving into the dossier.

**Then the results are merged** into the three files, and the whole thing goes through a
nine-rule gate before you see it.

To go further on one area afterwards, name it: `more on competitors`, `more on the
founders`. That re-dispatches the one researcher.

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
