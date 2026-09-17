# Could not find — Occam Industries

Three kinds, and they are not the same thing. `not-found` means searched with no match. `blocked` means the source exists and could not be reached. `not-checkable` means no public source of this kind exists for this jurisdiction.

## blocked

**TYR.vc's own portfolio page (tyr.vc/portfolio, aka tyrvc.com/portfolio) listing Occam as an investment**

Searched: https://www.tyr.vc/portfolio; https://www.tyrvc.com/portfolio.

**UK trade mark registrations for 'Occam' / 'OccamX' at UKIPO**

Searched: https://trademarks.ipo.gov.uk/ipo-tmtext/#/search?query=occam (returns a captcha/JS application gate, not machine-readable).

**Internet Archive Wayback Machine first-capture date for occam.industries (earliest capture observed directly, before the fetch_verify re-check, was timestamp 20260316015000 i.e. 16 March 2026, per a manual CDX query); at verification time the Internet Archive's own service was returning HTTP 503 ('Internet Archive services are temporarily offline'), so the citation could not be re-verified and is withheld**

Searched: http://web.archive.org/cdx/search/cdx?url=occam.industries*&output=text&limit=30&fl=timestamp,original,statuscode.

**occam.industries has no separate machine-readable sitemap.xml — requesting that path returns byte-identical content to a random nonexistent path on the same host (single-page-app fallback), which fetch_verify's control-probe logic correctly flags as unusable for citation even though it is itself the finding**

Searched: https://occam.industries/sitemap.xml.

**Gui Wainwright LinkedIn profile (personal details, full work history, education, account creation age)**

Searched: https://www.linkedin.com/in/guiamwainwright/; https://uk.linkedin.com/in/guiamwainwright.

**Occam Industries LinkedIn company page (headcount, founding year as stated by LinkedIn directly, verbatim)**

Searched: https://www.linkedin.com/company/occam-industries.

**Guy Walker LinkedIn profile — appears to be a separate, more recently joined Occam Industries hire (distinct from CEO Gui Wainwright); his exact title/role and prior employer history could not be independently confirmed**

Searched: https://www.linkedin.com/in/guywalkerit/; https://uk.linkedin.com/in/guywalkerit.

**Daniil Bash LinkedIn profile (full work history, Antler/A*STAR/University of Cambridge role details, dates)**

Searched: https://uk.linkedin.com/in/daniil-bash; https://www.linkedin.com/in/daniil-bash/.

**Emilie Clarke role/title history at Occam (founder associate to Chief of Staff transition timeline)**

Searched: https://sifted.eu/articles/founder-associate-career-move; https://www.vestbee.com/insights/articles/occam-closes-3-m.

**Xinterra's LinkedIn post confirming Daniil Bash's co-founder role and PhD ('We are proud of our co-founder Daniil Bash, who defended his PhD thesis today. Congrats Dr. Bash!')**

Searched: https://www.linkedin.com/posts/xinterra_we-are-proud-of-our-co-founder-daniil-bash-activity-7034395599336603648-uXME.

**Fortune Business Insights and Grand View Research market-size pages for counter-UAS / drone software**

Searched: fortunebusinessinsights.com/counter-uas-market-111906 (Cloudflare 'Just a moment...' challenge page returned); grandviewresearch.com/industry-analysis/drone-software-market-report (Cloudflare 'Just a moment...' challenge page returned).

**Swarmer's own site self-description (swarmer.com)**

Searched: swarmer.com (Cloudflare JS challenge / interstitial, no content served to non-browser fetch); businesswire.com press release (HTTP 403 Forbidden).

## not-checkable

**EUIPO trade mark registrations for 'Occam' / 'OccamX'**

Searched: No automated lookup performed within session; EUIPO eSearch requires an interactive session not accessible via simple HTTP fetch.

**Whois/RDAP registrant identity for occam.industries (name/org/contact) beyond dates and nameservers**

Searched: https://rdap.identitydigital.services/rdap/domain/occam.industries (registrant fields redacted per standard privacy/GDPR redaction in RDAP response).

**Occam Industries headcount as stated directly on occam.industries website (site is JS-rendered and could not be scraped via WebFetch)**

Searched: https://occam.industries/; https://occam.industries/careers.

**City, University of London degree claim for Gui Wainwright, checked against the institution's own records/press**

Searched: Gui Wainwright City University of London degree.

**occam.industries homepage meta description and og:description, quoted verbatim ("Occam Industries — European defence technology... Sole European supplier to the Ukrainian front line" / "Modernising automation for modern conflict environments. Sole European supplier to the Ukrainian front line.")**

Searched: https://occam.industries/ via curl (text is genuinely present in the raw HTML head on direct fetch); fetch_verify.py control-probe check: the site is a client-side SPA that serves an identical static index.html shell -- including these same meta tags -- for any path, including a deliberately nonexistent random path; the verifier therefore flags the homepage fetch as byte-identical to its own 404 fallback (soft-404) and the claim cannot be distinguished from a dead page by this method, even though the quoted text is real and live.

**Brave1's own site/channels (brave1.gov.ua, catalog.brave1.gov.ua, my.brave1.gov.ua) independently stating Occam was cleared for integration testing**

Searched: brave1.gov.ua/en and brave1.gov.ua news listings (no Occam mention found via curl/grep); catalog.brave1.gov.ua (public catalog requires Diia authorization; closed catalog requires military Delta-system verification, so cannot be checked directly); web search for site:brave1.gov.ua Occam and catalog.brave1.gov.ua Occam (no direct hits; only third-party press repeating the claim, plus a press-quoted statement from Brave1 CEO Andrii Hrytseniuk, captured as pr13).

**Occam Industries' own site (occam.industries) as a directly fetchable citation**

Searched: occam.industries is a client-rendered single-page app that serves an identical static HTML shell (with meta description tags) for every path, including nonexistent ones, so the automated fetch-verify control probe cannot distinguish the real page from a soft-404 and every direct citation of it fails verification; web.archive.org snapshots of occam.industries (5 captures, Mar-Jun 2026) are also unrendered SPA shells; their static meta description at the time read only 'Autonomy Simplified', an earlier, thinner tagline than the site's current live meta description ('Occam Industries — European defence technology. Tactical autonomy, machine vision, and scalable operational capability. Sole European supplier to the Ukrainian front line.', confirmed present in the live HTML source via direct curl but not independently verifiable through fetch_verify.py); used eu-startups.com's verbatim quotation of Occam's own product description ('a retrofit computer vision-enabled autopilot designed specifically for FPV drones', attributed to the company) as the verifiable stand-in for the target's self-description in every ring claim below.

**Full country-served lists and headcount/pricing signals for ring-1 and ring-2 competitors beyond what appears in the cited self-descriptions and funding press**

Searched: ModalAI (US-manufactured, sells globally per its own description) and Theseus (US, DoD/Special Forces customers per press) both serve markets outside the UK/Ukraine/wider-Europe scope the target is defined by, but no public pricing page was found on any of the ring-1/ring-2 sites checked (thefourthlaw.ai, theseus.us, dodsolution.com, auterion.com, modalai.com, quantum-systems.com, tekever.com, anduril.com) -- none publish list prices.

## not-found

**Antler's own portfolio directory page listing Occam Industries as a portfolio company (searched the general portfolio listing and a search-parameterised URL; only Antler's blog, not the portfolio grid itself, could be confirmed)**

Searched: https://www.antler.co/portfolio; https://www.antler.co/portfolio?search=occam.

**Freedom Fund VC's own site (freedom-fund.vc) listing Occam as a portfolio company**

Searched: http://freedom-fund.vc/; https://freedom-fund.vc/portfolio; http://freedom-fund.vc/portfolio.

**Presto Ventures' separate portfolio page (prestoventures.com/portfolio, distinct from the techhorizons.eu Presto Tech Horizons site) listing Occam**

Searched: https://www.prestoventures.com/portfolio.

**Independent (third-party) confirmation of Wainwright's specific employment at Cambridge Analytica or Ocado (e.g. via Ocado's own site, press mentioning him by name, or Cambridge Analytica records) beyond Occam-adjacent press (Antler blog, itkey.media) repeating the claim**

Searched: Gui Wainwright Ocado official; Gui Wainwright Cambridge Analytica; Guiam Wainwright Ocado Technology.

**OccamX pricing**

Searched: occam.industries site and JS bundle; press coverage (eu-startups, itkey.media, therecursive, oboronka.mezha.ua, bebeez, techfundingnews, startupnewswire).

**Named commercial or government customers with the counterparty's own site confirming a relationship with Occam Industries**

Searched: occam.industries site and JS bundle (no logos/customer names found); press coverage of the €3M pre-seed round (only investors and Brave1 named; 'European defence primes' and 'selected Ukrainian manufacturers' referenced but not named).

**Occam Industries GitHub repository activity, licences, last commit**

Searched: github.com/occam-industries (an org with this name exists but was created 2015-09-26, predates the company's 2024 founding, and its 2 public repos ('test', 'scaly_rshiny_1') are unrelated test/demo apps); GitHub search API for 'occam industries' and 'occamx' users/repos.

**Hacker News discussion of Occam Industries**

Searched: http://hn.algolia.com/api/v1/search?query=Occam%20Industries (zero results returned).

**Lever/Ashby job boards for Occam Industries**

Searched: api.lever.co/v0/postings/occamindustries; api.lever.co/v0/postings/occam (both returned 'Document not found'; Greenhouse board at boards-api.greenhouse.io/v1/boards/occamindustries/jobs is confirmed live and used instead, see pr9).

**ITAR/EAR exposure specific to Occam Industries**

Searched: occam.industries site and JS bundle; press coverage of the company (no ITAR/EAR statement found; company is UK-based so EAR/ITAR exposure would depend on US-origin components or technology, which was not confirmed in any source).

**Occam Industries comparison/alternatives page naming named competitors**

Searched: occam.industries site crawl for /compare, /vs, /alternatives pages (site has no such pages; it is a single-page app with no visible sub-navigation); site:occam.industries web search.

**Antler or Brave1 cohort page listing Occam alongside other named drone-autonomy portfolio companies as peers**

Searched: Antler defence tech cohort drone autonomy portfolio; antler.co blog Spring 2026 U.S. portfolio showcase (no Occam or drone-autonomy peer named); Brave1 market/dataroom listings for Occam specifically (not located by name in Brave1's own market/dataroom pages during this search).
