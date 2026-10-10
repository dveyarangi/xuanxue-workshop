---
name: analyse
description: >-
  Use to inspect a project's architecture, boundaries or shared-standard adoption,
  refresh scoped observations, and establish changed or missing project evidence.
---

# Analyse a project's relevant behavior

Establish the repository, inspected revision, scope and earlier evidence baseline.
Read the configured sources and reuse still-applicable evidence. Inspect source,
executable interfaces, checks, project reports and installed boundary summaries;
include relevant boundaries missing from current records.

Cover responsibilities, providers and consumers, data ownership, operations,
requests and responses, identity, time, access, errors, state and data guarantees,
supported versions, migration state and applicable operational standards. Follow
internal details when needed to establish externally observable behavior.
Inspect deployed configuration and runtime separately from repository state.

The working agent owns source investigation. Ask another project only for a
specific proof unavailable from accessible sources, stating the access or execution
gap. Missing evidence is an unknown, not proof of a defect or of compliance.

## Return the observation

Use the existing factual record or return a scoped result to the caller. Include
repository and revision, inspection date, scope, baseline, relevant facts and their
source links, checks/deployment evidence, changed facts and explicit unknowns.
Apply the subjects above to the scope; explain material exclusions. Bind each claim
to its actual evidence: a recent revision in the heading does not refresh older facts.

Do not prescribe a new serialization or rewrite unrelated inventory. Replace
superseded live facts in their owning home and retain necessary provenance.
Flag the possible effect on shared obligations; do not amend accepted promises
to match code. A changed path alone does not establish a changed guarantee.

A delegated investigation has one repository and declared scope, read access,
the governing references and this output requirement. It returns evidence to
the coordinating agent; it does not publish assignments or make shared decisions.

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
</installed>
