# 校对工作流与QA — 可观测与指标（规格层）

本文件定义 `proofreading-workflow-qa` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_proofreading_tasks_total` | counter | 1 | `status` |  | 校对任务计数（按状态） |
| `ls_proofreading_defects_total` | counter | 1 | `severity` | `category` | 缺陷计数（按严重度/类别） |
| `ls_proofreading_approvals_total` | counter | 1 | `decision` | `approver_role` | 批准计数（APPROVE/REJECT） |
| `ls_proofreading_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`task_id`/`defect_id`/`approval_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按单次任务精确定位，MUST 依赖 logs/traces/audit（见下文）。

## 2) Logs（结构化字段：最小集合）

每条关键事件日志 MUST 以结构化字段输出，并满足可追溯性：
- 必填：`timestamp`, `event_type`, `corpus_release_id`, `version_id`, `result`
- 条件必填（若适用）：`task_id`, `defect_id`, `approval_id`, `chain_id`, `request_id`, `trace_id`
- 失败必填：`rejection_reason_code`（或 `block_type`）

## 3) Traces（最小）

- 关键路径（缺陷登记、证据解析、批准写入、审计导出）SHALL 产生 trace/span。
- span 属性 MUST 至少包含：`corpus_release_id`, `version_id`；以及 `request_id/trace_id`（若适用）。

## 4) SLO（最小阈值）

以下阈值用于 `资产门禁` 的最小商业化基线；具体值可在后续迭代中收敛，但必须可执行、可判定：

- **审计可用性**：关键事件审计写入失败率 SHALL ≤ 0.01%（以 `ls_proofreading_audit_records_total` 与失败日志口径判定）
- **导出可用性**：审计导出失败 MUST 被记录并阻断资产晋级

