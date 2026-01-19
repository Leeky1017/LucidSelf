# ISSUE-5
- Issue: #5
- Branch: task/5-inner-sky-p0-batch01
- PR: https://github.com/Leeky1017/LucidSelf/pull/6

## Plan
- Land 20 P0 calibration cards for `inner_sky` (Prime Symbol + Signs)
- Verify cards comply with flat template + ontology alignment rules
- Run minimal local checks and deliver via PR with auto-merge

## Runs
### 2026-01-19 Create Issue (local)
- Command: `gh issue create -t "[CALIBRATION-P0-BATCH01] inner_sky: The Prime Symbol + Signs (20 cards)" -b "<body>"`
- Key output: `https://github.com/Leeky1017/LucidSelf/issues/5`

### 2026-01-19 Worktree setup (local)
- Command: `scripts/agent_worktree_setup.sh 5 inner-sky-p0-batch01`
- Key output: `OK: .worktrees/issue-5-inner-sky-p0-batch01 (task/5-inner-sky-p0-batch01)`

### 2026-01-19 Add calibration cards (local)
- Command: `rsync -a /tmp/lucidself_issue5_inner_sky_p0_batch01/calibrated/ 典籍/calibrated/`
- Evidence: `典籍/calibrated/cards/inner_sky/*.md`

### 2026-01-19 22:56 OpenSpec strict validation
- Command: `openspec validate --specs --strict --no-interactive`
- Key output: `Totals: 27 passed, 0 failed (27 items)`

### 2026-01-19 22:56 Gate-0 foundation (engine_id + identity)
- Command: `bash scripts/gates/gate0_engine_id_identity.sh`
- Key output: `8 passed`

### 2026-01-19 22:56 Gate-0 security + observability
- Command: `bash scripts/gates/gate0_security_observability.sh`
- Key output: `4 passed`

### 2026-01-19 22:56 Gate-0 versioning + deviation
- Command: `bash scripts/gates/gate0_versioning_deviation.sh`
- Key output:
  - `9 passed`
  - `artifacts/versioning/version_manifest.json`

### 2026-01-19 22:56 Unit tests
- Command: `PYTHONPATH=. .venv/bin/pytest backend/tests/unit -q`
- Key output: `108 passed`

### 2026-01-19 23:00 Push branch (local)
- Command: `git push -u origin HEAD`
- Key output: `new branch -> task/5-inner-sky-p0-batch01`

### 2026-01-19 23:01 PR preflight (local)
- Command: `scripts/agent_pr_preflight.sh`
- Key output: `OK: no overlapping files with open PRs`

### 2026-01-19 23:01 Create PR (local)
- Command: `gh pr create --base main --head task/5-inner-sky-p0-batch01 ...`
- Key output: `https://github.com/Leeky1017/LucidSelf/pull/6`
