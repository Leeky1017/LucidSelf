# 计费与权益 — 性能目标与测量方式（规格层）

本文件定义 `billing-and-entitlements` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 权益校验（entitlement check）
- 用量事件入账（usage ingest）
- 计费记录生成/更新（billing record）
- 争议开启/处理（dispute）
- 审计导出（export）

## 2) 性能目标（最小）

### 权益校验
- p95 延迟（端到端）SHALL ≤ 50ms（见 `ls_billing_entitlements_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 500 req/s（以 1 分钟窗口统计）

### 用量事件入账
- p95 延迟（端到端）SHALL ≤ 200ms
- 峰值吞吐（短时）SHALL ≥ 1,000 events/s

### 导出路径
- 审计导出任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_billing_entitlements_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在离线导出任务，MUST 记录任务开始/结束时间与结果，并可按 `version_id`/时间窗口定位。

