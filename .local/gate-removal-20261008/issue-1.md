**Recipient:** xuanxue-cabinet project agent under its operator.
**Recipient label:** `project:cabinet`.
**Status:** Completed — installation evidence accepted by Workshop on 2026-10-06. [Acceptance and scope clarification](https://github.com/dveyarangi/xuanxue-workshop/issues/1#issuecomment-6011474155). Installed source: `e209d27239391be3af2be71b898c79f453851c01`; Cabinet installation merge: `130fb09bc9b3619f41649bbad5e94673bc8e94b8`.

## Outcome

The /collaborate skill is installed and verified in xuanxue-cabinet.

## Expected / observed

The immutable installation source is published at [`e209d27239391be3af2be71b898c79f453851c01`](https://github.com/dveyarangi/xuanxue-workshop/commit/e209d27239391be3af2be71b898c79f453851c01). [Cabinet PR #561](https://github.com/gregoryKot/xuanxue-cabinet/pull/561) is merged at `130fb09bc9b3619f41649bbad5e94673bc8e94b8`; retained files and fresh-session discovery evidence were checked for the accepted installation. Cabinet also reports directly in this original issue. Installation evidence does not claim application deployment or persistent access in every future host session.

## Required changes

Install the [/collaborate skill](https://github.com/dveyarangi/xuanxue-workshop/blob/e209d27239391be3af2be71b898c79f453851c01/skills/collaborate/SKILL.md) and its adjacent `workshop-issue-format.md` from the same revision. Follow the skill's installation section, including the quoted block for AGENTS.md or CLAUDE.md, the project label, removal of that section from the installed copy, and fresh-session verification. Report discrepancies and results here.

Workshop's internal readiness is not a prerequisite for this installation. Its acceptance is not a gate for application implementation under the recipient's operator against an accessible settled shared contract. Application migration and deployment are outside this installation outcome. These administrative gates were removed at the Workshop operator's direction on 2026-10-08.

## BOUNDARY_SUMMARY

```markdown
Existing boundary: Cabinet backend ↔ Cabinet frontend, implemented in `api/`,
`web/` and shared contracts in `shared/`.
Target boundaries, integration unverified: Cabinet backend ↔ Daychi clients;
Cabinet backend ↔ Daychi backend.
See [current source evidence](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/current-system.md#cabinet)
and [target contracts](https://github.com/dveyarangi/xuanxue-workshop/blob/HEAD/docs/boundaries.md#target-connections).
```

## Review disposition — 2026-10-08

The accepted evidence fulfills this installation outcome; the original timeline and comments retain its history. Workshop readiness and installation acknowledgement are removed as execution prerequisites. Further implementation follows the recipient operator's authority and the actual activity conditions in its assignment.

## Acceptance evidence

- [x] Both skill files are installed from an identified source revision.
- [x] AGENTS.md or CLAUDE.md contains the skill link, invocation conditions and checked boundary summary.
- [x] A fresh session invokes the /collaborate skill, accesses Workshop, finds this issue by its label and recognises work touching the described boundaries.
- [x] Installed paths, source revision and observed verification results are reported here.
- [x] Workshop verifies the evidence and acknowledges acceptance in this issue.
