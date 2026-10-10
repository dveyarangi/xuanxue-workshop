# review-assignments — answered cross-project work with evidenced acceptance

- **instruction** `.agents/skills/review-assignments/SKILL.md`
- **state** installed

## How it works

The instruction discovers issued assignments and incoming requests at session
entry and handles current reports under the coordinating project's contract.
The project supplies tracker, responsibility, context and review obligations
through local rules. Relevant findings return to the existing coordination
pass at the affected stage; an in-progress review is reused rather than restarted.
The original issue conversation holds review history and acceptance evidence.
Discovery follows timeline references to reports and artifacts, including reports
held in other repositories. Direct comments are only one evidence surface.
Changed prerequisite evidence also affects dependent assignments, even when
their own conversations have not changed. The shared issue format owns dependency
conditions; local review obligations bind reassessment to evidence handling.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| reviewing cross-project work after session recovery | `.agents/skills/review-assignments/SKILL.md` | |
| routing a blocker or changed obligation back into coordination | `.agents/skills/coordinate/SKILL.md` | |
| handling a project report or incoming request | `.agents/skills/review-assignments/SKILL.md` | |
| reading reports and artifacts linked through an issue's timeline | `.agents/skills/review-assignments/SKILL.md` | |
| reassessing dependent assignments after prerequisite evidence changes | `.agents/skills/review-assignments/SKILL.md` | |
| reviewing relevant discussions when reconciliation begins or resumes | `.agents/skills/review-assignments/SKILL.md` | |
| supplying project context and entry invocation | `.agents/skills/mechanism/SKILL.md` | |
| installing or retracting the bindings | `.agents/scripts/gw/inject_rules.py` | |
| checking the declaration and installed bindings | `.agents/scripts/gw/mechanisms.py` | |
| rechecking instruction and entry agreement | `.agents/skills/maintain/SKILL.md` | |
| grading review decisions against real or representative evidence | — | unowned by design — the operator grades the observed decisions against the project contract |

## Install adds, uninstall removes

| part | where |
|---|---|
| review instruction | `.agents/skills/review-assignments/SKILL.md` |
| declaration | `.agents/mechanisms/review-assignments/review-assignments.md` |
| authored shared rules | `.agents/mechanisms/review-assignments/review-assignments.rules.md` |

Retraction removes the review-entry and maintenance bindings through the shared installer. Project
entry and context bindings are locally owned and are retracted at their source
when this instruction is removed.

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| entry and shared review obligations | `local.rules.md` | local |
| instruction delivery at entry | `AGENTS.md` | harness |
| boundary comparison | `.agents/skills/reconcile/SKILL.md` | reconcile |
| shared validation and loop routing | `.agents/skills/coordinate/SKILL.md` | coordinate |
| declaration checker | `.agents/scripts/gw/mechanisms.py` | mechanism-shape |
| rule installer and checker | `.agents/scripts/gw/inject_rules.py` | mechanism-shape |

## What it produces, and who reads it

The responsible project agent and operator read responses and acceptance in the
original issue. The coordinating operator reads the updated state and pending
decisions. Reconciliation reads returned project evidence and dispositions.
The mechanism emits no independent acknowledgement ledger or index; its outputs
use the configured tracker and the project's existing records and formats.

## Not yet at the shape

Declaration and binding checks cannot establish that a host actually invokes the
instruction or that a model judged evidence correctly. Fresh-session observation
and operator grading provide those distinct forms of evidence.

## What retires this

Retire it when the coordinating project no longer reviews cross-project work or
an accepted replacement assumes discovery, response and acceptance responsibility.

## What would show it working, graded by someone who did not build it

The operator observes a fresh ordinary session recovering its state before invoking
review and discovering current addressed work. The operator also grades obstacle,
incomplete-result, complete-result and already-closed-result cases against the
project contract. An unchanged coordinating-project answer produces no duplicate
response. Missing evidence produces an explicit pending action, not false acceptance.
An inaccessible tracker is reported as unavailable, not as an empty inbox.
An issue with no direct comments but a linked pull-request report or referenced
commit must produce an artifact-based review. An incidental mention must not
produce acceptance; an inaccessible reference must remain explicitly pending.
Acceptance follows required record reconciliation and references its result.
For prerequisite acceptance, the operator checks that dependent work is
reassessed without an invented Ready approval. A closed unaccepted prerequisite
must remain unsatisfied; provider-dependent integration must remain blocked even
when client development is eligible. An unchanged prerequisite produces no
duplicate response.
The structural checks reject a missing instruction or a missing or altered
installed context or entry binding. These checks do not grade semantic decisions.
