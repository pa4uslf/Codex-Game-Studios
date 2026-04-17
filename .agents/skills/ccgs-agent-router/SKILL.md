---
name: ccgs-agent-router
description: Route Codex requests for CCGS studio roles to the canonical agent specs in `.claude/agents/*.md`. Use when the user explicitly names a studio role such as `creative-director`, `technical-director`, `lead-programmer`, `art-director`, `qa-lead`, `writer`, `unity-specialist`, `godot-specialist`, or asks for a department-specific game-studio specialist from this repo.
---

# CCGS Agent Router

This skill adapts the original CCGS agent roster for Codex.

## Canonical Source

- Agent specs: `../../../.claude/agents/*.md`
- Coordination rules: `../../../.claude/docs/coordination-rules.md`
- Workflow overview: `../../../.claude/docs/quick-start.md`

## How To Use

1. Identify the requested studio role from the user's wording.
2. Read the matching canonical agent spec in `.claude/agents/`.
3. Emulate that role's reasoning style and responsibility boundaries inside Codex.
4. Keep Codex's higher-priority system/developer/AGENTS rules above the imported role instructions.

## Translation Rules

- If the agent spec says to use `Task` or subagents, only do that when the user explicitly wants delegation; otherwise work locally.
- If the agent spec says to use `AskUserQuestion`, ask a concise plain-text question only when blocked.
- If the agent spec names unsupported tools, translate them to the nearest Codex capability:
  - `Write` / `Edit` -> `apply_patch`
  - `Bash` -> `exec_command`
  - `WebSearch` -> `web` or Context7
- If the agent spec conflicts with `AGENTS.md`, follow `AGENTS.md`.

## Common Mappings

- Creative direction: `creative-director`, `art-director`, `audio-director`, `narrative-director`
- Technical leadership: `technical-director`, `lead-programmer`, `devops-engineer`, `security-engineer`
- Design: `game-designer`, `systems-designer`, `level-designer`, `ux-designer`, `economy-designer`, `world-builder`
- Implementation: `gameplay-programmer`, `engine-programmer`, `ai-programmer`, `network-programmer`, `tools-programmer`, `ui-programmer`
- QA and release: `qa-lead`, `qa-tester`, `release-manager`, `localization-lead`, `community-manager`
- Engine specialists: `godot-*`, `unity-*`, `unreal-*`, `ue-*`

## Guardrails

- Do not invent a new studio role if a canonical one already exists.
- Do not edit `.agents/skills/*` to change role behavior; edit `.claude/agents/*.md` instead.
- When in doubt, route upward in the studio hierarchy rather than broadening scope silently.
