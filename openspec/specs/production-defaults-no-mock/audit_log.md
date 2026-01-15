# 生产默认值（禁止Mock）— 审计日志（字段/脱敏/导出结构）

本文件定义 `production-defaults-no-mock` 的审计日志最小契约：字段集合、脱敏规则与导出结构。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 审计字段（最小集合）

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `audit_id` | 是 | 审计记录唯一标识 |
| `created_at` | 是 | ISO-8601 时间戳 |
| `event_type` | 是 | CONFIG_CHECK/MOCK_VIOLATION/STARTUP_FAILURE 等（受控词表） |
| `version_id` | 是 | 关联版本 |
| `environment` | 否 | 环境（若适用） |
| `result` | 是 | ALLOW/DENY/BLOCK |
| `reason_code` | 否 | 原因代码（见契约枚举） |
| `summary` | 否 | 最小可行动摘要（不得含敏感原文） |

## 2) 脱敏与最小化（MUST）

- 审计记录 MUST 不包含密钥、token 或不必要敏感原文。
- `summary` MUST 为最小可行动摘要；不得泄露敏感内容。

## 3) 审计导出结构（最小）

- 导出 MUST 提供 NDJSON（每行独立有效 JSON）。
- 导出 MUST 包含所有必填字段；缺失 MUST 失败并阻断。

