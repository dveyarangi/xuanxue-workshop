---
name: reconcile
description: >-
  Use during maintenance to reconcile project boundaries, refresh their
  documentation and instruction summaries, and issue corrective work.
---

# Reconcile project boundaries

Bring observed project boundaries, accepted agreements and coordinating records
into agreement, and derive the work required for their remaining differences.

A reconciliation is a pass that can span turns and sessions. Record its scope,
current stage and resumption point in the pass report. Decision and delivery
cycles follow their own instructions and authorization; incorporate their results
and resume this pass at the affected stage. Recheck affected findings when evidence
changes. Do not repeat completed collection or restart the pass on each turn.

For an explicitly requested preview, leave records unchanged and return proposed
record edits and issue bodies as local review artifacts, identified as proposals.

## Primary issue-output invariant

Apply the installed RC2 rule throughout the pass. Use
[CONTRACT-SHAPE.md](CONTRACT-SHAPE.md) to review the shared boundary definition.
For each applicable dimension, establish its agreed meaning and evidence; record
an explicit reason for each inapplicable dimension. Inspect available definitions
before asking for missing input. Bring unresolved shared choices to resolution.

## 1. Collect information

Read the sources named in Project context. Establish the projects, repositories,
boundaries and delivery scope. Reuse completed analysis and inspect available
source revisions, executable interfaces, checks, project-agent evidence and
installed boundary summaries. Include observed boundaries absent from the records.
Record inaccessible or missing evidence. Distinguish observed implementation,
verified deployment, accepted targets and proposals.

The working agent owns collection and source inspection. Request project evidence
only for a specific gap it cannot establish from available sources, stating why.

## 2. Compare

For each boundary, record:
`boundary | provider/consumers | documented promise | evidence/revision |
delta and consequence | disposition/issue`.

Check ownership and consumers; requests, responses, identifiers, access and errors;
supported versions, migration state and installed instruction summaries. Account
for completed work and decisions from intervening cycles before identifying the
remaining delta. Preserve accepted promises when code disagrees.

Compare provider and consumer interpretations of the shared shape, not just their
individual feature lists. Record mismatched and unresolved dimensions alongside
the current comparison finding.

## 3. Resolve differences

Give each finding a disposition:

- Documentation drift: prepare the factual correction; no project assignment.
- Unresolved shared decision: use /align and incorporate the accepted outcome.
- Project change: identify the correction or agreed migration action, its owner
  and affected consumers. Leave implementation with that owner.
- Missing evidence: retain explicit uncertainty and prepare only the specific
  evidence request collection could not satisfy. Absence of proof is not a defect.
- Unimplemented or deferred target: retain its state and dependencies; do not
  silently select open decisions or start deferred work.

Use the installed ticket rule below to shape remaining work from these dispositions.
Keep the coordinating project's outcome distinct from each recipient's action;
reuse completed analysis in both. One local outcome may produce several coordinated
issues, record changes or a disposition requiring no external issue.

Use the relevant decision or delivery cycle when a finding needs one. Return its
results to the comparison before continuing; those cycles do not replace the pass.
Accepted decisions land in their owning records during alignment.

Complete and agree the shared contract shape for implementation work before
publication preparation. Keep executable definitions in their owning home and
identify one immutable authority usable by every recipient. A missing definition
is an unresolved boundary; asking both projects to choose it during implementation
does not resolve it. Specific evidence or design requests remain distinguishable
from implementation assignments and cannot imply a settled contract.

## 4. Prepare publication

Prepare coherent record changes and short project boundary summaries with contract
links. Compare summaries with the last confirmed installed instructions. Without
an installed baseline, prepare the initial summary and record onboarding as
unverified; absence is not a regression.

Prepare project issues as outputs of the applicable local ticket. Each proposed
assignment must cite a current comparison row and state the remaining recipient
action, owner, dependencies and observable acceptance outcome. Verify that the gap
still exists and the action has not already been completed. Search existing
assignments and continue one covering the same action.

Each implementation issue identifies the same contract reference and common
examples/conformance outcomes, with that recipient's action and evidence against
them. Review the issue set together: probe boundary, empty, invalid, failure,
update and compatibility cases applicable to the contract. Two implementations
that satisfy their respective briefs must not be able to disagree on a shared
shape or guarantee. A counterexample returns the pass to resolution; Planned
status does not bypass this gate.

## Issue and report

This is the publication stage. Apply the authorized record changes and publish
accepted assignments through the project's tracker and issue format. Include the
complete BOUNDARY_SUMMARY when supplying or updating project instructions; keep
tasks and rationale outside it. Project changes remain with their owners.

Observe publication approvals and execution dependencies. Planned publication is
not execution release; issued work is not completed work. Read back published
outputs against the prepared scope and the local ticket's acceptance criteria.
Check that published contract references resolve to the intended immutable
revision, and that recipient bodies neither omit nor redefine its obligations.
Report record changes, issue links, checks, unresolved evidence and deferred work.
Keep recipient execution and integration acceptance visible after a handoff ticket
finishes. If publication is
pending, record the resumption point rather than treating the pass as complete.

## Project context

<installed by="reconcile">
**RC1** State shared boundary guarantees and observable acceptance outcomes. Leave
executable interfaces and internal mechanisms to the owning projects. Inspect
implementation details to verify the guarantees; bring them to alignment when
they reveal an unresolved cross-project obligation or require changing accepted
ownership, behavior, compatibility or scope.

**RC2** Implementation assignments sharing a boundary must prescribe the same fully
specified contract through one accessible immutable reference. Resolve every
applicable contract-shape dimension in .agents/skills/reconcile/CONTRACT-SHAPE.md
before issuing implementation work; leave no recipient choice that can change
interoperability or a shared data guarantee. Project ownership preserves the
authored home of executable definitions and internal implementation freedom,
not independently chosen boundary shapes. An incomplete shared contract blocks
implementation-issue publication, including Planned issues. Evidence or design
requests may gather missing input but cannot stand in for compatible implementation
assignments. Verify the issued result against this invariant.
</installed>

<installed by="local">
**L9** Read these repository-relative sources:
- Project repositories: README.md, Repository map.
- Observed boundaries and source revisions: docs/current-system.md.
- Accepted targets and consumers: docs/boundaries.md.
- Planned changes: docs/migration-changes.md.
- Scope limits: docs/stage-1.md.
- Ownership, routing, autonomy and acceptance: docs/agent-contract.md.
- Issue format and BOUNDARY_SUMMARY: skills/collaborate/workshop-issue-format.md.

**L11** For Workshop boundary alignment, reconciliation and assignments, apply the
scope-of-authority contract in docs/agent-contract.md#boundary-scope-and-product-language.

**L13** Use /ticket and its /impact pass to shape remaining reconciliation work into
local tickets for the coordinating project's outcomes. Obtain breakdown approval
before minting. Slice by outcome, not automatically by finding or recipient.
Published project issues may be ticket outputs; their publication does not
establish that the recipient's work is complete. Verify the ticket's own outcome:
a published handoff and a working integration have different completion criteria.
Continue existing assignments covering the same action. Routine factual corrections
and follow-up within an existing assignment need no additional local ticket.
</installed>
