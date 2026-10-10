# AGENTS.md

Shared instructions for every coding agent working on {{PROJECT_NAME}}. Keep this file short; details live in `docs/`.

## Project snapshot

- **{{PROJECT_NAME}}**: {{ONE_LINE_DESCRIPTION}}
- **Scope**: {{SCOPE}} <!-- e.g. "frontend only; the backend is built separately" -->
- **Stack**: {{STACK}}
- **Layout**:
  - `{{SOURCE_DIR}}/`: application source. Only shipping code and assets go here.
  - `docs/`: product, spec, design, research, progress.
  - `references/`: screenshots and visual assets for inspiration. Never ship these.

## Start of every session (every agent)

Do this before the first task, without being asked:

1. Read `docs/progress.md`: current status, next action, work in flight, decisions, blockers.
2. Check `git status` and `git log -5`. If git disagrees with `progress.md`, trust git and correct `progress.md`. If the owner edited the docs since the last session, follow their version.
3. If this file still has template placeholders (names in double curly braces), setup is unfinished: ask the owner to fill them before building.
4. Read only what the task needs: `docs/product.md`, `docs/spec.md`, `docs/design.md`; `references/README.md` for visual work; `docs/parallel-plan.md` if you are a parallel session.
5. Orient the owner. For a greeting, "continue" or "where were we": three lines (phase, last done, next action) plus any discrepancies. For a specific task: one line of orientation, then the task.

## Owner shortcuts

| The owner says | Do |
|----------------|----|
| "status", "where are we" | Summarize: phase, signed off, in progress, open feedback IDs, skipped items, questions waiting on the owner. |
| "handoff", "wrap up", "switching agents" | Update `docs/progress.md` (status, next action, in flight, session log), commit finished work if the approval mode allows, and report anything left uncommitted. |
| A list of changes or fixes | Add each to `docs/feedback.md` with an ID first, then work through them and report per ID. |
| New features | Add them to `docs/spec.md` (and `docs/design.md`) with IDs, propose milestones, get approval before building. |
| "change …", "update …" (goal, a feature, the design, the plan, these rules) | Edit the document where it lives (`docs/product.md`, `docs/spec.md`, `docs/design.md`, `docs/progress.md`, or this file), summarize what changed and what it affects, and get approval if it adds work or reorders the plan. |
| "I'll be away", "keep going" | Agree the boundary (which IDs, commit mode), stay inside it, queue questions in Blockers, leave a short report. |
| "help" | List these shortcuts in plain words: continue, status, handoff, a numbered list of fixes, new feature, change, help. |

## Workflow

1. Understand the requirement and inspect the existing code.
2. Research the relevant technologies and best practices.
3. Propose a plan with milestones and acceptance criteria (requirement IDs from `docs/spec.md`).
4. **Stop: get the owner's approval before implementing.**
5. Implement one approved milestone at a time.
6. Verify: build, test, and check the result yourself (see Verify).
7. **Stop: present results (with screenshots or output) and get feedback before the next milestone.**
8. Follow the Git rules below.
9. Update `docs/progress.md` before ending the session.

## Working principles

- Think before coding. State assumptions; surface contradictions or gaps in the docs instead of guessing.
- Prefer the simplest maintainable solution. No speculative abstractions or layers "for later".
- Make focused changes. Do not modify, reformat, or "clean up" unrelated code.
- Verify against explicit acceptance criteria. Report anything unmet, skipped, or unverified.
- Use subagents for independent research or reviews when it saves context or time.
- Match the existing code style and use the platform's current APIs.
- Feedback items get IDs in `docs/feedback.md`; report each one as done, partly done, or not done.

## Scope

{{SCOPE_RULES}} <!-- e.g. "Use realistic mock data behind clear interfaces where the backend is unavailable. Record backend needs in docs/progress.md › External dependencies." -->

## Do not, without explicit approval

- Change the tech stack, architecture, or deployment target.
- Add third-party dependencies.
- Change signing, credentials, identifiers, capabilities, or CI.
- Delete files or rewrite git history.

## Verify

```bash
# Build
{{BUILD_COMMAND}}

# Test
{{TEST_COMMAND}}
```

{{VISUAL_CHECK}} <!-- e.g. "Launch the app, screenshot every screen the change touched, compare with docs/design.md and references/." -->

Done means: builds with no new warnings, tests pass, and the result was checked by running it. Things only a person or a real device can check go in `docs/progress.md` › Blockers.

## Git

### Approval mode: **{{APPROVAL_MODE}}**

- `ask`: after each change, summarize what changed and whether verification passed, then ask: **improve further**, **commit only**, or **commit and push**? Wait for the answer.
- `commit-on-green`: once the verification gate passes, commit and push without asking, then report. Never push on a failed or unfinished gate.

Only the owner changes the mode. In either mode: never force-push, never rewrite published history, never merge to the main branch from a parallel session.

### Commit message

{{COMMIT_FORMAT}}

### Never commit

Secrets, tokens, `.env` files, personal signing or machine-specific settings, build output. Check `git diff --cached` before every commit.

## Handoff

Another agent or a fresh session may continue from where you stop, with nothing but these files. Before you stop, or when your context is running low:

1. Update `docs/progress.md` › Current status: phase, next action, and **in flight** (branch, uncommitted files, half-done steps).
2. Commit finished work if the approval mode allows; otherwise, or if work is unfinished, list exactly what is uncommitted and why.
3. Add one line to the session log.

## Record keeping

`docs/progress.md` is a handoff note, not a diary: current status, milestone changes, decisions (date, decision, why, rejected alternatives), blockers, one short session-log line. Prune it when it grows.
