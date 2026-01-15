# 可观测性与SLO — 数据字典与字段级约束（规格层）

本文件为 `observability-slos` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 指标定义（MetricDefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| metric_name | string | 是 | MUST 符合命名规范：`^[a-z][a-z0-9_]*$` | 指标名 |
| metric_type | string | 是 | MUST 属于 {counter, gauge, histogram, summary} | 类型 |
| unit | string | 是 | MUST 非空 | 单位 |
| required_labels | array&lt;string&gt; | 是 | 元素 MUST 符合 `^[a-z][a-z0-9_]*$`；MUST 非空 | 必选标签 |
| optional_labels | array&lt;string&gt; | 否 | 元素 MUST 符合 `^[a-z][a-z0-9_]*$` | 可选标签 |
| aggregation | string | 是 | MUST 非空 | 聚合口径 |
| description | string | 是 | MUST 非空 | 语义说明 |

**完整性语义（最小）**
- 指标名 MUST 全局唯一（在同一观测域内）；冲突 MUST 失败并阻断（`INVALID_METRIC_NAME` 或 `VALIDATION_FAILED`）。
- 标签集合 MUST 遵循低基数原则：`user_id`/`org_id`/`version_id`/`trace_id` SHOULD NOT 作为默认 metric 标签；违反 MUST 失败或要求显式豁免（`HIGH_CARDINALITY_LABEL`）。

## 2) 结构化日志字段规范（LogFieldSchema）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| schema_id | string | 是 | MUST 非空 | schema 标识 |
| schema_version | string | 是 | MUST 非空 | schema 版本 |
| fields | array&lt;object&gt; | 是 | MUST 非空 | 字段定义列表 |

字段定义对象（fields[*]）最小字段：
- `name`（string, MUST）：字段名（`^[a-z][a-z0-9_]*$`）
- `type`（string, MUST）：string/number/boolean/object/array
- `required`（boolean, MUST）
- `redaction`（string, SHOULD）：none/mask/hash/drop（脱敏策略）

## 3) trace 传播规范（TracePropagationSpec）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| request_id | string | 是 | MUST 非空 | 请求标识 |
| trace_id | string | 是 | MUST 非空 | 链路标识 |
| parent_span_id | string | 否 | 若提供 MUST 非空 | 父 span |
| span_id | string | 否 | 若提供 MUST 非空 | 当前 span |

**完整性语义（最小）**
- `request_id` 与 `trace_id` MUST 可关联到 logs/traces；缺失 MUST 被拒绝或被显式标注为不可追溯（口径必须确定性）。

## 4) SLO 定义（SLODefinition）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| slo_id | string | 是 | MUST 非空 | SLO 标识 |
| service | string | 是 | MUST 非空 | 服务/能力名称 |
| indicator | string | 是 | MUST 非空 | 指标口径 |
| threshold | string | 是 | MUST 非空 | 阈值表达 |
| window | string | 是 | MUST 非空 | 评估窗口 |
| target | string | 是 | MUST 非空 | 目标 |

**完整性语义（最小）**
- `slo_id` MUST 唯一；冲突 MUST 失败并阻断（`INVALID_SLO_DEFINITION`）。

## 5) 告警规则（AlertRule）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rule_id | string | 是 | MUST 非空且唯一 | 规则标识 |
| severity | string | 是 | MUST 非空 | 严重级别 |
| slo_id | string | 否 | 若提供 MUST 可解析到 SLODefinition.slo_id | 关联 SLO |
| summary | string | 是 | MUST 非空 | 可行动摘要 |

**完整性语义（最小）**
- `slo_id` 引用若不可解析 MUST 失败并阻断（引用可解析性）。

