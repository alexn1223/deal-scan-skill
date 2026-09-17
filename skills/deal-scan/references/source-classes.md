# Source classes

Every source record carries exactly one class. The class is assigned from the domain and
the relationship, not from how convincing the content is — it is a statement about
*provenance*, never about credibility.

| Class | Assigned when | What it proves |
|---|---|---|
| `registry` | A government or official body publishes it | That body recorded it |
| `primary-self` | The target's own domain, docs, app listing or filing text | That the target **said** it |
| `primary-third` | A counterparty's own domain — an investor, customer, partner, accelerator, regulator | That the counterparty said it about the target |
| `press` | A publication with a masthead | That a publication reported it |
| `aggregator` | A third-party database compiled it | That the database holds it |
| `social` | A profile page on a social or code platform | That the profile asserts it |
| `archive` | A capture service or certificate transparency log | That the content or certificate existed at a timestamp |

## The two that get confused

**`primary-self` is not evidence of the fact, only of the claim.** A company's about page
saying "a team of 40" establishes that the page says 40. Render it so a reader skimming
cannot mistake the claim for the number.

**`primary-third` is the strongest class available without a registry**, because the
counterparty had no obligation to say it. An investor's portfolio page listing the
company, a customer's case study naming them, an accelerator's batch directory — each is
a second party independently confirming. Seek these deliberately; they are what turns a
one-sided claim into a finding.

## Pairing

A claim with one source is a lookup. A claim with two sources of different classes is a
finding. When the two agree, say so and show both. When they disagree, show both and stop
— `findings.json` holds several sources per claim precisely so that disagreement survives
into the output instead of being resolved away.
