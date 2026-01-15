# semantic-layer-core — Intent Alignment

## 目的（可验收语言复述）

`semantic-layer-core` 规格用于把 LS 的「语义层核心」能力固化为可审计契约：定义语义条目（semantic entry）的数据模型、索引与查询响应的最小字段集合，并要求 provenance 与 citation_anchor 绑定可追溯到 `engine_id/user_id/version_id/corpus_release_id`，从而支撑 Gate-1 的“证据链可审计 + 语义契约稳定”与可执行验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（semantic entry、索引、provenance、citation_anchor 绑定、查询响应）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-1 的验收口径可执行；失败具备明确阻断策略并可追溯到 `version_id`（及 `corpus_release_id/engine_id/user_id`）。

