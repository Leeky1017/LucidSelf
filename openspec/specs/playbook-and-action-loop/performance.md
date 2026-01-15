# Playbook与行动闭环 — 性能目标与测量方式（规格层）

本文件定义 `playbook-and-action-loop` 的性能目标与最小测量口径。禁止写实现细节；仅定义 MUST/SHALL 与可判定口径。

## 1) 关键路径（最小集合）

- playbook 创建/更新（define）
- 执行启动/结束（execute）
- 审批决策（approve）
- 回滚执行（rollback）
- 审计导出（export）

## 2) 性能目标（最小）

### 控制面（创建/启动/审批/回滚触发）
- p95 延迟（端到端）SHALL ≤ 500ms（见 `ls_playbook_action_request_duration_ms`）

### 导出路径
- 审计导出任务 MUST 在 5 分钟内完成（以任务级 duration 指标/日志判定）

## 3) 测量口径（最小）

- 性能测量 MUST 使用统一口径的耗时指标（`ls_playbook_action_request_duration_ms`），并至少输出 p50/p95/p99。
- 若存在异步执行/回滚任务，MUST 记录任务开始/结束时间与结果，并可按 `user_id`/`version_id`/时间窗口定位。

