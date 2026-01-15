# 语义抽取质量门禁 — 可观测与指标（规格层）

本文件定义 `semantic-extraction-quality-gates` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_semantic_extraction_quality_gate_requests_total` | counter | 1 | `result` | `event_type`, `rejection_reason_code` | 按门禁评估请求计数（含拒绝/阻断/降级） |
| `ls_semantic_extraction_quality_gate_request_duration_ms` | histogram | ms | `result` | `event_type` | 门禁评估端到端耗时分布（p50/p95/p99） |
| `ls_semantic_extraction_quality_gate_failures_total` | counter | 1 | `failure_type` |  | 失败事件计数（阈值失败/口径无效/引用不可解析等） |
| `ls_semantic_extraction_quality_gate_failure_samples_total` | counter | 1 | `result` |  | 失败样本清单写入计数 |
| `ls_semantic_extraction_quality_gate_recheck_records_total` | counter | 1 | `decision` |  | 复检记录写入计数 |
| `ls_semantic_extraction_quality_gate_drift_events_total` | counter | 1 | `drift_type` |  | 门禁判定漂移事件计数 |
| `ls_semantic_extraction_quality_gate_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`org_id`/`version_id`/`corpus_release_id`/`gate_run_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `user_id/version_id/gate_run_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `engine_id`, `version_id`, `corpus_release_id`, `result`
- 条件必填（若适用）：`user_id`, `org_id`, `gate_run_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `failure_type`）

## 3) Traces（最小）

- 门禁评估关键路径（阈值加载、指标计算/聚合、引用解析、审计写入）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`engine_id`, `version_id`, `corpus_release_id`；以及 `user_id/org_id/gate_run_id/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-1 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（门禁评估）**：月度内部错误率 SHALL ≤ 0.1%（以 `result="INTERNAL_ERROR"` 或等价口径判定）
- **延迟（门禁评估）**：p95 `ls_semantic_extraction_quality_gate_request_duration_ms` SHALL ≤ 500ms
- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_semantic_extraction_quality_gate_audit_records_total` 与失败日志口径判定）

