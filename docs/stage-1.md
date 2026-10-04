# First stage: initial migration and agent integration

Accepted by the user, 2026-10-04. This is the first-stage goal, not a report of completion.

## Goal

Make Workshop capable of coordinating Cabinet and Daychi development through their
own coding agents and separate human operators. Ground that coordination in the
actual applications and an agreed minimal initial migration, preserving existing
functionality as far as possible.

The first action is to clean the documentation and separate current facts, accepted
target contracts, required changes, and responsibility for carrying out the work.

## Required outcomes

- Document how the applications are structured today and the existing boundary
  contracts, including Cabinet frontend to backend and the part shared with Daychi.
  Distinguish source evidence from verified running behavior.
- Document the initial target boundary contracts and the minimum changes needed
  to connect existing capabilities. Identify providers, consumers, data owners,
  affected projects, and responsible contributors.
- Give each fact and decision a clear documentary home. Keep current state,
  accepted target, proposed changes, and longer-term direction distinguishable.
- Prepare and create addressed work using the responsibility and tracker split in
  the [agent interaction contract](agent-contract.md#accepted-obligations).
- Establish the contract's return path for process problems and successful work,
  connecting completion evidence to updates of Workshop's current boundary records.

## Scope limits

Reuse existing functionality. A feature absent from an application is not added
merely because it would be useful during integration. Required contract adaptations
must be justified by the existing consumers and accepted target. The explicitly
accepted removal of per-date skips remains an exception, with its rationale in
the [target contract](boundaries.md#accepted-removal-of-per-date-skips).

Preserve Daychi's existing data-refresh and local reminder flow. Do not introduce
native server push or new background polling. Existing Cabinet browser push is
an existing capability, not a requirement to extend it to Daychi.

Backend consolidation and broader system redesign belong to the
[horizon](horizon.md). The wider goals in [PRODUCT.md](../PRODUCT.md) do not all
become first-stage deliverables. Add only obvious or trivial long-term observations
that help avoid blocking this migration.

## Completion

The stage ends when Workshop has collected confirmation that **both project
agents have successfully integrated with Workshop**, under their own operators.
Creating documents or issues alone does not meet this condition.

The confirmation must demonstrate that the agents can use the agreed instructions
and boundary contracts, find their addressed work, and return problems and results.
Successful work affecting a boundary must lead to Workshop's records describing
the evidenced current state. A closed project issue alone does not establish
that the records are current or that a change is deployed.

Reporting and acknowledgement are defined only in the
[agent interaction contract](agent-contract.md), which records the accepted exchange.
Its open decisions must be resolved and
the resulting process demonstrated before this completion condition is met.

This completion condition concerns integration of agents with Workshop. It does
not silently require completing every application migration assignment.
