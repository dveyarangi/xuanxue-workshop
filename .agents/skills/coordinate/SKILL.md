---
name: coordinate
description: >-
  Use to carry a cross-project change, shared standard, changed project evidence
  or assignment finding through coordinated work and acceptance.
  Use to propose further cross-project work from recorded remaining changes and dependencies.
---

# Coordinate cross-project work

Own the shared outcome under the configured responsibility and autonomy contract.
Identify the scope, affected projects, governing agreements, current evidence and
existing assignments. Distinguish a proposed change, accepted promise, observed
implementation, checked deployment and accepted result.

## Continue and resume

At entry or resumption, recover the pending action and its condition from the
existing owning work record and original assignments. Apply the installed entry
review rule RA2. With unchanged circumstances, retain the selected step or wait.
If no next action is recorded, or the user requests reconsideration or relevant
evidence changes, select the next action below. A stage result returns to this
same pass at the affected action.

Keep the agreed outcome visible across recipient handoffs. Assess completion
against its own acceptance criteria. A status label grants no execution authority.

For an explicit preview, return proposed edits and drafts without changing project
records or the tracker. A preview can be graded without releasing recipient work.

## Select the next action

Consider further work on the occasions above and when the current outcome
completes or waits on an external event.

Read the active ticket's Outcome, Acceptance criteria and dependencies, its place
in the queue and the current stage's scope through the source bindings in Project
context. For work outside that ticket, start from the bound accepted-contract
delta. Check the candidate against its cited agreement, source/runtime evidence
and existing assignments. Historical breakdowns do not establish the current queue.

### Actions and resumption

Use this navigation table to select a step from the recorded remainder. Linked
skills define execution; their installed rules below supply the routing contract.

| Established from the sources | Next action and route | Resume when / continue with |
|---|---|---|
| Relevant evidence is missing or changed | [/analyse](../analyse/SKILL.md): establish the scoped fact and its limits (AN1). | Observation available: compare it with the governing agreement. |
| Observed behavior differs from the agreement | [/reconcile](../reconcile/SKILL.md): determine the discrepancy and remaining owner action (RC3). | Disposition recorded: continue its resulting action. |
| The shared agreement leaves an unresolved choice | [/align](../align/SKILL.md): present the choice, constraints and recommendation (RC3). | Decision recorded in its authoritative home: reassess affected work. |
| A required outcome has no covering work | [/ticket](../ticket/SKILL.md), through [/impact](../impact/SKILL.md): prepare the breakdown (project decomposition rule). | Required breakdown approval obtained: create the approved work. |
| An agreed recipient action needs an assignment | [/issue](../issue/SKILL.md): prepare or update the assignment (IS1). | Publication conditions satisfied: publish within authority, then follow the original assignment. |
| An existing assignment covers the action | [/review-assignments](../review-assignments/SKILL.md): handle its blockers, questions and results in the original issue (RA2). | Findings handled: continue authorized work; later findings return to the affected action. |
| A required external result is unavailable | Identify the exact evidence or event, its provider and the action it blocks in the existing work record. | That evidence or event arrives: verify the condition and resume the blocked action. |

A next-step proposal names the originating acceptance criterion or delta item,
the evidenced remainder, its existing assignment or absence, the selected action
and its direct dependencies. Assess preparation, publication, implementation and
integration proof against their own dependency conditions; continue available
authorized actions while another action waits. Apply the entry
autonomy settings and the original assignment's execution conditions. Present
the prepared choice when a user decision is required.

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

**L18** Replace the reporting requirement in /coordinate's Outputs section with:
At a handoff or pause, explicitly state the current stage, the next concrete
action, who performs it, and any condition required to proceed. Link to the
existing owning work record.
</installed>
