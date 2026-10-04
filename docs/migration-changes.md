# Initial migration changes and contribution proposals

Derived from the [accepted target](boundaries.md) and [current source evidence](current-system.md).
The [first-stage goal](stage-1.md) limits this work. This document describes the
required delta and proposed assignments; it does not authorize sibling implementation.

## Changes derived from accepted contracts

This list records required changes separately from the target architecture, which
owns the accepted agreements and rationale. It feeds future project tickets;
implementation details and the contribution breakdown still require their own
alignment. It is not a claim that these changes are implemented or deployed.

| Accepted contract | Cabinet contribution | Daychi contribution | Decisions still needed |
|---|---|---|---|
| [Schedule access](boundaries.md#accepted-schedule-access) | Provide public schedule responses without Zoom details and authenticated responses with them. | Consume Cabinet's schedule with the agreed access behavior. | Date window, identifier mapping and disposition of the existing HTML fallback. |
| [Cabinet credentials](boundaries.md#accepted-content-admission) | Support Cabinet-issued bearer credentials for native clients while retaining web cookies and authoritative validation. | Obtain and present Cabinet credentials to the target APIs. | Authentication standard, acquisition, lifecycle and transition of existing users/credentials. |
| [Content admission](boundaries.md#accepted-content-admission) | Provide a narrow authoritative admission check. | Replace independent content admission with the accepted call to Cabinet and distinguish refusal from temporary failure. | Executable check schema, caller trust, verification and any cache bound; removal follows the target contract's consolidation binding. |
| [Reminder selections](boundaries.md#accepted-reminder-selections) | Support one-off dates and regular subscriptions in one account selection exposed to both clients. | Read and change the Cabinet-owned selection and migrate current local choices. | Lead times and migration rules. |
| [Daychi reminder delivery](boundaries.md#accepted-daychi-reminder-delivery) | Expose authoritative schedule and account selections for client refresh. | Adapt the existing refresh flow to Cabinet and reconcile local OS reminders. | Stale-data behavior and verification; no new background refresh capability. |
| [Removal of per-date skips](boundaries.md#accepted-removal-of-per-date-skips) | Keep per-date skip exceptions out of the target shared reminder contract. | Remove the option and its related behavior; include the accepted user rationale in the ticket text and propose treatment of saved exceptions. | Disposition of already saved exceptions. |

Native server push was rejected by the user as excessive for this scope on
2026-10-04. It is not a required project change.

## Unresolved compatibility details

Compare the [current source inventory](current-system.md) with the target before
selecting changes. The remaining decisions are:

- Required schedule window and response fields; identifier mapping between Daychi
  series/occurrences and Cabinet classes/lessons; treatment of the native HTML fallback.
- Credential acquisition and lifecycle, association of existing users/access grants,
  and the admission-check request, response and failure contract.
- Mapping of local selections to account selections without losing existing use
  without sign-in; lead-time differences and disposition of saved skipped dates.
- Stale-data and multi-client notification behavior while preserving existing
  refresh and delivery facilities. Do not add a background-refresh project.

## Information needed from project agents

Before drafting implementation tickets, request evidence for each relevant
boundary. This is a proposed investigation brief, not a ticket breakdown.

Each contribution should identify:

- The capability and concrete provider/consumer modules, with source references
  and the inspected revision.
- Existing requests, responses, identifiers, time semantics, access rules,
  errors, and relevant compatibility checks.
- Required consumer behavior that the existing provider contract cannot satisfy.
- Proposed contract additions or adaptations, with alternatives and decisions
  requiring agreement explicitly marked.
- Constraints from existing credentials, saved preferences, supported clients,
  compatibility, and deployment that could change the target contract. Detailed
  migration design follows contract agreement.
- Existing checks and proposed checks for each target promise, distinguishing
  source inspection, executed checks, and deployment evidence.

Cabinet's contribution covers its backend promises and existing frontend
dependencies. Daychi's contribution covers its frontend requirements, retained
content backend, and existing user preferences and credentials. These contributions
must converge on one agreement for each shared boundary.

## Review scenarios

Use these scenarios to expose missing decisions before implementation planning:

- An unauthenticated caller can receive the schedule without Zoom connection
  details; the schedule with those details requires authentication.
- A user signs in from Cabinet web and from a Daychi native client, then accesses
  Daychi content under the agreed permission policy.
- Access is revoked or credentials expire; each consumer applies the agreed
  outcome and recovery behavior.
- An existing recurring selection with a skipped date migrates with the agreed
  identifiers and reminder timing.
- A user has both clients installed; notification delivery follows the agreed
  policy, including offline behavior and duplicate prevention.
- Cabinet's existing frontend keeps working throughout the agreed API transition;
  a failed rollout has a defined recovery path.

These are contract-review scenarios, not assertions that the implementation
already passes them.

## Proposed contribution breakdown

These are later contract-contribution proposals. The first outgoing assignments
are instruction-installation requests under the
[Workshop rules](agent-contract.md#workshop-rules); this proposal does not issue them.

This earlier three-part proposal covers contract contributions only. It is not
an approved breakdown of the whole first stage: agent adoption and the return
path for results must also be covered before a stage-wide breakdown is accepted.
No ticket IDs or issue addresses have been allocated to these proposals.

Assignment routing and the return path follow the
[agent interaction contract](agent-contract.md). Each issued assignment must identify the
responsible project, accountable contributor, dependencies, expected evidence,
and where to return it. Issuing work does not establish adoption or authorize
Workshop to perform the project changes.

### cabinet-contract-contribution — Proposed

Intended contributor: Cabinet project agent under its operator. Destination: GitHub
Issue. Interaction: AFK. Independent of the Daychi contribution, after Workshop
instructions and a return address are available.

Outcome: Workshop can identify Cabinet's existing API promises, frontend
dependencies, and proposed support for Daychi from a source-grounded contribution.

Cover Cabinet backend to Cabinet frontend across the API surface consumed by the
frontend, marking the subset shared with Daychi. Cover Cabinet's provider side of
schedule, identity, access, and reminders for Daychi clients and retained content.
Reference the typed route map and its provider, consumer, and route-registration
checks. Describe existing promises separately from proposed extensions; identify
decisions for human review rather than accepting them within this contribution.

Completion evidence:

- Each relevant caller-to-provider path names modules, data ownership, source
  revision, contract definitions, and existing verification instruments.
- Cabinet web dependencies and shared versus Cabinet-specific promises are explicit.
- Proposed Daychi support states constraints, gaps, alternatives where needed,
  and checks; source evidence is distinguishable from runtime evidence.
- The contribution passes the /verify skill against this scope without application changes.

Parent scope: Cabinet web seam; Cabinet's provider side of both Daychi seams.

### daychi-contract-contribution — Proposed

Intended contributor: Daychi project agent under its operator. Destination: GitHub
Issue. Interaction: AFK. Independent of the Cabinet contribution, after Workshop
instructions and a return address are available.

Outcome: Workshop can identify Daychi's consumer requirements and retained content
promises from a source-grounded contribution.

Cover client to schedule provider, client authentication and content access, and
preferences through notification delivery. Cover Daychi backend to its clients
for retained content and Daychi's side of Cabinet identity recognition. Describe
the public calendar and native HTML fallback, identifier and saved-choice
semantics, local notification behavior, and credential/access requirements.
Propose required promises without selecting unresolved cross-project policy.

Apply the accepted [one-off and recurring reminders](boundaries.md#accepted-reminder-selections).
Identify the provider additions and client adaptations needed to support both
without requiring a person to unsubscribe after a one-off lesson date.

When this proposed assignment becomes a ticket for the Daychi agent, include
the user's [reason for removing per-date skips](boundaries.md#accepted-removal-of-per-date-skips)
in the ticket text, not only a removal instruction or a link. Explain why the
feature lacks a useful user trigger and why dismissing a single notification
makes the additional action unnecessary. Account for UI, reminder and personal
selection behavior, and propose a disposition for existing saved exceptions.

Completion evidence:

- Every relevant consumer requirement has a concrete user scenario and source
  references with the inspected revision.
- Retained content requests and their authentication/access dependencies are explicit.
- The ticket includes the accepted rationale for removing per-date skips;
  the contribution respects removal and proposes handling of saved exceptions.
- Required schedule windows, identity semantics, preference semantics, delivery,
  and failure behavior distinguish existing behavior from target proposals.
- Each proposed promise identifies existing or required checks; the contribution
  passes the /verify skill against this scope without application changes.

Parent scope: Daychi consumer side of Cabinet API; content API and trust boundary.

### agreed-target-seam-contracts — Proposed

Intended contributor: Workshop agent, with the user deciding unresolved contracts.
Destination: local Workshop inception queue. Interaction: HITL. Dependencies:
both contributions above.

Outcome: Each target seam has one agreed description connecting provider promises,
consumer requirements, ownership, and verification obligations.

Reconcile the contributions against the review scenarios. Keep common Cabinet API
promises in one account and consumer-specific requirements explicit. Resolve
contradictions with the user and land accepted decisions in architecture or the
owning contract description. Reference executable definitions in their projects;
do not duplicate their schema authority. Record implementation and transition
consequences separately from accepted promises.

Completion evidence:

- All four target connections have provider and consumer agreement recorded with
  decision provenance, data ownership, and accountable project responsibilities.
- Shared Cabinet API promises and consumer-specific requirements are unambiguous.
- Review scenarios have agreed outcomes and verification obligations; existing
  verification, proposed checks, and deployment evidence are distinguishable.
- Load-bearing decisions for these seams are resolved or explicitly deferred by
  the user with a condition and an interim contract.
- The accepted description passes the /verify skill; implementation consequences are
  traceable without claiming that the target is deployed.

Parent scope: one coherent target architecture spanning all four connections.

## Impact assessment of the proposed split

### Impact

The split changes the boundary description and prepares addressed documentation
work for two project agents and Workshop. It covers both sides of Cabinet's API,
Daychi content, and the identity/access relationship. The first two contributions
can be independently verified; their proposals need reconciliation before they
become shared promises. No sibling implementation is changed by this pass.

### Hidden edges

Cabinet's existing route map, web caller, and registered-route e2e guard already
share executable definitions. A second schema would introduce disagreement.
The student schedule query differs from Cabinet's general lesson query: a date
window supported by one route cannot be inferred for the other. Daychi's native
HTML fallback and local notifications constrain authority and delivery decisions.
The user accepted common content and a live Daychi-to-Cabinet admission check
with a consolidation straw dog after this draft split was prepared. Contributions
must respect that decision and resolve the remaining credential/check contract.
Claims about deployed support require runtime evidence.
The Workshop tracker is selected in the agent contract. Recipient access and
cross-clone claims remain open; local ticket creation cannot establish dispatch
or adoption by itself.

### Leave alone

Accepted provider assignments, sibling application code, releases, deployments,
and existing Cabinet-only workflows. Tracker, onboarding, and operational machinery
remain with their existing questions. The detailed migration plan follows the
accepted target contracts.

### Recommendation

For the contract-description portion, retain the proposed two independent project
contributions and one dependent HITL reconciliation. This does not cover the entire
[first-stage completion condition](stage-1.md#completion). Splitting by API feature would scatter the same frontend and
identity dependencies across several assignments. Combining both projects into
one contribution would obscure responsibility. At this architecture resolution,
each contribution spans complete consumer/provider paths and can be checked
without implementing the target behavior.
