# reconcile — rules installed into skills

| target | anchor |
|---|---|
| `.agents/skills/reconcile/SKILL.md` | `## Project context` |
| `.agents/skills/align/SKILL.md` | `</supporting-info>` |

<straw-dog question="q-0002.0002.0001">
## RC1 — boundary guarantees and project design

- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/align/SKILL.md`
- **authority** the user, 2026-10-04, boundary rule ownership and instruction placement

<rule>
State shared boundary guarantees and observable acceptance outcomes. Leave
executable interfaces and internal mechanisms to the owning projects. Inspect
implementation details to verify the guarantees; bring them to alignment when
they reveal an unresolved cross-project obligation or require changing accepted
ownership, behavior, compatibility or scope.
</rule>
</straw-dog>

## RC2 — one prescribed shared contract in implementation assignments

- **target** `.agents/skills/reconcile/SKILL.md`
- **target** `.agents/skills/align/SKILL.md`
- **authority** the user, 2026-10-05, contract-shape agreement as the primary issue-output invariant

<rule>
Implementation assignments sharing a boundary must prescribe the same fully
specified contract through one accessible immutable reference. Resolve every
applicable contract-shape dimension in .agents/skills/reconcile/CONTRACT-SHAPE.md
before issuing implementation work; leave no recipient choice that can change
interoperability or a shared data guarantee. Project ownership preserves the
authored home of executable definitions and internal implementation freedom,
not independently chosen boundary shapes. An incomplete shared contract blocks
implementation-issue publication, including Planned issues. Evidence or design
requests may gather missing input but cannot stand in for compatible implementation
assignments. Verify the issued result against this invariant.
</rule>
