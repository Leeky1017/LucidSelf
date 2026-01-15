# 地理编码一等公民 — 性能目标与测量方式（规格层）

本文件定义 `geocoding-first-class` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 地理编码请求处理（geocode）
- 精度/置信度评估（precision/confidence）
- 回退策略评估与记录（fallback）
- 审计写入与导出（audit write/export）

## 2) 性能目标（最小）

### 地理编码请求
- p95 延迟（端到端）SHALL ≤ 200ms（见 `observability.md` 的 `ls_geocoding_request_duration_ms`）
- 峰值吞吐（短时）SHALL ≥ 500 req/s（以 1 分钟窗口统计）

### 审计写入
- 关键事件审计写入新增耗时 p95 SHOULD ≤ 50ms（以审计写入日志/指标判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_geocoding_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在分段耗时度量，MUST 可关联到同一 `request_id/trace_id`，并可按 `version_id` 聚合。

