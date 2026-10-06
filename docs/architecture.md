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

Executable definitions have an owning project, while their externally observable
shape is one shared contract. Project-specific implementation does not create
separate data formats, parameters or guarantees for the same boundary version.

The [scope-of-authority contract](agent-contract.md#boundary-scope-and-product-language)
owns the distinction between shared boundary obligations and project-owned UX,
including separate product-language recommendations.

Workshop's boundary comparison covers Cabinet's existing frontend dependencies,
its provider contract for Daychi, Daychi's consumers and its retained content backend.
Project ownership of design and implementation does not transfer that comparison
to project agents. Source inspection, accepted promises, executed checks and
deployed support are distinct kinds of evidence.

## Contracts and state

The [current system](current-system.md) records observed structure and interface
behavior with source revisions. The [initial target contracts](boundaries.md)
hold accepted boundary decisions. [Migration changes](migration-changes.md)
describe the delta and proposed contributions, with responsibility assigned to
each project. These serve different purposes: an accepted target never proves
that a provider or consumer has implemented it.

Executable schemas remain in their owning projects. The first public schedule
pilot has a published [shared contract and conformance cases](contracts/public-lessons.md);
its Cabinet-owned definitions and deployed evidence are referenced in
[current-system](current-system.md#cabinet). Publication and verification for the
remaining authentication and account/reminder boundaries retain their open questions.

The [accepted scope clarification](agent-contract.md#boundary-scope-and-product-language)
requires one accessible immutable contract reference and common conformance cases
in coordinated implementation assignments. Readiness depends on completing the
shared shape; proposal ownership alone supplies no compatible baseline.

## Work and feedback

The [agent interaction contract](agent-contract.md) is the sole authored home for
assignment routing, reporting, record-update responsibility and acknowledgement.
It records the accepted Issues exchange and the remaining open decisions. Architecture
and project onboarding refer to that contract rather than defining another protocol.

The repository README is the product entry point for an arriving project agent.
It links to addressed work and the [/collaborate skill](../skills/collaborate/SKILL.md)
under the [entry and first-assignment contract](agent-contract.md#entry-and-first-assignment).
The shared tracker holds the concrete installation work.

The [coordination mechanism](../.agents/mechanisms/coordinate/coordinate.md)
owns the shared outcome and its clarity, consistency and completeness criteria.
Scoped analysis supplies evidence, reconciliation gives differences a disposition,
and issuing derives recipient assignments from one contract and ownership model.
Ongoing assignment review returns blockers, questions, changed dependencies and
completion evidence to the relevant stage. Stage boundaries add no approval.

Observed facts remain in the current-system record; accepted promises remain in
their contracts; remaining work stays in its owning ticket or existing issue.
Evidence stays at its source with scoped conclusions and links in these records.
The existing work record carries resumption state; no per-stage report or separate
acknowledgement ledger is required. Complete recipient context and compatibility
checks are necessary coordination work, not removable process overhead.

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
- [Gateway](boundaries.md#accepted-gateway-deferral): deferred by the user, 2026-10-05, until project contributions demonstrate a requirement that the accepted direct connections cannot satisfy. Native sign-in remains provisional.
