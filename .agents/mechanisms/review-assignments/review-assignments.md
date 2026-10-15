# review-assignments — answered cross-project work with evidenced acceptance

- **instruction** `.agents/skills/review-assignments/SKILL.md`
- **state** installed
- **record of** what must always hold

## How it works

The instruction discovers issued assignments and incoming requests at session
entry and handles current reports under the coordinating project's contract.
The project supplies tracker, responsibility, context, review obligations and
local review authority through local rules. A standing authorization can cover
periodic review; changing its activation does not change the shared responsibility
or acceptance contract. Relevant findings return to the existing coordination
pass at the affected stage; an in-progress review is reused rather than restarted.
The original issue conversation holds review history and acceptance evidence.
Discovery follows timeline references to reports and artifacts, including reports
held in other repositories. Direct comments are only one evidence surface.
Dependency review tests necessity as well as fulfillment against current source,
checks, runtime and operator evidence. Changed facts affect dependent assignments
even when their own conversations have not changed. The shared issue format owns
activity conditions; local review obligations bind reassessment and original-issue
correction to evidence handling. Document claims and acknowledgements describe
decisions and reviews but do not establish operational readiness.

Periodic activation uses mechanical change detection, local review leases and durable publication
recovery. The caller supplies a full reviewer; local snapshots and processing positions never
replace the original issue or become acceptance evidence. The periodic procedure owns the
local-progress record shape; the command's check validates its mechanical structure.
The project supplies reporting cadence, destination and reader bindings through local rules.
The report instruction owns the shared snapshot's format and publication; the validator
checks shape and rejects stale replacements. Session recovery and conversation readers
consume its dated facts without another acknowledgement ledger. A local external controller
runs discovery before invoking a standalone reviewer, so quiet runs use no model.
Scoped host capabilities retain authentication at the host: writes remain bound to selected
issues and the existing lease/publication checks; evidence reads stay within configured repositories.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| reviewing cross-project work after session recovery | `.agents/skills/review-assignments/SKILL.md` | |
| routing a blocker or changed obligation back into coordination | `.agents/skills/coordinate/SKILL.md` | |
| handling a project report or incoming request | `.agents/skills/review-assignments/SKILL.md` | |
| applying locally delegated authority during a periodic review | `.agents/skills/review-assignments/SKILL.md` | |
| detecting changes, claiming review and recovering publication | `.agents/skills/review-assignments/PERIODIC.md` | |
| maintaining the shared review snapshot | `.agents/skills/review-assignments/REPORT.md` | |
| reading reports and artifacts linked through an issue's timeline | `.agents/skills/review-assignments/SKILL.md` | |
| reassessing dependency necessity and fulfillment from observed conditions | `.agents/skills/review-assignments/SKILL.md` | |
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
| periodic procedure and progress format | `.agents/skills/review-assignments/PERIODIC.md` |
| mechanical discovery and delivery | `.agents/scripts/gw/board.py` |
| behavioral verification | `tests/test_board.py` |
| controlled HTTP demonstration | `tests/live_board_proof.py` |
| shared report instruction and format | `.agents/skills/review-assignments/REPORT.md` |
| shared report validator and writer | `.agents/scripts/gw/board_report.py` |
| detector-first controller | `.agents/scripts/gw/board_run.py` |
| Windows user task adapter | `.agents/scripts/gw/board_task.ps1` |
| controller and report verification | `tests/test_board_run.py` |
| scoped authenticated host capabilities | `.agents/scripts/gw/board_tools.py` |
| capability boundary verification | `tests/test_board_tools.py` |

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
The mechanism emits no independent acknowledgement ledger or index; its review outputs
use the configured tracker and the project's existing records and formats. Periodic execution
also retains local snapshots and processing/delivery positions, read by the reviewer on
resumption and the operator during recovery; these are working state, not another acceptance home.
The configured shared report is a current snapshot under REPORT.md's format, validated
by board_report.py. It links original outcomes and unresolved matters for the operator,
session recovery and configured conversation readers. It does not replace those records.

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
The operator grades a case where a settled accessible contract and operator
authority permit implementation while an installation acknowledgement is absent:
review removes the administrative hold from the original issue. A case without
a reachable conforming provider still cannot complete actual integration proof.
Changed runtime or operator evidence triggers reassessment even when the last
issue message is the coordinator's. A proposed shared promise change still returns
to alignment. Unchanged evidence produces no duplicate response.
The structural checks reject a missing instruction or a missing or altered
installed context or entry binding. These checks do not grade semantic decisions.
