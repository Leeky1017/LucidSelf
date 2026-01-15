# 引用与证据协议 — 数据字典与字段级约束（规格层）

本文件为 `citations-evidence-protocol` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) citation_anchor（CitationAnchor）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| anchor_id | string | 是 | MUST 唯一 | 锚点标识 |
| asset_id | string | 是 | MUST 非空 | 资产标识 |
| corpus_release_id | string | 是 | MUST 非空 | 发布版本 |
| l1_anchor | string | 是 | MUST 非空 | 内容锚点 |

## 2) evidence_chain（EvidenceChain）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| chain_id | string | 是 | MUST 唯一 | 证据链标识 |
| user_id | string | 是 | MUST 非空 | 用户标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 发布版本 |
| citation_anchors | array&lt;object&gt; | 是 | MUST 非空 | 引用锚点列表 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

**完整性语义（最小）**
- `citation_anchors[*]` 中的 `asset_id/corpus_release_id/l1_anchor` MUST 可解析到语料治理范围（与 `corpus_release_id` 一致）；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。

## 3) provenance 记录（ProvenanceRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| provenance_id | string | 是 | MUST 唯一 | 溯源标识 |
| chain_id | string | 是 | MUST 非空 | 证据链引用 |
| engine_id | string | 否 |  | 引擎标识（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 审计导出包（AuditExportBundle）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| bundle_id | string | 是 | MUST 唯一 | 导出标识 |
| chain_id | string | 是 | MUST 非空 | 证据链引用 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

