# 文本归一化与对齐 — 可观测与指标（规格层）

本文件定义 `text-normalization-alignment` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_text_norm_requests_total` | counter | 1 | `result` | `event_type`, `rejection_reason_code` | 按变换/对齐请求计数（含拒绝/阻断） |
| `ls_text_norm_request_duration_ms` | histogram | ms | `result` | `event_type` | 端到端耗时分布（p50/p95/p99） |
| `ls_text_norm_conflicts_total` | counter | 1 | `conflict_type` |  | 冲突/歧义计数 |
| `ls_text_norm_exception_items_total` | counter | 1 | `exception_type` |  | 例外条目计数 |
| `ls_text_norm_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`corpus_release_id`/`version_id`/资产 ID/原文片段等 SHOULD NOT 作为默认 metric 标签。
- 若需要按具体资产/版本定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `result`, `corpus_release_id`, `version_id`
- 条件必填（若适用）：`rule_set_id`, `mapping_id`, `audit_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（归一化变换、对齐映射、冲突检测、审计导出）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`corpus_release_id`, `version_id`；以及 `request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于资产门禁的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（归一化/对齐变换）**：月度成功率 SHALL ≥ 99.0%（不含客户端拒绝）
- **延迟（变换控制面）**：p95 `ls_text_norm_request_duration_ms` SHALL ≤ 500ms（以事件类型区分口径判定）

