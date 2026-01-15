# Playbook与行动闭环 — 安全与隔离边界（规格层）

本文件定义 `playbook-and-action-loop` 在安全/访问控制/隔离方面的最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- playbook 定义变更、执行、审批与回滚属于高敏感操作：
  - 非授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 授权策略 MUST 可审计（审计记录至少包含 `actor_type`/`actor_id`（脱敏）与 `result`）。
- 审批链路 MUST 可审计且不可绕过；绕过审批的执行 MUST 被阻断并记录审计事件。

## 2) 隔离边界（user_id/org_id 的适用方式）

- `user_id` 是本能力的主隔离边界：
  - 任一 playbook 定义/执行/审批/回滚记录不得跨越 `user_id` 的授权范围读取/写入敏感数据。
  - 若检测到跨边界访问意图，MUST 拒绝并写入审计记录（`UNAUTHORIZED`）。
- 若本能力引入 `org_id`（例如团队 playbook/组织级审批），系统 MUST 明确其隔离边界与授权范围，并同样满足可审计与越权阻断。

## 3) 敏感信息最小化

- 本能力产生的 logs/metrics/audit MUST 不包含不必要敏感原文（密钥、token、用户自由文本、行动细节原文等）。
- `user_id/actor_id` 等潜在敏感标识 SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可追责关联性。

