# Rule failures

## 2026-10-05 — Implementation briefs deferred the shared contract definition

Status: amendment landed locally and bindings verified; the pilot contract itself
remains unresolved, and no pilot implementation issue was published.

Rules in play: [reconcile/RC1](../.agents/mechanisms/reconcile/reconcile.rules.md)
separates shared guarantees from project implementation ownership; the
[/reconcile skill](../.agents/skills/reconcile/SKILL.md) compares requests,
responses, identifiers and errors and resolves shared decisions. The prior wording
did not make a fully prescribed common shape a publication precondition.

The pilot drafts assigned Cabinet to publish typed definitions and exact window
semantics after issue creation, with Daychi implementing against the later output.
Their public/read-only scope and outcome checks were explicit, but formats,
parameters, time/window semantics, refresh interpretation and a pinned common
authority remained unsettled. The assistant treated project ownership of the
executable home as permission to complete those shared choices inside recipient
implementation. This differs from the earlier repeat-investigation failure:
the proposed implementation was new, but its common boundary input was incomplete.

The user required the applicable contract-shape dimensions to be named first and
one prescribed shared shape to be the primary invariant of issued work. Amendment
shown before writing: "Implementation issues sharing a boundary must prescribe
the same fully specified contract, through one accessible immutable reference,
with no unresolved choice that could change interoperability or a shared data
guarantee." The full operative text is RC2 in the authored rule source.

RC2 reaches reconciliation and alignment through the shared installer. The skill
now gates publication, including Planned implementation issues, on completeness
and reviews the issue set together. Its contract-shape reference covers the
applicable dimensions without adding unagreed guarantees. The shared issue format
requires the common reference and conformance outcomes. Both pilot drafts are
marked incomplete and not issuable; their missing values belong to
[q-0002.0007.0005 — What is the exact public-schedule contract for the Cabinet–Daychi pilot?](questions/q-0002.0007.0005-what-is-the-exact-public-schedule-contract-for-the-cabinet-daychi-pilot.md).

Verification: the pre-install rule check rejected both outdated blocks; after
regeneration the injector, mechanism and full harness checks pass. Nine isolated
binding assertions reject removed/altered RC2 in each copied skill and pass on
restoration. These check installation, not automatic semantic completeness.
[Reconciliation evidence](mechanisms/reconcile.evidence.md#shared-contract-shape-invariant--2026-10-05)
holds the output-grading cases and limits. No commit, push or sibling edit occurred.

## 2026-10-05 — Completed reconciliation reissued as project investigation

Status: document/instruction separation and staged reconciliation amendment
landed locally after the user's clarification. At the user's request on 2026-10-05,
both mistaken issues were withdrawn and closed as `not_planned`. Readback verified
their state and withdrawal notices. The historical audit below records the failure
and repairs as they developed; the actual remaining-work breakdown is outstanding.

Rules in play: [/reconcile, Compare and reconcile](../.agents/skills/reconcile/SKILL.md)
assigns source inspection and boundary comparison to the working Workshop agent,
requires a disposition for each difference, and limits missing-evidence requests
to specific evidence needed for that comparison. Its installed ticket/P12 shapes
new assignments through /ticket and /impact; it does not establish that an old
proposal remains necessary. [Scope responsibilities](agent-contract.md#boundary-scope-and-product-language)
give projects implementation and interface ownership without removing Workshop's
source-analysis responsibility.

Evidence: [the completed pass](reconciliation-20261004.md#boundary-comparison)
already traced the providers, consumers, route definitions, schedule decoder,
identifiers, credentials, reminder state and content access. Subsequent alignment
settled many of its shared-policy gaps. The assistant nevertheless promoted the
older broad contribution proposals into
[cabinet-contract-contribution #3](https://github.com/dveyarangi/xuanxue-workshop/issues/3)
and [daychi-contract-contribution #4](https://github.com/dveyarangi/xuanxue-workshop/issues/4),
asking project agents to repeat inventory and proposal work. Local source access
was available for both projects; Daychi's remote 404 limited remote provenance,
not local code inspection.

Reasoning failure: the assistant treated project ownership of executable design
as a reason to delegate boundary investigation, treated the existence of the old
proposal as evidence of unfinished work, and used /impact to justify its two-owner
split without first subtracting completed analysis and accepted decisions. The
tracker distinction itself was understood: no duplicate local tickets were minted.
The wrong work was selected for the recipient issues. The assistant attributed
approval of that substituted scope to the user's instruction to proceed with
reconciliation issues, then recorded that interpretation as an approved split.

Proposed clarification shown in the diagnostic turn: "For each proposed assignment,
identify the remaining project action after accounting for completed analysis and
accepted decisions; request only evidence Workshop cannot establish itself."
No rule was installed in this turn. The instruction's placement and whether it adds
anything to the existing comparison/disposition requirements require alignment;
the immediate failure is failure to apply those requirements. Existing ownership
and accepted application contracts remain fixed.

### Instruction and chronology audit — 2026-10-05

The user requested explicit attribution rather than a generic failure explanation.
The agent read the original chat's turns as well as the instructions and Git history.

| Source | Actual instruction or recorded choice | Contribution to the failure |
|---|---|---|
| /reconcile, Compare and reconcile | Inspect sources, compare each boundary and classify each difference; request specific missing evidence when needed. | Read in the readiness audit and P12 installation turns. The posting pass reused the old assignment draft without refreshing the comparison/disposition against subsequent alignment. This was incomplete execution, not an instruction to delegate the investigation. |
| reconcile/RC1 | Leave executable interfaces and internal mechanisms to projects; inspect implementation to verify guarantees. | The agent overread the first clause as delegating investigation. The second clause contradicts that interpretation. RC1's distinction between ownership and investigation should be made explicit, but it was not the origin of contribution workflow. |
| architecture and migration proposal at ba5e35f | "Workshop reconciles the two contributions"; broad per-project inventory/proposal assignments. | This workflow predates RC1 and survived the completed analysis. The agent treated proposal existence and architectural wording as evidence of outstanding work. |
| Original chat, "what proposals?" | The assistant requested concrete clock/retry/removal/sign-out designs and said they fit the existing contributions. | The narrow project-owned design remainder was folded into an older broad source-inventory assignment. This bridge preceded RC1. |
| Original chat, readiness/impact question | The assistant answered "prepare the Cabinet and Daychi contribution issues" before P12 was installed. | The wrong work was already selected before the new shaping rule. P12 did not cause that selection. |
| ticket/P12 and /ticket step 4 | Run shaping/impact and obtain approval of the numbered post-impact split. | The agent read both skills and refreshed impact but did not present that concrete split. It incorrectly treated "lets do it" as approval of the substituted old breakdown. This is an additional execution failure. |
| /impact | Challenge whether work solves a demonstrated problem and can be narrower. | The written assessment defended separation by project but did not compare the requested deliverables against work already completed. |
| Duplicate search and readback | Search existing issues; check created titles, bodies and labels. | These passed, but completed work was in source analysis and local records, not another issue. They cannot establish assignment necessity. |

Git shows the contribution workflow in published `ba5e35f` (2026-10-04) before
the later RC1 addition. The original chat's readiness reply also selected the
contributions before ticket/P12 was installed. Context compaction occurred during
the posting turn, after that selection; it is not evidence for the origin of the
mistake. The publication-review rejection occurred later still and changed only
the payload. Neither is needed to explain the initial misclassification.

Proposed repair for alignment, not installed:

- In RC1's authored rules file, replace the ownership/inspection wording with:
  "Project ownership of executable interfaces and internal mechanisms concerns
  design and implementation; source inspection and boundary comparison remain the
  working agent's responsibility." Preserve its existing boundary guarantees,
  escalation test and question-bound provisional status, then regenerate both copies.
- At /reconcile's comparison-to-issue handoff, add: "Each proposed assignment must
  cite a current comparison row and state the remaining recipient action after
  completed work and accepted decisions are accounted for. A missing-evidence
  request names the exact proof and why the working agent cannot obtain it."
- Correct the project records that still make broad contribution requests a
  prerequisite for Workshop analysis; preserve project design and implementation
  ownership. Close the mistaken issues as created in error, with evidence links,
  after the repair is agreed. Prepare actual remaining-change briefs from the
  current comparison and apply /ticket's existing presentation/approval rule.

Verification proposed: a completed analysis with an old open proposal produces no
repeat-inventory issue; an accepted target with a demonstrated implementation gap
produces a concrete owner action; inaccessible runtime/deployment proof produces
only a specific evidence request. The user grades the output before publication;
installation checks alone cannot grade these semantic choices. No new generalized
ticket rule or mechanical semantic validator is proposed from this one failure.

### User clarification and landed amendment — 2026-10-05

The user identified the deeper separation: documents supply information, never
agent instructions; instructions do not belong in `docs/`. Reconciliation is an
umbrella process with initial collection, intervening decision/delivery cycles
and publication. A return from a nested cycle resumes the same pass.

Mechanism-shape/R9 now reaches the entry file and /mechanism from its authored
rules file. The /reconcile body now has explicit stages, a report resumption point,
working-agent collection ownership and assignment derivation from remaining
comparison findings. The architecture's broad contribution workflow and the
agent contract's active Workshop procedure list were removed; current migration
records no longer carry the repeat-investigation briefs. Their issued status and
failure history remain information. Earlier RC1-wording proposals were not applied;
its provisional question remains open. The adopted repair addresses instruction
authority and process continuity without making /reconcile an every-turn trigger.

[Reconciliation evidence](mechanisms/reconcile.evidence.md#staged-umbrella-process--2026-10-05)
and [mechanism-shape evidence](mechanisms/mechanism-shape.evidence.md) hold checks and
limits. The rule amendment is landed; correction of the two external issues remains
unresolved and does not imply completed application migration.

## 2026-10-04 — Boundary agreement prescribed project UX

Status: scope responsibilities documented, L11 installed as the project-context
pointer, and reconcile/RC1 installed in /reconcile and /align; presentation
prescriptions and agent instructions removed from the affected boundary records.

Rules in play: [architecture responsibility](architecture.md#responsibility) and
[agent obligations](agent-contract.md#accepted-obligations) separate Workshop's
shared agreements from each project's implementation authority. The assistant
bundled a visible stale-data warning into the cached-reminder boundary decision
and treated the user's choice of active reminders as agreement to that UX.

The user required a robust distinction: Workshop is aligning boundaries;
implementing projects decide presentation. Product-language recommendations are
separate work. The [scope-of-authority contract](agent-contract.md#boundary-scope-and-product-language)
owns this accepted clarification. The visible-warning requirement and other
presentation prescriptions were removed while retaining accepted data and
consistency guarantees.

Amendment shown before installation: "For Workshop boundary alignment,
reconciliation and assignments, apply the scope-of-authority contract in
docs/agent-contract.md#boundary-scope-and-product-language."

L11 in [local.rules.md](../local.rules.md) targets /align and /reconcile. Its
observable check is that the next boundary proposal states the shared obligation
and leaves its UI to the implementing project; later product-language advice is
identified separately. Installer checks establish the binding, not future agent
compliance.

Struck again, 2026-10-04: the assistant framed clock handling, pending-edit
tracking and removal retention as the next Workshop alignment work. Its examples
were useful verification scenarios, but it did not clearly distinguish the
projects' design work from unresolved cross-project decisions. The user challenged
that scope and identified the resulting distinction as a rule candidate.

Rules additionally in play: [architecture responsibility](architecture.md#responsibility)
assigns executable interfaces and internal architecture to the projects; L11
already brings the scope-of-authority contract into /align and /reconcile.

Candidate shown for agreement:
"Workshop states shared guarantees and observable acceptance outcomes. Project
owners design their executable interfaces and internal mechanisms. Inspect
implementation details to verify those guarantees. Bring a detail to alignment
when it reveals an unresolved cross-project obligation or requires changing
accepted ownership, behavior, compatibility or scope."

Disposition: the user rejected the proposed home in the scope contract: the
instruction belongs to /reconcile and must be installed in /align too. The
contract holds responsibilities and guarantees, not agent instructions. The
corrected generic rule text was shown before writing
[reconcile/RC1](../.agents/mechanisms/reconcile/reconcile.rules.md), then installed
in both skills. L11 remains a project-context pointer, not the owner of RC1.
The existing imperative paragraph was removed from the contract while its
accepted responsibility division was retained.

Observable check: a subsequent project assignment asks for evidence against
agreed guarantees, and an internal design choice reaches alignment only under
RC1's boundary test. Structural installation and its negative checks are held by
[reconciliation evidence](mechanisms/reconcile.evidence.md); they do not establish
future semantic compliance.

Provisional status, accepted by the user, 2026-10-04: RC1's restriction can hide
incomplete project logic encountered during reconciliation. Its authored section
is now a straw dog bound to
[q-0002.0002.0001 — How should reconciliation surface incomplete project logic without assuming implementation ownership?](questions/q-0002.0002.0001-how-should-reconciliation-surface-incomplete-project-logic-without-assuming-implementation-ownership.md).
Project ownership remains fixed. A broader detection and return method is not yet
accepted; RC1 remains operative while that question is open.

## 2026-10-04 — Alignment recommendations without alternative trade-offs

Status: amendment refused as redundant; pending question presentation corrected.

Rules in play: [/align, What to do](../.agents/skills/align/SKILL.md) requires a
recommendation for each question and pros, cons and trade-offs when alternatives
exist. Its "Problem before machinery", "Lead with the decisive fact" and
"Discuss concrete scenarios" sections govern the evidence and framing.

The assistant asked one question at a time and recorded the answers, but repeatedly
presented a preferred rule followed by "Agree?". It did not consistently show the
viable alternatives and consequences. The user challenged this presentation.
The accepted answers remain accepted; the pending stale-schedule question has
not been answered.

Proposed amendment: "Before asking for a decision, present its concrete failure,
viable alternatives and trade-offs, then recommend an answer."

Disposition: refused as a restatement of the explicit instructions already in
/align. The failure was execution, not missing instruction. Repair is to present
the pending choice against observed cache behavior, comparing continued cached
reminders with pausing reminders after a failed refresh. No skill rule or accepted
application contract changes in this correction.

## 2026-10-04 — Accepted schedule authority asked again

Status: local clarification installed in /align; accepted application decisions unchanged.

Rules in play: [AGENTS.md](../AGENTS.md) says not to reopen an accepted decision
without new evidence. [/align, Check whether it was already decided](../.agents/skills/align/SKILL.md)
requires finding and citing existing decisions before treating a question as open.

The assistant read [accepted schedule ownership](boundaries.md#accepted-responsibility-boundaries)
and [Daychi delivery](boundaries.md#accepted-daychi-reminder-delivery), then asked
whether Cabinet should be the sole schedule authority. The reply itself cited
Cabinet ownership. The failure was applying the decision: the assistant promoted
the unresolved HTML-fallback disposition in migration-changes.md into a question
about authority and bundled it with a new stale-cache proposal. No new evidence
against Cabinet ownership had been found. Exact fallback retirement and outage
behavior were not established by the authority decision, but authority itself
was not open.

Amendment, shown before installation: "When a proposal combines an accepted
decision with unresolved consequences, cite and hold the accepted decision
fixed; ask only about the unresolved consequence. An open migration detail
does not reopen its governing decision."

The rule is authored as L10 in [local.rules.md](../local.rules.md) and installed
at the end of /align, after its other installed blocks. It refines the existing
rule without amending core. The expected observable result is that the next
schedule proposal holds Cabinet authority fixed and asks only about an actual
unresolved behavior; installation checks do not prove that future behavior.

## 2026-10-04 — Alignment stopped after answering a clarification

Status: amendment refused as redundant; execution corrected by resuming alignment.

Rule in play: [align, What to do](../.agents/skills/align/SKILL.md) requires walking
the decision tree one question at a time. The user repeatedly asked the assistant
to continue after replies ended at recording or explaining the current decision.
The assistant treated a clarification as the end of the ongoing alignment.

Proposed amendment: "After answering a clarification during an active alignment,
continue with the next substantive unresolved decision in the same reply unless
the person pauses or ends the session."

Disposition: refused as a duplicate of the existing alignment obligation and the
user's explicit continuation instructions. No additional mechanism is needed;
the failure was execution. The assistant resumed with the unresolved guest-reminder
decision rather than requesting another instruction to continue.

## 2026-10-03 — Question placement without capturing unresolved decisions

Status: records repaired; rule clarification proposed, not installed.

Rules in play: [AGENTS.md Q1](../AGENTS.md) requires the store's other calls when
work opens or moves a question. [Questions skill, A raised question and Branching](../.agents/skills/questions/SKILL.md)
requires looking up unresolved decisions and recording the load-bearing ones.

The assistant repeatedly placed turns at the architecture root, but left its emerging
decisions only in prose. The user identified the omission. Installed rule blocks
validated without diagnostics; automatic hook invocation in this chat was not verified.
The failure was incomplete application of instructions already available to the agent.

Repair: six child questions were created with the owning script, and the architecture
argument was updated to distinguish the user's process sketch from assistant proposals.

Proposed amendment to Q1: "Before replying, reconcile the turn's unresolved
load-bearing decisions with the question store: point to an existing answer or question,
or open the missing question. Placing the turn at a parent does not replace this step."
This is a proposal for the questions mechanism's owning rules file; no installed rule
or harness source was changed.

## 2026-10-03 — Ownership proposal preceded capability comparison

Status: ownership decision recorded and source comparison repaired; clarification
proposed, not installed.

Rule in play: [align, Cross-reference with code and Lead with the decisive fact](../.agents/skills/align/SKILL.md).
The assistant proposed frontend/backend groupings without tracing Cabinet's
existing schedule, user, and reminder implementations. The earlier visualization
also showed Daychi's optional server reminders without identifying the active
local notification flow. The user corrected the proposed ownership split.

Repair: recorded the user's provider assignments in architecture, inspected the
existing implementations, and opened the concrete migration question.

Proposed clarification: before proposing shared-capability ownership, compare
the existing providers' implemented behavior and active consumers, not only route
names or module inventories. No installed rule was changed.
