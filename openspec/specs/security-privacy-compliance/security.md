# 安全/隐私/合规 — 安全与隔离边界（规格层）

本文件定义 `security-privacy-compliance` 的安全与隔离最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- 安全/隐私/合规相关操作（隐私请求处理、合规导出、事件响应记录）属于高敏感能力：
  - 未授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 访问控制证据 MUST 可审计（见 `audit_log.md`）。

## 2) 隔离边界（user_id/org_id）

- 任一涉及用户数据的合规产物 MUST 绑定 `user_id/org_id`（或明确为全局域并受更高权限保护）。
- 任何跨 `user_id/org_id` 边界的读写/导出 MUST 被拒绝并审计（`CROSS_TENANT_ACCESS`）。

## 3) 数据最小化与脱敏（MUST）

- 记录与导出 MUST 遵循最小化原则：仅保留履约与追责所需字段。
- 日志/审计/导出 MUST 不包含不必要敏感原文（密钥、token、用户自由文本等），并执行受控脱敏策略（见契约与 `audit_log.md`）。

