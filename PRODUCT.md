# Xuanxue Workshop

## Purpose

Enable developers and their coding agents to work across the school's software projects while preserving clear responsibilities, compatible interfaces, and coordinated changes.

## Goals

These are intended product capabilities. The accepted [first-stage goal](docs/stage-1.md)
defines which outcomes are required for initial migration and agent integration;
it does not commit the first stage to implementing every capability below.

### 1. Define responsibility boundaries

For every shared capability, identify its providing project, consumers, data owner, and accountable person. Specify who approves changes, releases them, and handles failures. Allow contributors to work across projects without transferring ownership implicitly.

### 2. Provide one onboarding process

Give new contributors and agents one entry point that connects their local working environment to the shared rules, contracts, and work board. Verify that the setup works and record the instruction version adopted. Support repeating onboarding when requirements change.

### 3. Maintain authoritative contracts

Define the interfaces and behavior that projects promise each other: authentication, permissions, data formats, identifiers, time handling, errors, and supported client versions. Record proposed changes separately from accepted contracts and deployed capabilities.

### 4. Publish changes and track adoption

Version shared instructions and agreements. For each published change, identify affected projects, required actions, and when adoption is required. Tell agents when they must reread instructions or repeat onboarding. Show which projects have adopted an update and which remain outstanding.

### 5. Coordinate work and communication

Provide a shared board for tasks, questions, decisions, and handoffs. Each task identifies its responsible contributor, affected projects, dependencies, status, and completion evidence. A new agent session must be able to discover ongoing work and continue from the recorded state.

### 6. Support safe parallel work

Let contributors reserve the scope of a change before editing. Detect overlapping reservations across files, contracts, and affected behavior. Support renewal, release, expiry, and explicit takeover so abandoned work does not block progress indefinitely.

### 7. Define shared operational standards

Set requirements for logs, error reporting, service health, release identification, and alerts. Make failures traceable across project boundaries. For each service, record the monitoring that is enabled, its last verification, and the person responsible for responding.

### 8. Verify shared obligations

Associate each enforceable requirement with a check and each judgment requiring review with an accountable reviewer. Reject releases that fail required compatibility checks. Track exceptions with an owner, reason, and expiry. Keep ownership, contracts, and operational records updated as part of completing the changes that affect them.
