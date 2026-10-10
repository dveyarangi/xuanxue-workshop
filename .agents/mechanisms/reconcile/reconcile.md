# reconcile — dispositions preserving shared obligations

- **instruction** `.agents/skills/reconcile/SKILL.md`
- **state** installed
- **kind** what must always hold

## How it works

Reconciliation compares observed project behavior and participant interpretations
with governing agreements. It owns dispositions and the remaining shared delta;
it does not collect all evidence again or publish assignments itself.
The coordinator owns overall routing and validation, including contract-shape
criteria. Project owners retain implementation and shared decisions retain their
accepted authority.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| comparing evidence with accepted obligations | `.agents/skills/reconcile/SKILL.md` |  |
| resolving an unresolved shared decision | | elsewhere — `.agents/skills/align/SKILL.md` — align owns this stage |
| collecting missing evidence | | elsewhere — `.agents/skills/analyse/SKILL.md` — analyse owns this stage |
| preparing owner assignments from dispositions | | elsewhere — `.agents/skills/issue/SKILL.md` — issue owns this stage |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction | `.agents/skills/reconcile/SKILL.md` |
| declaration | `.agents/mechanisms/reconcile/reconcile.md` |
| authored shared rules | `.agents/mechanisms/reconcile/reconcile.rules.md` |
| reference | `.agents/skills/reconcile/CONTRACT-SHAPE.md` |

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

Comparison findings and dispositions update the configured existing work record.
Accepted decisions update their owning agreements; remaining actions feed issuing
or approved ticket decomposition. No external issue is required for no-action,
factual correction or explicitly deferred work. No new record type is introduced.

## Not yet at the shape

Mechanical checks establish declaration, binding and reference integrity, not
semantic correctness of observations, agreements or assignments. Explicit evidence
limits and independent output grading bound those conclusions.

## What retires this

Retire when its responsibility is removed or an accepted replacement assumes its
outputs and readers. Retract its installed rules and update dependents first.

## What would show it working, graded by someone who did not build it

Grade an unchanged obligation, factual drift, implementation correction under an
unchanged contract, missing evidence, unresolved choice, accepted migration and
deferred work. A code difference must not redefine the accepted promise. A resumed
pass must account for completed work before deriving remaining actions.

The declaration and installation checkers must reject missing instructions and
missing or changed installed rules, and accept restored fixtures. Maintenance uses
the coordinator's shared binding without an additional per-stage report.

## Accepted separation requirements — 2026-10-06

The accepted separation, shared validation ownership and proportional process are
implemented by [coordinate](../coordinate/coordinate.md). The old contract-shape
path remains a compatibility link; the canonical criteria have one coordinator home.
