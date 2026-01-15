# 引擎ID治理 — 数据字典与字段级约束（规格层）

本文件为 `engine-id-governance` 的关键产物提供字段级约束表与最小完整性语义。禁止写实现细节；仅定义 MUST/SHALL 与可判定约束。

## 1) engine_id 注册表（EngineRegistryRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| engine_id | string | 是 | MUST 满足 `^[a-zA-Z_][a-zA-Z0-9_]*$`；MUST 全局唯一 | 引擎稳定标识 |
| version_id | string | 是 | MUST 非空；SHOULD 满足 `^ver_[a-z0-9]{12,}$` | 用于可复现/可审计的版本标识 |
| engine_version | string | 否 | SHOULD 满足语义版本 `^\\d+\\.\\d+\\.\\d+$` | 引擎自身版本（若适用） |
| kind | string | 否 | 若提供 MUST 属于 {calculator, semantic, rule, fusion} | 引擎类型（若适用） |
| status | string | 否 | 若提供 MUST 属于 {active, experimental, deprecated} | 生命周期状态（若适用） |
| depends_on | array&lt;string&gt; | 否 | 元素 MUST 满足 `engine_id` 约束 | 依赖引擎列表（若适用） |
| owner_team | string | 否 | SHOULD 非空 | 责任归属（若适用） |
| created_at | string | 否 | 若提供 MUST 为 ISO-8601 | 创建时间（若适用） |
| updated_at | string | 否 | 若提供 MUST 为 ISO-8601 | 更新时间（若适用） |

**完整性语义（最小）**
- `engine_id` MUST 唯一；重复注册 MUST 失败并产生可审计的拒绝原因。
- `depends_on[*]` MUST 可解析为已注册的 `engine_id`（不可解析 MUST 失败并阻断）。

## 2) 生命周期变更记录（EngineLifecycleEvent）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| event_id | string | 是 | MUST 满足 `^evt_[a-z0-9]{12}$`；MUST 唯一 | 事件标识 |
| engine_id | string | 是 | MUST 满足 `engine_id` 约束 | 关联引擎 |
| version_id | string | 是 | MUST 非空 | 事件版本 |
| event_type | string | 是 | MUST 属于 {REGISTER, UPDATE, STATUS_CHANGE, DEPRECATE, REPLACE, UNREGISTER} | 事件类型 |
| occurred_at | string | 是 | MUST 为 ISO-8601 | 发生时间 |
| actor_type | string | 否 | 若提供 MUST 属于 {system, user, service} | 操作者类型 |
| actor_id | string | 否 | 若提供 MUST 非空；MUST 遵循最小化/脱敏 | 操作者标识 |
| request_id | string | 否 | 若提供 MUST 非空 | 请求关联 |
| trace_id | string | 否 | 若提供 MUST 非空 | 追踪关联 |
| metadata | object | 否 | MUST 不包含不必要敏感原文 | 最小补充信息 |

**完整性语义（最小）**
- `engine_id` MUST 可解析（对 `REGISTER` 以外事件）；不可解析 MUST 失败并阻断。
- `event_type=REPLACE` 时 MUST 存在可解析的替代关系（见第 3 节）。

## 3) 弃用/替代关系（EngineDeprecationMapping）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| deprecated_engine_id | string | 是 | MUST 满足 `engine_id` 约束；MUST 可解析 | 被弃用引擎 |
| replacement_engine_id | string | 否 | 若提供 MUST 满足 `engine_id` 约束且 MUST 可解析 | 替代引擎 |
| effective_version_id | string | 是 | MUST 非空 | 生效版本 |
| reason | string | 否 | 若提供 MUST 可审计且不含敏感原文 | 摘要原因 |

**完整性语义（最小）**
- `deprecated_engine_id` MUST 可解析；不可解析 MUST 失败并阻断。
- `replacement_engine_id` 若提供 MUST 可解析；不可解析 MUST 失败并阻断。

## 4) 审计记录（AuditRecord）

| 字段 | 类型 | 必填 | 约束（最小） | 说明 |
| --- | --- | --- | --- | --- |
| audit_id | string | 是 | MUST 唯一；SHOULD 具备可追溯格式（实现可选） | 审计标识 |
| event_id | string | 是 | MUST 可解析到 EngineLifecycleEvent.event_id | 关联事件 |
| engine_id | string | 是 | MUST 满足 `engine_id` 约束 | 关联引擎 |
| version_id | string | 是 | MUST 非空 | 关联版本 |
| result | string | 是 | MUST 属于 {ALLOW, DENY, BLOCK} | 审计结果 |
| rejection_reason_code | string | 否 | 若提供 MUST 属于契约枚举 rejection_reasons[*].code | 拒绝原因 |
| created_at | string | 是 | MUST 为 ISO-8601 | 记录时间 |

**完整性语义（最小）**
- `event_id` MUST 可解析；不可解析 MUST 失败并阻断导出/晋级。
- `rejection_reason_code` 若提供 MUST 属于本能力契约枚举；否则 MUST 失败并阻断。

