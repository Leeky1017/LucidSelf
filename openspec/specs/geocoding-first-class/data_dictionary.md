# 地理编码一等公民 — 数据字典与字段约束（规格层）

本文件定义 `geocoding-first-class` 的关键产物数据字典与字段级约束（规格层）。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 标准化地理实体（NormalizedGeoEntity）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| geo_entity_id | string | 是 | MUST 唯一 | 地理实体标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| version_id | string | 是 | MUST 非空 | 版本标识（可复现） |
| normalized_name | string | 是 | MUST 非空 | 标准化名称 |
| latitude | number | 是 | MUST ∈ [-90, 90] | 纬度（WGS84） |
| longitude | number | 是 | MUST ∈ [-180, 180] | 经度（WGS84） |
| geocode_type | string | 是 | MUST ∈ {POINT, AREA} | 类型 |
| admin_level | string | 否 |  | 行政级别（若适用） |
| provider | string | 否 |  | 数据来源（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 精度/置信度元数据（PrecisionConfidenceMetadata）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| confidence_id | string | 是 | MUST 唯一 | 元数据标识 |
| geo_entity_id | string | 是 | MUST 非空 | 关联地理实体 |
| precision | string | 是 | MUST ∈ {ROOFTOP, STREET, CITY, REGION, COUNTRY, UNKNOWN} | 精度枚举 |
| confidence_score | number | 否 | SHOULD ∈ [0,1] | 置信度（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 回退记录（FallbackRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| fallback_id | string | 是 | MUST 唯一 | 回退记录标识 |
| user_id | string | 是 | MUST 非空 | 用户标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| geo_entity_id | string | 否 |  | 关联地理实体（若适用） |
| strategy | string | 是 | MUST ∈ {NONE, COARSE, BLOCK, UNKNOWN} | 回退策略 |
| reason_code | string | 否 |  | 回退原因（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 指标报表（MetricsReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报表标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| window_start | string | 是 | MUST 为 ISO-8601 | 统计窗口开始 |
| window_end | string | 是 | MUST 为 ISO-8601 | 统计窗口结束 |
| requests_total | number | 是 | MUST ≥ 0 | 请求总数 |
| success_rate | number | 否 | SHOULD ∈ [0,1] | 成功率（若适用） |
| fallback_rate | number | 否 | SHOULD ∈ [0,1] | 回退率（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `PrecisionConfidenceMetadata.geo_entity_id` MUST 可解析到 `NormalizedGeoEntity.geo_entity_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `FallbackRecord.geo_entity_id` 若出现 MUST 可解析到 `NormalizedGeoEntity.geo_entity_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。

