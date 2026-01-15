# llm-narrative-layer — Intent Alignment

## 目的（可验收语言复述）

`llm-narrative-layer` 规格用于把 LS 的「LLM 叙述层」能力固化为可审计契约：定义叙述输出 schema、模型/提示版本记录、引用绑定与内容安全审计的最小产物与标识符要求，并确保每次叙述输出可追溯到 `user_id`/`engine_id`/`version_id`/`prompt_id`/`model_version_id` 与证据链，从而为 Gate-2 的“可解释输出 + 安全合规 + 可复现”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（输出 schema、模型/提示版本记录、引用绑定、内容安全审计）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-2 的验收口径可执行；失败具备明确阻断策略并可追溯到 `prompt_id/model_version_id/version_id`。

