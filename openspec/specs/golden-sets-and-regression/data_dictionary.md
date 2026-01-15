# Golden Set与回归评测 — 数据字典与字段级约束（规格层）

本文件为 `golden-sets-and-regression` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) golden set 清单（GoldenSetDefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| golden_set_id | string | 是 | MUST 唯一 | golden set 标识 |
| version_id | string | 是 | MUST 非空 | 评测定义版本 |
| corpus_release_id | string | 是 | MUST 非空 | 关联语料发布版本 |
| engine_id | string | 是 | MUST 非空 | 关联引擎（若适用） |
| name | string | 是 | MUST 非空 | 名称 |
| description | string | 否 |  | 描述摘要（禁止敏感原文） |
| sample_count | number | 否 | MUST ≥ 0 | 样本量（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 覆盖率报告（CoverageReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| coverage_report_id | string | 是 | MUST 唯一 | 报告标识 |
| golden_set_id | string | 是 | MUST 非空 | 引用 golden set |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| corpus_release_id | string | 是 | MUST 非空 | 关联语料发布版本 |
| engine_id | string | 是 | MUST 非空 | 关联引擎（若适用） |
| coverage_ratio | number | 是 | MUST 在 0..1 | 覆盖率（0..1） |
| metrics | object | 否 |  | 最小指标明细（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 回归阈值（RegressionThreshold）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| threshold_id | string | 是 | MUST 唯一 | 阈值标识 |
| golden_set_id | string | 是 | MUST 非空 | 引用 golden set |
| version_id | string | 是 | MUST 非空 | 阈值定义版本 |
| engine_id | string | 是 | MUST 非空 | 适用引擎（若适用） |
| metric_name | string | 是 | MUST 非空 | 指标名（口径固定） |
| comparator | string | 是 | MUST 为枚举（>=/>/<=/<） | 比较符 |
| threshold_value | number | 是 | MUST 为数值 | 阈值数值 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 回归结果（RegressionRunResult）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| run_id | string | 是 | MUST 唯一 | 运行标识 |
| golden_set_id | string | 是 | MUST 非空 | 引用 golden set |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| corpus_release_id | string | 是 | MUST 非空 | 关联语料发布版本 |
| engine_id | string | 是 | MUST 非空 | 关联引擎（若适用） |
| overall_pass | boolean | 是 | MUST 非空 | 是否通过阈值门禁 |
| started_at | string | 是 | MUST 为 ISO-8601 | 开始时间 |
| finished_at | string | 否 | MUST 为 ISO-8601（若存在） | 结束时间 |
| failures | array&lt;object&gt; | 否 |  | 失败明细（最小化） |

## 5) 漂移告警（DriftAlert）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| alert_id | string | 是 | MUST 唯一 | 告警标识 |
| golden_set_id | string | 是 | MUST 非空 | 引用 golden set |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| corpus_release_id | string | 是 | MUST 非空 | 关联语料发布版本 |
| engine_id | string | 是 | MUST 非空 | 关联引擎（若适用） |
| drift_type | string | 是 | MUST 非空 | 漂移类型（枚举在规格层固定） |
| severity | string | 是 | MUST 非空 | 严重级别（枚举在规格层固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 完整性语义（最小）

- `CoverageReport.golden_set_id` / `RegressionThreshold.golden_set_id` / `RegressionRunResult.golden_set_id` / `DriftAlert.golden_set_id` MUST 可解析到 `GoldenSetDefinition.golden_set_id`；不可解析 MUST 阻断并返回确定性拒绝原因（`INVALID_GOLDEN_SET_ID` 或 `VALIDATION_FAILED`）。
- `corpus_release_id` 与 `version_id` 在同一次评测/回归运行中 MUST 一致或可判定兼容；不一致 MUST 阻断。

