# reconcile — evidence-backed boundary records and actionable project updates

- **instruction** `.agents/skills/reconcile/SKILL.md`
- **state** installed

## How it works

The /reconcile skill compares independent projects with their coordinating records.
Its procedure is portable; the project's local rules supply source pointers and
bind the pass to maintenance. The pass separates observed state from agreed targets
and produces addressed work only when a project must act. It owns no application
contracts, project routing convention or issue format.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| checking boundaries and deriving instruction summaries | `.agents/skills/reconcile/SKILL.md` | |
| choosing a disposition and issuing work | `.agents/skills/reconcile/SKILL.md` | |
| configuring source pointers and the maintenance binding | `.agents/skills/mechanism/SKILL.md` | |
| installing or retracting local bindings | `.agents/scripts/gw/inject_rules.py` | |
| checking declaration and installed bindings | `.agents/scripts/gw/mechanisms.py` | |
| handing results to the project's acceptance process | `.agents/skills/reconcile/SKILL.md` | |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction | `.agents/skills/reconcile/SKILL.md` |
| declaration | `.agents/mechanisms/reconcile/reconcile.md` |

The project authors source pointers and the maintenance invocation in its local
rules file. Install those rules with the shared installer and check them. On removal,
remove these local bindings and reinstall the local rules before removing the skill.
Do not edit installed blocks directly. Local bindings are instance-owned, not core.

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| maintenance entry | `.agents/skills/maintain/SKILL.md` | maintain |
| declaration and dependency checker | `.agents/scripts/gw/mechanisms.py` | mechanism-shape |
| installed-rule checker and installer | `.agents/scripts/gw/inject_rules.py` | mechanism-shape |
| local-rule convention | `.agents/skills/mechanism/SKILL.md` | mechanism-shape |

## What it produces, and who reads it

The maintenance report gives the operator evidence and dispositions per boundary.
Updated factual records and derived summaries are read by coordinating and project
agents. Addressed issues are read by the responsible project agent and its operator.
These use the existing project records and issue format supplied through context;
this mechanism creates no independent record kind or register.

## Not yet at the shape

No independent validator can prove semantic compatibility from prose. Source checks,
project evidence and explicit uncertainty bound the conclusions of each pass.

## What retires this

Retire it when cross-project boundary reconciliation ceases to be a responsibility
of the coordinating project or another accepted mechanism assumes the whole pass.

## What would show it working, graded by someone who did not build it

The operator reviews a preview containing an unchanged boundary, documentation drift,
a project-action deviation, an unimplemented target and missing evidence. It must
preserve accepted promises, avoid duplicate issues, emit an unambiguous summary and
avoid claiming implementation or deployment without evidence. The shared checkers
must reject a missing instruction file or a drifted installed invocation block.
