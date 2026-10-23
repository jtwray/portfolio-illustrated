# Portfolio change requests — draft PR #2

_Last reviewed: 2026-10-23. Source of truth for pre-approval scope review. This document **requests changes**, but does not represent implemented or verified features._

**PR:** https://github.com/jtwray/portfolio-illustrated/pull/2  
**Implementation policy:** one bounded slice at a time, commits only on a `feat/*` branch, followed by independent outcome review; no direct `main` changes or domain cutover.

## CR-001 — Feature Potty Weekend as a shipped product case study

![CR-001 Potty Weekend project-card concept — not implemented](visuals/cr-001-potty-weekend-card.svg)

[Scalable SVG](visuals/cr-001-potty-weekend-card.svg) · [Design asset index](visuals/README.md)

**Requested by:** portfolio owner, before approving PR #2.  
**Status:** Requested / specification prepared; **implementation not started**.  
**Proposed slice:** ILL-05 (portfolio only; do not modify Potty Weekend application).  
**Decision:** Add as a **fifth** portfolio project initially; do not displace an existing project without a separate, deliberate content decision.

### User story and value

As a technical hiring manager or potential client, I can recognize that the engineer identified a concrete family need and shipped a small, working, privacy-conscious web application rather than only building large infrastructure or describing concepts.

### Source and evidence

- Public live app: https://potty-weekend.netlify.app/
- Public repository: https://github.com/jtwray/potty-weekend
- Verification notes: https://github.com/jtwray/potty-weekend/blob/main/docs/VERIFICATION.md
- Technical README: https://github.com/jtwray/potty-weekend/blob/main/README.md
- Relevant implementation: `public/app.js`, `public/domain.js`, `public/storage.js`, and `tests/domain.test.js`.
- Source demonstrates a local-first app with injected IndexedDB storage adapter, event logging, adjustable timer, optional bowl photographs, and opt-in **experimental** interval suggestions. Public source includes automated unit tests and a published Netlify project.
- Limitations to disclose: device/origin-scoped records, no cloud sync, no guaranteed background alarms, and real phone/camera/parent-use checks not yet fully documented. Do not market heuristic suggestions as AI/ML, medical recommendations, or validated predictions.
- Some verification prose and test-count descriptions are older than the current source; ensure any quantitative claim matches the current branch before publication.

### Deliverables / scope

1. New project card titled **Potty Weekend**, category `product`, with a truthful status label (e.g. `Deployed · phone validation pending`).
2. A small `work/potty-weekend.html` case study: problem, key implementation decisions, privacy and storage boundaries, observable verification, known limitations, links to live app and source.
3. Reuse existing illustrated design, responsive card layout, project filters, and accessibility conventions; update the `All work` count from four to five.
4. Use existing verified non-sensitive visuals or a simple existing-style diagram. Do not publish any photos of a child, potty logs, or private family data.
5. Check project/source/demo links in a logged-out browser.

### Acceptance

- [ ] Card and case-study page work in desktop and phone-width preview; keyboard links and filtering are usable.
- [ ] Both live-app and source links open without account access.
- [ ] Case study explains IndexedDB/local-device privacy, timer limitations, experiments vs validated outcomes.
- [ ] No new claims of production outcomes, medical efficacy, ML/AI forecasting, or multi-device sync.
- [ ] Existing four project cards and contact journey still work.

### Out of scope

Potty Weekend feature development, marketing launch, app-store packaging, PWA/push, backend sync, real user tracking, testimonials, and a new portfolio redesign.

---

## CR-002 — Accessible résumé formats without losing the digital résumé link

![CR-002 résumé access wireframe — conceptual design, not implemented](visuals/cr-002-resume-access.svg)

[Scalable SVG](visuals/cr-002-resume-access.svg) · [Design asset index](visuals/README.md)


**Requested by:** portfolio owner, before approving PR #2.  
**Status:** Requested / specification prepared; **implementation not started**.  
**Proposed slice:** ILL-06A (public document access), with optional ILL-06B (email delivery) **deferred pending evidence and separate approval**.

### User story

As a recruiter or hiring manager, I can choose to browse a digital résumé on `w2.tuckerwray.com`, open a current PDF in a new tab, or download the same PDF. The link in the hamburger/navigation menu **must continue to route to the W2 digital portfolio**; it must not silently switch to a file.

### Recommended IA and MVP (ILL-06A)

1. Preserve the current main navigation **Résumé** link targeting `https://w2.tuckerwray.com/` on desktop and inside the mobile hamburger menu.
2. Add a clearly labeled **Résumé formats / Download résumé** area reachable on mobile and desktop (an inline, accessible menu adjunct or small résumé-access section; favor simplicity over nesting a difficult mobile submenu).
3. Provide exactly these actions when the final document has been supplied and verified:
   - **Digital résumé** — navigate to `https://w2.tuckerwray.com/` (existing behavior).
   - **View PDF** — open the hosted PDF URL in a new browser tab/window. Native PDF display is controlled by the visitor's browser; some browsers download rather than preview.
   - **Download PDF** — a reliably downloadable asset with a simple filename such as `Tucker-Wray-Software-Engineer-Resume.pdf`; validate actual browser behavior rather than assuming a cross-origin `download` attribute always forces saving.
4. PDF is the default share/preview format. Optional `.docx` download requires an actual current Word file and version parity; browser preview of Word is not guaranteed. Do not generate or serve unreviewed résumé claims.
5. The primary source résumé version, its date, its filename(s), and its update/ownership workflow must be confirmed before publishing. Do not assume a historical file is current.
6. Document basic accessibility (meaningful filenames and labels, keyboard actions, visible focus, PDF readability/text selection, appropriate document title) and verify assets load for logged-out visitors.

### Optional email flow (ILL-06B — later, **not a launch blocker**)

The requested interaction may show a validated email field and an action label that updates **as the visitor types**, e.g. `Email résumé to recruiter@example.com`. However:

- **MVP alternative:** a **Share by email** action launches an explicitly labeled, pre-composed `mailto:` draft with the public résumé PDF URL and digital résumé URL. The user reviews and sends from their own mail client; no claim of automatic delivery or attachment. This can be considered within ILL-06A only if it remains a tiny, reliable enhancement.
- **True automatic sending:** must be a separate approved ILL-06B with server-side transaction provider; restrict payload to one fixed public PDF/link, verify recipient input, apply abuse/rate controls and delivery limits, prevent open-relay behavior, avoid storing/leaking addresses, and make success/error/delivery semantics truthful. Dynamic button text should not imply delivery before confirmation.
- Do not automatically email entered third-party recipients, silently collect addresses, or claim delivery just because an HTTP request succeeded.

### Acceptance (ILL-06A)

- [ ] Existing W2 résumé link works as before in desktop and mobile hamburger navigation.
- [ ] Validated current résumé PDF opens in a separate tab where supported; downloadable PDF works; file has the approved current content.
- [ ] Labels distinguish digital website, PDF viewing, and downloading; responsive and keyboard-accessible controls.
- [ ] Logged-out visitor can access the file; no private API keys or résumé files with unintended personal/sensitive data.
- [ ] No automated email or backend dependency introduced.
- [ ] Optional share-by-email creates an editable draft only and accurately says so; otherwise omit entirely.

### Acceptance (ILL-06B — only after separate authorization)

- [ ] Recipient-specific dynamic CTA is understandable and accessibility-tested.
- [ ] Sending requires an explicit action and proper anti-abuse checks.
- [ ] Negative-path testing for invalid recipients, rate limiting, provider errors, duplicate requests, and privacy.
- [ ] No relay for arbitrary text, attachments, or bulk mail; clear delivery status and consent wording.

### Out of scope for current PR changes

Generating a résumé from incomplete evidence; automatic email delivery; CRM integrations; rewriting the W2 portfolio; third-party document-preview embedding; DNS/domain migration.

---

## CR-003 — ProofTree evidence-verified résumé tailoring from a job description

![CR-003 private JD-to-evidence-to-approved-résumé process — future design, not implemented](visuals/cr-003-prooftree-resume-flow.svg)

[Scalable SVG](visuals/cr-003-prooftree-resume-flow.svg) · [Editable Mermaid diagram and design notes](visuals/README.md#cr-003--ill-07--prooftree-résumé-tailoring)


**Requested by:** portfolio owner on 2026-10-23.  
**Status:** **Future backlog request only; not approved for execution and not required before PR #2 approval/cutover.**  
**Proposed slice:** ILL-07 (private, owner-operated capability; separate reviewed `feat/*` implementation when prerequisites are satisfied).  
**Dependency:** [ProofTree](https://github.com/jtwray/prooftree) must expose a reviewed, authenticated, read-only claim/evidence query contract. Its current documentation establishes a **private version-controlled record registry**, not an already verified live API. ProofTree owns its own API roadmap and claim-approval logic; this portfolio repository will integrate, not recreate or bypass them.

### User story and outcome

As the portfolio owner/job applicant, I can upload or paste a job description (JD), compare its actual must-have and nice-to-have requirements with my current documented competencies, review a **claim-by-claim evidence trace**, and produce a compelling role-specific résumé grounded in the strongest accurate and verifiable evidence available at generation time.

The optimizer seeks the **best truthful alignment**, not a maximal keyword match or a fabricated fit score. Unsupported JD requirements are explicitly exposed as gaps rather than invented as experience.

### Evidence scope and attribution

- **Professional history:** employer, role, dates, responsibilities and results from approved ProofTree `EXP-*` and `CL-*` records; distinguish personally reported employment history from independently corroborated duties.
- **Engineering artifacts:** scoped `SK-*`, `PRJ-*`, `EV-*` and `CL-*` records linked to actual GitHub repositories, immutable commits, PR diffs, tests, CI, deployments, and production observations where genuinely available.
- **AI-assisted engineering and orchestration:** user-approved evidence derived from ChatGPT discussions, Codex agent tasks, planning briefs, scope/acceptance decisions, human-in-the-loop (HITL) review, bug triage, prompt/task orchestration, implementation, and independently observed outcomes. Distinguish **designed**, **directed**, **reviewed**, **coded**, **tested**, **deployed**, and **operated**. Conversation plans and agent completion claims never prove implemented or production functionality by themselves.
- **Source permissions:** ChatGPT/Codex records must be accessible through explicitly consented, supported access or owner-curated evidence references/exports. No assumption that a public website can browse the user's chats, private GitHub repos, or connected tools. No ingestion of raw private conversations, employer code, client PII, secrets, or personal medical data into public assets.
- **ProofTree semantics:** use its `E0–E5` evidence classification and claim review state (`approved_for_scope`, `partially_supported`, etc.) **claim by claim**, with contribution, date, environment, limitations, conflict/supersession and access noted. Evidence levels describe observed proof **types**, not global competence scores.

### Proposed minimum workflow (ILL-07)

1. **Private owner-only entry:** authenticated screen/workspace for JD PDF/DOCX upload or pasted text, optional target role label, current approved master résumé version, and explicit consent for necessary processing. Do **not** expose JD parsing or ProofTree querying to anonymous portfolio visitors.
2. **Extract JD requirements:** identify skill, responsibility, seniority, domain and outcome requirements; separate required vs preferred and preserve original JD passages for traceability. Avoid treating boilerplate as requirements.
3. **ProofTree read-only retrieval:** query reviewed private records through an authenticated server-side integration, returning permitted claim text, stable record IDs, links, proof dates, human-vs-agent contribution and caveats. Define/version the API contract in ProofTree first; fail closed when auth/API/evidence is unavailable rather than generating fabricated substitutes.
4. **Build an internal alignment matrix:** `JD requirement → candidate supported claim → CL/SK/EXP/PRJ/EV IDs → allowed wording → support status → gaps`. Rank relevant evidence for this JD, favor direct support and recent relevant evidence; never hide conflicting or outdated evidence. Separate fully supported, supported with qualification, self-reported, and unsupported requirements.
5. **Generate a reviewable tailored résumé draft:** start from the owner-approved canonical résumé template and accurate immutable profile facts, prioritize relevant truthful bullets/keywords, preserve correct chronology/titles/education, and include agent-orchestration/HITL-SDLC capabilities only with accurate contribution language. No invented employers, tenures, certifications, metrics, production claims, personally coded lines or unsupported technologies.
6. **Human approval gate:** show generated résumé **alongside** a private evidence-mapping report and warnings/unsupported requirements; permit edit, reject, annotate or omit a claim before any approved résumé export.
7. **Export after approval:** downloadable accessible PDF and editable DOCX, sharing the same approved content, plus a private versioned provenance manifest (JD identifier/hash if practical, master résumé version, ProofTree snapshot/version, claim IDs, export date). Do not include internal private evidence references or sensitive chat data in public résumé exports by default.
8. **Manual reuse:** separate résumé per JD; preserve only consented, minimal private job/draft history, permit deletion, and ensure canonical generic public résumé files are never silently replaced by JD-specific versions.

### Acceptance criteria

- [ ] Authentication and access controls prevent public users from uploading JDs to private generation or querying ProofTree; ProofTree auth/API contract reviewed and verified without client-exposed secrets.
- [ ] Uploaded PDF/DOCX or pasted JD is parsed; original must-have/nice-to-have requirements are retained and checkable. Reject unsupported/malicious files safely; enforce file size/type limits and retention policy.
- [ ] A realistic JD maps to verified source record IDs, approved/scope-limited wording, contributor attribution, dates and links, with reproducible ranking notes and explicit evidence gaps.
- [ ] Tests demonstrate **no invented employment, dates, metrics, certifications, stack use or outcomes** even when the JD strongly requests an unsupported capability.
- [ ] ChatGPT/Codex evidence is only considered when imported/accessible with consent and attributable to actual human contribution; demonstrate that an agent suggestion alone is *not* resume proof.
- [ ] Contradictory, superseded, private, unreviewed and self-reported records are appropriately qualified or excluded; unavailable ProofTree service fails closed with a useful error.
- [ ] A reviewer can trace **every substantive generated claim** to a valid approved record or appropriately qualified self-report; gaps and caveats are visible before approval.
- [ ] No artifact is labeled approved until explicit owner signoff. After signoff, PDF/DOCX output preserves the approved text and is downloadable; private evidence mapping is not accidentally published.
- [ ] One end-to-end test uses a sanitized JD fixture with both supported and unsupported requirements; another tests missing/private evidence, integration outage and unauthorized requests.

### Out of scope / protection of existing work

- No auto-application, auto-bidding, outbound résumé email, bulk recruiter outreach, submission to job boards, or public anonymous generation.
- No automatic creation/promotion of ProofTree evidence from ChatGPT chats, Codex transcripts, memory summaries or unverifiable agent reports.
- No public exposure of private ProofTree data, protected employer/client documents, credentials, full private chats, or generative model context.
- No ProofTree database/API implementation inside the portfolio repo; API work is governed separately by ProofTree.
- No change to ILL-06A's existing downloadable **generic** résumé or the navigation link to the W2 résumé site.
- No impact on the current PR #2 acceptance gate or apex cutover timeline: **ILL-07 is future work after dependency readiness and separately reviewed scope**.

---

## PR #2 approval and slice boundaries

- CR-001 and CR-002 are **requested amendments**, not grounds to claim the draft PR already contains them.
- Owner requested documentation **before PR approval**. Treat both **ILL-05 and ILL-06A as proposed pre-approval scope additions** until the owner accepts the order, content, and the canonical résumé file.
- Implement **one slice at a time** after scope approval; separate commit(s) on `feat/illustrated-main-domain-readiness` (or successor `feat/*` branch if this PR is closed) followed by review.
- ILL-06B automatic delivery is **deferred**; do not block the portfolio cutover on building mail infrastructure.
- No PR merge, `main` update, `tuckerwray.com` promotion, or Zoho/DNS changes are authorized by this document.
