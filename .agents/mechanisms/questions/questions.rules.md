# questions — rules installed into the entry file and skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## General rules` |
| `.agents/skills/recall/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/conclude/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

## Q1 — every message is placed before it is answered

- **target** `AGENTS.md`
- **authority** the user, 2026-09-28 to 2026-10-03 — 01-0011.0100 decisions 25, 32, 39, 44, 45, 46, 47 and 56

<rule>
Before drafting a reply, place the message in the question store: read this turn's window — the
one the host's hook put in your context, or `questions.py --window --session <tag>`, the script
being `.agents/scripts/gw/questions.py` — and call `questions.py at q-N --session <tag>` where the
message lands, and the store's other calls whenever the turn's own work settles, opens or moves a
question:

- `questions.py at q-0004 --session <tag>`
- `questions.py open '<question>' --under q-0004 --session <tag>`, which prints the id it gave
- `questions.py close q-0004 decided '[link](../path.md) — who, date' --session <tag>`

Before opening a question, look for its answer in the docs and the code: found, point to it and
open nothing; not found, open it. A message that lands nowhere makes no call. Only the working
agent calls, never a helper. Under `debug=on`, head the reply with a one-cell table holding a row
for each question the turn stood on, in order, the first over `|---|`: `| ↳ **q-N** · <its
question as the window writes it> |` for the one the turn ends on, `| ✓ **q-N** · <question>
(<kind>: <its answer>) |` for one closed in it, the question alone for one it left open. For any
other call, a closure, a branching or a drop, read the questions skill.
</rule>

## Q2 — the wake opens at where the work stands

- **target** `.agents/skills/recall/SKILL.md`
- **authority** the user, 2026-09-29 to 2026-10-03 — 01-0011.0100 decisions 38, 39, 44 and 56

<rule>
Start from the wake's read — the one the host's session-start hook put in your context, or
`questions.py --wake`. Report where the other sessions stand, what is suspect, and which
deferrals may now be due; take this session's position from the person or estimate it, and
place it with `at`. Re-rank nothing another running session is on; then read the queue as this skill says.
</rule>

## Q3 — the conclude writes the leans and ends the session

- **target** `.agents/skills/conclude/SKILL.md`
- **authority** the user, 2026-09-29 and 2026-10-03 — 01-0011.0100 decisions 38 and 56

<rule>
Write a lean line on each question the session touched and left open —
`questions.py lean q-N '<line>' --session <tag>` — and nothing else: placements and closures were written as they
happened. As the conclude's last act, run `questions.py --end --session <tag>`.
</rule>

## Q4 — the store is checked, and finished subtrees archived

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-29 — 01-0011.0100.0010 RFC item 4, for M1's duty

<rule>
Check the question store with `questions.py --check`. A diagnostic is a finding; repair it under
the repair policy. Move each subtree it reports ready for `done/` with `move_doc.py`, every entry
of the subtree in one invocation, into `docs/questions/done/`.
</rule>

## Q5 — a question is named by its id and its words

- **target** `AGENTS.md`
- **authority** the user, 2026-10-03 — rule failure 17

<rule>
The first time a reply names a question, write its id with its question as the window writes it;
later mentions may be the id alone. A question the store does not hold yet is written out, never
named after the ticket it will belong to.
</rule>
