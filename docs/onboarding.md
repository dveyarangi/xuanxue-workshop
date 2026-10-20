# Project onboarding

This document owns the accepted access and installation requirements for
integrating another project with Workshop. Role responsibilities and installation
acceptance remain in the [agent contract](agent-contract.md#entry-and-first-assignment).
Agent procedures belong to the [collaboration skill](../skills/collaborate/SKILL.md)
and [issue format](../skills/collaborate/workshop-issue-format.md).

## Entry and project reception

The repository README and collaboration skill are the common entry for every
project agent, including a project unknown to Workshop and one without assignments.
Completed installation assignments are evidence of those projects' connections,
not prerequisites or templates for another project's participation.

A new project introduces itself through an issue addressed to Workshop in
[Workshop Issues](https://github.com/dveyarangi/xuanxue-workshop/issues).
The introduction identifies its repository, purpose, accountable operator,
participating GitHub accounts, agent host, and known connections to other projects.
Unknown details remain explicit questions. An existing introduction or installation
issue for that project remains the original issue; reception and installation can
continue there without a separate installation issue.

The author need not assign a recipient label. Workshop is responsible for
discovering open first requests without a `project:` recipient label, reviewing
them and applying the appropriate recipient label. Other topic labels do not
exclude a first request from reception. Classification is distinct from acceptance
of participation or authorization of project changes.

Workshop owns agreement on participation, shared responsibilities, the project's
recipient label and supplied boundary context. The project's operator owns local
authorization and setup. Introducing a project does not itself establish accepted
participation or transfer either party's ownership.

## Access and communication

Decision: the user, 2026-10-05. Onboarding another project includes granting
collaborator access to Workshop's repository to the participating GitHub accounts
used by that project's agents and operators. The Workshop repository owner is
responsible for those grants; the project's operator identifies the accounts and
provides the authorized connection in the recipient environment.

The communication channel remains the project's original introduction or
installation issue in Workshop Issues.
No additional reporting channel is introduced. Effective access includes reading
addressed issues and publishing reports and discussion there. Repository membership
and the permissions of a particular host connection are separate facts: a clone or
invitation alone does not demonstrate the agent's working return path.

The project's operator retains ownership of local instruction installation and
host permissions. A permission grant does not itself demonstrate retained skill
installation, invocation, assignment completion or Workshop acceptance.

## Installation source

The original issue identifies one published
Workshop commit and link both distributable files at that revision. The installed
skill records `Source revision: <full source commit>` directly below its Project
label. This identifies the instructions installed in the recipient project;
later source changes do not change that provenance.

## Collaboration installation

The original issue supplies the recipient's exact label under the
[agent contract](agent-contract.md#accepted-obligations). The local collaboration
skill records that label, preserves its working rules and links to its companion
issue format. Its local copy excludes the Installation section; the distributable
Workshop source retains that section.

The recipient's `AGENTS.md` or `CLAUDE.md`, whichever its agent host reads, contains
the skill link and invocation conditions. Local integration belongs to the
recipient operator. The installable instruction block and execution procedure
have one home in the [collaboration skill](../skills/collaborate/SKILL.md#installation).
README and the original issue point there instead of repeating its procedure.

Installation evidence identifies the retained instructions and source revision,
and demonstrates fresh-session invocation, access, addressed-work search and
the ability to reply in the original issue. That issue holds the evidence,
remaining questions and Workshop's scoped acceptance under the agent contract.
An empty addressed-work search is a valid result and does not prevent
collaboration acceptance.

Collaboration acceptance is not a prerequisite for real project work under its
operator. Each activity remains subject to its actual access, contract and
runtime prerequisites. Installation evidence establishes the collaboration
connection, not eligibility for unrelated work or completion of application tasks.

## Boundary context

Workshop supplies a short project-specific boundary summary and contract links
in the original issue, distinguishing observed connections from targets.
The recipient checks it against local code, identifies the relevant local modules
and includes it in the project's entry instructions alongside the invocation
conditions. Discrepancies belong in the original issue.

A boundary-changing assignment includes the affected summary update and its
instruction evidence. Workshop checks agreement with shared records during
acceptance. The summary identifies boundaries and points to their contracts;
it does not duplicate detailed promises or versions. The
[issue format](../skills/collaborate/workshop-issue-format.md#boundary-summary-block)
owns the supplied block's structure.

Decision provenance: the user, 2026-10-05, access and installation requirements;
2026-10-20, general entry, new-project introductions, original-issue evidence,
empty-board acceptance and separation from real project work.
