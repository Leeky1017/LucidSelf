# 引擎ID治理 — 可观测与指标（规格层）

本文件定义 `engine-id-governance` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_engine_governance_requests_total` | counter | 1 | `result` | `event_type`, `rejection_reason_code` | 按请求计数（含拒绝/阻断） |
| `ls_engine_governance_request_duration_ms` | histogram | ms | `result` | `event_type` | 端到端耗时分布（p50/p95/p99） |
| `ls_engine_governance_blocks_total` | counter | 1 | `block_type` | `event_type` | 阻断事件计数（门禁/依赖不可用等） |
| `ls_engine_governance_registry_integrity_failures_total` | counter | 1 | `failure_type` |  | 完整性校验失败计数（引用不可解析/冲突等） |
| `ls_engine_governance_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`engine_id`/`version_id`/`user_id`/`org_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `engine_id`/`version_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `engine_id`, `version_id`, `result`
- 条件必填（若适用）：`request_id`, `trace_id`, `user_id`, `org_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（注册/状态变更/弃用替代/审计导出）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`engine_id`, `version_id`；以及 `request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-0 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（治理读操作）**：月度成功率 SHALL ≥ 99.9%（不含客户端拒绝）
- **可用性（治理写操作）**：月度成功率 SHALL ≥ 99.5%（不含客户端拒绝）
- **延迟（治理读操作）**：p95 `ls_engine_governance_request_duration_ms` SHALL ≤ 100ms
- **延迟（治理写操作）**：p95 `ls_engine_governance_request_duration_ms` SHALL ≤ 200ms

