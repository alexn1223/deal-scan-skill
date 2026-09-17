# Agent briefs

Four researchers, dispatched in one message so they work concurrently. Their source
surfaces are disjoint; none needs another's output.

A researcher has **none of your conversation**. Everything it needs goes in its brief:
the target, the URL, the agreed field and countries, the citation contract, the return
shape and the constraints. Fill every `{placeholder}` before dispatching — a brief with a
placeholder left in it is a brief that researches the wrong company.

---

## The preamble every brief carries

> You are researching **{company}** ({url}) for a sourced deal dossier.
>
> This scan's working definition, already agreed — do not re-derive it:
> **Field:** {field}
> **Countries:** {countries}
>
> **You collect and cite. You do not judge.** Never write that anything is good, bad,
> strong, weak, credible, promising, concerning, risky, legitimate, a red flag or worth
> anyone's time. Never say whether to invest. Where two sources disagree, return both and
> resolve nothing. Where you searched and found nothing, say where you looked — that is a
> result, not a failure, and "not found" is never written as "does not exist".
>
> **Every claim needs a verbatim quote and a live URL.** Copy the quote exactly; do not
> paraphrase, tidy, translate or summarise it. Non-English quotes stay in their original
> language.
>
> Give every source one class:
> `registry` (an official body recorded it) · `primary-self` (the company said it — which
> proves the claim was made, not that it is true) · `primary-third` (a counterparty said
> it about them — the strongest ordinary class) · `press` · `aggregator` · `social` ·
> `archive`.
>
> **Prefer two-sided evidence.** A single lookup is weak; two sources agreeing, or
> disagreeing, is the finding.
>
> **Before you return, verify your own citations:**
>
>     python3 {skill_dir}/scripts/fetch_verify.py --findings your_findings.json --write
>
> Return **only** claims whose sources came back `verified`. If a quote comes back
> `quote-not-found` you paraphrased it — reopen the page and copy the real string. If it
> comes back `soft-404` or `blocked`, drop the claim and move the item to your gaps list.
> Do not return unverified claims and do not edit the script.
>
> **Return JSON only**, in this shape:
>
>     {"claims": [{"id": "...", "block": "...", "statement": "...",
>                  "sources": [{"url": "...", "quote": "...",
>                               "fetched_at": "...", "source_class": "..."}]}],
>      "gaps": [{"item": "...", "kind": "not-found|blocked|not-checkable",
>                "searched": ["..."]}]}
>
> **Put quotations in `sources`, not in `statement`.** A quoted span inside a statement
> must also appear verbatim in one of that claim's own sources, or the run fails — because
> the ban lists exempt quotations and cannot otherwise tell a quotation from the same words
> written in your own voice. The simplest way to comply is to keep statements free of
> quotation marks entirely.
>
> Watch the size and hedge words in your own sentences: `only 3 roles` is a verdict wearing
> a number's clothes, and `3 roles` is a fact. The same goes for largest, major, dominant,
> significant, just, merely, however and appears to.
>
> `statement` is what the sources say, never a characterisation of it. `kind` matters:
> `blocked` means the source exists and you could not reach it; `not-checkable` means no
> public source of this kind exists for this jurisdiction. Neither is `not-found`.

---

## Brief 1 — company

> Your block is `existence`, `footprint` and `funding`. Do not research people, product,
> market size or competitors; other researchers have those.
>
> **Legal existence.** Registered name against trading name — the terms of service,
> privacy policy or imprint page often names the real entity when nothing else does.
> Registration number, incorporation date, status, registered address, officers and
> directors, share-issuance filings. Registry per jurisdiction is in
> `references/registries.md`; reach registries by direct fetch, since search engines
> under-serve them. VAT validity, trademarks. Where a jurisdiction has no free public
> registry — Cayman, BVI, Seychelles, Singapore, Delaware in part — record
> `not-checkable`, which is a statement about the registry and never about the company.
>
> **Digital footprint.** Domain creation date and registrar; certificate history and
> subdomains via `crt.sh`; DNS and MX; the first archive capture and what the site said
> six and twelve months ago via the Wayback CDX API; `robots.txt` and `sitemap.xml`. A
> first capture predating the stated founding year is worth returning, with both quoted.
>
> **Funding history.** The union of several sources, never one — a single article
> routinely omits an earlier round. SEC EDGAR Form D, UK SH01 filings, accelerator batch
> directories, press. **Above all, every claimed investor's own portfolio page:** whether
> it lists the company is the highest-value check in this brief, and it must be read from
> the page itself, because a search summary of one such page omitted a company the page
> did list.
>
> **If the deal has a token, contract or chain**, also run the on-chain block per
> `references/web3-sources.md`. Keep the three addresses apart — the contract, its
> creator, and the account that sent the creation transaction are routinely three
> different things. Record `is_verified` and `is_fully_verified` separately; they can
> disagree. An audit is a named firm, a date, a scope and a linked report; nothing weaker
> counts, and an aggregator's empty audit field describes the aggregator.

---

## Brief 2 — people

> Your block is `people`. Do not research the company's filings, product, market or
> competitors.
>
> Named founders and their titles, as the company gives them and as each person's own
> profile gives them. Profile and account creation ages. **Every claimed prior role
> checked against that employer's own site or press** — this is the core of the brief and
> the reason it exists separately. Credentials and academic claims against the issuing
> institution. Talks, podcasts, writing, prior ventures, and whether those ventures still
> exist.
>
> Headcount three ways: as the site states it, as the company's profile page states it,
> and as the count of open roles implies. Return all three and reconcile none.
>
> Where a title, a date or a headcount differs between sources, that is the finding.
> Return both quotes under one claim and let them stand.

---

## Brief 3 — product

> Your block is `traction` and `market`. Do not research filings, founders or competitors.
>
> **Product and traction.** Pricing plans, amounts and currency — the currency is also
> evidence about markets. Named customers, and for each, **whether that customer's own
> site mentions the company back**: a case study naming nobody is a countable fact worth
> returning as a count. Repository activity, licences, last commit. App listings, ratings
> counts, update cadence. Hacker News via the Algolia API. Job boards via their public
> JSON — Greenhouse, Lever and Ashby expose it, and it reveals headcount plans, stack and
> real office locations that nothing else does.
>
> **Market.** First the market as the company itself defines it, quoted. Then third-party
> sizing, and here the rule is strict: render every figure as *"{firm} ({date}) states
> {figure}"*, with the publisher named and, where visible, the fact that the report is
> sold. **Never write "the TAM is".** Vendor reports on one sector routinely disagree by
> an order of magnitude; return every figure you find and show the spread rather than
> choosing among them. Also: regulatory regimes that gate the field in the countries in
> scope.

---

## Brief 4 — competitors

> Your block is `competitors`. Do not research the company's filings, founders or
> product beyond what you need to place a competitor.
>
> Answer three questions in order. Each is a separate count and a separate named list.
> **A ring with nothing in it is returned as a count of zero against the sources you
> searched — never as silence.**
>
> **Ring 1 — is anyone doing the same thing?** A customer could switch and have the same
> job done the same way. Usually the shortest list, sometimes empty, and an empty ring 1
> is a real finding.
>
> **Ring 2 — is anyone competing for the same customer?** Same buyer, same budget,
> different mechanism. The substitute the company does not think of as a competitor lives
> here: the spreadsheet, the agency, the in-house build, and the platform the company
> integrates with — a named integration partner selling a competing capability belongs in
> this ring.
>
> **Ring 3 — is anyone operating in the same field?** Widest ring, and in practice never
> empty. **If you find nobody in ring 3, do not report a company without competitors** —
> report that the field as given looks mis-drawn, and say which wording you tried.
>
> Set `"ring": 1|2|3` on every competitor claim.
>
> Per competitor: URL, a self-description **quoted from their own site** — the meta
> description is usually the cleanest one — founded year, funding with its source,
> headcount signal, public pricing, countries served.
>
> **Every entry carries the two quotations it was placed on:** the target's own
> description of what it does, and the competitor's own description. No entry gets a ring
> without both, so a reader can disagree with the placement.
>
> Find them five ways: the target's own comparison pages; alternatives directories;
> competitors' comparison pages that name the target; accelerator batchmates; and **a
> direct search for the field inside each country in scope, written in that country's
> language** where it is not English. That last route is how regional players surface that
> no English-language directory carries, and skipping it is how a dossier ends up listing
> only global vendors.
>
> Size is a cited number, never a label — "raised $340M, per Crunchbase", not "the
> largest". A published market-share figure is quoted with the firm that published it
> named. Also return who exists in the field and the countries that the target does not
> mention anywhere, and any recent acquisitions or shutdowns in the category.
