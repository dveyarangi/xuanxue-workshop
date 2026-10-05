---
name: implement
description: Use when agreed work is to be written into code.
---

Mechanism: not yet

Implement the work described by the relevant architecture decisions (spec,
ticket, RFC, prior discussion).

Pick entity names in vibe with the project glossary.
Do not use implementation-shaped names or parameters; orient them at the
function's meaning toward the client.

Use `/tdd` where possible, at pre-agreed seams. Make sure implementation, even
in dummy/degenerate form, fully follows contract surfaces in the docs.

Make methods behind main architectural boundaries clear — they should read
almost as a story explaining the boundary logic, with separate concerns
extracted to properly named sub-methods. Prefer to split submethods by
responsibility.

The code should read as a story. Make sure the main process appears first in
the file, where possible, and main boundaries' implementation reads through
entities, interfaces and submethods used as nouns, adjectives and verbs.

Mark code an open question's answer will change with a comment line beginning
`TODO` that names the question, per the entry file's straw-dog rule, and say so
in the docstring.

Make sure the errors follow error rules.

Make sure to read and follow `/improve-comments` rules. Mark other pending
actions — hotpaths that may need optimization, work with no named successor —
as `TODO` too; without a ticket they are notes, and the listing script reports
them as guesses.

During the work, run the checks in the project's verification set, as
[`/verify`](../verify/SKILL.md#the-verification-set) defines it. `/verify` is the
verification of landed work; a local run of a subset is not that pass.

Once done, and unless you need to take a break, use `/verify`.

Read `commit` from `AGENTS.md`. Do not commit until that switch allows it.
Repair during the work follows the `repair` switch; it is not a substitute
for `/verify`.
