# 知识图谱运行时语义查询 — 数据字典与字段级约束（规格层）

本文件为 `knowledge-graph-runtime-semanticquery` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 查询请求（SemanticQueryRequest）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| query_id | string | 是 | MUST 唯一 | 查询标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| query_key | string | 是 | MUST 非空 | 查询键（规范化后；禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 查询响应（SemanticQueryResponse）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| response_id | string | 是 | MUST 唯一 | 响应标识 |
| query_id | string | 是 | MUST 非空 | 关联查询 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| results | array&lt;object&gt; | 是 | MUST 非空 | 结果集合（最小化） |
| latency_ms | number | 否 | MUST ≥ 0（若出现） | 端到端延迟（ms） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 结果一致性声明（ConsistencyDeclaration）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| declaration_id | string | 是 | MUST 唯一 | 声明标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 适用版本 |
| equivalence_scope | string | 是 | MUST 非空 | 等价范围摘要（口径固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 延迟 SLO（LatencySLO）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| slo_id | string | 是 | MUST 唯一 | SLO 标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 适用版本 |
| p95_ms | number | 是 | MUST ≥ 0 | p95 阈值 |
| p99_ms | number | 否 | MUST ≥ 0（若出现） | p99 阈值 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `SemanticQueryResponse.query_id` MUST 可解析到 `SemanticQueryRequest.query_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `ConsistencyDeclaration.version_id` MUST 与查询/响应的 `version_id` 一致或可判定兼容；不一致 MUST 阻断（`VALIDATION_FAILED`）。
