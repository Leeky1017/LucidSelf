# 滥用防护与限流 — 数据字典与字段级约束（规格层）

本文件为 `abuse-and-rate-limits` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 限流策略（RateLimitPolicy）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| policy_id | string | 是 | MUST 唯一 | 策略标识 |
| version_id | string | 是 | MUST 非空 | 策略版本 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| scope | string | 是 | MUST ∈ {user, org, ip} | 作用域（规格层固定） |
| limit | number | 是 | MUST ≥ 0 | 额度阈值 |
| window | string | 是 | MUST 非空 | 时间窗口（5s/1m/1h 等） |
| action | string | 是 | MUST ∈ {throttle, challenge, ban, degrade} | 动作枚举（规格层固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 滥用信号证据（AbuseSignalEvidence）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| evidence_id | string | 是 | MUST 唯一 | 证据标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 检测口径版本 |
| signal_type | string | 是 | MUST 非空 | 信号类型（枚举在规格层固定） |
| score | number | 否 |  | 风险分数（若适用） |
| chain_id | string | 否 |  | 关联证据链（若适用，可解析） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 强制动作记录（EnforcementActionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| action_id | string | 是 | MUST 唯一 | 动作标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 执行口径版本 |
| action_type | string | 是 | MUST ∈ {BAN, CHALLENGE, DEGRADE, THROTTLE} | 动作类型枚举 |
| result | string | 是 | MUST ∈ {ALLOW, DENY, BLOCK} | 结果枚举 |
| rejection_reason_code | string | 否 | MUST ∈ 契约枚举（若出现） | 拒绝/阻断原因 |
| expires_at | string | 否 | MUST 为 ISO-8601（若出现） | 过期时间 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 复核记录（ReviewRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| review_id | string | 是 | MUST 唯一 | 复核标识 |
| action_id | string | 是 | MUST 非空 | 关联动作标识 |
| actor_type | string | 是 | MUST ∈ {system, user, service} | 操作者类型 |
| actor_id | string | 否 | MUST 脱敏/最小化（若出现） | 操作者标识 |
| decision | string | 是 | MUST ∈ {CONFIRM, REVERT} | 复核结论枚举 |
| notes | string | 否 |  | 备注（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `ReviewRecord.action_id` MUST 可解析到 `EnforcementActionRecord.action_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `AbuseSignalEvidence.chain_id` 若出现 MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
