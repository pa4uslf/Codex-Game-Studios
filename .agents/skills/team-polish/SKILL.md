---
name: team-polish
description: "Codex adapter for the original CCGS `team-polish` workflow. Canonical source: `.claude/skills/team-polish/SKILL.md`. Orchestrate the polish team: coordinates performance-analyst, technical-artist, sound-designer, and qa-tester to optimize, polish, and harden a feature or area for release quality."
---

# Codex Adapter: `team-polish`

Canonical source: `../../../.claude/skills/team-polish/SKILL.md`

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

Orchestrate the polish team: coordinates performance-analyst, technical-artist, sound-designer, and qa-tester to optimize, polish, and harden a feature or area for release quality.

## Maintenance

- Do not edit this generated file directly.
- Update `.claude/skills/team-polish/SKILL.md` or `tools/sync_codex_adapters.py`, then run:

```bash
python3 tools/sync_codex_adapters.py
```
