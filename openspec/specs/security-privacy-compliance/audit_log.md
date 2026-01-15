# 安全/隐私/合规 — 审计日志（字段/脱敏/导出结构）

本文件定义 `security-privacy-compliance` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | PRIVACY_REQUEST/ACCESS_CONTROL/INCIDENT 等（受控词表） |
| `result` | 是 | ALLOW/DENY/BLOCK |
| `rejection_reason_code` | 否 | 拒绝原因代码（见契约枚举） |
| `user_id` | 否 | 关联用户（若适用） |
| `org_id` | 否 | 关联组织（若适用） |
| `version_id` | 否 | 关联版本（若适用） |
| `request_id` | 否 | 请求关联标识（若适用） |
| `trace_id` | 否 | 追踪关联标识（若适用） |
| `summary` | 否 | 事件摘要（MUST 最小化且不含敏感原文） |

## 2) 脱敏与最小化（MUST）

- 审计记录 MUST 不包含不必要的敏感原文（密钥、token、用户自由文本、原始典籍全文等）。
- `user_id/org_id` 若属于敏感标识，SHOULD 进行脱敏或不可逆摘要；但 MUST 保持可审计关联性。
- `summary` MUST 为可行动的最小摘要；不得泄露敏感内容。

## 3) 审计导出结构（最小）

### 导出格式（MUST）

导出 MUST 提供 **NDJSON**（newline-delimited JSON）结构，每行一条审计记录，字段名与本文件一致。

### 导出校验（MUST）

- 导出 MUST 可通过 JSON 解析（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 视为失败并阻断。

