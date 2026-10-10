from pathlib import Path

p = Path('docs/questions/q-0002.0007.0006-how-should-public-schedule-reads-expose-partial-results-while-preserving-deployed-consumers.md')
header = p.read_text(encoding='utf-8').split('## Accepted outcome')[0]
body = '''## Decision — 2026-10-07

The user confirmed that the previous public pilot is not yet used and rejected
both version selection and public completeness metadata. The
[public lessons contract](../contracts/public-lessons.md) now defines the agreed
direct amendment: return valid rows, omit malformed individual lesson/class data,
and log each omitted occurrence at error severity with cause and available IDs.
Genuine retrieval/processing/code faults remain whole-read failures. Count mode
selects before omission without refill; window projection has no row cap. There
is no public distinction between genuinely empty and all-invalid results.

Daychi replaces its isolated pilot display on valid success, including empty,
while failed refresh preserves the prior result. Repair restores records with
the same identity. The client cannot infer source completeness or reliable
cancellation/deletion from absence; ordinary state/reminders stay isolated.

Sentry was raised as a possible later collector, not selected or installed in
this amendment. Inspection found Cabinet ADR-0053/0132 using Telegram and a
developer journal and rejecting Sentry. Its existing reporting hook runs in the
HTTP-500 filter, so handled omissions in HTTP 200 need their explicit log path.
Broader error-monitoring obligations remain in q-0002.0006.

The replacement Daychi body, Cabinet amendment and superseded-review replacement
are in [.local/partial-issue6.md](../../.local/partial-issue6.md),
[.local/partial-issue5-comment.md](../../.local/partial-issue5-comment.md) and
[.local/partial-issue5-review-replacement.md](../../.local/partial-issue5-review-replacement.md).
Fresh independent recipient reading passed the revised shape and set-wide
compatibility. No implementation or deployment was verified by that reading.

Pending publication action: obtain the existing scoped commit/push permission,
publish an immutable contract revision, replace the draft reference placeholders,
publish/read back the original issues, and retain recipient dependencies and
remaining implementation/native proof. No sibling edits or deployment are
authorized. Daychi installation progress is not acceptance; fresh-session and
accessible project commit/PR evidence remain outstanding in issue 2.
'''
p.write_text(header + body, encoding='utf-8', newline='\n')
print('Updated authored question body only.')
