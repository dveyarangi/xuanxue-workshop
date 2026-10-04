# Workshop architecture

Workshop coordinates boundary agreements and changes across the school's projects.
Its customers are the contributors and coding agents working under separate human
operators. The [first-stage goal](stage-1.md) defines the present delivery scope.

## Responsibility

Workshop owns the cross-project agreement: which module provides a capability,
which modules consume it, who owns the data, and what behavior must agree across
the boundary. Each project owns its internal architecture, executable interfaces,
implementation, and release process. A shared agreement does not transfer that
ownership or authorize Workshop to change a sibling project.

Cabinet's contribution must cover its existing frontend dependencies as well as
the provider contract for Daychi. Daychi's contribution must cover its consumers
and retained content backend. Workshop reconciles the two contributions; source
inspection, accepted promises, executed checks, and deployed support remain
distinct kinds of evidence.

## Contracts and state

The [current system](current-system.md) records observed structure and interface
behavior with source revisions. The [initial target contracts](boundaries.md)
hold accepted boundary decisions. [Migration changes](migration-changes.md)
describe the delta and proposed contributions, with responsibility assigned to
each project. These serve different purposes: an accepted target never proves
that a provider or consumer has implemented it.

Executable schemas remain in their owning projects. Workshop must refer to those
definitions when recording an agreement; the exact publication and verification
arrangement is still open. Cabinet already shares route definitions between its
API and web client, so coordination must account for that existing authority.

## Work and feedback

The [agent interaction contract](agent-contract.md) is the sole authored home for
assignment routing, reporting, record-update responsibility and acknowledgement.
It records the accepted Issues exchange and the remaining open decisions. Architecture
and project onboarding refer to that contract rather than defining another protocol.

The repository README is the product entry point for an arriving project agent.
It links to addressed work and the [/collaborate skill](../skills/collaborate/SKILL.md)
under the [entry and first-assignment contract](agent-contract.md#entry-and-first-assignment).
The shared tracker holds the concrete installation work.

The [/reconcile skill](../.agents/skills/reconcile/SKILL.md), invoked by the
/maintain skill, compares project evidence with these records and derives the
short boundary summaries supplied to project agents. Its project context is
installed from local rules. Reconciliation does not implement project changes
or substitute for the separate startup review and acceptance of assignments.

There is no mandatory bilateral PR approval ceremony: the user rejected it as
too cumbersome on 2026-10-03.

The selected publication and return address, and its verified readiness, are in
the [agent contract](agent-contract.md#workshop-address). Publication and access
from each operator's environment are dependencies of working agent integration.

## Deferred decisions

- [Contract maintenance and verification](questions/q-0002.0002-how-should-workshop-maintain-and-verify-boundary-contracts.md): schema references and evidence required for a shared promise.
- [Tracker access and claims](questions/q-0002.0004-where-should-shared-tickets-live-and-how-are-they-addressed-and-claimed.md): operator access, claims, and handling of the legacy horizon record.
- [Agent adoption](questions/q-0002.0005-how-should-agents-adopt-workshop-rules-and-discover-addressed-work.md): instructions and demonstrable integration under each operator.
- [Operational obligations](questions/q-0002.0006-what-visibility-and-error-monitoring-obligations-should-workshop-enforce.md): distinguish what initial coordination requires from the broader product goals.
