---
name: collaborate
description: >-
  Use at session startup to check cross-project assignments, before every change
  affecting documented project boundaries, and whenever coordinating across
  projects or communicating with Workshop.
---

[Workshop](https://github.com/dveyarangi/xuanxue-workshop) coordinates development
across the school's projects and maintains their shared boundary agreements.

Project label: <set from your installation issue>

Use [Workshop Issues](https://github.com/dveyarangi/xuanxue-workshop/issues) for
cross-project collaboration and messages to Workshop, following
[the issue format](workshop-issue-format.md). Internal project work uses the
project's own tracker and rules.

## Installation

1. Read your installation issue. It supplies your project label and the explicitly
   marked `BOUNDARY_SUMMARY` defined in the issue format. Use that block's content
   as the supplied summary; do not reconstruct it from the issue's other prose.
2. Install this file and [workshop-issue-format.md](workshop-issue-format.md)
   together in the location supported by your agent host. Replace the project-label
   placeholder in this file with the label from the issue.
3. Prepare the short boundary summary supplied by the issue for the block below:
   check which connections exist in the code and add the local module names or
   paths. Keep planned connections explicitly labelled as targets. Report any
   disagreement with the supplied description in the installation issue; this
   step does not implement the planned connections.
4. Add the following block to the project's `AGENTS.md` or `CLAUDE.md`, whichever
   the project agent reads. Replace `BOUNDARY_SUMMARY` with the short description
   from step 3 and its contract links, and `COLLABORATE_SKILL_PATH` with the path
   to the installed skill, relative to that file. Preserve existing instructions.

   > ## Workshop collaboration
   >
   > BOUNDARY_SUMMARY
   >
   > Use the [/collaborate skill](COLLABORATE_SKILL_PATH) at the start of every session,
   > before work affecting any boundary described above, and whenever coordinating
   > across projects or communicating with Workshop.

5. Record the source revision and remove this Installation section from the
   installed copy. Preserve the distributable source in Workshop.
6. Verify in a fresh session that the agent invokes the skill, accesses Workshop,
   finds its addressed issues, and recognises boundary-related work from its
   project instructions. Verify the installed format link resolves. Report in
   the original installation issue.

## Check addressed work

In [Workshop Issues](https://github.com/dveyarangi/xuanxue-workshop/issues), find
issues carrying your project label. Read relevant assignments, discussions and
dependencies, including follow-up on reported results. Follow your project's
operator instructions when choosing and executing work.

When an assignment supplies `BOUNDARY_SUMMARY`, use its marked content to update
the summary in the collaboration block of `AGENTS.md` or `CLAUDE.md`, checking it
against the local code and preserving the surrounding rules. If a required summary
is missing or ambiguous, request clarification in the assignment issue.

## Coordinate a boundary change

Read the relevant
[boundary agreements](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/boundaries.md),
the [current-state evidence](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/current-system.md),
and the owning project's executable definitions. Apply the
[contract-evolution agreement](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/agent-contract.md#contract-evolution):
work within the active contract can proceed under your project's authority;
a new version can coexist while the active contract remains fulfilled.

For a new version, open a migration-coordination issue addressed to
`project:workshop`. Coordinate
an incompatible replacement before implementing it; retire the old version only
after all known consumers confirm their transition.

Update the short boundary summary in `AGENTS.md` or `CLAUDE.md` when affected
and include those changes in your report for Workshop reconciliation.

## Discuss problems and report results

Discuss assignment problems in the original assignment issue.

For problems with Workshop itself, use the issue format's duplicate check and address
new issues to `project:workshop`.

Report results and answer follow-up questions in the original assignment issue.

Workshop reviews evidence, updates its records, acknowledges acceptance and
closes the assignment. A project-side closed state does not establish acceptance.
The [agent contract](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/agent-contract.md)
owns the shared responsibilities and recipient labels.
