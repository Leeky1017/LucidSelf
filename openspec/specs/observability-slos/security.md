# 可观测性与SLO — 安全与隔离边界（规格层）

本文件定义 `observability-slos` 在观测数据访问/导出方面的安全与隔离最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 观测数据访问控制（MUST）

- 原始 logs/traces 可能包含 `user_id`/`org_id`/业务字段，访问 MUST 受最小权限控制。
- 未授权访问 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
- 对外暴露的观测视图 SHOULD 默认最小化（聚合、脱敏、低基数），避免泄露敏感信息。

## 2) 隔离边界（user_id/org_id）

- 若观测查询/导出请求包含 `user_id`/`org_id` 作用域，系统 MUST 仅返回该作用域内的数据。
- 任一跨 `user_id/org_id` 边界的观测数据访问意图 MUST 被拒绝并审计。

## 3) 脱敏与最小化

- logs/audit/traces MUST 遵循最小化原则：不得记录密钥、token、用户自由文本等不必要敏感原文。
- 对 `user_id` 等标识，若属于敏感标识，SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可审计关联性。

