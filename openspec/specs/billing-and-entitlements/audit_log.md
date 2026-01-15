# 计费与权益 — 审计日志（字段/脱敏/导出结构）

本文件定义 `billing-and-entitlements` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | ENTITLEMENT_CHECK/USAGE_EVENT_INGEST/BILLING_RECORD_GENERATE/BILLING_RECORD_VOID/DISPUTE_OPEN/DISPUTE_RESOLVE/AUDIT_EXPORT |
| `user_id` | 否 | 用户标识（隔离边界；若适用） |
| `org_id` | 否 | 组织标识（若适用） |
| `version_id` | 是 | 版本标识 |
| `result` | 是 | PASS/DENY/BLOCK |
| `rejection_reason_code` | 否 | 拒绝/阻断原因代码（见契约枚举） |
| `entitlement_id` | 否 | 关联权益（若适用） |
| `usage_event_id` | 否 | 关联用量事件（若适用） |
| `billing_record_id` | 否 | 关联计费记录（若适用） |
| `dispute_id` | 否 | 关联争议（若适用） |
| `chain_id` | 否 | 关联证据链（若适用） |
| `currency` | 否 | 币种代码（若适用） |
| `amount` | 否 | 金额（若适用，禁止敏感支付信息） |
| `actor_type` | 否 | system/user/service（若适用） |
| `actor_id` | 否 | 操作者标识（必须脱敏/最小化） |
| `request_id` | 否 | 请求关联标识（若适用） |
| `trace_id` | 否 | 追踪关联标识（若适用） |

## 2) 脱敏与最小化（MUST）

- 审计记录 MUST 不包含不必要的敏感原文（例如：密钥、token、用户自由文本、支付卡号/支付凭据等）。
- `actor_id`/`user_id`/`org_id` 若属于敏感标识，SHOULD 进行脱敏或不可逆摘要；但 MUST 保持可审计关联性。
- 对外导出时 MUST 保留可定位问题所需的最小字段：`audit_id`, `created_at`, `event_type`, `version_id`, `result`, `rejection_reason_code`（若适用）。

## 3) 审计导出结构（最小）

### 导出格式（MUST）

导出 MUST 提供 **NDJSON**（newline-delimited JSON）结构，每行一条审计记录，字段名与本文件一致。

### 导出校验（MUST）

- 导出 MUST 可通过 JSON 解析（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 视为失败并阻断。

