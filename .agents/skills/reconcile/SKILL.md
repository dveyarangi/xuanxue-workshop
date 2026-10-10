---
name: reconcile
description: >-
  Use to compare project evidence with shared agreements, resolve boundary or
  standard-adoption differences, and determine remaining coordinated work.
---

# Reconcile shared obligations

Compare scoped observations, accepted agreements, installed summaries and current
assignment evidence. Account for completed work and decisions before identifying
the remaining difference. Preserve accepted promises when code disagrees.

For each relevant boundary or standard, retain in its existing work record:
`boundary | provider/consumers or affected projects | promise | evidence/revision |
delta and consequence | disposition/assignment`.
Compare shared meanings, not only local feature lists. Record mismatched or
unresolved dimensions with the finding.

## Resolve the difference

Give each finding a disposition:
- No remaining difference: retain sufficient evidence; no assignment.
- Factual record drift: correct its owning record; no project change.
- Implementation deviation: specify the owner correction under the same contract.
- Unresolved shared choice: use /align; incorporate the accepted decision.
- Accepted amendment or migration: state old/new obligations, affected consumers,
  compatibility and transition/retirement conditions.
- Missing evidence: retain uncertainty and obtain only proof unavailable through
  source investigation; absence of proof is not a defect.
- Unimplemented or deferred target: retain state and dependencies without
  silently starting deferred work.

Complete and agree the shared shape before implementation publication. A missing
definition is not permission for each recipient to choose it. Amendments use
accepted revisions and do not redefine earlier acceptance retroactively.
Accepted decisions update their owning records.

Return dispositions, record changes and remaining owner actions to the existing
pass. Keep the coordinating outcome distinct from recipient actions: one outcome
can produce several issues or no external issue. Use the installed routing rules
for missing observations and addressed work; unresolved choices return to /align.

## Project context

<installed by="coordinate">
**RC1** For cross-project work, state shared boundary guarantees and observable acceptance
outcomes. Projects own executable definitions and internal mechanisms; the shared
contract fixes their externally observable shape. Inspect implementation details to verify guarantees; bring them to
alignment when they reveal an unresolved shared obligation or require changing
accepted ownership, behavior, compatibility or scope.

**RC2** Cross-project implementation assignments prescribe one fully specified contract
through an accessible immutable authority and common conformance cases. Apply
.agents/skills/coordinate/CONTRACT-SHAPE.md to every applicable dimension, with a
reason for inapplicability. Leave no recipient choice that can change shared
formats, parameters, meanings, guarantees or interoperability. Internal designs
may differ. Each recipient's brief and cited authority must suffice without
Workshop session context; compatible implementations must follow from the briefs.
An incomplete shared shape blocks implementation publication, including Planned
issues. Design/evidence requests cannot substitute for this gate.

**CQ1** For cross-project work, apply .agents/skills/coordinate/VALIDATION.md during
inception and validation. Establish clarity for the next reader, consistency
with governing agreements and related work, and completeness of scoped obligations.
Derive recipient tasks from the same contract and ownership; assess individual
understanding and set-wide coverage. Revalidate affected meanings after edits.
Reduce process steps, never context required for compatible implementations.
Reuse valid evidence; stage changes add no approval.
</installed>

<installed by="analyse">
**AN1** When relevant source or runtime evidence is missing or changed, use /analyse at
.agents/skills/analyse/SKILL.md for the affected repository and scope. Reuse facts
whose basis remains valid. Return the observation to the existing work; do not
ask recipients to investigate what accessible sources can establish.
</installed>

<installed by="issue">
**IS1** For an approved remaining owner action or an assignment needing a body change,
use /issue at .agents/skills/issue/SKILL.md. Supply the governing agreement, current
evidence, scope and direct dependencies. Reuse the issue covering the action.
A routine factual correction or follow-up needs no additional local ticket.
Ordinary review responses stay with assignment review.
</installed>

<installed by="review-assignments">
**RA2** At coordination or reconciliation entry or resumption, use /review-assignments at
.agents/skills/review-assignments/SKILL.md for relevant assignments and incoming
requests unless already reviewed for this pass with no changed relevant evidence.
Reuse an active review supplied by the caller; do not recurse into it. Blockers,
questions and changed dependencies matter before completion reports arrive.
</installed>

<installed by="local">
**L9** Use the sources relevant to the current scope:
- Project repositories: README.md, Repository map.
- Observed boundaries and source revisions: docs/current-system.md.
- Accepted targets and consumers: docs/boundaries.md.
- Remaining changes: docs/migration-changes.md, Changes derived from accepted contracts;
  follow each row's cited agreement in docs/boundaries.md.
- Current work and order: docs/tickets/README.md, Queue; the active ticket's
  Outcome, Acceptance criteria and dependencies.
- Scope limits: docs/stage-1.md.
- Ownership, tracker discovery and acceptance: docs/agent-contract.md,
  Accepted obligations and Entry and first assignment; use the original issues
  returned by assignment review. Autonomy switches: AGENTS.md, Project-local.
- Issue format and BOUNDARY_SUMMARY: skills/collaborate/workshop-issue-format.md.

**L11** For Workshop boundary alignment, reconciliation and assignments, apply the
scope-of-authority contract in docs/agent-contract.md#boundary-scope-and-product-language.

**L13** Use /ticket and its /impact pass to shape remaining cross-project work into
local tickets for the coordinating project's outcomes. Obtain breakdown approval
before minting. Slice by outcome, not automatically by finding or recipient.
Published project issues may be ticket outputs; their publication does not
establish that the recipient's work is complete. Verify the ticket's own outcome:
a published handoff and a working integration have different completion criteria.
Continue existing assignments covering the same action. Routine factual corrections
and follow-up within an existing assignment need no additional local ticket.
</installed>
