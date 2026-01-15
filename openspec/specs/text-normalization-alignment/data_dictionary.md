# 文本归一化与对齐 — 数据字典与字段级约束（规格层）

本文件为 `text-normalization-alignment` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 归一化规则集（NormalizationRuleSet）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rule_set_id | string | 是 | MUST 唯一 | 规则集标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| name | string | 是 | MUST 非空 | 名称 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 对齐映射（AlignmentMapping）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| mapping_id | string | 是 | MUST 唯一 | 映射标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| source_asset_id | string | 否 |  | 源资产标识（若适用） |
| target_asset_id | string | 否 |  | 目标资产标识（若适用） |
| mapping_count | number | 否 | MUST ≥ 0 | 映射条目数量（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 变换审计记录（TransformationAuditRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| audit_id | string | 是 | MUST 唯一 | 审计标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| rule_set_id | string | 否 |  | 关联规则集（若适用） |
| mapping_id | string | 否 |  | 关联映射（若适用） |
| result | string | 是 | MUST 为枚举（ALLOW/DENY/BLOCK） | 决策结果 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 覆盖率报告（CoverageReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| coverage_report_id | string | 是 | MUST 唯一 | 报告标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| coverage_ratio | number | 是 | MUST 在 0..1 | 覆盖率（0..1） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 5) 例外清单（ExceptionList）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| exception_list_id | string | 是 | MUST 唯一 | 清单标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| exception_count | number | 否 | MUST ≥ 0 | 例外条目数量（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 完整性语义（最小）

- `AlignmentMapping.source_asset_id/target_asset_id` 若存在，MUST 可解析到 `corpus-governance` 的资产登记；不可解析 MUST 阻断并返回确定性拒绝原因（`INVALID_MAPPING` 或 `VALIDATION_FAILED`）。
- `corpus_release_id` 与 `version_id` MUST 与资产发布视图一致或可判定兼容；不一致 MUST 阻断。

