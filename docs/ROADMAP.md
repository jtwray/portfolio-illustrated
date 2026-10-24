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
| M2 — Curated proof checkpoint | **Started — evidence packet pending** | Tucker confirmed ProofTree has just started (2026-10-19); assemble the smallest verified, public-safe WAMIF evidence packet without waiting for the entire registry | ILL-02 |
| M3 — WAMIF link and claim correction | **Blocked by minimal evidence packet and destination review** | Select public-safe, logged-out-accessible project destination; correct both image/title links and technology/status claims | ILL-03 · [Issue #1](https://github.com/jtwray/portfolio-illustrated/issues/1) |
| M4 — Portfolio release QA and evidence hygiene | **Proposed** | Confirm remaining project links, copy, accessibility, mobile, outbound CTA, contact, and proof references without regressions | ILL-04 |

**ProofTree checkpoint (2026-10-19):** Tucker says the curated proof library was **just started**. The canonical [ProofTree repository](https://github.com/jtwray/prooftree) currently exists but has no committed files. This is a repository observation, **not** a judgment that no evidence exists in WAMIF or other projects. The portfolio needs only a minimal independently verified proof packet for ILL-03; ProofTree itself does not have to be finished.

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

## October 23 media workstream

The existing ILL-00–04 roadmap remains in place. Its October 19 status statements
are historical and have not been revalidated by this planning update. Use the
[project brain](PROJECT_BRAIN.md) to reconcile them before implementation.

| Step | State | Outcome | Slice |
| --- | --- | --- | --- |
| Recoverable media baseline | Preserved; draft PR #3 | Original 49-file package at `59081a1`; browser review still pending | [Checkpoint](PROJECT_MEDIA_REVIEW.md) |
| Dashboarda captures | Planned; next dispatch candidate | Reviewed PIN prompt and useful public-safe dashboard evidence | ILL-05 |
| Import Canary media | Waiting on Canary-owned CAN-01 | Approved images and captions with source revision and observed outcome | ILL-06 |
| Editorial/media acceptance | Planned | Four revised stories and a review package with accurate contribution/evidence wording | ILL-07 |
| Illustrated case-study integration | Planned | Four accessible case-study destinations and working project cards | ILL-08 |
| Release acceptance | Planned | Browser, mobile, keyboard, contact and resume checks on the reviewed commit | ILL-04 |

Sequence: ILL-05 → ILL-06 → ILL-07 → ILL-08 → ILL-04, with one implementation
slice active. Planning this sequence does not dispatch agents or authorize release.
Prior ILL-02/03 criteria may be satisfied by later evidence/integration work only
when explicitly mapped and verified; they are not automatically closed.

### Canary project dependency

Canary CLI execution/capture work and later status/history, Check now and guided
re-authentication are owned by `jtwray/agent-toolchain-canary`; their roadmap and
temporary-agent assignments live with that project. The transfer is recorded in
[Canary draft PR #1](https://github.com/jtwray/agent-toolchain-canary/pull/1).

Portfolio ILL-06 only imports the approved CAN-01 media export. CAN-02–04 do not block
this workstream. Do not duplicate their implementation contracts in this repository.
