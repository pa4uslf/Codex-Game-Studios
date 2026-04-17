---
name: test-helpers
description: "Codex adapter for the original CCGS `test-helpers` workflow. Canonical source: `.claude/skills/test-helpers/SKILL.md`. Generate engine-specific test helper libraries for the project's test suite. Reads existing test patterns and produces tests/helpers/ with assertion utilities, factory functions, and mock objects tailored to the project's systems. Reduces boilerplate in new test files."
---

# Codex Adapter: `test-helpers`

Canonical source: `../../../.claude/skills/test-helpers/SKILL.md`

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

Generate engine-specific test helper libraries for the project's test suite. Reads existing test patterns and produces tests/helpers/ with assertion utilities, factory functions, and mock objects tailored to the project's systems. Reduces boilerplate in new test files.

## Maintenance

- Do not edit this generated file directly.
- Update `.claude/skills/test-helpers/SKILL.md` or `tools/sync_codex_adapters.py`, then run:

```bash
python3 tools/sync_codex_adapters.py
```
