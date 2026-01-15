# 启动性与回归基线 — 可观测与指标（规格层）

本文件定义 `bootability-and-regression-baseline` 的最小可观测性契约：metrics、logs、traces 与最小 SLO。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) Metrics（名称/标签/单位/聚合口径）

| 指标名 | 类型 | 单位 | 必选标签（最小） | 可选标签 | 聚合口径（最小） |
| --- | --- | --- | --- | --- | --- |
| `ls_bootability_checks_total` | counter | 1 | `result` | `check_id` | 启动检查计数 |
| `ls_bootability_check_duration_ms` | histogram | ms | `result` |  | 启动检查耗时 |
| `ls_regression_runs_total` | counter | 1 | `result` | `suite_id` | 回归运行计数 |
| `ls_regression_run_duration_ms` | histogram | ms | `result` | `suite_id` | 回归耗时 |
| `ls_gate_blocks_total` | counter | 1 | `gate` |  | 阻断计数 |

## 2) SLO（最小阈值）

- 启动检查可用性：启动检查成功率（不含客户端拒绝）SHALL ≥ 99.9%
- 回归可用性：回归执行成功率（不含测试失败本身）SHALL ≥ 99.9%
- Gate-1 阻断记录生成 MUST 可靠（失败视为阻断）

