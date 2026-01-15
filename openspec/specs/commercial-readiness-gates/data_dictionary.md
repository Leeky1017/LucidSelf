# 商业化就绪门禁 — 数据字典与字段约束（规格层）

本文件定义 `commercial-readiness-gates` 的关键产物数据字典与字段级约束（规格层）。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 就绪清单（ReadinessChecklist）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| checklist_id | string | 是 | MUST 唯一 | 清单标识 |
| version_id | string | 是 | MUST 非空 | 版本标识（门禁决策基准） |
| gate | string | 是 | MUST 非空 | Gate 标识（例如 Gate-3） |
| items | array&lt;object&gt; | 是 | MUST 非空 | 清单项集合（结构化） |
| status | string | 是 | MUST ∈ {PASS, BLOCK} | 清单结果 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 审批记录（ApprovalRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| approval_id | string | 是 | MUST 唯一 | 审批标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| approver_role | string | 是 | MUST 非空 | 审批角色 |
| approver_id | string | 否 |  | 审批人标识（脱敏/最小化） |
| decision | string | 是 | MUST ∈ {APPROVE, REJECT} | 审批结论 |
| reason | string | 否 |  | 原因摘要（不得包含敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 支持与应急预案（SupportAndIncidentPlan）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| plan_id | string | 是 | MUST 唯一 | 预案标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| oncall_ref | string | 是 | MUST 非空 | 值班/支持引用 |
| escalation_ref | string | 是 | MUST 非空 | 升级链引用 |
| runbook_ref | string | 是 | MUST 非空 | 运行手册引用 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 发布许可证据（ReleaseLicenseEvidence）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| evidence_id | string | 是 | MUST 唯一 | 证据标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| artifacts | array&lt;object&gt; | 是 | MUST 非空 | 证据产物清单（结构化引用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `ReadinessChecklist.version_id` MUST 与审批记录/预案/证据产物中的 `version_id` 保持一致；不一致 MUST 阻断（`VALIDATION_FAILED`）。

