# LLM叙述层 — 安全与隔离边界（规格层）

本文件定义 `llm-narrative-layer` 在安全/访问控制/隔离方面的最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- 叙述输出（`NarrativeOutput`）、提示/模型版本记录、引用绑定与内容安全审计属于高敏感产物：
  - 非授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 授权策略 MUST 可审计（审计记录至少包含 `actor_type`/`actor_id`（脱敏）与 `result`）。
- 对外暴露 SHOULD 默认最小化：仅暴露必要字段；超出范围的字段 MUST 受权限控制。

## 2) 隔离边界（user_id/org_id）

- `user_id`/`org_id` 是本能力的主隔离边界：
  - 任一叙述输出、引用绑定、内容安全审计记录不得跨越 `user_id/org_id` 的授权范围读取/写入敏感数据。
  - 若检测到跨边界访问意图，MUST 拒绝并写入审计记录（`UNAUTHORIZED`）。
- 若存在管理员/审核角色，系统 MUST 明确其授权范围与审计口径；越权访问 MUST 记录审计事件并可导出。

## 3) 敏感信息最小化

- 本能力产生的 logs/metrics/audit MUST 不包含不必要敏感信息（密钥、token、用户自由文本、完整生成内容、原始引用片段等）。
- `user_id/org_id/actor_id` 等潜在敏感标识 SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可追责关联性。

