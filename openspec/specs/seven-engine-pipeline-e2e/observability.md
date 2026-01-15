# 七引擎流水线E2E — 可观测与指标（规格层）

本文件定义 `seven-engine-pipeline-e2e` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_e2e_pipeline_runs_total` | counter | 1 | `result` | `block_type` | E2E 执行计数（含拒绝/阻断） |
| `ls_e2e_pipeline_run_duration_ms` | histogram | ms | `result` |  | 端到端耗时分布（p50/p95/p99） |
| `ls_e2e_pipeline_handoff_failures_total` | counter | 1 | `stage` | `failure_type` | 阶段交接失败计数 |
| `ls_e2e_pipeline_recovery_actions_total` | counter | 1 | `action` |  | 失败恢复动作计数（RETRY/ROLLBACK/DEGRADE/ABORT） |
| `ls_e2e_pipeline_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`run_id`/`trace_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按单次执行精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `engine_id`, `version_id`, `corpus_release_id`, `result`
- 条件必填（若适用）：`user_id`, `run_id`, `stage_id`, `from_stage_id`, `to_stage_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 端到端执行（含各阶段处理与交接校验）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`engine_id`, `version_id`, `corpus_release_id`；以及 `run_id/stage_id/request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 Gate-2 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **可用性（E2E 执行）**：月度内部错误率 SHALL ≤ 0.1%（以 `result="INTERNAL_ERROR"` 或等价口径判定）
- **延迟（E2E 执行）**：p95 `ls_e2e_pipeline_run_duration_ms` SHALL ≤ 10,000ms
- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_e2e_pipeline_audit_records_total` 与失败日志口径判定）

