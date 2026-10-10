# Situations and edge cases

How to handle the cases the main flow does not cover directly. Find the closest match, apply it, and record anything unusual in `docs/progress.md` › Decisions.

## Contents

- Starting
- Project shape
- People and permissions
- Tools and environments
- During the project
- Parallel work

## Starting

| Situation | Handling |
|-----------|----------|
| Empty folder, no git | In step 0, offer `git init` and a minimal runnable project from the platform's official template. Ask for the stack; never choose it for the owner. |
| Code exists, no agent docs | Kickoff. Infer the stack, commands and structure from the code; mark inferred facts "(inferred; confirm)" and ask about them in one batch. |
| Agent files from another system (`CLAUDE.md`, `.cursor/rules`, `copilot-instructions.md`, a long README) | Adopt: merge their rules into `AGENTS.md`, turn the old files into pointers, keep anything project-specific. Show the owner what moved where. |
| The owner pastes everything in one message | Split it across the files, then confirm each file in turn. |
| "Skip the questions, just build" | Express kickoff (`intake.md` › Express kickoff): defaults for rules and conventions, goal and spec only, one plan approval. State every assumption. |
| The setup command is run again on a configured project | Resume instead. Offer to revisit a specific step; never re-scaffold over existing files. |
| The owner's request contradicts the docs | Point out the contradiction and ask which wins; then update the losing document. |

## Project shape

| Situation | Handling |
|-----------|----------|
| Tiny project (a script, a prototype, a weekend tool) | Light setup (`--light`): `AGENTS.md`, `docs/spec.md`, `docs/progress.md`, `docs/feedback.md`. Skip design, research and references unless asked. |
| Monorepo or several apps | One root `AGENTS.md` with shared rules; a short nested `AGENTS.md` per package for its own commands and conventions (most agents read the nearest file). One `docs/` at the root, with spec areas per package. |
| Not an app (library, API, CLI, data pipeline, infrastructure) | Same flow. "Run it and look" means calling the API, running the CLI, inspecting output or a plan; design may be API or interface design instead of visual design. |
| Backend owned by someone else | Record the boundary in `AGENTS.md` › Scope. Build against mocks behind clear interfaces and log every need in `docs/progress.md` › External dependencies. |
| Public repository | Reference images are often someone else's work: keep them out of the repo (gitignore `references/` except its README) or link to them instead. Never commit private notes about people or customers. |

## People and permissions

| Situation | Handling |
|-----------|----------|
| Several people direct the work | Record who decided what (`(Name)` instead of `(owner)`). Prefer a branch per milestone with pull requests. Personal settings stay out of shared files. |
| No push rights, or no remote | Commit locally, say so in the report, and keep a note in In flight. |
| The owner gives terse approvals | Read back the scope of each approval. Treat "what you suggest" as approval of the stated default only. |
| The owner is unavailable for a while | Away mode (`workflow.md` › Away mode). |
| An approval is needed from someone other than the owner | Ask the owner to obtain it; never act on a relayed or assumed approval. |

## Tools and environments

| Situation | Handling |
|-----------|----------|
| The agent cannot run scripts | Copy templates from `assets/templates/` by hand. |
| The agent has no subagents | Do research and reviews sequentially; keep each pass short. |
| The agent cannot message other sessions | Parallel sessions finish by asking the owner to paste their report into the coordinator. |
| The agent cannot run or view the product | Build and test, then list what still needs a person to check, under Blockers. Never present it as verified. |
| A tool or SDK is missing | Stop at step 0 (or as soon as found), tell the owner the exact install command, and continue with what does not depend on it. |
| Switching between tools mid-project | Add the new tool's pointer file if it does not read `AGENTS.md` natively (`docs-system.md`). Nothing else changes. |
| The agent does not support skills (for example Aider) | Point it at this skill's `SKILL.md` once for setup. Afterwards the project's `AGENTS.md` carries the workflow, so no skill is needed. |
| Another tool's rules file shadows `AGENTS.md` | Some agents read only the first instruction file they find (Zed prefers `.rules`). Merge that file into `AGENTS.md` and remove it, or reduce it to a pointer. |

## During the project

| Situation | Handling |
|-----------|----------|
| Requirements change mid-milestone | Update `docs/spec.md` (dated), re-check the milestone's acceptance items, and tell the owner what the change costs before continuing. |
| A new batch of features after the plan | New scope (`workflow.md` › New scope). |
| Feedback rounds keep going without sign-off | Status check (`workflow.md` › Sign-off and drift), then fold the decisions back into the spec. |
| Context is about to be compacted or the session must end | Hand off (`handoff.md` › Leaving) before it happens. |
| A secret was committed | Stop and tell the owner at once: the secret must be revoked or rotated. Rewriting history needs their explicit approval. |
| A test fails right before a push | Do not push. Fix it, or report the failure with its output. |
| The docs have grown large | Prune (`docs-system.md` › Keeping them small) and tell the owner in one line. |
| Two agents are open on the same checkout | One writer per working tree (`handoff.md` › Two agents at once). |

## Parallel work

| Situation | Handling |
|-----------|----------|
| The owner asks for session prompts before the project is ready | Readiness checklist (`parallel.md` › Asked for prompts before the project is ready). |
| A session needs a contract change | It adds an adapter in its own folder and requests the change in its report; the coordinator applies it. |
| A session goes quiet or crashes | Give the owner a nudge prompt: resume in the same worktree, finish the current step, write the report, push, report back. |
| Two sessions built the same thing | Keep one during the consistency pass, move it to the shared location, and point both features at it. |
| A merge conflicts | The coordinator resolves it on the main branch, runs the full gate, and notes the cause in the Merge log so the ownership map can be tightened. |
| The machine slows down | Pause a wave. Fewer sessions finishing beats many sessions stalling. |
