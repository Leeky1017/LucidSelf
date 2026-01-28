## 1. Implementation
- [ ] 1.1 Locate section `一．论十干十二支` in source and record line anchors
- [ ] 1.2 Draft 20 P0 calibration cards `zpzq_shigan_dizhi_001`–`020`
- [ ] 1.3 Verify factor_id alignment; mark `new_candidate` when missing (no ontology edits)

## 2. Testing
- [ ] 2.1 Validate Rulebook task: `rulebook task validate issue-3-zpzq-shigan-dizhi-p0-b01`
- [ ] 2.2 Run OpenSpec validation: `openspec validate --specs --strict --no-interactive`
- [ ] 2.3 Run gates: `bash scripts/gates/gate0_engine_id_identity.sh` (and other required gate0 scripts)
- [ ] 2.4 Run PR preflight: `bash scripts/agent_pr_preflight.sh`

## 3. Documentation
- [ ] 3.1 Update run log: `openspec/_ops/task_runs/ISSUE-3.md` (commands + key outputs)
