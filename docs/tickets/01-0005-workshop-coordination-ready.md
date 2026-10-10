# Workshop coordination ready

- **Status:** In progress
- **Type:** HITL
- **Plan:** [Workshop coordination ready RFC](../rfc/01-0005-workshop-coordination-ready.md) — one review skill after recall, sharing the installed feedback rule with reconciliation
- **Responsible contributor:** Workshop agent under its operator
- **Answers:** [q-0002.0005.0002](../questions/q-0002.0005.0002-does-ordinary-workshop-session-entry-invoke-and-exercise-assignment-review.md)
- **Outcome:** Workshop provides a published agent entry point and reviews issued assignments at startup through verified completion and acknowledgement.

## Parent

The agent-integration portion of the [first-stage goal](../stage-1.md), governed by
the [agent contract](../agent-contract.md). The user approved this three-part
first-launch breakdown on 2026-10-04. This is Workshop's own inception work; the
Cabinet and Daychi installations are separate issues in the Workshop GitHub tracker.

Related recipient installation outcomes are
[cabinet-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
and [daychi-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/2).
Both installations are accepted: [Cabinet](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155)
and [Daychi](https://github.com/dveyarangi/xuanxue-workshop/issues/2#issuecomment-6052903501).
This coordinator outcome remains incomplete and does not gate their work.
They are not local ticket copies. The user removed the readiness and
installation-acceptance dependencies on 2026-10-08.

The [recorded impact](../questions/q-0002.0005-how-should-agents-adopt-workshop-rules-and-discover-addressed-work.md#impact)
traces the startup, publication, issue-review and independent-operator dependencies.

## What to build

Deliver the dedicated Workshop startup-review skill and its durable invocation
wiring, retaining the existing recall obligation. The skill applies the Workshop
section of the canonical agent contract rather than carrying another authored copy.

Make the published repository entry sufficient for an arriving project agent to
find its installation issue and load the /collaborate skill it references.
README and installation issues link to the same skill; local project
installation remains the recipients' work. Establish how Workshop discovers
issued work using the recipient labels defined by the agent contract. Installation
issues supply the exact recipient label for the installed skill and the boundary
summary required by the agent contract for durable project instructions. Review
issued assignments and pending replies in its single GitHub tracker, including
results on already-closed issues. Keep those assignments distinguishable from
issues about Workshop functionality without requiring another success-report issue.

Complete the review path: investigate reported obstacles, propose alternatives
in the original issue, verify completion evidence, update affected Workshop
records, acknowledge the result and close completed assignments. Verification
must reject unsupported completion claims and must not infer deployment from
GitHub issue state. Repeated startup review must not repeat completed responses.

The [exchange contract](../agent-contract.md#exchange-through-github-issues) also
owns review history, the startup/reconciliation connection and the accepted
evidence standard. The outcome fulfils that contract through the installed review
instruction and its shared bindings.

Publish the README, canonical contract and Workshop review evidence under the
existing per-change commit and push approvals. Publication and independent review
are this outcome's obligations; they do not hold recipient execution. Workshop
does not perform the sibling installations itself.

## Acceptance criteria

- [x] The /reconcile skill is installed, declared and connected to the /maintain
  skill through local rules; its shared issue format supplies BOUNDARY_SUMMARY.
- [ ] The published README and installation issues point to the same distributable
  project-agent skill, which owns discovery and communication instructions.
- [ ] Each installation assignment supplies its project-specific boundary summary
  and requires installation, local-code reconciliation and verification of the
  instruction entry point under the agent contract.
- [x] A dedicated skill is invoked at Workshop session startup, preserving recall,
  and uses the canonical Workshop rules without duplicating their authority.
- [ ] Review finds relevant issued work and replies, including completion reports
  on closed issues; repeating a review does not duplicate completed responses.
- [ ] Beginning or resuming reconciliation incorporates relevant issue discussions
  and returned project evidence before deriving remaining changes or assignments.
- [ ] Representative issue evidence demonstrates the obstacle, incomplete-result,
  verified-result and already-closed-result paths against the accepted contract.
- [ ] Verified results lead to the necessary record updates, acknowledgement and
  closure; missing evidence does not produce false acceptance or deployment claims.
- [ ] Published instructions and review evidence are accessible from the repository
  entry and original installation issues; recipient execution follows its actual
  activity conditions and operator authority.
- [ ] /verify confirms the implemented skill, startup wiring, publication and
  issue-review behavior against the governing contract and project verification set.

## Out of scope

Project-local installations of the supplied /collaborate skill are performed by
Cabinet and Daychi agents in their addressed GitHub issues. Application contracts and migration changes
remain in [migration changes](../migration-changes.md). No application source,
credentials, deployment, data migration or backend consolidation is changed here.
No new background polling service or mandatory sibling harness installation.

## Parent scope addressed

Workshop's operational side of first-stage agent integration: published entry,
addressed work discovery, problem handling, evidence review, current-record updates
and acknowledgement. Successful installation in both projects remains separate
work and is required by the overall stage completion condition.
