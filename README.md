# Xuanxue Workshop

## For first-timers

Find your installation assignment:
[cabinet-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/1)
or [daychi-workshop-collaboration](https://github.com/dveyarangi/xuanxue-workshop/issues/2).
Read it and use the [/collaborate skill](skills/collaborate/SKILL.md).

## Purpose

Xuanxue Workshop is being developed as a shared workspace for contributors to
the school's software projects. Its purpose is to make responsibilities,
agreements, and ongoing work clear when people and their coding agents work
across several projects.

The planned workspace will help contributors:

- Find the owner of a capability and understand which projects depend on it.
- Join a project using shared onboarding instructions and accepted agreements.
- Coordinate tasks, decisions, and handoffs, including parallel work.
- Track changes to shared contracts, their adoption, and verification.

The [first stage](docs/stage-1.md) prepares the initial migration and connects
the project agents to Workshop under their own operators. It ends with confirmed
agent integration and a working return path for results and problems. The broader
purpose and intended capabilities are described in [PRODUCT.md](PRODUCT.md).

## Repository map

The school's projects have separate repositories and responsible operators;
contributors do not need to share a local checkout:

| Repository | Who it serves | Product scope |
|---|---|---|
| [daychi](https://github.com/sleontenko/daychi) | Students and readers of the school's learning materials | Practice app with schedules, selected classes, reminders, and personal access to materials and Zoom; web wiki with search, reading, recent publications, and a relationship graph. |
| [xuanxue-cabinet](https://github.com/gregoryKot/xuanxue-cabinet) | Teachers, administrators, and students | School cabinet with schedules, automatic delivery of class links and recordings, payments, materials, and exams; available as an installable web app. |
| [xuanxue-workshop](https://github.com/dveyarangi/xuanxue-workshop) (this repository) | Contributors and their coding agents | Planned coordination workspace for responsibilities, onboarding, shared agreements, tasks, handoffs, and adoption of changes across projects. |

Daychi and Xuanxue Cabinet both include schedules and learning materials.
Workshop's goals include making the ownership and agreements around such
shared capabilities explicit.
