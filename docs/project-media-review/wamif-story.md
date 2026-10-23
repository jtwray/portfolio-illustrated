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
