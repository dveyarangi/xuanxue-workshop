# review-assignments — rules installed into skills

| target | anchor |
|---|---|
| `.agents/skills/coordinate/SKILL.md` | `## Project context` |
| `.agents/skills/reconcile/SKILL.md` | `## Project context` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

## RA1 — review instruction and entry maintenance

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-05, session-entry review and reconciliation connection

<rule>
When maintaining cross-project assignment review, recheck the review-assignments
instruction, declaration, project context and entry bindings with mechanisms.py
--check and inject_rules.py --check. Confirm that entry recovery precedes review
and that direct reconciliation enters the same review without repeating an active pass.
Retain fresh-session invocation and operator grading as separate evidence;
structural checks do not establish them.
</rule>

## RA2 — review before deriving new work

- **target** `.agents/skills/coordinate/SKILL.md`
- **target** `.agents/skills/reconcile/SKILL.md`
- **authority** the user, 2026-10-06, ongoing review in the coordination loop

<rule>
At coordination or reconciliation entry or resumption, use /review-assignments at
.agents/skills/review-assignments/SKILL.md for relevant assignments and incoming
requests unless already reviewed for this pass with no changed relevant evidence.
Reuse an active review supplied by the caller; do not recurse into it. Blockers,
questions and changed dependencies matter before completion reports arrive.
</rule>
