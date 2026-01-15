# 语料发布流水线 — 性能目标与测量方式（规格层）

本文件定义 `corpus-release-pipeline` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 阶段运行（ingest/normalize/extract/qa/release）
- 校验报告生成（validation）
- 回滚执行（rollback）
- 审计导出（export）

## 2) 性能目标（最小）

### 关键阶段
- p95 阶段耗时 SHALL ≤ 30 分钟（以 `ls_corpus_release_pipeline_stage_duration_ms` 且按 `stage_name` 区分口径判定）

### 导出路径
- 审计导出任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的阶段耗时指标（`ls_corpus_release_pipeline_stage_duration_ms`），并至少输出 p50/p95/p99。
- 若存在异步阶段任务，MUST 记录任务开始/结束时间与结果，并可按 `corpus_release_id`/`version_id`/阶段/时间窗口定位。

