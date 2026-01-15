# 身份与数据隔离 — 数据字典与字段级约束（规格层）

本文件为 `identity-and-data-isolation` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 身份声明（IdentityClaim）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| user_id | string | 是 | MUST 非空；SHOULD 为稳定非 PII 标识 | 用户主边界 |
| org_id | string | 是 | MUST 非空；SHOULD 为稳定标识 | 组织/租户边界 |
| version_id | string | 是 | MUST 非空；SHOULD 满足 `^ver_[a-z0-9]{12,}$` | 版本标识 |
| request_id | string | 否 | 若提供 MUST 非空 | 请求关联 |
| trace_id | string | 否 | 若提供 MUST 非空 | 追踪关联 |
| issued_at | string | 否 | 若提供 MUST 为 ISO-8601 | 声明时间 |
| auth_method | string | 否 | 若提供 MUST 不泄露敏感凭据 | 认证方式 |

**完整性语义（最小）**
- `user_id`/`org_id` MUST 在同一请求上下文中保持一致；不一致 MUST 被拒绝并形成审计事件。

## 2) 访问控制决策记录（AccessControlDecisionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| decision_id | string | 是 | MUST 唯一 | 决策标识 |
| user_id | string | 是 | MUST 非空 | 主体 |
| org_id | string | 是 | MUST 非空 | 主体 |
| resource_type | string | 是 | MUST 非空 | 资源类型 |
| resource_id | string | 是 | MUST 非空；MUST 最小化/脱敏 | 资源标识 |
| action | string | 是 | MUST 非空 | 动作 |
| decision | string | 是 | MUST 属于 {ALLOW, DENY, BLOCK} | 决策结果 |
| rejection_reason_code | string | 否 | 若提供 MUST 属于契约枚举 rejection_reasons[*].code | 拒绝原因 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 决策时间 |
| request_id | string | 否 | 若提供 MUST 非空 | 请求关联 |
| trace_id | string | 否 | 若提供 MUST 非空 | 追踪关联 |

**完整性语义（最小）**
- `resource_id` MUST 采用最小化原则；禁止写入敏感原文。

## 3) 隔离违规审计（IsolationViolationAuditEvent）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| event_id | string | 是 | MUST 唯一 | 事件标识 |
| user_id | string | 是 | MUST 非空 | 主体 |
| org_id | string | 是 | MUST 非空 | 主体 |
| attempted_user_id | string | 否 | 若提供 MUST 最小化/脱敏 | 被尝试访问的 user |
| attempted_org_id | string | 否 | 若提供 MUST 最小化/脱敏 | 被尝试访问的 org |
| resource_type | string | 是 | MUST 非空 | 资源类型 |
| resource_id | string | 是 | MUST 非空；MUST 最小化/脱敏 | 资源标识 |
| action | string | 是 | MUST 非空 | 动作 |
| result | string | 是 | MUST 属于 {DENY, BLOCK} | 结果 |
| rejection_reason_code | string | 是 | MUST 属于契约枚举 | 拒绝原因 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| occurred_at | string | 是 | MUST 为 ISO-8601 | 发生时间 |
| request_id | string | 否 | 若提供 MUST 非空 | 请求关联 |
| trace_id | string | 否 | 若提供 MUST 非空 | 追踪关联 |

**完整性语义（最小）**
- 任何跨 `user_id`/`org_id` 的访问意图 MUST 产生此类事件或等价审计记录。

## 4) 删除/保留审计（DeletionRetentionAuditRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| audit_id | string | 是 | MUST 唯一 | 审计标识 |
| user_id | string | 是 | MUST 非空 | 关联用户 |
| org_id | string | 是 | MUST 非空 | 关联组织 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| action | string | 是 | MUST 属于 {DELETE, RETENTION} | 动作 |
| data_category | string | 是 | MUST 非空 | 数据类别 |
| result | string | 是 | MUST 属于 {ALLOW, DENY, BLOCK} | 结果 |
| created_at | string | 是 | MUST 为 ISO-8601 | 记录时间 |

**完整性语义（最小）**
- 删除与保留策略执行结果 MUST 可审计（至少可按 `user_id`/`org_id`/时间窗口定位）。

