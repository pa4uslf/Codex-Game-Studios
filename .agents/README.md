# Codex Adapter Layer

最后更新：2026-04-17

这个目录把仓库从 “Claude-first” 变成 “Codex 也能直接消费” 的版本，但不复制维护整套工作流。

## 设计原则

- `.claude/` 继续作为 canonical source。
- `.agents/skills/*/SKILL.md` 是给 Codex 的 adapter 层，统一告诉 Codex 去读哪个 canonical skill，以及如何把 Claude 专属工具语义翻译成 Codex 行为。
- 这样做可以避免在两个目录里分别维护 72 个技能正文。

## 你应该改哪里

- 改技能流程或文案：`.claude/skills/*/SKILL.md`
- 改角色定义：`.claude/agents/*.md`
- 改 Codex adapter 生成规则：`tools/sync_codex_adapters.py`

## 重新同步

```bash
python3 tools/sync_codex_adapters.py
python3 tools/sync_codex_adapters.py --check
```

## 额外入口

- `.agents/skills/ccgs-agent-router/SKILL.md`
  把 “creative-director / lead-programmer / qa-lead / art-director ...” 这类角色请求路由到原始 agent 定义。
