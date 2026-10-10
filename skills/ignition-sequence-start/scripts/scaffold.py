#!/usr/bin/env python3
"""Copy the Ignition Sequence Start templates into a project without overwriting anything.

Usage:
    python3 scaffold.py <project-dir> [--name NAME] [--light] [--parallel] [--gemini] [--aider] [--no-claude] [--dry-run]

Full setup (default): AGENTS.md, CLAUDE.md, docs/{product,spec,design,research,progress,feedback}.md
and references/README.md.
--light     Small projects: AGENTS.md, CLAUDE.md, docs/spec.md, docs/progress.md, docs/feedback.md.
--parallel  Adds docs/parallel-plan.md and docs/milestones/TEMPLATE.md.
--gemini    Adds GEMINI.md, a pointer to AGENTS.md for Gemini CLI.
--aider     Adds .aider.conf.yml, which loads AGENTS.md into Aider.
--no-claude Skips CLAUDE.md (only needed by Claude Code).
--dry-run   Lists what would be created and writes nothing (safe during step 0).

Existing files are never modified; they are reported as "kept" so they can be merged by hand.
{{PROJECT_NAME}} (with --name) and {{DATE}} are filled in; other placeholders are left for the
agent to complete during intake. Requires only the Python 3.8+ standard library.
"""

import argparse
import datetime
import pathlib
import sys

TEMPLATES = pathlib.Path(__file__).resolve().parent.parent / "assets" / "templates"

FULL = [
    "AGENTS.md",
    "CLAUDE.md",
    "docs/product.md",
    "docs/spec.md",
    "docs/design.md",
    "docs/research.md",
    "docs/progress.md",
    "docs/feedback.md",
    "references/README.md",
]
LIGHT = [
    "AGENTS.md",
    "CLAUDE.md",
    "docs/spec.md",
    "docs/progress.md",
    "docs/feedback.md",
]
PARALLEL = [
    "docs/parallel-plan.md",
    "docs/milestones/TEMPLATE.md",
]
GEMINI = ["GEMINI.md"]
AIDER = [".aider.conf.yml"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_dir", type=pathlib.Path, help="root of the project to set up")
    parser.add_argument("--name", help="project name used for {{PROJECT_NAME}}")
    parser.add_argument("--light", action="store_true", help="minimal setup for small projects")
    parser.add_argument("--parallel", action="store_true", help="add the parallel-work templates")
    parser.add_argument("--gemini", action="store_true", help="add a GEMINI.md pointer file")
    parser.add_argument("--aider", action="store_true", help="add an .aider.conf.yml that reads AGENTS.md")
    parser.add_argument("--no-claude", action="store_true", help="skip CLAUDE.md")
    parser.add_argument("--dry-run", action="store_true", help="list actions without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_dir.resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 1
    if not TEMPLATES.is_dir():
        print(f"error: templates not found at {TEMPLATES}", file=sys.stderr)
        return 1

    files = list(LIGHT if args.light else FULL)
    if args.parallel:
        files += PARALLEL
    if args.gemini:
        files += GEMINI
    if args.aider:
        files += AIDER
    if args.no_claude:
        files.remove("CLAUDE.md")

    replacements = {"{{DATE}}": datetime.date.today().isoformat()}
    if args.name:
        replacements["{{PROJECT_NAME}}"] = args.name

    created, kept = [], []
    for relative in files:
        target = root / relative
        if target.exists():
            kept.append(relative)
            continue
        text = (TEMPLATES / relative).read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        created.append(relative)

    verb = "would create" if args.dry_run else "created"
    for relative in created:
        print(f"{verb}: {relative}")
    for relative in kept:
        print(f"kept (already exists, merge by hand): {relative}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
