# Harness evidence

## Workshop update — 2026-10-04

Authorized by the user: "we shold install the update". Installed from a fresh
clone at `95535afbb840257752256e2d09433d2b4eb7c468`, upstream entry contract v25.
Workshop now announces `goodwolf-harness@95535af, 2026-10-04`.

The current source's installer ran with `--update --overwrite --at` at that
commit. A pre-update snapshot and raw update/check reports are retained outside
this repository at
`D:/Dev/workspaces/taichi_workspace/.local/harness-update-ecea07b6bbfb4823ab73157780eac4ab/`.
The snapshot was moved out of the repository after the injector correctly
reported its duplicate installed blocks as orphans. The next check has none.

Workshop's local rules, reconciliation declaration and skill, and delivery-status
file are byte-identical to the snapshot. RC1's rules file gained only its agreed
question wrapper; its installed copies were regenerated. Four existing straw-dog
bindings were migrated to questions without changing their bodies: startup
adoption to q-0002.0005, retained Daychi backend and temporary admission check to
q-0002.0009, and provisional native acquisition to q-0002.0010. The deferred
consolidation question does not make its two straw dogs due.

Verification:

- Injector: six rules files, expected blocks present, no orphans or diagnostics.
- Mechanism shape: no diagnostics or core/instance leaks.
- Question store: no diagnostics; the two existing similarity suggestions remain.
- Straw-dog listing over entry, core, docs and local rules: five question-bound
  statements, none due, no diagnostics.
- `git -c core.safecrlf=false diff --check`: passed.
- Full harness gate: `arrived: false`. Injector and shape passed; ref comparison
  differs only at `.agents/skills/align/SKILL.md`. The new `_differs` still removes
  only local blocks. An in-memory comparison removing the injector-validated
  reconcile block too matches the upstream shipped text exactly. The gate was
  not amended or bypassed.

Windows refused creation of both loader symlinks. The installer reports these
commands for the operator to run in an elevated Command Prompt:

```bat
mklink /D "D:\Dev\workspaces\taichi_workspace\xuanxue-workshop\.claude\skills" "..\.agents\skills"
mklink /D "D:\Dev\workspaces\taichi_workspace\xuanxue-workshop\.cursor\skills" "..\.agents\skills"
```

Then re-run `uv run --offline --no-project python .agents/scripts/gw/harness.py . --check`.
At installation, loader links did not resolve. No commit or push was performed.

## Loader links verified — 2026-10-05

The user reported repairing the links. A fresh `harness.py . --check` confirms
both `.claude/skills` and `.cursor/skills` resolve to `.agents/skills`. Injector
and shape still pass; the ref comparison still differs only at /align because
of the independently validated reconcile injection. Thus `arrived` remains
false for that known comparison limitation, with no pending loader repair.

## Workshop update — 2026-10-05

Authorized by the user: "lets update the harness to new version". Installed from
a fresh upstream clone at `9a6d26b025ccd3bc9feb11d0c29a9bb8bff10dd0`, upstream
entry contract v30. Workshop announces `goodwolf-harness@9a6d26b, 2026-10-05`.
The update uses the upstream installer with `--update --overwrite --at 9a6d26b`.

A pre-update snapshot, fetched source, comparison diff and preservation checker
are retained outside this repository at
`D:/Dev/workspaces/taichi_workspace/.local/harness-update-01a10ad8/`.
The snapshot includes the existing uncommitted core, project records and rules.

Two accepted rules absent upstream were moved without changing their bodies:
local mechanism-shape/R9 to local/L12, and local ticket/P12 to local/L13.
Their authored home is now `local.rules.md`, and the installer regenerated their
instruction surfaces. The old ticket injection was retracted before replacement.
Local installation initially refused the changed block and an anchor preceding
another mechanism's block; explicit overwrite and an anchor after all core blocks
completed the installation. No rule was dropped.

Before this evidence entry was appended, the project documents, distributable
collaboration skill, README, PRODUCT, CLAUDE entry and reconciliation declaration
and rules were byte-identical to the snapshot. The reconciliation skill changed
only by replacing its ticket/P12 injection with local/L13. Both loader links were
kept and resolve to `.agents/skills`.

Verification: injector and mechanism shape pass with no diagnostics or orphans;
question-store validation passes with the same two similarity suggestions;
five straw-dog bindings remain, none due; whitespace checks pass. Full harness
checking still reports `arrived: false`, with only `/align` differing from the
announced ref. Removing the injector-validated local and reconcile blocks in
memory makes `/align` exactly match shipped upstream text. The comparison gate
was neither amended nor bypassed. The shipped test suite was not run, as the
update's gate and project verification set do not require it. No commit or push
was performed.

## Workshop second update — 2026-10-05

Authorized by the user: "lets update again ) there is another version". Installed
from a fresh upstream clone at `5871845e4a8fface57bf6a9fa9c8e82c5ab61d71`;
the upstream entry contract remains v30. Workshop now announces
`goodwolf-harness@5871845, 2026-10-05`.

The upstream installer ran with `--update --at 5871845`, without overwrite.
It changed five files: the harness declaration, installer, installer tests,
harness skill and stamped entry file. No files were deleted. Both loader links
were kept and resolve. The pre-update snapshot, source, comparison and raw
update/check reports are retained outside this repository at
`D:/Dev/workspaces/taichi_workspace/.local/harness-update-01a10ad8-round2/`.

All 51 compared project records, collaboration assets, local rules, product
entry files and reconciliation surfaces were byte-identical to the snapshot
before this evidence entry was appended. Local/L12 and local/L13 remain installed.

The new upstream comparison recognizes injections from recipient-owned
mechanisms. The prior `/align` limitation is resolved: both the installation
gate and a subsequent fresh `--check` report `arrived: true`, with no differing
core files, injector diagnostics, shape diagnostics or pending link commands.
Whitespace checks pass. No core workaround, commit or push was made.

## Harness commit verification — 2026-10-05

The user authorized committing the harness changes. Installation commit
`6d9a0e5` contains shipped core at `5871845`, its regenerated instruction
surfaces and the preserved local/L12 and local/L13 rules. Other local rule
amendments, reconciliation changes and project records remain uncommitted.

The exact installation selected for commit was assembled from the committed
project baseline plus shipped upstream core and these two local rules. All
three required checks pass on that selection: harness `arrived: true`, injector
with no diagnostics, mechanism shape with no diagnostics. Its source local
rule identifiers were checked after correcting a Windows decoding issue in
the temporary selection; the corrected selection was checked again before
commit. Staging did not replace working files. Evidence is committed separately;
no push was performed.
