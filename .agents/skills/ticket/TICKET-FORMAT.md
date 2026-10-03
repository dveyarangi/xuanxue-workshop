# Ticket format

This shelf owns ticket naming, delivery-state vocabulary, the shape of a
ticket as a record, and how to amend the queue table in
`docs/tickets/README.md`. What an RFC *contains* is `/plan`'s.

## Numbering

```
docs/tickets/done/01-0010.0010-life-informs-dev-harness.md
              │  │    └── slug — what the ticket is. Never changes. Cite by this.
              │  └─────── position — global. Changes when priority changes.
              └────────── release — the contract the ticket serves.
```

- Names are `01-NNNN-slug.md`. Positions step by 10. Insert by splitting the
  difference: `0015`, then `0012`. Positions stay four digits — longer numbers
  break numeric ordering. When the gap is exhausted, take the nearest free
  slot on the correct side and note the placement in the queue row. Never
  renumber anything else.
- Allocate a position where the ticket will actually be worked, not merely at
  the end, checking both `docs/tickets/` and `docs/tickets/done/` for the
  surrounding positions.
- A child appends a four-digit position: `01-0010.0010`. Depth is unbounded
  and means "is a child of", nothing else — work merely filed after `0010`
  takes `0020`.
- A release closes when its contract's criteria are met, not on a date. A
  later release's ticket may land first.
- Completed tickets keep their number.

### One basename per work item

A ticket and its RFC share a basename. Cite by slug through a relative link;
add the `done/` segment when the target completes. The filename never
changes, only the folder.

When every acceptance box is checked, including `/verify`, move the ticket to
`docs/tickets/done/` and its RFC to `docs/rfc/done/`, and repair the
citations that pointed at them. A paired close (ticket + RFC) is one pass —
one invocation, so each moved record cites the other's final home:

```
uv run --offline --no-project python .agents/scripts/gw/move_doc.py \
    docs/tickets/RR-NNNN-slug.md docs/tickets/done/RR-NNNN-slug.md \
    docs/rfc/RR-NNNN-slug.md docs/rfc/done/RR-NNNN-slug.md
```

The mover repairs citations and touches nothing else — no checkbox, no
status, no date, no Git index. Eligibility, the ticket header and the queue
row are yours. [/maintain](../maintain/SKILL.md) owns the surrounding pass.

Artifacts predating this keep their names.

## Status

`Done` · `In progress` · `Ready` · `Partial` · `Planned` · `Blocked`

- **Ready** — dependencies complete, work can start. **Planned** —
  dependencies are not.
- **Partial** — some behavior landed; criteria remain open.
- **Blocked** — stuck for a reason *other than* an incomplete dependency.
  Waiting on a dependency is `Planned`.
- One parenthetical qualifier is allowed: `Planned (own align precedes)`,
  `Ready (aligned 2026-09-08)`. `Done`'s parenthetical opens with its date;
  words may follow after a comma: `Done (2026-09-08, split)`.

## The record

A ticket is a record of the ticket mechanism, and this section is its
declared shape — what `tickets.py --check` holds every live ticket to, format
never content *(the user, 2026-09-08)*.

- **A record** is one ticket file under `docs/tickets/`, live until paired
  close moves it to `done/`. **Tier 2**: read when the ticket is planned,
  implemented or verified, or through a citation. **What removes an entry**:
  paired close, when every acceptance box is checked, the `/verify` box
  included. Archived records are matched by name for pairing and exempt from
  everything else; older fields in them are left, and a live record carries
  none.
- **The stage** is read from the `Plan` bullet. *Incepted*, before its plan
  exists, a ticket hosts chunks: routed inputs, ideas, open questions, any
  section. *Shaped*, once its plan exists, it keeps only what is actual. A
  resolved decision lands in its durable home with its provenance and
  rewrites `What to build` in place; `Open issues` holds only what is
  unresolved; the session record holds the align. A checked box with its date
  is the whole verification record — no delivery log, no verification
  narrative.

### The header

The bullet list at the first non-blank line after the title, one form,
ending at the first line that is neither a bullet nor an indented
continuation. Known fields in this order, a one-off field anywhere before
`Outcome`, `Outcome` last:

```md
# {Title}

- **Status:** {value} {(qualifier)}
- **Type:** HITL | AFK
- **Plan:** [{title} RFC](../rfc/{basename}.md) — what it selected
- **Depends on:** [{title}](./RR-NNNN-slug.md) ({what it supplies})
- **Blocks:** [{title}](./RR-NNNN-slug.md) — {why}
- **Outcome:** {the delivered change, one sentence}
```

| Field | Presence | Checked | Written |
|---|---|---|---|
| `Status` | required | a [status](#status) value with at most one parenthetical; `Done`'s opens with the date | |
| `Type` | required | `HITL` or `AFK` | `HITL` needs a human decision or review; `AFK` merges unattended. |
| `Plan` | exactly when an RFC with the ticket's basename exists under `docs/rfc/` or its `done/` | its link resolves to that RFC | plus one clause on what it selected |
| `Depends on` | optional | every link resolves | blockers, each with a parenthetical naming what it supplies — not a bare link |
| `Blocks` | optional | every link resolves | only when the blocking relation is itself an argument; carries its `— why` |
| one-off fields | optional | every link resolves | `Trigger`, `Related`, `Owning decision` and the like, when the ticket carries that fact |
| `Outcome` | required, last | one sentence | observable behavior, never code shape |

`Kind` is not a field. Older tickets use `Legacy id:` / `RFC:` / `Parent PRD`
/ `User stories addressed`; they are archived, leave them.

### The sections

- `Title` — names the outcome, not the mechanism. No number, no release.
- `Parent` — the spec or coarse ticket this was carved from; otherwise the
  durable doc owning the context. Never a session. A subticket says which
  slice it is and what the parent keeps.
- One narrative section — titled for the claim it argues. Diagram the
  mechanism; link the evidence. Say what is deliberately *not* a defect. Omit
  when the framing is uncontested.
- `What to build` — **required**. End-to-end behavior, not a file-by-file
  plan. Each constraint carries its reason. Rewritten in place as decisions
  land.
- `Open issues` — the unresolved decisions and HITL forks, one bullet each,
  saying why it cannot be answered yet. Nothing resolved stays here.
- `Acceptance criteria` — **required**. Checkboxes, each observably true when
  done; one names `/verify`. Provisional criteria say so in the heading, after
  a dash, and are firmed in place at the align.
- `Out of scope` — what a reader expects and won't find, each with its actual
  home.
- `Parent scope addressed` — the parent's stories or criteria this closes, by
  number. The record of the split the user approved; nothing derives coverage
  from it yet.

An incepted ticket may hold any section besides the two required. A shaped
ticket holds the six named above and at most one narrative, nothing else;
its `Acceptance criteria` holds checkbox lines, their continuations and blank
lines, nothing else.

### Acceptance criteria

- Behavior altitude, always: types, fields, formulas and module layout are
  the RFC's.
- Name the instrument when the naive check would pass for the wrong reason.
- Refactor tickets: behavior unchanged, the new constraint machine-enforced
  by a failing guard test, dependents unblocked.
- A parent split into subtickets states the end-state that holds only when
  all children land.
- Check a box only for work that satisfied it; a criterion satisfied early is
  checked with a date.
- Every ticket includes a `/verify` criterion. A ticket is not Done until
  `/verify` has been run against it. Do not move to `done/` without it.

### Pairing

For every file under `docs/rfc/` or `docs/rfc/done/`, a ticket with the
same basename exists under `docs/tickets/` or `docs/tickets/done/`, and both
sit in the same folder state. Only names are read; nothing inside an RFC is.

### Conventions

- Cite by slug through a relative link; add the `done/` segment when the
  target completes.
- Reference the architecture, ADRs, glossary, open questions and edge records;
  never restate them.
- Date a criterion checked early and a status flip; nothing else accretes.
- Update the queue in the same pass.
- Wrap at ~100 columns.

## The queue

The queue is `docs/tickets/README.md`. `/ticket` amends **the table** in the
same pass as minting, a status flip, or a completion. Pacing prose around
the table (`Completed step`, `Current pass`, `Current stage`, working-document
pointers) is not the table; leave it in place, do not restate it here, and
do not replace it with another skeleton.

```md
| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Title](./RR-NNNN-slug.md) | Ready | HITL | {verbatim from the ticket header} |
```

| Field | Rule |
|---|---|
| `Last updated` | The date **delivery state** last moved, not the date the file was last touched. A copy-edit or a link repair does not advance it; a status flip, a minted ticket, or a reorder does. |
| `Ticket` | Relative link to the ticket. The row is deleted when the ticket closes: `done/` enumerates finished work, and the queue is delivery status. |
| `Status` | A [status](#status) value, including an allowed qualifier. |
| `Type` | `HITL` or `AFK`. |
| `Outcome` | Copied verbatim from the ticket header. |

When minting, add a row where the ticket will actually be worked. When
status, type, or outcome changes, update the row. When completing, delete the
row; the closing pass carries that duty as an installed rule. Do not add
columns.
