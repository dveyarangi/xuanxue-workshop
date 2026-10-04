# Boundary reconciliation evidence

2026-10-04. Scope: the reconciliation portion of
[workshop-coordination-ready](../tickets/01-0005-workshop-coordination-ready.md).

The [/reconcile skill](../../.agents/skills/reconcile/SKILL.md) replaces the
discussion draft. Its declaration is under `.agents/mechanisms/reconcile/`.
`local.rules.md` owns the project source pointers and the invocation installed
into the /maintain skill. The distributable procedure contains no project names
or copied boundary descriptions. Issue formatting remains in
[the shared format](../../skills/collaborate/workshop-issue-format.md).

## Verification

- Rule installation and mechanism checks pass with no diagnostics.
- Harness comparison against `goodwolf-harness@ebde4ab` passes; the new mechanism
  and skill are additions, and existing core changes are installed local rules.
- An isolated temporary copy passes both checks. Altering the maintenance
  invocation makes the rule check fail; removing the declared skill makes the
  mechanism check fail; restoring both makes both checks pass again (4 assertions).
- These checks establish structural installation, not the semantic correctness
  of every boundary or a completed end-to-end agent integration.
- Final question-store, ticket and straw-dog checks pass without diagnostics;
  `git diff --check` reports no whitespace errors. Of 135 local Markdown link
  targets inspected, 134 resolve and one is the documented installation placeholder
  `COLLABORATE_SKILL_PATH`. No obsolete draft links remain in the inspected scope.

## Outstanding evidence and publication

The separate Workshop startup-review skill and both project agents' installations
remain unverified. Host loader links for Claude and Cursor are absent; host skill
discovery was not tested. No application code or deployed behavior was changed
or tested in this maintenance pass.

GitHub inspection found the Workshop repository empty and installation issues
open, without recipient labels, still referring to the earlier skill path.
README now links to those existing issues directly. Revised bodies with explicit
`BOUNDARY_SUMMARY` blocks were prepared for review. Automatic approval review
initially blocked creating the recipient labels and assigning them.

After explicit user approval on 2026-10-04, Workshop created `project:cabinet`,
`project:daychi` and `project:workshop`, updated
[cabinet-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
and [daychi-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/2),
and applied their recipient labels. Readback confirmed that both bodies match the
approved files and both assignments remain open and Planned, awaiting publication
and Workshop readiness. This does not complete the readiness ticket or the
first-stage goal.
