# 校对工作流与QA — 数据字典与字段约束（规格层）

本文件定义 `proofreading-workflow-qa` 的关键产物数据字典与字段级约束（规格层）。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 校对任务（ProofreadingTask）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| task_id | string | 是 | MUST 唯一 | 任务标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| scope | object | 是 | MUST 非空 | 校对范围（结构化） |
| assignee_id | string | 否 |  | 指派标识（脱敏/最小化） |
| status | string | 是 | MUST ∈ {OPEN, IN_REVIEW, DONE} | 状态枚举 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 缺陷记录（DefectRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| defect_id | string | 是 | MUST 唯一 | 缺陷标识 |
| task_id | string | 是 | MUST 非空 | 关联校对任务 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| severity | string | 是 | MUST ∈ {P0, P1, P2} | 严重度 |
| category | string | 是 | MUST 非空 | 缺陷类别（口径固定） |
| chain_id | string | 否 |  | 证据链标识（若适用） |
| status | string | 是 | MUST ∈ {OPEN, FIXED, WONTFIX} | 状态枚举 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 批准记录（ApprovalRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| approval_id | string | 是 | MUST 唯一 | 批准标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| approver_role | string | 是 | MUST 非空 | 批准角色 |
| approver_id | string | 否 |  | 批准人标识（脱敏/最小化） |
| decision | string | 是 | MUST ∈ {APPROVE, REJECT} | 批准结论 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) QA 指标报表（QAMetricsReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报表标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| window_start | string | 是 | MUST 为 ISO-8601 | 统计窗口开始 |
| window_end | string | 是 | MUST 为 ISO-8601 | 统计窗口结束 |
| defects_total | number | 是 | MUST ≥ 0 | 缺陷总数 |
| p0_defects_total | number | 否 | MUST ≥ 0 | P0 缺陷数（若适用） |
| approval_rate | number | 否 | SHOULD ∈ [0,1] | 批准率（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `DefectRecord.task_id` MUST 可解析到 `ProofreadingTask.task_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `DefectRecord.chain_id` 若出现 MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。

