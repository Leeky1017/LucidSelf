# 语料发布流水线 — 数据字典与字段级约束（规格层）

本文件为 `corpus-release-pipeline` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 发布阶段记录（ReleaseStageRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| stage_id | string | 是 | MUST 唯一 | 阶段记录标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| version_id | string | 是 | MUST 非空 | 流水线/规则版本 |
| stage_name | string | 是 | MUST ∈ {ingest, normalize, extract, qa, release} | 阶段枚举（规格层固定） |
| status | string | 是 | MUST ∈ {pending, running, succeeded, failed, rolled_back} | 状态枚举 |
| started_at | string | 是 | MUST 为 ISO-8601 | 开始时间 |
| finished_at | string | 否 | MUST 为 ISO-8601（若出现） | 结束时间 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 校验报告（ValidationReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报告标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| version_id | string | 是 | MUST 非空 | 校验口径版本 |
| stage_name | string | 是 | MUST ∈ {ingest, normalize, extract, qa, release} | 关联阶段 |
| overall_pass | boolean | 是 | MUST 可判定 | 是否通过 |
| checks | array&lt;object&gt; | 否 |  | 检查项集合（最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) release artifacts（ReleaseArtifact）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| artifact_id | string | 是 | MUST 唯一 | 产物标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| version_id | string | 是 | MUST 非空 | 生成口径版本 |
| artifact_type | string | 是 | MUST 非空 | bundle/index/metadata 等 |
| uri | string | 否 |  | 产物定位符（若适用） |
| checksum | string | 否 |  | 校验和/摘要（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 回滚记录（RollbackRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rollback_id | string | 是 | MUST 唯一 | 回滚标识 |
| corpus_release_id | string | 是 | MUST 非空 | 被回滚语料发布版本 |
| rollback_to_release_id | string | 是 | MUST 非空 | 回滚目标语料发布版本 |
| version_id | string | 是 | MUST 非空 | 回滚口径版本 |
| reason | string | 否 |  | 原因摘要（禁止敏感原文） |
| result | string | 是 | MUST ∈ {PASS, BLOCK} | 结果枚举 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `ValidationReport.stage_name` MUST 与其对应的 `ReleaseStageRecord.stage_name` 一致或可判定关联；不一致 MUST 阻断（`VALIDATION_FAILED`）。
- `ReleaseArtifact.corpus_release_id` MUST 与 `ReleaseStageRecord.corpus_release_id` 一致；不一致 MUST 阻断（`VALIDATION_FAILED`）。
