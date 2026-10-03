# local — Xuanxue Workshop rules

| target | anchor |
|---|---|
| `AGENTS.md` | `## Project-local` |
| `.agents/skills/verify/SKILL.md` | `## The verification set` |

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
- **authority** the user, 2026-10-03

<rule>
README.md describes the project as a product for its users. Keep agent setup,
harness installation, maintenance commands, and installation reports out of it.
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
