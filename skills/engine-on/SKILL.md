---
name: engine-on
description: Starts a software project properly in any coding agent before code is written. Interviews the owner one step at a time (workflow, product goal, spec, git and approval conventions, design and references, research, milestone plan) and writes a small docs system (AGENTS.md plus docs/ for product, spec, design, research, progress, feedback) so any agent or fresh session can resume where work stopped. Also plans subagent and parallel-agent work with frozen contracts, ownership maps, isolated worktrees and report-back files. Use when the user says "engine on", starts or bootstraps a project, wants AGENTS.md, project docs, a workflow or milestones set up before coding, brings an existing repo under agent workflow, switches agents or sessions and needs a handoff or resume, or wants to split work across parallel agents without losing quality.
license: MIT
metadata:
  author: Justin Liao
  version: "0.1.0"
---

# Engine-on

Engine-on gets a project ready for agents before anything is built, and keeps it ready across agents, sessions and parallel workers. It rests on two ideas:

1. **Intake before implementation.** Ask for one thing at a time (rules, goal, spec, conventions, design, research, plan), write it down, confirm it, then move on. Code starts only after the owner approves a plan. Mistakes are cheapest here.
2. **The files are the memory.** Everything that matters lives in the repo: `AGENTS.md` for rules, `docs/` for knowledge and status. Any agent in any tool can read them cold and continue; nothing depends on a chat that will be summarized or lost.

## Pick the mode

Look at the project root before saying anything else:

| You find | Mode | Go to |
|----------|------|-------|
| No `AGENTS.md` and no `docs/progress.md` (empty repo, or code with no agent docs) | **Kickoff** | Kickoff below |
| `docs/progress.md` with an unfinished Intake checklist | **Continue intake** at the first unchecked step | `references/intake.md` |
| `docs/progress.md` with Phase Building or Refining | **Resume** | `references/handoff.md` |
| Agent instructions or docs that Engine-on did not create | **Adopt**: kickoff, merging what exists | `references/intake.md` › Fast paths |
| The owner wants work split across agents | **Parallel** | `references/parallel.md` |

Modes combine. Whenever Engine-on docs exist, start with the resume check (`references/handoff.md` › Arriving) and lead your reply with its short status, then handle what the owner asked. If the mode is still unclear, say what you found and ask.

Paths below are relative to this skill's directory (the folder containing this `SKILL.md`).

## Kickoff

Read `references/intake.md` first. Open with one short message: what Engine-on will do, that it takes nine short steps (0–8), and that nothing is implemented until the plan is approved. Then start step 0. Step 0 writes nothing until the owner says yes.

| Step | Ask for | Writes |
|------|---------|--------|
| 0 | Nothing: inspect the repo, propose the setup, wait for a yes | skeleton (via `scripts/scaffold.py`) |
| 1 | Workflow and rules (show defaults, ask what to change) | `AGENTS.md` |
| 2 | Product goal | `docs/product.md` |
| 3 | Specification | `docs/spec.md` (IDs, ambiguities, open questions) |
| 4 | Conventions: commit format, approval mode, branching, scope, build/test commands, hard limits | `AGENTS.md`, `docs/progress.md` |
| 5 | Approval for the first commit (after a secrets and local-settings check) | first commit |
| 6 | Design brief, references, pending assets | `docs/design.md`, `references/` |
| 7 | Research questions (derived; owner confirms) | `docs/research.md` |
| 8 | Approval of the milestone plan | `docs/progress.md` |

Rules for every step (details and question banks in `references/intake.md`):

- **One step per message.** Offer two ways to answer: paste what they have, or answer a few short questions.
- **Capture faithfully.** Keep the owner's wording and hierarchy; never drop or reinterpret a requirement. Interpretations go to the Ambiguities table.
- **Number every question** so terse answers ("yes; no; later; what you suggest") map back cleanly. Read back anything you had to interpret.
- **Tick the step** in `docs/progress.md` › Intake and set Next action after each one, so another agent can take over mid-intake.
- **Gate.** Wait for the owner's go before the next step. Never implement during intake. Commit and push only with explicit approval.

Scaffold with `python3 <this-skill>/scripts/scaffold.py <project-dir> --name "<Name>"` (`--parallel` adds the parallel-work files; `--dry-run` previews). It never overwrites. Without Python, copy the files from `assets/templates/`.

## After the plan: the build loop

Each milestone: re-read progress → plan briefly → implement focused changes → verify (build, tests, run it and look, exercise interactions) → present per requirement or feedback ID → stop for feedback → commit per the approval mode → update `docs/progress.md`. Review requests go into `docs/feedback.md` with IDs before work starts, so none are missed. Details: `references/workflow.md`.

Approval modes, set by the owner in `AGENTS.md`: `ask` (summarize, then ask: improve further, commit only, or commit and push) or `commit-on-green` (commit and push whenever the verification gate passes). Push only after reading a passing test result, never chained blindly after the test command.

## Switching agents and sessions

Before stopping or when context runs low, update `docs/progress.md` › Current status (phase, next action, **in flight**) and the session log. On arrival, read `AGENTS.md` then `docs/progress.md`, check git, and tell the owner the phase, the last thing done and the next action in three lines. `AGENTS.md` is the single rules file; other tools get a one-line pointer (`CLAUDE.md` holds `@AGENTS.md`). The resume prompt in `assets/prompts/resume.md` works in any agent, even without this skill. Details: `references/handoff.md`.

## Subagents and parallel agents

- **Subagents** (same session): fan out independent reading work (research topics, reference images, code review) and synthesize. They return summaries; the main agent writes the docs.
- **Parallel agents** (separate sessions writing code): only after a base and frozen contracts are on the main branch. Each session gets one milestone, its own branch and worktree, its own ports, devices and caches, an ownership map, reserved names and version ranges, a self-contained prompt, and a report file it sends back to the coordinator. The coordinator merges, integrates, runs a consistency pass, gets the owner's sign-off and cleans up. Recommend 2–4 writers, sized to what the machine can run.

Read `references/parallel.md` before proposing parallel work; it covers when not to, the contract and wave setup, the session prompt (`assets/prompts/parallel-session.md`) and the merge procedure.

## Files

- `references/intake.md`: the nine steps, question banks, fast paths, adopting existing repos.
- `references/docs-system.md`: what each file is for, size budgets, pointer files per agent, what goes where.
- `references/workflow.md`: the build loop, verification gate, feedback rounds, approval modes, versioning.
- `references/handoff.md`: leaving and arriving, switching tools, context compaction, stale docs.
- `references/parallel.md`: subagents, parallel sessions, contracts, isolation, reporting, merging.
- `assets/templates/`: `AGENTS.md`, `CLAUDE.md`, `docs/*.md`, `docs/milestones/TEMPLATE.md`, `references/README.md`.
- `assets/prompts/`: `resume.md`, `parallel-session.md`.
- `scripts/scaffold.py`: copies the templates into a project without overwriting.

## Principles

- **The owner's words are the source of truth.** Reorganize for clarity, never for meaning. Surface contradictions instead of resolving them silently.
- **Gates where mistakes are expensive**: before files are created, before code is written, before anything is pushed. Speed everywhere else.
- **Defaults, not menus.** Offer one recommended option with a reason, and accept "what you suggest" as approval of it.
- **Approvals mean exactly what was approved.** Read a short "ok" back with its scope; never relay or assume an approval the owner did not give.
- **Verify before saying done**, by running and looking, not by assuming. Say plainly what could not be checked.
- **Small docs.** Every session pays to read them. Rewrite current truth in place; prune logs; keep `AGENTS.md` short.
