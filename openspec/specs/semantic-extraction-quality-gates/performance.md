# 语义抽取质量门禁 — 性能目标与测量方式（规格层）

本文件定义 `semantic-extraction-quality-gates` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 门禁评估（evaluate）
- 质量指标口径/阈值配置加载（load config）
- 失败样本清单写入（failure samples）
- 复检记录写入（recheck）
- 审计导出（export）

## 2) 性能目标（最小）

### 门禁评估路径
- p95 延迟（端到端）SHALL ≤ 500ms（见 `ls_semantic_extraction_quality_gate_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 100 req/s（以 1 分钟窗口统计）

### 导出路径
- 审计导出任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_semantic_extraction_quality_gate_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在离线导出任务，MUST 记录任务开始/结束时间与结果，并可按 `version_id`/时间窗口定位。

