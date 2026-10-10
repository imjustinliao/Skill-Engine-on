# Intake: one step at a time

The intake turns what is in the owner's head (or in their notes) into files any agent can work from. It runs as nine short steps. Each step asks for one thing, writes it down, shows the owner what was captured, and moves on only when they agree.

## Contents

- How every step works
- Step 0: Inspect and agree the setup
- Step 1: Workflow and rules
- Step 2: Product goal
- Step 3: Specification
- Step 4: Conventions
- Step 5: First commit
- Step 6: Design and references
- Step 7: Research
- Step 8: Milestone plan
- Fast paths and edge cases

## How every step works

1. **Ask for one thing.** Say which step this is ("Step 3: the spec", of steps 0–8), what you need, and the two ways to give it: paste what they already have, or answer a few short questions. Many owners arrive with prepared documents; take them whole.
2. **Capture faithfully.** Keep the owner's wording and hierarchy. Reorganize for clarity, never for meaning: do not drop, merge away, or "improve" a requirement. Interpretation goes in the Ambiguities table, not into the requirement.
3. **Ask follow-ups as one numbered batch.** Number every question (`1.`, `2.`, …) and make each answerable in a few words, offering the likely options. Owners often reply tersely in order ("yes; no, single; later; what you suggest"). Map answers by number, read back any you had to interpret, and treat "what you suggest" as approval of your stated default. File every answer where it belongs before moving on; an answered question that never reaches the docs gets asked again later, and owners notice.
4. **Write the file, then show a short summary** of what it now says and what is still open.
5. **Tick the step** in `docs/progress.md` › Intake and set **Next action**, so a different agent or a fresh session can pick up mid-intake.
6. **Gate.** Do not start the next step, and never start implementing, until the owner agrees. "ok", "approve", "next" all count. When a short approval follows a message that asked several things, say what you take it to cover ("I'm reading 'approve' as the plan and the font choice, not the commit"), and never treat it as covering more.

The owner can say "skip" or "later" for any step: mark it `- [~] later` in Intake and continue. They can also hand over several steps in one message: process them in order, still one file at a time, and confirm each.

## Step 0: Inspect and agree the setup

- Inspect without changing anything: languages and frameworks, build and test commands, folder layout, existing docs and agent files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`), git status, branches, remote, CI.
- Check the toolchain actually works: the build runs, required SDKs, runtimes, simulators or emulators, and services are installed. A missing tool found now costs minutes; found mid-milestone (or by several parallel sessions at once) it costs hours. Read-only checks are fine; installing dependencies, downloading toolchains or anything networked needs the owner's yes, so ask as part of step 0.
- Note where docs and references must live so the build never picks them up (some project types compile or bundle everything inside the source folder).
- Propose the setup: which Engine-on files you will create (see `docs-system.md`), what you will keep or merge, and anything odd you noticed (secrets in the tree, no `.gitignore`, uncommitted work).
- Step 0 needs only two answers: **may I create the skeleton**, and **which agents will you use** (decides the pointer files; default: the current one). Ask anything else only if it blocks the setup.
- **Write nothing until the owner approves.** Then create the skeleton: `python3 <skill-dir>/scripts/scaffold.py <project> --name "<Name>"` (add `--parallel` only when parallel work is planned), or copy from `assets/templates/` by hand if Python is not available. The script never overwrites; merge "kept" files by hand.
- If the repo has no runnable app yet (empty, or only a stub), offer to scaffold a minimal runnable project from the platform's current official template first, so step 6 onward has something to verify against. Do not pick a stack on the owner's behalf: ask.

## Step 1: Workflow and rules

Show the default workflow and principles from the `AGENTS.md` template in a few lines and ask what to change. Common edits: approval gates, who reviews, whether subagents may be used, what "verified" means for this project.

Write: `AGENTS.md` (Workflow, Working principles, Handoff). Keep it short; details belong in `docs/`.

## Step 2: Product goal

Ask for: what they are building, why, the goal, what makes it different, target users, success metrics, non-goals. If they paste a goal statement, keep its voice; add only the missing headings as open questions.

Write: `docs/product.md`.

## Step 3: Specification

Ask for the requirements in whatever shape they have (outline, bullet list, user stories). Tell them more can be added later.

- Give every requirement a stable ID by area (`ONB-01`, `HOME-03`, `API-02`, `CLI-04`). The listed items become acceptance criteria (`- [ ]`).
- Preserve their hierarchy and words. Then re-read the source against the file and confirm nothing was dropped; owners notice when a sub-bullet goes missing.
- Collect **Ambiguities** (wording with more than one reading, each with the possible readings), **Assumptions** you had to make, and **Open questions** (missing information) in tables at the bottom.
- Ask the most important ones now as one numbered batch; leave the rest to the milestone that needs them, with a proposed default.

Write: `docs/spec.md`. Answers go into the requirement (dated) and the item leaves the table.

## Step 4: Conventions

One numbered batch:

1. **Commit format.** Offer the default `MAJOR.MINOR.PATCH - What changed` (1–15 words, no period, unique version each commit; patch for fixes and polish, minor for new features, major for big releases; start at 0.0.1), or Conventional Commits, or theirs.
2. **Approval mode.** `ask` (summarize, then ask improve / commit / commit and push) or `commit-on-green` (commit and push whenever the verification gate passes). Most owners start with `ask` and switch later; write down when they do.
3. **Branching.** Work on main, or a branch per milestone with PRs.
4. **Scope.** What this agent builds and what others own (for example "frontend only; the backend is built separately: use mocks behind clear interfaces and log backend needs").
5. **Build, test and run commands**, and the default device, browser, or environment for checks.
6. **Hard limits.** Dependencies, stack changes, signing, deletions: which need approval.

Write: `AGENTS.md` (Git, Scope, Verify, Do not), `docs/progress.md` (decisions).

## Step 5: First commit

Review everything to be committed: secrets, tokens, `.env`, personal or machine-specific settings (signing teams, local paths, IDE state), large binaries, duplicated instructions. Propose a `.gitignore` if missing. Suggest the message (for example `0.0.1 - Establish project documentation and agent workflow`) and **commit and push only with the owner's explicit yes.** Report the hash, branch, and push result.

## Step 6: Design and references

Ask for the design brief: the feeling, principles, style name if any, themes, typography, motion, accessibility needs, and reference images or links. Also ask what is still to come (logo, fonts, assets) and note it under Pending from owner.

- Save images to `references/` with descriptive kebab-case names. They are inspiration, never shipped and never copied.
- With many references, analyze them in parallel (subagents, a few images each) and write one entry per file: what it shows, what to borrow (mapped to requirement IDs), what to avoid. Then distill the **cross-cutting patterns** at the top of `references/README.md`; agents read that, not every entry.
- Requirements from the brief get `DES-NN` IDs. The researched, approved direction is written later under **Design direction**.

Write: `docs/design.md`, `references/README.md`.

## Step 7: Research

Derive the open technical and design questions from the spec and the design brief (platform APIs, libraries, patterns, licensing, performance, accessibility). Research them in parallel where the agent can (one subagent per topic, each returning a sourced summary), then synthesize. Check facts against current official docs; note dates. Propose, do not decide: anything that changes the stack or adds a dependency goes to the owner.

If the owner wants to move faster ("just plan and iterate"), cut research to the questions that block the first milestones.

Write: `docs/research.md`, and the approved **Design direction** in `docs/design.md`.

## Step 8: Milestone plan

Propose milestones (`M0` setup, `M1` foundations, then features), each with: scope, requirement IDs, acceptance criteria, how it will be verified, dependencies, and risks. Order them so the first one produces something runnable. Mark which milestones could run in parallel once a shared base and contracts exist (see `parallel.md`), and say what that costs.

**Get explicit approval.** Then set Phase to Building in `docs/progress.md`, remove the Intake section, and start M1 (or the parallel plan).

## Fast paths and edge cases

- **"Use defaults" / no time:** fill steps 1 and 4 with the defaults, ask only for the product goal and the spec, and say what was assumed.
- **One big brief:** split it across the files yourself, then confirm each file in turn.
- **Existing project with history:** run step 0 thoroughly, write the docs from the code and the owner's answers, and mark inferred facts "(inferred; confirm)".
- **Existing agent files:** merge into `AGENTS.md` and turn the others into pointers (see `docs-system.md`); never silently discard someone's rules.
- **The owner adds things out of order** (a haptics idea during the design step): write it where it belongs now, say where, and continue the current step.
