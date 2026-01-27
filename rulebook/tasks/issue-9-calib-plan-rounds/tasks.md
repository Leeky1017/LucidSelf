## 1. Implementation
- [ ] 1.1 新增 `.cursor/plans/典籍精校_轮次任务清单.md`（纯文字；每条任务一行；含任务身份与指令）
- [ ] 1.2 更新 `.gitignore`：允许追踪 `.cursor/plans/**`，但不追踪其他 `.cursor/*`
- [ ] 1.3 新增并持续更新 `openspec/_ops/task_runs/ISSUE-9.md`（记录关键命令与输出）

## 2. Testing
- [ ] 2.1 `openspec validate --specs --strict --no-interactive`
- [ ] 2.2 `bash scripts/gates/gate0_engine_id_identity.sh`
- [ ] 2.3 `bash scripts/gates/gate0_security_observability.sh`
- [ ] 2.4 `bash scripts/gates/gate0_versioning_deviation.sh`

## 3. Delivery
- [ ] 3.1 建 PR，body 含 `Closes #9`
- [ ] 3.2 required checks 全绿（ci / openspec-log-guard / merge-serial）
- [ ] 3.3 启用 auto-merge，并确认已实际合并

