---
name: deal-scan
description: Desk research on a startup deal — market, competitors, geography, company existence and founder verification — returned as a dossier in which every line carries a verbatim quote and a live URL. Use when checking out a company before or during a deal.
---

# deal-scan

Desk research on one company, returned as a sourced dossier. The skill searches to find
out what exists, fetches to make each line citable, and hands back three files: the
readable dossier, the same content structured, and an explicit list of what it could not
resolve.

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

If asked "so is this a good deal?", the answer is the fixed refusal in
`references/disclaimer.md`, not an opinion.

## What it produces

    dossier.md     the readable document — every line a quote and a link
    findings.json  the same content structured, one record per claim
    gaps.md        what could not be resolved, and where it was looked for

`gaps.md` is not optional. Silence about a missing thing reads as absence of a problem,
so every unresolved item is written down with the sources that were tried.

## Two gears

**Scan** is the default and the only thing that runs unasked. It is a bounded pass —
roughly 22–28 fetches — that covers every block below and ends with the gaps list.

**Deep** runs only when the user names a section: "go deep on competitors", "go deep on
the founders". It appends to the existing dossier under the same citation rules. Never
run a deep pass on your own initiative; the budget is the user's to spend.

Offer both in the first message, and say the scan's approximate fetch count before
starting, because on a Free claude.ai account that budget is real.

## Search finds, fetch cites

These two tools fail in opposite directions and are not interchangeable.

**Search has recall without precision.** It surfaces what you did not know to look for —
accelerator batches, prior raises, category acquisitions, competitor names, market
reports. It returns a synthesis across many pages and cannot tell you which page said
which thing.

**Fetch has precision without recall.** It quotes exactly, but only from a URL you
already have.

Therefore: **nothing enters the dossier on the strength of a search result alone.** Search
decides where to look. The fetch of that page is what makes a line citable. A claim you
could not fetch a page for goes in `gaps.md`, not in the dossier.

This is not a style preference. A search summary of an investor's portfolio page omitted
a portfolio company that the page itself listed; a dossier built on the summary would
have asserted, with confidence, something false about a real company.

## Source classes

Every source carries one, assigned mechanically from the domain. See
`references/source-classes.md`.

| Class | What it proves |
|---|---|
| `registry` | An official body recorded it |
| `primary-self` | The company **said** it — never that it is true |
| `primary-third` | A counterparty said it about them — the strongest ordinary class |
| `press` | A publication reported it |
| `aggregator` | A third-party database holds it |
| `social` | A profile asserts it |
| `archive` | A capture or certificate log recorded it at a date |

`primary-self` is the class most often mistaken for fact. Render it so the reader cannot
miss that it is the company's own claim.

The highest-value findings are almost never single lookups. They are two-sided: the
company names an investor — does that investor's own site list them? The site claims a
headcount — what does the company's LinkedIn page say? A founder claims a prior role —
does that employer's own site or the press say so? Pair sources deliberately.

## The blocks

Run every block in a scan. A block that yields nothing produces gaps entries, not silence.

1. **Legal existence** — registry, number, incorporation date, status, officers, share
   issuance filings, VAT validity, trademarks. Jurisdictions with no public registry
   (Cayman, BVI, Singapore, Delaware in part) are recorded as **not checkable**, which is
   not the same as not found. Registry map: `references/registries.md`.
2. **Digital footprint** — domain age, certificate history and subdomains via crt.sh,
   DNS and MX, first archive capture and what the site said earlier, robots and sitemap,
   and the pages themselves: about, team, pricing, customers, careers, docs, terms,
   privacy, imprint. The imprint and the terms of service often name the real legal
   entity when nothing else does.
3. **Founders and team** — named founders and titles, profile and account ages, claimed
   prior roles checked against those employers, credentials, headcount as stated by the
   site versus the company profile versus open job count.
4. **Traction signals** — pricing, named customers and whether the customer mentions them
   back, app listings, repository activity, Hacker News via the Algolia API, and job
   boards, whose public JSON reveals headcount plans, stack and real office locations.
5. **Funding history** — union of several sources, never one. A single article routinely
   omits an earlier round. SEC EDGAR Form D, UK SH01 filings, accelerator directories,
   and above all the claimed investors' own portfolio pages.
6. **Market** — the market as the company defines it, quoted. Then third-party sizing
   rendered only as *"&lt;firm&gt; (&lt;date&gt;) states &lt;figure&gt;"*, with who published it and
   what they were selling. Never "the TAM is". Vendor reports on the same market
   routinely disagree by an order of magnitude; show the spread and let it speak.
7. **Operating scope — the field, and the countries.** Everything in the competitor
   block depends on two decisions taken here, so both are written down where the user can
   correct them. **The field**: one line, built from the company's own self-description,
   quoted. **The countries**: where the customers and the revenue are, which is not
   necessarily where the company is registered or where the team sits. Evidence for the
   country list: the languages and currencies the site offers, customers named or
   described, the currency on the pricing page, job post locations, region-specific
   channels and integrations, and any regulatory regime the company says it operates
   under. Both the field and the country list are the scan's **working definition**,
   labelled as such and never written as a fact about the company. Say both back to the
   user before the competitor block runs — a wrong field produces a wrong competitor set,
   and correcting it here costs one message instead of a whole pass.
8. **Competitors — three rings, asked in order.** Each ring is a question with a count
   and a named list, and each is answered separately. A ring with nothing in it is
   reported as a count of zero against the sources searched, never as silence.

   **Ring 1 — is anyone doing the same thing?** A customer could switch and have the same
   job done the same way. Usually the shortest list, sometimes empty, and an empty Ring 1
   is a real finding worth stating plainly.

   **Ring 2 — is anyone competing for the same customer?** Same buyer and same budget,
   different mechanism. This is where the substitute the company does not think of as a
   competitor lives, including the spreadsheet, the agency, and the in-house build.

   **Ring 3 — is anyone operating in the same field?** Widest ring, and in practice never
   empty. It is the context the first two rings are read against.

   Per competitor, in every ring: URL, a self-description **quoted from their own site**,
   founded year, funding with its source, headcount signal, public pricing, and the
   countries served.

   **Ring assignment is a judgement, so it is shown rather than asserted.** Each entry
   carries the two quotations it was placed on — the target's own description of what it
   does, and the competitor's own description — so the reader can disagree with the
   placement. No entry is assigned a ring without both.

   **An empty Ring 3 fails the run.** Every field has other people working in it, so a
   Ring 3 of zero is evidence that the field in block 7 was drawn wrongly — too narrow,
   or in the wrong words — and the fix is to redraw it and search again. It is never
   written up as a company having no competitors.

   Found five ways: the target's own comparison pages; alternatives directories;
   competitors' comparison pages that name the target; accelerator batchmates; and a
   direct search for the field **within each country, in that country's language** where
   it is not English, which is how regional players surface that no English-language
   directory carries.

   Size is a cited number, never a label — "raised $340M, per Crunchbase", not "the
   largest". Published market-share figures are quoted with the firm that published them
   named, handled exactly as sizing is in block 6. Also recorded: who exists in the field
   and the countries that the target does not mention, and recent acquisitions or
   shutdowns in the category.

9. **Web3** — run only if the deal has a token, contract or chain. Endpoints and their
    traps are in `references/web3-sources.md`; all of it is reachable at tier 0 with no
    API key. Collect: the contract and whether its source is verified — `is_verified` and
    `is_fully_verified` are different fields and may disagree; the compiler version and
    verification timestamp; the creation transaction and its date; **three addresses kept
    apart** — the contract, its creator, and the account that sent the creation
    transaction, which are routinely three different things and whose conflation invents
    a fact; proxy type and implementations, recorded as fields rather than as a
    conclusion about upgradeability; supply and holder concentration; any published
    unlock schedule; audits as a named firm, date, scope and linked report, and nothing
    weaker; TVL and volume; repository ages and push dates; and prior launches by the
    same addresses.

10. **Run metadata** — branch taken, tier, every URL with its fetch timestamp and
    outcome, and the fetch count.

## Fetching is not trivial here

Run `scripts/fetch_verify.py`. Do not hand-verify.

**A 200 does not mean the page exists.** Single-page applications return HTTP 200 with a
"not found" body. Matching on the text of that body fails too, because frameworks ship
the string inside the bundle of every page, including live ones. The reliable test is a
**control probe**: fetch a deliberately random path on the same host first, fingerprint
the response, and compare every later fetch against it. A page byte-identical to the
control is dead, whatever its status code.

**A fetch has three outcomes, not two.** `found`, `not-found`, and `blocked`. Bot
protection, a paywall or a login wall is `blocked`, and recording it as `not-found` is a
lie: the information exists and could not be reached. `blocked` sources are listed in
`gaps.md` by name.

**Verify against raw bytes, never against a summarizer.** A fetch tool that answers a
prompt about a page returns a model's paraphrase; it will supply URLs that do not resolve
and quotes that do not appear. Draft from it if you like. Verification is exact substring
matching against the raw response, and that is what decides whether a line ships.

## Gates

    python scripts/fetch_verify.py --findings findings.json
    python scripts/validate_output.py --findings findings.json --dossier dossier.md

`fetch_verify.py` re-fetches every cited URL, control-probes its host, and asserts the
quoted string appears verbatim. `validate_output.py` requires that every claim carries at
least one verified source with a class and a timestamp, enforces
`references/ban-list.md`, and requires the gaps section to exist. A failing run does not
ship; fix the dossier or move the claim to `gaps.md`.

## Refusals

Asked whether to invest, whether the team is strong, whether the valuation is fair,
whether the market is attractive, or whether anything is a red flag: give the refusal in
`references/disclaimer.md` and offer to collect more sources instead.

This is desk research from public sources at one moment in time. It is not legal due
diligence, not an audit, not a background check, and not advice.
