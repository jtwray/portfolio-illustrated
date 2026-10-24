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
