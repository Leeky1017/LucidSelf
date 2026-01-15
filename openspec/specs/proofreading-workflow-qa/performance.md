# 校对工作流与QA — 性能目标与测量方式（规格层）

本文件定义 `proofreading-workflow-qa` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 缺陷登记与更新（defect ingest/update）
- 批准写入（approval write）
- QA 指标聚合与报表生成（metrics report）
- 审计导出（audit export）

## 2) 性能目标（最小）

### 报表生成
- QA 指标报表生成任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

### 审计导出
- 审计导出任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 若存在离线任务（报表/导出），MUST 记录任务开始/结束时间与结果，并可按 `corpus_release_id/version_id`/时间窗口定位。

