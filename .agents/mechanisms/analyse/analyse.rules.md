# analyse — rules installed into skills

| target | anchor |
|---|---|
| `.agents/skills/coordinate/SKILL.md` | `## Project context` |
| `.agents/skills/reconcile/SKILL.md` | `## Project context` |
| `.agents/skills/review-assignments/SKILL.md` | `## Project context` |
| `.agents/skills/issue/SKILL.md` | `## Project context` |

## AN1 — collect missing or changed project evidence

- **target** `.agents/skills/coordinate/SKILL.md`
- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/review-assignments/SKILL.md`
- **target** `.agents/skills/issue/SKILL.md`
- **authority** the user, 2026-10-06, approved coordination loop

<rule>
When relevant source or runtime evidence is missing or changed, use /analyse at
.agents/skills/analyse/SKILL.md for the affected repository and scope. Reuse facts
whose basis remains valid. Return the observation to the existing work; do not
ask recipients to investigate what accessible sources can establish.
</rule>
