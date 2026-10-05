---
name: reconcile
description: >-
  Use during maintenance to reconcile project boundaries, refresh their
  documentation and instruction summaries, and issue corrective work.
---

## Compare and reconcile

Read the sources named in Project context below. Take participating projects and
repository addresses from that map, and boundaries from the current and target
records. Inspect source revisions, executable interfaces, checks and project-agent
evidence. Include observed boundaries missing from the records. Respect the stage
scope and distinguish implementation, verified deployment and intended behavior.

For each boundary, record in the maintenance report:
`boundary | provider/consumers | documented promise | evidence/revision |
delta and consequence | disposition/issue`.

Check ownership and consumers; requests, responses, identifiers, access and error
behavior; supported versions and migration state; and the accuracy of the boundary
summary in the project's agent instructions. Record inaccessible or missing evidence.

Update factual records with evidence; preserve accepted promises when code disagrees.
Derive each project's short summary with contract links and compare it with the last
confirmed installed instructions. Without an installed baseline, prepare the initial
summary and record onboarding as unverified; absence is not a regression.

Classify each difference:

- Documentation or wording only: repair the records; no project issue.
- Project action required: an accepted active promise is violated, a consumer is
  affected, or installed instructions omit or misidentify a boundary or trigger.
  Issue the correction or agreed migration work to the responsible project.
- Missing evidence: mark unverified. Request specific project evidence when needed
  to resolve the comparison; do not infer a defect from missing evidence.
- Unimplemented target: retain planned status. Follow the agent contract's autonomy
  rules; do not start deferred work or silently resolve open shared decisions.

## Issue and report

Use the issue format named in Project context for routing, duplicate checks and
issue contents. Supply the recipient's summary in its defined `BOUNDARY_SUMMARY`
block. Follow the reporting and acceptance contract. Project changes remain with
their owners; issuing work does not establish its completion.

For an explicitly requested preview, leave records unchanged and return proposed
record edits and issue bodies as local review artifacts. Identify them as proposals.

## Project context

<installed by="local">
**L9** Read these repository-relative sources:
- Project repositories: README.md, Repository map.
- Observed boundaries and source revisions: docs/current-system.md.
- Accepted targets and consumers: docs/boundaries.md.
- Planned changes: docs/migration-changes.md.
- Scope limits: docs/stage-1.md.
- Ownership, routing, autonomy and acceptance: docs/agent-contract.md.
- Issue format and BOUNDARY_SUMMARY: skills/collaborate/workshop-issue-format.md.

**L13** Use /ticket and its /impact pass to shape remaining reconciliation work into
local tickets for the coordinating project's outcomes. Obtain breakdown approval
before minting. Slice by outcome, not automatically by finding or recipient.
Published project issues may be ticket outputs; their publication does not
establish that the recipient's work is complete. Verify the ticket's own outcome:
a published handoff and a working integration have different completion criteria.
Continue existing assignments covering the same action. Routine factual corrections
and follow-up within an existing assignment need no additional local ticket.
</installed>
