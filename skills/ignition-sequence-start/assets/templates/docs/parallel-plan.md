# Parallel plan

> {{DATE}}. The owner approved building {{MILESTONES}} in parallel sessions, coordinated by the session named **"{{COORDINATOR_NAME}}"**. Every parallel session follows this file. The coordinator merges each branch into `{{MAIN_BRANCH}}`, wires the pieces together, and runs a review pass with the owner per milestone.

## Base

Parallel work starts only after the base is on `{{MAIN_BRANCH}}` at `{{BASE_VERSION}}`: shared foundations plus the contracts below. Sessions build against `{{MAIN_BRANCH}}` and the contracts, never against another session's unmerged code.

## Waves

| Wave | Milestones | Starts |
|------|------------|--------|
| 1 | {{M_A}} · {{M_B}} · {{M_C}} | after base `{{BASE_VERSION}}` |

## Sessions

| Milestone | Branch | Versions | Worktree | Isolated resources |
|-----------|--------|----------|----------|--------------------|
| {{M_A}} | `milestone/{{m-a-slug}}` | `{{0.2.x}}` | `../{{repo}}-{{m-a}}` | {{port / simulator / build cache / database}} |

- One worktree and one branch per session: `git worktree add ../{{repo}}-<m> -b milestone/<slug> origin/{{MAIN_BRANCH}}`. If the agent already runs in its own worktree, `git switch -c milestone/<slug> origin/{{MAIN_BRANCH}}`.
- Anything two sessions could fight over gets one per session: dev-server ports, simulators or emulators, build caches, test databases, `.env` copies.
- Commits use the project format with the session's reserved versions only. Push only your own branch. Never push to `{{MAIN_BRANCH}}`, never merge, never force-push, never rebase published commits.

## Ownership map

Edit only what your milestone owns. Everything else is read-only. New files inside your own folders are always fine.

| Area | Owner |
|------|-------|
| Contracts, shared foundations, app entry point, dependency manifests, `docs/**` except `docs/milestones/`, `AGENTS.md` | **{{COORDINATOR_NAME}} only** |
| {{paths}} | {{M_A}} |
| tests for `<m>`, `docs/milestones/<m>.md` | that milestone |

- Need a shared component? Build it in your own folder under a specific name; the coordinator promotes it at merge.
- Need a contract change? Do not edit the contracts. Add an adapter or extension in your folder and describe the change in your report.
- Reserved names (types, routes, tables, CSS classes): create only your own.

## Contracts

Frozen interfaces every session codes against. Changes go through the coordinator.

| File | Provides | Used by |
|------|----------|---------|
| {{path}} | {{types, protocols, routes, schemas, events, mock implementations}} | {{milestones}} |

## Quality bar (every session)

- Builds with no new warnings; tests pass; the session checked its own result (screenshots or output) before reporting.
- Defaults chosen for open ambiguities are recorded in the report, not in `docs/spec.md`.

## Finish and report back

1. Write `docs/milestones/<m>.md` (template: `docs/milestones/TEMPLATE.md`), commit, `git push -u origin <branch>`.
2. Message the coordinator, if the agent can (for example `SendMessage` to "{{COORDINATOR_NAME}}"), with the first line `<M> done: <branch> pushed at <hash>`, then the report summary.
3. If messaging is not available, tell the owner: "Paste docs/milestones/<m>.md into {{COORDINATOR_NAME}}."
4. Stop. Do not start another milestone.

## Merge log (coordinator)

| Milestone | Merged at | Conflicts and fixes | Review |
|-----------|-----------|---------------------|--------|
