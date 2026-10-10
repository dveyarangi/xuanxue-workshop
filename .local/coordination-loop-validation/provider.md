## Recipient and outcome

Recipient: xuanxue-cabinet (`project:cabinet`). Cabinet supplies the school's public dated schedule through `GET /api/public/lessons`, with the agreed complete-window response, public projection and error behavior. Native Daychi is the new consumer; the existing Cabinet student client remains supported.

## Execution dependencies

- Workshop acceptance of [cabinet-workshop-collaboration #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1). That installation assignment already depends on Workshop coordination readiness; readiness is a transitive prerequisite here.

This assignment is blocked while that prerequisite lacks Workshop's acceptance acknowledgement. Once it is satisfied, Cabinet may select and execute this assigned work under its own operator. No separate `Ready` status change or new Workshop release approval is required by this assignment. Publication does not certify installation or deploy the API.

## Expected / observed

Cabinet source baseline: `628314472aa2752ebb2bbe9ab75ac3dea9791719`. Workshop inspected the existing protected student route, route map, DTOs, lesson/class reads and error handling at that revision.

| Boundary | Expected | Observed delta |
|---|---|---|
| Public schedule | Unauthenticated, explicitly allowlisted public lessons; count mode or a complete bounded window | Existing `/api/me/lessons` is authenticated, includes protected Zoom fields, has no per-item `classId`, and returns upcoming count results. The staff window's cap and silent omission of missing class metadata cannot satisfy the new public window. No public-route implementation evidence has been accepted. |

The existing endpoint's authentication remains appropriate. The new public route is additive.

## Shared contract and conformance

Authority: [Public lessons contract and common conformance cases](contract-e209d272.md).


That single reference defines both query modes, strict validation, exact response fields and identity meanings, complete-window guarantees, refresh behavior, errors, compatibility and common examples. Cabinet owns executable definitions implementing it; Daychi consumes the same agreement. Report the executable-definition revision as well as this Workshop contract revision.

This endpoint intentionally publishes only the public schedule. It does not return Zoom links, Zoom passwords or authentication credentials, and supplying a session does not broaden its response. The existing authenticated student endpoint retains its protected behavior. Public schedule access is an accepted boundary requirement; it does not publish authenticated lesson-access details.

## Impact and required changes

- Implement the additive public GET using Cabinet's existing route, query, validation and error conventions. Use an explicit response allowlist; making the existing student mapper public is insufficient.
- Return the agreed bare array with per-occurrence `id` and per-item `classId`. Preserve stable occurrence identities through moves and cancellation. Include cancelled lessons and sort by start; equal-start ordering remains unspecified.
- Supply count mode with default 10 and limit 1–50. Supply the complete half-open window, up to 28 UTC days, without a current-time filter, row cap or pagination. Reject invalid, unknown and repeated query parameters as defined by the shared contract.
- Produce the entire selected result or an error. Missing required class metadata or malformed required data must not silently remove a lesson.
- Preserve protected student access and projection, existing web consumers and all account/reminder behavior. No authentication integration, new background polling, gateway, migration cutover or content consolidation is requested.
- Provide a reproducible provider environment that a native Daychi device/emulator can reach: API origin, setup commands, executable-definition/provider revision and environment limitations. A disposable development provider is sufficient.
- Coordinate controlled fixture creation, reschedule and cancellation through Cabinet's responsible operator for Daychi's integration demonstration. Daychi remains a read-only consumer; this assignment adds no public mutation or clock-setting API. Implementation and operational ownership remain Cabinet's.

Paired consumer assignment: [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6). Its actual native integration proof depends on the reachable provider, executable definitions and controlled fixture setup supplied here.

## Acceptance evidence

Report in **this issue**:

1. Code commit/PR and executable-definition references; checks run and their results against every applicable common conformance case at the shared reference. Include the 201-row complete window, count limits, interval edges, strict invalid queries, moves/cancellation, missing metadata and existing error shapes.
2. Anonymous and session-bearing requests proving that Zoom/credential and other non-allowlisted fields stay absent; protected student regression results.
3. Reachable API origin, provider/runtime revision, reproducible setup, controlled fixture procedure and deployment status. Distinguish tests, running development capability and production deployment.
4. Affected boundary/instruction changes and remaining limitations. Keep project implementation choices within Cabinet; bring an incompatibility with the shared agreement back here before changing that agreement.

Cabinet's provider contribution is independently reviewable. Daychi's actual native integration proof is required to finish the combined connection, rather than to misclassify provider-only completion as a completed end-to-end migration.

## Reconciliation and communication

Use this original assignment for questions, blockers, completion evidence and Workshop's review/acknowledgement. Workshop reviews the claimed criteria, reconciles current implementation and remaining migration records, then acknowledges accepted evidence here and closes accepted work. Incomplete evidence receives a concrete follow-up here. Closing the issue alone does not establish acceptance. Do not create a separate success or acknowledgement issue.
