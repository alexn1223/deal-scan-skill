# deal-scan

A Claude skill for desk research on one startup deal.

It collects market, competitor, geography, company-existence and founder information for
a single company and returns a dossier in which **every line carries a verbatim quote and
a live URL**. It renders no verdicts: where two sources disagree, both are shown and
neither is resolved, and a request for a judgement gets a fixed refusal.

    dossier.md     the readable document
    findings.json  the same content structured, one record per claim
    gaps.md        what could not be resolved, and where it was looked for

## Install for Claude Code

    /plugin marketplace add <github-user>/deal-scan-skill
    /plugin install deal-scan@deal-scan-skill

## Install for claude.ai or Claude Desktop

Zip the skill folder and upload it in Settings → Capabilities → Skills.

    cd skills && zip -qr deal-scan.zip deal-scan

## Dependencies

None. Standard library only.

## Using it

Name the skill and give it at least one identifier — a company name, a URL, or a contract
address:

    use deal-scan on acme.io

A **scan** is the default: a bounded pass of roughly 22–28 fetches covering every block,
ending with an explicit list of what it could not resolve. A **deep** pass runs only when
you ask for one by section (`deep competitors`, `deep founders`).

Two bundled samples run end to end without supplying anything of your own — one equity
deal and one web3 deal, both with their verification results recorded:

    python3 skills/deal-scan/scripts/fetch_verify.py \
        --findings skills/deal-scan/samples/obriy-ai.findings.json

    python3 skills/deal-scan/scripts/validate_output.py \
        --findings skills/deal-scan/samples/angstrom.findings.json \
        --dossier  skills/deal-scan/samples/angstrom.dossier.md \
        --gaps     skills/deal-scan/samples/angstrom.gaps.md

## How it decides what may ship

Two scripts stand between the model and the output.

`fetch_verify.py` re-fetches every cited URL and asserts the quoted string is actually
there. It control-probes each host with a deliberately random path first, because a
single-page app answers HTTP 200 for URLs that do not exist and ships its own "not found"
text inside every page bundle — so neither the status code nor a content marker can be
trusted. It separates `blocked` from `not-found`, because bot protection is not absence
of information. It matches against raw bytes, and it handles JSON and markup differently,
because stripping tags from an explorer response full of source code destroys the content
being checked.

`validate_output.py` enforces eight rules: every claim sourced, every source classed and
timestamped, every source verified, both ban lists clear of skill-authored text, a
populated gaps file, every dossier quotation traceable to `findings.json`, and the
disclaimer present. Quotations are exempt from the ban lists — a source may say anything,
and quoting it is reporting, not asserting.

A run that fails either script does not ship.

## What it will not do

Tell you whether to invest, whether the team is strong, whether the valuation is fair, or
whether anything is a red flag. It offers to find more sources instead.

This is desk research from public sources at one moment in time. It is not legal due
diligence, not an audit, not a background check, and not advice.
