# Account reminder synchronization proposal

Prepared 2026-10-19 for [original request 17](https://github.com/dveyarangi/xuanxue-workshop/issues/17).
Status: proposed, neither an accepted contract nor an implementation assignment.
The [source comparison](../current-system.md#reminder-synchronization-source-comparison---2026-10-19)
records the inspected revisions and current gaps. The user confirmed on
2026-10-19 that Daychi has only test users/data; this is migration evidence,
not authorization to delete those data.

## Fixed requirements and open decisions

The accepted [selection, offline editing, lead-time and delivery agreements](../boundaries.md#accepted-reminder-selections)
remain authoritative: Cabinet account ownership; stable lesson occurrences and
recurring class choices; independent latest-edit reconciliation; Cabinet wins
equal-time conflicts; removals participate; offline edits survive failures;
explicit sign-out discards unsynced account edits; lead time is school default
or 0/15/30/60/120 minutes. Native delivery uses local OS reminders and existing
refresh occasions. Per-date skips are removed; cross-client duplicates are allowed.
The [native account-session contract](native-account-session.md) remains unchanged.

The proposal below makes the unresolved choices concrete. In dependency order:
individual-choice writes and the breaking legacy-write transition; edit clocks
and their accuracy limit; initial guest/account separation; the exact wire and
delivery bounds. None is accepted by preparation or by the dated test-data fact.

<straw-dog question="q-0002.0007.0002">

## Authority, identity and selection meaning

Cabinet owns account state. Cabinet web and native Daychi read and edit that same
state directly at the matching Cabinet issuer; no Daychi server or device is an
additional account authority. Browser and native clients use the existing production
and staging profiles, with separate credentials, caches and pending edits.

A class choice is keyed by Cabinet class ID; an individual choice by Cabinet
lesson ID. Clients treat IDs as opaque, case-sensitive strings. A lesson retains
its selection when moved, including outside the current schedule window. A
class choice includes its scheduled future occurrences without a client-local
subscription start date. A cancellation suppresses delivery without deleting the
selection; restoring the same occurrence restores eligibility. Missing calendar
rows do not constitute deselection. IDs are never reconstructed from names,
weekdays, times, legacy hashes or calendar dates.

Retain Cabinet's `scopeMode` (`all` or `selected`), including its existing `all`
default and remembered class list while `all` is active. Reminder eligibility is
the union of individually selected lessons and the recurring scope: every class
in `all`, or selected class IDs in `selected`. Turning an individual lesson off
removes only that explicit selection; it does not suppress a recurring reminder.
There are no negative per-date exceptions. Devices may present these choices
differently, while consuming the same account meaning.

The individual-lesson extension affects lesson reminders only. Existing Cabinet
class-scoped cancellation, recording and material notifications retain their
existing scope and notification-kind preferences. Device notification permission
and local delivery enablement remain device settings. No access entitlement,
attendance record, reservation or teacher notification is created by a selection.

## Operations and access

Both operations use HTTPS at `/api/me/notifications/lessons/sync`, with no query
parameters: `GET` reads a complete snapshot; `PATCH` submits individual edits and
returns their resolutions with a complete snapshot. JSON is UTF-8 with media
type `application/json`. Responses carry `Cache-Control: no-store`; no shared
cache, redirect, conditional GET or delta protocol is introduced.

Native requests use `Authorization: Bearer <existing Cabinet native credential>`
and no browser cookies. Cabinet validates the current native grant, account and
revocation state on each request. Browser requests use the matching existing
Cabinet session cookie; PATCH also requires Cabinet's nonempty
`X-Requested-With` CSRF header. Supplying both a native bearer and an active
browser session is rejected with 400 `ambiguous_credentials`. Native responses
do not create browser sessions. Browser renewal retains its existing behavior.
No request accepts a user/account ID that selects another account. Operations
are available to an authenticated, unblocked account without an additional role;
delivery still respects existing channel and notification-kind preferences.

Production uses `https://xuanxue.su`; staging uses
`https://staging.xuanxue.su`. Native credential handling remains within the
existing account-session owner, rather than exposing stored tokens to schedule
components. These routes add no content-check budget or new authentication
protocol. Existing general API abuse limits apply; 429 is a recoverable response,
not a promised per-grant capacity. Account data and credentials stay out of URLs,
public schedule responses and logs.

## Wire version 1

A snapshot is an object with these required fields, and no unspecified fields:

| Field | Type and meaning |
|---|---|
| `version` | Integer `1`. Unsupported versions are rejected, never guessed. |
| `accountId` | Current Cabinet account's opaque ID. |
| `revision` | Canonical nonnegative decimal string, monotonically increasing for changes to this account's synchronization state. |
| `serverTime` | Cabinet UTC time when composing the response, `YYYY-MM-DDTHH:mm:ss.SSSZ`. |
| `scopeMode` | Register `{value: "all"\|"selected", editedAt: timestamp\|null}`. |
| `scopeChosen` | Existing sticky boolean indicating an explicitly chosen scope; false for an untouched default. |
| `classSelections` | Complete array of `{id: string, editedAt: timestamp}` for positive recurring choices, sorted lexicographically by ID. |
| `lessonSelections` | Complete array of `{id: string, editedAt: timestamp}` for positive individual choices, sorted lexicographically by ID. |
| `leadTime` | Register `{value: 0\|15\|30\|60\|120\|null, editedAt: timestamp\|null}`; null means school default. |
| `schoolMinutes` | Current school default integer minutes, preserving Cabinet's existing 5..1440 range rather than limiting it to personal presets. |
| `classes` | Existing public-safe `LessonScopeClassDto[]`, sorted by ID, for Cabinet's selectable class catalogue; no meeting links or private account data. |

`revision` does not version school settings, class metadata or schedule rows;
those remain authoritative in each fresh response/source. Account registers and
selections are transactionally consistent. `serverTime` is not an edit time.
An untouched register has `editedAt: null`, older than every real edit. Explicit
school-default selection is `value: null` with a real timestamp. Positive
selection entries always have a real timestamp. An absent selection is false;
its removal timestamp remains on Cabinet, even though it is omitted from the
positive array. Missing class metadata never deletes the associated selection.
Empty arrays are a complete empty selection, not a failed or partial read.
There is no pagination or silent truncation of account state.

PATCH body is `{version: 1, edits: Edit[]}`. An edit is exactly one of:

```json
{"kind":"scope","value":"selected","editedAt":"2026-10-19T10:00:00.000Z"}
```
```json
{"kind":"class","id":"507f1f77bcf86cd799439011","value":true,"editedAt":"2026-10-19T10:00:01.000Z"}
```
```json
{"kind":"lesson","id":"507f1f77bcf86cd799439012","value":false,"editedAt":"2026-10-19T10:00:02.000Z"}
```
```json
{"kind":"lead","value":null,"editedAt":"2026-10-19T10:00:03.000Z"}
```

`scope` and `lead` edits have no `id`; selection edits require `id` and boolean
`value`. All timestamps are valid Gregorian UTC instants with exactly three
fractional digits and `Z`; local dates, offsets and numeric epoch values are not
accepted. No field is optional, except that `id` is absent for the two scalar
kinds. Unknown fields and duplicate keys in JSON objects are invalid. Unknown
kinds, null selections, unsupported lead values and duplicate edited keys in one
batch are invalid. A key is `(kind,id)` or just `kind` for scalar registers.

One request contains 1..64 distinct keys and at most 128 KiB of uncompressed JSON.
Clients split larger queues without sending multiple edits for the same key.
Cabinet validates IDs against its canonical ID encoding and existence on an add;
inactive but existing classes are permitted as today. Removing an unknown or
deleted ID is permitted and retains a tombstone, so cleanup is not blocked by
catalogue retirement. At most 50 positive class choices remain, preserving the
existing Cabinet bound. A merge exceeding that bound is rejected atomically.
No additional numerical cap is introduced for individual lesson choices; they
remain selected across window boundaries and are not deleted merely for age.

GET returns the snapshot. PATCH returns
`{snapshot: Snapshot, resolutions: Resolution[]}`. There is one resolution in
request order for every edit: `{edit: Edit, current: {value, editedAt}}`, where
`edit` echoes the exact submitted edit and `current` is Cabinet's resolved value
and timestamp for that key at the returned snapshot. `current.editedAt` can be
null only for an untouched default. A losing edit is a successful resolution,
not an HTTP failure. Selection false values appear in resolutions even though
they are absent from snapshot positive arrays.

For an account with no selectable classes or existing edits, PATCH
`{"version":1,"edits":[{"kind":"lead","value":0,"editedAt":"2026-10-19T10:00:00.000Z"}]}`
has this successful response (the revision is illustrative):

```json
{
  "snapshot": {
    "version": 1,
    "accountId": "507f1f77bcf86cd799439010",
    "revision": "1",
    "serverTime": "2026-10-19T10:00:01.000Z",
    "scopeMode": {"value":"all","editedAt":null},
    "scopeChosen": false,
    "classSelections": [],
    "lessonSelections": [],
    "leadTime": {"value":0,"editedAt":"2026-10-19T10:00:00.000Z"},
    "schoolMinutes": 45,
    "classes": []
  },
  "resolutions": [{
    "edit": {"kind":"lead","value":0,"editedAt":"2026-10-19T10:00:00.000Z"},
    "current": {"value":0,"editedAt":"2026-10-19T10:00:00.000Z"}
  }]
}
```

## Ordering, removals and retries

Each key has an independently ordered value and edit time. A strictly newer
timestamp replaces its stored value; an older or equal timestamp keeps Cabinet's
stored value. This includes false selections, selecting the school default and
an edit that repeats the current value. Such a newer no-op advances that key's
timestamp, preventing an older opposite edit from winning later. The untouched
default is older than a submitted real edit.

Cabinet validates the whole batch, then merges all keys atomically against current
state. It increments the account revision once if any stored value or timestamp
changes; otherwise the revision stays unchanged. No snapshot precondition rejects
independent edits simply because some other key changed. False-value tombstones
remain for the account lifetime, through late requests, ordinary refreshes and
retries. Deleting the account removes its state under existing account policy.
No operation-ID ledger, event bus or cross-device notification lock is needed.

Clients retain the latest local edit per key durably before treating it as saved
offline. They overlay pending edits on fetched state. A successful PATCH can clear
only the exact key, timestamp and value it submitted, after its resolution is
durably applied; a newer edit made while the request was in flight survives.
Lost responses are retried with the same edit timestamps and values. The merge
is idempotent. Late snapshots cannot regress account state: clients fence them
by issuer, account ID, session generation and revision, while still consuming
matching resolutions without deleting newer pending edits. Equal revisions do
not freeze school settings or calendar metadata. Malformed or incomplete replies
are failures and leave the last good snapshot and queue intact.

## Proposed edit clock and its limitation

Clients timestamp the user's action, not transmission or retry. They calibrate
UTC against the latest successful Cabinet `serverTime` and elapsed monotonic
time while that clock is available. After restart without a new calibration they
use device UTC plus the last known offset. Each key advances strictly beyond its
last known local or Cabinet timestamp, by at least one millisecond. Cabinet web
uses the same edit format and clock policy. A retry never obtains a new edit time.

Cabinet rejects the entire batch if any edit is more than five minutes beyond
Cabinet's current UTC, with 409 `clock_out_of_range`. It does not silently clamp
or restamp it. Old timestamps have no age cutoff: offline delivery may be delayed
indefinitely. A rejected future edit remains pending; synchronization resumes after
clock correction and the time becomes admissible, or a new explicit user edit
supersedes it. Clock errors never erase the queue or trigger sign-out.

This supplies deterministic latest-timestamp ordering, not proof of physical
action order across offline devices with inaccurate clocks. Even under the five
minute limit, skew can select the earlier physical action. Perfect real-time
ordering while offline cannot be established from these clients' clocks. This
accuracy tradeoff requires acceptance; receipt-time ordering would change the
already accepted latest-edit policy. No HLC/vector-clock scheme is proposed.

## Failure behavior

Failures use Cabinet's envelope
`{statusCode: number, code: string, message: string, requestId?: string}`. Messages
are human-readable, not machine discriminators. No error includes credentials.
Validation or authorization failures perform no writes, including on retries.

| HTTP/code | Meaning and client behavior |
|---|---|
| 400 `invalid_input` / `ambiguous_credentials` | Invalid shape, ID/add target or credentials combination; preserve queued edits and surface the failure, without endless automatic retries. |
| 401 `unauthorized` | Missing/invalid/revoked native or browser credential; apply the existing session lifecycle, preserve pending reminder intent isolated to that issuer/account, resume only after that same account authenticates. |
| 403 `forbidden` | Account refused/blocked; retain account-isolated queue without attempting to bypass refusal. |
| 409 `clock_out_of_range` | Future timestamp outside the proposed bound; retain queue as above. |
| 409 `selection_limit` | The merged positive class list would exceed 50; retain edits and require a deliberate selection correction. |
| 409 `sync_upgrade_required` | Retired full-list write attempted; no write, require a current client. |
| 413 `payload_too_large` | Over body bound; split a valid queue, retain intent. |
| 415 `unsupported_media_type` | Wrong media type; correct the client, retain intent. |
| 429 / 5xx, network failure or invalid response | Retain queue, snapshot and active reminders; retry on existing refresh occasions, respecting `Retry-After` when supplied. No new background retry service. |

Unknown codes are failures, never empty state. 401 invalidation is not the user's
explicit sign-out. Automatic session loss cannot reuse an account queue under a
different account or issuer. The existing credential owner may clear an invalid
credential while reminder intent remains segregated until authentication recovers.

## Initial connection and delivery compatibility

On sign-in, Daychi fetches Cabinet account state and binds schedule identities to
Cabinet's authoritative public lesson/class IDs. Legacy guest selections and lead
time stay in a separate guest store and are not automatically uploaded. There is
no heuristic conversion or real-user legacy migration job. Guest operation remains
available signed out. Explicit sign-out discards that account's unsynced edits and
cancels its owned local reminders, then restores the prior guest state; it does
not delete accepted Cabinet state or guest data. Late replies cannot reverse this.
Signing into another profile/account never imports the previous account's queue.

Daychi's account-bound calendar uses the accepted Cabinet public schedule source
and school-time window; it does not reconcile Cabinet selections against the old
HTML timetable. Startup, foreground return and the existing five-minute foreground
refresh fetch account state and calendar without adding push/background polling.
Each source is accepted only when valid; a failed calendar refresh preserves its
last good rows and OS reminders. A received account edit can still change reminders
against those retained rows. No schedule absence is interpreted as deselection.

Effective lead time is personal value or current `schoolMinutes`, including values
such as school-default 45. Cabinet and Daychi add personal zero and 120 support
where missing. Cabinet's proposed zero-lead window is the first scheduler tick in
`[startsAt, startsAt + 60 seconds)`, with its existing account/lesson deduplication;
it makes no hard real-time delivery promise. Missed windows are not replayed as
fresh reminders. Daychi schedules zero at the start when preparing a future event,
and does not create an immediate catch-up for an already-started lesson.

Daychi's existing 60-pending-notification bound becomes an explicit rolling
coverage limit: reconcile the earliest 60 eligible future reminders, ordered by
fire time then lesson ID, within the existing calendar window. A larger plan
cannot reject the entire reconciliation or cancel all existing reminders. Refill
occurs at existing successful refresh/reconciliation occasions; no guarantee is
made for later reminders without a subsequent reconciliation. OS permission,
platform limits and suspended-app behavior remain delivery limitations. Each
project deduplicates its own account/lesson delivery; duplicates between Cabinet
and Daychi remain allowed.

## Breaking write transition

Preserve Cabinet's existing account values at the initial schema transition.
Seed timestamps of existing explicit scalar values and positive class choices
from that preference document's `updatedAt`; untouched defaults have null time.
This is a one-time compatibility baseline, not recovered historical edit timing.
The new timestamped writers begin only after this baseline is established.

Cabinet web switches to individual-choice PATCH before account synchronization
is enabled in Daychi. At that coordinated cutover, the old scope and reminder
PUT routes return 409 `sync_upgrade_required` without mutation. Existing GET
representation remains readable. An old browser tab therefore receives an
upgrade failure rather than silently overwriting newer choices. This is an
explicit breaking change to the old write interface. Keeping unrestricted old
PUT saves active cannot satisfy independent-choice reconciliation. Rollback may
disable new editing; it cannot re-enable unfenced old writers against shared state.

The version-1 shape is additive until activation; it neither activates unfinished
schedule integration nor changes content, browser-wiki or native-session contracts.
Implementation publication requires an accepted immutable contract, coordinated
writer transition and addressed contributions. Local source inspection or two
passing independent suites alone do not establish deployed joint behavior.

## Common conformance outcomes

| Case | Required observation |
|---|---|
| Different keys | Offline add A and online removal B both survive, regardless of arrival order. Lead-time edits do not overwrite either. |
| Same key | Newer edit wins; equal-time opposite edit retains Cabinet's value. A same-value newer edit still advances ordering. |
| Removal and replay | A delayed old add cannot resurrect a removed class or lesson, including after refresh and a lost response. |
| Retry and concurrent local action | Exact retry is idempotent; reply to an older submitted edit never clears a newer local edit on that key. |
| Concurrent writers | Two authenticated clients merge against current state atomically; a stale whole snapshot cannot erase another key. |
| Response ordering | Lower-revision account snapshots and previous-session replies cannot regress current state; changed school metadata remains refreshable at equal account revision. |
| Empty/default | Untouched all/default differs from selected-empty and explicitly chosen school default; a null lead edit participates in ordering. |
| Mode and union | Switching all/selected preserves remembered class choices; a false individual choice cannot suppress its recurring selection. |
| Identity and lifecycle | Moving a selected lesson across dates/windows retains its ID/choice; cancellation suppresses and restoration restores eligibility. |
| Clock | Exactly five minutes ahead is admissible; greater skew rejects the entire batch without losing pending edits; old offline timestamps have no expiry. |
| Isolation and logout | Production/staging and two accounts have isolated queues; explicit logout discards only that account's unsynced intent; automatic 401/network failure does not. |
| Guest transition | Sign-in starts from Cabinet, leaves guest data intact and uploads no legacy selections; sign-out restores guest state. |
| Validation and limits | Wrong type, duplicate key, unsupported version, unknown add ID, 65 edits or body overflow cannot partially mutate state; a 51st positive class fails atomically. |
| Authentication | Browser CSRF, native revocation/blocking, mixed credentials, cross-account input and no-store/exposure behavior meet the access section. |
| Lead and delivery | Personal 0 and 120 and school-default 45 work on both ends; zero follows the stated window, with no cross-client exclusivity promise. |
| Refresh failure | Cached schedule, pending edits and existing reminders survive failed reads; received moves/cancellations take effect on recovery. |
| More than 60 | Earliest 60 are retained/scheduled deterministically; the complete plan is not rejected; later coverage depends on existing refill occasions. |
| Old client | Old full-list PUT after cutover returns upgrade failure with no mutation; updated web and Daychi can edit the same account safely. |
| Other behavior | Non-reminder Cabinet notification preferences, legacy guest access/content, native credential lifecycle and browser flows remain compatible. |

## Ownership and acceptance evidence

Cabinet owns the new authenticated operations, validation, atomic merge/removal
retention, baseline and legacy-write fence, web writer adoption and backend
reminder eligibility/zero delivery. Daychi owns account/issuer-scoped durable
edits, authenticated transport integration, stable schedule identity, guest
separation, logout/late-response handling, removal of per-date skips and bounded
OS reconciliation. Its recipient context includes why skips are removed: opening
the app to avoid one notification is not useful; dismissal suffices, and no
teacher is informed or reserved place released.

Workshop owns alignment of the choices above, one immutable accepted reference,
coverage of the common cases and joint acceptance. These are ownership statements,
not a delivery breakdown or authorization to change recipient repositories.
Provider HTTP/concurrency checks and consumer persistence/clock/lifecycle cases
need exact source revisions and executed results. Joint staging evidence uses
an authorized matching account, actual Cabinet web and an identified installed
Daychi build: different-key offline edits, same-key conflict/tie, removal/retry,
move/cancellation recovery and logout/account isolation, plus observed OS reminders
for supported lead values and capacity behavior. Existing accepted native-account
proof is reused; it is not repeated as a separate gate. No arbitrary fixture
mutation, production release or cleanup is authorized by this proposal.

</straw-dog>
