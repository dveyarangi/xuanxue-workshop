# Harness evidence

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
