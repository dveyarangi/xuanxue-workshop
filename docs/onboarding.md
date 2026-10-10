# Project onboarding

This document owns the accepted access and installation requirements for
integrating another project with Workshop. Role responsibilities and installation
acceptance remain in the [agent contract](agent-contract.md#entry-and-first-assignment).
Agent procedures belong to the [collaboration skill](../skills/collaborate/SKILL.md)
and [issue format](../skills/collaborate/workshop-issue-format.md).

## Access and communication

Decision: the user, 2026-10-05. Onboarding another project includes granting
collaborator access to Workshop's repository to the participating GitHub accounts
used by that project's agents and operators. The Workshop repository owner is
responsible for those grants; the project's operator identifies the accounts and
provides the authorized connection in the recipient environment.

The communication channel remains the original assignment in Workshop Issues.
No additional reporting channel is introduced. Effective access includes reading
addressed issues and publishing reports and discussion there. Repository membership
and the permissions of a particular host connection are separate facts: a clone or
invitation alone does not demonstrate the agent's working return path.

The project's operator retains ownership of local instruction installation and
host permissions. A permission grant does not itself demonstrate retained skill
installation, invocation, assignment completion or Workshop acceptance.

## Installation source

Decision: the user, 2026-10-05. Installation assignments identify one published
Workshop commit and link both distributable files at that revision. The installed
skill records `Source revision: <full source commit>` directly below its Project
label. This identifies the instructions installed in the recipient project;
later source changes do not change that provenance.

## Collaboration installation

The installation assignment supplies the recipient's exact label from the
[agent contract](agent-contract.md#accepted-obligations). The local collaboration
skill records that label, preserves its working rules and links to its companion
issue format. Its local copy excludes the Installation section; the distributable
Workshop source retains that section.

The recipient's `AGENTS.md` or `CLAUDE.md`, whichever its agent host reads, contains
the skill link and invocation conditions. Local integration belongs to the
recipient operator. The installable instruction block and execution procedure
have one home in the [collaboration skill](../skills/collaborate/SKILL.md#installation).
README and installation issues point there instead of repeating its procedure.

Installation evidence identifies the retained instructions and source revision,
and demonstrates invocation, access and discovery. The original installation
issue holds that evidence and Workshop's acceptance under the agent contract.

## Boundary context

Workshop supplies a short project-specific boundary summary and contract links
in the installation assignment, distinguishing observed connections from targets.
The recipient checks it against local code, identifies the relevant local modules
and includes it in the project's entry instructions alongside the invocation
conditions. Discrepancies belong in the original assignment.

A boundary-changing assignment includes the affected summary update and its
instruction evidence. Workshop checks agreement with shared records during
acceptance. The summary identifies boundaries and points to their contracts;
it does not duplicate detailed promises or versions. The
[issue format](../skills/collaborate/workshop-issue-format.md#boundary-summary-block)
owns the supplied block's structure.
