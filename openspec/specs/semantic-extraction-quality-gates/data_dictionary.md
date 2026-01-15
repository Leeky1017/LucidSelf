# 语义抽取质量门禁 — 数据字典与字段级约束（规格层）

本文件为 `semantic-extraction-quality-gates` 的关键产物提供字段级约束表与最小可判定语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 质量指标口径（QualityMetricDefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| metric_id | string | 是 | MUST 唯一 | 指标定义标识 |
| metric_name | string | 是 | MUST 非空 | 指标名称（口径固定） |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本（若适用，仍需可追溯） |
| engine_id | string | 否 |  | 适用引擎（若适用） |
| unit | string | 是 | MUST 非空 | 单位（ratio/count/ms 等） |
| aggregation | string | 是 | MUST 非空 | 聚合口径（mean/p95 等） |
| direction | string | 是 | MUST ∈ {higher_is_better, lower_is_better} | 指标方向 |
| description | string | 否 |  | 摘要（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 阈值配置（QualityThresholdConfig）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| threshold_id | string | 是 | MUST 唯一 | 阈值配置标识 |
| metric_name | string | 是 | MUST 非空 | 关联指标名称（口径固定） |
| version_id | string | 是 | MUST 非空 | 阈值配置版本 |
| engine_id | string | 否 |  | 适用引擎（若适用） |
| comparator | string | 是 | MUST ∈ {>=, >, <=, <} | 比较符（规格层固定） |
| threshold_value | number | 是 | MUST 可判定比较 | 阈值数值 |
| slo_window | string | 否 |  | 评估窗口（5m/1h/1d 等，若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) 门禁运行结果（QualityGateRunResult）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| gate_run_id | string | 是 | MUST 唯一 | 门禁运行标识 |
| user_id | string | 是 | MUST 非空 | 用户标识（隔离边界） |
| org_id | string | 是 | MUST 非空 | 组织/租户标识（隔离边界） |
| engine_id | string | 是 | MUST 非空 | 引擎标识（若适用） |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布版本 |
| overall_pass | boolean | 是 | MUST 可判定 | 是否通过门禁 |
| result | string | 是 | MUST ∈ {PASS, BLOCK, DEGRADED} | 结果枚举（规格层固定） |
| rejection_reason_code | string | 否 | MUST ∈ 契约枚举（若出现） | 拒绝/阻断原因 |
| failures | array&lt;object&gt; | 否 |  | 失败明细（最小化；禁止敏感原文） |
| started_at | string | 是 | MUST 为 ISO-8601 | 开始时间 |
| finished_at | string | 否 | MUST 为 ISO-8601（若出现） | 结束时间 |

## 4) 失败样本清单项（FailureSample）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| sample_id | string | 是 | MUST 唯一 | 样本标识 |
| gate_run_id | string | 是 | MUST 非空 | 关联门禁运行 |
| metric_name | string | 是 | MUST 非空 | 关联指标（口径固定） |
| severity | string | 是 | MUST ∈ {low, medium, high} | 严重度（规格层固定） |
| reference_id | string | 否 |  | 可解析引用标识（若适用，禁止敏感原文） |
| chain_id | string | 否 |  | 关联证据链（若适用；对齐 citations-evidence-protocol 的 EvidenceChain.chain_id） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 5) 复检记录（RecheckRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| recheck_id | string | 是 | MUST 唯一 | 复检记录标识 |
| original_gate_run_id | string | 是 | MUST 非空 | 原门禁运行标识 |
| recheck_gate_run_id | string | 否 |  | 复检门禁运行标识（若适用） |
| actor_type | string | 是 | MUST ∈ {system, user, service} | 操作者类型（规格层固定） |
| actor_id | string | 否 | MUST 脱敏/最小化（若出现） | 操作者标识 |
| decision | string | 是 | MUST ∈ {PASS, BLOCK} | 复检结论（规格层固定） |
| notes | string | 否 |  | 备注（禁止敏感原文） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `QualityThresholdConfig.metric_name` MUST 可解析到 `QualityMetricDefinition.metric_name`；不可解析 MUST 阻断（`METRIC_DEFINITION_INVALID`）。
- `QualityGateRunResult.rejection_reason_code` 若出现 MUST 属于契约 `rejection_reasons.code` 枚举；否则 MUST 视为无效并阻断（`VALIDATION_FAILED`）。
- `FailureSample.reference_id` 若出现 MUST 可解析到引用协议（例如 `citations-evidence-protocol` 的 `anchor_id`）或可判定为合法引用；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `FailureSample.chain_id` 若出现 MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE` 或 `VALIDATION_FAILED`）。
