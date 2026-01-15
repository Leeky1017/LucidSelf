# 启动性与回归基线 Tasks

## Contracts & Interfaces（契约与接口）
- [x] 已完成：用中文固化「启动性与回归基线」契约与标识符（保留 MUST/SHALL 与标准标题） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t01__contract_ids.txt)
- [x] 定义对外契约字段清单与拒绝原因枚举（机器可读） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t02__contract_fields_and_rejection_reasons.txt)

## Data & Integrity（数据与完整性）
- [x] 建立关键产物（启动检查清单、回归套件基线、失败阻断记录、版本关联报告）的数据字典与字段级约束表 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t03__data_dictionary.txt)
- [x] 定义引用可解析性、幂等/去重与冲突处理语义（规格层） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t04__integrity_semantics.txt)

## Runtime Behavior（运行时行为）
- [x] 定义关键路径的确定性边界与偏差检测/解释口径 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t05__determinism_boundary.txt)
- [x] 定义失败处理策略（拒绝/降级/重试/回滚触发）与信号产物 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t06__failure_strategy.txt)

## Observability & Metrics（可观测与指标）
- [x] 定义核心 metrics 列表（名称/标签/单位/聚合口径）与 SLO 阈值 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t07__metrics_slos.txt)
- [x] 定义审计日志字段与脱敏规则（最小化原则）与审计导出结构 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t08__audit_log_schema.txt)

## Security/Compliance（安全与合规）
- [x] 明确访问控制与隔离边界（user_id/org_id）在本能力中的适用方式 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t09__access_control.txt)
- [x] 明确保留/删除/合规审计所需证据项与留存期限（规格层） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t10__retention_policy.txt)

## Performance/Cost（性能与成本）
- [x] 定义性能目标（延迟/吞吐）与测量方式（指标口径） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t11__performance_targets.txt)
- [x] 定义成本目标与预算阈值（如 tokens/存储/计算）与告警策略 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t12__cost_budget.txt)

## Tests/Validation（测试与验证）
- [x] 已完成：`openspec validate --specs --strict --no-interactive` 通过 (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t13__openspec_validate_strict.txt)
- [x] 为本能力补齐系统级验证口径（命令/通过标准/失败阻断）并写入 `acceptance.md` (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t14__acceptance_updated.txt)

## Rollout/Risks（发布与风险）
- [x] 定义分阶段 rollout（shadow/canary/gradual）与回滚触发条件（契约级） (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t15__rollout_plan.txt)
- [x] 列出 Top 风险与缓解手段（证据/门禁/回退）并写入 `design.md` (evidence: openspec/_ops/spec_runs/bootability-and-regression-baseline/evidence/t16__risks.txt)
