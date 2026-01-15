# Playbook与行动闭环 — 数据字典与字段级约束（规格层）

本文件为 `playbook-and-action-loop` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) playbook 定义（PlaybookDefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| playbook_id | string | 是 | MUST 唯一 | playbook 标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| name | string | 是 | MUST 非空 | 名称 |
| description | string | 否 |  | 描述摘要（禁止敏感原文） |
| steps | array&lt;object&gt; | 是 | MUST 非空 | 步骤集合（最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 执行记录（ExecutionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| execution_id | string | 是 | MUST 唯一 | 执行标识 |
| playbook_id | string | 是 | MUST 非空 | 关联 playbook |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 执行版本 |
| status | string | 是 | MUST ∈ {pending, running, succeeded, failed, rolled_back} | 状态枚举 |
| started_at | string | 是 | MUST 为 ISO-8601 | 开始时间 |
| finished_at | string | 否 | MUST 为 ISO-8601（若出现） | 结束时间 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 审批记录（ApprovalRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| approval_id | string | 是 | MUST 唯一 | 审批标识 |
| execution_id | string | 是 | MUST 非空 | 关联执行 |
| user_id | string | 是 | MUST 非空 | 请求用户标识 |
| version_id | string | 是 | MUST 非空 | 审批口径版本 |
| actor_type | string | 否 | MUST ∈ {system, user, service}（若出现） | 审批者类型 |
| actor_id | string | 否 | MUST 脱敏/最小化（若出现） | 审批者标识 |
| decision | string | 是 | MUST ∈ {APPROVE, DENY} | 审批结论 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 回滚记录（RollbackRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rollback_id | string | 是 | MUST 唯一 | 回滚标识 |
| execution_id | string | 是 | MUST 非空 | 关联执行 |
| user_id | string | 是 | MUST 非空 | 请求用户标识 |
| version_id | string | 是 | MUST 非空 | 回滚口径版本 |
| reason | string | 否 |  | 回滚原因摘要（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `ExecutionRecord.playbook_id` MUST 可解析到 `PlaybookDefinition.playbook_id`；不可解析 MUST 阻断（`PLAYBOOK_NOT_FOUND` 或 `VALIDATION_FAILED`）。
- `ApprovalRecord.execution_id` MUST 可解析到 `ExecutionRecord.execution_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `RollbackRecord.execution_id` MUST 可解析到 `ExecutionRecord.execution_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
