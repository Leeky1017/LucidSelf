# 语料发布流水线 — 审计日志（字段/脱敏/导出结构）

本文件定义 `corpus-release-pipeline` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | CORPUS_STAGE_RUN/CORPUS_VALIDATION_REPORT/CORPUS_RELEASE_PUBLISH/CORPUS_ROLLBACK/AUDIT_EXPORT |
| `corpus_release_id` | 是 | 语料发布版本标识 |
| `version_id` | 是 | 口径版本标识 |
| `stage_name` | 否 | 关联阶段（若适用） |
| `stage_id` | 否 | 阶段记录标识（若适用） |
| `report_id` | 否 | 校验报告标识（若适用） |
| `artifact_id` | 否 | 产物标识（若适用） |
| `rollback_id` | 否 | 回滚标识（若适用） |
| `result` | 是 | PASS/DENY/BLOCK |
| `rejection_reason_code` | 否 | 拒绝/阻断原因代码（见契约枚举） |
| `actor_type` | 否 | system/user/service（若适用） |
| `actor_id` | 否 | 操作者标识（必须脱敏/最小化） |
| `request_id` | 否 | 请求关联标识（若适用） |
| `trace_id` | 否 | 追踪关联标识（若适用） |

## 2) 脱敏与最小化（MUST）

- 审计记录 MUST 不包含不必要的敏感原文（例如：密钥、token、典籍全文、资产原始内容等）。
- `actor_id` 若属于敏感标识，SHOULD 进行脱敏或不可逆摘要；但 MUST 保持可审计关联性。
- 对外导出时 MUST 保留可定位问题所需的最小字段：`audit_id`, `created_at`, `event_type`, `corpus_release_id`, `version_id`, `result`, `rejection_reason_code`（若适用）。

## 3) 审计导出结构（最小）

### 导出格式（MUST）

导出 MUST 提供 **NDJSON**（newline-delimited JSON）结构，每行一条审计记录，字段名与本文件一致。

### 导出校验（MUST）

- 导出 MUST 可通过 JSON 解析（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 视为失败并阻断。

