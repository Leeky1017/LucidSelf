# 跨书一致性与冲突 — 性能目标与测量方式（规格层）

本文件定义 `cross-book-consistency-conflicts` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 冲突检测（detect）
- 决策/例外写入（decision/approve）
- 冲突报表生成（report）
- 审计导出（export）

## 2) 性能目标（最小）

### 控制面（检测/决策触发）
- p95 延迟（端到端）SHALL ≤ 500ms（见 `ls_cross_book_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 50 req/s（以 1 分钟窗口统计）

### 作业面（批量检测/报表）
- 批处理任务 SHOULD 在 30 分钟内完成（以任务级 duration 指标/日志判定；阈值可按实际负载修订）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_cross_book_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在离线作业（批处理/导出），MUST 记录任务开始/结束时间与结果，并可按 `corpus_release_id`/时间窗口定位。

