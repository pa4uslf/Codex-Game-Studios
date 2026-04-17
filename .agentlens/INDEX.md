# AgentLens Index

最后更新：2026-04-17

## 这个仓库现在怎么读

- `AGENTS.md`
  仓库级 Codex 说明、canonical source 约定、同步方式。
- `.agents/README.md`
  Codex 适配层说明，解释为什么保留 `.claude/` 作为源头。
- `.agents/skills/INDEX.md`
  自动生成的 Codex 技能清单。
- `.agents/skills/ccgs-agent-router/SKILL.md`
  当用户点名某个 studio 角色时，用它把请求路由到 `.claude/agents/*.md`。
- `.claude/skills/*/SKILL.md`
  原始工作流定义，仍是单一事实源。
- `.claude/agents/*.md`
  原始角色定义。
- `.claude/docs/*`
  模板、流程、规则、引擎参考。

## 推荐阅读顺序

1. `AGENTS.md`
2. `.agents/README.md`
3. `.claude/docs/quick-start.md`
4. `.claude/docs/workflow-catalog.yaml`
5. 对应的 `.claude/skills/*/SKILL.md` 或 `.claude/agents/*.md`

## 目录职责

- `.agents/`
  Codex 可消费的适配层；以镜像和路由为主，不重复维护业务正文。
- `.claude/`
  上游 Claude 结构和正式工作流定义。
- `design/`
  GDD、视觉、叙事、关卡等设计资产。
- `docs/`
  架构、ADR、引擎参考、示例。
- `production/`
  阶段、迭代、故事、里程碑、会话状态。
- `src/`
  游戏源码。

## 维护规则

- 改技能正文：改 `.claude/skills/*/SKILL.md`，然后运行 `python3 tools/sync_codex_adapters.py`
- 改角色正文：改 `.claude/agents/*.md`
- 改 Codex 路由或生成策略：改 `tools/sync_codex_adapters.py`、`.agents/README.md` 或 `AGENTS.md`
