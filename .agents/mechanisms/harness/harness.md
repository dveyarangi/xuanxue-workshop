# harness — a project that is not the origin holds core whole, at the ref it announces, and can take a later one

- **instruction** `.agents/skills/harness/SKILL.md` — the four commands, install, update, check and the per-clone links, each refusal and what the person does, the first install's last step
- **state** installed
- **record of** what must always hold

## How it works

Core reaches a tree from a fresh clone of its repository at a ref and never from a working tree,
so what a recipient holds is what a commit holds. The manifest is everything under the core
directory plus the entry file, the host stub and the license; the project's local file is never
in it, which is what lets a redeploy overwrite core's content and nothing of the project's. What ships is
transformed before a byte is written: the origin's local blocks removed, every straw-dog wrapper
and every `TODO`'s question binding sheared with the content kept, the announce line stamped, and
the whole held to the leak rule the origin's check applies.

**The announce line is the revision.** A recipient's entry file reads
`Entry contract: <repository>@<ref>, <date>.`; every session there announces it, the check reads
it, and the shape check reads its `@` to know it stands in a recipient — where an unbound
`not yet` is upstream's gap and draws nothing. No record file: integrity is asked of the source,
by cloning the announced ref again and comparing. A change to the transformation therefore reads
as an edit in every recipient installed before it, until it updates. What the announced ref
shipped is read under the transformation alone, never held to today's shipping refusals: those
govern what may leave now, and a rule added after a ref shipped would otherwise strand every tree
that took it.

**The repository line is the source, as the announce line is the ref.** The harness skill carries
`Repository: <url>`, the only authored home of where core comes from: the script keeps no
constant and reads its default there, an install stamps a recipient's copy with the source the
run actually read — a URL verbatim, a path resolved absolute — and a fork edits the line once and
everything it installs names the fork. Both lines are the recipient's own facts living in core
files, so both are set aside when a copy is compared: a check or an update run from another
`--from` reads no edit in core. So is every block the recipient's own installer put in a core
file: its local block, and the block of a mechanism of its own, one whose rules file stands in
the tree and never shipped. A block no rules file owns is an edit. A stamped source is never a citation either, which the citation
reader settles for every reader of it, so a clone kept under a `docs/` directory does not make a
recipient fail its own shape check.

**Every refusal writes nothing**, and the loader links are the one step a person may finish by
hand: where the platform refuses to create a symlink, the run finishes everything else and ends
with the exact elevated command. Nothing is substituted for a link; a junction is refused by name.
A link that stands is removed only once its replacement exists, and one written to the skills
directory is kept even by a process that cannot see through it.

**The gate is the check, and it takes seconds.** Arrival and any later day's question are one
function: the copy against the ref, the injector's check, the shape check — the target's own
scripts, run as subprocesses, so what is checked is what arrived. The loader links are reported
beside the verdict and never decide it: a link the platform refused is the person's one
remaining step, and its command is already in the report. The shipped suite is not run here —
it costs minutes, and an install is seconds — a recipient that wants it names it in its own
verification set *(the user, 2026-09-21)*. The gate itself clones the source whole, over the
network, at every run. A copy drifting from its ref is maintenance's to find, never
verification's *(the user, 2026-10-09)*; no maintain pass runs the
gate: one is offered to the person, with its reason, only once the comparison reads no network and
takes no clone.

It is **installed**; a tree without it holds no core at all. The repository's root `README.md`
is not a part: it never ships, and a recipient has its own.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| installing a ref into an empty tree | `.agents/scripts/gw/harness.py` | |
| updating a tree that has a copy | `.agents/scripts/gw/harness.py` | |
| checking a copy against the ref it announces | `.agents/scripts/gw/harness.py` | |
| making a loader link, or handing the person the command | `.agents/scripts/gw/harness.py` | |
| reading a refusal and resuming | `.agents/skills/harness/SKILL.md` | |
| populating the local file after the first install | `.agents/skills/harness/SKILL.md` | |
| pointing a tree at another core, as a fork does | `.agents/skills/harness/SKILL.md` | |
| re-checking a recipient's copy against its ref in a maintain pass | — | not yet |
| knowing an update is available | — | unowned by design — a person asks for one; nothing polls the repository |
| verifying that a host reads the loader link | — | not yet |
| writing a fresh tree's delivery status | `.agents/scripts/gw/harness.py` | |
| opening a fresh tree's store with its roots, by the store's seed | `.agents/scripts/gw/harness.py` | |
| merging core's hook wiring into each host's file | `.agents/scripts/gw/harness.py` | |
| recording, per clone, the interpreter the hooks run under | `.agents/scripts/gw/harness.py` | |
| removing one mechanism from a tree | — | not yet |
| sending a change back to the repository | — | not yet |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/harness/SKILL.md` |
| this doc | `.agents/mechanisms/harness/harness.md` |
| the script | `.agents/scripts/gw/harness.py` |
| its tests | `.agents/scripts/gw/test/test_harness.py` |
| the entry file | `AGENTS.md` |
| the host stub | `CLAUDE.md` |

The entry file is this mechanism's whole file; two lines inside it are the shape's anchored
parts, and nothing asks about the overlap. The license ships and is not a row: it lives at the
source's root and at a recipient's `.agents/LICENSE`, and a row names one path that the shape check
reads in every tree. The loader links are made by this mechanism and are not its parts: they are the host's way in, never shipped, and a link a platform has refused
would otherwise fail the shape check for the same absence the report already names.

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| citation reader | `.agents/scripts/gw/docs_corpus.py` | `mechanism-shape`, the one that cannot leave |
| the delivery status's arrival state | `.agents/skills/ticket/QUEUE-ARRIVAL.md` | `ticket`, which owns the record and words it |
| the store's seed, its shelf and its reader | `.agents/scripts/gw/questions.py` | `questions`, which owns the store and words its roots |
| the hook wiring's directory, each file at its host file's path | `.agents/scripts/gw/questions.py` | `questions`, which words the hooks |
| the shape check | `.agents/scripts/gw/mechanisms.py` | `mechanism-shape` |
| test harness | `.agents/scripts/gw/test/repository.py` | `mechanism-shape` |
| the listing script | `.agents/scripts/gw/straw_dogs.py` | `maintain` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The recipient's core** — *what exists* — read by its every session, through the loader links its hosts
  follow.
- **The stamped announce line** — *what exists* — announced by the recipient's first reply; read by `--check` and
  `--update` to know what was installed, and by the shape check to know it stands in a recipient.
- **The report** — *what exists* — read by whoever ran the script. Its `pending` lines are read by
  the person who runs them.
- **A fresh tree's delivery status** — *what it intends to become* — read by the first session's `/recall`, which runs before
  anything has been written into the queue; worded by the `ticket` mechanism, placed here, and the
  instance's from its first line.
- **The stamped repository line** — *what must always hold* — read by the script whenever a run is given no `--from`,
  including the recipient's own copy at its own `--check`; and by a person or a fork asking where
  this tree's core comes from, or pointing it somewhere else.
- **Each host's hook file, core's entries merged in** — *what exists* — read by that host at session
  start and before each message, and by `--check`, which compares core's entries alone.
- **The interpreter record**, in the clone's Git directory — *what exists* — read by the hooks'
  wrapper before every hook; made by the link step, so `--links` is the one step a fresh clone runs.
- **The pending command** — *what exists* — read by a person, once, in an elevated prompt.

No record. The two stamped lines are the tree's, and nothing else is kept.

## Not yet at the shape

**The transformation is unguarded.** A change to the shear, the stamp or the local-block strip
reaches every recipient as a reported edit; nothing checks a change against the recipients that
exist.

## What retires this

A host that reads a repository directly at a ref, so that nothing need be copied and the ref is
the tree's by construction. Until then a copy is the only way core reaches a tree, and the copy
needs a revision and a check.

## What would show it working, graded by someone who did not build it

**The user, in a tree that took the harness by hand** at a version its entry file still announces
and has built on the copy since. It writes its answers into a local file, takes an update from the
repository, and the user grades: its local file survives byte-identical and its blocks are
restored last; its `docs/` is untouched; its links resolve; its announce line names the ref; the
gate passes, or says which of the three did not. An install that had to be hand-finished to reach
`arrived: true` reads identically to success in the report, and only the grader can say which it
was.
