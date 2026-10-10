from pathlib import Path

root = Path(__file__).resolve().parents[2]
migration = root / 'docs/migration-changes.md'
report = root / 'docs/reconciliation-20261004.md'
body = migration.read_text(encoding='utf-8')
marker = '## Proposed contribution breakdown'
start = body.index(marker)
history = body[start:]
replacement = '''## Proposed contribution breakdown

The earlier broad investigation pair was withdrawn as duplicate work. Its
[disposition and corrected impact](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05)
are historical evidence. It creates no recipient obligation.

The accepted public pilot is tracked by
[cabinet-daychi-public-schedule-connection](tickets/01-0007-cabinet-daychi-public-schedule-connection.md).
Its provider and consumer use the same published contract. Broader migration
changes above retain their unresolved decisions and require separately authorized scope.

## Impact assessment of the contribution split — refreshed 2026-10-05

See the [historical assessment](reconciliation-20261004.md#withdrawn-contribution-proposal--2026-10-05).
The current accepted-contract delta is the table above.
'''
report_body = report.read_text(encoding='utf-8')
new_marker = '## Withdrawn contribution proposal — 2026-10-05'
assert new_marker not in report_body
# Same directory: the moved block's relative links retain their meaning.
report.write_text(report_body.rstrip() + '\n\n' + new_marker + '\n\n'
                  + 'Historical proposal, withdrawal and impact copied from migration-changes\n'
                  + 'during maintenance on 2026-10-06; the statements below preserve that dated state.\n\n'
                  + history.replace('## ', '### '), encoding='utf-8')
migration.write_text(body[:start] + replacement, encoding='utf-8')
print('Moved contribution history to reconciliation evidence; retained inbound anchors.')
