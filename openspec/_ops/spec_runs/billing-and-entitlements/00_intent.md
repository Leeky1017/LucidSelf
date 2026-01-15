# billing-and-entitlements — Intent Alignment

## 目的（可验收语言复述）

`billing-and-entitlements` 规格用于把 LS 的「计费与权益」能力固化为可审计契约：定义权益定义、用量事件、计费记录与争议证据链的最小产物与标识符要求，并确保计费/权益判定可追溯到 `user_id`/`org_id`/`version_id`（以及 `corpus_release_id`/`engine_id` 若适用），从而为 Gate-3 的“商业化计费可执行 + 争议可审计”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（权益定义、用量事件、计费记录、争议证据链）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-3 的验收口径可执行；失败具备明确阻断策略并可追溯到 `user_id/org_id/version_id`。

