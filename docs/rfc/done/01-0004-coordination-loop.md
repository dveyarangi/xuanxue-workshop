# Cross-project changes stay coherent through delivery — implementation plan

**Authored:** 2026-10-06
**Last amended:** 2026-10-06

Implements [coordination-loop](../../tickets/done/01-0004-coordination-loop.md).

## Governing decisions

The [accepted mechanism revision](../../../.agents/mechanisms/reconcile/reconcile.md#accepted-separation-requirements--2026-10-06)
owns stage separation, coordinator-owned validation, ongoing issue review and
proportional execution. The [agent contract](../../agent-contract.md) owns project
authority and the exchange. The [architecture](../../architecture.md) separates
observed implementation, accepted targets and planned changes. Existing shared
application contracts and their immutable authorities remain unchanged.

The agreed design has one coordinator entry, scoped repository analysis, boundary
reconciliation, issuing and ongoing assignment review. Existing ticket/impact,
alignment, verification and maintenance are used at their applicable moments.
Stages are responsibilities, not required agent sessions or separate deliverables.

## Scope and ownership

| Part | Implementation and ownership |
|---|---|
| Coordinator | Add `.agents/skills/coordinate/SKILL.md` and its declared mechanism; it owns inputs, outcomes, routing, resumption and the shared validation set. |
| Analysis | Add `.agents/skills/analyse/SKILL.md` and its mechanism; extract existing collection subjects and evidence discipline, reusing current factual records. |
| Reconciliation | Narrow the existing instruction and declaration to comparison, dispositions and resolving differences against governing agreements. |
| Issuing | Add `.agents/skills/issue/SKILL.md` and its mechanism; own preparation, recipient/set review, current-brief maintenance, publication and readback. |
| Ongoing review | Retain `review-assignments`; make its findings route to the affected stage without recursively restarting discovery. |
| Shared validation | Move the full contract-shape reference into the coordinate skill directory; coordinator rules supply shared requirements at inception and validation. |
| Exchange format | Retain the collaboration companion as the single format for addressed assignments, direct dependencies, reports and boundary summaries. |
| Project bindings | Update authored local rules and reinstall; project-specific repositories, tracker, records and authority remain local. |

Each new mechanism declares its parts, readers, maintenance and retirement under
the existing mechanism format. Shared rules are authored once and installed;
stage bodies do not restate them. Calls to installed mechanisms follow the same
ownership convention. Existing generic scripts remain the installation machinery.

## Inputs, outputs and resumption

### Output inventory

| Output | Existing home and treatment |
|---|---|
| Scoped observed facts | Update current-system; link primary evidence instead of copying reports. |
| Accepted shared promise | Update its owning boundary/contract document only when the accepted promise changes. |
| Remaining work | Update the existing migration record, outcome ticket or addressed issue; no duplicate local ticket per recipient. |
| Recipient brief | Maintain its original issue; local drafts are review artifacts, not another authoritative assignment. |
| Resumption | Use the existing owning work record within its format; an inline action needs no new pass report. |
| Implementation evidence | Keep PRs, checks and issue reports at their source; records hold conclusions and references. |
| Mechanism verification | One evidence home per mechanism as required by the harness; stage evidence references the shared loop grading rather than duplicating it. |

No existing factual/contract record is retired by this refactor: those hold
different claims. Extra per-stage reports, observation formats, status ledgers
and duplicated evidence are excluded. Static skill/declaration files increase;
the implementation does not claim a net reduction in repository file count.

Coordinator inputs are a requested shared outcome, changed project evidence or
an assignment finding, plus governing agreements and existing work. It resumes
the applicable pass or ticket, recording scope, current action, evidence baseline,
pending decisions/dependencies and next action in that existing record. No extra
coordinator ledger or new state vocabulary is introduced.

The source role is explicit: proposed requirement, accepted obligation, observed
source behavior, checked deployment or reported result. One cannot establish the
others. An accepted standard can start work without a repository change; a source
change can warrant no action after comparison. A direct invocation of a stage
loads the same applicable coordinator requirements.

Analysis emits a scoped Markdown observation in the existing observed-state home,
configured by local rules. It has a stable project/scope heading; repository and
inspected revision; inspection date; previous evidence baseline or explicit
absence; responsibilities and data ownership; relevant interfaces, behavior and
standards; evidence links and their scopes; checks and deployment/configuration
evidence; changed facts; and unknowns or inaccessible material. Each factual claim
is bound to its actual source revision or observation. An aggregate heading cannot
imply that an older fact was rechecked. Inapplicable categories are explicit.

These are required information subjects, not a new serialized record type.
Workshop's configured home remains `docs/current-system.md`; analysis updates
its existing scoped sections without a new heading grammar, format migration or
observation-specific parser. Source-unavailable observations name the limitation
and do not claim an inspected revision. Existing evidence retains its own dated
limits; replaced live facts have one current home, with stable old anchors
retained as pointers where needed. Existing reference checks and review against
the information subjects validate this output. No separate per-stage report or
observation index is committed. A caller may delegate one repository and scope
without transferring normative decision rights.

Reconciliation retains its existing comparison fields and all dispositions.
It distinguishes implementation correction under an unchanged contract from an
accepted amendment. Missing evidence does not become a defect; unimplemented or
deferred targets do not become authorized work. An unresolved shared decision
returns to alignment; accepted decisions update their existing owning records.

Issuing consumes the approved outcome, governing requirements, current remaining
actions and dependencies. It continues an existing assignment where applicable.
Prepare recipient assignments as projections of the same immutable contract and
ownership relationships, informed by the scoped observed state and approved
change. For each shared obligation, derive the provider action, consumer action
and common conformance outcome together before composing the recipient briefs.
An already fulfilled obligation keeps its supporting evidence and counterpart
expectation; it does not generate redundant implementation work. Symmetry means
one shared meaning, not identical tasks or identical acceptance evidence.
This derivation belongs in the existing drafting/review work, without a separate
mapping register or generator. Recipient prose cannot independently redefine the
contract; necessary context and explicit immutable references make each brief
usable without reconstructing Workshop history.
It can emit implementation, design or evidence requests, explicitly distinguished.
Implementation requires the complete agreed shape even for Planned publication.
An issue is the current actionable brief, not a history of how it was discovered.
Publication retains the existing authority, fresh read and readback requirements.

Immediately before publication or an issue edit, check whether the governing
contract, relevant source evidence, dependencies or current issue content changed
since draft validation. Refresh only affected findings and checks. An unrelated
repository change does not invalidate a scoped observation; unresolved relevance
requires inspection, not an assumption of freshness. Preserve intervening issue
contributions and reconcile changed requirements before writing.

Issue-set publication may partially succeed. Record each successful issue identity
and readback in the existing pass, retain the remaining action, and resume by
updating or creating only what is missing. Do not duplicate, silently close or
recreate already published work. Do not claim the set is published until all
required bodies, contract references and direct dependency links are verified.
Each published implementation assignment must independently pass its contract
gate; a partial batch never permits an incomplete shared definition. Execution
eligibility still follows explicit dependencies, without an extra batch approval.

## Shared validation and stage checks

Coordinator requirements cover clarity for the next reader, consistency with
authorities and related outputs, and completeness of the declared scope. All
13 contract dimensions remain covered. Explicit unknowns are valid analysis
output; unknown shared choices cannot pass implementation publication. Every
in-scope obligation has an action and evidence of fulfilment, or a justified
disposition. Scope reductions and deferrals require their existing authority.

Install applicable shared rules into coordinate, analyse, reconcile, issue and
review-assignments, and into alignment and cross-project ticket shaping where
those requirements are needed. Keep longer criteria in a coordinator-owned
reference reached by the installed instruction. Recipient exchange fields stay
in their existing format. No second validation checklist is authored per stage.

Issue verification has two readings: a recipient reconstructs its work from the
brief, accessible authorities and its own repository/instructions; a set review
compares meanings, obligation coverage, dependencies and transition cases across
assignments. Independent grading is required for the substantive demonstration;
neither an author-only review nor successful scripts substitutes for it.

Ticket context is necessary implementation input, not removable ceremony. Each
reader receives only its own ticket, accessible cited authorities and its own
project context, without private Workshop clarification. Compare the resulting
interpretations against every applicable contract dimension and common case.
A pair of implementations allowed by the two briefs but incompatible with each
other is a publication-blocking counterexample. Brevity cannot omit context,
parameters, formats, data guarantees or acceptance conditions needed to rule it
out; internal designs may still differ. Process reductions preserve this check.

Maintenance rewrites the whole brief to its current meaning. An edit invalidates
only the relevant checks: a contract or dependency change requires corresponding
semantic review; factual/editorial correction needs a whole-body coherence and
reference check, not a new RFC, ticket or independent agent. Checks have no added
Ready approval. Common conformance cases remain with their contract authority.

Changed requirements are distinguished from clarifications of the same agreed
meaning. An amendment uses an accepted contract revision and explicit migration
obligations; it cannot retroactively redefine what satisfied a completed assignment.
Already-started dependent work is reassessed against the changed condition.

## Ongoing review and feedback

Preserve review after recall through L15. At coordinator entry, review relevant
assignments unless that work was already completed for this pass and no relevant
evidence changed. Review a full issue timeline including mentions and referenced
PR/commit artifacts, reports on closed issues and changed prerequisite evidence.
Evidence reused from an in-progress review is not rediscovered recursively.

Reuse established prerequisite evidence while its relevant basis remains valid;
do not request another confirmation merely because a new stage or session began.
Evidence stays at its source. Factual records retain the resulting scoped claim,
revision and evidence reference, rather than copying the issue conversation or
verification transcript. This preserves record reconciliation without creating
a second report exchange.

Route missing/changed facts to analysis; suspected shared differences to
reconciliation and alignment when needed; brief clarification to issuing; new
substantive work to outcome-based ticketing; completed work to evidence verification
and record reconciliation. Ordinary follow-up stays on the existing issue. A
problem arriving before completion is a first-class input. Fresh reads precede
responses and closure; tracker failure is reported, not treated as an empty inbox.

Dependencies specify the exact blocked activity and satisfaction evidence.
Development against an agreed contract can remain eligible while a provider blocks
live integration proof. Cycles or contradictory satisfaction conditions return
to coordination; arbitrary Ready labels cannot resolve them. Existing explicit
installation and operator conditions are retained rather than silently waived.

Acceptance evaluates the assignment's own outcome, reconciles affected records
before acknowledging it, and reassesses dependents. Published instructions,
implemented behavior, deployed support and verified integration remain separately
evidenced claims without a mandatory extra artifact for each. A handoff outcome
may finish while independently owned execution remains open.

## Rule migration and compatibility

Before changing instructions, account for each rule in existing collection,
comparison, resolution, publication, RC1/RC2 and local L8-L15: owner, reading
occasion and verification. This is implementation evidence, not a permanent
parallel instruction register. No rule is removed merely because its old owner
is being narrowed. Preserve the open RC1 question rather than silently settling it.

Move shared contract-shape ownership to coordinate and re-install its consumers;
retain a link at the old reference path for installed copies that resolve a moving
source. Pinned historical revisions remain unchanged. Check relative references
from the recipient package context as well as Workshop. Preserve the source
revision/version reporting contract and the complete boundary-summary format.

L9 distributes only the context each stage needs. L8 enters coordination for
cross-project maintenance. L13 continues to govern approved outcome-based work.
L14's review, original-channel action, acceptance and dependent reassessment
obligations remain authored once, with targets adjusted to their reading moments.
L15 keeps recall before review. The coordinator receives a finding from an active
review without invoking another review of the same work.

Update mechanism declarations, maintenance targets, architecture descriptions,
agent-contract references and collaboration-format links to the final ownership.
The architecture describes the result, not a second set of workflow instructions.
The readiness and application-integration tickets retain their independent scope.

## Implementation and proof

1. Establish the rule-preservation mapping and the valid/invalid cases below.
   Exercise existing declaration, installation and reference checks on isolated
   fixtures, confirming relevant failures and repairs before installing the new
   instructions. Reuse existing factual records; no observation parser or bulk
   format migration is required for this slice.
2. Add the three stage/entry instructions and declarations, then adjust existing
   instructions and authored rule targets in one coherent installation batch.
   Reinstall, repair links and run structural checks before using the new loop.
3. Exercise a scoped read-only lesson case from pinned evidence through drafts
   and subsequent issue findings. Do not create demonstration issues, mutate
   sibling projects or assert that the real integration is complete.
4. Exercise an explicitly illustrative shared-standard requirement whose projects
   can comply independently. Use it to detect forced provider/consumer assumptions;
   it does not adopt a monitoring vendor, standard or new product obligation.
5. Give substantive briefs to an independent reader with no Workshop conversation
   history, compare reconstructed obligations and grade the set. Retain the
   bounded result in the mechanism evidence. An independent agent may perform
   this check; operator authority over decisions and publication remains fixed.
6. Verify affected mechanisms and maintain their live outputs. Record the actual
   inspected scope and findings, not a manufactured clean baseline. Commit/push
   and external publication retain their separate approvals.

| Counterexample | Required result |
|---|---|
| Different parameter/time/refresh interpretations | Block implementation publication; return to the unresolved meaning. |
| Both briefs omit the same agreed obligation | Fail set completeness despite mutual consistency. |
| Valid source code but no deployment evidence | Preserve deployment uncertainty. |
| Referenced material inaccessible to the recipient | Fail actionable handoff; resolve access or supply usable authority. |
| Investigation history and obsolete wording in an edited brief | Rewrite to current work and recheck affected meaning. |
| Blocker reported through a linked PR before completion | Inspect its evidence and route the remaining coordination action. |
| Accepted prerequisite changes but dependent discussion is unchanged | Reassess the explicit dependent condition. |
| Interrupted pass or repeated unchanged review | Resume without restarting collection or repeating responses. |
| Simple factual correction | Complete inline with relevant checks and existing authority. |
| Tracker unavailable | Report the missing read/write and retain the pending action. |
| Only part of an issue set was published | Retain successful issue identities; resume missing work without duplication or a false completion claim. |
| Relevant contract, issue content or dependency changed after draft review | Refresh affected findings and validation before writing; preserve intervening contributions. |
| Provider unavailable but contract-based development is eligible | Block only the specified integration activity, subject to existing operator and installation conditions. |
| Cyclic dependencies or retroactive changes to accepted work | Return the contradictory obligation to coordination; do not invent eligibility or rewrite past acceptance. |

The minimal existing structural checks are `questions.py --check`,
`tickets.py --check`, `mechanisms.py --check` and `inject_rules.py --check`, plus
the affected reference/record checks. No new observation-validator test suite is
introduced. New mechanical checks require a demonstrated gap that existing checks
cannot cover; declaring any new record type would also require its mechanism
format and validator, so this plan deliberately retains the current record homes.
Implementation verification also runs the project's full verification set,
including the configured harness source comparison. Use Python 3.12+ through
the configured uv command. Script success establishes structural evidence only.

## Impact

Touches three new mechanism instructions/declarations, narrowed reconcile and
existing review, coordinator-owned shared rules/reference, analysis output requirements,
local installation targets and their derived blocks, and affected documentation
links. Observations reuse the current factual record; assignments retain their
existing exchange format and issue channel. No project implementation changes.

## Hidden edges

An old installed reference may follow HEAD while a contract pins a SHA; both must
remain usable. Changed evidence may invalidate only part of a scoped observation.
Whole-record timestamps must not imply universal freshness. Cross-stage routing
can accidentally recurse into review. Independent-standard adoption must not
inherit unnecessary integration gates. A complete draft can still omit a shared
obligation, so set coverage is separate from individual clarity.
Publication can partially succeed or race with new issue evidence; resumption
must retain successful work and refresh only invalidated findings. Changed scope
cannot silently rewrite the basis of earlier acceptance.

## Leave alone

Application promises, sibling source and releases, operator authority, accepted
deferrals, recipient protocol fields, existing readiness/integration outcomes,
and current approval switches. No background polling, dashboard, new mandatory
acknowledgement protocol or generalized agent platform is introduced.

## Recommendation

Proceed as one vertical slice. Reuse current rules, records, installer and review
instead of building a second workflow engine. The observed lesson failure and
the materially different independent-standard case bound validation. General
reuse beyond these cases remains a possibility, not an acceptance requirement.
This pass removes the proposed observation grammar/parser and retains all ticket
outcomes and dependencies. The added failure cases enforce existing resumption,
fresh-evidence and shared-contract obligations without adding approval stages.
