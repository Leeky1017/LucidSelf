# 计费与权益 — 数据字典与字段级约束（规格层）

本文件为 `billing-and-entitlements` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 权益定义（EntitlementDefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| entitlement_id | string | 是 | MUST 唯一 | 权益定义标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 权益口径版本标识 |
| plan_id | string | 否 |  | 套餐/计划（若适用） |
| product_id | string | 否 |  | 产品标识（若适用） |
| status | string | 是 | MUST ∈ {active, suspended, expired} | 状态枚举（规格层固定） |
| limits | object | 否 |  | 权益额度/限制（最小化；禁止敏感支付信息） |
| effective_from | string | 是 | MUST 为 ISO-8601 | 生效时间 |
| effective_to | string | 否 | MUST 为 ISO-8601（若出现） | 失效时间 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 用量事件（UsageEvent）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| usage_event_id | string | 是 | MUST 唯一 | 用量事件标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 计量口径版本标识 |
| event_type | string | 是 | MUST 非空 | 事件类型（枚举在规格层固定） |
| quantity | number | 是 | MUST ≥ 0 | 数量 |
| unit | string | 是 | MUST 非空 | 单位（tokens/requests/bytes 等） |
| occurred_at | string | 是 | MUST 为 ISO-8601 | 发生时间 |
| idempotency_key | string | 否 |  | 幂等键（若适用，用于去重） |
| source_request_id | string | 否 |  | 源请求标识（若适用） |

## 3) 计费记录（BillingRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| billing_record_id | string | 是 | MUST 唯一 | 计费记录标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 计费规则版本标识 |
| period_start | string | 是 | MUST 为 ISO-8601 | 周期开始 |
| period_end | string | 是 | MUST 为 ISO-8601 | 周期结束 |
| currency | string | 是 | MUST 为 ISO-4217 | 币种代码（例如 CNY/USD） |
| amount | number | 是 | MUST ≥ 0 | 金额（口径固定） |
| status | string | 是 | MUST ∈ {pending, issued, paid, void} | 状态枚举（规格层固定） |
| line_items | array&lt;object&gt; | 否 |  | 明细行（最小化；禁止敏感支付信息） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 争议证据链（DisputeEvidenceChain）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| dispute_id | string | 是 | MUST 唯一 | 争议标识 |
| billing_record_id | string | 是 | MUST 非空 | 关联计费记录 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 争议处理/证据口径版本 |
| chain_id | string | 是 | MUST 非空 | 关联证据链（可解析） |
| status | string | 是 | MUST ∈ {open, resolved} | 状态枚举（规格层固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `DisputeEvidenceChain.billing_record_id` MUST 可解析到 `BillingRecord.billing_record_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `DisputeEvidenceChain.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- 同一计费周期内的 `UsageEvent.user_id/org_id` MUST 与其被计入的 `BillingRecord.user_id/org_id` 一致；不一致 MUST 视为越权或数据污染并阻断（`UNAUTHORIZED` 或 `VALIDATION_FAILED`）。
