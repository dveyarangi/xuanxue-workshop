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

## Workshop update — 2026-10-08

Authorized by the user: "давай снова обновим харнесс", followed by
"прочитай репу еще раз, возьми последние изменения". The second fresh upstream
clone supplied `8a512d39f47ec09c1e76750ce82de8aad0c35cfc`, upstream v41.
Workshop announces `goodwolf-harness@8a512d3, 2026-10-08`.

The first pass installed `6845964d0509dead967f5eced26adaefa49385d8` (v37).
Its overwrite replaced the local skill-up description with upstream's equivalent
agent-instruction use case. Its new shape validator required a kind header in
five recipient-owned declarations: analyse, coordinate, issue, reconcile and
review-assignments. Each received only
`- **kind** what must always hold`; byte comparison against the first snapshot
confirms that removing that line restores each original declaration exactly.

The second pass used `--update --at 8a512d3`, without overwrite. It changed only
the recall skill, conclude skill and stamped entry file. Neither pass deleted
files. Fresh sources, snapshots, comparisons and verification reports are held
outside this repository in
`D:/Dev/workspaces/taichi_workspace/.local/harness-update-20261008-01a10ad8/`
and its `-round2` sibling.

Preservation comparison covered 93 files before this evidence entry was appended.
Local rules, all 18 recipient-owned mechanism and skill files, distributable
collaboration assets and product entry files match the second snapshot byte for
byte. The only changed project document was `docs/contracts/native-account-session.md`,
edited concurrently by the separate native-session work; this update did not
write or revert it. Both existing loader links resolve to `.agents/skills`.

The installation gate and an independent fresh `harness.py . --check` both
report `arrived: true` at `8a512d3`: no core differences, injector diagnostics,
orphans, shape diagnostics or pending link commands. Separate injector and shape
checks and `git -c core.safecrlf=false diff --check` pass. The shipped test suite
was not run; it is outside the project verification set for this update.

Session recovery and assignment review read all six Workshop issues and their
complete timelines, including relevant linked pull-request state. No new
unhandled report or changed prerequisite required an issue reply. Existing
reviews, queue order and the other session's native-account work were preserved.

## Ownership-test verification finding — 2026-10-08

The user requested another self-verification of Workshop readiness in session
`01a11a58-894d-7d52-af3b-008b2c32b221`. Beyond the project's named installation
gates, the reviewing agent ran the complete shipped standard-library suite:
`uv run --offline --no-project python -m unittest discover -s .agents/scripts/gw/test`.
The unchanged source ran 555 tests in 163.914 seconds: one failure, two skips.
The failing case is
`test_harness.ARefusal.test_gits_own_ownership_check_is_what_the_refusal_reads`.
A targeted repeat reproduced the failure. The full installation comparison at
`8a512d3`, rule injector and mechanism gates still pass; their success does not
establish a clean shipped-suite result.

The test replaces the `os.environ` object through `mock.patch.object`, then
expects Git's real ownership check to see `GIT_TEST_ASSUME_DIFFERENT_OWNER=1`.
On this Windows/Python 3.14 host, a child started without an explicit `env`
inherits the native process environment, not that replacement mapping. A
separate process probe returned `absent` with the replaced object, and `present`
both with an explicit `env` and with `mock.patch.dict(os.environ, ...)`.
The existing Git capability probe uses explicit `env`; the actual harness Git
call inherits it. That difference explains why the capability probe passes but
the action sees an ordinary owned repository. Child injector/shape calls then
receive the replacement mapping explicitly and fail later. The observed failure
does not demonstrate a defective production ownership refusal.

A first candidate using `patch.dict` around the entire existing assertion helper
failed before the action: that helper snapshots the Git index, which also
receives the ownership test knob. The final proposed repair snapshots before
setting the knob, runs only the installation action inside `patch.dict`, restores
the environment, checks its status, single refusal and diagnostic words, then
verifies the snapshot is unchanged. Its targeted run passed one test with no
skips. No helper is generalized and no ownership check or assertion is removed.

The [repair preview](../../.local/readiness-verification-20261008/harness-ownership-test.patch)
and [process probe](../../.local/readiness-verification-20261008/environment-probe.json)
are local diagnostic artifacts. The repair has not been applied to `.agents/` or
the upstream harness repository. The shipped file remains source-identical at
the announced ref. The project's `repair=ask` setting and the harness's source
ownership remain in effect.

The final candidate was also exercised against the complete suite by replacing
only that test method in memory: 555 tests in 120.361 seconds, zero failures,
zero errors, two skips. Both skips explicitly concern this process's lack of
permission to create a symlink. The
[candidate result](../../.local/readiness-verification-20261008/candidate-final-suite.json)
distinguishes this successful proposal check from the unchanged shipped source's
one failing test. No repository test, production function or saved Git setting
was modified.

### Full-tree commit recheck — 2026-10-10

The user authorized committing all accumulated repository changes. The complete
shipped suite ran 555 tests in 102.115 seconds, with the same ownership-fixture
failure above and two symlink-permission skips. The saved test and production
ownership behavior remain unchanged; the preview repair is still a proposal.
This is a repeat of the recorded Windows process-environment limitation, not
evidence of a clean shipped-suite run.

The announced `goodwolf-harness@8a512d3` reference, injector, mechanism, question
and ticket checks pass. A first full-tree injector pass detected redundant staging
copies of instruction files created during commit preparation. Those diagnostic
copies were retained as `.md.snapshot` files, after which the injector and complete
harness gates passed. They are evidence snapshots, not additional instruction homes.

## Workshop update — 2026-10-11

The user authorized bringing in the current harness: "тащи его". A fresh source
clone supplied `909b61ac1673ee330be0d85e15e7e8e682799fe2`, replacing the announced
`8a512d39f47ec09c1e76750ce82de8aad0c35cfc`. Workshop now announces
`Entry contract: goodwolf-harness@909b61a, 2026-10-11.`

The installer first visited `09dd48d189f9eb24271d80271eda764f5f04ee46`, whose hook
shelf identifies the preceding core commands, then installed the target ref.
This let the installer replace the old commands in all three host hook files
without retaining them as project hooks. New commands run the Git shell wrapper
and its recorded Python interpreter directly, without uv. Windows long-path
support was supplied per process; no global Git setting was changed.

The five Workshop mechanism declarations gained the current `record of` field
in place of `kind`. The question writer added the required record mark to all
30 question records; assertions confirmed unchanged identities, questions,
bodies and other metadata. Four live tickets and their queue gained the same
format metadata. Their status, scope and acceptance criteria did not change.
Workshop's own skills and rules remain present, including `step=ask` and the
local greeting handoff. The update does not perform assignment work or publish
issue replies.

Final verification:

- Harness gate: `arrived: true`; source comparison, injector and mechanism shape
  pass, with no differing core files. Both loader links resolve.
- Question store: 30 records, no diagnostics. Similarity suggestions remain
  advisory; this update makes no question-merging decision.
- Tickets: four live records, no diagnostics.
- `git -c core.safecrlf=false diff --check`: passes.
- The actual new Codex command accepts a UserPromptSubmit payload from a nested
  directory and returns the current session's question window.

The shipped unit suite was not run for this update. The direct hook probe does
not establish that the desktop will invoke it in a fresh session; that is the
user's planned greeting trial. Raw receipts, migration assertions and backups
are retained in `.local/harness-update-20261011/`, excluded only in this clone's
Git metadata. No commit or push was made.
