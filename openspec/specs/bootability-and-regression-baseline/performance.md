# 启动性与回归基线 — 性能目标与测量方式（规格层）

本文件定义 `bootability-and-regression-baseline` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 性能目标（最小）

- 启动检查：p95 `ls_bootability_check_duration_ms` SHALL ≤ 30s（按实际基线可收敛）
- 回归套件：回归运行结果 SHOULD 在 30 分钟内可见（用于门禁与回归定位；按套件规模可调但必须可审计）

## 2) 测量口径（最小）

- 启动检查与回归运行 MUST 记录开始/结束时间与结果，并可按 `version_id` 定位。
- 性能测量 MUST 输出 p50/p95/p99（若适用）。

