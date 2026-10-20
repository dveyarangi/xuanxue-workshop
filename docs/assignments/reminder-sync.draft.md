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

## Shared authority and accepted behavior

The complete [reminder synchronization contract](https://github.com/dveyarangi/xuanxue-workshop/blob/630120c1fb77cf0db2f23338b7631432110f2aa3/docs/contracts/reminder-sync.md),
its wire version 1 and common conformance outcomes govern both recipients. Its
linked native-account and public-calendar authorities remain binding.
Accepted immutable Workshop authority: `630120c1fb77cf0db2f23338b7631432110f2aa3`.
This revision includes the operator-approved 20 October acceptance-scope
amendment below. Existing server selection limits and rate limiting, wire
version 1, reminder behavior and rollout remain unchanged.
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
[current-delivery acceptance scope](https://github.com/dveyarangi/xuanxue-workshop/blob/630120c1fb77cf0db2f23338b7631432110f2aa3/docs/contracts/reminder-sync.md#current-delivery-acceptance-scope--2026-10-20).
Client rejection of an otherwise valid snapshot solely for containing more than
50 class IDs, and handling of supplied retry delays exceeding one hour, are not
acceptance requirements for this delivery. This supersedes the corresponding
correction requests in the [20 October review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6281943775)
and earlier supplied-delay follow-ups. No additional correction or regression
evidence for these two observations is required to accept either contribution
or close this issue. Reconsider them on evidence of an effect on normal operation.
The server's existing 50-class limit and rate limiting remain; other malformed
response, readback, no-replay, account-isolation and joint outcomes still apply.

## Accepted joint-proof runtime — 2026-10-20

The Workshop operator explicitly accepted the contract's
[installed iOS Simulator and real Cabinet staging scope](https://github.com/dveyarangi/xuanxue-workshop/blob/630120c1fb77cf0db2f23338b7631432110f2aa3/docs/contracts/reminder-sync.md#accepted-joint-proof-runtime--2026-10-20).

For current-delivery joint acceptance, installed Daychi in iOS Simulator connected
to real Cabinet staging is sufficient. Separate physical-device and Android runs
do not block acceptance or closure of original issue 17. Existing functional/common-case
obligations remain; this decision does not establish that the joint run has passed.

## Observed state and scope

The [source comparison](https://github.com/dveyarangi/xuanxue-workshop/blob/67bb5dde5489a8e6594a9d978e5ed8d3ad703724/docs/current-system.md#reminder-synchronization-source-comparison---2026-10-19)
pins Cabinet application source `5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05`;
Main `88794f67d45b2fd31c2bbbc796e0effa1591699d` adds only browser tests;
the final review also compared successor `ea4299606ef8a8e2091931645bf4d21c20c5a450`,
whose native GET-me budget change does not alter reminder settings or the public
calendar. This assignment neither changes nor reopens that separate capacity contract.
At that baseline, Cabinet used all/selected class scope, full-list PUTs and
separate lead updates, without individual lesson choices or personal zero. That
legacy scope also filters cancellation, recording and class-linked material notices.

As reviewed overnight on 20 October, Cabinet PR607 (delivery) and PR608
(seeding/legacy separation) are merged at e604adab and 9fc0703 respectively.
The [progress review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6279637451)
records inspected source and successful checks; actual deployment, migration
outcomes and complete joint acceptance are not established by those merges.
The observed migration preserves existing reminder choices first and caps the
combined class list at 50; preservation of an arbitrary larger combined selection
was not established.

The [correction review](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6281943775)
inspected PR609 at 8d932249 and PR610 at d855ba5, both then open/unmerged.
PR609 rejects the earlier invalid school-minute, slot and ID examples. Its two
remaining observations are covered by the acceptance amendment above. PR610
supplies reviewed source/check evidence for the separate StaffBoard test-mock
diagnosis. These dated reviews do not claim either candidate is now merged,
deployed or independently runtime-accepted.

Daychi's published draft PR19 at ea464ef has reviewed protocol, confirmed-save,
readback, account/guest, calendar and OS-queue source, six successful exact-source
checks and seven hash-verified, visually inspected synthetic QA images. The
159 app tests, native exports and queue receipts retain recipient provenance.
At that review the candidate remained default-off/unmerged; real Cabinet joint
saves and remaining consumer/device outcomes were not established. Reuse these
results and their disclosed limits rather than repeating valid proof.

The user confirmed test-only Daychi data. Cabinet's operator subsequently
[clarified that Cabinet has real registered accounts and active exam use](https://github.com/dveyarangi/xuanxue-workshop/issues/17#issuecomment-6265787981)
and explicitly accepted the initial reminder rollout as written for those accounts.
Explicit selected class IDs, personal lead values and other notice filters remain
preserved; default all-classes mode does not become reminder subscriptions. Exam
data is outside this work. No heuristic guest import or existing-data deletion is
assigned.

No agent-instruction or collaboration-summary replacement is supplied here.

## Cabinet responsibilities

- Provide the specified GET/PATCH for existing matching browser/native credentials,
  current account/grant validation, CSRF, private no-store responses and errors.
  Retain native-session ownership, issuer separation and credential lifecycle.
- Store complete positive class/lesson choices and nullable lead time with atomic
  specified-key updates, Cabinet commit ordering, exact committed snapshots and
  monotonic revisions. Validate whole batches before changes; preserve unrelated
  keys and implement no-op/removal/bound behavior without partial writes.
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

## Daychi responsibilities

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

Both projects can implement and run local/contract tests concurrently under their
operators after the complete immutable contract is accepted and published. No
recipient issue closure, Workshop readiness acknowledgement, native-content PR
merge or browser-wiki/DNS work gates that implementation. Existing public-calendar
work in [original 6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
and accepted native-session evidence can be reused where they prove this outcome.

Cabinet web/API deployment at the matching issuer enables Daychi shared editing.
Cabinet's operator owns provider release and staging account/fixture authorization;
Daychi's operator owns consumer release and an identified installed native build.
Those running ends and authorized fixtures enable real joint proof. This issue
does not independently authorize account mutation or a release. Workshop reviews
both local contributions and the shared proof against the same contract.

## Cabinet acceptance evidence

- Immutable source/PR references, executed HTTP/schema/access cases and a mapping
  to every applicable common conformance row. Include real concurrent independent
  and same-key saves, atomic invalid batches, exact snapshot/revision/no-op behavior,
  limits, privacy and revoked/blocked/mixed-auth cases.
- Executed web uncertainty/renewal/no-replay and account/session/revision safety
  cases; initial seeding/legacy writer separation and unaffected other notices.
- Backend delivery evidence for empty/union choices, moved/cancelled/restored
  occurrences, deduplication, zero at the start through +60 seconds, missed zero
  windows, positive leads and school default 45. Distinguish scheduler eligibility
  from external channel delivery latency.
- Report actual deployment state and version, without treating green CI as runtime
  proof. Joint staging evidence with Cabinet web and the identified installed Daychi
  build covers independent/same-key edits, uncertain readback, offline refusal with
  retained reminders, move/cancellation recovery and logout/issuer isolation.
  Either recipient may supply shared evidence; link it once in this issue rather
  than repeating runs without a missing obligation.

## Daychi acceptance evidence

- Immutable code/PR, executed consumer tests and a mapping to every applicable
  common conformance row. Include offline edit refusal, serial saves, uncertain
  committed/noncommitted outcomes, no automatic retry, concurrent readback,
  malformed success, lower/equal revisions and logout/account/issuer fencing.
- Guest/account storage and OS ownership proof, empty/union choices, absent metadata
  and out-of-window IDs, zero/120/default45, removal of skips, successful best-effort
  calendar replacement,
  successful move/cancellation/restoration recovery and failed-read preservation.
- Installed supported-device evidence identifies platform/OS/build, pending queue
  capacity handling, coverage/refill, permission and suspension limitations, and
  demonstrates that queue pressure cannot block confirmed deselections or received
  moves/cancellations. Local queue pressure must not truncate account state.
- Joint staging evidence with matching authorized account, Cabinet web/provider
  revision and identified installed native build demonstrates independent/same-key
  saves, lost-response readback, offline refusal with retained reminders,
  move/cancellation recovery and logout/issuer isolation. Reuse accepted native
  session and original 6 evidence where it actually proves these outcomes; do not
  repeat unrelated sign-in/content/browser runs. Shared artifacts can be linked
  once in this issue.

## Workshop review and completion

Workshop owns the immutable contract, shared conformance cases, clear owner actions
and evidence review. Report progress/blockers and immutable implementation results
in this existing issue under the relevant responsibility. Related alignment
decisions are communicated in one consolidated update; urgent recipient action
can be communicated earlier. No separate completion acknowledgement is a new gate.

Workshop has completed contract/assignment preparation and reviewed the source,
checks and synthetic progress linked above. It will review changed contributions
and actual joint results against the amended contract, reusing valid prior proof.
The remaining owner actions are Cabinet integration/deployment and actual rollout
preservation/separation evidence; Daychi remaining consumer/device evidence; and
joint staging proof. The two waived observations add no acceptance prerequisite. Reuse shared
artifacts rather than running the same proof twice. The issue closes when these
in-scope outcomes are accepted; already accepted account-session/public-provider
work and unrelated browser/content work retain their own scope.
