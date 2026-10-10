# The build loop

After the plan is approved, every milestone and every review round goes through the same loop. It is slow in the right places (before code is written, before work is called done) and fast everywhere else.

## Contents

- The loop
- Verification gate
- Presenting results
- Feedback rounds
- Commits and approval modes
- Sign-off and drift
- Versioning

## The loop

1. **Re-read** `docs/progress.md` and the milestone's requirement IDs.
2. **Plan the milestone** in a few lines (what, files, risks). For a new milestone, get approval; inside an approved milestone, proceed.
3. **Implement** in focused changes. Nothing unrelated.
4. **Verify** (gate below).
5. **Present** results and **stop** for feedback.
6. **Commit** per the approval mode.
7. **Update** `docs/progress.md` (and `docs/feedback.md`, `docs/design.md` if they changed).

## Verification gate

"Done" means all of these, checked by the agent itself, not left to the owner:

- It builds, with no new warnings.
- The tests pass. Read the result line (for example `TEST SUCCEEDED`, `0 failed`) instead of assuming. Never chain a push after the test command; look first.
- It was run and looked at: screenshots of every screen touched (both themes if there are two), CLI output, API responses, whatever the product shows. Compare with `docs/design.md` and `references/`.
- Interactions were exercised, not just rendered (tap, swipe, drag, type), because gesture and focus bugs only show under input.
- Anything that cannot be checked here (real device, haptics, sensors, payments, third-party accounts) is listed as unverified and added to Blockers.

If something fails, fix it or report it plainly with the output. Never present unverified work as done.

## Presenting results

Keep it short and checkable:

- What changed, per feedback ID or requirement ID: done, partly done (what's missing), or not done (why).
- Verification: build, tests, what was looked at, what could not be checked.
- Screenshots or output for what the owner should look at.
- Then the question the approval mode requires, or "pushed as <version>".

## Feedback rounds

Owners often send many requests in one message and add more while you work. To make sure nothing is lost:

1. Split the message into items and add each to `docs/feedback.md` with an ID (`FB-012`), in the owner's words, before starting.
2. Mid-work additions get their own IDs; finish or park the current item cleanly first.
3. Work through them; when two conflict, ask.
4. Report per ID. Mark done items with the commit.

Encourage numbered lists from the owner ("1. … 2. …") and screenshots labelled by item number; say so once, kindly, not every round.

## Commits and approval modes

The mode lives in `AGENTS.md` › Git. Only the owner changes it.

- **`ask`**: after verification, summarize and ask: improve further, commit only, or commit and push. Wait.
- **`commit-on-green`**: after the gate passes, commit and push, then report. Typical once the owner says "push once done" or "you can push without asking". Record the switch as a decision with the date.

Every commit, either mode: stage only project paths (never machine-specific files); check `git diff --cached` for secrets and local settings; one logical change per commit; never force-push or rewrite published history.

## Sign-off and drift

- **Sign off each milestone** against its requirement IDs before calling it done: every acceptance item met, met in the owner's newer form, or listed as a gap. Read-only audit subagents, one per milestone, make this quick.
- **Review rounds drift.** After several rounds of ad-hoc fixes, the spec falls behind what the owner now wants and requirements quietly slip. Every few rounds, or when the owner asks "where are we?", give a short status: what is signed off, what changed since, what was skipped, which open questions are still unanswered. Then fold the owner's newer decisions back into `docs/spec.md` and `docs/design.md`.
- **Re-ask unanswered questions** at these checkpoints instead of letting them sit in Blockers forever.

## Versioning

With the `MAJOR.MINOR.PATCH - What changed` format:

- **PATCH**: fixes, visual refinements, small improvements.
- **MINOR**: a new feature, screen, or capability (reset patch to 0). Long refinement phases tend to drift into "everything is a patch"; a new screen or behavior the user can see is a minor bump.
- **MAJOR**: a product generation, breaking change, or release milestone.
- Each commit gets the next unused version after `git log`. Parallel sessions use their reserved ranges.
- A commit version is not an app or package release version; do not change those unless the owner asks.
