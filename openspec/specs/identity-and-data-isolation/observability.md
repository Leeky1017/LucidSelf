# 身份与数据隔离 — 可观测与指标（规格层）

本文件定义 `identity-and-data-isolation` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_identity_isolation_requests_total` | counter | 1 | `result` | `action`, `resource_type`, `rejection_reason_code` | 按请求计数（含拒绝/阻断） |
| `ls_identity_isolation_request_duration_ms` | histogram | ms | `result` | `action`, `resource_type` | 端到端耗时分布（p50/p95/p99） |
| `ls_identity_isolation_violations_total` | counter | 1 | `violation_type` | `resource_type` | 隔离违规/越权计数 |
| `ls_identity_isolation_blocks_total` | counter | 1 | `block_type` |  | 阻断事件计数（门禁/依赖不可用等） |
| `ls_identity_isolation_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`org_id`/`version_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `user_id`/`org_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `action`, `resource_type`, `result`, `user_id`, `org_id`, `version_id`
- 条件必填（若适用）：`request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（鉴权决策、隔离校验、删除/保留审计）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`user_id`, `org_id`, `version_id`；以及 `request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-0 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（鉴权决策）**：月度成功率 SHALL ≥ 99.9%（不含客户端拒绝）
- **延迟（鉴权决策）**：p95 `ls_identity_isolation_request_duration_ms` SHALL ≤ 50ms
- **隔离违规监控**：`ls_identity_isolation_violations_total` 的异常抬升 MUST 告警并可审计

