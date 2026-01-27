# ISSUE-13
- Issue: #13
- Branch: task/13-cal-zpzq-r01-ganzhi
- PR: <fill-after-created>

## Plan
- 产出《子平真诠》R01（论十干十二支·上）Scholarly 精校卡，落盘到 `典籍/calibrated/cards/zpzq/zpzq_r01_ganzhi_001.md`。
- 新增 rulebook task `rulebook/tasks/issue-13-cal-zpzq-r01-ganzhi/`，并在本文件记录关键执行证据。
- 通过 PR 交付并启用 auto-merge，required checks 全绿后确认实际合并。

## Runs
### 2026-01-28 init
- Command: `gh auth status && git remote -v`
- Key output: logged in as `Leeky1017`; remote=`https://github.com/Leeky1017/LucidSelf.git`
- Evidence: issue `#13`

### 2026-01-28 worktree setup
- Command: `scripts/agent_controlplane_sync.sh`
- Key output: `sync check failed: main...origin/main = 1 0` (control-plane main ahead by 1)
- Command: `scripts/agent_worktree_setup.sh 13 cal-zpzq-r01-ganzhi --base origin/main --no-sync`
- Key output: worktree ready at `.worktrees/issue-13-cal-zpzq-r01-ganzhi` (base `origin/main`)

### 2026-01-28 authoring
- Change: add RUN_LOG `openspec/_ops/task_runs/ISSUE-13.md`
- Change: add rulebook task `rulebook/tasks/issue-13-cal-zpzq-r01-ganzhi/`
- Change: add calibration card `典籍/calibrated/cards/zpzq/zpzq_r01_ganzhi_001.md`

### 2026-01-28 local gates
- Command: `openspec validate --specs --strict --no-interactive`
- Key output: `Totals: 27 passed, 0 failed`
- Command: `bash scripts/gates/gate0_engine_id_identity.sh`
- Key output: `8 passed`
- Command: `bash scripts/gates/gate0_security_observability.sh`
- Key output: `4 passed`
- Command: `bash scripts/gates/gate0_versioning_deviation.sh`
- Key output: `9 passed`
- Command: `pytest backend/tests/unit -q`
- Key output: `FAILED (ModuleNotFoundError: No module named 'backend')`
- Command: `PYTHONPATH=. .venv/bin/pytest backend/tests/unit -q`
- Key output: `108 passed`

