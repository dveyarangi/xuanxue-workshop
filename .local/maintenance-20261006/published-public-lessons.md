# Public lessons contract

Consolidated 2026-10-05 from the user's accepted
[first schedule connection](../boundaries.md#accepted-first-schedule-connection).
This is the maintained target definition and common conformance reference.
It preserves the accepted agreement; consolidation does not require voting on it
again. Current implementation/deployment evidence belongs in
[current-system](../current-system.md), separately from these promises.

Cabinet source baseline: `628314472aa2752ebb2bbe9ab75ac3dea9791719`;
Daychi source baseline: `5f9ba442e04cd5dfa70527b9e670b491c491888c`.
The field meanings and strict validation conventions were checked against those
sources and Cabinet's installed validation libraries. A new route's conformance
still requires implementation evidence; source conventions alone do not prove it.

## Authority and scope

Cabinet owns the school's dated lessons and class metadata and supplies the API.
Native Daychi consumes this public, read-only schedule in its staged pilot path.
Workshop owns the shared agreement, addressed assignments, result review and
evidenced boundary records. Cabinet authors executable route, query and response
definitions; internal provider/client implementation and presentation remain with
their respective projects.

The pilot displays Cabinet's complete dated schedule for fourteen school calendar
dates and reflects moves and cancellations on refresh. It preserves ordinary
Daychi schedule, cache, selections and OS reminders and the protected Cabinet
student route. Source cutover, accounts, authentication integration, shared
reminder preferences, native push, new background polling, gateway and backend
consolidation are outside this slice.

## Operation, transport and request

- External operation: `GET /api/public/lessons`, relative to the configured Cabinet
  API origin. Cabinet's shared route-map key is `GET /public/lessons`; application
  setup supplies `/api`.
- No request body, credential or custom header is required. Success and API errors
  use JSON objects/arrays with UTF-8 strings and `application/json` media type.
  Standard URL encoding applies; an offset's literal `+` must be encoded as `%2B`.
- The origin is environment configuration, not a new routing service. Integration
  evidence records the actual scheme/host/port and provider revision. A native
  device or emulator must be able to reach that origin.
- Supported query parameters are `limit`, `from`, `to`, each at most once. There
  are no class, status, tag, user, cursor or pagination parameters. Unknown,
  repeated or structurally invalid parameters fail with 400 `invalid_input`.
  This retains Cabinet's strict DTO validation convention.

| Retrieval mode | Query | Meaning |
|---|---|---|
| Count | Neither `from` nor `to`; optional `limit` | Upcoming lessons with `startsAt >=` provider current time, at most the selected limit. Default 10. |
| Complete window | Both `from` and `to`; no `limit` | All dated lessons with `from <= startsAt < to`; no current-time filter, row cap or pagination. |

`limit` is a numeric query value converting to an integer 1–50, following Cabinet's
existing numeric transformation and integer validation. Empty, nonnumeric,
noninteger or out-of-range values fail. Daychi sends ordinary decimal integers
when using count mode. There is no request parameter to set the provider clock.

`from` and `to` are valid ISO 8601 date-times with explicit `Z` or numeric offset
(`+HH:mm`, `-HH:mm`, `+HHmm` or `-HHmm`). Instants normalize to UTC before
comparison. Require `to > from` and `to <= from + 4 weeks` in UTC (28 days).
One bound alone, a date/time without an offset, invalid bounds, or a window mixed
with `limit` fails with 400 `invalid_input`. Window membership is by current start,
not duration overlap. A lesson ending within the window but starting before it
is excluded; one starting before `to` and ending after it is included.

Daychi requests local midnight today in `Asia/Jerusalem` through local midnight
fourteen calendar dates later. Each bound uses its own date's timezone offset.
This includes earlier lessons today and can span 335 or 337 hours at offset
changes rather than exactly 336. Other callers need not use midnight bounds.

## Success response and field meanings

HTTP 200 with a bare array. Each item has exactly this public projection, using
the accepted Cabinet student fields plus `classId`. No field below is nullable;
only `location` is optional and omitted when absent. Empty strings and empty
arrays retain their ordinary values rather than meaning a missing item.

| Field | JSON type | Meaning |
|---|---|---|
| `id` | string | Cabinet dated lesson identity, encoded unchanged as the existing lesson ObjectId string. |
| `classId` | string | Cabinet class identity, encoded as its ObjectId string; multiple lessons can share it. |
| `startsAt` | string | Current start as ISO 8601 UTC with `Z`, using Cabinet's existing date serialization. |
| `durationMin` | number | Lesson duration in minutes, as in the existing student DTO. |
| `classTitle` | string | Current class title. |
| `groupLabel` | string | Current class group label. |
| `format` | string enum | `online`, `offline`, `both`. |
| `location` | optional string | Class location; omitted when absent. |
| `topic` | string | Dated lesson topic. |
| `status` | string enum | `scheduled`, `cancelled`. |
| `tags` | array of strings | Public lesson tags; missing legacy tags produce `[]`. |

Both IDs are nonempty, case-sensitive opaque values for the consumer. Their scope
is the configured Cabinet data environment; no cross-environment identity promise
is made. One occurrence appears at most once in a response. Its ID survives a
change in start time or cancellation. Daychi does not derive IDs from dates,
titles or weekly school-template series. `classId` is a relationship on each
item, not a user subscription list.

Return both scheduled and cancelled matching lessons. Use ascending `startsAt`
order, following Cabinet's existing schedule convention. The existing query
does not specify an equal-start tie order:
equal-start ordering is unspecified; count mode may select any tied occurrence
at its limit. Daychi may choose presentation order but must not rely on provider
tie order. No additional ID ordering requirement is introduced.

The public projection is an explicit field allowlist. It excludes Zoom links,
Zoom passwords, all authentication credentials, staff-only fields, recordings,
planner metadata and any other fields outside the table. A supplied session does
not broaden the projection. The existing protected student route retains its
protected behavior. This explanation belongs in the original Cabinet assignment.

## State, refresh and effects

Each request retrieves Cabinet's current matching lessons; each successful
complete-window result becomes the pilot's displayed result for those dates.
A move within the window updates the same occurrence. A move outside it removes
that occurrence from the displayed window. A cancellation remains represented
by its status while its current start remains in the window. HTTP 200 `[]` clears
the previous displayed list. These are already accepted refresh semantics.

Consistency follows ordinary Cabinet current-state reads. The accepted array
shape has no snapshot envelope or revision token, so the caller cannot request a
frozen revision across separate reads. This contract adds no transaction,
delta/tombstone stream or push requirement. A later successful refresh receives
later data. Missing required metadata must still fail the request rather than
silently omit a lesson. The existing provider queries lessons and classes
separately; implementing the agreed data guarantees remains Cabinet's task.

GET changes no account, lesson, class or reminder state. Repeating the read is
permitted, subject to Cabinet's existing throttling. The pilot does not merge
school-template, Telegram-correction or demo rows into Cabinet results. It does
not substitute for the ordinary Daychi loader or its cache/reminder flow. Internal
storage of the pilot's previous result and UI presentation remain Daychi's.

## Failures and recovery

API-origin errors use Cabinet's existing `ApiErrorBody`:

| Field | JSON type | Meaning |
|---|---|---|
| `statusCode` | number | HTTP status, equal to the response status. |
| `code` | string | Cabinet machine-readable error code. |
| `message` | string | User-facing error explanation; no private fields or raw internal exception data. |
| `details` | optional array of strings | Validation details for `invalid_input`; omitted otherwise. |
| `requestId` | optional string | Diagnostic request identifier, when supplied. |

| Condition | HTTP/code |
|---|---|
| Invalid query | 400 / `invalid_input` |
| Missing/malformed required source data or unexpected provider failure | 500 / `internal_error` |
| Explicit service unavailability | 503 / `not_available` |
| Existing throttle refusal | 429 / `rate_limited` |

No partial array is returned on failed production of the selected result. Network
failures and intermediary failures may have no Cabinet JSON error body. Daychi
treats any non-200 response, failed transport, or malformed success array/item as
a failed refresh; HTTP 200 `[]` alone means an empty successful result. It retains
the prior successful Cabinet result and exposes failure. With no prior result it
shows unavailable. These failures do not alter ordinary Daychi state.

400 requires correcting the request; 5xx/transport failure can be retried by a
later user refresh; 429 requires waiting. No automatic retry schedule or new
background polling is part of the contract. Failure messages and diagnostic
details contain no private schedule-access fields.

## Common examples

Window request (plus signs URL encoded):

```text
GET /api/public/lessons?from=2026-10-05T00:00:00%2B03:00&to=2026-10-19T00:00:00%2B03:00
```

The UTC bounds are `2026-10-04T21:00:00Z` inclusive and
`2026-10-18T21:00:00Z` exclusive. Provider current time does not narrow this
window. A response item can be:

```json
{
  "id": "000000000000000000000003",
  "classId": "100000000000000000000001",
  "startsAt": "2026-10-05T15:00:00.000Z",
  "durationMin": 60,
  "classTitle": "Tai chi",
  "groupLabel": "School",
  "format": "both",
  "topic": "Practice",
  "status": "scheduled",
  "tags": []
}
```

`location` is omitted here. Adding it as a string is valid; adding a Zoom or
credential field is not. The item represents 18:00 school time on that date.

Fixed boundary fixture, all with valid class metadata:

| Lesson ID suffix | UTC start | Expected in that window |
|---|---|---|
| `001` | `2026-10-04T20:59:59Z` | Excluded even if its duration overlaps the window. |
| `002` | `2026-10-04T21:00:00Z` | Included. |
| `003` | `2026-10-05T15:00:00Z` | Included. |
| `004` | `2026-10-06T16:00:00Z` | Included with `cancelled` status. |
| `005` | `2026-10-18T20:59:59Z` | Included even if its duration ends after the window. |
| `006` | `2026-10-18T21:00:00Z` | Excluded. |

Use full IDs `000000000000000000000001` through `000000000000000000000006`;
the initial expected sequence is `002`, `003`, `004`, `005`. Move `003` to
`2026-10-07T15:00:00Z`: it retains its ID, follows `004` in start order, and its
old time is absent. Move it to `2026-10-20T15:00:00Z`: it is absent from the window.
Cancel `005`: it remains in the response with the same ID and cancelled status.

Offset-change example: the fourteen school dates beginning `2024-10-20` use
`from=2024-10-20T00:00:00+03:00` and `to=2024-11-03T00:00:00+02:00`.
Those bounds normalize to `2024-10-19T21:00:00Z` and `2024-11-02T22:00:00Z`:
337 hours while still covering fourteen calendar dates. The host's Israel
timezone data confirms both offsets. No historical-data deployment is required
to run the deterministic timezone check.

## Common conformance and acceptance evidence

Both recipients use these cases; internal test tools remain project-owned.

1. Validate the exact public fields/types/enums, omitted location, empty tags,
   same-class relationships, unique occurrence IDs and UTC serialization.
2. With 201 distinct valid lessons in a supported window, return all 201. Count
   fixtures freeze the provider clock and check default 10, limit 1 and limit 50,
   inclusion exactly at current time, and exclusion before it. There is no
   production clock-setting API.
3. Check the concrete interval fixture and fourteen-date offset-change example
   above, including an earlier lesson on today's date and different offset
   representations of the same bounds.
4. Check within-window move, move outside window, cancellation, successful empty
   replacement and successful refresh after a failed one.
5. Reject half windows, mixed modes, malformed or offset-free date-times,
   nonpositive span, more than 28 UTC days, invalid limits, duplicate query keys
   and unsupported parameters. Exactly 28 days is supported.
6. Fail on missing required class metadata or malformed required lesson data;
   never silently omit an occurrence. Check existing 400/429/500/503 error shapes
   where emitted and failed transport/malformed success without an API error body.
7. Prove public projection with no session and with a session: class- and
   occurrence-level Zoom data remain absent, alongside credentials and other
   non-allowlisted fields. The public route requires no login.
8. Prove failed refresh retains the previous pilot result and an initial failure
   shows unavailable. Ordinary Daychi cache, selections and OS reminders remain
   unaffected by successful and failed pilot reads.
9. Verify existing Cabinet protected student access/projection and ordinary
   Daychi schedule and reminder behavior are preserved.
10. Demonstrate a native Daychi device/emulator reaching the actual Cabinet
    provider, showing dated data, a reschedule/cancellation after refresh, failure
    retention and recovery. Fixture-only UI is insufficient. Record contract,
    provider/client commit references, API origin, platform/runtime, steps,
    observed results and deployment status. A disposable development provider is
    sufficient for integration proof; do not claim production deployment from it.

## Revision, publication and compatibility

This maintained record and its common examples define one shared agreement.
Both project assignments cite the exact same commit-bound GitHub file URL.
A branch/HEAD link or an unpublished local review artifact is not the
implementation authority. The authored executable definitions land in
Cabinet and implement that fixed agreement; Daychi consumes it without an
independent schema choice. Report the executable-definition revision in evidence.

The public route is additive; existing protected route shapes and behavior are
preserved. Assignment changes affecting agreed shared behavior return to Workshop
alignment. Project autonomy follows
[contract evolution](../agent-contract.md#contract-evolution): a new
coexisting version can be introduced while the active contract remains fulfilled.
An incompatible replacement is coordinated before implementation; the old version
is retired only after all known consumers confirm transition. Source commits can
differ while satisfying the same fixed assignment contract. Deployment is reported
separately from source conformance.

The [agent interaction contract](../agent-contract.md#exchange-through-github-issues)
owns publication/release responsibilities, execution dependencies, original-issue
communication and evidence acceptance. This record defines the shared wire
contract and common acceptance outcomes; it does not authorize implementation or
claim deployed behavior.

