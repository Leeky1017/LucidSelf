# knowledge-graph-runtime-semanticquery — Intent Alignment

## 目的（可验收语言复述）

`knowledge-graph-runtime-semanticquery` 规格用于把 LS 的「知识图谱运行时语义查询」能力固化为可审计契约：定义查询契约、结果一致性声明、延迟 SLO 与审计日志的最小产物与标识符要求，并确保运行时查询可追溯到 `user_id`/`engine_id`/`version_id`，从而为 Gate-2 的“可解释输出前置保障（确定性 + 延迟）”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（查询契约、结果一致性声明、延迟 SLO、审计日志）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-2 的验收口径可执行；失败具备明确阻断策略并可追溯到 `user_id/engine_id/version_id`。

