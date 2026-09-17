---
name: deal-scan-lite
description: A quick web-search brief on a startup — who the team is, what the company does, how big the field is, whether they have raised, and who else works in it — with a link on every line. Use for a fast first look at a company.
---

# deal-scan-lite

A quick first look at one company, from web search alone. Four questions, in order,
because each one tells you how to ask the next. Fifteen minutes, one pass, no setup.

One company per run. Everything here comes from searching the open web.

## The line

This skill collects and links. It does not judge.

It may say what a source says, who said it and when. It may say that two sources disagree,
and show both. It may say it looked for something and did not find it, and name where it
looked.

It may never say a company is good, risky, credible, promising, concerning or a scam. It
may never say whether to invest, meet or pass. Avoid the size and hedge words too — "the
largest", "only three people", "however", "appears to", "worth noting". Write the number
and let it sit there.

If asked "so is this a good deal?", say plainly that this is a first look built from
public sources, that it has no basis for an opinion, and offer to go deeper on whichever
part matters.

## Four steps, in order

### 1. Who they are and what they do

Search the company by name, then its site. Get: what it sells, in its own words; the
founders and their titles; roughly when it started; where it is based. Read the About and
team pages if they exist.

Finish this step by writing down, in one line each:

- **The field**, in the company's own language wherever possible.
- **The countries** where its customers are — which is not necessarily where it is
  registered. Site languages, pricing currency, named customers and job locations all
  point at this.

**Say both back to the user before going on.** Everything after this depends on them, and
a wrong field sends steps 2 and 4 somewhere useless.

### 2. How big the field is, and who the customers would be

Search for sizing of that field. Every figure is written as *"&lt;firm&gt; (&lt;date&gt;) states
&lt;figure&gt;"* — named publisher, named date. **Never "the market is worth X".** These are
vendor reports sold for money, and reports on the same sector routinely disagree by an
order of magnitude. Find two or three, show the spread, and let the disagreement be the
finding.

Then: who actually buys this. Take it from the company's own customer and pricing pages
where they exist, from the job posts it runs, and from who its named customers are —
not from a guess about who might want it.

### 3. Have they raised

Search for funding news. Get the amount, the date, the round name and the investors. Then
two checks worth the extra minute:

- **Look for more than one round.** A single article routinely omits an earlier raise.
- **Open a named investor's own portfolio page.** Whether they list the company is the
  single most useful thing in this step, and it takes one click.

Different sources often give different amounts for the same round, in different
currencies. Report every figure with its source; reconcile nothing.

### 4. Who else works in this field

Three questions, each answered with a count and names:

- **Anyone doing the same thing?** A customer could switch and get the same job done the
  same way. Often a short list, sometimes none — and none is a real finding.
- **Anyone chasing the same customer?** Same buyer, different approach. The in-house
  build, the agency, the spreadsheet, and the platform this company integrates with all
  live here.
- **Anyone else in the field at all?** Nearly always someone. **If this comes back empty,
  the field in step 1 was drawn wrong** — redraw it and search again, rather than
  reporting a company with no competitors.

For each name: what they say they do, quoted from their own site, and their size as a
**cited number** — "raised $40M, per Crunchbase" — never as "the biggest".

If the customers are in a country that does not speak English, **search in that language
too.** Regional players often appear nowhere in English-language listings, and skipping
this is how a brief ends up naming only the global vendors.

## Every line carries a link

No claim without a source next to it. Prefer the company's own site for what the company
claims, a counterparty's site for anything about a relationship — an investor listing
them, a customer naming them — and a publication for events.

Mark what kind of source each one is, because it changes what the line proves:

- **the company itself** — proves they said it, never that it is so
- **a counterparty** — the strongest thing you can get quickly
- **press** · **a database** · **a profile**

Say what you looked for and did not find. An absent registration number or an unnamed
customer list is worth writing down; silence about it reads as though there was nothing to
find. Distinguish **could not find it** from **could not reach it** — a page behind a
login or a bot wall is not an absence.

## What this version does not do

It is built on search, so it inherits search's limits, and you should know them:

- **Quotes are not verified.** A search result is a summary across many pages, it
  paraphrases, and it can attribute things to the wrong source. Quote from a page you
  actually opened, and treat anything from a results summary as a lead rather than a fact.
  A search summary of an investor's portfolio page once omitted a company that page did
  list — the same check by opening the page gave the opposite answer.
- **No company registry.** Incorporation dates, officers, share filings and previous
  company names are not covered here, and they are often where the interesting
  disagreement is.
- **No domain age, archive history or on-chain data.**

For any of that — and for quotes checked verbatim against the live page by script — use
the full `deal-scan` skill, which runs four researchers in parallel and gates the result.
It needs Claude Code, because it dispatches subagents. This one runs anywhere.

## Disclaimer

Reproduce this at the end of every brief:

> This is a quick first look assembled from public web sources at a single moment in time.
> It is not due diligence, not an audit, not a background check and not investment advice.
> Nothing here is a judgement about the company, the people or the opportunity. Sources go
> stale and absence from a search is not evidence that something does not exist. Anything
> that matters to a decision should be confirmed with the company or with counsel first.
