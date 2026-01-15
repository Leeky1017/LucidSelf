# 七引擎流水线E2E — 性能目标与测量方式（规格层）

本文件定义 `seven-engine-pipeline-e2e` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 端到端执行（run）
- 阶段交接校验（handoff validate）
- 失败恢复（recovery）
- 审计写入与导出（audit write/export）

## 2) 性能目标（最小）

### E2E 执行
- p95 延迟（端到端）SHALL ≤ 10,000ms（见 `observability.md` 的 `ls_e2e_pipeline_run_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 10 runs/min（以 1 分钟窗口统计）

### 交接校验
- 单次交接校验新增耗时 p95 SHOULD ≤ 200ms（以分段 span 或阶段性日志口径判定）

### 审计写入
- 关键事件审计写入新增耗时 p95 SHOULD ≤ 50ms（以审计写入日志/指标判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_e2e_pipeline_run_duration_ms`），并至少输出 p50/p95/p99。
- 若存在分段耗时度量，MUST 可关联到同一 `run_id/trace_id`，并可按 `engine_id/version_id/corpus_release_id` 聚合。

