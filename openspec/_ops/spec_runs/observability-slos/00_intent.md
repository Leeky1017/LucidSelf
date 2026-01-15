# observability-slos — Intent Alignment

## 目的（可验收语言复述）

`observability-slos` 规格用于把 LS 的指标（metrics）、结构化日志（logs）、链路追踪（traces）与 SLO/告警规则固化为**可执行、可审计、可复现**的契约，使故障定位、门禁阻断与商业化运行基线具备统一口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的观测字段、命名/标签规范、SLO/告警口径与验收方式。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（指标规范、日志字段规范、trace 传播规范、SLO/告警规则）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- 观测数据可按 `request_id`/`trace_id`/`version_id`/`engine_id`/`user_id` 关联定位（在避免高基数指标标签的前提下）。
- Gate-0 相关验收口径可执行；失败具备明确阻断策略。

