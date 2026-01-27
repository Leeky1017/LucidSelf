# ISSUE-9
- Issue: #9
- Branch: task/9-calib-plan-rounds
- PR: <fill-after-created>

## Plan
- 在仓库 `.cursor/plans/` 持久化“典籍精校轮次任务清单”（纯文字；每条任务对应一本书一行；包含任务身份与可复制指令）。
- 更新 `.gitignore`：保持 `.cursor/` 默认忽略，但允许追踪 `.cursor/plans/**`。
- 通过 PR 交付，required checks 全绿并启用 auto-merge。

## Runs
### 2026-01-27 init
- Command: `gh auth status`
- Key output: logged in as `Leeky1017`
- Evidence: issue `#9`

### 2026-01-27 plan materialization
- Command: `scripts/agent_controlplane_sync.sh`
- Key output: `Already up to date.`
- Command: `scripts/agent_worktree_setup.sh 9 calib-plan-rounds`
- Key output: worktree ready at `.worktrees/issue-9-calib-plan-rounds`
- Change: add plan file `.cursor/plans/典籍精校_轮次任务清单.md`
- Change: update `.gitignore` to allow tracking `.cursor/plans/**`
- Change: add rulebook task `rulebook/tasks/issue-9-calib-plan-rounds/`

### 2026-01-27 local gates
- Command: `openspec validate --specs --strict --no-interactive`
- Key output: `Totals: 27 passed, 0 failed`
- Command: `bash scripts/gates/gate0_engine_id_identity.sh`
- Key output: `8 passed`
- Command: `bash scripts/gates/gate0_security_observability.sh`
- Key output: `4 passed`
- Command: `bash scripts/gates/gate0_versioning_deviation.sh`
- Key output: `9 passed`

### 2026-01-27 staging note
- Note: local `.git/info/exclude` contains `.cursor/`; used `git add -f .cursor/plans/典籍精校_轮次任务清单.md` to stage.

