## 1. Implementation
- [ ] 1.1 Create run log `openspec/_ops/task_runs/ISSUE-5.md` and keep appending evidence
- [ ] 1.2 Add 20 P0 calibration cards under `典籍/calibrated/cards/inner_sky/` (continuous IDs 001–020)
- [ ] 1.3 Ensure every card follows `典籍/CALIBRATION_TEMPLATE_EN.md` (A–F filled; tables meet minimum row requirements)
- [ ] 1.4 Summarize `new_candidate` factor_id suggestions (no ontology edits)

## 2. Testing
- [ ] 2.1 `openspec validate --specs --strict --no-interactive`
- [ ] 2.2 Run minimal CI-equivalent checks locally: gate scripts + unit tests

## 3. Delivery
- [ ] 3.1 PR includes `Closes #5` + `openspec/_ops/task_runs/ISSUE-5.md`; required checks are green; auto-merge enabled

