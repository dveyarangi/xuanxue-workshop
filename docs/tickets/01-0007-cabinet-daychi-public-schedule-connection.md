# Cabinet–Daychi public schedule connection

- **record of** what it intends to become
- **Status:** Planned
- **Type:** HITL
- **Answers:** [q-0002.0002.0002](../questions/q-0002.0002.0002-which-workshop-outcomes-should-the-remaining-reconciliation-pass-deliver.md)
- **Outcome:** A verified native Daychi connection to Cabinet's public dated schedule, with separately reviewed provider/client contributions and Workshop records reconciled to their evidence.

## Parent

The [first-stage goal](../stage-1.md) and existing
[reconciliation pass](../reconciliation-20261004.md) supply the context.
The accepted [first schedule connection](../boundaries.md#accepted-first-schedule-connection)
and [public lessons contract](../contracts/public-lessons.md) govern the result.

## What to build

Issue the first addressed application pair: Cabinet provides the public lessons
API; Daychi consumes it in its native staged pilot. Both assignments use the same
accessible immutable contract and common conformance cases, so their results can
be reviewed against one agreement.

Recipient development proceeds under its operator against the accessible settled
shared contract. Workshop readiness and installation acceptance do not gate it.
A reachable conforming Cabinet provider, controlled fixtures and an actual native
runtime are conditions of integration proof, assessed from current evidence.
Publication can precede execution eligibility and does not finish this outcome.

The [2026-10-06 environment check](../current-system.md#cabinet-public-schedule-environments--checked-2026-10-06)
identifies `https://staging.xuanxue.su` as the native test provider and links its
runtime evidence and existing staff fixture controls. The latest check also
confirms the original public route on production at `fc2dee2`. The user amended
the not-yet-used pilot on 2026-10-07: omit corrupt rows with error-level logs,
without adding a version selector or completeness metadata. Valid-only omission and
explicit logs are verified in the scoped 2026-10-08 provider review below. Actual
native refresh proof remains outstanding; fixture writes belong to Cabinet's
authorized operator. Daychi's installation is accepted in issue 2. The user removed
readiness and installation-acceptance gates on 2026-10-08; issue 6 retains only the
activity conditions needed for actual integration proof.

Review contribution evidence in the original assignments, reconcile current
boundary and remaining migration records, then publish those records before
acceptance acknowledgement. Preserve ordinary Daychi schedule/reminders and the
protected Cabinet student route. Implementation and release remain with project
operators.

The production target is `https://xuanxue.su`, serving the
[same public API](../boundaries.md#accepted-first-schedule-connection).
Native proof on staging is sufficient for this outcome. Production deployment
remains under Cabinet's operator.

## Acceptance criteria

- [x] 2026-10-05: Both addressed issues are published with the same accessible immutable
  contract and common cases, correct recipient labels and explicit execution dependencies.
  [cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5)
  and [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
  share [contract revision e209d27](https://github.com/dveyarangi/xuanxue-workshop/blob/e209d27239391be3af2be71b898c79f453851c01/docs/contracts/public-lessons.md).
- [x] 2026-10-08: Cabinet's public provider and protected-route regression evidence satisfies
  the amended shared agreement, including valid-only rows, error logs for omitted
  corrupt occurrences and genuine whole-read errors; reviewed evidence identifies
  reachable setup/runtime and deployment limits.
  [Scoped review](../current-system.md#assignment-evidence--reviewed-2026-10-08):
  PR 570 / `868a4ed`, successful merge CI and staging runtime verified;
  production retains `fc2dee2`. Records were published at `48ddb32` and
  [Cabinet's contribution accepted](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052988637).
- [ ] Daychi's pilot satisfies the consumer cases and preserves ordinary schedule,
  cache, selections, access credentials and OS reminders.
- [ ] Actual native-to-provider evidence demonstrates dated results, controlled
  reschedule/cancellation, mixed valid/invalid reads, repair recovery and
  failed-refresh retention, with reproducible
  environment and revision references; mock-only results are insufficient.
- [ ] Workshop reviews each contribution, records verified capability and remaining
  migration scope, publishes reconciled records and acknowledges accepted evidence
  in the original issues.
- [ ] /verify confirms this ticket's complete outcome against the governing
  contract, contribution evidence and Workshop records.

## Progress review — 2026-10-10

Daychi supplied new native and TestFlight 17 progress reports in the original
issue. The [current evidence](../current-system.md#assignment-and-native-profile-recheck--2026-10-10)
distinguishes reported checks/native reads/release from inspectable implementation
and verified integration. No additional acceptance criterion is checked by this
review: published client/QA artifacts and controlled provider/native proof remain
missing. Physical-device release and Android product checks are not added as new
Workshop gates beyond the existing native device/emulator and retained-behavior
criteria.

The [original Cabinet issue follow-up](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6090400430)
requests the authorized fixture operator, integration origin/revision, identities,
timing and cleanup for the already-scoped joint proof. The
[Daychi response](https://github.com/dveyarangi/xuanxue-workshop/issues/6#issuecomment-6090404158)
requests accessible client/QA evidence and records that fixture coordination is
underway. Cabinet provider acceptance stands; issue 6 remains open. Queue order
is unchanged. The next review resumes when accessible client evidence or the
operator-owned fixture arrangement arrives; available recipient work continues
under its own operator.

## Out of scope

Broader account/reminder migration, authentication integration and schedule-source
cutover remain in [migration changes](../migration-changes.md). Gateway and backend
consolidation retain their deferred scope. Later assignment pairs require their
own scope authorization.
