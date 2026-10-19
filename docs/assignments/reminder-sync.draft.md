# Shared account reminders — consolidated update for existing issue 17

## Recipients and outcome

Existing work: [reminder synchronization 17](https://github.com/dveyarangi/xuanxue-workshop/issues/17).
Cabinet provides shared confirmed settings and uses them in web/backend reminders;
Daychi uses the same settings and authoritative calendar in its native reminder
path. Workshop owns contract compatibility and acceptance. All work and reports
remain in that issue, with `project:workshop`, `project:cabinet` and `project:daychi`
labels when the accepted implementation responsibilities are published. No new
issue, local ticket or decomposition approval is needed for this existing outcome.

Status: final review proposal for the existing issue body; implementation
responsibilities become issued only after acceptance of the complete contract.
The issue stays open for the outstanding owner actions and joint proof after
contract publication. Publication alone does not establish a working integration.

## Shared authority and accepted behavior

The complete [reminder synchronization contract](../contracts/reminder-sync.md),
its wire version 1 and common conformance outcomes govern both recipients. Its
linked native-account and public-calendar authorities remain binding. The final
published issue body will cite a full immutable Workshop commit for that contract;
the relative draft link is review material, not an issued implementation authority.

Cabinet owns account settings; only explicitly selected classes/lessons are
eligible, and new accounts start empty. Saves are online and Cabinet-confirmed;
independent keys survive and the last Cabinet commit wins on one key. An uncertain
save recovers by reading current state, never by automatic mutation replay.
Offline viewing and scheduled local reminders remain. Leads are school default
or 0/15/30/60/120; zero targets start with up to one minute processing tolerance.
Other notification filters remain separate. No fixed 60-reminder account cap,
offline outbox, client-clock policy, native push or new background polling exists.

## Observed state and scope

The [source comparison](../current-system.md#reminder-synchronization-source-comparison---2026-10-19)
pins Cabinet application source `5838fa5fef3bbd7a0e22aa43b68cf7fd72397a05`;
Main `88794f67d45b2fd31c2bbbc796e0effa1591699d` adds only browser tests;
the final review also compared successor `ea4299606ef8a8e2091931645bf4d21c20c5a450`,
whose native GET-me budget change does not alter reminder settings or the public
calendar. This assignment neither changes nor reopens that separate capacity contract.
Cabinet currently has all/selected class scope, full-list PUTs and separate lead
updates; it lacks individual lesson choices and personal zero. The old scope
also filters cancellation, recording and class-linked material notices.

Daychi main `c146326c7ea552772d8c804b3a08ad5637ca5eb0` uses legacy identities
and device-wide settings in its ordinary path; its separate Cabinet pilot has
real IDs without writing ordinary reminder state. Lead persistence lacks
120/null/default handling, and the local planner throws above 60 items. Those
are implementation gaps, not new shared product decisions. Its native account
session is accepted. Native-content PR18 is separate and does not gate this work.

The user confirmed test-only Daychi data and no current Cabinet users. No real-user
migration or heuristic legacy import is assigned; existing guest/test data remain.
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

The remaining owner actions are Cabinet implementation/deployment evidence, Daychi
implementation/installed-device evidence and joint staging proof. Reuse shared
artifacts rather than running the same proof twice. The issue closes when these
in-scope outcomes are accepted; already accepted account-session/public-provider
work and unrelated browser/content work retain their own scope.
