# 生产默认值（禁止Mock）— 数据字典与字段级约束（规格层）

本文件为 `production-defaults-no-mock` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) 配置校验规则（ConfigValidationRule）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| rule_id | string | 是 | MUST 唯一 | 规则标识 |
| environment | string | 是 | MUST 非空（受控词表） | 环境 |
| config_key | string | 是 | MUST 非空 | 配置键 |
| condition | string | 是 | MUST 非空（可判定表达） | 条件 |
| action | string | 是 | MUST 属于 {ALLOW, DENY, BLOCK} | 动作 |
| reason_code | string | 是 | MUST 属于契约枚举 rejection_reasons[*].code | 原因代码 |

## 2) 环境隔离约束（EnvironmentIsolationConstraint）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| constraint_id | string | 是 | MUST 唯一 | 约束标识 |
| environment | string | 是 | MUST 非空（受控词表） | 环境 |
| policy | string | 是 | MUST 非空（可判定摘要） | 策略 |

## 3) 启动失败原因记录（StartupFailureRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| failure_id | string | 是 | MUST 唯一 | 失败标识 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| environment | string | 否 | 若提供 MUST 非空 | 环境 |
| reason_code | string | 是 | MUST 属于契约枚举 | 原因代码 |
| summary | string | 是 | MUST 非空；不得含敏感原文 | 最小摘要 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

## 4) 违规审计（MockViolationAudit）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| audit_id | string | 是 | MUST 唯一 | 审计标识 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| environment | string | 否 | 若提供 MUST 非空 | 环境 |
| violation_type | string | 是 | MUST 非空（受控词表） | 违规类型 |
| result | string | 是 | MUST 属于 {DENY, BLOCK} | 结果 |
| created_at | string | 是 | MUST 为 ISO-8601 | 时间戳 |

