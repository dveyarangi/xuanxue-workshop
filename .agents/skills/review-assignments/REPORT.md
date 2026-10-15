# Shared review report

Maintain the configured shared review report when findings, decisions or operational state change.
Preserve unresolved matters until evidence resolves them. Link original issues and governing
records; the report grants no authority and does not replace their history. Keep unchanged runs
silent. Readers use the dated report as context, not proof of a fresh board read. Validate and
publish complete replacements atomically, refusing a changed prior version.

## Format

Use the heading “Board review”, the record kind “what happened”, a Reviewed timestamp with
timezone or “none”, and these sections in order: Reviewed scope, Results, Open matters,
Operations. Keep every section nonempty. Record only inspected scope and sourced outcomes.
Preserve unresolved matters until their sources resolve them. The controller owns Operations;
preserve it during semantic replacement. Read the current version, prepare the complete
replacement, then use board_report.py write with the expected version. A conflict requires
rereading and reconciliation.

```markdown
# Board review

- **record of** what happened
- **Reviewed:** none

## Reviewed scope

No review recorded.

## Results

No result recorded.

## Open matters

Consult original assignments and the question store.

## Operations

No controller outcome recorded.
```

## Publication

The interface is `.agents/scripts/gw/board_report.py` with `version PATH`,
`check PATH` and `write PATH --source UTF8_FILE --expected VERSION`.
The version is a SHA-256 digest or `absent`. The writer validates shape, excludes
cooperating writers, checks the version and atomically replaces the complete file.
This guards publication, not the truth or completeness of an agent's conclusions.

The latest snapshot is read by the operator, session recovery and configured conversation
readers. It is replaced after meaningful review or controller recovery/failure, and retired
with periodic review after outstanding matters have homes elsewhere. Original issue history
and governing records retain their own lifetimes.
