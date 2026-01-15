# 部署与发布 — 性能目标与测量方式（规格层）

本文件定义 `deployment-release` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 环境晋级（promotion）
- 发布验证（verification）
- 回滚触发与执行（rollback）
- 审计导出（export）

## 2) 性能目标（最小）

### 控制面（晋级/回滚触发）
- p95 延迟（端到端）SHALL ≤ 1,000ms（见 `ls_deployment_release_request_duration_ms`）

### 发布验证
- 发布验证任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

### 回滚执行
- 回滚执行任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_deployment_release_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在异步验证/回滚任务，MUST 记录任务开始/结束时间与结果，并可按 `version_id`/环境/时间窗口定位。

