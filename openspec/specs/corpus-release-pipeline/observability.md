# 语料发布流水线 — 可观测与指标（规格层）

本文件定义 `corpus-release-pipeline` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_corpus_release_pipeline_runs_total` | counter | 1 | `result` | `stage_name`, `rejection_reason_code` | 按流水线阶段运行计数 |
| `ls_corpus_release_pipeline_stage_duration_ms` | histogram | ms | `result` | `stage_name` | 阶段耗时分布（p50/p95/p99） |
| `ls_corpus_release_pipeline_validation_reports_total` | counter | 1 | `result` | `stage_name` | 校验报告产出计数 |
| `ls_corpus_release_pipeline_rollbacks_total` | counter | 1 | `result` |  | 回滚执行计数 |
| `ls_corpus_release_pipeline_drift_events_total` | counter | 1 | `drift_type` |  | 发布漂移事件计数 |
| `ls_corpus_release_pipeline_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`corpus_release_id`/`version_id`/`artifact_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `corpus_release_id` 精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `corpus_release_id`, `version_id`, `result`
- 条件必填（若适用）：`stage_name`, `stage_id`, `report_id`, `artifact_id`, `rollback_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（阶段执行、校验、产物生成、回滚、审计写入）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`corpus_release_id`, `version_id`；以及 `stage_name/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-2 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（流水线控制面）**：月度内部错误率 SHALL ≤ 0.1%（以 `result="INTERNAL_ERROR"` 或等价口径判定）
- **延迟（关键阶段）**：p95 `ls_corpus_release_pipeline_stage_duration_ms` SHALL ≤ 300,000ms（5 分钟；以 `stage_name` 区分口径判定）
- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_corpus_release_pipeline_audit_records_total` 与失败日志口径判定）

