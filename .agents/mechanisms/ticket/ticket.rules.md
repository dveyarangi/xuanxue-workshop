# ticket — rules installed into skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/plan/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/align/SKILL.md` | `### Record resolutions in the owning ticket inline` |
| `AGENTS.md` | `## General rules` |
| `.agents/skills/recall/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/ticket/SKILL.md` | `### 1. Locate the parent` |

## P1 — finished is every box checked

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-06

<rule>
A ticket is finished when every acceptance box is checked, the verification box included.
</rule>

## P2 — the pair closes in one invocation

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the install RFC of 2026-09-06, which specified the mover

<rule>
Close a ticket and its RFC together, in one invocation, and every eligible pair in the same
invocation: `move_doc.py [--dry-run] SRC DST [SRC DST ...]`, into `docs/tickets/done/` and
`docs/rfc/done/`.
</rule>

## P3 — the header is the maintainer's

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the install RFC of 2026-09-06, which specified the mover

<rule>
Update the ticket header yourself; the mover changes no checkbox, status, date or prose and
leaves the Git index alone. Treat a refusal as a finding. Repair or deliberately leave what it
reports it cannot rewrite, and say which. Git recovers committed or staged content only.
</rule>

## P5 — the records are checked by their maintainer

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-08

<rule>
Check the ticket records with `tickets.py --check` — format never content, live rows only. A
diagnostic is a finding; repair it under the repair policy.
</rule>

## P12 — the live tickets are read from the list

- **target** `.agents/skills/recall/SKILL.md`
- **target** `.agents/skills/ticket/SKILL.md`
- **authority** the user, 2026-10-10

<rule>
Read the live tickets with `tickets.py --list` before ordering the queue or minting a ticket.
</rule>

## P6 — an RFC is named by its ticket

- **target** `.agents/skills/plan/SKILL.md`
- **authority** the user, 2026-09-08

<rule>
Name the RFC by the owning ticket's basename, under `docs/rfc/`, with no serial of its own; it
moves to `docs/rfc/done/` with the ticket.
</rule>

## P7 — a resolved decision leaves the ticket for its durable home

- **target** `.agents/skills/align/SKILL.md`
- **authority** the user, 2026-09-08; against the store, 2026-10-03; the owner first, 2026-10-04

<rule>
Land a resolved decision in its durable home with its provenance, and rewrite the ticket in
place to what is now true; close the question it answers against that home — against the ticket's
decision while it has not landed, after assigning the question to the ticket if it has no owner —
and when a decision lands, repoint every entry closed against it there.
</rule>

## P10 — an align on a ticket opens with what the ticket is

- **target** `.agents/skills/align/SKILL.md`
- **authority** the user, 2026-09-27

<rule>
Open an align on a ticket by saying what the ticket is: what it builds and the problem it answers,
in plain words, each of its terms explained, before the necessity gate or any question.
</rule>

## P11 — the ticket is swept for consistency when the align ends

- **target** `.agents/skills/align/SKILL.md`
- **authority** `/align`'s own text, moved here 2026-09-29

<rule>
Sweep the ticket for internal consistency at the end: an early section may still assert what a
later resolution changed.
</rule>

## P9 — a ticket is named by a link, or by a slug and its state

- **target** `AGENTS.md`
- **authority** the user, 2026-09-21; the slug in the link text, 2026-09-26; each reply on its
  own, 2026-10-10

<rule>
In every reply and every record, the first mention of a ticket — a table's cell included — is a
link to its record whose text carries its slug, its whole id leading it if at all; later mentions
in that reply or record may be the whole id alone. Name one that has no record yet by a slug and
its state word.
</rule>
