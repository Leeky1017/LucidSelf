# 版本化与偏差检测 — 可观测与指标（规格层）

本文件定义 `versioning-and-deviation-detection` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_version_manifest_entries_total` | counter | 1 | `status` | `engine_id` | 版本条目计数（注意基数） |
| `ls_compatibility_checks_total` | counter | 1 | `result` |  | 兼容性检查计数 |
| `ls_compatibility_check_duration_ms` | histogram | ms | `result` |  | 兼容性检查耗时 |
| `ls_deviation_reports_total` | counter | 1 | `deviation_type` |  | 偏差报告计数 |
| `ls_gate_blocks_total` | counter | 1 | `gate` |  | 阻断事件计数 |

**标签约束（最小）**
- metrics 标签 MUST 避免高基数；`version_id` SHOULD NOT 作为默认 metric 标签。

## 2) Logs/Traces（最小）

- 偏差检测与阻断决策 MUST 输出结构化日志，并包含 `version_id`/`engine_id`（若适用）。
- 关键路径 SHOULD 产生 trace/span，并包含 `version_id`（以及 `request_id/trace_id` 若适用）。

## 3) SLO（最小阈值）

- 偏差检测成功率（不含客户端拒绝）SHALL ≥ 99.9%
- 偏差检测延迟：p95 `ls_compatibility_check_duration_ms` SHALL ≤ 200ms（或按业务定义）
- Gate-0 阻断记录生成 MUST 可靠（失败视为阻断）

