# Portfolio change requests — draft PR #2

_Last reviewed: 2026-10-23. Source of truth for pre-approval scope review. This document **requests changes**, but does not represent implemented or verified features._

**PR:** https://github.com/jtwray/portfolio-illustrated/pull/2  
**Implementation policy:** one bounded slice at a time, commits only on a `feat/*` branch, followed by independent outcome review; no direct `main` changes or domain cutover.

## CR-001 — Feature Potty Weekend as a shipped product case study

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

## PR #2 approval and slice boundaries

- CR-001 and CR-002 are **requested amendments**, not grounds to claim the draft PR already contains them.
- Owner requested documentation **before PR approval**. Treat both **ILL-05 and ILL-06A as proposed pre-approval scope additions** until the owner accepts the order, content, and the canonical résumé file.
- Implement **one slice at a time** after scope approval; separate commit(s) on `feat/illustrated-main-domain-readiness` (or successor `feat/*` branch if this PR is closed) followed by review.
- ILL-06B automatic delivery is **deferred**; do not block the portfolio cutover on building mail infrastructure.
- No PR merge, `main` update, `tuckerwray.com` promotion, or Zoho/DNS changes are authorized by this document.
