# Handoff: switching agents and sessions

Projects outlive any single conversation. Context windows fill and get summarized, owners switch between tools (Claude Code, Codex, Cursor, Gemini, Copilot…), and several sessions may work at once. Engine-on makes all of these the same event: **the next agent reads the files and continues.**

## Contents

- Leaving: the handoff note
- Arriving: the resume protocol
- Switching tools
- Context compaction
- Signs the docs are stale

## Leaving: the handoff note

Before stopping, when context is running low, or before the owner says they're switching:

1. `docs/progress.md` › Current status:
   - **Phase** and **Active milestone**.
   - **Next action**: one concrete step, and whether the owner already approved it.
   - **In flight**: branch, uncommitted files, half-done steps, background jobs, anything a newcomer would trip over. "none" when clean.
2. Finish or commit the current logical change. If something stays uncommitted on purpose, say what and why in In flight.
3. Open feedback items are in `docs/feedback.md` with their status.
4. One session-log line: date, agent, version, what happened.

Write it for a stranger: no "as discussed", no references to the chat.

## Arriving: the resume protocol

1. Read `AGENTS.md`, then `docs/progress.md`.
2. `git status`, `git log -5`, current branch.
3. Run the arrival checklist:
   - Does git match progress.md (last commit, branch, In flight)? Does the last commit's content match its message?
   - Are there unfilled `{{PLACEHOLDERS}}` in `AGENTS.md` (stack, build and test commands, approval mode, commit format)? Those are unfinished intake steps (usually 1 and 4); offer to finish them before building, since nothing can be verified without them.
   - Do the active milestone's requirement IDs exist in `docs/spec.md` with acceptance items?
   - Is there an unfinished Intake checklist? If the section is missing but Phase is Intake, rebuild it from the files that exist.
4. Read only the docs the next action needs.
5. Reply with three lines (phase, what was last done, next action and anything in flight), then a short **Discrepancies** list if the checklist found any, with numbered questions.

On arrival you may fix plain factual slips in `docs/progress.md` (a branch name, a missing session-log line) and say so; anything that changes meaning, scope or a decision, ask first. "Where were we?" asks for the status, not for work: wait for a go even if the next action was approved earlier. "Continue" or "go" starts the approved next action.

The owner can trigger this in any agent with the prompt in `assets/prompts/resume.md`; it works even where Engine-on is not installed, because `AGENTS.md` carries the protocol.

## Switching tools

- All rules live in `AGENTS.md`; each tool gets only a pointer file (`docs-system.md` › One instruction file, many agents). Adding a tool mid-project means adding its pointer, nothing else.
- Keep tool-specific state out of the docs (session IDs, local paths, a personal device name). If a tool needs it, it goes in that tool's local settings.
- Different tools have different abilities (subagents, messaging, browsers, simulators). Docs describe *what* to verify; each agent picks *how*. If an agent cannot verify something it should, it says so in the report and Blockers.

## Context compaction

When the conversation is summarized, details not written down are at risk. Before it happens (or right after, if it already did): make sure exact commands, IDs, debug flags, device names, and gotchas the next steps depend on are in the docs or the session notes, not only in the summary. Recurring project knowledge (how to launch a debug screen, a flaky test) goes in `AGENTS.md` or `docs/research.md`; one-off state goes in In flight.

## Signs the docs are stale

- progress.md's Next action is already done in git.
- A milestone is "in progress" with no commits for a long time.
- Decisions contradict the current code.
- The owner corrects something the docs state.

Fix the docs first, then continue. Stale docs mislead every agent that comes after.
