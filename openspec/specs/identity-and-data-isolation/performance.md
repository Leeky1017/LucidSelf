# 身份与数据隔离 — 性能目标与测量方式（规格层）

本文件定义 `identity-and-data-isolation` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 鉴权决策与隔离校验（读/写请求前置）
- 隔离违规检测与审计写入
- 删除/保留审计记录与导出

## 2) 性能目标（最小）

### 鉴权决策
- p95 延迟（端到端）SHALL ≤ 50ms（见 `ls_identity_isolation_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 500 req/s（以 1 分钟窗口统计）

### 审计写入
- 审计写入路径 MUST 不得成为主要瓶颈；若不可用，MUST 触发阻断或降级并可审计（见 `design.md`）。

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_identity_isolation_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在离线导出任务，MUST 记录任务开始/结束时间与结果，并可按 `org_id`/时间窗口定位（在不违反最小化原则下）。

