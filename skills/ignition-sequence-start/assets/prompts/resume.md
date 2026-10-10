# Resume prompt

For the owner to paste into any agent (a different tool, a fresh session, or after a context reset). It works without the skill installed, because everything it needs is in the repository. Most agents run this check on their own at session start (it is in `AGENTS.md`); use the prompt when one does not.

```text
Continue this project. Read AGENTS.md, then docs/progress.md, then check `git status` and `git log -5`. Tell me in three lines: the phase, what was last done, and the next action (plus anything in flight or uncommitted). Then wait for my go, unless progress.md says the next action is already approved.
```

Short form for agents that already load AGENTS.md automatically:

```text
Resume from docs/progress.md.
```
