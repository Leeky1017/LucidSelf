# 安全/隐私/合规 — 可观测与指标（规格层）

本文件定义 `security-privacy-compliance` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_security_privacy_requests_total` | counter | 1 | `result` | `request_type`, `rejection_reason_code` | 隐私请求计数 |
| `ls_security_privacy_request_duration_ms` | histogram | ms | `result` | `request_type` | 隐私请求处理耗时 |
| `ls_security_unauthorized_total` | counter | 1 | `reason` | `resource_type` | 越权/未授权事件计数 |
| `ls_security_incidents_total` | counter | 1 | `severity` | `status` | 安全/隐私事件计数 |
| `ls_security_audit_records_total` | counter | 1 | `result` |  | 审计记录写入计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`user_id`/`org_id`/`version_id` SHOULD NOT 作为默认 metric 标签。
- 若需要按 `user_id/org_id` 精确定位，MUST 依赖 logs/traces/audit。

## 2) Logs/Traces（最小）

- 关键事件（隐私请求状态变化、越权拒绝、事件响应）MUST 输出结构化日志，并可关联 `request_id/trace_id`（若适用）。
- 关键路径 SHOULD 产生 trace/span，并包含 `version_id`（以及 `user_id/org_id` 若适用且不违反最小化原则）。

## 3) SLO（最小阈值）

- **隐私请求履约**：DELETE/EXPORT 等请求在可承诺窗口内完成率 SHALL ≥ 99%（窗口由业务定义但必须可审计）
- **越权拦截**：越权请求 MUST 100% 被拒绝并形成审计记录（作为阻断条件）
- **审计写入可用性**：关键审计记录写入成功率 SHALL ≥ 99.9%

