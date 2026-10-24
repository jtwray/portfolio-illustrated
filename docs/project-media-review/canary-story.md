# Agent Toolchain Canary

Finding the failing layer

**Card:** Read-only toolchain probes turn environment and access failures into redacted, classified diagnostic reports.

**Skills:** Node.js, Developer tooling, Failure classification, Safe scheduling design

**Status:** Public CLI · source inspected

## Situation

An agent workflow may fail because a runtime is missing, repository access is unavailable, or an endpoint cannot be reached. Repeating checks manually makes it harder to distinguish a new fault from a recurring one and risks copying sensitive diagnostic output.

## Task

Provide a repeatable diagnostic utility that checks specific layers, redacts reports, compares outcomes across runs, and keeps durable operational guidance under human review.

## Action

The Node CLI defines runtime, Git, GitHub API, HTTPS, and loopback probes. An allowlist constrains subprocess commands. Report persistence applies redaction, run locking prevents overlap, and previous-state comparison classifies new, repeated, recovered, and retirement-candidate outcomes. Scheduler adapters describe Windows, macOS, and Linux execution paths without conflating an ordinary Node process with connected agent plugins.

## Result

The public implementation and scheduling documentation are inspectable at a pinned revision, with test definitions in the repository. This package captures the repository, scheduling contract, and classification source. No fresh test run, installed schedule, unattended run, or measured reduction in troubleshooting time is claimed.

## Feature stories

### A useful boundary around automation

The tool checks what an ordinary local process can observe. Connected plugin identity and agent browser behavior remain explicit manual or agent-assisted checks. This makes its diagnostic scope understandable.

### Incident memory, with human review

A repeated matching failure is different from a first failure; recovery is different from durable resolution. Classification informs review, while people decide changes to operational guidance.

## Media

- [The diagnostic contract](assets/screenshots/portfolio-canary-overview.jpg): Public README explaining scope, setup, and redacted local reports.
- [Scheduling boundaries](assets/screenshots/portfolio-canary-scheduling.jpg): Public scheduling documentation distinguishing planning from explicit installation/removal.
- [Classification and persistence](assets/screenshots/portfolio-canary-classification.jpg): Public state.js source. The repository is compact/minified; use the diagram as the primary visual and this capture as a secondary receipt.

## Links

- [Public repository](https://github.com/jtwray/agent-toolchain-canary)
- [Pinned probes](https://github.com/jtwray/agent-toolchain-canary/blob/ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa/src/probes.js)
- [Pinned classification](https://github.com/jtwray/agent-toolchain-canary/blob/ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa/src/state.js)
- [Pinned safety](https://github.com/jtwray/agent-toolchain-canary/blob/ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa/src/safety.js)

## Evidence and limits

ProofTree PRJ-0002, EV-0005–EV-0006 and Slice 1.4 EV-0019; source ed9703c7ead7c36ecf4b5554d56fa9cfc88501aa; public browser captures 2026-10-23.

This is a command-line utility, so no Netlify web-app link is applicable. Repository screenshots show source/documentation, not captured successful execution. Cross-platform operation still needs platform-specific receipts.

**Contribution:** Confirm exact human and AI roles before first-person publication. No personal claim is approved by this draft.
