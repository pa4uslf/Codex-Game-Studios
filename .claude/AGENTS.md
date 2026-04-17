# `.claude/` 工作说明

- 这里仍然是本仓库工作流、角色、规则、模板的 canonical source。
- 改技能正文请改 `.claude/skills/*/SKILL.md`，不要先改 `.agents/skills/*/SKILL.md`。
- 改完技能正文后运行 `python3 ../tools/sync_codex_adapters.py`，同步 Codex adapter。
- `.claude/agents/*.md` 是角色原始定义；Codex 通过 `.agents/skills/ccgs-agent-router/SKILL.md` 来消费它们。
