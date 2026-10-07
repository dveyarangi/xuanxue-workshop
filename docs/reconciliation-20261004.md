# Boundary reconciliation — 2026-10-04

## Public best-effort amendment — 2026-10-07

The user changed the [public pilot agreement](boundaries.md#accepted-first-schedule-connection):
return valid lessons, omit malformed individual records and log each omission at
error severity. The prior public contract is not yet used, so the same operation
is amended directly. No version, completeness header, envelope or client warning
state is added. The [public contract](contracts/public-lessons.md) owns exact
selection, output, empty-result, logging, whole-read-error and recovery cases.

The earlier pinned mapper counterexamples below remain evidence of invalid
emitted public data. The remedy now omits/logs those rows rather than failing
the whole read; operational database/class-read/code failures remain errors.
Old deployed healthy samples do not prove the amended handling. Cabinet's existing
HTTP-500 reporting path does not automatically see a handled omission in HTTP 200.
The contract requires its explicit error log without choosing or installing an
external collector. Cabinet's ADR-0053/0132 currently use Telegram and a developer
journal and reject Sentry; any collector change belongs to its own observability
decision, not this public response amendment.

Daychi's replacement assignment and Cabinet's superseding comment passed fresh
independent recipient reading against one fixed authority. The user authorized
scoped commit/push and original-issue updates on 2026-10-07. The
[Daychi assignment](https://github.com/dveyarangi/xuanxue-workshop/issues/6) and
[Cabinet amendment/review conversation](https://github.com/dveyarangi/xuanxue-workshop/issues/5)
carry the exact published contract and current recipient obligations.
Provider/client implementation,
Daychi installation acceptance and native proof remain separate outstanding work.
Dated sections below retain their original acceptance basis.

The [2026-10-06 maintenance report](maintenance-20261006.md) holds the latest
scope, boundary dispositions and resumption point. Dated sections below retain
their inspection and publication history; older pending/availability statements
are snapshots, not the current work queue. The
[migration question](questions/q-0002.0007-how-will-daychi-migrate-schedule-users-and-reminders-to-cabinet-while-retaining-its-content-backend.md#initial-usage-and-ongoing-synchronization--2026-10-04)
holds subsequent work-scope corrections; the boundary record holds accepted contracts.

## Cabinet assignment review — 2026-10-06

### Onboarding document maintenance — 2026-10-06

Scope: onboarding's access/source requirements and the references to its Cabinet
case history. The user identified that a reader joining a project gains nothing
from the installation issue's report/closure history in the onboarding contract.
Removed that history there; the case-specific accepted return-path disposition
now lives in this report, alongside its implementation evidence. Updated both
inbound references. Onboarding retains its general accepted requirements.
Application boundaries, installation acceptance and issue 5's provider defect
are unchanged. Existing comparison/evidence above remains the reconciliation
baseline; no new tracker action or shared decision is needed. No mechanism is
due; referenced targets and whitespace pass, and no source-link repair or Git
publication is included in this editorial pass.

### Direct reports and production verification — 2026-10-06

**Installation acceptance disposition:** Cabinet issue 1's retained installation
and reported discovery satisfy its result criteria and the prior user acceptance
of its evidence. Workshop readiness was its execution prerequisite; unfinished
coordinator readiness is not an additional criterion for this already-performed
installation result. No shared application boundary contract changed in the
installation contribution. Under the exchange agreement, acknowledgement can
confirm that fact using the pinned Cabinet/Workshop source evidence. This
supersedes the review response's unnecessary hold on readiness and record
publication for issue 1. Provider conformance in issue 5 and the coordinator's
own readiness/publication work remain distinct and incomplete.

Workshop posted [acceptance](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155),
closed issue 1 as completed and updated its status/evidence checklist. The
[dependency update](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011484164)
confirms that issue 5's installation prerequisite is satisfied. Provider
required-data correction remains its outstanding acceptance action. These
operations publish no Git commit and do not complete coordinator readiness.
Readback confirms the exact acceptance comment, completed closure, updated issue
body/checklist and the dependency message in issue 5. The latter remains open.

Continued the existing review after direct Cabinet reports appeared in
[cabinet-workshop-collaboration #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6009267281)
and [cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6009269862),
including its subsequent staging and production updates. Read current bodies,
all comments, complete timelines (6 events in issue 1, 8 in issue 5), linked
PR discussions, pinned artifacts and final-head checks. Daychi issues 2 and 6
still have no recipient reports in their complete timelines. Withdrawn issues
3 and 4 remain withdrawn; no new assignment or cycle was started.

| Boundary | Provider / consumer | Promise | Evidence / revision | Delta and consequence | Disposition |
|---|---|---|---|---|---|
| Collaboration installation and return | Workshop / Cabinet agent | Retained host instructions, discovery and original-issue report | Installation report; both retained files at Cabinet `fc2dee2`; source Workshop `e209d27`; PR 561 final 19 checks successful | Skill equals the source after removal of Installation, label replacement and provenance insertion; companion is byte-identical. Direct reporting now works in the reported session | Installation accepted and issue 1 closed; issue 5's prerequisite is satisfied. Source-link correction and coordinator readiness/publication remain separate work |
| Public provider deployment | Cabinet / public readers and native Daychi | Reachable agreed GET, protected student route retained | Deployment reports; release workflow 37424107719; full `release`/tag SHA; anonymous probes at 07:09 UTC | Both staging and production now serve public windows at `fc2dee2`; prior production 404 is superseded | Update current environment/migration records and Daychi's brief; production deployment is verified, provider conformance remains incomplete |
| Required response data | Cabinet / public readers | Malformed required source data fails the whole request with `500 internal_error` | Pinned mapper, lean service/join, route decorator and error filter; validation e2e; isolated projection reproduction | Missing duration disappears from serialized DTO; an invalid class format is copied unchanged. Missing-class e2e does not cover these cases | Request Cabinet runtime enforcement and HTTP tests for invalid lesson/class data and mixed valid/invalid selections in existing issue 5 |

The projection reproduction uses the pinned mapper body with its TypeScript
annotation removed and the same Luxon UTC conversion for valid dates. It proves
the two projection/serialization counterexamples, not a live corrupt-database
HTTP result. No application data or sibling source was changed. Evidence:
[counterexample](../.local/reconciliation-20261006/mapper-counterexample.mjs),
[report/CI snapshot](../.local/reconciliation-20261006/report-review-evidence.json)
and [live probes](../.local/reconciliation-20261006/report-review-live-probes.json).

The source companion link remains broken after installation, a Workshop-owned
follow-up already accepted as outside Cabinet's copying responsibility. The
current issue 1 body does contain the prescribed fenced BOUNDARY_SUMMARY, so the
report's plain-prose discrepancy is not reproduced against that body. The
reported source-revision placement matches the accepted onboarding requirement.
No source-rule amendment or installation repair is included in this review.

Cabinet's installation prerequisite is satisfied by the acceptance linked above.
Daychi development still needs accepted issue 2 installation, and actual
integration needs provider conformance and controlled fixture execution.
Deployment alone satisfies neither remaining dependency. The current pass
resumes at Cabinet's required-data repair, native proof and coordinator
publication. Readiness stays first in the local queue; gateway and content
consolidation remain deferred.

Review responses were posted in
[issue 1](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011345915)
and [issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011347777).
Issue 6's production row now identifies the verified `fc2dee2` deployment and
retains the unchanged contract and execution dependencies. Readback matches
both prepared comments and the consumer body. The subsequent acceptance above
closed issue 1; issues 5 and 6 remain open with their existing recipient labels.

The mapper reproduction passes its two assertions. Question-store diagnostics
and whitespace checks pass; the two known similarity suggestions remain.
Ticket checking finds no issue in the affected connection/readiness records;
its full scan retains the unchanged horizon record's missing Answers and
retired Open issues diagnostics. No unrelated repair is included.
Straw-dog listing has no diagnostics or due entries.

### Environment and fixture follow-up — 2026-10-06

Scope: existing Cabinet public-schedule environments and staff fixture controls,
their effect on the native Daychi assignment and this coordinating outcome.
The user supplied the hosts and asked Workshop to inspect sources itself and
update the ticket, Daychi issue and relevant architecture. Workshop read pinned
Cabinet runbook, staff frontend, controller and service sources, checked both
branch heads, and probed public HTTPS endpoints without credentials or writes.
The [current-system environment evidence](current-system.md#cabinet-public-schedule-environments--checked-2026-10-06)
owns the addresses, probe results, runtime revisions and derived fixture controls.

| Boundary | Provider / consumer | Promise | Evidence / revision | Delta and consequence | Disposition |
|---|---|---|---|---|---|
| Public schedule origin | Cabinet / native Daychi | Reachable configured origin serving the agreed read | Staging health and public reads, runtime `fc2dee2`; pinned Cabinet runbook | The existing staging provider is reachable from Workshop; production remains on older `27f3e7b` and returns 404 for the route | Correct records and Daychi issue to use staging; actual native-device evidence remains required |
| Controlled lesson changes | Cabinet operator / native Daychi | Native refresh demonstrates stable moves and cancellation | Existing planning editor and authenticated lesson operations at `fc2dee2` | Fixture functionality is already implemented; a broad request to explain/create it would repeat inspectable work | Supply source-derived controls; coordinate only operator access, concrete fixtures and execution |
| Malformed source data | Cabinet / public readers | Entire selected result or `500 internal_error` | Existing public mapper finding at `fc2dee2` | The live sample is valid but does not establish behavior for corrupt required fields | Keep the validation correction and HTTP-level evidence request in Cabinet assignment 5 |

This supersedes the missing-origin/setup and missing-fixture-instructions
assessment below. No native client proof, authenticated fixture mutation or
production promotion was performed. Wire definitions, implementation ownership,
execution dependencies and acceptance criteria remain fixed. The pass resumes
at provider validation correction and actual native integration proof, with
record publication and formal acknowledgements still pending.

Publication result: [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
was updated in place and read back exactly, retaining `project:daychi`, open state,
the immutable `e209d27` contract and all execution dependencies. The coordinating
ticket and architecture point to the environment evidence. Cabinet's narrower
follow-up is prepared locally at
[cabinet-public-lessons-followup.md](../.local/reconciliation-20261006/cabinet-public-lessons-followup.md);
it has not been posted. No issue closure, sibling edit, live fixture mutation,
commit or push occurred.

Subsequent clarification in the same session: the user requested recording the
production address as a promise. The
[accepted production target](boundaries.md#accepted-first-schedule-connection)
now has its architectural home; Daychi issue 6 states it explicitly alongside
the observed 404 and was read back exactly. Staging acceptance and current
execution dependencies are preserved. This does not certify production deployment
or add a deadline or production-release prerequisite to the pilot.

Editorial maintenance correction: the user identified investigation history in
Daychi issue 6. Its environment/test section was rewritten as a current brief:
correct origins, production target, dated availability, fixture controls and
remaining proof. The typo/DNS story, conversational attributions and commentary
about what Cabinet need not repeat were removed. Readback matched exactly;
contract, dependencies, acceptance criteria, open state and label were preserved.
The coordinating ticket was similarly cleaned; current-system and boundary
records retain the operative facts. This pass report owns the correction history.

Checks for this follow-up: maintenance dueness reports no due project mechanisms;
mechanism declarations, installed rule blocks, question-store diagnostics,
straw-dog diagnostics and whitespace checks pass. The connection ticket's format
passes. The full ticket scan retains two diagnostics in the unchanged horizon
[daychi-backend-capabilities-in-cabinet](tickets/01-0010-daychi-backend-capabilities-in-cabinet.md):
no Answers bullet and a retired Open issues section. That record is outside this
environment/assignment correction; no unrelated repair or mechanism amendment
was performed. The question store also retains its two existing similarity
findings; neither is a diagnostic introduced by this pass.

The user requested full mention discovery and another review of both Cabinet
assignments. Bodies, direct comments, complete timelines, linked PR discussions,
diffs, commits and CI were read. Both issues remain open with no direct comments;
both have inspectable recipient reports through their timeline references.
References to withdrawn issue 3 and paired issue 6 establish context and
dependencies, not completed work. No new consumer implementation report appears
in issue 6's timeline. Source and deployment remain separate claims.

### cabinet-workshop-collaboration

[cabinet-workshop-collaboration #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
links [Cabinet PR 561](https://github.com/gregoryKot/xuanxue-cabinet/pull/561) and
merge commit [`130fb09`](https://github.com/gregoryKot/xuanxue-cabinet/commit/130fb09bc9b3619f41649bbad5e94673bc8e94b8).
The PR is merged; all 19 checks on final head `6121838` succeeded. Earlier runner
delays reported in its discussion are superseded by that successful run.

The retained artifacts contain both collaboration files, source revision
`e209d27239391be3af2be71b898c79f453851c01`, the `project:cabinet` adaptation,
installation-section removal, CLAUDE invocation/summary and the Git ignore
exception. The report describes a separate agent discovering the source, label,
issues and boundary conditions. This is inspectable code and a reported discovery
result; Workshop did not observe that host's session directly.

The [installed companion](https://github.com/gregoryKot/xuanxue-cabinet/blob/130fb09bc9b3619f41649bbad5e94673bc8e94b8/.claude/skills/collaborate/workshop-issue-format.md)
still links `../../.agents/skills/reconcile/CONTRACT-SHAPE.md`. From the installed
directory this resolves under `.claude/.agents/`, where no appendix is installed.
The defect is in Workshop's published source, not a Cabinet copying discrepancy.
Remaining action: Workshop repairs and publishes the portable source link, then
Cabinet supplies corresponding installation evidence under its own operator.
Workshop readiness and acceptance acknowledgement are also outstanding.
Durable files are now confirmed; the earlier temporary/unmerged state is obsolete.

### cabinet-public-lessons

[cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5)
links [Cabinet PR 562](https://github.com/gregoryKot/xuanxue-cabinet/pull/562) and
merge commit [`fc2dee2`](https://github.com/gregoryKot/xuanxue-cabinet/commit/fc2dee20d64d91122a58e57709c378c5fc91bae7),
which matches directly read remote `main`. Its final head `4a8b795` has 19 successful
checks. Initial head `38542eb` failed the coverage ratchet, 99.19% → 98.9%; the
later commit added service/controller/query tests and resolved that failure.
The PR checklist and original test count lag those final artifacts.

The additive unauthenticated route, public allowlist, count/window selection,
unlimited bounded window, cancellation/move behavior and strict query validation
are inspectable. Tests include the common six-row fixture, 201-row window,
337-hour offset change, session-invariant public projection, missing-class 500
and protected student regression. Cabinet's instruction summary identifies the
new route; admission/authentication/reminder migration remains separate.

**Contract finding:** the
[public mapper](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/public-lesson.mapper.ts)
copies `durationMin`, class strings/enums, `topic` and `status` without validating
their required types/presence. The service reads lean rows; join/decryption does
not validate those values. `ApiRoute` supplies compile-time typing and metadata;
the app's ValidationPipe validates request inputs, not these response objects.
A selected stored row with valid IDs/date/class but missing `durationMin` reaches
the mapper unchanged: its undefined value disappears during JSON serialization.
The inspected path therefore permits malformed success instead of the contract's
whole-request `500 internal_error`. This is a source-derived counterexample,
not a live corrupt-database HTTP experiment. Current tests exercise a missing
class, but do not establish this broader required-data guarantee.

Remaining Cabinet evidence: runtime enforcement and corrupt-source HTTP cases
for required lesson/class data; reachable API origin, provider/runtime revision,
reproducible device/emulator setup and operator-controlled fixture changes.
A development provider suffices; production deployment is not required. Cabinet
owns its implementation and fixture operations; Daychi is the read-only consumer.
Tests alone do not establish the reachable provider or actual native integration.

### Cabinet return-path acceptance — 2026-10-06

Decision: the user, 2026-10-06, for
[cabinet-workshop-collaboration #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1).
Validated reports and retained artifacts linked from its timeline established
the factual return path through Cabinet PR 561. The user accepted that evidence
despite the recipient session's inability to comment directly in Workshop.
Direct reporting remained the agent/operator's follow-up; the inherited source
link defect remained Workshop's follow-up. This was a disposition for the observed
Cabinet case, not a change to future onboarding access requirements. Subsequent
direct reporting and completed installation acceptance are recorded in the
[latest review](#direct-reports-and-production-verification--2026-10-06).

### Disposition and continuation

Subsequent operator decision, 2026-10-06: the
[Cabinet return-path disposition](#cabinet-return-path-acceptance--2026-10-06)
accepts the installation evidence through the validated PR references. Direct
commenting is retained as operator/agent follow-up, not an acceptance blocker;
the Workshop-authored link defect is also Workshop-owned follow-up. This
supersedes the installation evidence hold in the preceding assessment. Formal
issue acknowledgement, publication and the remaining Workshop readiness work
have not occurred; provider issue 5 remains incomplete on its own evidence.

The following paragraph records the state before that decision:

Both reports are discovered and reviewed; neither assignment is accepted or
closed by Workshop. Issue 5's prerequisite still requires Workshop acceptance
of issue 1. The existing implementation is recorded without treating its merge
as satisfaction of that prerequisite. Provider conformity/environment and actual
Daychi proof remain incomplete under the existing
[cabinet-daychi-public-schedule-connection](tickets/01-0007-cabinet-daychi-public-schedule-connection.md).

The [review amendment evidence](mechanisms/review-assignments.evidence.md#timeline-discovery-and-cabinet-replay--2026-10-06)
records installed full-timeline discovery and its checks. This pass changed local
instructions and factual records only. No source portability repair, sibling
change, external reply, acceptance, dependency release, commit or push occurred.
Concrete follow-up above is prepared for the existing original issues; the
publication and communication checkpoints remain. Queue order is preserved.

## Continuation status — 2026-10-05

The [2026-10-06 Cabinet assignment review](#cabinet-assignment-review--2026-10-06)
supersedes this section's older Cabinet revision and no-report assessment.
Its linked PRs are now merged; Workshop acceptance and integration are still open.

Dependency clarification has reached the shared issue format and distributable
collaboration discovery instruction. Authored local review rule L14 now requires
reassessment of dependent assignments when prerequisite evidence changes and is
installed into review and reconciliation. The
[amendment evidence](mechanisms/review-assignments.evidence.md#dependency-reassessment-amendment--2026-10-05)
records passing binding, mechanism and full harness checks. These changes remain
local and unpublished; the existing publication resumption point is retained.

The pass is resumed below at comparison and resolution. The earlier pilot drafts
remain retired; the user confirmed that their retirement did not revoke the
already-agreed public schedule connection.
Completed collection is reused, with changed evidence and the candidate seam
rechecked. No readiness prerequisite has been released.

Current resumption point: the already-agreed public schedule definition and common
examples are consolidated in the maintained
[public lessons contract](contracts/public-lessons.md). The user's requested
[participant/reconciliation planning pass](../.local/reconciliation-20261005/participant-reconciliation-plan.md)
traces each recipient/operator's result, controlled data changes, reachable native
provider setup, original-issue evidence review and record publication before
acknowledgement. It corrects the review draft's unsupported blanket reapproval and
version-change approval gates; accepted API behavior and compatible-coexistence
autonomy remain fixed. A new vote on the already-agreed contract is not required.
The user approved the one-outcome breakdown and separately authorized its contract
commit and push on 2026-10-05. The
[cabinet-daychi-public-schedule-connection](tickets/01-0007-cabinet-daychi-public-schedule-connection.md)
is minted locally behind readiness. Commit
[`e209d27`](https://github.com/dveyarangi/xuanxue-workshop/commit/e209d27239391be3af2be71b898c79f453851c01)
publishes only the contract and accepted boundary scope. The addressed contributions
[cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5)
and [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
are published, with matching immutable contract references, recipient labels,
installation prerequisites and reciprocal links. Readback matches the prepared
bodies after normalizing GitHub CRLF. The remote contract blob matches the local
committed blob. Readiness/onboarding and actual integration evidence remain.
Literal examples and Cabinet's installed validation-library behavior were checked;
these are definition/source checks, not public-route or native runtime proof.
The first-stage goal remains evidence that both separately operated project agents
can receive addressed work and return evidence that Workshop reconciles; it does
not become completion of the entire application migration.

## Resumed comparison and resolution — 2026-10-05

**Scope:** Continue the existing first-stage boundary pass and specify its first
useful Cabinet–Daychi application connection. Readiness and recipient installation
retain their existing work records. No new four-outcome queue is proposed here.

**Stage:** First application pair published after approved breakdown and immutable
contract publication; recipient execution and evidence reconciliation remain.

**Resumption point:** Continue Workshop readiness in existing queue order, accept
recipient installation evidence in the original assignments, and review new
provider/client reports in application issues 5 and 6 as they arrive. The local
connection ticket stays incomplete until actual integration and record
reconciliation satisfy its criteria. No later application pair is authorized.

### Evidence and issue review snapshot — 2026-10-05

- Cabinet local and remote `main` remain
  `628314472aa2752ebb2bbe9ab75ac3dea9791719`. Local changes are `CLAUDE.md` and
  `.cursor/` from the reported collaboration dry run. The installed skill names
  `project:cabinet` and source `ba5e35f24e49ac2931f3af9382646c5cbd87e1e8`;
  its presence does not establish durable adoption or acceptance.
- Daychi's clean local checkout and readable remote `main` both remain
  `5f9ba442e04cd5dfa70527b9e670b491c491888c`. Repository access now succeeds;
  the earlier 404 is historical. Runtime and deployment remain unverified.
- Workshop remote `master` is now
  `e209d27239391be3af2be71b898c79f453851c01`. The local review skill and its
  after-recall and reconciliation bindings are installed; fresh-session review,
  independent grading and publication remain in
  [workshop-coordination-ready](tickets/01-0005-workshop-coordination-ready.md).
- All issue states were read. Installation issues
  [cabinet-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
  and [daychi-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/2)
  remain open and Planned. Contribution issues
  [cabinet-contract-contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/3)
  and [daychi-contract-contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/4)
  remain withdrawn and closed. The repository comment read returned no comments.
  There is no new report to accept, investigate or answer; no repeated message was
  posted. The Daychi assignment's dated access failure remains historical evidence,
  not a reason to commission another inventory.

### Boundary comparison snapshot — 2026-10-05

| Boundary | Provider / consumers | Documented promise | Evidence / revision | Delta and consequence | Disposition / issue |
|---|---|---|---|---|---|
| Public schedule | Cabinet / Daychi clients and Cabinet web | Public schedule omits Zoom; complete bounded date-window retrieval supports fourteen days; preserve Cabinet web count behavior. | Cabinet `62831447`: `shared/src/lessons.ts`, `my-lessons-routes.ts`; API `my-lessons.controller.ts`, `my-lessons.service.ts`, `my-lesson.mapper.ts`, `dto/list-my-lessons.dto.ts`, `auth/auth.guard.ts`; shared contract published at Workshop `e209d27`. | Student read still requires a cookie, defaults to ten items, has no window query or class ID, and emits Zoom fields. Opening that route without a safe response projection cannot satisfy the public contract. | Unimplemented target assigned in [cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5); execution waits for accepted Cabinet installation. |
| Cabinet schedule consumption | Cabinet / Daychi native client | Receive authoritative dated occurrences with stable identity and cancellations; eventual cutover preserves cached schedule and reminders after failed refresh. | Daychi `5f9ba44`: `schedule/load.ts`, `model.ts`, `use-schedule.ts`, app `_layout.tsx`; shared contract published at Workshop `e209d27`. | Decoder requires school URL and weekly-template metadata. Successful normal refresh writes the schedule cache and immediately reconciles OS reminders. Endpoint replacement is therefore broader than a display read. | Isolated pilot assigned in [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6); accepted Daychi installation precedes development, and Cabinet issue 5 supplies actual integration prerequisites. Ordinary-source cutover and shared reminder adaptation stay separate. |
| Credentials and content admission | Cabinet / Daychi clients and retained backend | Cabinet authority, web cookie/native bearer, narrow admission and installation-local sign-out are accepted. | Prior source comparison remains at unchanged commits; accepted intervening decisions are in the target record. | Final acquisition/lifecycle and admission schema remain open. An authentication-first connection must settle these additional dimensions and adapt existing protected content behavior. | Retain unresolved decisions; candidate has more dependencies than a public read. No implementation issue prepared. |
| Shared selections and reminder delivery | Cabinet / Cabinet web and Daychi clients | Shared one-off/recurring choices, independent offline edits, lead time and existing delivery channels. | Prior comparison at unchanged commits; Daychi normal refresh/reminder coupling rechecked. | Class-only Cabinet scope, local Daychi choices and clock/removal reconciliation require coordinated stateful changes. | Retain accepted obligations and unresolved synchronization work; do not include them in the first public display connection. |
| Source access | Project repositories / Workshop | Evidence must be inspectable at identified revisions. | Both remote commit reads now match local source. | Earlier Daychi remote-access uncertainty is resolved for Workshop's connected account. Recipient access and running configurations are still separate proof. | Current-system provenance refreshed; no recipient source-inventory request needed. |
| Workshop exchange and installed summaries | Workshop / both project agents | Original issues hold problems, results and acceptance; summaries distinguish observed and target boundaries. | Current issue bodies/comments; installed local review rules; Cabinet dry-run files. | No new reports or boundary implementation. Both issue summary blocks still match the evidenced connections. | Reuse installation issues, keep dependencies, no summary rewrite or acknowledgement. |

Paths are relative to each owning repository. Retained comparisons are not new
test executions. The reinspection establishes source behavior, not deployment.

### Agreed first outcome

**[cabinet-daychi-public-schedule-connection](tickets/01-0007-cabinet-daychi-public-schedule-connection.md) — Planned, HITL.** A native Daychi
read-only path displays actual Cabinet dated lessons for a complete fourteen-day
window without credentials or Zoom fields. A refresh reflects a reschedule or
cancellation. The path preserves the ordinary Daychi schedule, choices, cache and
OS reminders while proving a real provider/consumer connection. Presentation and
internal implementation remain project-owned.

Cabinet supplies the public contract and provider implementation while preserving
its existing web consumer. Daychi consumes the same fixed definition. Workshop
owns agreement, coordinated issue preparation, evidence review and reconciliation;
it does not implement either sibling. The complete contract and common conformance
cases precede issue preparation, with one accessible immutable reference for both.

Dependencies: Workshop readiness, each recipient's onboarding and a published
readable contract baseline govern execution. Fully specifying this
outcome can proceed while those prerequisites remain open. The result is complete
only with inspectable provider and native-consumer evidence and the reconciled
boundary record, not with publication of two issues.

First-stage scope covered: a concrete minimal connection of existing schedule
capabilities, plus the addressed-work and result-review exchange. This stage does
not require all account, reminder or service-retirement changes to accompany it.

#### Impact

One outcome crosses Cabinet's typed API/provider and Daychi's native reader, plus
Workshop's contract, assignment and acceptance records. Public response privacy,
window completeness and occurrence identity are shared obligations. Existing
Cabinet web behavior must be verified. The client path must demonstrate real
Cabinet data and updates without affecting ordinary reminder state.

#### Hidden edges

The current mapper includes Zoom; auth removal alone is insufficient. The current
count limit cannot imply fourteen-day completeness. The shared class join silently
omits orphaned lessons, so the complete-window contract must account for that
behavior. Daychi's decoder and correction adapter assume school-template data;
normal refresh mutates reminders. Route/projection, count/window and failure
agreements now constrain these changes. The complete contract review consolidates
their exact definitions and common evidence set for acceptance before assignments.
Source availability proves neither native connectivity nor deployment.

#### Leave alone

Accepted schedule authority and access, ordinary Daychi refresh/reminders, school
source cutover conditions, Cabinet web behavior, account/access decisions, shared
offline selection work, recipient implementation ownership, queue order and
retired drafts. Gateway and consolidation remain deferred. No background refresh,
native push or new sample-data product feature is included.

#### Recommendation

Continue with this agreed first connection's shared contract. It meets the accepted need
for a useful small connection with fewer state and credential dependencies than
authentication or reminders. Cost is inferred from inspected coupling, not measured
implementation effort. The user corrected the assistant's repeated scope question
on 2026-10-05: the connection was already agreed. The single-outcome breakdown is
now approved and minted, and its first application pair is published. The agreed
definition is immutable at the published contract revision; actual provider and
native evidence remain outstanding.

### Remaining publication and verification

Application issues 5 and 6 are published, and the approved two-file contract
commit is pushed. No sibling implementation, deployment or readiness release
was performed. Other Workshop rules, ticket and reconciliation records remain
local and uncommitted.
Updated source-access provenance is the only current-system fact changed in this
continuation. The first outcome's scope and API agreement are accepted. Its
breakdown and contract commit/push approvals have been exercised; recipient
execution still depends on acknowledged installation. The redundant
blanket contract-approval request was withdrawn. Current-system's
older broad contribution-confirmation wording is a documentation-drift candidate:
completed source collection should not be assigned again; specific runtime,
deployment and recipient evidence remains missing. Its wording repair is not
included in this continuation's evidence refresh.

Participant-pass checks: the maintained contract's response/interval/move/offset
examples and 37 local links across the contract, boundary, question and planning
artifacts pass. Existing Cabinet validation libraries reject duplicate scalar
arrays, unknown fields and empty limits under its source configuration. Live
issue states and all repository issue comments were rechecked: both installations
remain Planned, retired investigations remain withdrawn, and no new messages were
found. No application route or native conformance execution was claimed. This
pass changes local definitions/planning records, not sibling code or remote issues.

Verification for this continuation: harness reference, injector and shape gates
pass at `5871845`; seven mechanism declarations and 25 installed blocks across
seven rule sources pass without diagnostics or orphans. The question-store check
has no diagnostics and retains its two known similarity suggestions for distinct
migration/consolidation and credential/gateway scopes. Whitespace checks pass.
The straw-dog scan's one unwrapped candidate is the historical original comparison's
readiness dependency, not a new unsettled instruction. No application checks were
rerun: this continuation updates records and assesses unchanged source, rather
than implementing or asserting runtime compatibility.

## Retired attempt — 2026-10-05

The user retired this issue-preparation attempt before concluding the session.
The unpublished pilot pair is archived below; no local tickets or new project
issues were minted. The proposed four-outcome breakdown was never approved and
is historical, not the next session's queue. Broad investigation issues
[#3](https://github.com/dveyarangi/xuanxue-workshop/issues/3) and
[#4](https://github.com/dveyarangi/xuanxue-workshop/issues/4) are already closed as
not planned, as recorded in [migration changes](migration-changes.md).

Completed collection remains evidence. A new reconciliation attempt resumes by
rechecking affected revisions and selecting a small useful first connection,
then resolving its full shared shape before issue preparation. Accepted boundary
agreements remain in their owning records. Adoption, implementation and deployed
verification remain outstanding.

The user's contract-shape clarification is installed as RC2: implementation
assignments prescribe one complete shared shape through an accessible immutable
reference and common conformance cases. Internal implementation stays project-owned.
The [pilot contract question](questions/done/q-0002.0007.0005-what-is-the-exact-public-schedule-contract-for-the-cabinet-daychi-pilot.md)
records unresolved dimensions if that candidate is selected again; it does not
make the retired pilot an active assignment.

## Proposed remaining outcomes — 2026-10-05

<details>
<summary>Retired, unapproved breakdown — historical proposal only</summary>

The user requested the first application work maximize useful connection while
remaining cheap enough to test the issue exchange, with exactly one new issue per
project. Other local tickets may be created, but only that first pair is to be
published. The proposed first outcome is a working public-schedule pilot; the
three later outcomes are handoffs. A pilot needs actual provider/consumer evidence
to finish. Each later handoff delivers an agreed published baseline and scoped
assignments, without establishing recipient implementation or deployment.
Every implementation pair already prescribes the complete shared shape before
publication. Project ownership denotes the executable definitions' authored home
and internal choices, not independent contract selection.
The [migration delta](migration-changes.md#changes-derived-from-accepted-contracts)
and the comparison rows below supply its evidence; broad inventories are completed work.

### 1. cabinet-daychi-public-schedule-pilot — Proposed

- **Interaction:** HITL while the common request/response and data semantics remain
  unresolved; implementation can proceed within the fixed shape after agreement.
  The proposed read-only staging is presented for breakdown approval.
- **Depends on:** No new application outcome. Recipient execution retains Workshop
  readiness, that recipient's onboarding and a readable pilot baseline. Cabinet's
  provider contract precedes Daychi's final interoperability proof.
- **Parent scope covered:** The schedule comparison finding and first-stage
  addressed-work/return-path outcomes, exercised through one actual application seam.
- **Workshop outcome:** A native Daychi test path displays actual Cabinet public
  schedule data, and Workshop verifies the paired reports and updates the evidenced
  boundary state. Only this outcome produces the first two application issues.
- **Cabinet action:** Supply a public, complete bounded fourteen-day schedule from
  existing dated lessons, with usable identity/time/status and no private Zoom
  details. Preserve the current protected/count-based Cabinet web contract. Cabinet
  owns their authored home and implementation; both issues prescribe the same
  agreed query, typed data definition and guarantees before publication.
- **Daychi action:** Consume that definition through an opt-in native read-only
  path, reusing schedule presentation where practical. Keep pilot data out of the
  ordinary attendance, cache, private Zoom and local-notification flow. No school
  correction, fallback or sample data can masquerade as Cabinet data in the pilot.
- **Acceptance:** One existing native target reads a reachable Cabinet local/preview
  service without credentials, displays real occurrences and reflects an operator's
  reschedule/cancellation after refresh. Checks prove public response privacy,
  complete window coverage beyond the old count limit, empty/failure cases and
  preserved ordinary app behavior. The reports identify running revisions and
  reproducible steps; Workshop acknowledges evidence and records the limited pilot
  boundary. Posting the pair alone cannot close this ticket. No production rollout
  or full HTML-source removal is required.

Retired draft pair, never published:
[Cabinet provider issue](../.local/reconciliation-20261005/retired/cabinet-public-schedule-issue.md)
and [Daychi consumer issue](../.local/reconciliation-20261005/retired/daychi-public-schedule-issue.md).
The Daychi issue's running-provider dependency will link to the Cabinet issue at
publication. No existing assignment covers this implementation pair.

### 2. cabinet-access-handoff — Proposed

- **Interaction:** HITL. The authentication standard and remaining shared lifecycle
  obligations require the user's decision; accepted Cabinet authority, transports
  and installation-scoped sign-out remain fixed.
- **Depends on:** No other new handoff. Publication retains commit and push approval.
- **Parent scope covered:** Credentials, content admission and sign-out comparison
  findings; the first-stage requirement for agreed targets and addressed work.
- **Workshop outcome:** A usable shared access agreement and coordinated Cabinet
  and Daychi assignments for native acquisition, authenticated API use and retained
  content admission, without transferring account authority to Daychi.
- **Remaining recipient actions:** Cabinet supplies native credential issuance and
  validation, the narrow admission check and lifecycle support while preserving web
  cookies. Daychi consumes those credentials in its clients and retained content
  backend, replacing independent admission for the shared protected calls. Each
  project owns the authored home of its executable definitions and internal
  implementation while conforming to the same prescribed shared shape.
- **Acceptance:** Shared acquisition/lifecycle obligations are resolved or explicitly
  bounded by accepted provisional agreements. Published issues cite the governing
  revision and existing source findings; name expiry, renewal, revocation, caller
  trust and interoperability work precisely; distinguish refusal from temporary
  failure; require proof of installation-local sign-out and preserved Cabinet web
  access. Daychi public content and admin imports retain their separate access paths.
  Readback and /verify establish the handoff, without claiming working integration.

### 3. schedule-cutover-handoff — Proposed

- **Interaction:** HITL for completing and agreeing the common contract shape;
  implementation then follows that fixed shape without reopening accepted behavior.
- **Depends on:** The public-schedule pilot supplies proven provider/consumer
  references; cabinet-access-handoff supplies authenticated access obligations.
  Full source removal additionally waits for recipient reminder/identity
  compatibility evidence, not merely these handoffs' publication.
- **Parent scope covered:** Schedule and school-HTML comparison findings; the
  first-stage requirement for minimum adaptations and addressed work.
- **Workshop outcome:** Coordinated assignments for Cabinet schedule provision and
  Daychi consumption, with a concrete gate for removing the competing HTML source.
- **Remaining recipient actions:** Reuse the pilot's public definition and checks;
  Cabinet completes authenticated access and occurrence/class identity usable by
  both consumers while preserving Cabinet web. Daychi adapts its decoder, source
  selection and existing correction/refresh flow, then removes the school-HTML
  source only after the agreed integration checks pass.
- **Acceptance:** Published issues trace to the schedule rows and accepted contracts;
  require public responses to omit Zoom, complete fourteen-day coverage, stable
  occurrence identity through rescheduling, received cancellations and retention of
  cached Cabinet data after refresh failure. Cabinet supplies typed definitions and
  compatibility evidence; Daychi supplies consumer and cutover evidence. Exact query
  names and identifier encoding are fixed in the common contract before either
  implementation issue is published. Readback and /verify establish
  a scoped handoff; source removal requires later provider/consumer integration proof.

### 4. shared-reminders-handoff — Proposed

- **Interaction:** HITL for completing and agreeing shared synchronization and
  identity guarantees; internal implementation follows the fixed common shape.
- **Depends on:** The access and schedule handoffs supply the referenced credential,
  schedule-identity and recipient scopes. This dependency concerns coherent handoff
  publication; recipient implementation dependencies are stated separately in issues.
- **Parent scope covered:** Reminder selection/delivery findings, offline edits and
  lead time, and accepted removal of per-date skips; minimum changes and addressed work.
- **Workshop outcome:** Coordinated assignments for one shared account selection and
  lead time, consumed through existing Cabinet and Daychi delivery channels.
- **Remaining recipient actions:** Cabinet extends class-based preferences with
  one-off occurrence selections and reconciles selections, removals and lead time.
  Daychi pulls account data on sign-in, preserves offline edits through failures,
  reconciles existing local reminders and removes per-date skips. Project-owned
  synchronization design conforms to shared clock/conflict, removal and retry
  guarantees fixed before publication; internal pending-edit storage stays local.
- **Acceptance:** Issues require independent choices, latest-edit conflict resolution
  with Cabinet winning equal times, the agreed lead-time options, stable one-off
  identity, preserved pending edits and cached reminders, and discard of unsynced
  edits on explicit sign-out without cross-account replay. Cabinet compatibility
  evidence covers cancellation, recording and material notices that share the current
  class scope. The Daychi assignment carries the accepted skip-removal rationale.
  Initial scope uses the dated no-legacy-data report in the migration question;
  no historical import is added. Readback and /verify establish the handoff.

### Existing work and release conditions

[workshop-coordination-ready](tickets/01-0005-workshop-coordination-ready.md)
remains the existing queue's first item. Startup review, readiness publication and
acceptance wiring stay there. The two existing installation issues retain access,
instruction installation and fresh-session proof; routine follow-up and acceptance
continue in those issues. No new ticket duplicates those outcomes.

Only the public-schedule pilot's pair is proposed for issue publication now. The
other three outcomes remain local tickets after approval; their later conversion
is not authorized by this first-pair instruction.

Preparation and Planned posting of the proposed handoffs can precede onboarding.
Recipient execution waits for Workshop readiness, that recipient's confirmed
onboarding and a readable governing baseline. A handoff does not release execution
or complete the first stage. The overall stage still requires confirmed integration
of both agents and the return path for problems, results and record updates.

Gateway and content consolidation remain deferred. Native push, new background
refresh, notification deduplication and product presentation remain outside these
handoffs. Missing runtime or deployment proof becomes a specific acceptance request,
not a broad source-investigation assignment.

### Impact assessment of this split

#### Impact

The revised split adds one narrow, working connection before the three remaining
handoffs. The pilot adapts Cabinet public reads and a Daychi native display path,
with one implementation issue per project. It proves provider, consumer and issue
return/acceptance together. Shared sign-in and reminders would couple more state,
open lifecycle decisions and multiple consumers; document-only work would not
connect the applications. The public path therefore offers a useful connection
with fewer dependencies, though implementation cost is not yet measured. Providers,
data owners and implementers remain Cabinet and Daychi under separate operators.

#### Hidden edges

Local source reinspection on 2026-10-05 retains Cabinet `62831447` and Daychi
`5f9ba44`. Cabinet has instruction-only working changes; Daychi's local tree is
clean. Remote freshness and deployed behavior are not established by these reads.
The current Cabinet mapper includes Zoom, so removing its auth guard alone is
unsafe. Daychi's decoder is school-bound, its attendance identities are series/date
based and schedule refresh immediately changes OS reminders. The read-only pilot
avoids that coupling while testing a real provider. The pilot uses an existing
native target; browser CORS and a new deployment platform are not prerequisites.

Schedule occurrence/class identity is shared by retrieval and reminders. Credentials
are shared by authenticated schedule, account state and retained content. Reminder
scope also controls existing Cabinet notices. The proposed dependencies and explicit
compatibility evidence preserve those connections. Executable schemas have
project-owned authored homes; their externally observable shape and guarantees
are common and fixed before implementation assignments.
Source freshness must be checked when preparing each concrete assignment. Latest
accepted agreements remain local, so readable baseline publication and approval are
real dependencies. A posted assignment or closed handoff ticket proves no deployment.

#### Leave alone

Completed collection; accepted application semantics; sibling source and releases;
the existing readiness ticket and installation issues; the local queue order;
deferred gateway/consolidation; existing refresh and delivery channels; project UX.
No bulk legacy-data migration follows from the dated initial-usage report.

#### Recommendation

Proceed with the public-schedule pilot first and retain the three later handoffs
as local work. The initial broad schedule cutover was narrowed: changing the main
loader would pull reminder identity, private Zoom and cache migration into the
first pair. This revised scope removes those dependencies and requires an actual
Cabinet-to-Daychi display demonstration. Reuse pilot implementation and evidence
in the eventual cutover. Preserve the existing readiness priority and obtain
approval of the revised membership/dependencies before minting. Complete and agree
the shared pilot contract before publishing its pair; no later implementation
assignment is published under the user's first-pair instruction. The unresolved
shapes make these decision-bearing HITL outcomes at this stage.
</details>

## Original scope

Scope: the first substantive /reconcile pass over Cabinet's web/API seam,
Daychi's client/API and school-HTML seams, accepted Cabinet/Daychi targets,
and Workshop instruction publication and adoption. Governing records:
[current system](current-system.md), [targets](boundaries.md),
[migration changes](migration-changes.md), [stage scope](stage-1.md), and
[agent contract](agent-contract.md). This pass changes Workshop records and
existing installation assignments; implementation and releases remain with
each project's operator.

## Evidence and revisions

- Cabinet: clean local checkout and remote `main` at
  `628314472aa2752ebb2bbe9ab75ac3dea9791719`. Provider/data owner: Cabinet;
  accountable implementation contributor: Cabinet agent under its operator.
- Daychi: clean local checkout at `5f9ba442e04cd5dfa70527b9e670b491c491888c`.
  The connected GitHub account gets 404 for the repository. Local source is
  readable, but remote freshness and operator access cannot be established.
  Provider of retained content and accountable client contributor: Daychi agent
  under its operator. Cabinet is the accepted target data owner for users,
  schedule and authenticated selections.
- Workshop: GitHub reports a public repository with admin permission for the
  connected account. `master` is `ba5e35f24e49ac2931f3af9382646c5cbd87e1e8`.
  README, contract and skill were read back. This establishes source publication,
  not startup-review readiness or project adoption.
- All Workshop issues, including closed issues, were searched. Only installation
  issues [cabinet-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
  and [daychi-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/2)
  were returned; both are open, recipient-labelled, Planned and have no replies.
  No completion evidence was available to accept.

## Boundary comparison

| Boundary | Provider / consumers | Documented promise | Evidence / revision | Delta and consequence | Disposition / issue |
|---|---|---|---|---|---|
| Cabinet API ↔ Cabinet web | Cabinet backend / Cabinet frontend | Preserve existing workflows and authoritative shared route definitions. | `62831447`: `shared/src/api-routes.ts`, `web/src/api/apiRoute.ts`, `web/src/api/http.ts`, `api/test/api-routes.e2e-spec.ts`. Typed requests, cookie credentials, mutation CSRF header, error envelope and response-version handling exist. | No source contradiction established in the inspected schedule/auth/reminder paths. Route registration and typed checks exist; their current execution and deployment were not demonstrated. | Preserve active definitions in Cabinet. Runtime and supported-version evidence remains unverified. |
| Schedule for Daychi | Cabinet target / Daychi clients, Cabinet web | Public responses omit Zoom; authenticated responses may include it. Preserve existing calendar use and agree identifiers/window. | Cabinet `62831447`: `my-lessons-routes.ts`, `lessons.ts`, `my-lessons.controller.ts`, `my-lessons.service.ts`, `my-lesson.mapper.ts`. Daychi `5f9ba44`: `schedule/load.ts`, `model.ts`, `attendance.ts`, `practice_api/schedule_source.py`. | Cabinet student route requires a cookie, accepts only a 10/default, 50/max count and returns lesson IDs without class IDs. Daychi expects a fourteen-day snapshot with series/date IDs, source and freshness fields. A direct endpoint substitution cannot preserve choices or decode the response. | Unimplemented target. Workshop/user owns window, identity and response agreement; project agents own proposals and later adaptation. No active-contract defect or migration issue inferred. |
| School HTML ↔ native Daychi schedule | School website / Daychi backend and native app | Existing source and native fallback; target ownership moves to Cabinet. | `5f9ba44`: `schedule/load.ts`, `source.ts`, `zoom.ts`, `practice_api/schedule_source.py`. Native races HTML and API; web omits HTML fallback. Bundled timing corrections run after loading. | HTML-derived data cannot establish Cabinet cancellations or transfers; old correction rules may conflict with dated lessons. Existing record omitted the correction adapter. | Factual record expanded. Fallback and correction treatment belong to the existing migration decision; no new refresh mechanism introduced. |
| Credentials | Cabinet target / Cabinet web, Daychi clients and backend | Web cookie, native Cabinet bearer; Cabinet owns validation and lifecycle. | Cabinet `62831447`: `auth.guard.ts`, `auth.service.ts`, `session-cookie.ts`. Daychi `5f9ba44`: `access/session.ts`, `practice_api/daychee_app.py`. | Cabinet guard reads cookies, not bearer; Daychi uses independent opaque credentials with format constraints. Cabinet credential acquisition, format and existing-user transition remain undecided. | Unimplemented target. Preserve current authority descriptions and accepted target; standard/lifecycle decisions stay open. |
| Content admission and retained content | Daychi content backend / native app and wiki; Cabinet target admission / Daychi backend | Retain Daychi content, use narrow live Cabinet admission for protected calls; refusal differs from temporary failure. | `5f9ba44`: `daychee_app.py`, `wiki_app.py`, `wiki_graph.py`, `public_wiki.py`, `wiki_content.py`. Four protected content reads, four feature-gated public reads, and two admin import/status routes. | Current app injects its own invitation-store authorizer. Cabinet admission schema is not implemented or agreed. Public routes and admin imports are separate access paths; general profile response is not a narrow admission contract. | Unimplemented target. Keep public/admin access explicit in future contribution. Content consolidation remains deferred; no service retirement assignment. |
| Reminder selection | Cabinet target / Cabinet web and Daychi clients | One account selection supports individual dates and recurring classes. | Cabinet `62831447`: `lesson-notifications.ts`, `notifications-routes.ts`, web `useLessonScope.ts` and `useLessonReminder.ts`. Daychi `5f9ba44`: `attendance.ts`, `use-schedule.ts`. | Cabinet scope contains class IDs only, no one-off dates, with 15/30/60/120 or school default. Daychi stores one-off, recurring and skipped dates locally with 0/15/30/60. Cabinet scope also affects cancellations, recordings and materials, so changing it can alter existing web behavior. | Unimplemented target. Resolve timing and saved-selection transition with the user; retain accepted skip-removal rationale. No isolated removal assignment while saved exceptions remain undecided. |
| Reminder delivery | Cabinet existing inbox/browser push / Cabinet web; Cabinet target data / Daychi local OS reminders | Preserve Daychi refresh/local delivery, exclude native server push. | Cabinet `62831447`: `lesson-reminder.service.ts`, `push-sender.service.ts`, `web/public/sw.js`. Daychi `5f9ba44`: `use-schedule.ts`, `local-reminders.ts`, `reminder-plan.ts`. | Source supports the documented channels. Daychi restores cached data and reconciles reminders before first refresh; failure leaves that data in place. Stale cancellations and multi-client delivery require agreed behavior, not a new push adapter. | Existing channels confirmed by inspection. Record precise stale-data starting point; keep target policy unresolved. |
| Workshop ↔ project agent instructions | Workshop / Cabinet and Daychi agents under separate operators | Published skill, labelled discovery, complete summary and demonstrated invocation/reporting. | Workshop `ba5e35f`; issue bodies/comments read back; local Cabinet `CLAUDE.md`, Daychi root and app instructions inspected. No confirmed installed /collaborate baseline found. | Source is published and public, contrary to the readiness record. No project report demonstrates installation, access or invocation. Missing baseline is onboarding uncertainty, not an instruction regression. | Correct publication facts and reuse issues 1 and 2. Keep Planned until Workshop readiness is confirmed; request installation/access evidence in the original issues. |

Source paths in the table are relative to their owning repository; Cabinet shared
files live under `shared/src/`, provider files under `api/src/`. Daychi client
feature paths live under `apps/practice-app/src/features/`. Full revisions above
bind the inspection. Deployed capabilities and supported client versions remain
unverified across both projects.

## Project summaries

The complete fenced `BOUNDARY_SUMMARY` in each existing installation issue agrees
with the observed and target connections. Cabinet identifies its backend/frontend
and both planned Daychi connections. Daychi identifies both clients, retained
backend, native HTML source and both planned Cabinet connections. No summary
change is needed. The recipient agent must map these to local modules and return
its actual instruction revision; there is no installed baseline to compare yet.

## Changes and routing

Updated the current-system record with fresh inspection provenance and the
schedule identity/decoder/correction constraints. Updated the agent contract's
publication facts. Updated the existing installation issues with the published
revision, remaining readiness dependency and specific evidence requests. Their
summary blocks, recipient labels, scope and acceptance requirements stay intact.

No new application assignments were issued. The agent contract requires confirmed
onboarding before application work; accepted targets do not establish an active
implemented promise. The existing migration and credential questions hold the
decisions needed to make those assignments precise. Workshop startup readiness
remains in [workshop-coordination-ready](tickets/01-0005-workshop-coordination-ready.md).
No sibling edits, releases, commit or push were performed in this pass.

## Checks and limits

Daychi's existing attendance and schedule-model tests executed under local Node
24.14.1: ten passed, covering one-off/recurring selection, skip behavior, DST,
cancellation, reminder reconciliation, duplicate IDs and freshness boundaries.
The attempted access-session and schedule-Zoom test files could not load because
`typescript` and `htmlparser2` are absent locally; this is missing execution
evidence, not an application regression. Dependencies were not installed.
Daychi CI declares Node 22; this local run does not establish CI compatibility.
Cabinet's route-registration, authentication and reminder checks were inspected,
not executed. Neither production behavior nor a native notification device was tested.

Workshop mechanism/binding, question, ticket and straw-dog checks pass with no
diagnostics; whitespace validation passes. The question check suggests that the
migration and consolidation questions may be duplicates based on shared words.
Their recorded scopes differ: one retains Daychi content and the other defers
its consolidation, so they remain separate. Both remote issue updates were
fetched again and matched the intended bodies, recipient labels and open state.
The reconciliation procedure
has now been exercised against real source and tracker evidence; end-to-end
operator adoption and deployment acceptance remain outstanding.

## Withdrawn contribution proposal — 2026-10-05

Historical proposal, withdrawal and impact copied from migration-changes
during maintenance on 2026-10-06; the statements below preserve that dated state.

### Proposed contribution breakdown

This heading is retained for existing links. The older broad contribution proposal
was promoted into two Planned issues on 2026-10-05. The user then challenged their
scope as repeating Workshop's completed investigation. The earlier statement of
breakdown approval was the assistant's mistaken interpretation. At the user's
request on 2026-10-05, both were withdrawn and closed as `not_planned`. Readback
confirmed closure and the withdrawal notices; no recipient action is required.

#### cabinet-contract-contribution — Withdrawn, created in error

[cabinet-contract-contribution #3](https://github.com/dveyarangi/xuanxue-workshop/issues/3)
is addressed to the Cabinet project agent under its operator, with label
`project:cabinet`. Its posted scope requests an API inventory and proposals. That
inventory overlaps Workshop's completed work; the issue's existence does not
establish a remaining need for it.

#### daychi-contract-contribution — Withdrawn, created in error

[daychi-contract-contribution #4](https://github.com/dveyarangi/xuanxue-workshop/issues/4)
is addressed to the Daychi project agent under its operator, with label
`project:daychi`. Its posted scope requests a client/content inventory and proposals.
That inventory overlaps Workshop's completed work. Its body contains the user's
skip-removal rationale. No implementation or execution release occurred.

#### agreed-target-seam-contracts — Unissued proposal

The older third proposal described dependent Workshop alignment after those
contributions. No local ticket or issue was minted for it. Workshop's comparison
and subsequent alignment already advanced that outcome; it is not an instruction
to wait for repeated project investigations.

The [failure trace](rule-failures.md#2026-10-05--completed-reconciliation-reissued-as-project-investigation)
records the work-selection mistake. Actual remaining project changes are described
by the accepted-contract delta above; unresolved decisions and verification limits
retain their own records. The whole first stage is not an approved delivery breakdown.

### Impact assessment of the contribution split — refreshed 2026-10-05

The first refresh defended the split by project, without checking completed work.
The user rejected the resulting broad investigation scope. This corrected account
supersedes that recommendation; the posted issues are withdrawn and closed,
with their cancelled briefs retained as historical records.

#### Impact

The posted issues changed coordination records and requested project investigation
already substantially completed by Workshop. No sibling implementation changed.
The accepted-contract delta still identifies real migration changes, independently
of these mistaken assignments.

#### Hidden edges

Old proposal prose was treated as workflow authority, while implementation
ownership was mistaken for investigation ownership. Tracker duplicate searches
could not find completed work held in local source-analysis records. Some narrow
runtime/deployment proof and executable design choices remain open; that does not
make the broad inventory outstanding. Latest accepted contracts remain local.

#### Leave alone

Accepted provider assignments and boundary behavior; sibling application code,
releases, deployments, Cabinet-only workflows and project UX; deferred gateway
and backend consolidation; existing refresh facilities and installation/readiness
assignments. No duplicate local tickets or new legacy migration program exists.

#### Recommendation

Rethink the assignment scope. The existing comparison and accepted decisions are
the basis for identifying specific remaining changes and unavailable proof. A new
post-impact breakdown has not been accepted or issued. Publication and execution
dependencies remain distinct, and the local delivery queue is unchanged.
