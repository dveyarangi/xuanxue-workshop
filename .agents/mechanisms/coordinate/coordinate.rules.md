# coordinate — rules installed into skills

| target | anchor |
|---|---|
| `.agents/skills/coordinate/SKILL.md` | `## Project context` |
| `.agents/skills/analyse/SKILL.md` | `## Project context` |
| `.agents/skills/reconcile/SKILL.md` | `## Project context` |
| `.agents/skills/issue/SKILL.md` | `## Project context` |
| `.agents/skills/review-assignments/SKILL.md` | `## Project context` |
| `.agents/skills/align/SKILL.md` | `</supporting-info>` |
| `.agents/skills/ticket/SKILL.md` | `## Layout` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

<straw-dog question="q-0002.0002.0001">
## RC1 — shared boundaries and project ownership

- **target** `.agents/skills/coordinate/SKILL.md`
- **target** `.agents/skills/analyse/SKILL.md`
- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/issue/SKILL.md`
- **target** `.agents/skills/review-assignments/SKILL.md`
- **target** `.agents/skills/align/SKILL.md`
- **target** `.agents/skills/ticket/SKILL.md`
- **authority** the user, 2026-10-04; coordinator ownership, 2026-10-06

<rule>
For cross-project work, state shared boundary guarantees and observable acceptance
outcomes. Projects own executable definitions and internal mechanisms; the shared
contract fixes their externally observable shape. Inspect implementation details to verify guarantees; bring them to
alignment when they reveal an unresolved shared obligation or require changing
accepted ownership, behavior, compatibility or scope.
</rule>
</straw-dog>

## RC2 — one prescribed shared shape

- **target** `.agents/skills/coordinate/SKILL.md`
- **target** `.agents/skills/analyse/SKILL.md`
- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/issue/SKILL.md`
- **target** `.agents/skills/review-assignments/SKILL.md`
- **target** `.agents/skills/align/SKILL.md`
- **target** `.agents/skills/ticket/SKILL.md`
- **authority** the user, 2026-10-05; coordinator ownership and full recipient context, 2026-10-06

<rule>
Cross-project implementation assignments prescribe one fully specified contract
through an accessible immutable authority and common conformance cases. Apply
.agents/skills/coordinate/CONTRACT-SHAPE.md to every applicable dimension, with a
reason for inapplicability. Leave no recipient choice that can change shared
formats, parameters, meanings, guarantees or interoperability. Internal designs
may differ. Each recipient's brief and cited authority must suffice without
Workshop session context; compatible implementations must follow from the briefs.
An incomplete shared shape blocks implementation publication, including Planned
issues. Design/evidence requests cannot substitute for this gate.
</rule>

## CQ1 — shared quality through the loop

- **target** `.agents/skills/coordinate/SKILL.md`
- **target** `.agents/skills/analyse/SKILL.md`
- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/issue/SKILL.md`
- **target** `.agents/skills/review-assignments/SKILL.md`
- **target** `.agents/skills/align/SKILL.md`
- **target** `.agents/skills/ticket/SKILL.md`
- **authority** the user, 2026-10-06, approved coordination loop

<rule>
For cross-project work, apply .agents/skills/coordinate/VALIDATION.md during
inception and validation. Establish clarity for the next reader, consistency
with governing agreements and related work, and completeness of scoped obligations.
Derive recipient tasks from the same contract and ownership; assess individual
understanding and set-wide coverage. Revalidate affected meanings after edits.
Reduce process steps, never context required for compatible implementations.
Reuse valid evidence; stage changes add no approval.
</rule>

## CQ2 — re-enter the existing coordination pass

- **target** `.agents/skills/review-assignments/SKILL.md`
- **authority** the user, 2026-10-06, approved coordination loop

<rule>
When an assignment finding needs renewed coordination across stages, use
/coordinate at .agents/skills/coordinate/SKILL.md with the finding, evidence,
existing outcome and resumption point. Mark the issue review already in progress
so entry does not recursively repeat it. Continue in the original issue.
</rule>

## CQ3 — maintain the shared validation and loop

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-06, approved coordination loop

<rule>
When maintaining coordination, recheck the coordinate, analyse, reconcile, issue
and review-assignments declarations and installed rules with mechanisms.py --check
and inject_rules.py --check. Check live links, shared validation/contract
references and recipient access to their published forms. Recheck affected outputs
against their shared criteria; clean structural checks alone do not prove quality.
Use existing records and evidence, not another per-stage maintenance report.
</rule>
