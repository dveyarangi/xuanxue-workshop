# local — Xuanxue Workshop rules

| target | anchor |
|---|---|
| `AGENTS.md` | `## Project-local` |
| `.agents/skills/verify/SKILL.md` | `## The verification set` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/reconcile/SKILL.md` | `## Project context` |

## L1 — project purpose and current state

- **target** `AGENTS.md`
- **authority** PRODUCT.md and the working tree, inspected 2026-10-03

<rule>
Xuanxue Workshop coordinates development across the school's software projects.
Read PRODUCT.md for the purpose and goals. Those goals describe intended capabilities;
the current tree starts with the product document and the development harness.
Distinguish proposed agreements, accepted contracts, and deployed capabilities.
</rule>

## L2 — project boundaries

- **target** `AGENTS.md`
- **authority** PRODUCT.md, goals 1, 3, 5, and 6

<rule>
daychi and xuanxue-cabinet are separate sibling projects. Work in this repository
does not implicitly transfer their ownership or authorize changing them. Identify
providers, consumers, data owners, responsible contributors, and affected projects
when recording shared contracts or coordinated work.
</rule>

## L3 — autonomy switches

- **target** `AGENTS.md`
- **authority** harness defaults and installation scope, 2026-10-03

<rule>
commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=ask
</rule>

## L4 — Python runtime

- **target** `AGENTS.md`
- **authority** verified local environment, 2026-10-03

<rule>
The harness scripts require Python 3.12 or later and only the standard library.
In this workspace, run them with uv run --offline --no-project python.
</rule>

## L6 — audience of the project README

- **target** `AGENTS.md`
- **authority** the user, 2026-10-04, repository-link onboarding clarification

<rule>
README.md is the product entry point for contributors and project agents. Direct
an arriving agent to the canonical collaboration skill. README and installation
issues point to the skill rather than duplicating its working instructions.
Keep harness installation commands, maintenance commands and installation reports
out of it.
</rule>

## L7 — question debug mode

- **target** `AGENTS.md`
- **authority** the user, 2026-10-04

<rule>
debug=on
</rule>

## L5 — verification set

- **target** `.agents/skills/verify/SKILL.md`
- **authority** project toolchain inspected during installation, 2026-10-03

<rule>
Run from the repository root:

```
uv run --offline --no-project python .agents/scripts/gw/harness.py . --check
uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --check
uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --check
```

The harness check clones its announced source ref and requires network access.
There is no application toolchain, typechecker, or application test suite in this
repository yet. For documentation changes, verify claims against PRODUCT.md and
the affected projects' authoritative sources, and verify referenced paths exist.
When changing records, run the owning mechanism's validator for those records.
</rule>

## L8 — boundary reconciliation during maintenance

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-04, reconciliation and cleanup agreement

<rule>
For maintenance of Workshop's project or boundary records, invoke the /reconcile
skill at .agents/skills/reconcile/SKILL.md before the final report. Include its
boundary comparisons, record changes, issue links and unresolved evidence in
that report. Check its declaration and installed bindings with the existing
mechanisms.py --check and inject_rules.py --check commands.
</rule>

## L9 — reconciliation sources

- **target** `.agents/skills/reconcile/SKILL.md`
- **authority** the user, 2026-10-04, references instead of repeated project facts

<rule>
Read these repository-relative sources:
- Project repositories: README.md, Repository map.
- Observed boundaries and source revisions: docs/current-system.md.
- Accepted targets and consumers: docs/boundaries.md.
- Planned changes: docs/migration-changes.md.
- Scope limits: docs/stage-1.md.
- Ownership, routing, autonomy and acceptance: docs/agent-contract.md.
- Issue format and BOUNDARY_SUMMARY: skills/collaborate/workshop-issue-format.md.
</rule>
