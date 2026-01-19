# Tasks — Add ZPZQ Calibration Cards (P0 Batch 01)

## 0) Change bootstrap
- [ ] 0.1 `openspec validate add-zpzq-calibration-cards-p0-b01 --strict --no-interactive`

## 1) Implementation
- [ ] 1.1 Create output dir: `典籍/calibrated/cards/zpzq/`
- [ ] 1.2 Produce 20 cards: `zpzq_shigan_dizhi_001`–`020` (P0)
- [ ] 1.3 Verify each card:
  - [ ] A–F sections present
  - [ ] A: `source_anchor` is `路径:行号`; `source_text` is verbatim
  - [ ] B: factor table >= 3 rows; `factor_id` aligned or `new_candidate`
  - [ ] C/D/E/F: each table >= 1 row

## 2) Validation (repo minimum)
- [ ] 2.1 `openspec validate --specs --strict --no-interactive`
- [ ] 2.2 `bash scripts/gates/gate0_engine_id_identity.sh`
- [ ] 2.3 `bash scripts/gates/gate0_security_observability.sh`
- [ ] 2.4 `bash scripts/gates/gate0_versioning_deviation.sh`
- [ ] 2.5 `pytest backend/tests/unit -q`

## 3) Delivery
- [ ] 3.1 Update run log: `openspec/_ops/task_runs/ISSUE-3.md`
- [ ] 3.2 Run preflight: `bash scripts/agent_pr_preflight.sh`
- [ ] 3.3 Open PR with `Closes #3` and enable auto-merge

