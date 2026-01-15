# LLM叙述层 — 数据字典与字段级约束（规格层）

本文件为 `llm-narrative-layer` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 叙述输出（NarrativeOutput）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| output_id | string | 是 | MUST 唯一 | 输出标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 叙述层版本 |
| prompt_id | string | 是 | MUST 非空 | 提示标识 |
| model_version_id | string | 是 | MUST 非空 | 模型版本标识 |
| output_schema_version | string | 是 | MUST 非空 | schema 版本 |
| sections | array&lt;object&gt; | 是 | MUST 非空 | 结构化段落（内容需合规） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 提示版本记录（PromptVersionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| prompt_id | string | 是 | MUST 非空 | 提示标识 |
| prompt_version | string | 是 | MUST 非空 | 提示版本 |
| version_id | string | 是 | MUST 非空 | 记录版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 模型版本记录（ModelVersionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| model_version_id | string | 是 | MUST 唯一 | 模型版本标识 |
| provider | string | 是 | MUST 非空 | 提供方 |
| model_name | string | 是 | MUST 非空 | 模型名称 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 引用绑定（CitationBinding）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| binding_id | string | 是 | MUST 唯一 | 绑定标识 |
| output_id | string | 是 | MUST 非空 | 关联输出 |
| chain_id | string | 是 | MUST 非空 | 关联证据链 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 5) 内容安全审计（ContentSafetyAudit）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| safety_audit_id | string | 是 | MUST 唯一 | 安全审计标识 |
| output_id | string | 是 | MUST 非空 | 关联输出 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 策略版本 |
| result | string | 是 | MUST ∈ {ALLOW, BLOCK} | 结果枚举 |
| policy_id | string | 否 |  | 策略标识（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `CitationBinding.output_id` MUST 可解析到 `NarrativeOutput.output_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `CitationBinding.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `ContentSafetyAudit.output_id` MUST 可解析到 `NarrativeOutput.output_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
