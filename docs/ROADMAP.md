# Illustrated Portfolio — Roadmap

_Last reviewed: 2026-10-27 (contact delivery and tools planning update)_

## Mission

Present Tucker Wray's software engineering and small-business systems work in an approachable, visually distinctive, **evidence-backed** portfolio. The site should generate trustworthy inquiries while preserving independently managed projects and domains.

**Planning authority:** this repository owns the illustrated portfolio's roadmap and slices. WAMIF Rebuild owns its own product roadmap in `jtwray/wamif-rebuild/docs/roadmap.md`; do not overwrite or duplicate that plan here.

**Live site:** https://illustrated.tuckerwray.com (`jtwray/portfolio-illustrated`, Netlify `portfolio-illustrated`, `main`). The user verified that the illustrated subdomain serves this site over HTTPS while `tuckerwray.com` still serves the original portfolio. The primary domain migration is **not** approved by this roadmap.

## Roadmap

| Milestone | Status | Gate / observable outcome | Slice |
| --- | --- | --- | --- |
| M0 — Independent illustrated release | **Complete** | Separate GitHub repo, static Netlify deploy, branded HTTPS subdomain, project cards, responsive design, Netlify form registered | ILL-00 |
| M1 - Lead capture end-to-end | **Owner-confirmed delivery (2026-10-27)** | Manual test visible in Netlify Forms and the intended inbox; earlier automated test found in Spam. [Dated record](records/contact-intake-2026-10-27.md) | ILL-01 |
| M2 — Curated proof checkpoint | **Started — evidence packet pending** | Tucker confirmed ProofTree has just started (2026-10-19); assemble the smallest verified, public-safe WAMIF evidence packet without waiting for the entire registry | ILL-02 |
| M3 — WAMIF link and claim correction | **Blocked by minimal evidence packet and destination review** | Select public-safe, logged-out-accessible project destination; correct both image/title links and technology/status claims | ILL-03 · [Issue #1](https://github.com/jtwray/portfolio-illustrated/issues/1) |
| M4 — Portfolio release QA and evidence hygiene | **Proposed** | Confirm remaining project links, copy, accessibility, mobile, outbound CTA, contact, and proof references without regressions | ILL-04 |

**ProofTree checkpoint (2026-10-19):** Tucker says the curated proof library was **just started**. The canonical [ProofTree repository](https://github.com/jtwray/prooftree) currently exists but has no committed files. This is a repository observation, **not** a judgment that no evidence exists in WAMIF or other projects. The portfolio needs only a minimal independently verified proof packet for ILL-03; ProofTree itself does not have to be finished.

Only **one implementation slice** should be active at a time. Work marked *Proposed* is not an implementation authorization. M1 capture/inbox delivery is closed on owner confirmation; retain ordinary contact regression checks. ILL-02 remains a separate evidence checkpoint while the full ProofTree system is developed independently.

## Try my tools workstream - planning baseline (2026-10-27)

Tucker endorsed a bounded small-business demo catalogue and requested that the
plan be preserved on a main-based branch with a draft PR. The recommended entry
point is a static /tools/ secondary page, with progressive interaction and
product-owned trial backends. See [the complete plan](TRY_MY_TOOLS.md).

| Slice | State | Outcome |
| --- | --- | --- |
| ILL-TOOLS-00 | Preserved in the draft PR | Catalogue, architecture, limits, service paths, and contact evidence |
| ILL-TOOLS-01 | Implemented and locally verified; owner review pending | Matching catalogue page, one isolated sample, and existing-form inquiry handoff |
| ILL-TOOLS-02 | Proposed; provider/budget controls required | Verified email trial with enforced usage limits |
| ILL-TOOLS-03 | Proposed; per-product readiness required | Additional tools added individually |

These namespaced IDs avoid existing ILL-05/06/07 work on other open branches.
The branch now implements the catalogue and an isolated fictional sample; see the
[review record](records/tools-page-2026-10-27.md). Live messaging and production
product integrations remain later work. Product roadmaps stay in their own repos.
Existing WAMIF, readiness, media, and domain-cutover gates retain their own scope.

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
