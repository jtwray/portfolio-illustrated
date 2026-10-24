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
