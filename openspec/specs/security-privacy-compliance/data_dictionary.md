# 安全/隐私/合规 — 数据字典与字段级约束（规格层）

本文件为 `security-privacy-compliance` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 数据分类标签（DataClassificationLabel）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| label_id | string | 是 | MUST 唯一；MUST 非空 | 标签标识 |
| name | string | 是 | MUST 非空；SHOULD 为受控词表 | 标签名称 |
| sensitivity | string | 是 | MUST 属于 {public, internal, confidential, secret} 或等价受控词表 | 敏感级别 |
| redaction_policy | string | 是 | MUST 属于 {none, mask, hash, drop} 或等价受控词表 | 脱敏策略 |

## 2) 访问控制证据（AccessControlEvidence）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| evidence_id | string | 是 | MUST 唯一 | 证据标识 |
| user_id | string | 是 | MUST 非空 | 主体 |
| org_id | string | 是 | MUST 非空 | 主体 |
| resource_type | string | 是 | MUST 非空 | 资源类型 |
| action | string | 是 | MUST 非空 | 动作 |
| decision | string | 是 | MUST 属于 {ALLOW, DENY, BLOCK} | 决策 |
| rejection_reason_code | string | 否 | 若提供 MUST 属于契约枚举 | 拒绝原因 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 记录时间 |

## 3) 隐私请求处理记录（PrivacyRequestRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| request_id | string | 是 | MUST 唯一 | 请求标识 |
| user_id | string | 是 | MUST 非空 | 请求用户 |
| org_id | string | 是 | MUST 非空 | 请求组织 |
| request_type | string | 是 | MUST 非空 | 请求类型（受控词表） |
| status | string | 是 | MUST 非空 | 状态（受控词表） |
| result | string | 否 | 若提供 MUST 属于 {ALLOW, DENY, BLOCK} | 完成结果 |
| rejection_reason_code | string | 否 | 若提供 MUST 属于契约枚举 | 拒绝原因 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

**完整性语义（最小）**
- `request_id` MUST 唯一；重复 MUST 幂等或冲突（见 `design.md`）。

## 4) 事件响应记录（IncidentResponseRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| incident_id | string | 是 | MUST 唯一 | 事件标识 |
| severity | string | 是 | MUST 非空 | 严重级别 |
| status | string | 是 | MUST 非空 | 处置状态 |
| summary | string | 是 | MUST 非空；MUST 不含敏感原文 | 摘要 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |
| resolved_at | string | 否 | 若提供 MUST 为 ISO-8601 | 解决时间 |

