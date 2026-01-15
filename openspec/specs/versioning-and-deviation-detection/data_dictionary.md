# 版本化与偏差检测 — 数据字典与字段级约束（规格层）

本文件为 `versioning-and-deviation-detection` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 版本清单（VersionManifest）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| version_id | string | 是 | MUST 非空；SHOULD 满足 `^ver_[a-z0-9]{12,}$` | 版本标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |
| status | string | 是 | MUST 非空（受控词表） | 状态 |
| notes | string | 否 | 若提供 MUST 可审计 | 摘要 |

**完整性语义（最小）**
- `version_id` MUST 唯一；冲突 MUST 失败并阻断。

## 2) 兼容性声明（CompatibilityStatement）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| from_version_id | string | 是 | MUST 非空 | 来源版本 |
| to_version_id | string | 是 | MUST 非空 | 目标版本 |
| compatible | boolean | 是 | MUST 可判定 | 是否兼容 |
| scope | string | 否 | 若提供 MUST 为受控词表 | 范围 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

**完整性语义（最小）**
- `from_version_id` 与 `to_version_id` MUST 可解析到 VersionManifest.version_id；不可解析 MUST 失败并阻断。

## 3) 偏差报告（DeviationReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报告标识 |
| version_id | string | 是 | MUST 可解析到 VersionManifest.version_id | 被评估版本 |
| baseline_version_id | string | 是 | MUST 可解析到 VersionManifest.version_id | 基线版本 |
| deviation_type | string | 是 | MUST 非空（受控词表） | 偏差类型 |
| summary | string | 是 | MUST 非空（可行动） | 摘要 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

## 4) 阻断记录（BlockRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| block_id | string | 是 | MUST 唯一 | 阻断标识 |
| gate | string | 是 | MUST 非空（Gate-0/1/2/3/资产门禁） | 门禁 |
| version_id | string | 是 | MUST 可解析到 VersionManifest.version_id | 关联版本 |
| reason | string | 是 | MUST 非空（可行动） | 原因摘要 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

