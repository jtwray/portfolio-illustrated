# Try my tools: small-business demo catalogue

_Status: ILL-TOOLS-01 implemented and locally verified; owner review pending. Updated 2026-10-27._
_Repository: jtwray/portfolio-illustrated. Starting main: 6c28b3f1422fc9ff0d72b712d6e74bc122653443._

## Purpose and authorization

Let a small-business visitor experience a small, useful result, then request setup,
customization, repair, training, or ongoing care. Tucker endorsed this concept and
requested a branch from the portfolio's main and a descriptive draft PR.

The initial documentation checkpoint preserved this plan and the owner's contact
confirmation. The branch now also implements ILL-TOOLS-01: the /tools/ page, a
fictional inquiry-board sample, portfolio links, and an editable contact handoff.
See the [implementation review record](records/tools-page-2026-10-27.md).
Live sending and product integrations remain later slices.

## Page architecture

Use a dedicated **/tools/** secondary page, implemented as **tools/index.html** in
this existing static portfolio. Reuse its typography, colors, navigation, footer,
and accessible controls. Add a visible "Try my tools" navigation link and a modest
homepage invitation when that page is implemented.

Use ordinary links and progressive JavaScript enhancements for interactive sample
experiences. A full SPA/router/framework migration is unnecessary for the catalogue.
Visitors should be able to open, refresh, bookmark, and navigate back from /tools/
without relying on a client-side router.

The portfolio owns the catalogue, explanations, readiness labels, and inquiry handoff.
Existing product repositories own their executable applications and product roadmaps.
Authenticated trials use reviewed backend endpoints in the appropriate application;
credentials and sending permissions never live in public page code.

Keep the existing illustrated host for the initial implementation. This plan does
not depend on, or approve, an apex-domain migration.

### Page outline

1. Heading: "Try a useful tool for your business."
2. Short explanation: free, bounded examples; sample data clearly identified.
3. Tool cards: business problem, what happens, limits, readiness, and one relevant action.
4. Working sample/trial or a link to that tool's focused experience.
5. After-result choices: "Set this up for me", "Fix something similar", or an optional follow-up request.
6. Brief explanation of setup, custom builds, repairs, training, and ongoing care.

Keep employment and general portfolio navigation available. The tools catalogue
adds a business entry point without replacing the professional portfolio.

## Proposed catalogue and evidence

Inventory reflects source/documentation and prior project reports reviewed on
2026-10-26, with portfolio main checked on 2026-10-27. These are adaptation proposals,
not claims that the original products or future trials are all ready. The isolated
portfolio sample was browser-tested for ILL-TOOLS-01; the existing products were
not re-tested by that slice.

| Foundation | Bounded free experience | Paid continuation | Readiness / next work |
| --- | --- | --- | --- |
| Dashboarda | Explore a clearly labeled sample customer/job/task board; filter records and inspect changes | A business dashboard and connected workflows | Isolated portfolio sample implemented and locally verified; production Dashboarda remains separate |
| SignalDesk | Add one sample prospect, repeat the operation, and see an update without duplicate records | Form/CRM/Airtable synchronization and follow-up workflow | Feature implementation evidence exists; verify the exact revision and an isolated destination before offering a live sync |
| Email Action dashboard | Explore fictional messages and the actions they require | Inbox triage and follow-up setup | Existing display application; it does not establish sending or an authorized live-inbox integration |
| HTML-to-PDF API | Complete a short sample estimate and download its PDF | Branded estimates, reports, and document generation | Prior local HTML rendering was reported; locate source/deployment and recheck the chosen template path before enabling a trial |
| Agent Toolchain Canary | Inspect a clearly labeled sample diagnostic report and suggested next steps | Troubleshooting, repairs, monitoring, and maintenance | Existing CLI; offer a guided example rather than remote access to a visitor's machine |
| Southside SaaS Starter | Explore a sample application after its runtime and inquiry paths are verified | Setup, customization, training, or a bounded managed service | Prior private preview report; application verification and commercial connections remain incomplete |
| New verified-message trial | Verify the visitor's own email and receive one preset sample reminder | Business confirmations, reminders, and follow-ups | New capability; backend verification, provider setup, delivery checks, and cost controls are required |

Sources: [Dashboarda](https://github.com/jtwray/dashboarda),
[SignalDesk feature PR](https://github.com/jtwray/dashboarda/pull/2),
[Canary](https://github.com/jtwray/agent-toolchain-canary), and
[Southside Automation source](https://github.com/jtwray/Southside-Automations-website).

The PDF and starter entries rely on prior project reports and remain proposals
until their exact source/runtime is inspected. Southside Automation is an existing
service/inquiry destination, not proof that the separate SaaS Starter is complete.

Personal projects such as WAMIF and Potty Weekend can remain portfolio evidence;
a specific business use case should precede adapting them into business trials.
Keep the wider catalogue, and implement experiences in readiness order. Do not
require every app to be trial-ready before releasing the first useful page.

## Trial behavior and limits

Use three explicit experience types:

- **Explore a sample:** public fictional data, no email or phone gate, no access to private production records.
- **Run a limited trial:** a real bounded action with clear inputs, limits, and observed outcome.
- **Request a walkthrough:** for work requiring sensitive data, account access, or substantial setup.

Only working, verified experiences get a "Try free" action. Planned experiences
get truthful availability text and a walkthrough/inquiry action. Simulation must
be labeled; a sample screen cannot claim that a message or sync actually occurred.

Initial proposed email-trial contract:

- One verified recipient, one preset business message, and one successful demo action per recipient per 24 hours.
- Verify control of the actual destination on the server before authorizing that action; a shared dashboard PIN is not recipient verification.
- Bound code requests, resend frequency, guesses, action attempts, and request sizes by destination and session/network signals.
- Set explicit global daily action and monetary limits before enabling sends; include verification traffic in those limits.
- Enforce limits before incurring provider cost, stop when exhausted, and provide an operator kill switch.
- Make retries idempotent so refresh/double-click does not send additional messages.
- Explain queued, delivered where observed, failed, expired, and quota-exhausted states accurately.
- Keep credentials and verification codes out of browser storage, URLs, public repositories, and diagnostic output.
- Use the minimum contact/trial data needed; agree retention and deletion behavior before launch.

Exact provider, operating budget, retention period, and numerical verification
limits are implementation decisions to settle before live sending, not questions
blocking this documentation PR. Start with email. SMS or push requires a separate
delivery/setup review before being advertised.

For the PDF trial, use preset templates and bounded text fields rather than
arbitrary URLs or uploaded HTML. For sync, use a dedicated demo destination and
separate sessions; never connect anonymous visitors to Tucker's production data.

Verification design reference:
[Twilio verification best practices](https://www.twilio.com/docs/verify/developer-best-practices).
Provider guidance informs controls; it is not a provider selection or authorization to spend.

## Inquiry and follow-up journey

~~~mermaid
flowchart LR
  A["Choose a business problem"] --> B["Explore sample or run bounded trial"]
  B --> C["See the result and its limits"]
  C --> D["Request setup or repair"]
  C --> E["Optionally request follow-up"]
  D --> F["Clarify scope or discovery call"]
  E --> F
  F --> G["Scoped quote and agreed work"]
  G --> H["Delivery and training"]
  H --> I["Optional ongoing care"]
~~~

Browsing or entering a verification code does not opt a visitor into marketing.
An inquiry allows the requested reply; any broader follow-up invitation is a
separate, unchecked choice with clear wording and a recorded scope.

Suggested post-result actions:

- "Set this up for my business."
- "I have something similar that needs fixing."
- Optional: "Email me about adapting this tool to my business."

Initially hand off to the existing reachout form with a user-editable message
identifying the selected tool and request. Preserve its current field contract
where possible. A visitor explicitly submits the inquiry. Do not silently add
automatic replies, subscriptions, CRM writes, or an outreach sequence.

The existing portfolio form's record capture and inbox notification are
[owner-confirmed](records/contact-intake-2026-10-27.md). A future tool-specific form,
new form fields, opt-in storage, or new delivery route needs its own relevant checks.

## Service paths

| Need | Offer and next step |
| --- | --- |
| Something is broken | Brief problem description, bounded diagnosis, then a repair scope/quote |
| Connect existing tools | Setup, integration, launch checks, and training |
| Build a new workflow | Discovery as needed, then a scoped build quote |
| Keep it working | Agreed maintenance/monitoring/support with explicit coverage and limits |

Discovery calls are useful when scope is unclear; a straightforward repair need
not be forced through a long funnel. No prices, service-level commitments,
unlimited support, or business-success guarantees are set by this plan.

Measure completed demos, explicit setup/repair inquiries, qualified conversations,
quotes, and paid work. Aggregate trial counts and voluntarily submitted inquiry
context are enough for the first iteration; do not add tracking dependencies just
to launch the catalogue.

## Delivery sequence and acceptance

Use the namespaced IDs below to avoid the existing ILL-05/06/07 IDs used by other
open portfolio branches. Keep implementation work in bounded, reviewable slices.

| Slice | Outcome | Acceptance evidence |
| --- | --- | --- |
| ILL-TOOLS-00 | Preserve this plan and contact confirmation | Documentation review, links/paths checked, main-based branch and descriptive draft PR; no runtime files changed |
| ILL-TOOLS-01 | Implemented/local verification complete; owner review pending: catalogue page and isolated dashboard-pattern sample | /tools/ direct navigation/refresh works; desktop/mobile and keyboard checks; sample data and availability labels are accurate; inquiry handoff retains the selected tool; existing contact/navigation still work |
| ILL-TOOLS-02 | Verified email trial | Server-side destination binding; real send only to the verified recipient; tested resend/guess/usage/global-budget limits and retry behavior; no sensitive logs; observed success/failure states; explicit inquiry and separate optional follow-up |
| ILL-TOOLS-03 | Add other ready tools individually | Each tool has a source revision, truthful mode/limits, isolated data, product-specific verification, and a relevant service handoff |

The form-delivery blocker is closed by Tucker's confirmation; do not repeat a
production submission just to satisfy an outdated planning note. Normal contact
regression checks remain part of future behavior-changing work.

## Branch reconciliation and merge meaning

This branch starts from main at the SHA above. It is independent of the existing
readiness PR #2, media-plan PR #3, and screenshot PR #4. Those branches have their
own incomplete work and may contain older contact-verification wording.

Reconcile shared README/roadmap/slice edits when combining branches. Preserve their
unrelated plans and media. Supersede stale contact wording with the dated owner
record without claiming that every gate in those PRs is complete.

The branch now includes the plan and ILL-TOOLS-01. Merging it will publish the
catalogue and sample through the existing main deployment. It does not activate
live messaging, connect production product data, submit the contact form, merge
the other drafts, or authorize a domain cutover. Owner review and merge remain
outstanding; no merge or domain change was performed in this work.
