# Tucker Wray — Illustrated Portfolio

An alternative, responsive, static developer portfolio using original mixed-media-inspired illustration, warm paper colors, expressive serif typography and accessible navigation.

## Preview locally

Open `index.html` in a browser or start a static server such as `python -m http.server 8000` from the repository root. The site has no build step, npm dependencies or runtime API keys.

## Try my tools (PR candidate)

The new [tools page](tools/index.html) is available at /tools/ when served over
HTTP. It contains one interactive, fictional inquiry board and six other
catalogue entries with discussion/planned-trial labels. The sample keeps state
only in the current page and resets on reload.

Tool inquiry links draft an editable message in the existing Netlify reachout
form; they do not submit it. Live email sending remains a future slice.
See the [implementation review record](docs/records/tools-page-2026-10-27.md).

## Source

- `index.html`: semantic HTML and portfolio content.
- `assets/styles.css`: responsive visual design.
- `assets/app.js`: mobile menu, project filters and progressive enhancements.
- `assets/art/`: original illustration assets (two generated WebP compositions and four SVG illustrations).

This is an independently deployed illustrated portfolio candidate, **not** a cutover of `tuckerwray.com`. The illustrated person is a conceptual figure, not a verified portrait of Tucker Wray. The project vignettes are illustrations, not application screenshots.

## Publishing safely

The `main` branch is deployed as a static site on Netlify at **https://illustrated.tuckerwray.com**. The original `tuckerwray.com` portfolio is intentionally independent; do not change its domains or email DNS without a separate reviewed cutover plan.

The contact form uses Netlify Forms markup and a honeypot. On a Netlify deployment, test a submission and enable the appropriate form notifications. On localhost or `file://`, the form cannot deliver messages; use the email link.

Before promoting this design to the apex domain, review project claims, content links, accessibility, and contact routing; protect Zoho email DNS records (MX/SPF/DKIM/DMARC) and the legacy archive migration plan.

## Planning and verification

- [Illustrated portfolio roadmap](docs/ROADMAP.md)
- [Scoped slices and acceptance criteria](docs/SLICES.md)
- [Try my tools: catalogue, page architecture, and delivery plan](docs/TRY_MY_TOOLS.md)
- [Owner-confirmed contact intake, reported 2026-10-27](docs/records/contact-intake-2026-10-27.md)
- [WAMIF proof/link follow-up](https://github.com/jtwray/portfolio-illustrated/issues/1)

Tucker confirmed on 2026-10-27 that his manual portfolio-form test appears in both his email inbox and Netlify Forms. The earlier automated test was in the Spam tab; see the dated contact-intake record above. The former capture/inbox-delivery blocker is closed on owner evidence. ProofTree was just started (2026-10-19); the public repo is currently empty, and a minimal WAMIF evidence packet remains to be assembled in Slice ILL-02.

## Project links

- WAMIF — https://github.com/jtwray/wamif
- ShelterGaze — https://github.com/jtwray/Shelter-Gaze
- Dashboarda — https://github.com/jtwray/dashboarda
- GitHub — https://github.com/jtwray
