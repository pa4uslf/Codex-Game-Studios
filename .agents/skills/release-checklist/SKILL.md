---
name: release-checklist
description: "Codex adapter for the original CCGS `release-checklist` workflow. Canonical source: `.claude/skills/release-checklist/SKILL.md`. Generates a comprehensive pre-release validation checklist covering build verification, certification requirements, store metadata, and launch readiness."
---

# Codex Adapter: `release-checklist`

Canonical source: `../../../.claude/skills/release-checklist/SKILL.md`

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

Generates a comprehensive pre-release validation checklist covering build verification, certification requirements, store metadata, and launch readiness.

## Maintenance

- Do not edit this generated file directly.
- Update `.claude/skills/release-checklist/SKILL.md` or `tools/sync_codex_adapters.py`, then run:

```bash
python3 tools/sync_codex_adapters.py
```
