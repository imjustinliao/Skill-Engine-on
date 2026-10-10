---
name: ignition-sequence-start
description: Sets up and runs a software project for coding agents from the first message to the last. Interviews the owner one step at a time (workflow, product goal, spec, conventions, design, research, milestone plan) before any code is written, and writes a small docs system (AGENTS.md plus docs/ for product, spec, design, research, progress, feedback) that lets any agent, in any tool or fresh session, resume exactly where work stopped. Also handles handoffs, status checks, new scope, review rounds, subagents, and parallel agents coordinated through frozen contracts, ownership maps, isolated worktrees and report-back files. Use when the user says "ignition sequence start", starts or bootstraps a project, wants AGENTS.md, project docs, a workflow or milestones set up, brings an existing repo under an agent workflow, asks where things stand, is switching agents, sessions or context, adds a new batch of features, or wants work split across subagents or parallel agents.
license: MIT
compatibility: Any coding agent that can read files and run shell commands (Claude Code, Codex, Cursor, Gemini CLI, Grok Build, GitHub Copilot, OpenCode, Cline, Goose and others). Python 3 is optional, for the scaffold script.
metadata:
  author: Justin Liao
  version: "0.2.0"
---

# Ignition Sequence Start

This skill prepares a project for coding agents before anything is built, then keeps it moving across sessions, tools and parallel workers. It rests on two ideas:

1. **Intake before implementation.** Collect one thing at a time (rules, goal, spec, conventions, design, research, plan), write it down, confirm it, then move on. Code starts only after the owner approves a plan, because mistakes are cheapest before code exists.
2. **The repository is the memory.** Rules live in `AGENTS.md`; knowledge and status live in `docs/`. Every agent loads `AGENTS.md` at the start of a session, so after setup a new session or a different tool resumes on its own, with or without this skill installed.

The skill is needed for setup, for adding scope, and for parallel work. Day-to-day sessions run from the project's own `AGENTS.md`.

## Route the request

Look at the project root and the owner's message. **Modes combine:** whenever project docs exist, run the arrival check first (`references/handoff.md` › Arriving) and lead with its short status, then route the request itself with the table below.

Paths in this skill are relative to its own directory, the folder containing this `SKILL.md`. If that location is unknown, find it by searching the agent's skill folders for `ignition-sequence-start/SKILL.md`.

| Situation or phrase | Do this | Details |
|---------------------|---------|---------|
| "Ignition sequence start" with no `AGENTS.md` or `docs/progress.md` (empty repo, only a README, or code with no agent docs) | **Kickoff** | Kickoff below, `references/intake.md` |
| `docs/progress.md` has an unfinished Intake checklist | **Continue intake** at the first open step | `references/intake.md` |
| Project docs exist; new session, new agent, "where were we", "continue" | **Resume** | `references/handoff.md` › Arriving |
| "Handoff", "wrap up", "switching to another agent", context running low | **Hand off** | `references/handoff.md` › Leaving |
| "Status", "where are we", "what was skipped" | **Status check** | `references/workflow.md` › Sign-off and drift |
| A list of fixes or changes after a review | **Review round** | `references/workflow.md` › Feedback rounds |
| "Change …", "update …": the goal, a feature, the design, the plan, the rules or anything given during setup | **Revise** | `references/workflow.md` › Revising earlier decisions |
| "New features", a new batch of requirements after the plan | **New scope** | `references/workflow.md` › New scope |
| "I'll be away", "keep going without me" | **Away mode** | `references/workflow.md` › Away mode |
| Research, many files or images to read, an audit | **Subagents** | `references/parallel.md` › Subagents |
| "Run these in parallel", "give me prompts for other agents" | **Parallel** | `references/parallel.md` |
| Agent files or docs from another system | **Adopt** (kickoff that merges, never discards) | `references/intake.md` › Existing projects |
| "Help", "what can I say", "how do I use this" | **Show the cheat sheet** below | — |
| Anything unusual: monorepo, team, no git, tiny script, limited agent | **Check the edge cases** | `references/situations.md` |

If the situation is still unclear, say what you found and ask.

## Kickoff

Read `references/intake.md` first. If the owner asks for speed ("express", "skip the questions"), follow its Express kickoff.

Otherwise open with a short, plain message that a first-time user understands, then go straight into step 0. For example:

```text
Ignition sequence start. Before any code, we'll set this up together in a few short steps,
ending with a plan you approve. Answer in a few words, paste notes you already have, or say
"skip". First, let me look at what's here.
```

Every setup message stays short (about 150 words plus at most three numbered questions) and ends with what to type next, with an example answer ("You can reply: yes; just this one"). Avoid internal terms ("intake", "step 0", "scaffold", "pointer file", "stack") unless the owner uses them first. Adapt to the owner's experience (`references/intake.md` › Match the owner): someone new to coding gets plain words, recommended defaults and the short path. Step 0 writes nothing until the owner says yes.

| Step | Ask for | Writes |
|------|---------|--------|
| 0 | Nothing yet: inspect the repo, propose the setup and its size (full or light), ask which agents will be used | skeleton via `scripts/scaffold.py` |
| 1 | Workflow and rules (show defaults, ask what to change) | `AGENTS.md` |
| 2 | Product goal | `docs/product.md` |
| 3 | Specification | `docs/spec.md` (IDs, assumptions, ambiguities, open questions) |
| 4 | Conventions: commit format, approval mode, branching, scope, build and test commands, hard limits | `AGENTS.md`, `docs/progress.md` |
| 5 | Approval for the first commit, after a secrets and local-settings check | first commit |
| 6 | Design brief, references, pending assets | `docs/design.md`, `references/` |
| 7 | Research questions (derived from the spec and design; owner confirms) | `docs/research.md` |
| 8 | Approval of the milestone plan | `docs/progress.md` |

Rules for every step:

- **One step per message.** Offer two ways to answer: paste existing material, or answer a few short questions.
- **Capture faithfully.** Keep the owner's wording and hierarchy. Never drop or reinterpret a requirement; interpretations go in the Assumptions and Ambiguities tables.
- **Number every question** so short answers ("yes; no; later; what you suggest") map back cleanly. File every answer before moving on.
- **Record progress** in `docs/progress.md` › Intake after each step, so another agent can continue mid-intake.
- **Gate.** Wait for the owner before the next step. Never implement during intake. Commit and push only with explicit approval.

Scaffold with `python3 scripts/scaffold.py <project-dir> --name "<Name>"`. Options: `--light` for small projects, `--parallel` for parallel-work files, `--gemini` and `--aider` for those agents' pointer files (see `references/docs-system.md`), `--no-claude` to skip `CLAUDE.md` when Claude Code is not used, `--dry-run` to preview without writing anything. It never overwrites. Without Python, copy the files from `assets/templates/` by hand.

When the plan is approved, end setup with the cheat sheet below, so the owner knows how to work from here.

## Cheat sheet

Show this after setup and whenever the owner asks for help, in the owner's language:

```text
You're set up. From here, just talk to me normally. These also work in any agent:

  continue        pick up where we left off (new chat or another agent)
  status          where things stand and what's waiting on you
  handoff         save progress before closing the chat or switching agents
  1. … 2. …       a numbered list of fixes, each tracked and reported back
  new feature: …  added to the plan before any code
  change …        update anything from setup: goal, features, design, plan, rules
  help            show this list
```

## After the plan

Each milestone runs the same loop: re-read progress, plan briefly, implement focused changes, verify (build, tests, run it and look, exercise interactions), present results per requirement or feedback ID, stop for feedback, commit per the approval mode, update `docs/progress.md`. Details in `references/workflow.md`.

The approval mode is set by the owner in `AGENTS.md`: `ask` (summarize, then ask: improve further, commit only, or commit and push) or `commit-on-green` (commit and push whenever the verification gate passes). Push only after reading a passing test result, never chained blindly after the test command.

## Parallel work in brief

- **Subagents** (inside one session) fan out reading: research topics, reference images, audits, reviews. They return summaries; the main agent writes the docs.
- **Parallel sessions** (separate agents writing code) start only after a base and frozen contracts are on the main branch. Each session gets one milestone, its own branch, worktree and resources, an ownership map, reserved names and versions, a self-contained prompt, and a report it sends back. A coordinator merges, integrates, runs a consistency pass, gets the owner's sign-off and cleans up. Recommend 2–4 writers, sized to the machine.

Read `references/parallel.md` before proposing either.

## Files

- `references/intake.md`: steps 0–8, sizing, question banks, express kickoff, existing projects.
- `references/docs-system.md`: what each file is for, size budgets, pointer files per agent, what goes where.
- `references/workflow.md`: build loop, verification gate, feedback rounds, approval modes, new scope, away mode, sign-off, versioning.
- `references/handoff.md`: leaving, arriving, switching tools, two agents at once, context compaction.
- `references/parallel.md`: subagents, parallel sessions, readiness, contracts, isolation, reporting, merging.
- `references/situations.md`: edge cases and how to handle each.
- `assets/templates/`: files copied into projects (`AGENTS.md`, pointer files for Claude Code, Gemini CLI and Aider, `docs/`, `references/README.md`).
- `assets/prompts/`: `resume.md`, `parallel-session.md`.
- `scripts/scaffold.py`: copies the templates without overwriting.

## Principles

- **The owner's words are the source of truth.** Reorganize for clarity, never for meaning. Surface contradictions instead of resolving them silently.
- **Gates where mistakes are expensive**: before files are created, before code is written, before anything is pushed. Move quickly everywhere else.
- **Defaults, not menus.** Recommend one option with a reason; "what you suggest" approves it.
- **Approvals mean exactly what was approved.** Read a short "ok" back with its scope. Never assume or relay an approval the owner did not give.
- **Verify before reporting done**, by running and looking, not by assuming. State plainly what could not be checked.
- **Small docs.** Every session pays to read them. Rewrite current truth in place, prune logs, keep `AGENTS.md` short.
