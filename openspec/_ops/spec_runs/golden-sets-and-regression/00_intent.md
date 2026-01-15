# golden-sets-and-regression — Intent Alignment

## 目的（可验收语言复述）

`golden-sets-and-regression` 规格用于把 LS 的「Golden Set 与回归评测」能力固化为可审计契约：定义 golden set 的版本化、覆盖率报告、回归阈值与结果、以及漂移告警的最小产物与标识符要求，并确保评测与门禁结果可追溯到 `version_id`（以及 `corpus_release_id`/`engine_id` 如适用），使 Gate-1 的“语义可靠性”有可执行、可阻断、可复现的验收口径。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（golden set 清单、覆盖率报告、回归阈值与结果、漂移告警）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-1 的验收口径可执行；失败具备明确阻断策略并可追溯到 `version_id`（及 `corpus_release_id`/`engine_id` 如适用）。

