# Rule failures

## 2026-10-06 — Coordinator draft omitted input sources and action definitions

Status: closed; the user approved the replacement coordinator instructions and
the skill-up description trigger, installed and checked on 2026-10-06.

Struck again, 2026-10-06: the approved action table was compressed to rule IDs,
and the completeness review incorrectly counted that as preserving the requested
form. The user also identified missing explicit resumption conditions. Restored
the table in the coordinator skill with source condition, action and continuation,
plus recovery of the pending action from the existing work record. The acceptance
comparison now checks the requested structure as well as covered meanings.
The subsequent scoped maintenance replaced opaque route references with direct
skill links and removed repeated review, wait and dependency instructions; its
[evidence](mechanisms/coordinate.evidence.md#scoped-maintenance-of-the-further-work-change--2026-10-06)
distinguishes source tracing from independent behavioral grading.

Rules in play: [mechanism](../.agents/skills/mechanism/SKILL.md#siblings)
requires skill-up when writing skill instructions;
[skill-up](../.agents/skills/skill-up/SKILL.md) requires precise instructions,
references to existing owners and a fit/overlap/contradiction check. The assistant
did not invoke skill-up and drafted generic goal, obligation and next-action
wording without connecting it to the project's sources and existing stage routes.
The user identified that this left the resulting choice underdetermined.

Proposed amendment: apply skill-writing checks to drafts as well as installed
text; resolve each consequential input to its authoritative source or installed
project binding, and each action to its defined operation or owning skill.
Existing operations are referenced, not redefined. The
[question argument](questions/done/q-0002.0002.0004-when-should-coordination-propose-or-prepare-further-work.md#draft-rejected-for-unspecified-inputs-and-actions--2026-10-06)
holds the source/routing audit and amendment proposal. The replacement draft uses
those inputs and operations. The accepted coordinator section and installed L9
now connect selection to these sources and existing routes. The user chose a
one-sentence skill-up description amendment: "Use whenever writing any
instructions, whether to a file or directly in a reply." The broader proposed
body check was not added. Its upstream transfer is
[goodwolf-harness issue 3](https://github.com/dveyarangi/goodwolf-harness/issues/3).

## 2026-10-06 — Direct reconciliation lost its review entry

Status: repaired and independently graded.

The accepted [exchange contract](agent-contract.md#exchange-through-github-issues)
requires relevant issue review when reconciliation begins or resumes. The loop
extraction preserved review on coordinator entry but omitted its direct-reconcile
binding. Structural checks passed because they checked declared targets, not
whether an accepted invocation occasion had been omitted.

Amendment: existing review rule RA2 now says "At coordination or reconciliation
entry or resumption" and is installed in both skills. Its active/current-review
exception prevents repeated work. RA1 now checks direct entry explicitly.
[Maintenance evidence](mechanisms/coordinate.evidence.md#maintenance--2026-10-06)
records the direct, reused and changed-evidence cases and their independent grade.

## 2026-10-06 — Investigation history published in a live assignment

Status: closed; issue and records repaired, and creation/edit-time coverage landed
in the [issue skill](../.agents/skills/issue/SKILL.md#validate-and-maintain), 2026-10-06.

Struck again in the agent contract on 2026-10-06: earlier maintenance removed
commit/dry-run history but left a duplicated readiness snapshot and installation
requirements mixed with role guarantees. The follow-up moves installation
requirements to onboarding, replaces status with links to its existing owners,
and corrects architecture's claim that readiness lives in the contract. The
[scoped report](maintenance-20261006.md#agent-contract-separation-follow-up--2026-10-06)
records surviving fact homes and preserves the published anchors. This applies
the existing A1/E1 rule rather than introducing a new document or workflow.

Struck again, 2026-10-06, in the onboarding contract: the assistant appended
Cabinet installation reports, acceptance and closure history to a document that
owns general access and source requirements. The case-specific disposition and
evidence belong to the reconciliation report. Removed the story from onboarding,
preserved the accepted case disposition in that report and retargeted its incoming
links. This repeats the purpose/home failure below; it does not extend the open
issue-brief validation question into a new onboarding mechanism.

Struck again in the wider 2026-10-06 maintenance scope: the general agent
contract retained installation chronology, and migration-changes retained the
withdrawn investigation proposal and its correction story. Replaced them with
pointers to dated evidence and preserved the moved facts in the reconciliation
report. The existing editorial-gate question remains the amendment's home.

The subsequent mechanism audit found that the earlier redundant-rule diagnosis
was too broad. The local ticket's actual-content and consistency rules depend on
stage/alignment; the external issue format and routine edit path have no explicit
final editorial gate. Improvement is held by
[q-0002.0002.0003 — How should Workshop validate issue briefs at creation and after edits?](questions/done/q-0002.0002.0003-how-should-workshop-validate-issue-briefs-at-creation-and-after-edits.md).
The historical diagnosis and proposed amendment below record what was said before
that audit; no new rule is installed by this correction.

Rules in play: [/maintain A1 and E1](../.agents/skills/maintain/SKILL.md) require
coherent records and one home per fact. [Publication preparation, now owned by /issue](../.agents/skills/issue/SKILL.md#derive-and-draft)
requires a current comparison and remaining recipient action; the pass report
owns stage and resumption history. The assistant updated Daychi issue 6 with a
misspelled-host/DNS anecdote, conversational decision attribution and commentary
about correcting its previous request. The factual update was checked, but the
issue was not reviewed as a standalone current work brief.

Proposed amendment: "Maintain an issued brief around its current outcome,
contract, prerequisites and evidence; keep investigation and revision history
in the owning pass report." An additional rule is declined because this repeats
the existing record-purpose and publication requirements and the user's explicit
correction. Execution repair: rewrite the live environment/test section, preserve
all contract and acceptance obligations, clean the coordinating ticket and related
records, and read back the issue. The correction history remains in the
[pass report](reconciliation-20261004.md#environment-and-fixture-follow-up--2026-10-06).

## 2026-10-06 — Empty comments mistaken for absence of a report

Status: amendment landed locally; binding, mechanism and harness checks pass.

Rules in play: [review discovery](../.agents/skills/review-assignments/SKILL.md#discover-pending-work)
required discussion and closure context, and [L14](../local.rules.md#l14--issue-review-action-and-return-to-work)
required reviewing project reports. The review read direct comments, found none,
and asked the user for a comment URL. Cabinet's installation report was already
linked from issue 1's timeline to PR 561. The discovery wording also excluded
pull requests without distinguishing assignment selection from report evidence.

Amendment shown before writing: read the full paginated timeline and follow
relevant PR, commit and issue references to their reports, artifacts and checks.
Empty comments do not prove no report; a mention does not prove completion;
inaccessible references remain explicit uncertainty. L14 owns this shared rule
and installs it into review and reconciliation. Primary assignment discovery
excludes PRs while report inspection includes referenced PRs.

The [real-corpus replay](mechanisms/review-assignments.evidence.md#timeline-discovery-and-cabinet-replay--2026-10-06)
found reports for both Cabinet assignments and detected changed PR/CI evidence
on reread. Structural checks verify installation, not semantic review quality.

## 2026-10-05 — Assignment status obscured execution dependencies

Status: amendment landed locally; harness, declaration and binding checks pass.

Struck again, 2026-10-08: a Daychi agent stopped at the original readiness and
installation-acceptance holds despite a settled accessible implementation contract.
L14 reassessed fulfillment of written dependencies without reassessing whether
they protected an obligation. L16 required removing steps that protect none but
did not put that assessment at the review occasion. The earlier correction removed
an extra Ready approval while retaining the original ceremonial dependency.

Amendment shown before writing and accepted by the user's request: L14 assesses
each dependency's necessity and fulfillment from current source, executed checks,
runtime and operator evidence, updates the original issue, and removes unsupported
holds. Document claims, status and acknowledgement alone establish neither. Only
activity-specific observable conditions remain; shared promise changes return to
alignment. Readiness and installation acceptance do not gate recipient implementation.
The issue format and contract are corrected at their own homes. This supersedes
the installation-before-development example below; provider-before-native-proof
remains necessary. The amendment is landed locally and the original issue bodies
are updated; publication of this rule follows the existing commit/push checkpoint.
Binding, mechanism, ticket and question checks pass. The full harness reference
check detects the pre-existing `skill-up` description change; this pass leaves
that unrelated source divergence intact.

Struck again, 2026-10-06: the review treated coordinator readiness and record
publication as extra acceptance criteria for Cabinet's verified installation.
Readiness was an execution prerequisite; the installed review rule already
permits acknowledgement confirming that no shared boundary changed. The review
added an unnecessary hold instead of applying those distinctions. Correction:
accept/close the complete installation, return its prerequisite effect to issue 5,
and retain coordinator readiness and provider conformance in their own scopes.
The landed dependency and acknowledgement wording below covers this failure;
no additional approval rule or mechanism amendment is needed.

Rules in play: the [issue format](../skills/collaborate/workshop-issue-format.md)
required linked dependencies, and [collaboration discovery](../skills/collaborate/SKILL.md#check-addressed-work)
required reading them. The drafts nevertheless repeated readiness as a separate
application gate, used Planned without a satisfaction condition, and left the
Cabinet prerequisite insufficiently linked in Daychi's assignment. The user
asked who would remember to set work Ready. Draft repairs alone left future issue
creation and dependency-change handling ambiguous.

Amendment shown before writing: link direct prerequisites, distinguish starting,
integration and completion, identify satisfaction evidence and acceptance owner,
and derive eligibility without an extra Ready approval. The format owns these
conditions. Collaboration discovery points there; local review rule L14 requires
reassessment of affected assignments when prerequisite evidence changes.

The installation-before-development and provider-before-native-proof cases have
different blocked stages and share the need for explicit dependency conditions.
No new issue state, acknowledgement ledger or background monitor was introduced.

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
[q-0002.0007.0005 — What is the exact public-schedule contract for the Cabinet–Daychi pilot?](questions/done/q-0002.0007.0005-what-is-the-exact-public-schedule-contract-for-the-cabinet-daychi-pilot.md).

Verification: the pre-install rule check rejected both outdated blocks; after
regeneration the injector, mechanism and full harness checks pass. Nine isolated
binding assertions reject removed/altered RC2 in each copied skill and pass on
restoration. These check installation, not automatic semantic completeness.
[Reconciliation evidence](mechanisms/reconcile.evidence.md#shared-contract-shape-invariant--2026-10-05)
holds the output-grading cases and limits. No commit, push or sibling edit occurred.

## 2026-10-05 — Completed reconciliation reissued as project investigation

Struck again, 2026-10-06: the proposed Cabinet follow-up asked for provider setup
and fixture instructions before reading the existing runbook, deployment probes
and lesson-management controls. The user supplied host addresses and required
Workshop to derive what its own source inspection could establish. The explicit
[Collection rule, now owned by /analyse](../.agents/skills/analyse/SKILL.md#analyse-a-projects-relevant-behavior)
already makes collection the working agent's responsibility and limits evidence
requests to specific gaps it cannot establish. The earlier proposed amendment
below already covers this repeat; no additional rule is needed. Execution
correction: inspect and record the live staging provider and existing controls,
update the Daychi assignment, and retain only operator-specific coordination and
unperformed native-test evidence as unknowns. These checks do not settle the
separate required-data validation finding.

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

Struck again, 2026-10-10: native recipient questions exposed that RC1/L11's
project-ownership distinction had been applied to security protocol choices simply
because they could preserve the same visible wire. The user clarified that
Workshop selects security principles and protocols even without a wire change.
That accepted amendment is landed in
[Security authority](agent-contract.md#security-authority), within the role contract
L11 already brings to alignment. Native-token protection, pending-login protection
and continuation decisions are now in the native contract and paired local briefs;
amended publication is not yet claimed.

The subsequent URL question further separates browser exposure from inter-project
dependency: an exact continuation pathname need not be chosen by Workshop merely
because the browser visits it. The assistant's claim that choosing `/login/native`
was itself required by the security correction was too broad. The
[native ticket diagnostic](tickets/01-0008-native-cabinet-account-session.md#continuation-url-diagnostic--2026-10-10)
holds the concrete distinction and independent material. The existing completeness
criteria continue to govern shared behavior; no rule requiring Workshop to choose
every browser-visible route is proposed.

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

Struck again, 2026-10-08: during native-session alignment, the assistant read the
agreed browser/code-and-PKCE method but treated its provisional wording as a reason
to ask for the method again. The user corrected the repeated approval request.
The entry prohibition on reopening accepted decisions and
[L10, accepted premises during alignment](../local.rules.md#l10--accepted-premises-during-alignment)
already required holding the method fixed and asking only about unresolved wire
or recovery consequences. Proposed reminder: "Provisional wire details do not
reopen an agreed acquisition method." Refused here as a restatement of L10, with
no rule addition. Execution correction: record the reaffirmed method in its
operative contract home and continue with actual unresolved failure behavior.

Struck again, 2026-10-05: while resuming reconciliation, the assistant treated
retirement of incomplete implementation drafts as revocation of the agreed public
schedule connection and asked the user to select it again. The user corrected
that inference. L10 and the entry prohibition on reopening accepted decisions
were already operative; there was no new evidence against the scope. The records
now distinguish retained scope from retired drafts, and work continues on the
unresolved shared contract. The installed amendment below remains applicable;
no duplicate rule is added.

Struck again, 2026-10-05: after recording the complete-window read and refresh
scope, the assistant presented ordinary successful reload as a fresh decision.
The user pointed out it was already decided. This follows from the accepted
current-schedule result and reschedule/cancellation behavior; no new contrary
evidence was found. L10 and the existing prohibition on reopening decisions
already cover the case. Proposed wording, "Do not ask approval for consequences
entailed by accepted behavior," is refused as redundant with those instructions.
Execution correction: remove successful refresh from the unresolved list, record
its derivation against the accepted scope, and continue shared conformance work.

Struck again, 2026-10-05: the assistant turned consolidation of the accepted
contract and source-derived details into a blanket reapproval checkpoint. The
user requested another planning pass instead. The pass also found draft wording
requiring Workshop alignment for every shared version change, contradicting the
accepted compatible-coexistence autonomy in the agent contract. No published
agreement or application code was changed. The consolidation was corrected,
its evolution clause restored to the existing agreement, and participant/result
review paths checked. Proposed amendment, "Consolidation does not reopen its
accepted inputs or add authority," is refused as redundant with L10 and the
scope/evolution constraints already read. Execution correction: land the fixed
definition, remove the false reapproval gate and present only the actual local
breakdown/publication checkpoints.

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

Struck again, 2026-10-11, session `01a127cf-692a-70d1-b8d4-28b653b5ce15`:
an ordinary greeting invoked recall and assignment discovery, but the assistant
ended after finding a new Cabinet provider report without proposing the next
action or requesting its start. The initial diagnosis incorrectly called the
status-only stop itself a violation. The user clarified that a greeting means
status, followed by a proposed action under step=ask or execution under step=auto.
The later answer-only restriction was respected. The
[fresh-entry diagnosis](questions/q-0002.0005.0002-does-ordinary-workshop-session-entry-invoke-and-exercise-assignment-review.md#discovery-stopped-before-review--2026-10-11)
records the corrected diagnosis and fresh-session grading cases. Local L15 now
defines that entry handoff and local L3 sets step=ask using the existing ask
default. The earlier automatic-review proposal was withdrawn. Issues remain
unchanged during the user's pipeline-only diagnosis.

Struck again, 2026-10-10: clarification about the reviewed native-session tasks
and their next step led to explanatory replies without a clear pipeline stage
and concrete next action. The user corrected the initial diagnosis: repeated
verification is acceptable; settled questions must not return without changes
that make them relevant. The entry contract, L10 and coordinate continuation
already preserve accepted decisions and the selected step. No additional generic
continuation or anti-rechecking reminder is proposed. The user accepted the stronger
report sentence in English. L18 in local.rules.md overrides coordinate's reporting
requirement and is installed there: stage, next action, actor and any condition
for proceeding are explicit at a handoff or pause.
The user authorized the prepared publication; commit b8ab296 and
native issues 7/8 were published and read back. The distinct conclude-only push
restriction is repaired by L17 in local.rules.md, installed into AGENTS.md and
/conclude with push=ask retained. Its diagnosis and behavioral cases are recorded in
[the pipeline question](questions/done/q-0002.0002.0005-how-should-the-delivery-pipeline-make-its-current-stage-and-next-action-clear-without-reopening-settled-decisions.md).

Struck again, 2026-10-06, session `01a1114c-a3d8-7b71-be77-b242d14ca5cb`:
the initial question asked what /coordinate says, but subsequent clarification
established the expectation of preparing further work while recipient results
wait. The assistant continued explaining the route instead of carrying out
concrete preparation. It let queue order and downstream execution/publication
conditions stand in for a preparation hold. The
[coordinator selection instruction](../.agents/skills/coordinate/SKILL.md#select-the-next-action)
already requires considering further work during external waits, assessing
preparation separately and continuing available authorized actions. Its
[declaration](../.agents/mechanisms/coordinate/coordinate.md#what-would-show-it-working-graded-by-someone-who-did-not-build-it)
explicitly rejects blocking unrelated contract preparation on integration.
Proposed reminder: "Continue authorized preparation to the next actual checkpoint
after answering a clarification." This repeats the previously refused amendment
below and the existing coordinator instruction; no rule change is made.
The diagnostic identifies an execution failure; concrete next-work preparation
has not been completed by this diagnostic.

Struck again, 2026-10-06: after the user requested conclusion and commit, the
assistant stopped for another confirmation of the connected Workshop bundle.
The user reiterated the commit instruction. Existing explicit authorization takes
precedence over a skill's default clarification guidance; no additional approval
rule is needed. Execution correction: commit the prepared work and its dependencies.

Struck again, 2026-10-05: the assistant ended several replies after recording a
decision or installing the reconciliation feedback step, without continuing the
already-authorized readiness work or reaching a genuine human checkpoint. The
user asked why replies stopped after three sentences. The same rejected amendment
below applies; no second entry or duplicate rule was added. Execution correction:
continue the current readiness ticket through planning, implementation and checks,
with short progress updates between actions. This does not grant commit, push,
repair or next-cycle permission.

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
