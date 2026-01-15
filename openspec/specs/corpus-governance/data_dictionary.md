# 语料治理 — 数据字典与字段级约束（规格层）

本文件为 `corpus-governance` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 资产登记（AssetRegistration）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| asset_id | string | 是 | MUST 唯一；MUST 非空 | 资产标识 |
| corpus_release_id | string | 是 | MUST 非空 | 发布版本标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| name | string | 是 | MUST 非空 | 资产名称 |
| source | string | 是 | MUST 非空 | 来源摘要（可追溯） |
| license_id | string | 是 | MUST 非空 | 许可标识 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

## 2) 许可与使用约束（LicenseConstraint）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| license_id | string | 是 | MUST 唯一；MUST 非空 | 许可标识 |
| allowed_use | array&lt;string&gt; | 是 | MUST 非空 | 允许用途 |
| restrictions | array&lt;string&gt; | 否 |  | 限制条款 |
| attribution_required | boolean | 是 | MUST 可判定 | 是否要求署名 |

**完整性语义（最小）**
- 使用/发布资产前 MUST 校验许可约束；违反 MUST 阻断并形成审计记录（`LICENSE_VIOLATION`）。

## 3) 版本与血缘（LineageRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| asset_id | string | 是 | MUST 非空 | 资产标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 发布版本标识 |
| derived_from | array&lt;string&gt; | 否 | 元素 MUST 非空 | 上游资产列表 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

**完整性语义（最小）**
- `derived_from[*]` 若存在 MUST 可解析到已登记的 `asset_id`；不可解析 MUST 失败并阻断（`LINEAGE_NOT_RESOLVABLE`）。

## 4) 退役记录（RetirementRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| retirement_id | string | 是 | MUST 唯一 | 退役标识 |
| asset_id | string | 是 | MUST 非空 | 被退役资产 |
| effective_version_id | string | 是 | MUST 非空 | 生效版本 |
| reason | string | 是 | MUST 非空（可审计摘要） | 原因 |
| created_at | string | 是 | MUST 为 ISO-8601 | 创建时间 |

