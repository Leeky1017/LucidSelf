# 身份与数据隔离 — 安全与隔离边界（规格层）

本文件定义 `identity-and-data-isolation` 的安全/访问控制/隔离最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 隔离边界（MUST）

- `user_id` 是用户数据读写隔离的主边界；`org_id` 是多租户隔离边界。
- 任一数据读写/导出/检索请求 MUST 绑定到明确的 `user_id` 与 `org_id`（或在规格中明确其为全局域并受高权限保护）。
- 请求试图跨越 `user_id/org_id` 的隔离边界 MUST 被拒绝（`CROSS_TENANT_ACCESS` 或 `UNAUTHORIZED`）并写入审计记录。

## 2) 访问控制（最小）

- 系统 MUST 对每次受保护资源访问产生可审计的决策结果（ALLOW/DENY/BLOCK）。
- 对于敏感操作（例如 DELETE、批量导出、管理员接口）MUST 采用更严格的授权策略；不满足授权 MUST 拒绝并审计。

## 3) 信息最小化与泄露控制（MUST）

- 拒绝响应与日志/audit MUST 遵循最小化原则：不得泄露不属于当前 `user_id/org_id` 的资源内容或敏感原文。
- 在跨租户访问被拒绝时，系统 SHOULD 避免泄露“目标资源是否存在”的额外信息；但 MUST 保留可审计线索（见 `audit_log.md`）。

