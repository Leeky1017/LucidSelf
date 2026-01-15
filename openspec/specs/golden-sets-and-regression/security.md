# Golden Set与回归评测 — 安全与隔离边界（规格层）

本文件定义 `golden-sets-and-regression` 在安全/访问控制/隔离方面的最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- golden set 定义、阈值更新、回归运行触发与审计导出属于高权限操作：
  - 非授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 授权策略 MUST 可审计（审计记录至少包含 `actor_type`/`actor_id`（脱敏）与 `result`）。
- 评测结果读取与导出 MUST 遵循最小化原则：仅暴露必要字段；超出范围的字段 MUST 受权限控制。

## 2) 隔离边界（user_id/org_id）

- 当请求上下文包含 `user_id`/`org_id` 时，系统 MUST 将其作为隔离边界：
  - 任一 golden set/回归结果/漂移告警不得跨越 `user_id/org_id` 的授权范围读取/写入敏感数据。
  - 若检测到跨边界访问意图，MUST 拒绝并写入审计记录（`UNAUTHORIZED`）。
- 若本能力为系统级评测（与单一 `user_id/org_id` 无关），系统 MUST 明确其为“全局域”，并仅允许被授权的系统/服务账户调用；普通用户上下文 MUST 被拒绝或被忽略且可审计（实现可选，但口径必须明确）。

## 3) 敏感信息最小化

- 本能力产生的 logs/metrics/audit MUST 不包含不必要敏感原文（密钥、token、用户自由文本等）。
- `user_id/org_id/actor_id` 等潜在敏感标识 SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可追责关联性。

