# Golden Set与回归评测 — 性能目标与测量方式（规格层）

本文件定义 `golden-sets-and-regression` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 覆盖率计算（report）
- 回归运行与阈值判定（run/threshold）
- 漂移检测与告警（drift）
- 审计导出（export）

## 2) 性能目标（最小）

### 阈值判定（控制面）
- p95 延迟（端到端）SHALL ≤ 500ms（见 `ls_golden_sets_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 50 req/s（以 1 分钟窗口统计）

### 回归运行（作业面）
- 回归运行任务 MUST 在 30 分钟内完成（以任务级 duration 指标/日志判定；阈值可按实际负载修订）

### 漂移检测
- 漂移检测与告警生成 SHOULD 在 10 分钟内完成（以任务级口径判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_golden_sets_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在离线作业（回归/漂移检测/导出），MUST 记录任务开始/结束时间与结果，并可按 `golden_set_id`/`version_id`/时间窗口定位。

