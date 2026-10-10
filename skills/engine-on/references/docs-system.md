# The docs system

Every file has one job. Together they let any agent, in any tool, start cold and do the right next thing. The rule of thumb: **if it only exists in the chat, it does not exist.**

## Contents

- The files
- Keeping them small
- One instruction file, many agents
- What goes where

## The files

| File | Job | Changes when |
|------|-----|--------------|
| `AGENTS.md` | Rules for every agent: snapshot, read order, workflow, principles, scope, verify, git, handoff. | The owner changes a rule. |
| `CLAUDE.md` (and other pointer files) | Point an agent's native instruction file at `AGENTS.md`. | Never, once made. |
| `docs/product.md` | What, why, goal, users, success, non-goals. | Rarely. |
| `docs/spec.md` | Requirements with stable IDs and acceptance items; ambiguities and open questions. | The owner adds or decides something. |
| `docs/design.md` | The owner's vision and design requirements; the approved design direction (current truth). | Direction changes: rewrite in place. |
| `docs/research.md` | Dated findings and recommendations with sources. | New research. |
| `docs/progress.md` | Current status, next action, in flight, milestones, decisions, blockers, external dependencies, short session log. | Every session. |
| `docs/feedback.md` | Owner review requests with IDs and status. | Every review round. |
| `docs/parallel-plan.md` | Waves, branches, ownership, contracts, report-back. | Only when working in parallel. |
| `docs/milestones/<m>.md` | One report per parallel milestone. | When a session finishes. |
| `references/README.md` | Index of visual references with cross-cutting patterns first. | New references. |

## Keeping them small

Every session pays to read these files, so size is a cost. Budgets that held up in practice:

- `AGENTS.md` under ~150 lines. It holds rules, not knowledge.
- `docs/progress.md` under ~200 lines: keep the ~15 latest decisions and ~10 latest session-log lines; move older ones to `docs/archive/` (create it when first needed).
- `docs/design.md`: the Design direction is current truth. Rewrite it when the owner changes something; do not append "(owner, date): now it's X" paragraphs. Git keeps history.
- `references/README.md`: the cross-cutting patterns (5–10 bullets) are what agents read; detailed entries are lookup only.
- Milestone reports are historical once merged; say so at the top of `progress.md` so agents do not treat them as current.

When a file outgrows its budget, propose a prune to the owner in one line, then do it.

## One instruction file, many agents

`AGENTS.md` is the single source of rules. Other agents get a pointer, never a copy, so rules cannot drift apart:

| Agent | What it reads | What to create |
|-------|---------------|----------------|
| Codex, Cursor, GitHub Copilot, Windsurf, Amp, OpenCode, Jules, Zed, Aider, and most others | `AGENTS.md` natively | nothing |
| Claude Code | `CLAUDE.md`; recent versions also read `AGENTS.md`, but only when no `CLAUDE.md` exists | `CLAUDE.md` containing `@AGENTS.md` (works in every version, and leaves room for Claude-only notes) |
| Gemini CLI | `GEMINI.md` by default | `GEMINI.md` containing `@AGENTS.md`, or `"context": {"fileName": ["AGENTS.md", "GEMINI.md"]}` in `.gemini/settings.json` |
| Anything else | whatever it loads | a one-line pointer: "Follow AGENTS.md." |

Create only the pointers for agents the owner actually uses (ask in step 0). Some agents cap instruction files (Codex reads at most 32 KiB of `AGENTS.md` by default), another reason to keep it short. Agent support changes often; when unsure, check the agent's current docs instead of assuming.

Personal, machine-specific preferences (local paths, a personal simulator, editor settings) do not belong in `AGENTS.md`. They go in the agent's local or user-level settings, which are not committed.

## What goes where

| Thing | Where |
|-------|-------|
| A new requirement or an owner decision about behavior | `docs/spec.md` (dated) |
| A design change | `docs/design.md` › Design direction (rewritten in place) |
| Why we chose X over Y | `docs/progress.md` › Decisions |
| "Please fix / change …" from a review | `docs/feedback.md` |
| Something we wait on (backend, assets, accounts, legal) | `docs/progress.md` › External dependencies or Blockers |
| A new rule for how agents work | `AGENTS.md` |
| What happened this session | one line in `docs/progress.md` › Session log |
| Facts learned from research | `docs/research.md` |
