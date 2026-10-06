---
name: coordinate
description: >-
  Use to carry a cross-project change, shared standard, changed project evidence
  or assignment finding through coordinated work and acceptance.
---

# Coordinate cross-project work

Own the shared outcome under the configured responsibility and autonomy contract.
Identify the scope, affected projects, governing agreements, current evidence and
existing assignments. Distinguish a proposed change, accepted promise, observed
implementation, checked deployment and accepted result.

## Continue the loop

Enter the stage selected by the installed routing rules. Reuse an active pass and
completed analysis; refresh only evidence affected by a relevant change. A finding
returned by a stage continues the same pass, not another invocation of its entry
review. Resolve conflicting obligations with the decision owner.

Keep the agreed outcome visible across recipient handoffs. Published instructions
do not establish implementation or integration. Finish against the outcome's own
acceptance criteria; otherwise identify the remaining owner action or decision.
Do not introduce a stage approval or infer authorization from a status label.

For an explicit preview, return proposed edits and drafts without changing project
records or the tracker. A preview can be graded without releasing recipient work.

## Outputs

Update the existing home of each changed fact: observed state, accepted agreement,
remaining work or addressed assignment. Evidence stays at its source; records
carry the scoped conclusion, revision and link. Do not copy issue conversations
or verification transcripts into several records.

Use the existing owning work record, within its format, for scope, evidence
baseline, pending action and resumption. Inline work needs no separate pass report.
A ticket holds a verifiable outcome; an issue holds its recipient's current work.
No per-stage report, acknowledgement ledger, dependency-status register or
per-recipient local ticket is required. Report the outcome and remaining work
with links to their homes.

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

<installed by="reconcile">
**RC3** For a suspected difference between project behavior, requirements or participant
interpretations, use /reconcile at .agents/skills/reconcile/SKILL.md. Supply scoped
evidence and the governing agreement; incorporate its disposition into the same
pass. An unresolved shared decision goes to /align, not into implementation
instructions as a choice for each recipient.
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
- Planned changes: docs/migration-changes.md.
- Scope limits: docs/stage-1.md.
- Ownership, routing, autonomy and acceptance: docs/agent-contract.md.
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
