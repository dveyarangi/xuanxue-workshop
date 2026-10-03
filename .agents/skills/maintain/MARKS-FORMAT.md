# Marks format

This shelf owns the format of the marks, the maintain mechanism's one record:
`docs/mechanisms/maintenance.md`, a heading, a line pointing here, and one table, written only by
`maintain.py --mark`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|

- One row per mechanism per level; `level` is `rules` or `output`.
- `fingerprint` is 64 lowercase hex, of what the level was checked against; `date` is
  `YYYY-MM-DD`; `outcome` is `amended` or `nothing to change`.
- A row whose mechanism is no longer declared is dropped at the next mark. Rows are sorted by
  mechanism, then level.
- Read by `--check` at every pass; a malformed row fails the check and refuses every mark until it
  is repaired.
- In a recipient the mechanisms that came with core are maintained where core is made: the check
  leaves them out and a mark refuses them.
