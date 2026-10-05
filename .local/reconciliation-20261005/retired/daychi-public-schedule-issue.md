# daychi: display the Cabinet public schedule in a native connection pilot

**Retired — unpublished draft, withdrawn at the user's request on 2026-10-05.**

Historical brief only. No recipient action is assigned. The shared contract was
incomplete; no implementation issue was published and no completion is claimed.
A future reconciliation must re-evaluate the scope and prepare a new complete pair.

<details>
<summary>Withdrawn review draft</summary>

**Recipient:** daychi project agent under its operator.
**Recipient label:** `project:daychi`.
**Status:** Planned. Execution awaits Workshop readiness, confirmed Daychi
onboarding and Workshop's identification of the readable pilot baseline here.

## Shared contract and conformance — publication blocked

The canonical pilot contract is incomplete. The exact window/time semantics,
request parameters, response schema and meanings, complete-window refresh
semantics, failure behavior, immutable reference and common conformance examples
must be agreed before this implementation issue can be published. Both recipient
issues must refer to that same complete definition; neither recipient chooses
these dimensions during implementation. The remaining text is a scope draft,
not permission to fill those gaps independently.

## Outcome

An opt-in native Daychi test path displays actual dated lessons from Cabinet's
public fourteen-day schedule, proving the first direct Cabinet–Daychi connection.
The pilot is read-only and does not replace the ordinary schedule/reminder flow.

## Expected / observed

The [target connections](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/boundaries.md#target-connections)
assign schedule provision to Cabinet. Public schedule responses omit Zoom and
date-window mode supports complete fourteen-day coverage. Workshop will identify
the governing pilot revision before execution; HEAD links do not release work.

Source rechecked locally on 2026-10-05 at `5f9ba442e04cd5dfa70527b9e670b491c491888c`:
`apps/practice-app/src/features/schedule/load.ts` races Daychi API with native
school HTML; `model.ts` requires a school-bound weekly snapshot; `zoom.ts` applies
timing corrections. `use-schedule.ts` writes fetched data to the ordinary cache
and reconciles local notifications. `attendance.ts` derives recurring identities
from school series/date IDs. Replacing only the URL would not prove this pilot
and would affect reminders. No broad client inventory is requested.

## Impact and required changes

Implement a small, explicitly selected native test path that requests Cabinet's
published public window contract and displays its actual occurrences, including
cancellations and received time changes. Reuse existing schedule presentation
where practical; Daychi owns the test entry, adapter and presentation. Consume
the common immutable contract revision supplied to both issues; data format,
request construction and interpretations follow it, not an independently chosen
schema or convention.

Keep the pilot data separate from ordinary schedule cache, attendance choices,
local OS notification reconciliation and private Zoom lookup. The public path
requires no credential. Cabinet times and IDs are authoritative within this path:
do not apply school-HTML corrections or rebuild its IDs from title/date.
Do not silently fall back to school HTML, the old Daychi API or sample data when
claiming a successful Cabinet read. A failed refresh must be distinguishable from
a successful read, and any retained pilot data must actually come from Cabinet.

Both issues already supply the same complete pinned contract at publication;
Cabinet's issue supplies its implementation and a reachable local/preview service.
Final interoperability proof requires that running provider and the shared
conformance cases; no independent Daychi contract design is assigned. One
existing native target is enough for the pilot; web support and production source
replacement belong to later work. No UI redesign or new background refresh is assigned.

## Acceptance evidence

- [ ] On an existing native test target, a no-session request to the identified
  Cabinet service displays its actual fourteen-day data; a stub-only run is insufficient.
- [ ] Request/response interpretation conforms to the exact contract revision and
  common examples used by Cabinet, including time/window and refresh semantics.
- [ ] A known Cabinet lesson appears with the correct time/status and retained
  identity; after an operator changes its time or cancels it, refresh reflects that
  change. Report both build/service revisions and reproducible steps.
- [ ] Empty, invalid and unavailable-provider cases are checked; the pilot never
  presents another source as Cabinet or applies school timing corrections.
- [ ] Tests show the pilot does not write ordinary preferences/cache, invoke
  private Zoom lookup or schedule/cancel normal OS reminders. Returning to ordinary
  use preserves its prior behavior and data.
- [ ] Report implementation/PR references, checks and results, test target and
  limits. Workshop verifies the paired evidence, updates its current boundary
  record and acknowledges the pilot, without claiming full migration or deployment.

No shared sign-in, account reminders, skip removal, HTML-source removal, content
admission change, gateway or production rollout is assigned. Report blockers and
results in this original issue using /collaborate; include any affected local
instruction/summary revision or explain why the existing summary remains accurate.

</details>
