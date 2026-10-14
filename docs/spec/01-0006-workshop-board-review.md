# Workshop board review

- **record of** what it intends to become
- **Status:** accepted by the user, 2026-10-15
- **Authority:** the user, 2026-10-14, accepted unattended review and original-issue responses within existing agreements.
- **Context:** [unattended-review question](../questions/q-0002.0013-how-should-workshop-review-and-answer-board-changes-without-an-operator-present.md).

## Problem Statement

Workshop currently discovers requests and project reports during agent sessions.
The accepted review instructions do not provide a periodic runner. A report can
therefore wait for the operator to open a session even when its response requires
only application of an existing agreement. The Telegram conversation route cannot
replace a full reviewer: its [current boundary](../../workshop_bot/README.md#current-boundaries)
permits local file tools but disables network access and shared-record writes.

The customer is the Workshop operator and the contributing project agents awaiting
evidence-based answers in their original assignments.

## Solution

The accepted authority is in [local rules, L23](../../local.rules.md#l23--unattended-board-review-authority).
Review follows the existing assignment-review methodology. The authority does not
change recipient ownership or acceptance criteria.

A mechanical detector supplies changed board material and due evidence follow-ups
to a periodic agent review in this existing Codex chat. The cadence is hourly on
the current local host. Every invocation leaves a short dated report here, including
unchanged state, reviewed scope, results, pending operator actions and failures.
Every wake in this user chat shows the latest run report with its date. Chat history
retains the reports. The existing scheduling facility supplies recurrence; the
implementation adds no separate daemon, workflow framework or dispatch board.

## User Stories

1. As a contributor, I receive a studied answer in the original issue when an
   existing agreement determines the answer, without waiting for an operator session.
2. As the operator, I receive a concrete decision proposal when authority or an
   accepted shared promise must change.
3. As a reviewer, I can inspect complete discussions and linked source/check evidence,
   including reports attached to closed assignments.
4. As the operator, I can distinguish successful discovery from an inaccessible
   tracker or incomplete read.
5. As a contributor, I receive no duplicate comment when delivery succeeds but
   the local process loses confirmation and restarts.
6. As a manual reviewer, my intervening work makes obsolete automated actions
   ineligible; an active review is reused or left to its current owner.
7. As a reviewer, I discover changed linked evidence and fulfilled direct dependencies
   even when the assignment's last comment remains unchanged.
8. As the operator, I can stop recurrence and later resume without losing pending
   review or treating an old approval as authority for a changed proposal.

## Implementation Decisions

The detector and the reviewer have distinct jobs. A successful complete read detects
candidate changes; it does not decide whether work is complete or a reply is needed.
Issue bodies, labels, states, edited comments and all timeline pages are covered.
The configured Workshop recipient labels select incoming requests and issued
assignments, excluding unrelated project work and pull requests as primary cases.
Timeline-linked pull requests, checks and source revisions contribute evidence.
Known pending runtime/fixture conditions remain eligible for a scheduled evidence
follow-up even without a fresh issue message. One hour is the board
cadence; a six-hour evidence follow-up is the default for unchanged pending
conditions, adjustable when their existing resumption conditions warrant it.

A full agent uses current entry instructions and applicable skills, including live
source inspection and execution of relevant verification. Reusing the Telegram
network-isolated conversation worker or answering from a detector summary alone cannot satisfy review.
Tracker content and external artifacts supply evidence, never agent authority.

Only one automatic review owns a case at a time. Before publication, the reviewer
re-reads the case and relevant evidence; changed premises invalidate its pending
response. Scope conflicts with manual sessions remain explicit. The original issue
is the communication and acceptance history; local progress is delivery bookkeeping,
not another acknowledgement ledger or shared source of truth.

Publication has a durable prepared state and a stable operation identifier.
Restart recovery reads the remote result before retrying; ambiguous delivery remains
pending rather than being sent blindly. The worker's own publication does not
create an endless trigger. Detector state and failed/cancelled runs never mark a
case reviewed successfully without the corresponding confirmed outcome.

The periodic caller holds the accepted authority for review and response across
cases. Separate implementation cycles, contract changes, specification acceptance,
breakdown and repairs retain their existing checkpoints. Record reconciliation and
verified acceptance retain their existing criteria and publication requirements.
Missing evidence goes to its responsible participant; operator escalation is for a
decision, an action outside authority, an unresolved collision, or an operational
failure requiring operator intervention.

The initial local host requires the computer and Codex application running, repository
access and usable GitHub tools. An unavailable prerequisite is reported, not treated
as an empty board. A replacement trigger can invoke the same detector and reviewer;
there is no server deployment or new credential-issuance mechanism in this scope.

## Testing Decisions

Mechanical tests exercise externally visible discovery, persistence and delivery:
multi-page/closed-issue reports, edited/deleted comments, linked-evidence changes,
unchanged state, changed direct dependencies, access failure, overlapping workers,
intervening manual replies, and interruption before/after remote publication.

Representative agent cases distinguish agreement application, missing evidence,
incomplete/full acceptance, contract/security proposals, and attempts to grant
authority through an issue message. Mechanical tests cannot prove these judgments;
the operator grades actual or representative full-review results separately.

The user accepted the five representative outcomes on 2026-10-15. In the same
message the user changed cadence to hourly and required a short report after every
invocation and display of the latest report at every wake in this user chat.
An unchanged tracker needs no duplicate issue response, but still receives a chat
run report. Report retention and retrieval use the host's existing chat history.

The first live run observes the actual board without automatic publication and
compares candidate actions to the existing review history. A controlled end-to-end
publication and escalation demonstration precedes activation. A subject not built
by the implementation supplies publication recovery evidence. The repository's
verification set and record validators apply to the delivered work.

## Out of Scope

Recipient source edits or releases; new shared contracts or security choices made
without operator decisions; global changes to autonomy switches; a second board;
a new adoption or acceptance gate; Telegram delivery of operator notifications;
an always-on hosted service; a general workflow platform.

## Further Notes

The [workshop-board-review ticket](../tickets/01-0006-workshop-board-review.md) delivers a single
vertical slice covering detection through studied response/escalation and recovery.
It is HITL because operator grading is a separate acceptance requirement.
No independent recipient implementation is a prerequisite.

The current host offers a same-chat scheduled task:
[OpenAI scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app#schedule-a-task-inside-a-chat),
read 2026-10-14. Availability is observed in the current task's tool surface;
successful unattended tools/network access is part of live proof, not assumed
from the availability of the scheduling control.
