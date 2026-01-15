# 版本化与偏差检测 — 性能目标与测量方式（规格层）

本文件定义 `versioning-and-deviation-detection` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 版本解析与兼容性判定
- 偏差检测与报告生成
- 阻断记录生成与导出

## 2) 性能目标（最小）

- 兼容性判定：p95 `ls_compatibility_check_duration_ms` SHALL ≤ 200ms（或按业务定义）
- 偏差检测：偏差检测结果 SHOULD 在 5 分钟内可见（用于门禁阻断与回归定位）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（如 `ls_compatibility_check_duration_ms`），并至少输出 p50/p95/p99。
- 偏差报告生成 MUST 记录开始/结束时间与结果，并可按 `version_id` 定位。

