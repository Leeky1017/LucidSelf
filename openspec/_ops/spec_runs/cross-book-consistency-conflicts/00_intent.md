# cross-book-consistency-conflicts — Intent Alignment

## 目的（可验收语言复述）

`cross-book-consistency-conflicts` 规格用于把 LS 的「跨书一致性与冲突」资产能力固化为可审计契约：定义跨书/跨源冲突的发现、归因、决策与例外批准的最小产物与标识符要求，并确保冲突记录与处置链路可追溯到 `corpus_release_id` 与 `version_id`，满足资产门禁对“许可/血缘/QA/冲突处置可追溯”的可执行验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（冲突记录、来源引用、决策与例外批准记录、冲突报表）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- 资产门禁验收口径可执行；失败具备明确阻断策略并可追溯到 `corpus_release_id`/`version_id`。

