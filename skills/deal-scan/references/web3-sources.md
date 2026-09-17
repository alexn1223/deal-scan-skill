# Web3 sources

The web3 branch runs at tier 0 with no API key. Every endpoint below was exercised
against a live contract; each is free and returns JSON.

## Chain data — Blockscout

Blockscout serves a public API with no key and no signup. Prefer it to Etherscan, whose
API requires a key.

    https://eth.blockscout.com/api/v2/addresses/{address}
    https://eth.blockscout.com/api/v2/smart-contracts/{address}
    https://eth.blockscout.com/api/v2/transactions/{tx_hash}

Other chains have their own Blockscout instances; a chain with none falls back to that
chain's own explorer, and if that is unreachable the whole web3 block is recorded as
`blocked`, never assumed.

## Protocol data — DefiLlama

    https://api.llama.fi/protocols
    https://api.llama.fi/protocol/{slug}

Carries TVL, chains, category, listing date, GitHub org and audit links. Class
`aggregator`.

**The `audits` field is about DefiLlama, not about the protocol.** `audits: 0` means
DefiLlama holds no audit link. It does not mean no audit exists, and writing it up that
way is a verdict manufactured out of a database's coverage gap. Record it as
`not-found` with DefiLlama named as the source searched.

## Code — GitHub

    https://api.github.com/orgs/{org}/repos
    https://api.github.com/repos/{org}/{repo}/contents

Unauthenticated and rate-limited to 60 requests an hour, which is ample for one scan.
Gives repository ages, push dates, star counts and licences.

## Three addresses, not one

"The deployer" is ambiguous and routinely reported wrong. A contract creation involves up
to three distinct addresses, and a scan records all of them separately:

| Field | What it is |
|---|---|
| the contract | The address being examined |
| `creator_address_hash` | What created it — **often another contract**, such as a CREATE2 factory |
| the creation transaction's `from` | The externally owned account that sent the transaction |

On a live example these were three different addresses, and the creator was itself an
unverified contract. Collapsing them into "deployed by X" states something no source
said. Report each under its own label, and where the creator is a contract, say so.

## Verified is not one thing

`is_verified` and `is_fully_verified` are separate fields and can disagree — a contract
can carry verified source that is a partial rather than an exact match. Record both, with
the compiler version and the `verified_at` timestamp. Writing "source verified" where the
explorer says partially verified overstates what the explorer said.

`proxy_type: null` together with an empty `implementations` array is the evidence that a
contract is not behind a proxy. Record the fields, not the conclusion.

## Audits

An audit is a named firm, a date, a scope and a linked report. Nothing else counts.

A search result whose title contains the word "audit" is not an audit. In testing, the
single audit-shaped result for a protocol was a paid educational package on a third-party
store, and its URL returned 404 when fetched. Had the scan trusted the search summary it
would have recorded an audit that does not exist.

Where no audit is found, the gap entry reads: searched, named sources, no report located
— which is not a statement that the code is unaudited.
