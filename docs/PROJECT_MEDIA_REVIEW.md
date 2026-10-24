# Project media review checkpoint

The original October 23, 2026 review package is preserved unchanged in
`project-media-review/`. Its per-file SHA-256 receipts are in
`project-media-review-baseline.json`. Open `project-media-review/index.html`
to review the four case studies and their media.

This checkpoint does not integrate the package into the live site's navigation
or replace its existing project cards. The original package's scope and
verification notes remain intact.

## Follow-up requested by Tucker

- Add Dashboarda app screenshots where useful. Tucker is comfortable showing
  the PIN prompt and current dashboard state. Review each capture for private
  email, household, application, contact or other personal information; source
  information being public does not make every combined dashboard view public.
  Keep the PIN and credentials out of captures. Use clean or synthetic data
  where a real view would disclose private records.
- Prefer actual Canary CLI captures showing successful, failed, skipped and
  inconclusive probes with a caption recording command, revision, date and
  environment. Show only observed outcomes. A controlled demonstration failure
  should be labeled as such. Redact reports and machine/account details before
  publishing. Do not install schedules or alter authentication just to create media.
- Consider a separately bounded Canary status-view slice: most recent check,
  freshness, per-probe outcome, observed unchanged-status duration and history.
  Explain gaps in checks. Sampled checks do not prove continuous uptime;
  longest observed passing/failing streaks should be named accordingly.
- A Check now action would need an authenticated executor and a bounded,
  allowlisted diagnostic contract. A web dashboard cannot directly run a local
  CLI. A re-authentication action should open the appropriate secure provider
  flow; automatic reconnection is provider-specific and does not mean silently
  granting or widening access. These are ideas for a later slice, not features
  included in this checkpoint.

Preserve this baseline commit before media revisions. Use subsequent commits
and the established feature-branch review process for improvements.

## Brain and dispatch plan — October 23, 2026

Use [PROJECT_BRAIN.md](PROJECT_BRAIN.md) as the restart point, the
[roadmap](ROADMAP.md#october-23-media-workstream) for sequence, and
[SLICES.md](SLICES.md#october-23-media-slice-contracts) for ILL-05–08 contracts.
This planning setup does not dispatch implementation agents or accept the draft media.

## Ownership correction — October 23, 2026

Tucker requested that Canary work move to its own project. Canary owns diagnostic
runs/captures, status/history, Check now and re-authentication planning; see
[Canary draft PR #1](https://github.com/jtwray/agent-toolchain-canary/pull/1).
Portfolio ILL-06 only requests/imports approved media. This supersedes any earlier
suggestion that the portfolio brain should direct Canary execution or product work.
