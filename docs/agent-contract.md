# Workshop and project-agent contract

Contract for responsibility boundaries between Workshop, Cabinet and Daychi agents.
Accepted by the user, 2026-10-04, including the role separation, startup review,
reporting channels and installation-first order below.

This document owns role responsibilities and shared guarantees. The
[/collaborate skill](../skills/collaborate/SKILL.md) is the single
authored home for the recipient agent's working instructions. README and installation
issues direct the agent to that skill instead of repeating its procedure. Local
installations preserve the working rules, record their project-recipient label,
remove the installation section from the local copy, and adapt host integration.
The distributable source retains its installation section. Workshop's
own review duties are separate below.
Structure for collaboration issues in Workshop's tracker and reports within them belongs to
[workshop-issue-format.md](../skills/collaborate/workshop-issue-format.md), installed
beside the /collaborate skill and referenced by the
[/reconcile skill](../.agents/skills/reconcile/SKILL.md). Internal project
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

## Workshop address

Selected by the user, 2026-10-04:
[dveyarangi/xuanxue-workshop](https://github.com/dveyarangi/xuanxue-workshop).
This repository publishes the canonical contract and hosts the
[single inter-agent issue tracker](https://github.com/dveyarangi/xuanxue-workshop/issues).
The canonical document path within that repository is `docs/agent-contract.md`.

Readiness checked on 2026-10-04: the repository is private, Issues are enabled,
and the current CLI account has admin access. The remote is empty, so the local
contract has not been published there. Access for the Cabinet and Daychi operators
and their agents must be demonstrated during onboarding; current local credentials
do not establish their access.

## Entry and first assignment

The operator gives the project agent the Workshop repository link. README points
to installation assignments and the /collaborate skill, which owns installation
and communication. Installation issues point to the same skill. This entry route belongs to Workshop,
not to the installation ticket's outcome.

The first assignment requests installation of a local collaboration skill, its
invocation conditions, and the durable instruction that makes the project agent
use it. It references the /collaborate skill below. The agent implements the
local integration under its own operator and reports the installation evidence
in that same issue. The installation outcome is a collaboration skill installed
and verified in the recipient project. Subsequent application work follows
confirmed onboarding.

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

These rules are for the Workshop agent, not instructions to install in projects.

1. Issue addressed work to project agents in Workshop Issues. The first issues
   request the local collaboration-skill installation defined above and evidence
   that its invocation conditions and instruction entry point work.
   Application migration assignments follow that onboarding; they are not the
   first outgoing issues. The earlier [contract-contribution proposal](migration-changes.md#proposed-contribution-breakdown)
   is not a substitute for the installation assignments.
2. At session startup, run a dedicated skill to review outgoing assignments and
   their replies. It must inspect completion reports even when a project agent has
   already closed the issue; GitHub closed state alone is not acceptance evidence.
3. When an agent reports an assignment problem, investigate the evidence and
   propose an alternative solution in that same issue. Apply the contract-evolution
   agreement below when a shared boundary must change.
4. When work appears complete or an agent reports completion/closure, verify it
   against the assignment and its evidence. Raise missing evidence or unmet
   requirements in the original issue; do not accept completion on assertion alone.
5. For verified work, update the affected Workshop records, acknowledge acceptance
   with links to the resulting document revision, and close the outgoing assignment.
   If it is already closed, still verify, update records and acknowledge. If no
   boundary changed, say so in the acknowledgement rather than fabricating an update.
6. Process issues addressed to Workshop, record their resolution, and close them
   when the Workshop work is complete.

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

<straw-dog until="The dedicated Workshop review skill is implemented, invoked at session startup and verified against this contract" ticket="docs/tickets/01-0005-workshop-coordination-ready.md">
The dedicated startup skill is an accepted requirement; it has not been implemented
or wired into startup by this contract edit. Its implementation must preserve this
single source for the role rules. It must run as part of Workshop startup alongside
its existing session-entry obligations.
</straw-dog>

The [adoption question](questions/q-0002.0005-how-should-agents-adopt-workshop-rules-and-discover-addressed-work.md)
holds skill implementation, project instruction installation, work discovery and
integration evidence. Reachable repository addresses and permissions must be
established before the agents can use the exchange. No background service or
unattended polling is implied by the startup requirement.
