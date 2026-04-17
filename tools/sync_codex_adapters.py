#!/usr/bin/env python3
"""Generate Codex adapters for CCGS skills from the canonical .claude skills."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
AGENTS_SKILLS = ROOT / ".agents" / "skills"


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def list_skills() -> list[tuple[str, str, Path]]:
    skills: list[tuple[str, str, Path]] = []
    for path in sorted(CLAUDE_SKILLS.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        name = meta.get("name", path.parent.name)
        description = meta.get("description", f"Codex adapter for {name}.")
        skills.append((name, description, path))
    return skills


def render_skill(name: str, description: str, source: Path) -> str:
    rel_source = source.relative_to(ROOT).as_posix()
    return f"""---
name: {name}
description: "Codex adapter for the original CCGS `{name}` workflow. Canonical source: `{rel_source}`. {description}"
---

# Codex Adapter: `{name}`

Canonical source: `../../../{rel_source}`

## How to use this adapter

1. Read the canonical source file before acting.
2. Follow its workflow in Codex.
3. Translate Claude-only constructs as follows:
   - `AskUserQuestion` -> ask the user directly only when blocked; otherwise continue with the narrowest safe assumption.
   - `Task` / subagents -> use Codex delegation only when the user explicitly requests parallel or delegated agent work.
   - `Write` / `Edit` -> use `apply_patch` for manual edits.
   - `Bash` -> use `exec_command` with minimal, verifiable commands.
   - `WebSearch` -> use `web` or Context7 with primary sources.
4. Treat `.claude/docs/*`, `.claude/rules/*`, and linked templates as canonical until a repo-local Codex-native replacement exists.
5. If the canonical source conflicts with repo `AGENTS.md`, follow `AGENTS.md` first.

## Original description

{description}

## Maintenance

- Do not edit this generated file directly.
- Update `{rel_source}` or `tools/sync_codex_adapters.py`, then run:

```bash
python3 tools/sync_codex_adapters.py
```
"""


def render_index(skills: list[tuple[str, str, Path]]) -> str:
    lines = [
        "# Codex Skill Index",
        "",
        "最后更新：2026-04-17",
        "",
        "这些 adapter 文件由 `python3 tools/sync_codex_adapters.py` 生成。",
        "canonical source 仍然在 `.claude/skills/*/SKILL.md`。",
        "",
        f"总数：{len(skills)}",
        "",
    ]
    for name, description, _ in skills:
        lines.append(f"- `{name}`: {description}")
    lines.append("")
    return "\n".join(lines)


def expected_files() -> dict[Path, str]:
    skills = list_skills()
    files: dict[Path, str] = {
        AGENTS_SKILLS / "INDEX.md": render_index(skills),
    }
    for name, description, source in skills:
        files[AGENTS_SKILLS / name / "SKILL.md"] = render_skill(name, description, source)
    return files


def write_files(files: dict[Path, str]) -> None:
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def check_files(files: dict[Path, str]) -> int:
    mismatches: list[str] = []
    for path, content in files.items():
        if not path.exists():
            mismatches.append(f"MISSING {path.relative_to(ROOT)}")
            continue
        current = path.read_text(encoding="utf-8")
        if current != content:
            mismatches.append(f"STALE   {path.relative_to(ROOT)}")
    if mismatches:
        print("Codex adapters are not in sync:")
        for item in mismatches:
            print(f"- {item}")
        print("Run: python3 tools/sync_codex_adapters.py")
        return 1
    print(f"Codex adapters are in sync ({len(files)} files checked).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify adapters are up to date.")
    args = parser.parse_args()

    if not CLAUDE_SKILLS.exists():
        print(f"Missing canonical skill directory: {CLAUDE_SKILLS}", file=sys.stderr)
        return 1

    files = expected_files()
    if args.check:
        return check_files(files)

    write_files(files)
    print(f"Wrote {len(files)} Codex adapter files under {AGENTS_SKILLS.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
