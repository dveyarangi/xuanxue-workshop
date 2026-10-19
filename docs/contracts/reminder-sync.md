# Account reminder synchronization proposal

Revised 2026-10-19 for [original request 17](https://github.com/dveyarangi/xuanxue-workshop/issues/17).
Status: accepted product decisions with a proposed executable interface and
delivery bounds; not an implementation assignment or deployed capability.
The [source comparison](../current-system.md#reminder-synchronization-source-comparison---2026-10-19)
records the inspected revisions. The user confirmed on 2026-10-19 that Daychi
has only test users/data and nobody currently uses Cabinet. No live-user
migration or staged old-client rollout is required by that evidence; existing
data deletion is not authorized.

## Accepted behavior and remaining preparation

The [selection agreement](../boundaries.md#accepted-reminder-selections) fixes
Cabinet ownership, stable lesson and class IDs, shared chosen-only selections
and an empty initial selection. The user accepted [online-only editing](../boundaries.md#accepted-online-only-reminder-editing)
on 2026-10-19: changes to shared selections and lead time require a successful
Cabinet save. Cabinet orders successful saves. Offline viewing and already
scheduled local reminders remain available. An uncertain save is checked against
Cabinet after reconnecting rather than assumed successful/failed or replayed.

This supersedes the 4 October offline-editing and client-edit-time conflict
policy, including its equal-time tie rule and durable offline queue. There is no
remaining client-clock decision. Different choices remain independent; a
selection save cannot overwrite an unrelated selection or the lead time.
The supported lead times, removal of per-date skips, existing pull occasions,
native local delivery and allowed cross-client duplicate reminders remain fixed.
The [native account-session contract](native-account-session.md) is unchanged.

The user accepted on 2026-10-19 that the zero-minute reminder targets the start
and may be sent up to one minute afterward. This tolerance does not shift the
positive before-start lead times. The [lead-time agreement](../boundaries.md#accepted-reminder-lead-times)
owns the decision; there is no remaining zero-minute timing choice.

Workshop still finalizes the executable wire and delivery bounds below against
those decisions. Preparing them does not authorize recipient implementation or
accept every proposed transport detail. Device presentation belongs to its project.

<straw-dog question="q-0002.0007.0002">

## Authority, identity and selection meaning

Cabinet owns shared account reminder settings. Cabinet web and native Daychi
read and change that state directly at the matching Cabinet issuer. Production
and staging have separate credentials, account caches and request generations.
No Daychi server or device becomes another shared-state authority.

A recurring selection is keyed by Cabinet class ID; an individual selection by
Cabinet lesson ID. Clients treat IDs as opaque, case-sensitive strings. A moved
lesson retains its selection across dates and calendar windows. A recurring
choice covers that class's scheduled future occurrences without a local start
date. Cancellation suppresses delivery without deselecting; restoration of the
same occurrence restores eligibility. An absent calendar row is not deselection.
Legacy titles, weekday/time hashes and dates are not identity mappings.

Reminder eligibility is the union of individually chosen lessons and occurrences
of explicitly chosen classes. Both sets start empty. There is no all-classes mode
or implicit subscription to new classes. Removing an individual selection does
not suppress a recurring choice; per-date skips are excluded. Duplicate eligibility
for one lesson produces one reminder within each project's delivery channel.

This extension affects lesson reminders. Cabinet's existing cancellation,
recording and class-linked material filters retain their own all/selected scope
and notification-kind preferences, separately from reminder choices. Device
notification permission and local delivery enablement remain device settings.
Selections do not change access, attendance, reservations or teacher notifications.

## Operations and access

HTTPS `GET /api/me/notifications/lessons/sync` returns a complete snapshot.
`PATCH` on the same route changes specified keys and returns the complete
post-save snapshot. There are no query parameters. Requests and responses use
UTF-8 `application/json`; responses include `Cache-Control: no-store`.
There is no shared cache, redirect, conditional GET or delta protocol.

Native requests use the existing Cabinet native bearer credential and no browser
cookies. Cabinet validates the current grant, account and revocation state on
each request. Browser requests use the matching existing Cabinet cookie; PATCH
requires Cabinet's nonempty `X-Requested-With` CSRF header. An active browser
session together with a native bearer is 400 `ambiguous_credentials`. Native
responses create no browser session; browser renewal remains unchanged. The
server derives account identity from authentication, never a caller-selected ID.
Authenticated, unblocked accounts need no additional role; existing delivery
channel and notification-kind preferences still apply.

Production uses `https://xuanxue.su`, staging `https://staging.xuanxue.su`.
Native transport stays within the existing credential owner. There is no new
authentication protocol, Daychi service credential or content-check capacity
amendment. Existing general API abuse limits apply; 429 is recoverable, without
a new per-grant throughput promise. Private settings and credentials stay out of
URLs, public calendar responses and logs.

## Wire version 1

Both successful operations return the same snapshot object, with these fields:

| Field | Type and meaning |
|---|---|
| `version` | Integer `1`. Unsupported versions are rejected. |
| `accountId` | Current Cabinet account's opaque ID. |
| `revision` | Canonical nonnegative decimal string, increasing when stored reminder settings change. |
| `classIds` | Complete positive recurring-selection string array, sorted lexicographically by ID. |
| `lessonIds` | Complete positive individual-selection string array, sorted lexicographically by ID. |
| `leadMinutes` | `0`, `15`, `30`, `60`, `120` or `null`; null follows the school default. |
| `schoolMinutes` | Current school default, preserving Cabinet's integer 5..1440 range. |
| `classes` | Existing public-safe `LessonScopeClassDto[]`, sorted by ID, for the selectable class catalogue; no private meeting links. |

The first two arrays are empty for a new account. Absence of an ID means false;
empty arrays are complete empty selections, never a failed read. Account settings
are transactionally consistent. A revision matches `^(0|[1-9][0-9]*)$` and is
ordered numerically as an arbitrary-precision integer, not lexicographically.
The account revision does not version school
settings, class metadata or calendar rows; those remain refreshable when its
revision is unchanged. Missing catalogue metadata does not deselect a saved ID.
There is no pagination, hidden date-window filtering or silent truncation of
account selections. No client edit timestamp, clock calibration, scope mode,
per-choice timestamp or removal-history field exists in this wire.

PATCH is `{version: 1, changes: Change[]}`. A change is exactly one of:

```json
{"kind":"class","id":"507f1f77bcf86cd799439011","selected":true}
```
```json
{"kind":"lesson","id":"507f1f77bcf86cd799439012","selected":false}
```
```json
{"kind":"lead","minutes":null}
```

Selection changes require `id` and boolean `selected`; `lead` has neither field
and requires `minutes` from the enum above. Fields cannot be omitted or replaced
with null except `minutes`. Unknown fields/kinds, duplicate JSON object keys,
unsupported versions and duplicate changed keys in a batch are invalid. A key
is `(kind,id)` for a selection, or `lead` for the scalar setting.

One request has 1..64 distinct keys and at most 128 KiB of uncompressed JSON.
Larger deliberate saves use sequential batches; an error stops remaining batches
without queuing them for replay. Already confirmed batches remain saved. IDs
must use Cabinet's canonical encoding; adding requires an existing lesson/class,
including an inactive existing class. Removing an unknown or retired ID succeeds
as a no-op. At most 50 positive class choices remain, preserving the existing
Cabinet bound; exceeding it rejects the whole batch. No extra numerical cap is
introduced for individual choices, and selections survive calendar-window shifts.

For an account with no selectable classes, PATCH
`{"version":1,"changes":[{"kind":"lead","minutes":0}]}` can return:

```json
{
  "version": 1,
  "accountId": "507f1f77bcf86cd799439010",
  "revision": "1",
  "classIds": [],
  "lessonIds": [],
  "leadMinutes": 0,
  "schoolMinutes": 45,
  "classes": []
}
```

## Saves, concurrency and uncertain outcomes

Cabinet validates the complete batch and applies its specified keys atomically
against current account state. Other choices are untouched. Successful commits
have one Cabinet-defined order; for the same key, the last committed value wins.
This is server save order, not device action time or a client timestamp tie.
Different clients' unrelated choices survive in either commit order. The revision
increments once if any value changes, and remains unchanged for a pure no-op.
No whole-snapshot precondition rejects an unrelated choice merely because another
key changed. No offline merge, durable edit outbox, clock guard or timestamp
tombstone history is required.

Daychi makes shared edits unavailable when offline and marks a change saved only
after a valid Cabinet save response or subsequent authoritative read confirms
current settings. A local draft is not shared state and does not alter scheduled
reminders before confirmation. Mutation requests are not automatically retried,
including by transport/session-renewal wrappers. One client sends deliberate
saves serially; it does not queue new offline intent during a failed/uncertain save.

A lost response, timeout, malformed response or server error can leave the save
outcome unknown: Cabinet may have committed it. The client keeps its last confirmed
settings and existing reminders, then reads Cabinet's current state on the next
successful reconnect/refresh before permitting further deliberate saves. It does
not label the uncertain mutation definitely failed, roll back server state or
silently resend it. The read establishes current state at that read's revision;
it is not a historical receipt proving whether that earlier request committed.
Other online clients may have changed the same key in the meantime. A user can
make a new deliberate save after refresh; this is a new Cabinet-ordered action.

Clients reject late responses from another issuer, account or session generation,
and lower account revisions cannot regress confirmed settings. Equal revisions
do not freeze school/catalogue metadata. Explicit logout clears local transient
draft/request state and cancels account-owned local reminders; it never replays
an old request on a later sign-in. A request already accepted by Cabinet is not
undone by local logout. Authentication/network failures are not explicit logout,
and preserve the last confirmed account cache without creating an edit queue.

## Failure behavior

Failures use Cabinet's envelope
`{statusCode: number, code: string, message: string, requestId?: string}`.
Human-readable messages are not machine discriminators. Validation and refusal
responses perform no reminder writes. Network failures and 5xx are not proof of
rollback. Trace request IDs are not idempotency keys or permission to replay.

| HTTP/code | Meaning and recovery |
|---|---|
| 400 `invalid_input` / `ambiguous_credentials` | Invalid shape/add target or mixed credentials; no write. Correct the input/client. |
| 401 `unauthorized` | Apply the existing credential lifecycle; resume reading/editing only under the authenticated matching account. |
| 403 `forbidden` | Account refused/blocked; no bypass or reminder write. |
| 409 `selection_limit` | More than 50 positive class choices would result; no batch write. |
| 413 `payload_too_large` | Body over bound; no write. Correct/split a new deliberate save. |
| 415 `unsupported_media_type` | Wrong media type; no write. Correct the client. |
| 429 | Respect `Retry-After` when supplied; no automatic mutation replay. Refresh before another deliberate save. |
| 5xx, network failure, invalid/incomplete reply | Preserve confirmed cache and active reminders; recover by reading Cabinet, not resending the change. |

Unknown errors are failures, never empty state. Read retries use existing refresh
occasions; no new background retry service or polling is introduced. Account and
issuer isolation remain enforced through all recovery and credential changes.

## Sign-in, guest state and delivery compatibility

On sign-in, Daychi reads Cabinet account settings and uses Cabinet public
lesson/class identity. Legacy guest choices and lead time remain separate and
are not automatically uploaded. No heuristic conversion or real-user migration
job is required. Existing guest data and independently owned guest operation stay
isolated from account synchronization. Signing out restores the prior guest state,
without deleting accepted Cabinet settings. Other profiles/accounts never inherit
transient drafts or in-flight request state.

The account calendar uses the accepted Cabinet source and school-time window,
not the old HTML timetable. Startup, foreground return and the existing five-minute
foreground refresh read calendar and settings. Failed reads retain their last good
data and scheduled reminders. Successful account changes can reconcile against
retained calendar rows; received moves/cancellations take effect after a successful
calendar refresh. An unseen change can leave a stale reminder. There is no new
native push, background refresh or cross-client delivery exclusivity.

Effective lead time is personal value or current `schoolMinutes`, including an
arbitrary supported default such as 45. Cabinet and Daychi add personal zero/120
support where missing. Cabinet targets the start for zero lead and uses the first
eligible scheduler tick in `[startsAt, startsAt + 60 seconds]`, within the accepted
one-minute tolerance and existing account/lesson deduplication. This is not an
intentional delay and does not move positive lead-time targets. Missed windows
are not replayed as fresh reminders; delivery-channel limits remain. Daychi
schedules zero at the start of a future lesson, not as catch-up after it starts.

Proposed Daychi capacity is the earliest 60 eligible future local reminders within
the existing calendar window, ordered by fire time then lesson ID. A larger plan
cannot reject the whole reconciliation or cancel all existing reminders. Refill
uses existing successful refresh/reconciliation occasions; later reminders have
no coverage guarantee without another reconciliation. OS permission, platform
limits and suspended-app behavior remain delivery limitations. Duplicates between
Cabinet and Daychi remain allowed.

## Initial write rollout

Preserve existing Cabinet notification preferences. Existing explicit selected-mode
class IDs seed reminder class choices; an all-classes filter never expands into
reminder subscriptions. The legacy filter and remembered IDs stay stored for other
notification kinds. Retain the existing personal lead value or school default.
No historical edit-time reconstruction or timestamp baseline is needed.

Cabinet web and API update together before Daychi shared editing is enabled.
Retire the old reminder-minutes PUT with ordinary 404 `not_found`; keep the legacy
scope PUT solely for other class-scoped notices, without access to reminder
selections. Existing GET representation remains readable with the same separation.
No active-user staged rollout, special upgrade error or refresh-approval checkpoint
is required. Whole-list writers do not remain active against shared reminder
state. A rollback can disable shared editing, not restore unsafe whole-list saves.

This proposed version does not activate unfinished schedule integration or alter
native-session, content or browser-wiki contracts. Recipient implementation
publication requires one accepted immutable wire, common cases and the approved
addressed contributions. This document grants no fixture mutation or release.

## Common conformance outcomes

| Case | Required observation |
|---|---|
| Offline editing | No shared selection/lead save is available offline; no local edit becomes confirmed or replays after reconnect. Cached viewing and scheduled reminders continue. |
| Different keys | Concurrent saves adding A and removing B both survive in either Cabinet commit order; lead changes cannot overwrite them. |
| Same key | The last Cabinet commit wins without client timestamps, clock inspection or equal-time rules. |
| Removal/no-op | Removing a selected ID changes only that key; removing an absent ID succeeds without a new revision. Repeating a stored value is a no-op. |
| Uncertain save | A committed save with a lost response and a noncommitted save are both recovered by reading current Cabinet state, without automatic mutation replay or assumed rollback. |
| Concurrent readback | If another client changes a setting after an uncertain save, readback displays the current value rather than attributing it to the uncertain request. |
| Late responses | Lower revisions and another account/session/issuer cannot regress confirmed settings; metadata remains refreshable at equal account revision. |
| Empty/union | New accounts have no reminders; only explicit class/lesson choices confer eligibility. Individual removal cannot suppress recurring eligibility; other notice filters cannot change reminder choices. |
| Identity | Moves across dates/windows retain a lesson choice; cancellation suppresses and restoration restores delivery eligibility. |
| Logout/refusal | Explicit logout cancels account reminders/clears transient work; accepted server state survives. Refusal/network failures retain confirmed cache without cross-account replay. |
| Guest transition | Sign-in uses Cabinet, leaves guest data intact and uploads nothing automatically; sign-out restores guest state. |
| Validation | Invalid kind/shape/ID, duplicate keys, unsupported version, 65 changes, body overflow or a 51st positive class cannot partially write the batch. |
| Access | Browser CSRF, native grant revocation/account blocking, mixed credentials, no-store and account isolation match the access section. |
| Lead/delivery | Personal 0/120 and school-default 45 work on both ends. Zero targets the start with up to 60 seconds of accepted processing tolerance; positive lead targets remain before start. Native capacity remains proposed. |
| Read failure/recovery | Last good calendar/settings and scheduled reminders survive; received cancellations/moves apply on recovery, without an offline edit queue. |
| Capacity | More than 60 eligible reminders retains/schedules the earliest 60 deterministically; later coverage depends on existing refill occasions. |
| Rollout/regressions | Updated web and Daychi edit the same account safely; retired lead PUT is 404, legacy scope PUT affects only other notices, and guest/content/session/browser obligations remain compatible. |

## Ownership and evidence

Cabinet owns authenticated GET/PATCH, validation, atomic ordered saves, state
revision, initial values, safe legacy route separation, web adoption and backend
reminder selection/zero support. Daychi owns confirmed account/issuer-scoped cache,
online-only editing, authenticated transport, uncertain-save readback, calendar
identity, late-response/logout isolation, guest separation, removal of per-date
skips and bounded OS reconciliation. Its recipient context includes why skips
were removed: dismissing a notification suffices; the action informs no teacher
and releases no reservation.

Workshop owns final shared definitions, delivery alignment, immutable accepted
authority, common-case coverage and joint acceptance. This is not a delivery split
or recipient authorization. Provider HTTP/concurrency checks and client offline,
uncertain-response, cache/lifecycle and OS cases need exact revisions and executed
results. Joint staging proof uses an authorized matching account, Cabinet web and
an identified installed Daychi build, covering concurrent independent/same-key
saves, lost-response readback, offline edit refusal with retained reminders,
move/cancellation recovery and logout/isolation. Existing accepted native-account
proof is reused; two independent local successes alone do not prove integration.

</straw-dog>
