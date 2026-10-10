from pathlib import Path
import subprocess

root = Path.cwd()

def original(path):
    return subprocess.check_output(['git', 'show', f'HEAD:{path}']).decode('utf-8')

def replace(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one occurrence: {old[:100]!r}')
    return text.replace(old, new)

def write(path, text):
    (root / path).write_text(text, encoding='utf-8', newline='\n')

c = original('docs/contracts/public-lessons.md')
c = replace(c, 'It preserves the accepted agreement; consolidation does not require voting on it\nagain.', 'Amended by the user, 2026-10-07: the not-yet-used public pilot is a\nbest-effort read of valid schedule records. Individual malformed records are\nomitted and logged at error severity; they do not fail the remaining result.\nThere is no version selector or public completeness metadata.')
c = replace(c, "The pilot displays Cabinet's complete dated schedule for fourteen school calendar\ndates", "The pilot displays Cabinet's valid dated schedule records for fourteen school calendar\ndates")
c = replace(c, '| Complete window |', '| Window |')
c = replace(c, 'All dated lessons with `from <= startsAt < to`; no current-time filter, row cap or pagination.', 'Select all dated lessons with `from <= startsAt < to`; return those with valid public projections, without a current-time filter, row cap or pagination.')
c = replace(c, 'arrays retain their ordinary values rather than meaning a missing item.', '''arrays retain their ordinary values rather than meaning a missing item.

The existing operation and bare array are amended directly: no version query,
response envelope, completeness header or omitted-record list is added. The user
confirmed on 2026-10-07 that the previous public pilot contract is not in use.

Window mode projects all query-selected candidates. Count mode selects the first
requested number of candidates in start order before projection, then omits
invalid candidates without backfilling; fewer than the limit can be returned.
Missing class metadata or an invalid public lesson/class value omits the affected
occurrence, including all selected occurrences depending on an invalid shared
class. Allowed empty strings, optional absent `location` and missing legacy tags
producing `[]` are valid and cause no omission. No malformed public item is emitted.
Coverage is scoped to query-selected rows; this adds no collection-wide corruption
scan of records whose stored start cannot match the selection predicate.

Each omitted occurrence produces an error-level operator log with its reason,
lesson ID and class ID where available, and request ID when available. Logs
contain no Zoom/authentication secrets or raw private source records. This signal
must be emitted in the omission path even though the HTTP request succeeds; it
cannot depend on the HTTP-500 exception handler. Logging tool, diagnostic sink
and internal implementation remain Cabinet's. Connecting an external error
collector is outside this amendment; no Sentry integration is claimed or required.
Unexpected code faults, failed lesson/class retrieval or inability to process
the selection reliably still fail the request; only identified invalid record
data is omitted.''')
c = replace(c, 'Each request retrieves Cabinet\'s current matching lessons; each successful\ncomplete-window result becomes the pilot\'s displayed result for those dates.', '''Each request retrieves Cabinet's current matching valid lessons; each valid
window result becomes the pilot's displayed list for those dates. This is a
best-effort view: omitted corrupt records cannot be distinguished by the consumer
from absent records. The API supplies no completeness signal and Daychi needs
no new partial-result state or warning. Absence is not authoritative proof of
cancellation or deletion; returned `status: cancelled` remains explicit.
No pilot read changes ordinary reminders, selections or the ordinary cache.''')
c = replace(c, 'the previous displayed list. These are already accepted refresh semantics.', 'the previous displayed list, including when all selected candidates were invalid.\nAn empty response means no valid public rows were available for this read, not\nproof that the underlying source contains no lessons. A later successful read\nshows repaired records again with their existing identities.')
c = replace(c, 'later data. Missing required metadata must still fail the request rather than\nsilently omit a lesson.', 'later data. Missing/invalid individual records are omitted and logged as defined\nabove; no public completeness guarantee is made.')
c = replace(c, '| Missing/malformed required source data or unexpected provider failure | 500 / `internal_error` |', '| Unexpected provider failure, including failed retrieval or unreliable processing of the selected set | 500 / `internal_error` |')
c = replace(c, 'No partial array is returned on failed production of the selected result.', 'Individual invalid records do not fail the selected result; operator logs carry\nthe omissions. A genuine whole-read failure returns an error, never a partial\nsuccess body.')
c = replace(c, 'a failed refresh; HTTP 200 `[]` alone means an empty successful result.', 'a failed refresh; HTTP 200 `[]` is a valid successful result even if all\nselected candidates were omitted.')
c = replace(c, 'Cancel `005`: it remains in the response with the same ID and cancelled status.', '''Cancel `005`: it remains in the response with the same ID and cancelled status.

If only `003` has a missing required duration, the same request returns `002`,
`004`, `005` with HTTP 200 and logs the omitted `003` as an error. Repairing `003`
restores all four. If all four are invalid, the result is `[]` with omission error
logs; if no candidate matches, it is `[]` without omission logs. No response
metadata distinguishes these two empty results.''')
c = replace(c, '''6. Fail on missing required class metadata or malformed required lesson data;
   never silently omit an occurrence. Check existing 400/429/500/503 error shapes
   where emitted and failed transport/malformed success without an API error body.''', '''6. Mixed valid/invalid lesson or class data returns HTTP 200 containing exactly
   the valid rows, with an error log for each omitted occurrence. Cover missing
   duration, invalid format, missing class and all affected occurrences of a bad
   shared class; assert reason, available IDs/request ID and absence of secrets.
   All-invalid selection returns `[]` with error logs; a genuinely empty selection
   returns `[]` without omission logs. Valid empty strings, optional absent location
   and missing legacy tags remain valid. Count limit 2 with an invalid first
   candidate and two later valid candidates returns only the second, without refill.
   Genuine lesson/class read failure or unexpected code fault returns 500
   `internal_error`, not 200. Check existing 400/429/503 error shapes where emitted
   and failed transport/malformed success without an API error body.''')
c = replace(c, '8. Prove failed refresh retains the previous pilot result and an initial failure', '8. Prove a mixed result replaces the displayed list with exactly its valid rows,\n   all-invalid `[]` clears it, and repairing source data restores the same IDs\n   after refresh. No completeness state or older-row merge is required.\n   Prove failed refresh retains the previous pilot result and an initial failure')
c = replace(c, '    observed results and deployment status. A disposable development provider is', '    observed results and deployment status. Include a controlled mixed-source\n    result and repair/recovery in disposable development/test data. Corruption\n    fixtures do not belong in production. A disposable development provider is')
c = replace(c, 'Both project assignments cite the exact same commit-bound GitHub file URL.', '''Both project assignments cite the exact same commit-bound GitHub file URL.
The user confirmed that the previously published public pilot is not yet used,
and authorized direct replacement of its all-or-error guarantee. The route,
query and response field set remain the same; no coexisting version or legacy
retirement work is introduced. Cabinet's amendment comment replaces the original
issue's whole-result-failure instructions; Daychi's issue body adopts this same
best-effort agreement. Deployment at the old source revision does not establish
conformance to the amended behavior. This does not change protected Cabinet
web contracts or ordinary Daychi schedule/reminder contracts.''')
write('docs/contracts/public-lessons.md', c)

b = original('docs/boundaries.md')
b = replace(b, '''Failure and recovery agreed by the user, 2026-10-05: a successful read returns
the complete matching result, or the selected count-mode result; it never silently
omits a matching lesson because required lesson/class data cannot be produced.
Missing required data is a failed read; an empty successful result is distinct.
Use Cabinet's existing error conventions, without exposing private schedule data.''', '''Failure and recovery amended by the user, 2026-10-07: public pilot reads return
valid available lessons while omitting individual malformed records with
error-level operator logs. Availability of the remaining schedule takes priority
over complete delivery. The prior public pilot contract is not yet used, so its
guarantee is replaced directly without a version selector or completeness metadata.
The client cannot distinguish an omitted invalid record from an absent record.
Failed retrieval or unreliable processing of the selected set still fails the
read using Cabinet's error conventions, without exposing private schedule data.''')
b = replace(b, 'ordinary failure handling; no partial-success response or recovery protocol is\nintroduced.', 'ordinary failure handling. A valid best-effort result is a successful read,\nnot a failed refresh; it needs no new completeness or warning state.')
b = replace(b, '''the window. A successful empty list clears the previous displayed result. This
is the accepted read-and-refresh behavior, not an additional approval checkpoint.''', '''the window. A successful empty list clears the previous displayed result,
including when all selected rows were invalid; it means no valid rows available
and does not prove the source contains no lessons. Repairing records restores
them on a later successful read. This pilot display does not infer reminder or
account mutation from absent rows.''')
write('docs/boundaries.md', b)

s = original('docs/current-system.md')
s = replace(s, 'implement the fixed [public wire contract](contracts/public-lessons.md).', 'implement the original public wire shape at\n[Workshop e209d27](https://github.com/dveyarangi/xuanxue-workshop/blob/e209d27239391be3af2be71b898c79f453851c01/docs/contracts/public-lessons.md).')
s = replace(s, 'under [issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011347777).', '''under [issue 5](https://github.com/dveyarangi/xuanxue-workshop/issues/5#issuecomment-6011347777).

The user replaced the not-yet-used public pilot's all-or-error guarantee on
2026-10-07. The [amended contract](contracts/public-lessons.md) requires valid-only
best-effort rows and error-level logs for omitted corrupt occurrences, without a
version selector or public completeness metadata. The pinned projection findings
remain invalid emitted data; allowing omission does not authorize malformed rows.
Amended implementation/deployment and native recovery evidence remain unverified.
Cabinet's existing error reporting uses a developer journal and Telegram
(ADR-0053/0132); Sentry was rejected there. The inspected reporting path is called
by the HTTP-500 filter, so it does not establish reporting for handled omissions
in HTTP 200. Such omissions need their own explicit error-log path.''')
write('docs/current-system.md', s)

m = original('docs/migration-changes.md')
m = m.replace('the provider required-data correction', 'the provider valid-only omission/logging correction')
m = m.replace('correct required-data enforcement and preserve protected Cabinet web behavior.', 'enforce valid public rows, omit malformed individual records with error logs, and preserve protected Cabinet web behavior.')
m = m.replace('Public pilot schema/identities are fixed.', 'Public pilot schema/identities are fixed; the not-yet-used read now returns valid best-effort rows without completeness metadata.')
write('docs/migration-changes.md', m)

t = original('docs/tickets/01-0007-cabinet-daychi-public-schedule-connection.md')
t = replace(t, 'confirms the public route on production at `fc2dee2`. Required-data validation\nand actual native refresh evidence are outstanding;', '''confirms the original public route on production at `fc2dee2`. The user amended
the not-yet-used pilot on 2026-10-07: omit corrupt rows with error-level logs,
without adding a version selector or completeness metadata. Valid-only omission,
explicit log evidence and actual native refresh proof are outstanding;''')
t = replace(t, '  the shared agreement; reviewed evidence identifies reachable setup/runtime and deployment limits.', '  the amended shared agreement, including valid-only rows, error logs for omitted\n  corrupt occurrences and genuine whole-read errors; reviewed evidence identifies\n  reachable setup/runtime and deployment limits.')
t = replace(t, '  reschedule/cancellation, failed-refresh retention and recovery, with reproducible', '  reschedule/cancellation, mixed valid/invalid reads, repair recovery and\n  failed-refresh retention, with reproducible')
write('docs/tickets/01-0007-cabinet-daychi-public-schedule-connection.md', t)

r = original('docs/reconciliation-20261004.md')
r = replace(r, '# Boundary reconciliation — 2026-10-04', '''# Boundary reconciliation — 2026-10-04

## Public best-effort amendment — 2026-10-07

The user changed the [public pilot agreement](boundaries.md#accepted-first-schedule-connection):
return valid lessons, omit malformed individual records and log each omission at
error severity. The prior public contract is not yet used, so the same operation
is amended directly. No version, completeness header, envelope or client warning
state is added. The [public contract](contracts/public-lessons.md) owns exact
selection, output, empty-result, logging, whole-read-error and recovery cases.

The earlier pinned mapper counterexamples below remain evidence of invalid
emitted public data. The remedy now omits/logs those rows rather than failing
the whole read; operational database/class-read/code failures remain errors.
Old deployed healthy samples do not prove the amended handling. Cabinet's existing
HTTP-500 reporting path does not automatically see a handled omission in HTTP 200.
The contract requires its explicit error log without choosing or installing an
external collector. Cabinet's ADR-0053/0132 currently use Telegram and a developer
journal and reject Sentry; any collector change belongs to its own observability
decision, not this public response amendment.

Daychi's replacement assignment and Cabinet's superseding comment are prepared
against one fixed authority. Scoped commit/push approval is still required before
immutable publication and original-issue updates. Provider/client implementation,
Daychi installation acceptance and native proof remain separate outstanding work.
Dated sections below retain their original acceptance basis.''')
write('docs/reconciliation-20261004.md', r)

d = (root / '.local/partial-issue6-before.md').read_text(encoding='utf-8')
d = d.replace('e209d27239391be3af2be71b898c79f453851c01/docs/contracts/public-lessons.md', 'CONTRACT_REVISION/docs/contracts/public-lessons.md')
d = d.replace("Cabinet's complete dated schedule", "Cabinet's valid available dated schedule")
d = d.replace('complete-window guarantees', 'bounded-window coverage, best-effort valid-only results and operator logging')
d = d.replace('The result is the complete window, including windows with more than 200 lessons.', 'There is no window row cap, including windows with more than 200 valid lessons. Individually malformed source records are omitted and logged by Cabinet; no completeness header, envelope or version selector is added.')
d = d.replace('A successful window read replaces the pilot\'s prior window:', 'A valid best-effort window read replaces the pilot\'s prior window with exactly its returned valid rows:')
d = d.replace('and `200 []` clears it.', 'and `200 []` clears it even when all selected rows were invalid. An empty response means no valid rows available, not proof that no source lessons exist. No completeness/partial-result state or new warning is required; do not merge older rows or infer reminder/account mutation from absent items.')
d = d.replace('Cabinet provider acceptance remains incomplete on malformed required source data under #5; healthy live results do not resolve that guarantee.', 'These probes verify the original deployed operation, not the amended best-effort handling. Cabinet acceptance under #5 requires omission/logging of corrupt source rows, valid-only success data and genuine whole-read errors; healthy live results do not resolve those cases.')
d = d.replace('Provider conformance, including required-data validation,', 'Provider conformance, including valid-only omission and error logs,')
d = d.replace('complete results, stable move/cancellation, empty replacement, malformed data,', 'uncapped valid results, stable move/cancellation, mixed-result replacement, all-invalid empty replacement and source-repair recovery, malformed success data,')
d = d.replace('Demonstrate reschedule/cancellation after refresh, failed refresh retention and recovery with controlled provider changes.', 'Demonstrate reschedule/cancellation, a controlled mixed valid/invalid result, return of repaired records, failed refresh retention and recovery. Corrupt-source fixtures use disposable development/test data, never production.')
d = d.replace('Coordinate a dedicated one-off staging lesson with an authorized Cabinet teacher, assistant or admin.', 'Coordinate a dedicated one-off lesson in the selected integration environment with its authorized Cabinet operator. Staging or a disposable development provider is sufficient; the staging UI URL below is an example, not an additional deployment prerequisite.')
d = d.replace('## Controlled native test', '''The [2026-10-06 installation progress report](https://github.com/dveyarangi/xuanxue-workshop/issues/2#issuecomment-6022727525) leaves fresh-session and accessible project commit/PR evidence outstanding. Workshop acceptance of #2 is not established by that report. This amendment does not release client development before its existing prerequisite.

## Controlled native test''')
write('.local/partial-issue6.md', d)

comment = '''Contract amendment — 2026-10-07

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
'''
write('.local/partial-issue5-comment.md', comment)

old = (root / '.local/partial-issue5-review-replacement.md').read_text(encoding='utf-8')
para = old.split('\n\n')[1]
review = f'''Workshop review — 2026-10-06; policy follow-up — 2026-10-07

{para}

The user has amended the public pilot's failure policy. The [current Cabinet
amendment](CABINET_AMENDMENT_URL) and its immutable contract supersede this
review's whole-request-500 repair instructions. The previous public pilot is
not yet used; no version/legacy operation is required. Corrupt individual records
are omitted with an error log while valid records remain available. Genuine
operational failures still fail the read.

The [public mapper at fc2dee2](https://github.com/gregoryKot/xuanxue-cabinet/blob/fc2dee20d64d91122a58e57709c378c5fc91bae7/api/src/lessons/public-lesson.mapper.ts)
copied required lean values without runtime enforcement. Isolated counterexamples
showed missing duration omitted from serialized JSON and invalid class format
returned unchanged. These are pinned-source findings, not live corrupt-database
experiments. They remain invalid public data under the amended contract.

Keep valid public field enforcement; implement the omission/error-log and HTTP
cases specified in the newer amendment instead of whole-read failure on corrupt
records. Preserve empty strings, absent optional location, missing legacy tags
-> `[]`, public exposure boundaries and protected student behavior. Report code
and executed checks in this original issue.

Cabinet installation is [accepted in #1](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155).
Native evidence remains with [daychi-public-lessons #6](https://github.com/dveyarangi/xuanxue-workshop/issues/6)
and the combined connection. This review does not claim amended deployment or
acceptance.
'''
write('.local/partial-issue5-review-replacement.md', review)
print('Revised contract, six scoped records and three issue drafts; no tracker or Git publication.')
