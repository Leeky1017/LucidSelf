# versioning-and-deviation-detection — Intent Alignment

## 目的（可验收语言复述）

`versioning-and-deviation-detection` 规格用于把 LS 的版本体系与偏差检测固化为可审计契约：明确 `version_id`/`engine_id` 的追溯关系、版本清单与兼容性声明的字段语义，并定义偏差报告与阻断记录，使“相同输入+相同版本”下的输出漂移可检测、可解释、可阻断。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（版本清单、偏差报告、兼容性声明、阻断记录）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- 可观测/审计字段明确，且可按 `version_id`/`engine_id`（及 `request_id/trace_id` 如适用）关联定位。
- Gate-0 相关验收口径可执行；失败具备明确阻断策略。

