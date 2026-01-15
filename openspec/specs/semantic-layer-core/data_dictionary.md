# 语义层核心 — 数据字典与字段级约束（规格层）

本文件为 `semantic-layer-core` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) semantic entry（SemanticEntry）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| semantic_entry_id | string | 是 | MUST 唯一 | 语义条目标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| semantic_key | string | 是 | MUST 非空 | 语义键（规范化后） |
| payload | object | 否 |  | 最小化语义载荷（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 索引条目（SemanticIndexEntry）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| index_entry_id | string | 是 | MUST 唯一 | 索引条目标识 |
| semantic_entry_id | string | 是 | MUST 非空 | 关联语义条目 |
| index_name | string | 是 | MUST 非空 | 索引名称（口径固定） |
| index_key | string | 是 | MUST 非空 | 索引键（规范化后） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) provenance 记录（ProvenanceRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| provenance_id | string | 是 | MUST 唯一 | 溯源标识 |
| semantic_entry_id | string | 是 | MUST 非空 | 关联语义条目 |
| chain_id | string | 否 |  | 关联证据链（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) citation_anchor 绑定（CitationAnchorBinding）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| binding_id | string | 是 | MUST 唯一 | 绑定标识 |
| semantic_entry_id | string | 是 | MUST 非空 | 关联语义条目 |
| anchor_id | string | 是 | MUST 非空 | 引用锚点标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 5) 查询响应（SemanticQueryResponse）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| response_id | string | 是 | MUST 唯一 | 响应标识 |
| query_id | string | 是 | MUST 非空 | 查询标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| results | array&lt;object&gt; | 是 | MUST 非空 | 结果集合（最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 完整性语义（最小）

- `CitationAnchorBinding.anchor_id` MUST 可解析到 `citations-evidence-protocol` 的 `CitationAnchor.anchor_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- 绑定的 `corpus_release_id` MUST 与语义条目/查询上下文一致或可判定兼容；不一致 MUST 阻断（`VALIDATION_FAILED`）。

