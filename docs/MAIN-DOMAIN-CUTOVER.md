# Illustrated portfolio — main-domain promotion checklist

_Last reviewed: 2026-10-23. This is a **feature-branch preparation plan**, not a production cutover._

## Candidate and scope

- Candidate: `illustrated.tuckerwray.com` (Netlify project `portfolio-illustrated`), based on `jtwray/portfolio-illustrated`.
- Proposed destination: `tuckerwray.com` (and verify `www.tuckerwray.com` separately).
- Keep `w2.tuckerwray.com` as a recruiter-specific destination and `southside.tuckerwray.com` as business-services funnel.
- Keep existing `tuckerwray.com` Netlify project and its submission history intact for safe rollback.
- Do **not** change the GitHub default branch, directly commit to `main`, change DNS, or reassign any domains while this PR is open.

## Content improvements in this feature branch

- [x] Preserve illustrated visual identity while clarifying full-stack engineering and automation positioning.
- [x] Put Dashboarda and Agent Toolchain Canary first and link to public engineering evidence.
- [x] Add concise source-linked case studies that state limitations.
- [x] Replace WAMIF's misleading Next.js tag and weak public-source shortcut with a public-safe project overview.
- [x] Add prominent hiring/résumé and small-business routes.
- [x] Preserve the existing Netlify `reachout` form and thank-you page (no form markup changes).

## Outstanding pre-approval change requests

- [ ] **CR-001 (ILL-05)** — review/implement a fifth Potty Weekend project card and accurate case study. Evidence is in the public app/repository; real-phone outcomes remain unverified.
- [ ] **CR-002 (ILL-06A)** — retain the existing W2 résumé navigation and add a verified-current PDF view/download path. Document ownership/versioning and validate desktop/mobile behavior.
- [ ] Decide explicitly whether either requested change is required before the current PR merges, or will be implemented as its own reviewed successor `feat/*` PR. **No request is completed simply by adding documentation.**
- [ ] **ILL-06B automatic email** remains deferred; do not add a mail-sending endpoint as a prerequisite to the portfolio migration.

See [full change requests](./CHANGE-REQUESTS.md), [roadmap](./ROADMAP.md), and [slice gates](./SLICES.md).

## Verification before merging

- [ ] Review rendered desktop and mobile branch preview for hero, navigation, cards, footers, and contrast.
- [ ] Verify all `work/*.html` links, GitHub references, résumé link, Southside link, and external destinations logged out.
- [ ] Confirm WAMIF language with actual implementation evidence when a sanitized packet is ready. No publishing private genealogy/source.
- [ ] Check keyboard and filter behavior; assess accessibility and responsive layout.
- [ ] Confirm illustrated site's registered Netlify `reachout` form by form name and fields, submit a legitimate live test, verify stored submission, and confirm target-inbox notification. The form was registered with one historical submission as of 2026-10-22; that alone is **not** confirmation of email delivery.
- [ ] Confirm GitHub PR checks / deploy preview show the final commit.
- [ ] Review the site's existing Google indexing/SEO needs and add canonical/redirect handling for apex only at cutover.

## Domain and rollback safeguards

1. Capture the current apex project ID, deploy ID, site settings, custom-domain configuration, and snapshot/backup of the current website.
2. Confirm the legacy portfolio remains available at an explicit archive address such as `2020.tuckerwray.com`; test its content and links.
3. Record existing DNS zone values. **Do not change Zoho Mail records, MX, SPF, DKIM, DMARC, or unrelated DNS records.** Existing business email and MFA must remain untouched.
4. After approved PR merge and QA, arrange Netlify custom-domain migration using the appropriate project/domain management surface. Do not assume DNS changes are necessary.
5. Validate HTTP(S), certificate issuance, apex and `www` behavior, contact delivery, and all project page routes after the switch.
6. Keep old Netlify project available and document a tested reverse domain-assignment procedure in case rollback is required.
7. Only after successful cutover, decide whether `illustrated.tuckerwray.com` should remain live or 301-redirect to the apex. Avoid duplicate indexed content and canonical-host ambiguity.

**Release gate:** no automatic domain cutover from a feature branch. Explicitly review the pull request and verify contact end-to-end before moving `tuckerwray.com`.
