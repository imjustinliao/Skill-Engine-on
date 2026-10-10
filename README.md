# Ignition Sequence Start

**Set up your project once. Every coding agent can continue it after that.**

You describe what you want to build, one short step at a time. The agent writes it down in your repo, plans it with you, and only then starts coding. When you open a new chat or switch to another agent, it picks up exactly where you left off.

Works with Claude Code, Codex, Cursor, Gemini CLI, Grok, GitHub Copilot, and most other coding agents.

## 1. Install

```bash
npx skills add imjustinliao/Skill-Ignition-Sequence-Start
```

Pick your agent when asked. Other ways to install are listed further down.

## 2. Start

Open your project folder (new or existing) in your agent and type:

```text
ignition sequence start
```

The agent asks a few short questions, one topic at a time:

1. How you like to work
2. What you're building and why
3. What it should do
4. Your preferences (commits, approvals, tools)
5. How it should look
6. The plan

Answer in a few words, paste notes you already have, or say **"skip"**. Nothing is built until you approve the plan.

In a hurry? Type `ignition sequence start, express` and you only describe the goal and the features.

## 3. Keep going

After setup, just talk to your agent normally. These phrases also work in any agent, any time:

| Say | What happens |
|-----|--------------|
| **continue** | Picks up where the last session stopped |
| **status** | Where things stand and what's waiting on you |
| **handoff** | Saves progress before you close the chat or switch agents |
| a numbered list of fixes | Each fix is tracked and reported back one by one |
| **new feature: …** | Added to the plan before any code is written |
| **change …** | Updates anything from setup, for example *"change the plan: do login first"*, *"update the design: darker colors"*, *"change my rules: commit when tests pass"* |
| **help** | Shows this list |

That's it. The rest is optional.

---

## Your project's docs

Everything you share during setup is written into plain Markdown files in your project, and the agent keeps them up to date as you build:

```
AGENTS.md          how agents work on this project (read automatically)
docs/product.md    your goal: what, why, for whom
docs/spec.md       what it should do, as a checklist
docs/design.md     how it should look and feel
docs/progress.md   the plan, where things stand, decisions made
docs/feedback.md   your requests and their status
docs/research.md   what was looked into, with sources
```

Small projects get only `AGENTS.md`, `spec.md`, `progress.md` and `feedback.md`.

You can read and edit these files yourself at any time. The next agent follows your version.

<details>
<summary><b>Run several agents in parallel</b></summary>

After the plan is approved, ask for it, for example: *"run M3 and M4 in parallel"*.

The agent checks the work splits cleanly, sets up shared contracts and rules for who edits what, and gives you one prompt per agent. Each agent works on its own branch and reports back when done. The first agent merges everything and reviews it with you. Two to four agents at once works best.

</details>

<details>
<summary><b>Other ways to install</b></summary>

**Claude Code plugin**

```text
/plugin marketplace add imjustinliao/Skill-Ignition-Sequence-Start
/plugin install ignition-sequence-start@skill-ignition-sequence-start
```

**Manual:** copy `skills/ignition-sequence-start/` into your agent's skills folder.

| Agent | Folder |
|-------|--------|
| Claude Code | `~/.claude/skills/` |
| Codex, Cursor, Gemini CLI, Grok, Copilot, OpenCode, Goose, Amp, and most others | `~/.agents/skills/` |

**Claude apps:** zip the `ignition-sequence-start` folder and upload it under Customize › Skills.

**Agents without skill support** (such as Aider): ask the agent to read `skills/ignition-sequence-start/SKILL.md` from this repo and follow it.

</details>

<details>
<summary><b>If an agent doesn't pick up where you left off</b></summary>

Paste this into the agent. It works even without the skill installed:

```text
Continue this project. Read AGENTS.md and docs/progress.md, check git, then tell me in three lines where things stand and what's next.
```

</details>

<details>
<summary><b>Customize it</b></summary>

Fork this repo and edit:

- `skills/ignition-sequence-start/assets/templates/AGENTS.md`: default rules, approvals, commit format
- `skills/ignition-sequence-start/references/intake.md`: the setup questions

</details>

<details>
<summary><b>How the skill is organized</b></summary>

```
skills/ignition-sequence-start/
├── SKILL.md         entry point: picks what to do from your repo and your words
├── references/      detailed guides, loaded only when needed
├── assets/          templates copied into your project, plus prompts
└── scripts/         scaffold.py, which copies templates without overwriting
```

</details>

## License

[MIT](LICENSE) © 2026 Justin Liao
