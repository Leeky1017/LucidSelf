# 可观测性与SLO — 指标规范与SLO（规格层）

本文件为 `observability-slos` 定义全局最小可观测契约：指标命名/标签规范、核心指标清单与 SLO 阈值。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 指标命名规范（MUST）

- 指标名 MUST 满足：`^[a-z][a-z0-9_]*$`
- 指标名 SHOULD 使用 `ls_` 前缀（LucidSelf），并以语义结尾表达单位（如 `_ms`, `_bytes`, `_total`）。
- 标签名 MUST 满足：`^[a-z][a-z0-9_]*$`

## 2) 标签与基数约束（MUST/SHOULD）

- metrics 标签 MUST 避免高基数；以下标识符 SHOULD NOT 作为默认 metric 标签：
  - `user_id`, `org_id`, `version_id`, `request_id`, `trace_id`（以及任何自由文本）
- 若需要按上述标识符定位，MUST 依赖 logs/traces/audit。
- 若确需高基数标签，必须显式豁免并可审计（否则视为 `HIGH_CARDINALITY_LABEL`）。

## 3) 核心指标清单（最小）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_requests_total` | counter | 1 | `result` | `endpoint`, `method` | 按请求计数（含拒绝/阻断） |
| `ls_request_duration_ms` | histogram | ms | `result` | `endpoint`, `method` | 端到端耗时分布（p50/p95/p99） |
| `ls_errors_total` | counter | 1 | `error_type` | `endpoint` | 服务端错误计数 |
| `ls_blocks_total` | counter | 1 | `block_type` | `capability` | 阻断事件计数（门禁/依赖不可用等） |
| `ls_audit_records_total` | counter | 1 | `result` | `capability` | 审计记录写入计数 |
| `ls_slo_breaches_total` | counter | 1 | `slo_id` | `severity` | SLO 违约计数 |

## 4) SLO 阈值（Gate-0 最小基线）

- **API 可用性**：月度成功率 SHALL ≥ 99.9%（不含客户端拒绝）
- **API 延迟**：p95 `ls_request_duration_ms` SHALL ≤ 200ms
- **Trace 覆盖率**：可追踪请求占比（具备 `trace_id`）SHALL ≥ 99%
- **结构化日志覆盖率**：关键请求日志具备必填字段占比 SHALL ≥ 99%

