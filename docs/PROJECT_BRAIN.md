# Brain — Portfolio evidence and STAR stories

_Initialized: October 23, 2026. Owner: Tucker Wray._

## Authority and current state

This central conversation is the project brain: product direction, bounded assignments,
scope checks, review decisions and handoffs stay here. Temporary agents implement or
review a single assigned slice. This file is the durable restart point; the
[roadmap](ROADMAP.md) and [slice contracts](SLICES.md) hold scope and acceptance.

Repository: `jtwray/portfolio-illustrated`. Current planning branch:
`feat/project-media-review`, draft [PR #3](https://github.com/jtwray/portfolio-illustrated/pull/3).
The original 49-file package is preserved at commit
`59081a1c3d9dc4bfe1055db3eaf7f3e48f268b54` and described in
[the checkpoint](PROJECT_MEDIA_REVIEW.md). Its assembled HTML has not passed browser QA.
The checkpoint is a recoverable draft, not an accepted or published portfolio release.

| Queue | Work | State |
| --- | --- | --- |
| Now | Establish the brain, bounded contracts and handoff templates | Planning setup recorded; no implementation agent active |
| Next | ILL-05 — Dashboarda screenshots | First candidate for dispatch after the preflight below |
| Next | ILL-06 — Import approved Canary media | Depends on Canary-owned CAN-01; no CLI execution assigned here |
| Next | ILL-07 — Revised stories and media review | After both capture slices |
| Next | ILL-08 — Case-study integration | After editorial acceptance and branch/PR reconciliation |
| Next | ILL-04 — Release QA | After integration; reuse the existing QA slice |
| External | Canary execution evidence and product roadmap | Owned by the Canary project; [draft PR #1](https://github.com/jtwray/agent-toolchain-canary/pull/1) |
| Needs reconciliation | ILL-01–03 and other open portfolio change requests | October 19 status text is historical; do not assume current completion |

Tucker's ownership decision: the Canary project plans and reviews CLI execution,
status/history, Check now and provider re-authentication. This brain requests an
approved evidence export and integrates it; it does not assign Canary implementation
or probe runs. Later Canary product work is not a portfolio prerequisite.

Before first dispatch, inspect current main, open PRs and any applicable AGENTS.md.
Reconcile existing contact/proof/link gates and resume-menu change requests with this
workstream; record evidence and a concrete base branch. Do not silently mark earlier
gates complete or overwrite another portfolio's migration roadmap.

## Roles and cycle

- **Tucker + brain:** choose one bounded slice; approve intent, contribution wording,
  material scope changes and final merge/publication. The brain maintains the queue.
- **Temporary dev** (`d — ILL-xx`): implement only the contract, verify outputs, make
  logical commits and return exact branch/commit/artifact references.
- **Temporary reviewer** (`r — ILL-xx`): independently inspect the actual committed
  files and outputs against acceptance criteria; do not rely on the dev report alone.
- **Git/PR handoff:** the brain or a bounded chores agent prepares the reviewable PR
  after acceptance. Tucker's merge/publication gate remains explicit.

Assign → implement and commit → brain sanity check → independent review → specific
rework if needed → verify the revised commit → Tucker acceptance → next slice.

The brain may immediately return an obvious scope error or unsupported claim to the
dev, or an out-of-scope demand to the reviewer. Future enhancements are backlog items;
they are not acceptance blockers. Review the changed output after rework. There is
only one implementation slice active at a time; do not launch the whole roadmap.

## Branch and persistence contract

Start a fresh `feat/ill-xx-...` branch from current main after prerequisites are
available there. For unmerged prerequisites, the brain must explicitly name a
stacked base, PR target and dependency. Never guess or force-push a shared branch.
Use the shared repository/workspace and preserve unrelated work.

Keep the original `docs/project-media-review/` package and its baseline manifest
unchanged; place revised assets/drafts in `docs/project-media-updates/`.
Commit at meaningful boundaries and before every review. A commit in scratch alone
is not the durable handoff: push the feature branch and confirm its remote SHA.
If push is blocked, return the exact blocker and recovery location; do not claim it
is saved remotely. Do not merge, publish or change production from an agent brief
unless that action has been separately authorized.

## Dev handoff template

The brain fills every bracket before dispatch and includes the full slice contract.
Return this prompt to Tucker for a separate temporary chat, or launch one temporary
agent when Tucker has requested in-session delegation.

> You are `d — [slice ID]`, a temporary implementation agent for Tucker's portfolio.
> Repository: jtwray/portfolio-illustrated. Workspace: [absolute checkout path].
> Approved base: [branch + full SHA]; work branch: [feat/...]; PR base: [branch].
> Read docs/PROJECT_BRAIN.md and applicable AGENTS.md. Your entire scope is:
> [paste the chosen slice's goal, inputs, allowed files, exclusions and done criteria].
> Inspect the actual files. Implement only that scope. Preserve the original package
> and unrelated work. Record observed evidence and exact limitations. Run relevant
> checks and commit meaningful changes before review. Push and verify the remote
> branch if authorized by this assignment. Do not merge or publish.
> Return: branch/base/head SHA, changed files, criterion-by-criterion results,
> commands/check results, artifact/preview links, known gaps and exact review steps.
> If blocked, report the smallest missing input; do not fabricate a successful result.

## Reviewer handoff template

> You are `r — [slice ID]`, an independent temporary reviewer for Tucker's portfolio.
> Repository/workspace: [repo + absolute checkout path].
> Review base: [full SHA]; implementation branch and head: [branch + full SHA].
> Contract: [paste the exact accepted criteria and exclusions].
> Read docs/PROJECT_BRAIN.md and applicable AGENTS.md. Inspect the actual diff and
> artifacts at that head; independently run the relevant app/output checks.
> Do not edit the implementation or merge/publish. Judge only the assigned scope.
> Return PASS, CHANGES REQUESTED or BLOCKED, with a result and evidence for each
> criterion. Every blocker must cite a file/output and give a minimal correction and
> verification step. Separate optional future work. State anything you could not test.

## Handoff record template

For each assignment, append a short record here or link a committed report:
slice ID; accepted contract; dev/reviewer identity or chat link; base/branch/head;
artifact/preview links; checks; decision; unresolved gaps; next action.
Record the commit actually reviewed. A new head requires review of relevant changes.
