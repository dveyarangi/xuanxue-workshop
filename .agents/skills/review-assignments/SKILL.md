---
name: review-assignments
description: >-
  Use at session entry to review cross-project assignments and incoming requests,
  and when handling project-agent reports, problems or completion evidence.
---

# Review cross-project assignments

## Discover pending work

Read the configured project context and the responsibility and acceptance
contract. Find issued assignments and requests addressed to the coordinating
project using its tracker and recipient labels. Include assignments in every
issue state. Exclude pull requests from the primary assignment search, but inspect
them when linked as reports or evidence. Establish the current unanswered action
under the installed discovery and review rule.

Distinguish an incoming request from a report on an outgoing assignment. Identify
the role speaking from the assignment and conversation; an account name alone
does not identify that role or prove acceptance. Match claimed results to the
assignment's criteria and the referenced artifacts and checks.

## Handle the findings

Apply the installed review and continuation rule. Reuse evidence and an issue
review already in progress. Keep the current reconciliation pass's scope and
resumption point when a finding requires boundary-record changes.

Identify the current action before accepting a result: a blocker, question,
changed prerequisite, contradictory interpretation or completion report. Use the
installed stage routes for missing facts, shared differences and brief changes.
Direct dependencies block their specified activity, not every local action.
Return dependency cycles or incompatible conditions to coordination rather than
inventing eligibility. A new requirement cannot retroactively redefine acceptance.

Reuse established prerequisite evidence while its relevant basis remains valid.
Record scoped conclusions and evidence links in their existing home; do not copy
verification transcripts between issues and documents. Unchanged evidence needs
neither another confirmation nor another response.

Before replying or closing, reread the issue for intervening messages or changed
evidence and reassess the action if needed. Read back responses, closure and the
record revision they reference. If a required tracker read or write fails, report
the limitation and the pending action; do not infer acceptance or an empty inbox.
Continue independently authorized work that does not require the missing evidence.

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

**CQ2** When an assignment finding needs renewed coordination across stages, use
/coordinate at .agents/skills/coordinate/SKILL.md with the finding, evidence,
existing outcome and resumption point. Mark the issue review already in progress
so entry does not recursively repeat it. Continue in the original issue.
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

**L14** Review relevant assignments and discussions in Workshop GitHub Issues, including
unreviewed reports on closed issues. Use their evidence in collection and comparison. Reuse an in-progress
review of the same issue. An unchanged conversation and unchanged relevant evidence
need no repeated response; the original issue holds the review history.

Read each issue's full timeline across all pages, including mentions and
cross-references, alongside its body, comments and closure events. Follow relevant
links to pull requests, commits and other issues; read their reports and inspect
the referenced artifacts and check results. An empty comments list does not
establish absence of a report; a mention alone does not establish completion.
Report inaccessible referenced evidence explicitly.

Act on the findings in the original issue. Investigate problems and request missing
work or evidence there. Bring unresolved shared decisions to /align and return the
agreed outcome to the issue. Accept complete, inspectable evidence against the
assignment's criteria; repeat checks when needed to resolve gaps or contradictions.
A bare completion claim or closed issue is insufficient.

For a verified complete result, reconcile affected Workshop records before
acknowledgement and closure. Observe commit and push approvals when publishing
record changes. The acknowledgement references the resulting record revision or
confirms that no boundary changed. Preserve the distinction between accepted
contracts, implementation evidence and deployed behavior.

Reassess each dependency's necessity and fulfillment from current source,
executed checks, runtime and operator evidence. A document, ticket status or
acknowledgement alone does not establish either. Use the dependency conditions in
skills/collaborate/workshop-issue-format.md; update the original issue to remove
ceremonial or unsupported holds and retain only dependencies tied to a specific
activity and observable condition. Changes to shared promises return to /align.
Workshop readiness and collaboration-installation acceptance do not gate recipient
implementation under its operator against an accessible settled shared contract.

After accepting a prerequisite or reviewing changed relevant evidence, reassess
affected dependent assignments and communicate changed eligibility or required
action in their original issues. An unchanged dependent conversation does not make
changed evidence irrelevant; unchanged conditions require no repeated response.

After handling the findings, report what changed, what remains blocked or undecided,
and where the existing queue stands. Preserve its order. Resume already-authorized
work; use /align when a decision is needed and retain the next-cycle checkpoint.
If nothing new requires action, continue the agreed work.
</installed>
