# 滥用防护与限流 — 安全与隔离边界（规格层）

本文件定义 `abuse-and-rate-limits` 在安全/访问控制/隔离方面的最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- 策略管理、强制动作与复核属于高敏感操作：
  - 非授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 授权策略 MUST 可审计（审计记录至少包含 `actor_type`/`actor_id`（脱敏）与 `result`）。
- 对外暴露的限流/封禁信息 SHOULD 默认最小化：仅暴露必要字段；超出范围的字段 MUST 受权限控制。

## 2) 隔离边界（user_id/org_id）

- `user_id`/`org_id` 是本能力的主隔离边界：
  - 任一滥用证据、强制动作与复核记录不得跨越 `user_id/org_id` 的授权范围读取/写入敏感数据。
  - 若检测到跨边界访问意图，MUST 拒绝并写入审计记录（`UNAUTHORIZED`）。

## 3) 敏感信息最小化

- 本能力产生的 logs/metrics/audit MUST 不包含不必要敏感原文（密钥、token、用户自由文本、原始请求 payload 等）。
- `ip`/`user_id`/`org_id`/`actor_id` 等潜在敏感标识 SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可追责关联性。

