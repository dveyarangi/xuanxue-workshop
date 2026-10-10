# Workshop and project-agent contract

Contract for responsibility boundaries between Workshop, Cabinet and Daychi agents.
Accepted by the user on 2026-10-04, with clarifications through 2026-10-08 incorporated.

This document owns role responsibilities and shared guarantees. The
[/collaborate skill](../skills/collaborate/SKILL.md) is the single
authored home for the recipient agent's working instructions. README and installation
issues direct the agent to that skill instead of repeating its procedure. Local
installations preserve the working rules, record their project-recipient label,
remove the installation section from the local copy, and adapt host integration.
The distributable source retains its installation section. Workshop's
responsibilities and acceptance conditions are documented below. This document
is an information source; agent procedures live in their instruction files.
Structure for collaboration issues in Workshop's tracker and reports within them belongs to
[workshop-issue-format.md](../skills/collaborate/workshop-issue-format.md), installed
beside the /collaborate skill and used by the
[/issue skill](../.agents/skills/issue/SKILL.md). Internal project
work and issues follow their own project rules.

## Accepted obligations

Cabinet and Daychi have separate operators and own their implementation and setup.
Workshop owns coordination and the evidence-backed current boundary records.
The [first-stage goal](stage-1.md#completion) owns the overall completion condition;
[boundary contracts](boundaries.md) own the application promises.

All inter-agent assignments, both outgoing and incoming, live in Workshop's GitHub
Issues. Recipient labels, accepted by the user on 2026-10-04, identify addressed
work: `project:daychi` for Daychi, `project:cabinet` for xuanxue-cabinet, and
`project:workshop` for Workshop. A recipient label names who is to perform the
work, not who opened the issue. Project agents address migration-coordination
requests and Workshop-functionality reports to `project:workshop`.
Workshop applies the recipient label when issuing work. The installation issue
supplies the recipient's exact label and requires recording it inside the installed
skill. The project's `AGENTS.md` or `CLAUDE.md`, as read by its agent, holds the
skill link and invocation conditions. The installable block is owned by the skill.
Project repositories are not separate dispatch boards.
Workshop inception work stays in its local ticket queue. Incoming issues about
Workshop functionality or contract migrations are external requests, distinct from that local inception
queue. The local folder spelling and remaining addressing details belong to the
[tracker question](questions/q-0002.0004-where-should-shared-tickets-live-and-how-are-they-addressed-and-claimed.md).

## Boundary scope and product language

Decision: the user, 2026-10-04. Workshop defines shared ownership, data semantics,
consistency, failure obligations and observable acceptance outcomes. Implementing
projects own executable interfaces, internal mechanisms, UX and presentation.
Product-language recommendations are separate work and do not become boundary
requirements.

Boundary agreements constrain behavior that must agree across projects.
Assignments and acceptance evidence are governed by this division of authority.

Clarified by the user, 2026-10-05: project ownership of executable definitions
identifies their authored home; it does not permit independently selected
cross-project contract shapes. Coordinated implementation has one fully specified
externally observable contract, covering operations, parameters, data formats and
meanings, identities, time/window semantics, data guarantees, access, failures,
state/effect semantics and compatibility where applicable. Internal implementations
may differ while fulfilling that same shape.

Implementation assignments share an accessible immutable contract reference and
common conformance examples/outcomes. An incomplete shared shape is unresolved
coordination, even when the assignments are Planned. Separate project proposals
do not establish a compatible implementation assignment. The
[coordinator's contract-shape reference](../.agents/skills/coordinate/CONTRACT-SHAPE.md)
holds the dimensions used to assess completeness. The
[coordination mechanism](../.agents/mechanisms/coordinate/coordinate.md) owns shared
validation across analysis, reconciliation, issuing and ongoing review; each stage
owns its production and checks. Independent implementations satisfying their
recipient briefs must agree on shared shapes and guarantees. Full recipient
context remains mandatory while process steps are kept proportional to the work.

## Workshop address

Selected by the user, 2026-10-04:
[dveyarangi/xuanxue-workshop](https://github.com/dveyarangi/xuanxue-workshop).
This repository publishes the canonical contract and hosts the
[single inter-agent issue tracker](https://github.com/dveyarangi/xuanxue-workshop/issues).
The canonical document path within that repository is `docs/agent-contract.md`.

Repository access, installed source revisions and assignment acceptance are
evidenced in the [current-state record](current-system.md) and
[adoption question](questions/q-0002.0005-how-should-agents-adopt-workshop-rules-and-discover-addressed-work.md).
The [reconciliation report](reconciliation-20261004.md#cabinet-assignment-review--2026-10-06)
owns the dated installation, access and publication history. Source publication
alone does not establish recipient adoption or release an unsatisfied dependency.

## Entry and first assignment

The [onboarding agreement](onboarding.md#access-and-communication) owns participant
access and the original-issue communication requirement when another project joins.

The operator gives the project agent the Workshop repository link. README points
to installation assignments and the /collaborate skill, which owns installation
and communication. Installation issues point to the same skill. This entry route belongs to Workshop,
not to the installation ticket's outcome.

The first assignment's outcome is collaboration installed and verified in the
recipient project under its operator. Installation is a separately reviewable outcome;
its acceptance and Workshop's internal coordination readiness do not gate application
implementation. Recipient operators own authorization of their local work against
an accessible settled shared contract. Posting does not establish adoption.

Dependencies distinguish starting work from integration proof and completion.
Work against an agreed contract and proof requiring a conforming reachable
provider have different prerequisites.
Eligibility follows the actual conditions for each activity and the recipient
operator's authority; Planned/Ready wording adds no separate release approval.
Workshop dependency review assesses both necessity and fulfillment from source,
executed checks, runtime and operator evidence. Documents record shared obligations;
document claims, status and acknowledgements alone do not prove operational readiness.
Dependencies protect specific obligations, such as a reachable conforming provider
and controlled fixtures for actual native proof. Changed conditions are reflected
in the affected original issue; shared promise changes retain coordination.
The [issue format](../skills/collaborate/workshop-issue-format.md#dependencies)
owns dependency fields and interpretation.

### Boundary summary in project instructions

Accepted by the user, 2026-10-04. Workshop supplies a short project-specific
boundary summary and links to the corresponding contracts in the installation
assignment. It distinguishes observed boundaries from unimplemented targets.

The project agent checks that summary against its code, identifies the local
modules involved, and installs it in the project's `AGENTS.md` or `CLAUDE.md`
alongside the rule to invoke the /collaborate skill whenever work touches those boundaries.
Discrepancies are reported in the original assignment. Detecting that work affects
a boundary must not depend on already having loaded the collaboration skill.

Assignments changing a boundary require updating the local summary when affected.
The project agent includes the resulting instruction changes in its evidence;
Workshop checks their agreement with the shared records during acceptance. The
summary identifies boundaries and points to contracts; detailed promises and
versions remain in their authoritative records.

## Project-agent rules to install

Cabinet and Daychi install
the [/collaborate skill](../skills/collaborate/SKILL.md) under their own
operators. That skill owns the procedures for discovery, installation, invocation,
assignment discussion, result reporting and duplicate checks for Workshop problems.
The project agent implements local work; Workshop retains shared-record maintenance
and acceptance responsibility. This section does not carry a second procedure.

## Workshop rules

The existing anchor is retained for published links. This section documents
responsibilities and required outcomes, not agent instructions.

Workshop is accountable for addressed assignments, startup review, resolution of
reported assignment problems, evidence verification, reconciled records and
acceptance acknowledgement. Initial recipient assignments concern verified local
collaboration installation. That installation and Workshop readiness do not gate
application implementation under the recipient operator against an accessible
settled shared contract.

The intended startup-review capability covers assignments and replies, including
completion reports in already-closed issues. GitHub state alone is not acceptance
evidence. This capability remains part of the unverified readiness work.

An accepted outgoing assignment has evidence checked against its scope, affected
records reconciled, and a Workshop acknowledgement referencing the resulting
record revision or confirming that no boundary changed. Missing requirements and
evidence, reported problems, alternatives and their resolution belong to the
original assignment. Incoming Workshop assignments have recorded resolutions
when Workshop's work is complete. Contract changes retain the evolution agreement
below; project operators retain implementation and release ownership.

## Directions and issue ownership

| Direction | Work performed by | Review and closure |
|---|---|---|
| Workshop to Cabinet or Daychi | The addressed project agent under its operator | Workshop verifies the result, reconciles its records and closes the issued assignment. |
| Project agent to Workshop about Workshop functionality | Workshop | Workshop resolves and closes its incoming issue. |
| Project agent to Workshop requesting contract migration | Workshop coordinates; affected project agents implement their parts | Workshop checks provider and consumer evidence, updates records and closes the migration request. |

Creating, executing and accepting an assignment are different responsibilities.
The Workshop review obligation applies to the assignments it issues, not to all
internal issues or PRs in a project repository.

## Exchange through GitHub Issues

The original assignment issue holds its report, problems, alternatives, evidence,
follow-up questions and Workshop acknowledgement. Returning a result or updating
Workshop records does not require a second issue. The separate incoming channel
handles problems with Workshop functionality and requests to coordinate contract
migrations. Problems with Workshop functionality remain subject to the skill's
duplicate check.

An acknowledgement means Workshop has checked the result and reconciled its
records. An accepted target, a project completion report, or a closed GitHub issue
alone does not establish the deployed state of a boundary.

Clarified by the user, 2026-10-05: the original issue's conversation and closure
hold the review history; there is no separate local acknowledgement ledger.
An unchanged conversation whose last message is Workshop's needs no repeated
response. A new project report requires review, including when the project agent
has closed the issue before Workshop acceptance.

Accepted by the user, 2026-10-05: startup review discovers pending issue
conversations; boundary reconciliation uses the relevant discussions and returned
evidence when beginning or resuming its comparison. A boundary-affecting result
feeds Workshop's record reconciliation before acceptance acknowledgement. Responses
and acceptance remain in the original issue. The dedicated Workshop review skill
supplies session-entry discovery; shared review obligations also apply when
reconciliation begins or resumes.

Accepted by the user, 2026-10-05: Workshop can accept complete, inspectable project
evidence against an assignment's criteria without repeating the installation in
the recipient operator's environment. Artifact and check evidence must support
the claimed outcome; a bare completion claim is insufficient. Checks are repeated
when necessary to resolve a gap or contradiction. This does not transfer recipient
installation or release ownership to Workshop.

## Contract evolution

Accepted by the user, 2026-10-04. A project can work autonomously within the active
boundary contract. It can also introduce a new contract version without waiting
for Workshop approval while continuing to fulfil the active contract. A version
identifier alone does not establish compatibility.

The initiating project opens a Workshop issue to coordinate migration to the new
version. Workshop coordinates affected consumers and records the transition.
An incompatible replacement requires coordination before implementation; the old
version is retired only after all known consumers have confirmed their transition.

Provider and consumer checks supply evidence of working behavior. Workshop reviews
that evidence and reconciles shared records before closing the migration. This
responsibility does not imply an implemented executable compatibility validator
or make prior Workshop approval a gate for introducing a coexisting version.

## Adoption and implementation

<straw-dog question="q-0002.0005">
The dedicated /review-assignments skill and its after-recall entry binding are
installed locally. Coordination and direct reconciliation enter the same review;
an active pass reuses completed review while its relevant evidence remains unchanged.
The [review evidence](mechanisms/review-assignments.evidence.md) records passing
structural gates, observed fresh-session invocation and actual Cabinet result
handling. [Coordination evidence](mechanisms/coordinate.evidence.md) supplies bounded
independent instruction grading; published readiness and recipient-host proof remain incomplete.
Cabinet installation issue 1 and Daychi installation issue 2 are accepted/closed;
their evidence does not introduce an additional native implementation gate.
</straw-dog>

The [adoption question](questions/q-0002.0005-how-should-agents-adopt-workshop-rules-and-discover-addressed-work.md)
holds skill implementation, project instruction installation, work discovery and
integration evidence. Reachable repository addresses and permissions must be
established before the agents can use the exchange. No background service or
unattended polling is implied by the startup requirement.
