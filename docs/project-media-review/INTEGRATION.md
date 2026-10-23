# Proposed slice: illustrated project evidence pages

This package was created in response to Tucker's October 23 media request. It does not modify the live illustrated portfolio, existing PRs, application code, DNS, or deployments.

## Recommended UX

Keep the illustrated visual identity. Four featured cards should link in the same tab to real pages: `/projects/wamif/`, `/projects/dashboarda/`, `/projects/agent-toolchain-canary/`, `/projects/potty-weekend/`. This review's anchors demonstrate the information hierarchy; production should use dedicated, shareable pages with sensible back navigation. Keep existing unrelated portfolio work/history available rather than deleting it as part of this slice.

Each card: conceptual illustration or actual product capture, precise one-sentence value, three or four supported skill tags, status, one “Read case study” primary action. On each case-study page show a screenshot, concise problem/result, contribution statement, story, diagrams, evidence gallery, then optional technical sections. Keep evidence limitations next to the relevant claim. Screenshots open in a keyboard-accessible full-size view. Preserve text captions and descriptive alt text.

External app/repository links use `target="_blank" rel="noopener noreferrer"` and a visible new-tab indicator. WAMIF and Potty Weekend have app links. WAMIF source remains private. Dashboarda points to public source/PR; do not present the PIN-gated dashboard as an anonymous demo. Canary points to its public repository; do not invent a Netlify app.

## Feature depth

- WAMIF: 1 parent STAR + individual routes, multi-person chronology, uncertainty/visual-overlap engineering details. Keep unreleased spiderfy work clearly separate.
- Dashboarda: 1 parent STAR + stable identity and SignalDesk details. Keep branch/deploy/runtime states distinct.
- Canary: 1 parent STAR + probe boundaries and incident lifecycle details. Prefer diagrams to tiny code images.
- Potty Weekend: 1 parent STAR + one short storage/UX section. A narrow product can demonstrate strong engineering without more nesting.

## Implementation boundary

Re-read current portfolio branch, PRs, roadmap and AGENTS.md before creating a fresh feat/* branch. Reconcile any in-flight portfolio change requests, including the resume-menu behavior, before implementation. Do not append this work blindly to an existing PR. Update the roadmap with a new unambiguous slice ID after inspecting current IDs.

## Acceptance

- Four cards reach four accessible case-study pages; live app/source CTAs follow the rules above.
- At least one relevant evidence capture per project, ideally three. Package currently contains 3 for WAMIF, 3 for Potty Weekend, 3 for Canary, and 3 for Dashboarda.
- Confirm exact personal role and agent assistance; keep results matched to observed evidence. Avoid blocked publication becoming a reason to erase legitimate firsthand contribution.
- Diagrams remain legible on mobile: show vertically or open full size, with equivalent text. Do not squeeze two diagrams into unreadable columns.
- Verify keyboard navigation, disclosure controls, link targets, images, 360px layout, and existing contact/resume behavior on a preview.
- No private code, real genealogy uploads, dashboard records, child logs/photos, credentials, or unsupported metrics.
- Only merge/publish through the user's established review workflow.

## Optional fifth project

Keep this slice at four. ProofTree may later become an evidence-system case study; Eagle Rock Animal ER may be the strongest client-outcome story once its receipts and shareable material are assembled. Neither is represented by fabricated media in this package.
