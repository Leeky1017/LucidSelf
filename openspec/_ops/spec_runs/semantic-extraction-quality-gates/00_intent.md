# semantic-extraction-quality-gates — Intent Alignment

## 目的（可验收语言复述）

`semantic-extraction-quality-gates` 规格用于把 LS 的「语义抽取质量门禁」能力固化为可审计契约：定义质量指标口径、阈值配置、失败样本清单与复检记录的最小产物与标识符要求，并确保门禁结果可追溯到 `version_id` 与 `corpus_release_id`，从而为 Gate-1 的“质量门禁阈值明确 + 回归基线可执行”提供可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（质量指标口径、阈值配置、失败样本清单、复检记录）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-1 的验收口径可执行；失败具备明确阻断策略并可追溯到 `version_id`/`corpus_release_id`。

