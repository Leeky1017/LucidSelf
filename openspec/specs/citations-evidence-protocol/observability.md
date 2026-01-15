# 引用与证据协议 — 可观测与指标（规格层）

本文件定义 `citations-evidence-protocol` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_citations_evidence_requests_total` | counter | 1 | `result` | `event_type`, `rejection_reason_code` | 按请求计数（含拒绝/阻断） |
| `ls_citations_evidence_request_duration_ms` | histogram | ms | `result` | `event_type` | 端到端耗时分布（p50/p95/p99） |
| `ls_citations_evidence_anchor_resolution_failures_total` | counter | 1 | `failure_type` |  | 引用锚点解析失败计数 |
| `ls_citations_evidence_drift_events_total` | counter | 1 | `drift_type` |  | 证据链漂移/偏差事件计数 |
| `ls_citations_evidence_audit_exports_total` | counter | 1 | `result` |  | 审计导出计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`org_id`/`version_id`/`corpus_release_id`/`chain_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `user_id`/`version_id`/`chain_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `result`, `version_id`, `corpus_release_id`
- 条件必填（若适用）：`chain_id`, `anchor_id`, `asset_id`, `request_id`, `trace_id`, `user_id`, `org_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（证据链校验/生成、引用锚点解析、审计导出）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`version_id`, `corpus_release_id`；以及 `chain_id/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-1 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（证据链校验）**：月度成功率 SHALL ≥ 99.9%（不含客户端拒绝）
- **可用性（审计导出）**：月度成功率 SHALL ≥ 99.5%（不含客户端拒绝）
- **延迟（证据链校验）**：p95 `ls_citations_evidence_request_duration_ms` SHALL ≤ 200ms
- **延迟（审计导出触发）**：p95 `ls_citations_evidence_request_duration_ms` SHALL ≤ 500ms（以触发端到端耗时口径判定）

