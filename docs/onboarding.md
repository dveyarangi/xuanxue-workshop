# Project onboarding

This document owns the accepted access and communication requirements for
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
