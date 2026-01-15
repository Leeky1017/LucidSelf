# fusion-engine-explainability — Intent Alignment

## 目的（可验收语言复述）

`fusion-engine-explainability` 规格用于把 LS 的「融合引擎可解释性」能力固化为可审计契约：定义融合决策解释输出、证据对齐引用、置信度/不确定性与可复现回放输入集的最小产物与标识符要求，并确保每次融合决策解释可追溯到 `engine_id`/`version_id`/`corpus_release_id` 与证据链，从而为 Gate-2 的“可解释决策 + 可复现回放 + 可审计证据”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（解释记录、证据对齐引用、置信度/不确定性、回放输入集）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-2 的验收口径可执行；失败具备明确阻断策略并可追溯到 `version_id/corpus_release_id/engine_id`。

