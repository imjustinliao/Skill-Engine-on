# Resume prompt

For the owner to paste into any agent (a different tool, a fresh session, or after a context reset). It works without the skill installed, because everything it needs is in the repository. Most agents run this check on their own at session start (it is in `AGENTS.md`); use the prompt when one does not.

```text
Continue this project. Read AGENTS.md and docs/progress.md, check git, then tell me in three lines where things stand and what's next.
```

Short form for agents that already load AGENTS.md automatically:

```text
Resume from docs/progress.md.
```
