---
name: maintain
description: >-
  Use to hold a declared scope of the tree in agreement — docs to the
  meta-rules, docs to their implementation, records to their format, every
  fact to one home — and to repair the drift; also to retire an expired straw
  dog or archive a finished record. Drift only: a landed slice is verified,
  not maintained.
---

One pass over a declared scope. The scope decides which rules apply.

## Hold

- **A1** Hold four things in agreement: docs to the meta-rules and their format; docs to their
  implementation, both ways; live records to their declared format; every fact to one home.
- **A2** Maintain drift only: a governing side that moved with no landing behind it, or clean
  landings that no longer agree. A landed slice is verified, not maintained.
- **A3** When a governing side moves, re-check what it governs, upper link first: the mechanism
  shape, then a mechanism's doc and rules, then its records. Do not stop at the link you were
  sent for.
- **A4** Read dueness from `maintain.py --check` at the start of every pass. Do not infer it.

## Scope

- **B1** Declare the scope first — the tree, a project, or one work item with its consumers and
  governing docs — and write it into the report.
- **B2** Certify only what you examined; mark nothing checked that was not. Route a finding
  outside the scope to the record that owns its subject — the open issue that already holds it,
  else the owning work item, else `/align` — after searching the open issues, so a finding
  already held is cited, not rewritten.
- **B3** Archive every finished record, whatever scope you declared. The record's format says
  what finished means and where it goes.
- **B4** Re-check every mechanism the check reports due or never maintained, whatever scope you
  declared: its doc against the meta-rules at `rules`; its records against its doc and format at
  `output` — the live ones, and historical ones where a mechanical change stays in this tree, never
  records on a remote board.

## Judge

- **C1** Decide that a record is finished yourself; scripts move and check form, never decide.
- **C2** Decide whether a straw dog's condition holds from observable evidence. The tool never
  interprets an `until`; report an unresolved condition as unresolved.
- **C3** Before removing a straw dog, rehome what outlives it, children before parent. Write
  what is then true where the block was.

## Repair

- **D3** Preserve the facts an archived record records. Never invent a past fact; never imply a
  later requirement was met at the time.
- **D4** Treat a mechanical repair that stopped partway as unfinished: inspect the files against
  what it reported done and pending, finish under the repair policy, and never report a repair
  that did not finish.

## One home per fact

- **E1** Replace a restatement with a pointer. A summary that points deeper is not a duplicate.
- **E2** Let live records carry duplicate context; their indexes may not.
- **E3** Do not cite a record for architecture in a core document.

## Straw dogs

- **T1** List with `straw_dogs.py docs AGENTS.md local.rules.md .agents README.md`. Any diagnostic fails the run;
  zero straw dogs is clean.
- **T2** Remove one you have judged obsolete with `--remove FILE:LINE --expect <fingerprint>`.
  A straw dog holding a nested one is refused: dispose of the children, scan again.
- **T3** Guess with `--guess` over the scope you declared, and judge each candidate: wrap and
  bind it, or leave the claim it is.

## Installed from other mechanisms

One rule of `/spec`'s, held here by hand until that mechanism is declared and installs it:

- **P4** Before archiving a spec, confirm its surviving agreements have homes, its obligations
  have dispositions, and its open issues keep owners.

<installed by="mechanism-shape">
**R1** Check a record-bearing mechanism's records with its maintainer script — format never
content, live rows only. Where the script is missing, write it: that is the maintenance.

**R2** Compare a mechanism against what governs it with line endings normalised, its evidence
excluded, and installed blocks excluded.

**R3** Move story out of a doc into its evidence.

**R4** Render an index on request; never commit one beside its records. A file listing what other
files each say for themselves is an index, whatever it is called — an allowlist, a register,
a manifest — and each entry belongs at its authored home, wrapped there if provisional.
</installed>

<installed by="ticket">
**P1** A ticket is finished when every acceptance box is checked, the verification box included.

**P2** Close a ticket and its RFC together, in one invocation, and every eligible pair in the same
invocation: `move_doc.py [--dry-run] SRC DST [SRC DST ...]`, into `docs/tickets/done/` and
`docs/rfc/done/`.

**P3** Update the ticket header yourself; the mover changes no checkbox, status, date or prose and
leaves the Git index alone. Treat a refusal as a finding. Repair or deliberately leave what it
reports it cannot rewrite, and say which. Git recovers committed or staged content only.

**P5** Check the ticket records with `tickets.py --check` — format never content, live rows only. A
diagnostic is a finding; repair it under the repair policy.

**P8** Delete the ticket's row from the queue when you close it. The queue is delivery status, and
`docs/tickets/done/` is where finished work is enumerated; a row for an archived ticket is a
second home for what that folder already says.
</installed>

<installed by="questions">
**Q4** Check the question store with `questions.py --check`. A diagnostic is a finding; repair it under
the repair policy. Move each subtree it reports ready for `done/` with `move_doc.py`, every entry
of the subtree in one invocation, into `docs/questions/done/`.
</installed>

<installed by="local">
**L8** For maintenance of Workshop's project or boundary records, invoke the /reconcile
skill at .agents/skills/reconcile/SKILL.md before the final report. Include its
boundary comparisons, record changes, issue links and unresolved evidence in
that report. Check its declaration and installed bindings with the existing
mechanisms.py --check and inject_rules.py --check commands.
</installed>

## Finish

- **F1** Run the checks in the project's verification set that the scope touched.
- **F2** Report: the declared scope, what was checked, what was repaired and against which
  rule, what moved, the marks written, what remains open and who owns it, and what you did not
  cover.
- **F3** Do not verify landed work; a close needs verification to have already happened.
- **F4** Mark each level you re-checked, as the step that closes it and before the report:
  `maintain.py --mark <mechanism> <level> <outcome>`. Mark nothing you did not re-check. An edit
  made between the re-check and its mark is cleared unread.

## Marks

The marks' format is [MARKS-FORMAT.md](./MARKS-FORMAT.md).
