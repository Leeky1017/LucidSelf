# seven-engine-pipeline-e2e — Intent Alignment

## 目的（可验收语言复述）

`seven-engine-pipeline-e2e` 规格用于把 LS 的「七引擎端到端流水线」固化为可审计、可回归的阶段契约：定义各阶段交接（handoff）与校验记录、E2E trace 关联、失败恢复记录的最小产物与标识符要求，并确保一次 E2E 执行可追溯到 `engine_id`/`version_id`/`corpus_release_id` 与证据链（如适用），从而为 Gate-2 的“端到端可观测 + 阶段交接可校验 + 失败可定位”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（阶段契约、handoff 校验记录、E2E trace、失败恢复记录）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-2 的验收口径可执行；失败具备明确阻断策略并可追溯到 `engine_id/version_id/corpus_release_id`。

