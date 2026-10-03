# ticket — tracks a unit of work as a record with an outcome and observable criteria, from mint to close

- **instruction** `.agents/skills/ticket/SKILL.md` — the act: sizing, slicing, impacting the split, presenting the breakdown, minting
- **state** installed

## How it works

A ticket is a tracked unit of work: an outcome, observable criteria, and the decisions it still
owns, held as one file whose shape is the format shelf's and whose state is a folder. The skill
says how work is sized and sliced into tickets and how a breakdown is approved; the shelf says
what a ticket is as a record — its name, its header, the sections its stage admits, what finishes
it and what removes it; the mover closes a finished ticket with its RFC and repairs every citation
that pointed at them; the maintainer holds every live ticket to the shelf's shape.

**Paired close is a behavior of this mechanism and `/maintain` is its actor.** The duty that a
finished ticket moves is written once, in this mechanism's rules file, and reaches `/maintain` as
an installed block; `/maintain` is not a part of this mechanism, it is the target the duty is
installed into. Two other skills act on a ticket rule in their own work and receive it the same
way: `/plan` names an RFC by its ticket, and `/align` lands a resolved decision in its durable
home and rewrites the ticket in place.

**A ticket holds what is actual at its stage** *(the user, 2026-09-08)*. Until its plan exists it
is incepted and hosts chunks — routed inputs, ideas, open questions. Once its plan exists it is
shaped and keeps the work, its criteria, and only what is still open; a resolved decision lives in
its durable home and in the session record, not in the ticket.

It is **installed**. A tree without it tracks work some other way; the parts table below is what
an installer adds and an uninstaller removes.

The queue's table is still a copy of the ticket headers, amended by hand at every mint, flip and
close, and the shelf's queue section says how. When the queue is derived, that section and the
moment that reads it both go, along with P8, which is wrapped at its own home in the rules file.

**Who decided each rule.** The skill and the shelf carry their rules with no attribution; this doc
carries it. A rule with a name and date is that person's to amend, through `/align`.

| rule | decided by |
|---|---|
| P1 — finished is every box checked, `/verify` included | the user, 2026-09-06 |
| P2, P3 — the pair closes in one invocation; the header is the maintainer's | the install RFC of 2026-09-06, which specified the mover |
| P5 — the records are checked by `tickets.py` | the user, 2026-09-08, owed to `/maintain`'s M1 |
| P6 — an RFC is named by its ticket | the user, 2026-09-08 |
| P7 — a resolved decision leaves the ticket for its durable home | the user, 2026-09-08 |
| P8 — a closed ticket leaves the queue | the user, 2026-09-09 |
| P9 — a ticket is named by a link, or by a slug and its state | the user, 2026-09-21; the slug in the link text, 2026-09-26 |
| P10 — an align on a ticket opens with what the ticket is | the user, 2026-09-27 |
| P11 — the ticket is swept for consistency when the align ends | `/align`'s own text, moved here 2026-09-29 by 01-0011.0100 decision 15 |
| the record's shape — one header form, `Type` required, `Kind` gone, `Outcome` one sentence, the stage read from the plan, the sections a stage admits | the user, 2026-09-08 |
| the status vocabulary, numbering and one basename per work item | with the selected skills, 2026-09-06 |
| check-only, and nothing retires this | the user, 2026-09-08 |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| deciding a chunk is ticket-sized, or needs `/align` or a spec first | `.agents/skills/ticket/SKILL.md` | |
| decomposing a parent into slices, and impacting the split | `.agents/skills/ticket/SKILL.md` | |
| presenting the breakdown for approval under the `breakdown` switch | `.agents/skills/ticket/SKILL.md` | |
| numbering, naming and placing a ticket | `.agents/skills/ticket/TICKET-FORMAT.md` | |
| writing a ticket to the shape its stage requires | `.agents/skills/ticket/TICKET-FORMAT.md` | |
| flipping a status | `.agents/skills/ticket/TICKET-FORMAT.md` | |
| amending the queue's table | `.agents/skills/ticket/TICKET-FORMAT.md` | |
| resolving a decision a ticket owns | `.agents/skills/align/SKILL.md` | |
| naming an RFC for a ticket | `.agents/skills/plan/SKILL.md` | |
| deciding a ticket is finished | `.agents/skills/maintain/SKILL.md` | |
| closing a finished ticket with its RFC | `.agents/skills/maintain/SKILL.md` | |
| repairing the citations a close breaks | `.agents/scripts/gw/move_doc.py` | |
| checking live records against the shape | `.agents/scripts/gw/tickets.py` | |
| listing finished records not yet moved | — | not yet |
| rendering the queue from the tickets | — | not yet |
| ordering the queue and writing its pacing prose | — | not yet |
| promoting an open question of the store into a ticket | `.agents/skills/ticket/SKILL.md` | |
| verifying a ticket's criteria against landed work | — | elsewhere — landing-time agreement is verification, `.agents/skills/verify/SKILL.md` |
| writing an RFC's contents | — | elsewhere — what an RFC holds is planning's, `.agents/skills/plan/SKILL.md` |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| removing this mechanism from a tree | — | not yet |
| reading how a shaped ticket reached its decisions | — | unowned by design — the durable home carries the decision with its provenance and the session record the align; looking it up needs no rule |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/ticket/SKILL.md` |
| format shelf | `.agents/skills/ticket/TICKET-FORMAT.md` |
| the queue's arrival state | `.agents/skills/ticket/QUEUE-ARRIVAL.md` |
| this doc | `.agents/mechanisms/ticket/ticket.md` |
| its rules file | `.agents/mechanisms/ticket/ticket.rules.md` |
| the mover | `.agents/scripts/gw/move_doc.py` |
| the mover's tests | `.agents/scripts/gw/test/test_paired_close.py` |
| the mover's tests | `.agents/scripts/gw/test/test_refusals.py` |
| the mover's tests | `.agents/scripts/gw/test/test_citations.py` |
| the mover's tests | `.agents/scripts/gw/test/test_command_line.py` |
| the mover's tests | `.agents/scripts/gw/test/test_failure_contract.py` |
| the maintainer | `.agents/scripts/gw/tickets.py` |
| the maintainer's tests | `.agents/scripts/gw/test/test_tickets.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| citation reader | `.agents/scripts/gw/docs_corpus.py` | `mechanism-shape`, the one that cannot leave |
| test harness | `.agents/scripts/gw/test/repository.py` | `mechanism-shape` |
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The tickets** — read by `/plan` for what to build, by `/implement` for the same, by `/verify`
  for the criteria, by `/maintain` for whether each is finished, and through citations from every
  record that cites work by its slug.
- **The queue's table** — read at wake by whoever resumes, as the entry file routes them; a copy
  until the queue is derived from the tickets.
- **The maintainer's report** — read by `/verify` through the verification set and by `/maintain`
  under P5. Its exit status is what the set consumes; its JSON is for the person reading a
  failure. It writes nothing.
- **The mover's report** — read by the maintainer who ran it: what moved, what was repaired, what
  it could not rewrite.
- **The rules file** — read by the installer alone, and by whoever amends a rule of this mechanism
  that another skill reads. Its blocks sit in `/maintain`, `/plan`, `/align` and the entry file's
  general rules.

Nothing else; no index of its own. The register of tickets is the queue, which is still copied by hand rather than derived.

## Not yet at the shape

**Four `not yet` rows**, each naming a ticket that exists: the archive listing, the derived
queue, the pacer, the installer.

**The queue's table is still a copy.** The shelf's queue section instructs the copy inside a
straw dog, and the maintainer does not read the queue at all.

**The maintainer reads names in `done/` and nothing else there.** A half-closed pair is caught by
name; an archived record written under an older shelf is never reported, and that is the
exemption working, not a gap.

## What retires this

Nothing. Tracking work is core to the method: a tracker that held the rows would move where the
record lives and would still need the method to say what a unit of work is, how it is sliced and
when it is done *(the user, 2026-09-08)*. The only condition that would retire it is all work being
done, which never arrives. This section states that so nobody re-investigates it.

## What would show it working, graded by someone who did not build it

Two graders, two questions, pre-registered at the align that declared this mechanism and its
`/plan`.

**The session that declares `/plan`**
grades the pairing rule and the `Plan` bullet: did they hold against `/plan`'s own record shape,
or did this doc claim of an RFC what `/plan`'s declaration had to take back? A pairing check that
had to be moved out of `tickets.py` is this doc having claimed too much.

**The session that lands the archive listing**
grades the record declaration as the first reader that was written for: was the shelf's *The
record* enough to read eligibility from — the boxes, the `/verify` box, the folder — or did the
shape have to be amended to make the listing possible? A shape amended by its first reader was
declared for the wrong reader.
