# xuanxue-cabinet: provide the public schedule for the Daychi connection pilot

**Retired — unpublished draft, withdrawn at the user's request on 2026-10-05.**

Historical brief only. No recipient action is assigned. The shared contract was
incomplete; no implementation issue was published and no completion is claimed.
A future reconciliation must re-evaluate the scope and prepare a new complete pair.

<details>
<summary>Withdrawn review draft</summary>

**Recipient:** xuanxue-cabinet project agent under its operator.
**Recipient label:** `project:cabinet`.
**Status:** Planned. Execution awaits Workshop readiness, confirmed Cabinet
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

An unauthenticated Daychi native test client can retrieve a complete fourteen-day
Cabinet schedule without Zoom connection details. This is the provider half of
the first Cabinet–Daychi connection pilot.

## Expected / observed

The [target contract](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/boundaries.md#accepted-schedule-access)
accepts public schedule access without Zoom; count/date-window retrieval preserves
Cabinet web and supports Daychi's fourteen-day coverage. Workshop will identify the
governing revision before execution; HEAD links provide context, not release.

Source rechecked locally on 2026-10-05 at `628314472aa2752ebb2bbe9ab75ac3dea9791719`:
`shared/src/my-lessons-routes.ts` and `api/src/lessons/my-lessons.service.ts` expose
an authenticated count-limited upcoming list. `my-lesson.mapper.ts` includes Zoom
links/passwords. Making that route public without adapting its projection would
violate the accepted access rule. Existing dated lesson IDs, starts, duration and
status provide the starting point; no broad interface inventory is requested.

## Impact and required changes

Implement the narrow public read contract for a supported bounded fourteen-day
window, backed by Cabinet's existing dated lessons. Supply the identity, title,
time/duration and status needed for Daychi to display the actual occurrences;
the same lesson keeps its identity when its time changes. Omit Zoom links,
passwords and other private connection data in the server response, including
class-level defaults and lesson overrides. Preserve Cabinet's existing web
authentication, count behavior and protected responses.

Cabinet owns the authored home of the executable definitions and its internal
implementation. Routes, query names, window bounds, validation and the typed
schema must match the common immutable contract supplied in this issue before
publication. Implement that agreed definition and report conformance to its
common examples; the issue does not delegate contract selection. Reuse the
existing Cabinet model and checks; this is implementation of one provider path,
not a request to investigate the whole API. Return any new shared obligation to
Workshop rather than selecting it silently.

The paired Daychi issue refers to the identical contract revision. A reachable local or preview
service for an existing native Daychi target is enough for the joint pilot;
production deployment and browser-wide CORS support are not required here.
Provider availability precedes joint acceptance, not the recipient's preparation.

## Acceptance evidence

- [ ] No-session requests return the supported schedule without Zoom details;
  checks seed both class defaults and lesson overrides to prove absence on the wire.
- [ ] Window checks cover empty data, interval boundaries, cancelled lessons,
  rescheduling with stable identity and data exceeding the old count limit;
  a response described as complete is not silently truncated.
- [ ] The implementation conforms to the common pinned contract and examples
  used by Daychi, including exact window and data semantics; existing Cabinet
  web/count and authentication checks pass.
- [ ] Report the implementation revision/PR, checks and results, reachable test
  service and its running revision. Distinguish source, execution and deployment.
  Do not post credentials or private connection details in examples.
- [ ] The paired Daychi test reads actual Cabinet data. Workshop reviews both
  reports, updates the evidenced boundary state and acknowledges the pilot result.

No new sign-in, account synchronization, reminders, source cutover, content
migration, gateway or production rollout is assigned. Preserve the existing
project ownership and release workflow. Report blockers, executable definitions
and completion in this original issue using /collaborate; include any affected
instruction/summary revision or explain why the existing summary remains accurate.

</details>
