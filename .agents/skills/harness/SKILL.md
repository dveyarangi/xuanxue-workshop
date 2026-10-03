---
name: harness
description: >-
  Use when asked to install the harness into a project, to update a tree that already holds it,
  or to confirm a copy is intact; and in a freshly installed tree, which has core and none of the
  project's own answers yet.
---

The source is always the repository, cloned fresh at a ref; a working tree is never read. Where
that repository is, this tree says once:

Repository: https://github.com/dveyarangi/goodwolf-harness.git

That is the only authored home of it. The script reads its default `--from` there, an install
stamps a recipient's copy with the source the run actually read, and a fork edits the line once
and everything it installs names the fork. A check or an update from another `--from` sets the
line aside rather than reading an edit in core, as it does the local block.

Run the script from any clone of the harness, or from the tree's own copy once it has one:

```
python <clone>/.agents/scripts/gw/harness.py <target> --install [--from REPOSITORY] [--at REF]
python <target>/.agents/scripts/gw/harness.py <target> --update [--overwrite] [--from REPOSITORY] [--at REF]
python <target>/.agents/scripts/gw/harness.py . --check [--from REPOSITORY]
```

`--from` defaults to the harness's own repository; `--at` to its default branch's head, and takes
a branch, a tag or a commit. To try a ref before it is pushed, pass a local clone's path as
`--from`: its committed `HEAD` is then the ref. The target is the top level of a git work tree.

## What a run does

Copies every file under `.agents/` plus `AGENTS.md` and `CLAUDE.md`, and the source's root
`LICENSE` as `.agents/LICENSE`, with the origin's local blocks removed and every straw-dog wrapper sheared so the rule stays and the condition does not;
stamps the entry file's announce line `<repository>@<ref>, <date>`, which is the tree's only
revision record and what every session there announces; makes the loader links; installs every
mechanism's rules and then the project's local file last; and runs the gate — the copy compared
against the ref, the injector's check, the shape check, in seconds. The report ends
`arrived: true` only when all three hold, and says beside it whether each loader link resolves.
The shipped suite is not run; a project that wants it runs it from its own verification set.
Whether a host reads the link is not observable from inside a tree; the first session announcing
the stamped line is the evidence a person reads.

## Refusals, and what to do

Every refusal writes nothing and names its step.

- **A link the platform refused to create** is not a refusal: everything else landed, and the
  report's `pending` lines are the exact commands. Present them to the person verbatim, to run
  once in an elevated prompt, then run `--check`.
- **A `<project-local>` block in the entry file**: its content is the project's and the file is
  overwritten. Move each fact into `local.rules.md` as a rule, delete the block, run again.
- **A core file that differs from the announced ref**: an edit made in core. Keep it out of core
  — a project's answer or override goes in the local file — and run `--update --overwrite`,
  which replaces the file and names it.
- **A tree that announces no ref**: a copy that predates this script. `--update --overwrite` is
  required; nothing is deleted, and files under `.agents/` outside the manifest are reported as
  the project's own.
- **The injector refused**: an override naming a rule this ref no longer sends there, or a local
  anchor a new anchor now follows. Fix the local file, run `inject_rules.py local --install`, then
  `--check`.
- **A junction, a directory or a file where a link goes**: the project's own. Move it; a symlink
  goes there.
- **No readable `Repository:` line beside the script**: with no `--from`, the script cannot tell
  where core comes from. Pass `--from` this once, then restore the line — it is what every later
  run reads.
- **A ref whose harness skill carries no such line**: not the harness, in the same sense as an
  entry file with no announce line. Check the ref, or the repository.
- **The source itself as target**: the origin is never installed into.

## After the first install

The tree has core and no answers. Write `local.rules.md` beside the entry file, in the rules-file
format the entry file's *Project-local* section describes, from the environment you stand in: the
project's facts for the entry file, its autonomy switches, and its verification set — its
typechecker, its tests, every command required of landed work, read off its own toolchain. Then
`inject_rules.py local --install`, and `--check`. A project that wants core re-checked on every
`/verify` names `harness.py . --check` in that set.

`uv run --offline --no-project python` is the harness's own habit; the scripts need only the
standard library, so a bare `python` works.
