# 启动性与回归基线 — 数据字典与字段级约束（规格层）

本文件为 `bootability-and-regression-baseline` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 启动检查清单（StartupCheckItem）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| check_id | string | 是 | MUST 唯一 | 检查项标识 |
| name | string | 是 | MUST 非空 | 名称 |
| required | boolean | 是 | MUST 可判定 | 是否必须 |
| status | string | 是 | MUST 属于 {PASS, FAIL, SKIP} | 状态 |
| reason_code | string | 否 | 若提供 MUST 属于契约枚举 | 原因代码 |

## 2) 回归套件基线（RegressionSuiteBaseline）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| suite_id | string | 是 | MUST 唯一 | 套件标识 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| tests | array&lt;string&gt; | 是 | MUST 非空 | 测试项列表 |
| pass_threshold | string | 是 | MUST 非空（可判定表达） | 通过阈值 |

## 3) 失败阻断记录（BlockRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| block_id | string | 是 | MUST 唯一 | 阻断标识 |
| gate | string | 是 | MUST 非空 | 门禁 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| reason_code | string | 是 | MUST 属于契约枚举 | 原因代码 |
| summary | string | 是 | MUST 非空（可行动） | 摘要 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 版本关联报告（VersionLinkReport）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| report_id | string | 是 | MUST 唯一 | 报告标识 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| artifacts | array&lt;object&gt; | 是 | MUST 非空 | 关联产物 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

