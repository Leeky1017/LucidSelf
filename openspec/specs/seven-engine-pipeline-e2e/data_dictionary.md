# 七引擎流水线E2E — 数据字典与字段约束（规格层）

本文件定义 `seven-engine-pipeline-e2e` 的关键产物数据字典与字段级约束（规格层）。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 阶段契约（StageContract）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| stage_id | string | 是 | MUST 唯一 | 阶段标识 |
| stage_name | string | 是 | MUST 非空 | 阶段名称（口径固定） |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识（可复现） |
| input_schema_version | string | 是 | MUST 非空 | 输入 schema 版本 |
| output_schema_version | string | 是 | MUST 非空 | 输出 schema 版本 |
| required_inputs | array&lt;object&gt; | 是 | MUST 非空 | 必需输入字段集合（结构化） |
| required_outputs | array&lt;object&gt; | 是 | MUST 非空 | 必需输出字段集合（结构化） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 2) 交接校验记录（HandoffValidationRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| handoff_id | string | 是 | MUST 唯一 | 交接记录标识 |
| run_id | string | 是 | MUST 非空 | E2E 执行标识 |
| from_stage_id | string | 是 | MUST 非空 | 上游阶段标识 |
| to_stage_id | string | 是 | MUST 非空 | 下游阶段标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| user_id | string | 否 |  | 用户标识（若适用） |
| result | string | 是 | MUST ∈ {PASS, BLOCK, ERROR} | 校验结果 |
| rejection_reason_code | string | 否 |  | 拒绝/阻断原因代码（见契约枚举） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 3) E2E Trace 关联（E2ETraceLink）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| trace_id | string | 是 | MUST 非空 | Trace 标识 |
| run_id | string | 是 | MUST 非空 | E2E 执行标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| stage_spans | array&lt;object&gt; | 否 |  | 阶段 span 元数据（若适用） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 失败恢复记录（FailureRecoveryRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| recovery_id | string | 是 | MUST 唯一 | 恢复记录标识 |
| run_id | string | 是 | MUST 非空 | E2E 执行标识 |
| engine_id | string | 是 | MUST 非空 | 引擎标识 |
| version_id | string | 是 | MUST 非空 | 版本标识 |
| corpus_release_id | string | 是 | MUST 非空 | 语料发布标识 |
| failed_stage_id | string | 是 | MUST 非空 | 失败阶段标识 |
| action | string | 是 | MUST 非空 | 恢复动作（口径固定） |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 字段级约束（跨实体，最小）

- `HandoffValidationRecord.from_stage_id/to_stage_id` MUST 可解析到 `StageContract.stage_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `HandoffValidationRecord.run_id` MUST 可与 `E2ETraceLink.run_id` 形成可追溯关联；缺失/无法关联 MUST 记录可审计事件。

