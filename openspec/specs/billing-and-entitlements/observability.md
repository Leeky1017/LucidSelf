# 计费与权益 — 可观测与指标（规格层）

本文件定义 `billing-and-entitlements` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_billing_entitlements_requests_total` | counter | 1 | `result` | `event_type`, `rejection_reason_code` | 按请求计数（权益校验/计量/计费/争议） |
| `ls_billing_entitlements_request_duration_ms` | histogram | ms | `result` | `event_type` | 端到端耗时分布（p50/p95/p99） |
| `ls_billing_usage_events_total` | counter | 1 | `result` |  | 用量事件入账计数（含拒绝/冲突） |
| `ls_billing_billing_records_total` | counter | 1 | `result` | `status` | 计费记录生成/更新计数 |
| `ls_billing_disputes_total` | counter | 1 | `status` |  | 争议开启/关闭计数 |
| `ls_billing_drift_events_total` | counter | 1 | `drift_type` |  | 计费漂移事件计数 |
| `ls_billing_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`org_id`/`version_id`/`billing_record_id`/`usage_event_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `user_id/org_id/version_id/billing_record_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `version_id`, `result`
- 条件必填（若适用）：`user_id`, `org_id`, `entitlement_id`, `usage_event_id`, `billing_record_id`, `dispute_id`, `chain_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（权益校验、用量入账、计费记录生成、争议证据链关联、审计导出）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`version_id`；以及 `user_id/org_id/billing_record_id/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-3 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（计费关键路径）**：月度内部错误率 SHALL ≤ 0.05%（以 `result="INTERNAL_ERROR"` 或等价口径判定）
- **延迟（权益校验）**：p95 `ls_billing_entitlements_request_duration_ms` SHALL ≤ 50ms（以事件类型区分口径判定）
- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_billing_audit_records_total` 与失败日志口径判定）

