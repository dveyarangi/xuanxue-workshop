# Shared account reminders

## Recipients and outcome

Existing work: [reminder synchronization 17](https://github.com/dveyarangi/xuanxue-workshop/issues/17).
Cabinet provides shared confirmed settings and uses them in web/backend reminders;
Daychi uses the same settings and authoritative calendar in its native reminder
path. Workshop owns contract compatibility and acceptance. All work and reports
remain in this issue, addressed to `project:workshop`, `project:cabinet` and
`project:daychi`. No new
issue, local ticket or decomposition approval is needed for this existing outcome.

Status: implementation in progress. The complete contract and this existing-issue
implementation assignment were approved by the Workshop operator on 2026-10-19.
Workshop's contract/assignment preparation is complete. Cabinet's merged read/save
API, delivery and cutover slices have reviewed source/check progress, and
Daychi has a reviewed draft candidate. Deployment/rollout and remaining
consumer/device and joint outcomes still require their existing evidence. The issue
stays open for those existing owner actions; no new shared decision or Workshop
readiness acknowledgement is required.

## Essential acceptance — 2026-10-21

Decision: the Workshop operator, 2026-10-21: remove everything unnecessary from
acceptance, following the explicit review of required outcomes and excess gates.
The operator reaffirmed preservation of existing implementation and staging;
the purpose is to remove unnecessary ceremony and clear integration closure.
This section governs current acceptance and closure of original 17.

Cabinet web and installed Daychi in iOS Simulator with real Cabinet staging use
the same confirmed reminder settings. Only selected classes/lessons generate
reminders; new accounts start empty. Independent changes survive; the last
Cabinet commit wins for the same key. Uncertain saves recover by reading current
state without automatic mutation replay or false success. Offline editing is
unavailable while confirmed cached viewing/reminders survive. Received moves and
cancellations are applied; account/issuer/guest state stays separate. Agreed
personal leads and the school default retain their product meanings.

The previously agreed joint proof remains: different/same-key saves,
committed/noncommitted lost-response readback, offline refusal with retained
reminders, move/cancellation recovery and logout/account/issuer isolation.
Preservation of existing choices and separation of legacy writers remain;
reuse credited automated migration and regression evidence. Physical devices,
Android, production mobile release and an exhaustive platform matrix are
non-blocking. Existing source, automated and synthetic evidence remains credited.

Technical quotas and exact counter/window, restart, replacement or replica
behavior are not acceptance or closure requirements. Neither are the reminder
50-class, 64-change and 128-KiB boundaries or exact retry-delay boundary tests.
Existing compatible API values, working protections and useful tests may remain;
no removal or reimplementation in recipient code is assigned. Malformed input
must still cause no unauthorized content, partial save or false confirmation.
No performance/stress target or expanded device/environment matrix is added.
Already credited evidence is reused; neither a new report format nor repeating
accepted builds, installation, account proof, CI or synthetic QA gates closure.

Sole common authority: [reminder-sync](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/reminder-sync.md#essential-acceptance--2026-10-21), immutable revision `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
The following technical sections preserve compatible exchange and credited work;
they do not add acceptance gates beyond this operator-agreed section.

## Shared authority and accepted behavior

The complete [reminder synchronization contract](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/reminder-sync.md),
its wire version 1 and common conformance outcomes govern both recipients. Its
linked native-account and public-calendar authorities remain binding.
Accepted immutable Workshop authority: `3c6ff8a7136483b3d266786fa8267eab4f2d2828`.
This revision includes the operator-approved 21 October essential-acceptance
reduction above. Existing wire-version-1 values may remain for compatibility;
numeric selection/payload/rate boundaries and their proof do not gate closure.
Core reminder behavior and safe rollout remain.
Both projects implement that exact wire and its common conformance outcomes.

Cabinet owns account settings; only explicitly selected classes/lessons are
eligible, and new accounts start empty. Saves are online and Cabinet-confirmed;
independent keys survive and the last Cabinet commit wins on one key. An uncertain
save recovers by reading current state, never by automatic mutation replay.
Offline viewing and scheduled local reminders remain. Leads are school default
or 0/15/30/60/120; zero targets start with up to one minute processing tolerance.
Other notification filters remain separate. No fixed 60-reminder account cap,
offline outbox, client-clock policy, native push or new background polling exists.

## Current-delivery acceptance scope — 2026-10-20

The Workshop operator approved the contract's
[current-delivery acceptance scope](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/reminder-sync.md#current-delivery-acceptance-scope--2026-10-20).
Client rejection of an otherwise valid snapshot solely for containing more than
50 class IDs, and handling of supplied retry delays exceeding one hour, are not
acceptance requirements for this delivery. This supersedes the corresponding
correction requests in the [20 October review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6281943775)
and earlier supplied-delay follow-ups. No additional correction or regression
evidence for these two observations is required to accept either contribution
or close this issue. Reconsider them on evidence of an effect on normal operation.
The 21 October decision additionally excludes numerical server/client bounds
and exact retry delays as acceptance obligations. Existing values may remain
for compatibility. Safe validation, readback, no-replay, isolation and joint
outcomes still apply.

## Accepted joint-proof runtime — 2026-10-20

The Workshop operator explicitly accepted the contract's
[installed iOS Simulator and real Cabinet staging scope](https://github.com/dveyarangi/xuanxue-workshop/blob/3c6ff8a7136483b3d266786fa8267eab4f2d2828/docs/contracts/reminder-sync.md#accepted-joint-proof-runtime--2026-10-20).

For current-delivery joint acceptance, installed Daychi in iOS Simulator connected
to real Cabinet staging is sufficient. Separate physical-device and Android runs
do not block acceptance or closure of original issue 17. Existing functional/common-case
obligations remain; this decision does not establish that the joint run has passed.

## Credited evidence and remaining closure actions — 2026-10-21

The credited work below is retained under the operator-approved 21 October
acceptance reduction above. The original issue remains the
Cabinet/Daychi/Workshop work and evidence channel.

### Credited — no repeat implementation or accepted checks

- Cabinet GET/PATCH, online confirmed web edits/readback, specified-key atomic
  saves/revisions, lesson delivery, selected-mode seeding, retained other-notice
  preferences and retired/separated legacy writers have reviewed source and
  executed automated evidence in [the source/cutover review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6279637451).
  Valid Mongo migration and real-AppModule cutover tests are credited.
- PR609 validation/recovery changes and PR610's StaffBoard test diagnosis/fix are
  reviewed in [the correction review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6281943775).
  These changes are merged; fresh 21 October Cabinet staging health is 200 at
  20128fb, Mongo up, scheduler enabled/non-stale. Provider deployment is credited;
  a new deployment is not requested as proof of the already running revision.
- The two observations about client rejection solely for 51 returned class IDs
  and supplied retry delays over one hour are operator-waived for this delivery.
  They require no correction or regression evidence as closure prerequisites.
  The 21 October reduction also removes numeric bound/counter proof from closure;
  existing values may remain without corrective implementation or new tests.
- Daychi PR19 ea464ef protocol/confirmed-save/readback/fencing/guest/calendar/
  bounded-queue source and six successful exact-source checks are reviewed.
  Seven inspected synthetic QA images, the reported 159 app tests/native exports
  and queue receipts are credited within their stated provenance/scope, including
  60-of-100 coverage, cancellation/refill, empty-calendar choice preservation and
  logout clearing. No repeat screenshot set or new platform matrix is requested.
- Existing native-account and public-provider acceptance remains valid. Daychi
  PR19 is still draft/default-off at the reviewed source; that marker alone is
  not a closure criterion, and these synthetic results do not claim real Cabinet
  shared saves. Initial-rollout approval for existing Cabinet users remains as
  [clarified by Cabinet's operator](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6265787981).

### Remaining actions and responsible parties

| Owner | Only remaining action | Completion evidence / condition |
|---|---|---|
| Cabinet under @kotlarewski | Supply the outstanding actual rollout receipt on the deployed revision: applied seeding preserves explicit choices/personal lead/other notices; all-mode does not create reminder subscriptions; retired/legacy writers retain their accepted separation. | Reuse the credited Mongo/AppModule regressions and deployment identity. Return the missing runtime/migration outcome, not another implementation, full suite or audit of every user. Exam data is outside this work; no deletion or guest import is assigned. |
| Daychi under @stnleo | Identify the installed iOS Simulator reminder candidate connected to real Cabinet staging for the shared account/web/app exercise. Reuse existing code, exports, queue/coverage evidence and mapping where applicable. | The actual connected runtime and its versions are identified. Physical hardware/Android, merge or production mobile release are not independent acceptance gates. Existing queue evidence is not re-requested solely because the transport changes; changed behavior or an identified gap determines any scoped check. |
| Cabinet and Daychi agents under @kotlarewski / @stnleo | Return the existing common joint cases with the matching authorized account, Cabinet web/provider and installed Daychi: different-key and same-key saves; committed/noncommitted uncertain-save readback without replay; offline edit refusal with retained reminders; received move/cancellation recovery; logout/account/issuer isolation. | Actual shared outcomes are reported once here, with existing source/automated proofs reused. This agreed joint proof has not been claimed complete. No fresh live-fixture matrix is added. |
| Workshop under @Yarangi | Reconcile the above results against the immutable shared contract and credited case mapping, then record full acceptance and close when the outstanding outcomes are complete. | No repeated accepted account/schedule/content/browser run, new screenshot/cold-start/platform criterion or additional Ready checkpoint. |

The accepted iOS Simulator runtime and the two explicit client waivers above
govern closure. Physical-device/Android delivery and unclaimed QA disclosures
alone do not add blockers. Browser 12/13 and native content 15/16 remain separate.
No actual shared save, preservation result or account/fixture operation is claimed
by this status update itself.

## Retained Cabinet contract responsibilities

These retain shared behavior subject to essential acceptance above, not a request to repeat the credited
implementation or checks. Only the remaining actions above are outstanding.


- Provide the specified GET/PATCH for existing matching browser/native credentials,
  current account/grant validation, CSRF, private no-store responses and errors.
  Retain native-session ownership, issuer separation and credential lifecycle.
- Store complete positive class/lesson choices and nullable lead time with atomic
  specified-key updates, Cabinet commit ordering, exact committed snapshots and
  monotonic revisions. Validate whole batches before changes; preserve unrelated
  keys and implement safe no-op/removal behavior without partial writes.
- Adopt the shared API in Cabinet web: confirmed online-only editing, serialized
  saves, no automatic mutation retry and current-state readback after uncertainty.
  Fence stale account/session/revision responses. This recovery behavior applies
  to web as well as native; browser renewal must not replay a mutation implicitly.
- Make backend lesson-reminder recipients the union of selected classes and
  selected lesson IDs. Preserve stable occurrence identity through moves,
  cancellation/restoration, channel/kind preferences and per-account/lesson
  delivery deduplication. Support personal 0/120 and all valid school defaults;
  implement the contract's zero-start processing window without shifting positive
  lead targets or introducing missed-window catch-up.
- Implement initial seeding, web/API cutover and legacy-route separation exactly
  as the contract states. Other notice filters and channel preferences survive;
  legacy all-mode never becomes implicit reminder subscriptions. Retired lead PUT
  is 404; old scope PUT cannot replace reminder selections. A rollback disables
  shared editing rather than restoring unsafe whole-list reminder writes.

Cabinet owns executable schemas, persistence, transaction/concurrency mechanisms,
module layout, UI presentation and scheduler internals within these observable
guarantees. No offline merge, client clock policy, idempotency ledger, native push,
content-access amendment, new roles or deployment mechanism is assigned.
No agent-instruction or collaboration-summary replacement is supplied by this issue.

## Retained Daychi contract responsibilities

These retain shared behavior subject to essential acceptance above, not a request to repeat the credited
source, checks, synthetic QA or exports. Only the remaining actions above are outstanding.


- Connect the accepted native account owner to authenticated GET/PATCH at the
  matching Cabinet issuer. Do not expose credentials to schedule state, send browser
  cookies or introduce a new auth/content path. Validate complete successful
  snapshots and fence late account/session/issuer or lower-revision responses.
  Equal revisions still allow refreshed school/catalogue metadata.
- Scope confirmed settings/cache and account-owned OS notifications by issuer and
  account. On sign-in read Cabinet without uploading guest choices. Preserve guest
  state separately; restore it on sign-out. Explicit logout cancels account reminders
  and discards transient work, while a network/auth failure preserves confirmed
  cache under the existing lifecycle. No old save may replay into another sign-in.
- Make shared selection/lead edits online-only, serialized and confirmed by Cabinet.
  A local draft must not change scheduled reminders. Disable automatic mutation
  replay, including session-renewal wrappers. After an uncertain response retain
  confirmed settings/reminders and read current Cabinet state before another
  deliberate save; do not treat readback as a receipt for the lost operation.
- Connect the signed-in account calendar to the accepted Cabinet public source,
  stable occurrence/class IDs and the full requested school-time window, with
  best-effort omission handling from the shared contract. Do not generate Cabinet IDs from legacy labels or
  catalogue slots, or fall back to HTML as account authority. Retain chosen IDs
  outside the current calendar window and missing catalogue labels.
- Reconcile OS reminders from confirmed union eligibility, future starts and the
  effective lead (0/15/30/60/120 or the actual school default, e.g.45). Preserve
  existing refresh occasions and good cache/reminders on failed reads; apply
  received moves/cancellations and confirmed deselections. Zero schedules at a
  future start, without catch-up after start. Device permission/local delivery
  enablement remains local; cross-client duplicate delivery is allowed.
- Remove per-date skips from the account reminder path. The product rationale is
  that opening the app merely to avoid one reminder is not useful: dismissing the
  notification suffices, and skipping informs no teacher or frees a reserved place.
  An individual deselection cannot suppress an independently selected class.
- Replace the unconditional 60-item failure with supported-device queue handling
  that preserves complete account choices and still applies deselections and
  received moves/cancellations. Queue sizing, prioritization and replenishment
  belong to Daychi within existing refresh occasions. State measured coverage and
  OS/suspension limitations; do not add a shared selection cap or background/push
  channel, or claim unlimited device delivery.

Daychi owns executable adapters, local storage/queue design, internal modules,
presentation and permission flow within the shared outcomes. Guest operation stays
independently owned. Content, meeting access, native/browser sign-in protocols,
legacy content retirement and unrelated UI redesign are outside scope.
No agent-instruction or collaboration-summary replacement is supplied by this issue.

## Execution dependencies and acceptance ownership

Cabinet staging web/API deployment is already confirmed at 20128fb; it is not a
fresh deployment or readiness request. Existing contract/common-case/source and
local test work is credited above. Matching authorized account access and an
identified installed Cabinet-connected Simulator runtime enable the remaining
common shared-save/readback/offline/calendar/logout outcomes. Cabinet owns any
actual rollout/account-authority work; Daychi owns its selected runtime. No
account mutation or recipient release is authorized by this status update.

Neither issue closure, Workshop readiness acknowledgement, native-content PR
merge nor browser DNS gates those remaining preparations. Accepted native-account
and public-calendar evidence remains reusable where it establishes the same
outcome. Workshop reconciles the agreed remaining outcomes and existing proof.

## Credited Cabinet evidence and remaining proof

The source/HTTP/atomicity/concurrency/web-recovery/delivery/migration-regression,
legacy separation and staging-deployment evidence is credited as listed above.
Retain the essential user-outcome coverage; do not rerun or resubmit already inspectable
accepted checks. Cabinet's missing actual rollout outcome and the common joint
results are the only remaining evidence actions listed in the current table.

## Credited Daychi evidence and remaining proof

The reviewed code, successful exact-source checks, synthetic storage/guest/
calendar/queue receipts and installed QA/export evidence are credited as listed
above, within their recorded scope. No new physical-device, Android, screenshot,
populated-guest cold-start or platform requirement is inferred from disclosures.
The identified Cabinet-connected Simulator runtime and agreed actual joint cases
in the current table remain; reuse existing proof without another unrelated
sign-in/content/browser/account or successful public-provider run.

## Workshop review and completion

Workshop's contract/assignment preparation and source/automated/synthetic reviews
are complete within the credited scopes above. Workshop reviews only changed
evidence and the current table's missing rollout/actual joint outcomes against the
accepted immutable contract and waivers. Shared artifacts are linked once here;
no duplicate proof, new issue or separate Ready/acknowledgement checkpoint is added.
The issue closes after the outstanding agreed outcomes are evidenced and accepted.
Existing accepted account/public-provider work and separate browser/content work
retain their own scopes. The explicit operator-approved acceptance reduction above grants no
account/fixture/release authority.
