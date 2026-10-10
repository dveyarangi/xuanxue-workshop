Contract amendment — 2026-10-07

The user has changed the failure policy: return the valid available schedule,
omit individual malformed records and log each omission at error severity. The
previous public pilot contract is not yet used, so amend the existing operation
directly. No version selector, response envelope, completeness header or client
partial-result warning is added.

This amendment supersedes the original issue's entire-result-or-error instruction
and the [2026-10-06 review](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011347777).
Authority shared with [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6):
[Public lessons contract and common conformance cases](https://github.com/dveyarangi/xuanxue-workshop/blob/CONTRACT_REVISION/docs/contracts/public-lessons.md).
The fixed reference owns all query, field, identity, selection, omission/logging,
refresh, empty-result and genuine failure meanings.

## Provider action

- Keep `GET /api/public/lessons`, existing query modes and bare-array projection.
  Validate each selected lesson/class public projection; omit affected occurrences
  for malformed data or missing class metadata. Every selected occurrence using
  a bad shared class is affected. Return HTTP 200 containing only valid rows.
- Missing duration and invalid class format remain invalid data; do not emit
  malformed public DTOs. Preserve valid empty strings, optional absent location
  and missing legacy tags -> `[]`. Keep validation work already underway, but
  change the consequence of identified corrupt records from whole-read 500 to
  omission/error log. Do not change protected student behavior.
- Log each omitted occurrence at `error` with its cause, lesson/class IDs where
  available and request ID when available, excluding credentials/private rows.
  Emit this signal on the omission path despite HTTP 200; relying on the global
  HTTP-500 filter is insufficient. Logging tool/internal mechanisms remain Cabinet's.
  No Sentry installation or replacement of existing monitoring is assigned here.
- Count mode selects first-limit candidates before validation and does not refill;
  window mode projects all selected candidates without a row cap. No collection-wide
  corruption scan is requested. All-invalid and genuinely empty selections both
  return `[]`; only the former emits omission error logs. No public metadata
  distinguishes them, and no completeness guarantee is made.
- Failed database/class retrieval, unexpected code faults or inability to process
  the selected set reliably still return the established error envelope (500
  `internal_error`, or existing applicable 503/429). Do not catch every exception
  and relabel it as corrupt-record omission. Preserve all public exposure and
  protected-route/account/reminder boundaries.

## Evidence and dependencies

Cabinet installation is [accepted in #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155);
no new Ready approval is required. Cabinet executes under its own operator. The
verified staging/production deployment at `fc2dee2` does not establish amended
omission/logging behavior.

Report implementation commit/PR, executable-definition revision, reachable origin
and actual runtime/deployment status here. Cover every applicable common case,
including HTTP-level mixed lesson/class corruption, missing class, shared bad class,
all-invalid and truly empty selections; error logs with cause/IDs; healthy 201-row
window; count without refill; genuine read/code failure; public allowlist and
protected/student regressions. Corruption fixtures use disposable development/test
data, never production. No stricter field contract is introduced.

Coordinate controlled lesson creation/move/cancellation and mixed-source/repair
native proof with Daychi's authorized operator in the selected reachable test
environment. Existing staff controls support ordinary fixtures; no public write
or clock-setting API is added. Daychi remains read-only, replaces the pilot list
with returned valid rows, and preserves ordinary cache/selections/reminders.

Workshop reviews provider evidence here. Native proof remains in #6 and is required
for the combined connection; provider publication/deployment alone is not its
acceptance. Original-issue communication and ownership remain unchanged.
