# security-privacy-compliance — Task Breakdown (inputs/actions/artifacts/acceptance/evidence)

证据目录约定：

- 单任务证据：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/<task_id>__<short_name>.txt`
- 任务组回归：`openspec/_ops/spec_runs/security-privacy-compliance/02_regression_after_group_<n>.txt`

## Group 1 — Contracts & Interfaces（契约与接口）

### t01 — 固化契约与标识符（已存在为 [x]）
- **输入**：`openspec/specs/security-privacy-compliance/spec.md`
- **动作**：确认契约/标识符以 MUST/SHALL 与标准标题固化且可严格校验
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t01__contract_ids.txt`

### t02 — 对外契约字段清单 + 拒绝原因枚举（机器可读）
- **动作**：新增机器可读的字段清单与拒绝原因枚举（版本化）
- **产物**：`openspec/specs/security-privacy-compliance/contract/security_privacy_compliance_contract.v1.json`
- **验收命令**：
  - `.venv/bin/python -c 'import json; json.load(open(\"openspec/specs/security-privacy-compliance/contract/security_privacy_compliance_contract.v1.json\")); print(\"OK\")'`
  - `openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t02__contract_fields_and_rejection_reasons.txt`

## Group 2 — Data & Integrity（数据与完整性）

### t03 — 数据字典与字段级约束表
- **动作**：补齐关键产物的数据字典与字段级约束表（规格层）
- **产物**：`openspec/specs/security-privacy-compliance/data_dictionary.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t03__data_dictionary.txt`

### t04 — 引用可解析性 + 幂等/去重 + 冲突处理语义
- **动作**：定义引用解析、幂等/去重、冲突处理的规范语义（不含实现）
- **产物**：`openspec/specs/security-privacy-compliance/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t04__integrity_semantics.txt`

## Group 3 — Runtime Behavior（运行时行为）

### t05 — 确定性边界 + 偏差检测/解释口径
- **产物**：`openspec/specs/security-privacy-compliance/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t05__determinism_boundary.txt`

### t06 — 失败处理策略 + 信号产物
- **产物**：`openspec/specs/security-privacy-compliance/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t06__failure_strategy.txt`

## Group 4 — Observability & Metrics（可观测与指标）

### t07 — metrics 列表 + SLO 阈值
- **产物**：`openspec/specs/security-privacy-compliance/observability.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t07__metrics_slos.txt`

### t08 — 审计日志字段 + 脱敏规则 + 导出结构
- **产物**：`openspec/specs/security-privacy-compliance/audit_log.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t08__audit_log_schema.txt`

## Group 5 — Security/Compliance（安全与合规）

### t09 — 访问控制与隔离边界适用方式
- **产物**：`openspec/specs/security-privacy-compliance/security.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t09__access_control.txt`

### t10 — 保留/删除/合规审计证据项与期限
- **产物**：`openspec/specs/security-privacy-compliance/compliance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t10__retention_policy.txt`

## Group 6 — Performance/Cost（性能与成本）

### t11 — 性能目标 + 测量方式
- **产物**：`openspec/specs/security-privacy-compliance/performance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t11__performance_targets.txt`

### t12 — 成本目标 + 预算阈值 + 告警策略
- **产物**：`openspec/specs/security-privacy-compliance/cost.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t12__cost_budget.txt`

## Group 7 — Tests/Validation（测试与验证）

### t13 — `openspec validate --strict` 通过（已存在为 [x]）
- **产物**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t13__openspec_validate_strict.txt`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t13__openspec_validate_strict.txt`

### t14 — 补齐系统级验证口径（acceptance.md）
- **产物**：`openspec/specs/security-privacy-compliance/acceptance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t14__acceptance_updated.txt`

## Group 8 — Rollout/Risks（发布与风险）

### t15 — 分阶段 rollout + 回滚触发条件
- **产物**：`openspec/specs/security-privacy-compliance/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t15__rollout_plan.txt`

### t16 — Top 风险与缓解手段（写入 design.md）
- **产物**：`openspec/specs/security-privacy-compliance/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/security-privacy-compliance/evidence/t16__risks.txt`

