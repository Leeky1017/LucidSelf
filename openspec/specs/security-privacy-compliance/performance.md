# 安全/隐私/合规 — 性能目标与测量方式（规格层）

本文件定义 `security-privacy-compliance` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- 越权/违规拦截（在线路径）
- 隐私请求处理（DELETE/EXPORT 等，可能为异步作业）
- 审计导出与事件响应记录

## 2) 性能目标（最小）

- 越权拦截：拒绝决策 SHOULD 在 50ms 内完成（端到端 p95）。
- 隐私请求履约：处理延迟 MUST 可测量并可审计；SLO 由 `observability.md` 固定口径。

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（如 `ls_security_privacy_request_duration_ms`），并至少输出 p50/p95/p99。
- 异步履约任务 MUST 记录开始/结束时间与结果，并可按 `request_id`/时间窗口定位。

