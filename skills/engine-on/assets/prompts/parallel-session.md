# Parallel session prompt

Fill one copy per session and give it to the owner to paste into a new agent session. Self-contained: the session has none of the coordinator's context.

```text
You are the {{M}} session for {{PROJECT_NAME}} ({{one line}}, repo "{{REPO_PATH}}"). {{N}} sessions run in parallel off the same base; a coordinating session named "{{COORDINATOR_NAME}}" merges everything. Milestone: {{M}} {{Title}} ({{requirement IDs}}).

## Ground rules (owner-approved for this session)
- Plan and implement {{M}} end to end without stopping for approval. Choose sensible defaults for open questions and record them in your report. Commit to YOUR branch and push YOUR branch only. Never push to or merge into {{MAIN_BRANCH}}, never force-push, never rewrite history, never touch other branches.
- Read first: AGENTS.md, docs/parallel-plan.md (MANDATORY: ownership map, contracts, conflict rules), docs/spec.md, docs/design.md, docs/research.md, and the existing code in {{shared folders}}.
- Isolation: `git fetch origin`. If you are in the shared checkout, run `git worktree add "../{{repo}}-{{m}}" -b milestone/{{slug}} origin/{{MAIN_BRANCH}}` and work ONLY there. If you already run in your own worktree, `git switch -c milestone/{{slug}} origin/{{MAIN_BRANCH}}`.
- Your own resources: {{port / simulator / build cache / database}}. Never use another session's.
- Use the contracts as they are. Do NOT edit: {{read-only paths}}.
- Never merge or rebase {{MAIN_BRANCH}} into your branch; the coordinator integrates.
- Don't start large fan-outs of your own (other sessions share this machine); a few focused subagents are fine.
- Quality: no new warnings; tests for your logic in {{test path}}; check your own result ({{screenshots / output}}) before reporting.

## Scope: you own {{paths}}
- {{deliverable 1}}
- {{deliverable 2}}
- Defaults to record: {{ambiguity IDs → suggested defaults}}

## When done
1. Write docs/milestones/{{m}}.md (template in docs/milestones/TEMPLATE.md).
2. Commit with your reserved versions ({{first version}}, then the next patch…), format from AGENTS.md. Push: `git push -u origin milestone/{{slug}}`.
3. Report: if you can message other sessions, send "{{COORDINATOR_NAME}}" a message whose first line is "{{M}} done: milestone/{{slug}} pushed at <hash>", followed by the report summary. Otherwise tell the owner: "Paste docs/milestones/{{m}}.md into {{COORDINATOR_NAME}}."
4. Stop. Don't start other milestones.
```
