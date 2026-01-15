# corpus-release-pipeline — Intent Alignment

## 目的（可验收语言复述）

`corpus-release-pipeline` 规格用于把 LS 的「语料发布流水线」能力固化为可审计契约：定义语料发布的阶段记录、校验报告、release artifacts 与回滚记录的最小产物与标识符要求，并确保每次语料晋级/回滚可追溯到 `corpus_release_id` 与 `version_id`，从而为 Gate-2 的“可发布晋级 + 可回滚 + 可审计”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（发布阶段记录、校验报告、release artifacts、回滚记录）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-2 的验收口径可执行；失败具备明确阻断策略并可追溯到 `corpus_release_id/version_id`。

