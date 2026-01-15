# 部署与发布 — 数据字典与字段级约束（规格层）

本文件为 `deployment-release` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 发布产物清单（ReleaseArtifactManifest）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| manifest_id | string | 是 | MUST 唯一 | 清单标识 |
| version_id | string | 是 | MUST 非空 | 发布版本标识 |
| engine_id | string | 否 |  | 引擎标识（若适用） |
| corpus_release_id | string | 否 |  | 语料发布版本标识（若适用） |
| artifacts | array&lt;object&gt; | 是 | MUST 非空 | 产物集合（最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 环境晋级记录（PromotionRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| promotion_id | string | 是 | MUST 唯一 | 晋级标识 |
| version_id | string | 是 | MUST 非空 | 晋级版本标识 |
| from_env | string | 是 | MUST ∈ {dev, staging, prod} | 来源环境（规格层固定） |
| to_env | string | 是 | MUST ∈ {dev, staging, prod} | 目标环境（规格层固定） |
| result | string | 是 | MUST ∈ {PASS, BLOCK} | 结果枚举（规格层固定） |
| rejection_reason_code | string | 否 | MUST ∈ 契约枚举（若出现） | 拒绝/阻断原因 |
| actor_type | string | 否 | MUST ∈ {system, user, service}（若出现） | 操作者类型 |
| actor_id | string | 否 | MUST 脱敏/最小化（若出现） | 操作者标识 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 发布验证报告（ReleaseVerificationReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报告标识 |
| version_id | string | 是 | MUST 非空 | 被验证版本 |
| environment_id | string | 是 | MUST 非空 | 验证环境标识 |
| overall_pass | boolean | 是 | MUST 可判定 | 是否通过 |
| checks | array&lt;object&gt; | 否 |  | 检查项集合（最小化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 回滚记录（RollbackRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rollback_id | string | 是 | MUST 唯一 | 回滚标识 |
| target_version_id | string | 是 | MUST 非空 | 被回滚版本 |
| rollback_to_version_id | string | 是 | MUST 非空 | 回滚目标版本 |
| environment_id | string | 是 | MUST 非空 | 回滚环境标识 |
| reason | string | 否 |  | 原因摘要（禁止敏感原文） |
| result | string | 是 | MUST ∈ {PASS, BLOCK} | 结果枚举（规格层固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `PromotionRecord.rejection_reason_code` 若出现 MUST 属于契约 `rejection_reasons.code` 枚举；否则 MUST 阻断（`VALIDATION_FAILED`）。
- 发布验证失败（`overall_pass=false`）与晋级阻断（`result="BLOCK"`）必须可追溯到同一 `version_id` 与环境上下文；不可追溯 MUST 视为无效并阻断（`VALIDATION_FAILED`）。
