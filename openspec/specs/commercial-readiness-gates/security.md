# 商业化就绪门禁 — 安全与隔离边界（规格层）

本文件定义 `commercial-readiness-gates` 在安全/访问控制/隔离方面的最小契约。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 访问控制（最小）

- 就绪清单、审批记录与发布许可证据属于高敏感产物（影响对客户开放与法律/财务风险）：
  - 非授权请求 MUST 被拒绝（`UNAUTHORIZED`）并写入审计记录。
  - 授权策略 MUST 可审计（审计记录至少包含 `actor_type`/`actor_id`（脱敏）与 `result`）。
- 审批链相关操作 MUST 采用最小权限：仅具备相应角色/职责的主体可执行 APPROVE/REJECT。

## 2) 隔离边界（user_id/org_id）

- 若门禁评估面向特定租户/组织，`org_id` MUST 作为隔离边界：
  - 任一审批记录、许可证据不得跨越 `org_id` 的授权范围读取/写入敏感数据。
  - 若检测到跨边界访问意图，MUST 拒绝并写入审计记录（`UNAUTHORIZED`）。

## 3) 敏感信息最小化

- logs/metrics/audit MUST 不包含不必要敏感信息（密钥、token、客户合同信息、支付信息、用户自由文本等）。
- `actor_id`/`org_id` 等潜在敏感标识 SHOULD 采用脱敏或不可逆摘要；但 MUST 保持可追责关联性。

