# Illustrated Portfolio — Roadmap

_Last reviewed: 2026-10-19_

## Mission

Present Tucker Wray's software engineering and small-business systems work in an approachable, visually distinctive, **evidence-backed** portfolio. The site should generate trustworthy inquiries while preserving independently managed projects and domains.

**Planning authority:** this repository owns the illustrated portfolio's roadmap and slices. WAMIF Rebuild owns its own product roadmap in `jtwray/wamif-rebuild/docs/roadmap.md`; do not overwrite or duplicate that plan here.

**Live site:** https://illustrated.tuckerwray.com (`jtwray/portfolio-illustrated`, Netlify `portfolio-illustrated`, `main`). The user verified that the illustrated subdomain serves this site over HTTPS while `tuckerwray.com` still serves the original portfolio. The primary domain migration is **not** approved by this roadmap.

## Roadmap

| Milestone | Status | Gate / observable outcome | Slice |
| --- | --- | --- | --- |
| M0 — Independent illustrated release | **Complete** | Separate GitHub repo, static Netlify deploy, branded HTTPS subdomain, project cards, responsive design, Netlify form registered | ILL-00 |
| M1 — Lead capture end-to-end | **Needs verification** | One legitimate inquiry visible in Netlify Forms, expected inbox notification received, handling/spam path checked | ILL-01 |
| M2 — Curated proof checkpoint | **Awaiting Tucker** | Ask whether curated proof library / ProofTree / Engineering Skills Registry is complete; identify verified, public-safe evidence and gaps for showcased work | ILL-02 |
| M3 — WAMIF link and claim correction | **Blocked by M2 and destination review** | Select public-safe, logged-out-accessible project destination; correct both image/title links and technology/status claims | ILL-03 · [Issue #1](https://github.com/jtwray/portfolio-illustrated/issues/1) |
| M4 — Portfolio release QA and evidence hygiene | **Proposed** | Confirm remaining project links, copy, accessibility, mobile, outbound CTA, contact, and proof references without regressions | ILL-04 |

Only **one implementation slice** should be active at a time. Work marked *Proposed* is not an implementation authorization. The next unclosed acceptance gate is M1; M2 can be clarified conversationally without starting a competing coding slice.

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
