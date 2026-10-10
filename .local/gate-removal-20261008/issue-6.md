## Recipient and outcome

Recipient: daychi (`project:daychi`). Native Daychi displays Cabinet's valid available dated schedule for fourteen school calendar dates in the staged pilot, reflects reschedules/cancellation on refresh and preserves the ordinary schedule and reminder path.

## Execution dependencies

Daychi may implement this client under its operator against the accessible settled shared contract below. Workshop coordination readiness and acceptance of [installation #2](https://github.com/dveyarangi/xuanxue-workshop/issues/2) are not prerequisites. Planned/Ready wording adds no release approval.

Actual native integration proof requires a reachable conforming Cabinet provider and executable definitions, authorized controlled fixtures for moves, cancellation, corrupt-source omission and repair, and an actual native device/emulator. [Cabinet provider assignment #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5) supplies the provider evidence and operator-owned fixture procedure. Current verified provider evidence is listed below. Cabinet's contribution or a client mock suite alone does not complete the combined connection.

Workshop review reassesses dependency necessity and fulfillment from source, executed checks, runtime and operator evidence and updates this original issue when those facts change. Administrative gates were removed at the Workshop operator's direction on 2026-10-08.

## Expected / observed

Daychi source baseline: `5f9ba442e04cd5dfa70527b9e670b491c491888c`. Workshop inspected the schedule loader, schedule/cache/reminder flow, native pilot surfaces and access client at that revision.

| Boundary | Expected | Observed delta |
|---|---|---|
| Native Cabinet schedule pilot | Read the agreed public dated lessons from Cabinet; preserve ordinary client state | The ordinary loader uses Daychi's own schedule API/HTML and corrections, then writes schedule cache and OS reminders. Its behavior does not implement this Cabinet pilot. No actual native-to-Cabinet proof has been accepted. |

The ordinary schedule remains a supported path. This assignment adds the staged public pilot, rather than cutting over that loader or adding a login requirement.

## Shared contract and conformance

Authority: [Public lessons contract and common conformance cases](https://github.com/dveyarangi/xuanxue-workshop/blob/4aec5f84130c2dd8df6875c30fd94c3cf2a5ec74/docs/contracts/public-lessons.md).


That single reference defines the exact request, bare response array, fields and identities, bounded-window coverage, best-effort valid-only results and operator logging, refresh/error semantics, compatibility and common examples. Cabinet owns executable definitions; Daychi consumes them and reports their revision. Internal client structure and presentation remain Daychi's.

## Cabinet environments

The configured origin excludes `/api`; the operation is `GET /api/public/lessons`.

| Environment | Origin | Role and observed evidence |
|---|---|---|
| Staging | `https://staging.xuanxue.su` | Native pilot provider. Verified 2026-10-08 at approximately 05:14 UTC: health 200 at `868a4ed`, MongoDB up and a fourteen-day public window returning 63 valid public rows without Zoom fields. |
| Production | `https://xuanxue.su` | Production origin; health still reports `fc2dee2` in the same check. Amended malformed-row behavior is not verified on production. Production rollout belongs to Cabinet's operator. |

[Cabinet's provider report](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052693441), [merged PR #570](https://github.com/gregoryKot/xuanxue-cabinet/pull/570) and [successful merge CI](https://github.com/gregoryKot/xuanxue-cabinet/actions/runs/37729360044) supply inspectable executable-definition, omission/logging, validation and protected-route regression evidence. Workshop inspected source and check logs and [accepted that contribution](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6052988637). Healthy live samples alone do not prove corrupt-source behavior. These observations establish provider availability at the stated time, not the Daychi native demonstration.

Staging or a disposable development provider is sufficient for native proof. Record its current `/api/health` revision, origin, fixtures and native observations during the demonstration; identities belong to the selected data environment. Fixture authorization and execution remain with Cabinet's operator. The controlled mixed/corrupt/repair cases require disposable development/test data, never production.

[Daychi's installation acceptance](https://github.com/dveyarangi/xuanxue-workshop/issues/2#issuecomment-6052903501) records the verified installation result. It is separate from implementation eligibility.

## Controlled native test

Coordinate a dedicated one-off lesson in the selected integration environment with its authorized Cabinet operator. Staging or a disposable development provider is sufficient; the staging UI URL below is an example, not an additional deployment prerequisite. The operator creates it through **Занятия → Разовое занятие** at [`/planning/new`](https://staging.xuanxue.su/planning/new), selecting an existing class, start, duration and topic. At `/planning/{lessonId}`, the operator edits its start and uses **Отменить занятие** with confirmation; **Вернуть в расписание** restores it. Date/time inputs use the operator browser's local timezone and are converted to UTC.

The existing [staff lesson API](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/lessons.controller.ts) supports creation through `POST /api/lessons` and moves/cancellation through `PATCH /api/lessons/{id}`. Fixture writes belong to Cabinet's authorized operator; Daychi stays read-only.

Capture the fixture/class IDs and refresh results after creation, a move within the window, a move outside it, and cancellation inside it. Arrange operator access and timing for the demonstration. Provider conformance, including valid-only omission and error logs, is an integration dependency under [cabinet-public-lessons #5](https://github.com/dveyarangi/xuanxue-workshop/issues/5).

## Impact and required changes

- Read `GET /api/public/lessons` at the configured Cabinet API origin without a credential/custom-header requirement. Configure an origin reachable from the actual native device/emulator; no gateway or authentication integration is requested.
- Request local midnight today in `Asia/Jerusalem` through local midnight fourteen calendar dates later. Use each bound's actual offset, correctly URL encode it, and include earlier lessons today. There is no window row cap, including windows with more than 200 valid lessons. Individually malformed source records are omitted and logged by Cabinet; no completeness header, envelope or version selector is added.
- Interpret per-occurrence `id` as the stable opaque identity and `classId` as its class relationship. Do not derive IDs from titles/dates, add a separate class-ID subscription list, or depend on equal-start ordering.
- Display both scheduled and cancelled occurrences. A valid best-effort window read replaces the pilot's prior window with exactly its returned valid rows: moves retain identity, occurrences moved outside it disappear, and `200 []` clears it even when all selected rows were invalid. An empty response means no valid rows available, not proof that no source lessons exist. No completeness/partial-result state or new warning is required; do not merge older rows or infer reminder/account mutation from absent items.
- Reject malformed success data as a failed refresh. Any failed transport or non-200 result retains the previous successful Cabinet result and exposes failure; with no previous result, show unavailable. Recovery uses a later successful refresh. Do not represent an error as an empty successful schedule.
- Preserve the ordinary schedule, cache, selections, access credentials and OS reminders during successful and failed pilot reads. The ordinary loader's cache/reminder writes and access client's credential-clearing behavior must not leak into this public pilot.
- Do not merge school-template, Telegram-correction or demo rows into Cabinet results. No source cutover, account/reminder mutation, background polling, native push or backend consolidation belongs to this assignment.
- Coordinate controlled lesson changes with Cabinet's operator for the native demonstration. Daychi has read-only access; fixture mutations stay with the provider's responsible operator.

## Acceptance evidence

Report in **this issue**:

1. Client commit/PR, shared contract and Cabinet executable-definition revisions; checks and results for the applicable common conformance cases, including exact fields, fourteen school dates across an offset change, interval edges, uncapped valid results, stable move/cancellation, mixed-result replacement, all-invalid empty replacement and source-repair recovery, malformed success data, initial failure, retained prior result and recovery.
2. Regression evidence that ordinary schedule/cache/selections, access credentials and OS reminders remain intact after successful and failed pilot requests.
3. An actual native device/emulator reaching the actual Cabinet provider. Record API origin, provider/client revisions, platform/runtime, reproducible steps and observed dated data. Demonstrate reschedule/cancellation, a controlled mixed valid/invalid result, return of repaired records, failed refresh retention and recovery. Corrupt-source fixtures use disposable development/test data, never production. Mock-only or fixture-only UI does not finish this criterion. A disposable development provider is sufficient; report production deployment separately.
4. Affected boundary/instruction changes and remaining limitations. Keep implementation/presentation choices within Daychi; bring a conflict with the shared agreement back here before changing it.

Client implementation proceeds under Daychi's operator against the settled shared contract. Provider reachability and controlled fixture changes are additional dependencies of actual integration proof. A completed client mock suite alone does not finish the combined connection.

## Reconciliation and communication

Use this original assignment for questions, blockers, completion evidence and Workshop's review/acknowledgement. Workshop reviews the claimed criteria, reconciles provider/client implementation and remaining migration records, then acknowledges accepted evidence here and closes accepted work. Incomplete evidence receives a concrete follow-up here. Closing the issue alone does not establish acceptance. Do not create a separate success or acknowledgement issue.
