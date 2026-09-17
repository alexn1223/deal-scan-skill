# Ban list

Two lists, two scopes. `scripts/validate_output.py` parses this file mechanically: it reads the two fenced code blocks below, in order, as List A and List B. Each non-empty, non-`#` line inside a block is one entry. An entry containing a space is matched as a case-insensitive phrase (whitespace runs collapsed to one space, both sides); an entry with no space is matched as a whole word (`\b<entry>\b`, case-insensitive).

Both lists apply to **skill-authored text only** — every byte of `dossier.md` and `gaps.md` except the spans marked as verbatim quotes and except the disclaimer paragraph. A quoted source may contain any word at all; that is the point of quoting it. A press headline containing "fraud" is quotable. The skill writing "fraud" in its own voice is not.

**List A — verdict vocabulary.** Characterizations of a company, a person, a market or a number. This skill characterizes nothing.

```
good
bad
strong
weak
solid
credible
legitimate
suspicious
concerning
questionable
promising
attractive
unattractive
impressive
disappointing
risky
safe
proven
unproven
red flag
green flag
green light
warning sign
scam
fraudulent
shady
trustworthy
untrustworthy
overvalued
undervalued
fair value
reasonable
excessive
should
recommend
recommended
advise
we suggest
worth a look
worth taking
pass on
avoid
invest
compelling
thin
robust
healthy
unhealthy
mature
immature
crowded
underserved
winner
loser
leader
laggard
best in class
market leading
major
dominant
dominates
significant
largest
biggest
well-funded
key player
major player
top player
household name
```

Size words sit in List A for the same reason as the verdict words. "The largest player in
the category" is an assertion no source made; "raised $340M, per Crunchbase" is a fact
with a link. Competitor size is always a cited number or a quoted market-share figure with
the firm that published it named — never an adjective.

**List B — smuggled-inference markers.** Hedges, framings and emphasis that carry a judgment without naming one. "Only three employees" is a verdict wearing a number's clothes; "three employees" is a fact. These are the ways characterization re-enters a document that has banned the obvious words.

```
appears to
appears that
seems to
seems that
suggests
suggesting
indicates
indicating
implies
implying
raises questions
raises concerns
worth noting
notably
interestingly
surprisingly
strikingly
tellingly
unsurprisingly
however
despite
although
merely
simply
just
only
as few as
as little as
no more than
fails to
failed to
neglects to
omits
lacks
missing
absent any
one would expect
typically
usually
normally
standard
market standard
comparable
in line with
out of line
above average
below average
outlier
```
