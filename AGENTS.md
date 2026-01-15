<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# LucidSelf — Agent Instructions

本仓库目标：构建 LucidSelf（LS）系统，并以 OpenSpec 作为工程控制台，确保演进 **可审计 / 可追溯 / 可复现**。

## 文档权威（必须遵守）

- 项目宪法：`openspec/project.md`（最高优先级）。
- 权威规格：`openspec/specs/**/spec.md`（定义 MUST/SHALL + 可验收场景）。
- Rulebook：`rulebook/tasks/**`（执行清单与落盘证据）。
- 其他文档（`docs/`、说明性 md）仅作为入口/指针，避免形成第二套权威。

## 交付流程（硬门禁）

LucidSelf 采用 `$openspec-rulebook-github-delivery`：

- GitHub 是并发与交付唯一入口：**Issue → Branch → PR → Checks → Auto-merge**。
- Issue 号 `N` 是任务唯一 ID：
  - 分支名：`task/<N>-<slug>`
  - 每个 commit message 必须包含 `(#N)`
  - PR body 必须包含 `Closes #N`
  - PR 必须新增/更新：`openspec/_ops/task_runs/ISSUE-N.md`
- required checks：`ci` / `openspec-log-guard` / `merge-serial`。
- 建议用 worktree 隔离开发：
  - 创建：`scripts/agent_worktree_setup.sh "$N" "$SLUG"`
  - 清理：`scripts/agent_worktree_cleanup.sh "$N" "$SLUG"`
- PR 前预检：`scripts/agent_pr_preflight.sh`（文件重叠风险）。
- 一键 PR + auto-merge：`scripts/agent_pr_automerge_and_sync.sh`

## 变更规则（spec-first）

- 新增能力/行为变更/契约变更：先写 OpenSpec / Rulebook，再实现代码。
- 禁止 silent failure：异常必须可见（错误码/错误信息）并能落盘证据。
- 禁止提交敏感信息：API keys / tokens / passwords / `.env` / 本机配置不得进入 git。

## 本地验证（最小集）

- `openspec validate --specs --strict --no-interactive`
- `bash scripts/gates/gate0_engine_id_identity.sh`
- `bash scripts/gates/gate0_security_observability.sh`
- `bash scripts/gates/gate0_versioning_deviation.sh`
- `pytest backend/tests/unit -q`
