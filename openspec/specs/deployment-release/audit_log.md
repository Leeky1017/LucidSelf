# 部署与发布 — 审计日志（字段/脱敏/导出结构）

本文件定义 `deployment-release` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | RELEASE_MANIFEST_PUBLISH/PROMOTION_ATTEMPT/VERIFICATION_RUN/ROLLBACK_TRIGGER/ROLLBACK_EXECUTE/AUDIT_EXPORT |
| `version_id` | 是 | 版本标识 |
| `from_env` | 否 | 来源环境（若适用） |
| `to_env` | 否 | 目标环境（若适用） |
| `environment_id` | 否 | 环境标识（若适用） |
| `result` | 是 | PASS/DENY/BLOCK |
| `rejection_reason_code` | 否 | 拒绝/阻断原因代码（见契约枚举） |
| `promotion_id` | 否 | 关联晋级记录（若适用） |
| `report_id` | 否 | 关联验证报告（若适用） |
| `rollback_id` | 否 | 关联回滚记录（若适用） |
| `actor_type` | 否 | system/user/service（若适用） |
| `actor_id` | 否 | 操作者标识（必须脱敏/最小化） |
| `request_id` | 否 | 请求关联标识（若适用） |
| `trace_id` | 否 | 追踪关联标识（若适用） |

## 2) 脱敏与最小化（MUST）

- 审计记录 MUST 不包含不必要的敏感原文（例如：密钥、token、用户自由文本、部署凭据等）。
- `actor_id` 若属于敏感标识，SHOULD 进行脱敏或不可逆摘要；但 MUST 保持可审计关联性。
- 对外导出时 MUST 保留可定位问题所需的最小字段：`audit_id`, `created_at`, `event_type`, `version_id`, `result`, `rejection_reason_code`（若适用）。

## 3) 审计导出结构（最小）

### 导出格式（MUST）

导出 MUST 提供 **NDJSON**（newline-delimited JSON）结构，每行一条审计记录，字段名与本文件一致。

### 导出校验（MUST）

- 导出 MUST 可通过 JSON 解析（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 视为失败并阻断。

