# 融合引擎可解释性 — 数据字典与字段约束（规格层）

本文件定义 `fusion-engine-explainability` 的关键产物数据字典与字段级约束（规格层）。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 解释记录（ExplanationRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| explanation_id | string | 是 | MUST 唯一 | 解释记录标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识（可复现） |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识（可复现） |
| user_id | string | 否 |  | 用户标识（若适用；隔离边界） |
| decision_id | string | 是 | MUST 非空 | 融合决策标识 |
| narrative_output_id | string | 否 |  | 关联叙述输出（若适用） |
| playback_input_set_id | string | 是 | MUST 非空 | 关联回放输入集 |
| confidence_score | number | 否 | SHOULD ∈ [0,1] | 置信度（若适用） |
| uncertainty | object | 否 |  | 不确定性说明（结构化，若适用） |
| evidence_alignments | array&lt;object&gt; | 否 |  | 证据对齐引用集合（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 证据对齐引用（EvidenceAlignment）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| alignment_id | string | 是 | MUST 唯一 | 对齐标识 |
| explanation_id | string | 是 | MUST 非空 | 关联解释记录 |
| chain_id | string | 是 | MUST 非空 | 证据链标识（对齐 `citations-evidence-protocol`） |
| anchor_ids | array&lt;string&gt; | 否 |  | 引用锚点集合（若适用） |
| score | number | 否 | SHOULD ∈ [0,1] | 对齐评分（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 可复现回放输入集（PlaybackInputSet）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| playback_input_set_id | string | 是 | MUST 唯一 | 输入集标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| user_id | string | 否 |  | 用户标识（若适用） |
| input_items | array&lt;object&gt; | 是 | MUST 非空 | 输入项集合（结构化引用/快照，最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `EvidenceAlignment.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `EvidenceAlignment.explanation_id` MUST 可解析到 `ExplanationRecord.explanation_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `ExplanationRecord.playback_input_set_id` MUST 可解析到 `PlaybackInputSet.playback_input_set_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。

