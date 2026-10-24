# Illustrated portfolio — four project stories

Prepared October 23, 2026. Review draft; not published.

These are project-level STAR narratives. Exact human/agent contribution must be confirmed before converting Action sections to first person. Results distinguish source, tests, deployment, and observed behavior.

---

# WAMIF

Making family history explorable

**Card:** Turn genealogy records into individual life routes and a shared chronology, with uncertainty kept visible.

**Skills:** React, TypeScript, Domain modeling, Data visualization

**Status:** Live application · private source

## Situation

Genealogy files describe people, family relationships, dates, and places in separate records. Understanding how lives unfold across geography requires assembling those records while keeping incomplete dates and unresolved places visible.

## Task

Provide an explorable view of an individual life and a recorded ancestor-to-descendant lineage, without presenting uncertain dates as exact occurrences or relationship links as geographic travel.

## Action

The React/TypeScript application separates GEDCOM parsing, normalization, place resolution, relationship queries, chronology, and rendering. Individual routes retain their own events. Lineage uses a recorded direct relationship path and shared calendar boundaries while keeping each person’s route independent. Event detail explains date and location interpretation; local SVG works without an external map provider.

## Result

The live sample was opened on October 23, 2026. Individual event stepping, selected-event details, and a four-person lineage workspace were observed and captured. The October 22 evidence audit separately links the deployed master revision to successful CI. This demonstrates an inspectable application; it does not establish genealogy accuracy, adoption, or configured Mapbox behavior.

## Feature stories

### One life, many records

Problem: dates and places are scattered through GEDCOM records. Approach: normalize life events, retain place-resolution provenance, and build a chronological route. Result observed: stepping the sample changed the active event, route, and story panel. Unknown-date records remained inspectable.

### Several generations, one calendar

Problem: a relationship chain is easy to misread as one continuous trip. Approach: derive recorded parent-child paths, retain per-person routes, and reveal them on shared chronology boundaries. Result observed: the sample opened four people with three recorded handoffs. Relationships remain untimed context.

### Uncertainty and visual overlap

Problem: approximate dates and nearby markers can imply more certainty than the records support. Approach: explain intervals and location provenance, distinguish collision disclosures from shared geography, and keep inspection separate from playback. The newer lineage spiderfy PR was separate from the audited production revision; it is not advertised here as released.

## Media

- [Individual Life Route](assets/screenshots/portfolio-wamif-route.jpg): Live synthetic sample: route diagram, current event, and chronological event rail.
- [Explain the selected event](assets/screenshots/portfolio-wamif-detail.jpg): Live synthetic sample: stepping to a marriage and opening its event/provenance detail.
- [Independent routes on shared chronology](assets/screenshots/portfolio-wamif-lineage.jpg): Live synthetic sample: an opened four-person lineage after stepping calendar boundaries. This is the SVG renderer, not a geographic basemap.

## Links

- [Public demo](https://wamif-rebuild.netlify.app/)

## Evidence and limits

ProofTree PRJ-0003, EV-0007–EV-0010; architecture and domain source at 612a76432a8014c8d228ee1c0fca28ccdedd5010; live browser observations 2026-10-23.

Screenshots use the application’s bundled content labeled synthetic. Source is private. No private repository images or family uploads are included. External geocoding and Mapbox/globe configuration were not exercised.

**Contribution:** Confirm exact human and AI roles before first-person publication. No personal claim is approved by this draft.


---

# Dashboarda

Keeping repeated research usable

**Card:** Purpose-built dashboards retain stable records and run history; the SignalDesk extension connects research to an Airtable workflow.

**Skills:** TypeScript, Serverless APIs, Data synchronization, Integration design

**Status:** Public source · live dashboard requires PIN

## Situation

Repeated research produces overlapping items, while follow-up decisions need durable records. Copying the same information between a dashboard and a work tracker can create duplicates or overwrite human-owned notes and task state.

## Task

Keep small dashboards independently deployable and make repeated imports reconcile stable identities. For the SignalDesk extension, synchronize research fields while preserving Airtable-owned qualification and activity state.

## Action

Dashboarda’s state handlers use Netlify Functions and Blobs, stable item keys, first/last-seen metadata, and bounded run history. The SignalDesk feature branch reuses persisted identities, maps allowlisted research fields, compares destination records, skips unchanged items, and applies bounded retries. Research synchronization and native Airtable task automation have separate responsibilities.

## Result

The reviewed source and public SignalDesk PR provide concrete implementation evidence. The October 22 audit records successful feature CI and a ready deployment with a registered cron. The October 23 live page prompted for a PIN, so no private dashboard data was captured. An independently observed unattended synchronization run remains an evidence gap.

## Feature stories

### Stable records across repeated updates

The state handler chooses a stable identity and retains firstSeenAt, lastSeenAt, and seenCount. This gives repeated observations a durable record instead of an append-only pile of copies.

### SignalDesk: separate research from follow-up

Research fields belong to the synchronizer; qualification, notes, and activity lifecycle belong to Airtable. The branch uses destination diffing and upserts. The public PR is a feature-specific receipt, not evidence that every dashboard is continuously operating.

## Media

- [SignalDesk change under review](assets/screenshots/portfolio-dashboarda-pr.jpg): Public draft PR #2. Its body contains project-reported receipts; the screenshot does not independently reproduce those runs.
- [Durable state and stable identity](assets/screenshots/portfolio-dashboarda-state.jpg): Public state-handler source; source evidence rather than a runtime screenshot.
- [Small apps, one repository](assets/screenshots/portfolio-dashboarda-repository.jpg): Public repository showing the independently deployable dashboard apps.

## Links

- [Public repository](https://github.com/jtwray/dashboarda)
- [SignalDesk PR #2](https://github.com/jtwray/dashboarda/pull/2)
- [Pinned state handler](https://github.com/jtwray/dashboarda/blob/56a0b1b0aa7d2e571696e74f7f31a6568680aa67/apps/local-prospects/netlify/functions/state.mts)
- [SignalDesk source](https://github.com/jtwray/dashboarda/blob/ad436cf3d4cec4ced7e14ef465235416cf39454e/apps/local-prospects/signaldesk/sync.ts)

## Evidence and limits

ProofTree PRJ-0001, EV-0001–EV-0004 and EV-0017; Dashboarda main 56a0b1b0aa7d2e571696e74f7f31a6568680aa67; SignalDesk head ad436cf3d4cec4ced7e14ef465235416cf39454e. Live PIN gate observed 2026-10-23.

The live dashboard is PIN gated and is not a suitable anonymous portfolio demo. Public repository/PR images are documentation and source evidence. Scheduled deployment is distinct from observed scheduled execution.

**Contribution:** Confirm exact human and AI roles before first-person publication. No personal claim is approved by this draft.


---

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


---

# Potty Weekend

A little less to remember

**Card:** A calm practice-day aid combines reminders, fast attempt logging, and history stored in the same browser.

**Skills:** Browser UX, IndexedDB, Storage boundaries, Domain logic

**Status:** Live application · public source

## Situation

A parent supporting a practice day has to notice cues, remember check-ins, and recall recent attempts. The tool needs to support that activity without turning the child’s progress into a performance target.

## Task

Make reminders and quick logging available in one simple interface, with persistent local history and clear limits around device storage, notifications, and observational estimates.

## Action

The single-page application combines a foreground reminder, fast attempt entry, calm feedback, and a history view. A storage port separates the UI from an IndexedDB adapter. Stable IDs and schema versions leave a migration seam; optional photos are stored separately from record metadata. The current scope keeps logs on one browser/device and does not ship parent sharing or cloud backup.

## Result

The live reminder, entry, and empty-history views were observed and captured on October 23, 2026, without creating child records. The reviewed source contains the persistence boundary and domain logic, and the October 22 audit records a ready static deployment. Real-device persistence, camera behavior, and a full practice day remain separate checks; no training outcome is claimed.

## Feature stories

### Small product, substantive engineering

A narrow purpose still creates meaningful design decisions: a persisted absolute reminder deadline, an injectable storage interface, atomic photo/record operations, and clear local-data boundaries. These are better explained as one short engineering section than several nested case studies.

## Media

- [Start with a calm reminder](assets/screenshots/portfolio-potty-overview.jpg): Live empty-session reminder view; no child data.
- [Fast attempt entry](assets/screenshots/portfolio-potty-entry.jpg): Live empty-session interface while exploring an outcome option; no attempt was saved.
- [History and data boundaries](assets/screenshots/portfolio-potty-history.jpg): Live empty-session summary/log, including the local-storage and export explanation.

## Links

- [Live application](https://potty-weekend.netlify.app/)
- [Public repository](https://github.com/jtwray/potty-weekend)
- [Pinned storage interface](https://github.com/jtwray/potty-weekend/blob/63495ae2796ef04fdd2e2aa55f4e39ae62a723e5/public/storage.js)

## Evidence and limits

ProofTree PRJ-0004, EV-0011–EV-0013; source 63495ae2796ef04fdd2e2aa55f4e39ae62a723e5; live browser observations 2026-10-23.

All captures show an empty browser session; no real child records or bowl photos are included. Logs are local to the browser, device, and origin. No cloud sync, reliable closed-tab alerts, or promised training result.

**Contribution:** Confirm exact human and AI roles before first-person publication. No personal claim is approved by this draft.
