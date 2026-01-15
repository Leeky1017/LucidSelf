# LLM叙述层 — 可观测与指标（规格层）

本文件定义 `llm-narrative-layer` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_llm_narrative_requests_total` | counter | 1 | `result` | `rejection_reason_code` | 叙述生成请求计数（含拒绝/阻断） |
| `ls_llm_narrative_request_duration_ms` | histogram | ms | `result` |  | 端到端耗时分布（p50/p95/p99） |
| `ls_llm_narrative_citation_binding_failures_total` | counter | 1 | `failure_type` |  | 引用绑定/解析失败计数 |
| `ls_llm_narrative_safety_blocks_total` | counter | 1 | `policy_id` |  | 内容安全阻断计数 |
| `ls_llm_narrative_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`prompt_id`/`model_version_id`/`output_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `output_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `engine_id`, `version_id`, `result`
- 条件必填（若适用）：`user_id`, `prompt_id`, `model_version_id`, `output_id`, `chain_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（叙述生成、引用绑定/解析、安全审计、审计写入）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`engine_id`, `version_id`；以及 `prompt_id/model_version_id/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-2 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（叙述生成）**：月度内部错误率 SHALL ≤ 0.1%（以 `result="INTERNAL_ERROR"` 或等价口径判定）
- **延迟（叙述生成）**：p95 `ls_llm_narrative_request_duration_ms` SHALL ≤ 2,000ms
- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_llm_narrative_audit_records_total` 与失败日志口径判定）

