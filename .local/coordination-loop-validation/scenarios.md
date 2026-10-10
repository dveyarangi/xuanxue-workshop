# Coordination grading scenarios

Use the installed coordinator, stage instructions and validation criteria. These
are isolated tests, not instructions to post issues or assert current deployments.
Lesson reader fixtures preserve historical drafts; their relative contract link
resolves the exact published e209d272 Git object. Environment facts in them are
dated evidence, not a new runtime check. Evaluate stale-evidence handling separately.

## Independent adoption

Illustrative agreed standard, not a real project requirement: each backend's
existing health response gains a public `release` field, a lowercase full 40-hex
Git commit identifying the deployed application build. Existing response behavior
is preserved. No secrets or user data are included. A build lacking a resolvable
commit fails deployment preparation; it does not publish a fabricated release.
Evidence is the deployment's build revision plus its observed health response.
Each project owns its build/runtime changes and can adopt independently.

Project A has the exact field and matching deployment proof. Project B lacks it.
What work remains, for whom, and does either need a provider/consumer integration
gate? Also assess a draft for B permitting `release: "latest"`.

## Shared interface

1. A provider brief permits a maximum 200 rows; the shared contract requires a
   complete window and the consumer expects all rows. Both local test suites pass.
2. Both briefs omit cancellation behavior, but their shared authority specifies it.
   They each link the full authority. Assess whether omission alone proves a gap,
   and what changes if they explicitly exclude implementing cancellation.
3. The consumer gets `200 []` and retains the prior list; the provider correctly
   returned an empty successful result. Is this compatible?
4. Two readers have different internal caches but agree on externally required
   replacement and failure retention behavior. Does that require alignment?

## Entry, changes and return

5. An issue has no comments but its timeline mentions a PR reporting a blocker.
6. A reviewed prerequisite becomes accepted; its dependent issue has no new message.
   Client development needs installation; live integration also needs the provider.
7. Review invokes coordinator for a finding. Coordinator enters while that same
   issue review is active. What happens next? What if evidence changes meanwhile?
8. One issue publishes successfully and the second write fails. The first has a
   complete contract and identity. Resume without new permissions or duplicates.
9. A contract amendment and a recipient edit arrive after draft validation.
10. There is a factual typo in a current brief, no changed shared meaning.
11. The tracker cannot be read. What can be concluded and what may continue?
12. The provider reports green CI and completed implementation but no runtime
    evidence. The claimed outcome requires an actual native connection.

Give specific dispositions and identify instruction gaps. Do not treat an
instruction naming a requirement as evidence that an actual implementation obeys it.
