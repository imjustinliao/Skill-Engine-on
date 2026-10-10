# Subagents and parallel agents

Parallel work buys speed with coordination cost. Done well, several milestones land in the time of one, with no merge conflicts. Done carelessly, you get duplicated components, inconsistent behavior, a choking machine, and a long cleanup. This file is the careful version.

## Contents

- Two kinds of parallelism
- Subagents: fan out reading, keep writing central
- Should this run in parallel?
- Asked for prompts before the project is ready
- 1. Land the base and freeze the contracts
- 2. Write the parallel plan
- 3. Write one prompt per session
- 4. While sessions run
- 5. Merge, integrate, review
- 6. Sign-off and cleanup
- Parallel fixes during review rounds

## Two kinds of parallelism

| | Subagents | Parallel sessions |
|--|-----------|-------------------|
| What | Helpers inside one session | Separate agent sessions, often separate tools or windows |
| Good for | Research, reading many files or images, reviews, audits | Building independent milestones |
| Writes code? | Rarely; when they do, in an isolated worktree | Yes, each on its own branch and worktree |
| Context | Gets a brief, returns a summary | Gets a self-contained prompt, returns a report file |
| Coordination | The main agent synthesizes | A named coordinator session merges |

## Subagents: fan out reading, keep writing central

- Give each subagent one independent question and everything it needs; it does not share your history.
- Ask for a structured, sourced summary in return, with a length limit. The main agent writes the docs.
- Good fan-outs: one per research topic; a few reference images each; one read-only auditor per milestone checking requirement IDs; independent critics (accessibility, platform guidelines, performance) before a merge.
- One research pass, then plan. If the owner says "just plan and iterate", stop researching.
- When a subagent must write code (parallel fixes during review rounds), give it an isolated worktree and the same rules a parallel session gets, and merge its result yourself.

## Should this run in parallel?

Say yes only if all of these hold:

- The plan is approved and the milestones touch **different files**. Overlap means conflicts, or one milestone silently re-building another's UI.
- What they share can be pinned down as **contracts** before anyone starts.
- The machine can take it. Each session runs its own builds, tests, devices or servers; six sessions with their own simulators overloaded a fast laptop in practice. Recommend **2–4 writers**, in waves if there are more.
- Someone, the coordinator plus the owner, has time to merge and review what comes back.

If not, run milestones one after another, and use subagents for research and review only. Say what you recommend and why; the owner may still choose more. Then make it as safe as you can.

To size it, check the machine (`nproc` or `sysctl -n hw.ncpu`, and free memory). As a rough guide, each session that runs its own builds, tests and a simulator or dev server wants about two cores and several GB of memory, on top of the coordinator.

## Asked for prompts before the project is ready

Owners in a hurry often ask for the session prompts straight away. Do not hand out prompts that cannot work; a session without contracts or acceptance criteria will guess, and three sessions guess three different ways. Check readiness, then offer the shortest path to it:

- [ ] The milestones are approved and each has acceptance items in `docs/spec.md`.
- [ ] `AGENTS.md` has real build, test and verify commands (no `{{PLACEHOLDERS}}`).
- [ ] The main branch is clean: work in flight on the active milestone is committed, parked on a branch, or becomes one of the parallel sessions.
- [ ] The base and contracts are on the main branch, with tests.
- [ ] `docs/parallel-plan.md` is committed.

Say what is missing as a numbered list, propose to do the missing pieces yourself right now (most take one focused pass), and give the prompts as soon as the list is done. If the owner is short on time, ask only the questions that block the base and use stated defaults for the rest.

## 1. Land the base and freeze the contracts

Before any session starts, the coordinator puts on the main branch:

- **Shared foundations** every milestone needs (design tokens, base components, app shell entry point, domain models).
- **Contracts**: the interfaces sessions code against: types and protocols, navigation or routes, API and data schemas, events, stores, plus **mock or simulated implementations** so every session can run its part alone.
- **Tests for the contracts.** They catch broken shared code once, instead of six times.
- A **toolchain check**: build tools, SDKs, simulators or runtimes, services, all present. A missing tool discovered by six sessions at once is six blocked sessions.

Push the base, record its version, and name the coordinating session (for example "Main") so sessions can address it. Only then tell the owner to launch sessions.

## 2. Write the parallel plan

Scaffold `docs/parallel-plan.md` (`scaffold.py --parallel`) and fill it:

- **Waves and sessions**: milestone, branch `milestone/<slug>`, worktree folder, reserved commit versions, and the isolated resources each session gets (ports, simulators or emulators, build caches, databases, `.env` copies).
- **Ownership map**: which paths each milestone may edit; everything shared (contracts, foundations, entry point, dependency manifests, `docs/` except its own report, `AGENTS.md`) belongs to the coordinator. Name any single-line exceptions explicitly.
- **Reserved names** per milestone (types, routes, tables, CSS classes) so two sessions cannot create the same thing.
- **Rules**: new shared pieces go in your own folder under a specific name (the coordinator promotes them); contract changes are requested in the report, never made; temporary edits to shared files for local viewing are reverted before every commit; never merge or rebase the main branch into your branch; never push to main.
- **Quality bar and report template** (`docs/milestones/TEMPLATE.md`).

Commit the plan to the main branch before sessions start, so every session reads the same rules.

## 3. Write one prompt per session

Fill `assets/prompts/parallel-session.md` once per session. Each prompt must stand alone: the session has none of the coordinator's context. It states:

- The owner's pre-approval: plan and implement end to end without stopping for approval, commit and push **its own branch only**, record defaults instead of asking. Without this, every session stops and waits for the owner.
- What to read first, the isolation commands, its resources, what it must not edit.
- Its scope, deliverables, and the ambiguity defaults to use.
- Not to start large fan-outs of its own (they multiply machine load).
- How to finish: report file, reserved versions, push, report back with the first line `<M> done: <branch> pushed at <hash>`, or ask the owner to paste the report; then stop.

Give the owner the prompts with plain instructions: open N new sessions, paste one prompt each, come back to the coordinator.

## 4. While sessions run

- Watch for reports. Agents that can message each other (for example Claude Code's `ListAgents` and `SendMessage`) report directly; otherwise the owner pastes `docs/milestones/<m>.md` into the coordinator.
- Broadcast rule changes to every session at once when something shared changes (a newly discovered build blocker, a clarified contract).
- Answer contract questions with explicit conditions, and record them in the plan.
- **Never relay an approval the owner did not give.** If a session asks for something only the owner can approve, ask the owner.
- For a session that went quiet, give the owner a short nudge prompt: finish the current step, write the report, push, report back.

## 5. Merge, integrate, review

For each finished branch, in dependency order where possible:

1. Merge into the main branch (a merge commit, using the next free version).
2. Run the full verification gate: build, all tests, run it and look.
3. Wire it in as a **separate commit**, following the report's integration steps.
4. Promote shared components the session built locally, and apply requested contract changes yourself.
5. Record the merge in the plan's Merge log.

After all merges, run a **consistency pass**: duplicated components, diverging behavior for the same state, features nobody asked for, mismatched styles. Independent reviewers (subagents) are good at finding these. Then bump the version to the next **minor** above every reserved range (for example `0.8.0 - Integrate M2–M7`), so the main branch does not stay stuck inside the last session's range.

## 6. Sign-off and cleanup

- **Sign-off per milestone with the owner**, against requirement IDs. Read-only audit subagents, one per milestone, can check the spec item by item and list gaps. Update the spec to the owner's latest decisions before more ad-hoc fixes pile up.
- **Clean up** once merged: remove worktrees (`git worktree remove`), delete merged branches (ask before deleting remote ones), shut down and delete the extra simulators, servers, and caches the sessions created.
- Update `docs/progress.md`: milestone statuses, decisions, the next action. Mark milestone reports as historical.

## Parallel fixes during review rounds

When a review round has several independent areas, the coordinator can run them as background subagents in isolated worktrees:

- Write one shared brief file: the owner's feedback verbatim with IDs, plus rules for every agent (owned paths, own device or port, one commit with no push, what to return: branch and hash, changes per feedback ID, interpretations, screenshots, test results, decisions needed).
- Merge (squash is fine) and version on the main branch yourself; run the gate after each.
- If the owner prefers it done in the main session, do that; parallelism is a tool, not a rule.
