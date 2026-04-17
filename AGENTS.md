# Codex Game Studios

这个仓库的目标是让 Codex 能直接消费原本为 Claude Code 设计的游戏工作流，而不是重写一套平行体系。

## 先读哪里

1. 先读 `.agentlens/INDEX.md` 做导航。
2. 仓库级规则看本文件。
3. 具体工作流、技能、角色、模板的 canonical source 仍然在 `.claude/`。
4. Codex 适配层在 `.agents/`，其中 `.agents/skills/*/SKILL.md` 由脚本生成。

## Canonical Source

- 技能正文以 `.claude/skills/*/SKILL.md` 为准。
- 角色定义以 `.claude/agents/*.md` 为准。
- 规则、模板、流程说明以 `.claude/docs/*` 和 `.claude/rules/*` 为准。
- `.agents/skills/*/SKILL.md` 是给 Codex 用的 adapter，不要手改；改完 `.claude/skills/*/SKILL.md` 后运行 `python3 tools/sync_codex_adapters.py`。

## Codex 适配约定

- 原技能里出现 `AskUserQuestion` 时，在 Codex 里只在确实阻塞时直接追问用户；否则按最窄、最安全的解释继续。
- 原技能里出现 `Task` / subagent 时，只有用户明确要求并行/委派时才用 `spawn_agent`；否则本地执行。
- 原技能里出现 `Write` / `Edit` 时，手工改文件统一用 `apply_patch`。
- 原技能里出现 `WebSearch` 时，优先用 `web` 或 Context7，并遵守主文档/官方来源优先。
- 原技能里引用的 `.claude/docs/*`、模板和规则，在没有 Codex 专门替代物之前都继续视为正式文档。

## 修改边界

- 这次仓库已经是 Codex fork 版本；新增改动优先写到 `AGENTS.md`、`.agentlens/`、`.agents/`、`README.md`、`UPGRADING.md` 和必要的同步脚本。
- 除非任务直接要求，不要批量重写 `.claude/skills/*` 的工作流内容，只做必要的兼容说明或源头修正。
- 如果要改技能内容，优先改 `.claude/skills/*/SKILL.md`，然后重新同步 `.agents/skills/*`。

## 提交前检查

- `python3 tools/sync_codex_adapters.py --check`
- `git diff --check`
- 文档里涉及“今天 / 最近 / 当前版本”时，优先写绝对日期，例如 `2026-04-17`
