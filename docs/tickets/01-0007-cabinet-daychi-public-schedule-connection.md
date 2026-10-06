# Cabinet–Daychi public schedule connection

- **Status:** Planned
- **Type:** HITL
- **Depends on:** [workshop-coordination-ready](./01-0005-workshop-coordination-ready.md)
  (verified Workshop coordination and review capability)
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

Each recipient's accepted installation precedes its development. Workshop
readiness is already a prerequisite of those installation assignments. The
reachable Cabinet provider and controlled fixture setup precede actual native
integration proof; client development can proceed against the agreed contract.
Publication can precede execution eligibility and does not finish this outcome.

The [2026-10-06 environment check](../current-system.md#cabinet-public-schedule-environments--checked-2026-10-06)
identifies `https://staging.xuanxue.su` as the native test provider and links its
runtime evidence and existing staff fixture controls. The latest check also
confirms the public route on production at `fc2dee2`. Required-data validation
and actual native refresh evidence are outstanding; fixture writes belong to
Cabinet's authorized operator.

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
- [ ] Cabinet's public provider and protected-route regression evidence satisfies
  the shared agreement; reviewed evidence identifies reachable setup/runtime and deployment limits.
- [ ] Daychi's pilot satisfies the consumer cases and preserves ordinary schedule,
  cache, selections, access credentials and OS reminders.
- [ ] Actual native-to-provider evidence demonstrates dated results, controlled
  reschedule/cancellation, failed-refresh retention and recovery, with reproducible
  environment and revision references; mock-only results are insufficient.
- [ ] Workshop reviews each contribution, records verified capability and remaining
  migration scope, publishes reconciled records and acknowledges accepted evidence
  in the original issues.
- [ ] /verify confirms this ticket's complete outcome against the governing
  contract, contribution evidence and Workshop records.

## Out of scope

Broader account/reminder migration, authentication integration and schedule-source
cutover remain in [migration changes](../migration-changes.md). Gateway and backend
consolidation retain their deferred scope. Later assignment pairs require their
own scope authorization.
