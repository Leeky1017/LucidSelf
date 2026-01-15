# 语料治理 — 审计日志（字段/脱敏/导出结构）

本文件定义 `corpus-governance` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | ASSET_REGISTER/LICENSE_CHECK/LINEAGE_UPDATE/RETIREMENT 等 |
| `asset_id` | 否 | 关联资产 |
| `corpus_release_id` | 否 | 关联发布版本 |
| `version_id` | 否 | 关联版本 |
| `result` | 是 | ALLOW/DENY/BLOCK |
| `rejection_reason_code` | 否 | 拒绝原因（见契约枚举） |
| `summary` | 否 | 最小可行动摘要 |

## 2) 审计导出结构（最小）

- 导出 MUST 提供 NDJSON（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 失败并阻断。

