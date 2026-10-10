# Handoff: switching agents and sessions

Projects outlive any single conversation. Context windows fill and get summarized, owners switch between tools (Claude Code, Codex, Cursor, Gemini CLI, Copilot and others), and several sessions may work at once. This skill makes all of these the same event: **the next agent reads the files and continues.**

Arriving needs no command. The project's `AGENTS.md` (loaded automatically by every agent, directly or through a pointer file) tells each new session to run the arrival check below. Leaving needs one word from the owner, or the agent's own judgment when context runs low.

## Contents

- Leaving: the handoff note
- Arriving: the resume protocol
- Switching tools
- Two agents at once
- Context compaction
- Signs the docs are stale

## Leaving: the handoff note

When the owner says "handoff", "wrap up" or that they are switching agents, when context is running low, or before ending a session:

1. `docs/progress.md` › Current status:
   - **Phase** and **Active milestone**.
   - **Next action**: one concrete step, and whether the owner already approved it.
   - **In flight**: branch, uncommitted files, half-done steps, background jobs, anything a newcomer would trip over. "none" when clean.
2. Finish the current logical change and commit it if the approval mode allows (in `ask` mode, ask). Anything left uncommitted goes in In flight with the reason.
3. Open feedback items are in `docs/feedback.md` with their status.
4. One session-log line: date, agent, version, what happened.

Write it for a stranger: no "as discussed", no references to the chat.

## Arriving: the resume protocol

1. Read `AGENTS.md`, then `docs/progress.md`.
2. `git status`, `git log -5`, current branch.
3. Run the arrival checklist:
   - Does git match progress.md (last commit, branch, In flight)? Does the last commit's content match its message?
   - Are there unfilled `{{PLACEHOLDERS}}` in `AGENTS.md` (stack, build and test commands, approval mode, commit format)? Those are unfinished intake steps (usually 1 and 4); offer to finish them before building, since nothing can be verified without them.
   - Do the active milestone's requirement IDs exist in `docs/spec.md` with acceptance items? If the spec, product or design files are still empty templates, intake steps 2, 3 or 6 never happened: say so and offer to run them.
   - Is there an unfinished Intake checklist? If the section is missing but Phase is Intake, rebuild it from the files that exist.
   - Concretely: compare `git show --stat HEAD` with its message, and look in `git status` for untracked source folders that should have been committed.
   - If the approval mode in `AGENTS.md` is blank, treat it as `ask`.
4. Read only the docs the next action needs.
5. Reply according to the first message:
   - **A greeting, "continue", "where were we":** three lines (phase, what was last done, next action and anything in flight), then a short **Discrepancies** list if the checklist found any, with numbered questions.
   - **A specific task:** one line of orientation ("Picking this up during M3; the main branch is clean"), any discrepancy that affects the task, then the task within the current approvals. A small fix or question proceeds. A new feature or behavior is new scope (`workflow.md` › New scope): capture it and propose where it fits; it does not displace an already-approved next action unless the owner says so.
   - **The owner cannot reply right now** (an unattended run): ask the numbered questions once, make no assumptions beyond recorded defaults, and leave the questions in Blockers.

On arrival you may fix plain factual slips in `docs/progress.md` (a branch name, a missing session-log line) and say so; anything that changes meaning, scope or a decision, ask first. "Where were we?" asks for the status, not for work: wait for a go even if the next action was approved earlier. "Continue" or "go" starts the approved next action.

If an agent skips the arrival check, the prompt in `assets/prompts/resume.md` triggers it explicitly. It works even where this skill is not installed, because `AGENTS.md` carries the protocol.

## Switching tools

- All rules live in `AGENTS.md`; each tool gets only a pointer file (`docs-system.md` › One instruction file, many agents). Adding a tool mid-project means adding its pointer, nothing else.
- Keep tool-specific state out of the docs (session IDs, local paths, a personal device name). If a tool needs it, it goes in that tool's local settings.
- Different tools have different abilities (subagents, messaging, browsers, simulators). Docs describe *what* to verify; each agent picks *how*. If an agent cannot verify something it should, it says so in the report and Blockers.

## Two agents at once

Two agents writing to the same checkout overwrite each other's work and confuse each other's git state. When the owner has more than one agent open on a project:

- Give each writer its own worktree and branch (`git worktree add ../<repo>-<name> -b <branch>`), or keep all but one read-only (reviewing, researching, answering questions).
- If both must change code at once, it is parallel work: set it up properly (`parallel.md`).

## Context compaction

When the conversation is summarized, details not written down are at risk. Before it happens (or right after, if it already did): make sure exact commands, IDs, debug flags, device names, and gotchas the next steps depend on are in the docs or the session notes, not only in the summary. Recurring project knowledge (how to launch a debug screen, a flaky test) goes in `AGENTS.md` or `docs/research.md`; one-off state goes in In flight.

## Signs the docs are stale

- progress.md's Next action is already done in git.
- A milestone is "in progress" with no commits for a long time.
- Decisions contradict the current code.
- The owner corrects something the docs state.

Fix the docs first, then continue. Stale docs mislead every agent that comes after.
