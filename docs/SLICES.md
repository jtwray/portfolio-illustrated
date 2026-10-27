# Illustrated Portfolio — Slices

_Last reviewed: 2026-10-27 (contact delivery and tools planning update)_

## Slice operating rules

- One small, testable vertical slice at a time. Planning a slice does **not** authorize implementation, merges, production cutover, private-repository exposure, or changing DNS.
- Keep the site usable at the end of every slice. Verify a relevant deploy, preferably from an isolated branch/PR for implementation changes.
- Product-specific roadmaps remain in their own repositories. These slice IDs are **ILL-xx** to avoid collisions with WAMIF, Dashboarda, or other project numbering.
- A missing evidence source is a **blocked/unknown** state, not proof that a feature or asset has been completed.

## ILL-00 — Illustrated site foundation [Complete]

**Outcome:** Independently deployed site with original artwork, responsive HTML/CSS/JS, custom `illustrated.tuckerwray.com` HTTPS domain, corrected "Tucker Wray" wordmark, branded form confirmation page, and registered Netlify `reachout` form.

**Verified:** Netlify returned a ready deploy from `main`; form detection was enabled, the `reachout` fields and honeypot were registered; the user verified the branded site/old apex separation and HTTPS. **Update 2026-10-27:** Tucker has since confirmed manual submission capture and inbox notification; see the dated ILL-01 record below.

No further implementation is implied.

## ILL-01 - Contact intake acceptance test [Owner-confirmed delivery, 2026-10-27]

**Owner confirmation (reported 2026-10-27):** the manual test is visible in the
intended email inbox and Netlify Forms. The earlier automated test was found in
the Spam tab. This closes the capture/inbox-delivery blocker. See the
[dated evidence record](records/contact-intake-2026-10-27.md).
No new production submission or independent inbox inspection was performed.
The protocol below is retained for future regression checks; confirmation-page
and reply-to behavior were not separately reported in this confirmation.

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

## ILL-TOOLS-00 through ILL-TOOLS-03 - Try my tools

The [tools plan](TRY_MY_TOOLS.md#delivery-sequence-and-acceptance) contains the
catalogue, page structure, per-tool readiness, boundaries, and acceptance criteria.

- **ILL-TOOLS-00:** preserve the plan and owner-confirmed contact evidence in a main-based draft PR.
- **ILL-TOOLS-01:** implemented and locally verified; owner review pending. Static /tools/ catalogue, isolated inquiry-board sample, and existing-form inquiry handoff. See the [review record](records/tools-page-2026-10-27.md).
- **ILL-TOOLS-02:** proposed verified email trial; settle provider, budget, retention, and enforceable controls before live sends.
- **ILL-TOOLS-03:** proposed additional tools, each with its own product-specific checks.

ILL-TOOLS-00 was the documentation checkpoint. The branch now also contains
ILL-TOOLS-01; merging will publish the catalogue and fictional sample through the
existing main deployment. Live sending remains ILL-TOOLS-02. These IDs avoid
collisions with other open portfolio branches. Production product implementation
stays with each product repository; the portfolio owns its catalogue and sample.
