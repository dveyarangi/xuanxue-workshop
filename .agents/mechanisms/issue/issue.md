# issue — complete compatible recipient assignments

- **instruction** `.agents/skills/issue/SKILL.md`
- **state** installed

## How it works

Issuing derives specialized recipient work from an agreed outcome, immutable
contract, ownership and scoped observations. It owns drafting, recipient/set review,
current-body maintenance, publication and readback. The coordinator supplies the
quality and shared-shape criteria; the configured collaboration format owns the
recipient exchange. An independently invoked issue skill receives those same rules.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| creating or revising an addressed assignment | `.agents/skills/issue/SKILL.md` |  |
| checking independent recipient understanding | `.agents/skills/issue/SKILL.md` |  |
| publishing and recovering partial publication | `.agents/skills/issue/SKILL.md` |  |
| handling resulting reports | | elsewhere — `.agents/skills/review-assignments/SKILL.md` — review-assignments owns this stage |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction | `.agents/skills/issue/SKILL.md` |
| declaration | `.agents/mechanisms/issue/issue.md` |
| authored shared rules | `.agents/mechanisms/issue/issue.rules.md` |


Retraction uses the shared installer before removing owned parts. Reuse by other
mechanisms is an explicit dependency; replacing ownership preserves those readers.

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| rule installer | `.agents/scripts/gw/inject_rules.py` | mechanism-shape |
| declaration checker | `.agents/scripts/gw/mechanisms.py` | mechanism-shape |
| outcome decomposition | `.agents/skills/ticket/SKILL.md` | ticket |
| project context and authority | `local.rules.md` | local |
| shared validation | `.agents/skills/coordinate/VALIDATION.md` | coordinate |

## What it produces, and who reads it

Prepared and published issue bodies are read by each recipient and its operator.
Drafts are local review artifacts; published issues own addressed work. The existing
pass records pending publication and successful issue identities. No per-recipient
local ticket or duplicate contract definition is created.

## Not yet at the shape

Mechanical checks establish declaration, binding and reference integrity, not
semantic correctness of observations, agreements or assignments. Explicit evidence
limits and independent output grading bound those conclusions.

## What retires this

Retire when its responsibility is removed or an accepted replacement assumes its
outputs and readers. Retract its installed rules and update dependents first.

## What would show it working, graded by someone who did not build it

An independent recipient reconstructs obligations from its brief and usable
authorities without author explanation. Grade mismatched parameters, missing
guarantees, shared omission, stale evidence and unreachable references. A factual
edit needs no extra ticket. A partially successful publication must preserve
existing identities and resume the missing work without claiming set completion.

The declaration and installation checkers must reject missing instructions and
missing or changed installed rules, and accept restored fixtures. Maintenance uses
the coordinator's shared binding without an additional per-stage report.
