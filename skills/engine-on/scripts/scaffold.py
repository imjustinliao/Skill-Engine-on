#!/usr/bin/env python3
"""Copy the Engine-on doc templates into a project without overwriting anything.

Usage:
    python3 scaffold.py <project-dir> [--name "Project"] [--parallel] [--dry-run]

Creates AGENTS.md, CLAUDE.md, docs/{product,spec,design,research,progress,feedback}.md
and references/README.md. --parallel also adds docs/parallel-plan.md and
docs/milestones/TEMPLATE.md. Existing files are never touched; they are listed as
"kept" so the agent can merge by hand. {{PROJECT_NAME}} and {{DATE}} are filled in;
every other {{PLACEHOLDER}} is left for the agent to fill during intake.

Standard library only (Python 3.8+).
"""

import argparse
import datetime
import pathlib
import sys

TEMPLATES = pathlib.Path(__file__).resolve().parent.parent / "assets" / "templates"

CORE = [
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
PARALLEL = [
    "docs/parallel-plan.md",
    "docs/milestones/TEMPLATE.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("project_dir", type=pathlib.Path)
    parser.add_argument("--name", help="project name for {{PROJECT_NAME}}")
    parser.add_argument("--parallel", action="store_true", help="also add the parallel-work templates")
    parser.add_argument("--dry-run", action="store_true", help="list what would happen, write nothing")
    args = parser.parse_args()

    root = args.project_dir.resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 1

    replacements = {"{{DATE}}": datetime.date.today().isoformat()}
    if args.name:
        replacements["{{PROJECT_NAME}}"] = args.name

    created, kept = [], []
    for relative in CORE + (PARALLEL if args.parallel else []):
        source = TEMPLATES / relative
        target = root / relative
        if target.exists():
            kept.append(relative)
            continue
        text = source.read_text(encoding="utf-8")
        for key, value in replacements.items():
            text = text.replace(key, value)
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        created.append(relative)

    prefix = "would create" if args.dry_run else "created"
    for relative in created:
        print(f"{prefix}: {relative}")
    for relative in kept:
        print(f"kept (already exists, merge by hand): {relative}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
