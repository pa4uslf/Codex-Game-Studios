<p align="center">
  <h1 align="center">Codex Game Studios</h1>
  <p align="center">
    Turn a single Codex session into a full game development studio.
    <br />
    49 studio roles. 72 workflow skills. One Codex-compatible game-dev system.
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href=".claude/agents"><img src="https://img.shields.io/badge/agents-49-blueviolet" alt="49 Agents"></a>
  <a href=".agents/skills"><img src="https://img.shields.io/badge/codex%20skills-72-green" alt="72 Codex Skills"></a>
  <a href=".claude/hooks"><img src="https://img.shields.io/badge/hooks-12-orange" alt="12 Hooks"></a>
  <a href=".claude/rules"><img src="https://img.shields.io/badge/rules-11-red" alt="11 Rules"></a>
  <a href="https://github.com/pa4uslf/Codex-Game-Studios"><img src="https://img.shields.io/badge/fork-pa4uslf%2FCodex--Game--Studios-24292f?logo=github" alt="Fork Repo"></a>
  <a href="https://github.com/Donchitos/Claude-Code-Game-Studios"><img src="https://img.shields.io/badge/upstream-Donchitos%2FClaude--Code--Game--Studios-f5f5f5?logo=github" alt="Upstream Repo"></a>
</p>

---

## Why This Exists

Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"

**Codex Game Studios** is a Codex-first fork of the original Claude Code Game Studios. It keeps the upstream `.claude/` workflow assets as the canonical source, then adds a Codex adapter layer (`AGENTS.md`, `.agentlens/INDEX.md`, `.agents/skills/*`) so the same studio system can be used cleanly from Codex.

The result: you still make every decision, but now you have a team structure that asks the right questions, catches mistakes early, and stays usable in both Codex and the original Claude setup.

> Fork note: as of `2026-04-17`, this repo is maintained as the Codex-compatible fork at `pa4uslf/Codex-Game-Studios`.

---

## Table of Contents

- [What's Included](#whats-included)
- [Codex Compatibility](#codex-compatibility)
- [Studio Hierarchy](#studio-hierarchy)
- [Skills And Commands](#skills-and-commands)
- [Getting Started](#getting-started)
- [Upgrading](#upgrading)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Design Philosophy](#design-philosophy)
- [Customization](#customization)
- [Platform Support](#platform-support)
- [Community](#community)
- [Upstream Credit](#upstream-credit)
- [License](#license)

---

## What's Included

| Category | Count | Description |
|----------|-------|-------------|
| **Studio Roles** | 49 | Canonical role definitions in `.claude/agents/` across design, programming, art, audio, narrative, QA, and production |
| **Workflow Skills** | 72 | Canonical workflow definitions in `.claude/skills/`, mirrored to `.agents/skills/` for Codex |
| **Hooks** | 12 | Automated validation on commits, pushes, asset changes, session lifecycle, agent audit trail, and gap detection |
| **Rules** | 11 | Path-scoped coding standards enforced when editing gameplay, engine, AI, UI, network code, and more |
| **Templates** | 39 | Document templates for GDDs, UX specs, ADRs, sprint plans, HUD design, accessibility, and more |
| **Codex Layer** | 1 | `AGENTS.md`, `.agentlens/INDEX.md`, `.agents/README.md`, and generated adapters for Codex |

## Codex Compatibility

This fork is organized around a simple split:

- `.claude/` remains the canonical source for skills, roles, rules, templates, and hooks.
- `.agents/skills/*/SKILL.md` are generated Codex adapters that point back to the canonical `.claude/skills/*/SKILL.md`.
- `AGENTS.md` and `.agentlens/INDEX.md` give Codex a stable repo-native entry point.

If you update a canonical skill, regenerate the Codex layer with:

```bash
python3 tools/sync_codex_adapters.py
```

## Studio Hierarchy

Agents are organized into three tiers, matching how real studios operate:

```
Tier 1 — Directors (Opus)
  creative-director    technical-director    producer

Tier 2 — Department Leads (Sonnet)
  game-designer        lead-programmer       art-director
  audio-director       narrative-director    qa-lead
  release-manager      localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
  gameplay-programmer  engine-programmer     ai-programmer
  network-programmer   tools-programmer      ui-programmer
  systems-designer     level-designer        economy-designer
  technical-artist     sound-designer        writer
  world-builder        ux-designer           prototyper
  performance-analyst  devops-engineer       analytics-engineer
  security-engineer    qa-tester             accessibility-specialist
  live-ops-designer    community-manager
```

### Engine Specialists

The template includes agent sets for all three major engines. Use the set that matches your project:

| Engine | Lead Agent | Sub-Specialists |
|--------|-----------|-----------------|
| **Godot 4** | `godot-specialist` | GDScript, Shaders, GDExtension |
| **Unity** | `unity-specialist` | DOTS/ECS, Shaders/VFX, Addressables, UI Toolkit |
| **Unreal Engine 5** | `unreal-specialist` | GAS, Blueprints, Replication, UMG/CommonUI |

## Skills And Commands

These workflow names are canonical across both environments:

- In Claude, they are exposed as slash commands like `/start`.
- In Codex, use the same workflow name by asking for it directly, for example: `运行 start workflow`、`执行 brainstorm skill`、`按 setup-engine 流程继续`。
- The Codex entry point is `.agents/skills/*`, which routes back to the canonical `.claude/skills/*/SKILL.md`.

Core workflow set:

**Onboarding & Navigation**
`/start` `/help` `/project-stage-detect` `/setup-engine` `/adopt`

**Game Design**
`/brainstorm` `/map-systems` `/design-system` `/quick-design` `/review-all-gdds` `/propagate-design-change`

**Art & Assets**
`/art-bible` `/asset-spec` `/asset-audit`

**UX & Interface Design**
`/ux-design` `/ux-review`

**Architecture**
`/create-architecture` `/architecture-decision` `/architecture-review` `/create-control-manifest`

**Stories & Sprints**
`/create-epics` `/create-stories` `/dev-story` `/sprint-plan` `/sprint-status` `/story-readiness` `/story-done` `/estimate`

**Reviews & Analysis**
`/design-review` `/code-review` `/balance-check` `/content-audit` `/scope-check` `/perf-profile` `/tech-debt` `/gate-check` `/consistency-check`

**QA & Testing**
`/qa-plan` `/smoke-check` `/soak-test` `/regression-suite` `/test-setup` `/test-helpers` `/test-evidence-review` `/test-flakiness` `/skill-test` `/skill-improve`

**Production**
`/milestone-review` `/retrospective` `/bug-report` `/bug-triage` `/reverse-document` `/playtest-report`

**Release**
`/release-checklist` `/launch-checklist` `/changelog` `/patch-notes` `/hotfix`

**Creative & Content**
`/prototype` `/onboard` `/localize`

**Team Orchestration** (coordinate multiple agents on a single feature)
`/team-combat` `/team-narrative` `/team-ui` `/team-release` `/team-polish` `/team-audio` `/team-level` `/team-live-ops` `/team-qa`

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- Codex CLI
- **Optional**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) if you also want to use the original upstream environment
- **Recommended**: [jq](https://jqlang.github.io/jq/) (for hook validation) and Python 3 (for JSON validation)

All hooks fail gracefully if optional tools are missing — nothing breaks, you just lose validation.

### Setup

1. **Clone or use as template**:
   ```bash
   git clone https://github.com/pa4uslf/Codex-Game-Studios.git my-game
   cd my-game
   ```

2. **Open Codex** and start from the repo root:
   ```bash
   codex
   ```

3. **Let Codex read the repo entry points**:
   - `AGENTS.md`
   - `.agentlens/INDEX.md`
   - `.agents/skills/INDEX.md`

4. **Use the same workflow names as the original system**:
   - `start` — first-session onboarding
   - `brainstorm` — explore game ideas from scratch
   - `setup-engine godot 4.6` — configure your engine if you already know
   - `project-stage-detect` — analyze an existing project

5. **If you also use Claude Code**, the original `.claude/` structure still works:
   ```bash
   claude
   ```

## Upgrading

Already using an older Claude-first or early fork version? See [UPGRADING.md](UPGRADING.md)
for migration steps, including the `2026-04-17` Codex adapter layer.

## Project Structure

```
AGENTS.md                           # Codex repo entry point
.agentlens/INDEX.md                 # Repo navigation map for Codex
CLAUDE.md                           # Master configuration
.agents/
  README.md                         # Codex adapter layer notes
  skills/                           # Generated Codex adapters for the 72 canonical skills
.claude/
  settings.json                     # Hooks, permissions, safety rules
  agents/                           # 49 canonical role definitions
  skills/                           # 72 canonical workflow definitions
  hooks/                            # 12 hook scripts (bash, cross-platform)
  rules/                            # 11 path-scoped coding standards
  statusline.sh                     # Status line script (context%, model, stage, epic breadcrumb)
  docs/
    workflow-catalog.yaml           # 7-phase pipeline definition (read by /help)
    templates/                      # 39 document templates
src/                                # Game source code
assets/                             # Art, audio, VFX, shaders, data files
design/                             # GDDs, narrative docs, level designs
docs/                               # Technical documentation and ADRs
tests/                              # Test suites (unit, integration, performance, playtest)
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes (isolated from src/)
production/                         # Sprint plans, milestones, release tracking
```

## How It Works

### Agent Coordination

Agents follow a structured delegation model:

1. **Vertical delegation** — directors delegate to leads, leads delegate to specialists
2. **Horizontal consultation** — same-tier agents can consult each other but can't make binding cross-domain decisions
3. **Conflict resolution** — disagreements escalate up to the shared parent (`creative-director` for design, `technical-director` for technical)
4. **Change propagation** — cross-department changes are coordinated by `producer`
5. **Domain boundaries** — agents don't modify files outside their domain without explicit delegation

### Collaborative, Not Autonomous

This is **not** an auto-pilot system. Every agent follows a strict collaboration protocol:

1. **Ask** — agents ask questions before proposing solutions
2. **Present options** — agents show 2-4 options with pros/cons
3. **You decide** — the user always makes the call
4. **Draft** — agents show work before finalizing
5. **Approve** — nothing gets written without your sign-off

You stay in control. The agents provide structure and expertise, not autonomy.

### Automated Safety

**Hooks** run automatically on every session:

| Hook | Trigger | What It Does |
|------|---------|--------------|
| `validate-commit.sh` | PreToolUse (Bash) | Checks for hardcoded values, TODO format, JSON validity, design doc sections — exits early if the command is not `git commit` |
| `validate-push.sh` | PreToolUse (Bash) | Warns on pushes to protected branches — exits early if the command is not `git push` |
| `validate-assets.sh` | PostToolUse (Write/Edit) | Validates naming conventions and JSON structure — exits early if the file is not in `assets/` |
| `session-start.sh` | Session open | Shows current branch and recent commits for orientation |
| `detect-gaps.sh` | Session open | Detects fresh projects (suggests `/start`) and missing design docs when code or prototypes exist |
| `pre-compact.sh` | Before compaction | Preserves session progress notes |
| `post-compact.sh` | After compaction | Reminds Claude to restore session state from `active.md` |
| `notify.sh` | Notification event | Shows Windows toast notification via PowerShell |
| `session-stop.sh` | Session close | Archives `active.md` to session log and records git activity |
| `log-agent.sh` | Agent spawned | Audit trail start — logs subagent invocation |
| `log-agent-stop.sh` | Agent stops | Audit trail stop — completes subagent record |
| `validate-skill-change.sh` | PostToolUse (Write/Edit) | Advises running `/skill-test` after any `.claude/skills/` change |

> **Note**: `validate-commit.sh`, `validate-assets.sh`, and `validate-skill-change.sh` fire on every Bash/Write tool call and exit immediately (exit 0) when the command or file path is not relevant. This is normal hook behavior — not a performance concern.

**Permission rules** in `settings.json` auto-allow safe operations (git status, test runs) and block dangerous ones (force push, `rm -rf`, reading `.env` files).

### Path-Scoped Rules

Coding standards are automatically enforced based on file location:

| Path | Enforces |
|------|----------|
| `src/gameplay/**` | Data-driven values, delta time usage, no UI references |
| `src/core/**` | Zero allocations in hot paths, thread safety, API stability |
| `src/ai/**` | Performance budgets, debuggability, data-driven parameters |
| `src/networking/**` | Server-authoritative, versioned messages, security |
| `src/ui/**` | No game state ownership, localization-ready, accessibility |
| `design/gdd/**` | Required 8 sections, formula format, edge cases |
| `tests/**` | Test naming, coverage requirements, fixture patterns |
| `prototypes/**` | Relaxed standards, README required, hypothesis documented |

## Design Philosophy

This template is grounded in professional game development practices:

- **MDA Framework** — Mechanics, Dynamics, Aesthetics analysis for game design
- **Self-Determination Theory** — Autonomy, Competence, Relatedness for player motivation
- **Flow State Design** — Challenge-skill balance for player engagement
- **Bartle Player Types** — Audience targeting and validation
- **Verification-Driven Development** — Tests first, then implementation

## Customization

This is a **template**, not a locked framework. Everything is meant to be customized:

- **Add/remove agents** — delete agent files you don't need, add new ones for your domains
- **Edit agent prompts** — tune agent behavior, add project-specific knowledge
- **Modify skills** — adjust workflows to match your team's process
- **Add rules** — create new path-scoped rules for your project's directory structure
- **Tune hooks** — adjust validation strictness, add new checks
- **Pick your engine** — use the Godot, Unity, or Unreal agent set (or none)
- **Set review intensity** — `full` (all director gates), `lean` (phase gates only), or `solo` (none). Set during `/start` or edit `production/review-mode.txt`. Override per-run with `--review solo` on any skill.

## Platform Support

Tested on **Windows 10** with Git Bash. All hooks use POSIX-compatible patterns (`grep -E`, not `grep -P`) and include fallbacks for missing tools. Works on macOS and Linux without modification.

## Community

- **Fork repo** — [pa4uslf/Codex-Game-Studios](https://github.com/pa4uslf/Codex-Game-Studios)
- **Upstream repo** — [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
- **Issues** — open issues against the fork for Codex-specific problems; upstream remains the reference for original Claude workflow evolution

---

## Upstream Credit

This fork stands on top of the original work by `Donchitos/Claude-Code-Game-Studios`.
The Codex layer in this repo is meant to preserve that workflow while making it usable from Codex without hand-maintaining two separate systems.

---

*Built for Codex, kept compatible with the original Claude workflow assets.*

## License

MIT License. See [LICENSE](LICENSE) for details.
