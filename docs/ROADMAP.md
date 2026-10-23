# Illustrated Portfolio — Roadmap

_Last reviewed: 2026-10-23 (change-request intake; earlier evidence status retained as originally recorded)_

## Mission

Present Tucker Wray's software engineering and small-business systems work in an approachable, visually distinctive, **evidence-backed** portfolio. The site should generate trustworthy inquiries while preserving independently managed projects and domains.

**Planning authority:** this repository owns the illustrated portfolio's roadmap and slices. WAMIF Rebuild owns its own product roadmap in `jtwray/wamif-rebuild/docs/roadmap.md`; do not overwrite or duplicate that plan here.

**Live site:** https://illustrated.tuckerwray.com (`jtwray/portfolio-illustrated`, Netlify `portfolio-illustrated`, `main`). The user verified that the illustrated subdomain serves this site over HTTPS while `tuckerwray.com` still serves the original portfolio. The primary domain migration is **not** approved by this roadmap.

## Roadmap

| Milestone | Status | Gate / observable outcome | Slice |
| --- | --- | --- | --- |
| M0 — Independent illustrated release | **Complete** | Separate GitHub repo, static Netlify deploy, branded HTTPS subdomain, project cards, responsive design, Netlify form registered | ILL-00 |
| M1 — Lead capture end-to-end | **Needs verification** | One legitimate inquiry visible in Netlify Forms, expected inbox notification received, handling/spam path checked | ILL-01 |
| M2 — Curated proof checkpoint | **Started — evidence packet pending** | Tucker confirmed ProofTree has just started (2026-10-19); assemble the smallest verified, public-safe WAMIF evidence packet without waiting for the entire registry | ILL-02 |
| M3 — WAMIF link and claim correction | **Blocked by minimal evidence packet and destination review** | Select public-safe, logged-out-accessible project destination; correct both image/title links and technology/status claims | ILL-03 · [Issue #1](https://github.com/jtwray/portfolio-illustrated/issues/1) |
| M4 — Portfolio release QA and evidence hygiene | **Proposed** | Confirm remaining project links, copy, accessibility, mobile, outbound CTA, contact, and proof references without regressions | ILL-04 |
| M5 — Potty Weekend portfolio proof | **CR-001 requested / not implemented** | Fifth card and honest case study linking shipped app, public source and limitations; independent preview review | [Card concept](./visuals/cr-001-potty-weekend-card.svg) · ILL-05 · [Change requests](./CHANGE-REQUESTS.md#cr-001--feature-potty-weekend-as-a-shipped-product-case-study) |
| M6 — Résumé file availability | **CR-002 requested / not implemented** | Preserve the existing W2 digital résumé link; add approved-current PDF open/download actions and accessible navigation | [Mockup](./visuals/cr-002-resume-access.svg) · ILL-06A · [Change requests](./CHANGE-REQUESTS.md#cr-002--accessible-résumé-formats-without-losing-the-digital-résumé-link) |
| M7 — Recipient email option | **Deferred / separate approval** | Validate actual demand, delivery architecture, consent, anti-abuse and privacy before enabling automatic sending | ILL-06B |
| M8 — ProofTree JD-to-résumé tailoring | **CR-003 future / dependency-gated / not implemented** | Authenticated owner-only JD upload, evidence-to-requirement matching and approval-gated PDF/DOCX export, requiring a verified read-only ProofTree API | [Workflow visual](./visuals/cr-003-prooftree-resume-flow.svg) · ILL-07 · [Change request](./CHANGE-REQUESTS.md#cr-003--prooftree-evidence-verified-résumé-tailoring-from-a-job-description) |

> [Visual design index](./visuals/README.md) — version-controlled concept images for the résumé access and future ProofTree flow; they do not represent deployed functionality.

**Future request (2026-10-23):** CR-003 proposes ILL-07, an authenticated, ProofTree-backed JD upload and evidence-verified résumé tailoring tool. The ProofTree API and permitted ChatGPT/Codex evidence access are **dependencies, not assumed capabilities**. This is future owner-only functionality, explicitly **not a condition for PR #2 approval or domain cutover**; see [change request](./CHANGE-REQUESTS.md#cr-003--prooftree-evidence-verified-résumé-tailoring-from-a-job-description) and [slice](./SLICES.md#ill-07--prooftree-backed-jd-to-résumé-tailoring-cr-003--future-dependency-gated).

**PR #2 review decision (2026-10-23):** The portfolio owner requested two documented, **pre-approval** change requests, CR-001 Potty Weekend and CR-002 résumé access, on `feat/illustrated-main-domain-readiness`. Both are proposed work, **not** completed by this documentation update. CR-002's automatic-email phase ILL-06B is deferred. See [change requests](./CHANGE-REQUESTS.md) and [slices](./SLICES.md). The existing navigation link to `https://w2.tuckerwray.com/` is preserved. This does not authorize merge or apex promotion.

**ProofTree checkpoint (updated 2026-10-23):** The [ProofTree repository](https://github.com/jtwray/prooftree) is **private** and has a committed evidence-registry scaffold, standards, schemas, and audit documentation. Its checked-in state describes working feature-branch audits and outstanding verification/merge gaps; it does **not** establish that an authenticated claim-query API exists. For ILL-03 the portfolio still needs only the minimum public-safe, independently checked WAMIF proof, not a completed ProofTree platform.

Only **one implementation slice** should be active at a time. Work marked *Proposed* is not an implementation authorization. The next unclosed acceptance gate is M1; ILL-02 may inventory evidence while the full ProofTree system is being developed independently.

## WAMIF decision record / guardrails

- Current public portfolio image and title both link to `https://github.com/jtwray/wamif` (public).
- Newer canonical engineering work lives in `jtwray/wamif-rebuild`, currently **private**; an anonymous visitor cannot inspect its GitHub source.
- WAMIF Rebuild documentation describes a **React + TypeScript + Vite** application, while the illustrated portfolio currently advertises **Next.js**. Check the exact evidence and correct any inaccurate claim when auditing the featured project.
- Candidate destinations: verified publicly accessible live demo, carefully sanitized public case study, or a public repository if separately approved. Do not automatically make private source or sensitive genealogy data public.
- Before changing a link: check proof sources, project status, demo accessibility, privacy, and claims. Update both WAMIF entry points together and verify in a signed-out browser.
- Do not treat a WAMIF product milestone as an illustrated portfolio slice.

## Outside this portfolio scope

- **Airtable / SignalDesk automation:** separate project roadmap; continue its narrow opportunity-sync vertical slice first.
- **n8n:** a *near-term Toolbelt Growth* backlog candidate after the narrow Airtable workflow, not an immediate portfolio/webhook feature.
- **RAG and voice/video avatars:** later, evidence- and use-case-gated explorations. No speculative agents, infrastructure, new branches, or webhook orchestration in this roadmap.
- No changes to `tuckerwray.com`, `www`, existing archive arrangements, or Zoho MX/SPF/DKIM/DMARC.

See [slices](./SLICES.md) for scope, dependencies, and acceptance criteria.
