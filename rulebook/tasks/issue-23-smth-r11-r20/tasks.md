## 1. Implementation
- [x] 1.1 建立输出目录 `典籍/calibrated/cards/smth/`
- [x] 1.2 产出 10 张 Deep 精校卡（文件名严格匹配 Issue #23 的 deliverables 列表）
- [x] 1.3 每张卡包含：`source_range`（行号锚点）、至少 1 条 `rule_smth_*` 规则草案、因子表（`existing/new_candidate`）、跨体系桥接（含 `neutral_tag`）
- [x] 1.4 新增并维护 `openspec/_ops/task_runs/ISSUE-23.md`（关键命令与关键输出落盘）

## 2. Testing
- [x] 2.1 `openspec validate --specs --strict --no-interactive`
- [ ] 2.2 `bash scripts/gates/gate0_engine_id_identity.sh` (skipped: env deps missing)
- [ ] 2.3 `bash scripts/gates/gate0_security_observability.sh` (skipped: env deps missing)
- [ ] 2.4 `bash scripts/gates/gate0_versioning_deviation.sh` (skipped: env deps missing)
- [ ] 2.5 `pytest backend/tests/unit -q` (skipped: env deps missing)

## 3. Documentation
- [ ] 3.1 PR 描述包含 `Closes #23`，并在合并后回填 `openspec/_ops/task_runs/ISSUE-23.md` 的 PR 链接
