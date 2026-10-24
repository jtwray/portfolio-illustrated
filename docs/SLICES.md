# Illustrated Portfolio — Slices

_Last reviewed: 2026-10-19_

## Slice operating rules

- One small, testable vertical slice at a time. Planning a slice does **not** authorize implementation, merges, production cutover, private-repository exposure, or changing DNS.
- Keep the site usable at the end of every slice. Verify a relevant deploy, preferably from an isolated branch/PR for implementation changes.
- Product-specific roadmaps remain in their own repositories. These slice IDs are **ILL-xx** to avoid collisions with WAMIF, Dashboarda, or other project numbering.
- A missing evidence source is a **blocked/unknown** state, not proof that a feature or asset has been completed.

## ILL-00 — Illustrated site foundation [Complete]

**Outcome:** Independently deployed site with original artwork, responsive HTML/CSS/JS, custom `illustrated.tuckerwray.com` HTTPS domain, corrected "Tucker Wray" wordmark, branded form confirmation page, and registered Netlify `reachout` form.

**Verified:** Netlify returned a ready deploy from `main`; form detection was enabled, the `reachout` fields and honeypot were registered; the user verified the branded site/old apex separation and HTTPS. **Not verified:** full form submission and inbox delivery.

No further implementation is implied.

## ILL-01 — Contact intake acceptance test [Next / Awaiting end-to-end proof]

**Goal:** Prove a genuine visitor inquiry reaches the owner, not just that the form markup is detected.

**In scope**
1. Check the `reachout` form notification is configured for the chosen inbox (`james@tuckerwray.com` if confirmed) through Netlify's submission notifications settings.
2. Submit one ordinary non-spam browser inquiry via the live illustrated URL; verify the confirmation page.
3. Verify the exact inquiry appears under Netlify Forms (or resolve a spam classification).
4. Confirm the notification email reaches the chosen inbox, including reply-to behavior.
5. Record test date/result; resolve only observed defects.

**Done when:** live submission + captured record + recipient delivery verified, without affecting the old portfolio or mail DNS.

**Explicitly out of scope:** webhook/n8n, automatic responses, CRM writes, lead scoring, unattended outreach.

## ILL-02 — Curated proof inventory checkpoint [Started / Minimal proof packet pending]

**Status confirmed 2026-10-19:** Tucker reports the ProofTree/Engineering Skills Registry was **just started**. Its public [repository](https://github.com/jtwray/prooftree) exists but has no committed files as of this check. The full registry is **not a prerequisite** for resolving the illustrated portfolio WAMIF links.

**In scope**
1. Identify publicly shareable, **verified** project claims and source references for the projects on this illustrated portfolio, prioritizing WAMIF.
2. Record the minimal WAMIF proof packet: problem, own contribution, implementation, screenshots/demo, test/deploy evidence, limitations, and public-safe link.
3. Mark uncertain/missing proof as unverified; propose the smallest missing piece rather than inventing supporting evidence.

**Near-term WAMIF packet (independent of full ProofTree):** identify the canonical WAMIF Rebuild source, document the problem and Tucker’s contribution, confirm architecture/stack from code, reference tests and deployment evidence, select a privacy-safe screenshot/demo or public case study, and label all gaps explicitly. Never claim evidence that was not reviewed.

**Done when:** this *minimal* WAMIF proof packet and public-safe destination choices are documented, making ILL-03 actionable; a complete ProofTree product is not required.

**Out of scope:** building a new proof registry app, generating unverified testimonials, exposing private artifacts.

## ILL-03 — WAMIF destination and copy correction [Blocked / Issue #1]

**Dependency:** ILL-02 enough to support an accurate public-facing project claim.

**In scope**
1. Verify present links and actual WAMIF Rebuild technology, including the portfolio's current `Next.js` tag against React/Vite source.
2. Pick an approved destination that an anonymous visitor can open (live demo, public-safe case study, or separately approved public repo).
3. Update WAMIF image and title links together; update technology, maturity, and claims as needed.
4. Test the target logged out and both click targets on desktop/mobile.

**Done when:** both WAMIF CTAs reach the intended accessible proof, text matches verified evidence, and other cards still work.

**Do not:** make `jtwray/wamif-rebuild` public by default, leak private GEDCOM/data or secrets, or alter WAMIF application code.

## ILL-04 — Evidence-backed portfolio QA [Proposed; not approved for execution]

**In scope:** verify featured project links and status labels, responsive/navigation/accessibility checks, email and contact paths, canonical host and optional metadata/SEO hygiene; fix only demonstrated defects.

**Done when:** a small recorded QA checklist demonstrates no broken outbound links, misleading claims, or contact regressions.

**Out of scope:** portfolio overhaul, a second framework migration, new sales pipelines, n8n workflows, RAG/avatars.

---

**Backlog separation:** Airtable/SignalDesk is its own already-scoped integration effort; n8n belongs in a later Toolbelt Growth slice; RAG/voice/video-avatar explorations follow a clearly justified use case, not this portfolio launch.

## October 23 media slice contracts

Status for ILL-05–08: **planned, not dispatched**. Read
[PROJECT_BRAIN.md](PROJECT_BRAIN.md) for current queue, base-branch preflight,
temporary-agent prompts and acceptance workflow. The original package and baseline
manifest remain unchanged. Revisions go under `docs/project-media-updates/`.

### ILL-05 — Dashboarda screenshots

**Goal:** Show what Dashboarda actually looks like while keeping each published
capture appropriate for public portfolio use.

**Inputs:** The preserved Dashboarda story, evidence ledger, current app and
[media checkpoint](PROJECT_MEDIA_REVIEW.md).

**In scope / allowed changes:** New Dashboarda captures and a capture ledger under
`docs/project-media-updates/`; relevant planning/status documentation. Capture the
empty PIN prompt and at least one useful dashboard view. Prefer reviewed real public
rows; clearly label demonstration data if needed. Use an isolated session or fixture
instead of altering production records. Inspect full-size images for private records,
annotations, PINs and credentials.

**Done when:** Both captures are legible; each records source, date, environment,
live-versus-demonstration status and alt text/caption; an independent reviewer checks
the pixels and privacy treatment. If authorized access is unavailable, report the
specific blocker rather than inventing a live view.

**Out of scope:** App features, auth changes, exposing credentials, changes to
production data, Canary status panel or portfolio navigation.

### ILL-06 — Import approved Canary media

**Goal:** Incorporate authentic Canary CLI evidence produced and independently
reviewed by the Canary project.

**Dependency:** CAN-01 from the Canary project's
[own roadmap / draft PR #1](https://github.com/jtwray/agent-toolchain-canary/pull/1).
The Canary brain assigns execution/capture work and reviews it there. This portfolio
slice may request the export but must not run probes or assign product work.

**In scope / allowed changes:** Import approved public-safe images and neutral
caption/alt-text manifest under `docs/project-media-updates/`; update relevant
planning/status documentation. Check provenance: exact source revision, command,
date, environment class, observed outcome and any demonstration label. Keep local
Canary reports/config/state/logs and machine/account details out of this repo.

**Done when:** Imported images are legible and public-safe; captions match the
Canary-approved evidence; the originating commit/review and export are linked.
Unobserved outcomes remain explicit. If CAN-01 is pending, mark the dependency
blocked instead of recreating its work in this project.

**Out of scope:** CLI runs, Canary code/credential/schedule changes, status UI,
Check now, re-authentication, and inventing terminal results.

### ILL-07 — Revised four-project media and STAR review

**Goal:** Produce one reviewable editorial package using the accepted capture work.

**Inputs:** ILL-05/06 outputs; preserved WAMIF, Dashboarda, Canary and Potty Weekend
stories, diagrams, evidence ledger, QA and integration proposal.

**In scope / allowed changes:** Revised review page, captions, asset references,
stories, claim/evidence ledger and verification notes under
`docs/project-media-updates/`; planning status updates. Reuse the original material
where it remains accurate. Keep source evidence, observed execution, deployment and
user-reported contribution distinct. Confirm contribution wording with Tucker where
the evidence does not establish the human/agent split.

**Done when:** All four projects can be reviewed together; relevant real captures
appear with accurate captions; links/assets resolve; the review page is inspected in
a browser at desktop and 360px; limitations remain adjacent to the affected claim.
Tucker accepts the stories and wording before site integration. Unknowns stay explicit.

**Out of scope:** New projects, new product features, changing application code in
the featured repos, live portfolio navigation, domain migration or deployment.

### ILL-08 — Illustrated case-study integration

**Goal:** Turn the accepted review material into accessible portfolio case studies.

**Dependencies:** ILL-07 acceptance; current main/open PR/resume-change reconciliation;
an explicit base branch and approved integration scope. Follow
[the preserved integration proposal](project-media-review/INTEGRATION.md).

**In scope / allowed changes:** Illustrated portfolio HTML/CSS/JS, case-study pages
and approved media assets, plus verification/planning documentation. Four project
cards lead to shareable case-study destinations with useful return navigation,
supported skills/status, captions, alt text, and accessible full-size media.
Keep unrelated work/history available.

**Done when:** All four card destinations work; WAMIF is reachable without exposing
private source/data; Dashboarda is accurately identified as gated; Canary is described
as a CLI; Potty Weekend claims match its browser-local behavior. Keyboard/mobile
behavior and existing contact/resume paths work on a branch preview. Record exact
commit, preview and observed checks for independent review.

**Out of scope:** Primary-domain cutover, DNS/email changes, resume-generation
features, building ProofTree/API capabilities or modifying the featured products.

**Next gate:** Reuse ILL-04 for release QA on the integrated commit. Record the
contact and resume checks and unresolved earlier gates; Tucker's acceptance and
merge/publication decision follow review.
