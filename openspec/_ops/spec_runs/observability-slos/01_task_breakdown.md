# observability-slos — Task Breakdown (inputs/actions/artifacts/acceptance/evidence)

证据目录约定：

- 单任务证据：`openspec/_ops/spec_runs/observability-slos/evidence/<task_id>__<short_name>.txt`
- 任务组回归：`openspec/_ops/spec_runs/observability-slos/02_regression_after_group_<n>.txt`

## Group 1 — Contracts & Interfaces（契约与接口）

### t01 — 固化契约与标识符（已存在为 [x]）
- **输入**：`openspec/specs/observability-slos/spec.md`
- **动作**：确认契约/标识符以 MUST/SHALL 与标准标题固化且可严格校验
- **产物**：规格文件维持严格格式
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t01__contract_ids.txt`

### t02 — 对外契约字段清单 + 拒绝原因枚举（机器可读）
- **输入**：本 spec 对外行为与字段语义
- **动作**：新增机器可读的字段清单与拒绝原因枚举（版本化）
- **产物**：`openspec/specs/observability-slos/contract/observability_slos_contract.v1.json`
- **验收命令**：
  - `.venv/bin/python -c 'import json; json.load(open(\"openspec/specs/observability-slos/contract/observability_slos_contract.v1.json\")); print(\"OK\")'`
  - `openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t02__contract_fields_and_rejection_reasons.txt`

## Group 2 — Data & Integrity（数据与完整性）

### t03 — 数据字典与字段级约束表
- **输入**：关键产物定义（指标规范/日志规范/trace 传播规范/SLO/告警规则）
- **动作**：补齐数据字典与字段级约束表（规格层）
- **产物**：`openspec/specs/observability-slos/data_dictionary.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t03__data_dictionary.txt`

### t04 — 引用可解析性 + 幂等/去重 + 冲突处理语义
- **输入**：t03 数据字典与现有 Requirements
- **动作**：定义引用解析、幂等/去重、冲突处理的规范语义（不含实现）
- **产物**：`openspec/specs/observability-slos/design.md`（新增语义章节）
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t04__integrity_semantics.txt`

## Group 3 — Runtime Behavior（运行时行为）

### t05 — 确定性边界 + 偏差检测/解释口径
- **输入**：Requirements: Runtime Determinism
- **动作**：定义“等价输出”边界与偏差检测/解释口径（规格层）
- **产物**：`openspec/specs/observability-slos/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t05__determinism_boundary.txt`

### t06 — 失败处理策略 + 信号产物
- **输入**：关键路径与门禁阻断要求
- **动作**：定义拒绝/降级/重试/回滚触发的策略与必须产物（指标/日志/审计事件）
- **产物**：`openspec/specs/observability-slos/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t06__failure_strategy.txt`

## Group 4 — Observability & Metrics（可观测与指标）

### t07 — metrics 列表 + SLO 阈值
- **输入**：Requirement: Observability
- **动作**：定义 metrics 名称/标签/单位/聚合口径与最小 SLO 阈值
- **产物**：`openspec/specs/observability-slos/observability.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t07__metrics_slos.txt`

### t08 — 审计日志字段 + 脱敏规则 + 导出结构
- **输入**：安全/合规最小化原则
- **动作**：定义审计字段、脱敏规则与审计导出结构（规格层）
- **产物**：`openspec/specs/observability-slos/audit_log.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t08__audit_log_schema.txt`

## Group 5 — Security/Compliance（安全与合规）

### t09 — 访问控制与隔离边界适用方式
- **输入**：LS 术语 user_id/org_id，Requirement: Security/Privacy/Compliance
- **动作**：明确本能力在观测数据访问/导出下的隔离边界与拒绝策略
- **产物**：`openspec/specs/observability-slos/security.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t09__access_control.txt`

### t10 — 保留/删除/合规审计证据项与期限
- **输入**：合规与审计需求
- **动作**：定义证据项清单与留存期限（规格层）
- **产物**：`openspec/specs/observability-slos/compliance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t10__retention_policy.txt`

## Group 6 — Performance/Cost（性能与成本）

### t11 — 性能目标 + 测量方式
- **输入**：关键路径（指标采集/日志写入/trace 传播/SLO 评估）
- **动作**：定义延迟/吞吐目标与测量口径（指标口径）
- **产物**：`openspec/specs/observability-slos/performance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t11__performance_targets.txt`

### t12 — 成本目标 + 预算阈值 + 告警策略
- **输入**：成本维度（存储/计算/日志/追踪）
- **动作**：定义预算阈值与告警策略（规格层）
- **产物**：`openspec/specs/observability-slos/cost.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t12__cost_budget.txt`

## Group 7 — Tests/Validation（测试与验证）

### t13 — `openspec validate --strict` 通过（已存在为 [x]）
- **输入**：全仓 OpenSpec 严格校验
- **动作**：运行严格校验并固化证据
- **产物**：`openspec/_ops/spec_runs/observability-slos/evidence/t13__openspec_validate_strict.txt`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t13__openspec_validate_strict.txt`

### t14 — 补齐系统级验证口径（acceptance.md）
- **输入**：本 spec 的可执行验收需求
- **动作**：在 `acceptance.md` 写清系统级验证命令/通过标准/失败阻断
- **产物**：`openspec/specs/observability-slos/acceptance.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t14__acceptance_updated.txt`

## Group 8 — Rollout/Risks（发布与风险）

### t15 — 分阶段 rollout + 回滚触发条件
- **输入**：门禁与阻断策略
- **动作**：定义 shadow/canary/gradual 与回滚触发条件（契约级）
- **产物**：`openspec/specs/observability-slos/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t15__rollout_plan.txt`

### t16 — Top 风险与缓解手段（写入 design.md）
- **输入**：本能力关键风险面
- **动作**：列出 Top 风险、证据/门禁/回退与缓解策略
- **产物**：`openspec/specs/observability-slos/design.md`
- **验收命令**：`openspec validate --strict`
- **证据落点**：`openspec/_ops/spec_runs/observability-slos/evidence/t16__risks.txt`

