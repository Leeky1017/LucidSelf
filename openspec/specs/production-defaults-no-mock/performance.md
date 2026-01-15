# 生产默认值（禁止Mock）— 性能目标与测量方式（规格层）

本文件定义 `production-defaults-no-mock` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 启动前配置校验（阻断路径）
- 运行时关键配置变更校验（若适用）
- 违规检测与审计写入

## 2) 性能目标（最小）

- 启动前配置校验：p95 `ls_prod_defaults_config_check_duration_ms` SHALL ≤ 100ms
- 违规检测：检测到违规后 SHOULD 在 1 分钟内形成可审计事件（用于阻断与回滚）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_prod_defaults_config_check_duration_ms`），并至少输出 p50/p95/p99。
- 违规检测与审计写入 MUST 记录事件时间与可见时间，确保可复盘。

