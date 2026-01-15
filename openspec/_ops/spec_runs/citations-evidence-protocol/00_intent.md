# citations-evidence-protocol — Intent Alignment

## 目的（可验收语言复述）

`citations-evidence-protocol` 规格用于把 LS 的引用与证据链协议固化为可审计契约：定义引用格式、证据链字段、与 `corpus_release_id`/`version_id` 的追溯关系，并对缺失/伪造/不可解析引用形成确定性阻断，使用户可见结论具备可验证证据基础。

## 边界（不做什么）

- 本 spec 仅定义 MUST/SHALL 的契约、字段语义、门禁与验收口径。
- 本 spec 不规定具体实现细节、代码路径、技术选型或伪代码。

## 成功条件（可判定）

- 关键产物（引用格式、证据链、校验结果、阻断记录）具备字段级约束与完整性语义。
- 对外契约字段与拒绝原因以机器可读形式固定，并可通过命令验证。
- Gate-1 的验收口径可执行；失败具备明确阻断策略并可追溯到 `corpus_release_id`。

