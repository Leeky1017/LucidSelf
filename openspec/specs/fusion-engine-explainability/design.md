# 融合引擎可解释性 Design

## 设计意图
本设计文档用于固定「融合引擎可解释性」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`llm-narrative-layer`, `citations-evidence-protocol`

## 必备标识符（最小集）
- `engine_id`, `version_id`, `corpus_release_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）

- `EvidenceAlignment.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- 解释记录中声明的对齐引用（若存在）MUST 与对应 `chain_id` 所含引用锚点一致或可判定兼容；不一致 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）

- 系统 MUST 定义确定性的去重键，以避免重复解释记录、重复对齐引用或重复回放输入集导致审计链路漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 解释记录：`explanation_id`
  - 证据对齐引用：`alignment_id`
  - 回放输入集：`playback_input_set_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）

- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）

- 在相同输入（含 `engine_id/version_id/corpus_release_id/playback_input_set_id`）下重复执行时：
  - 输出 MUST 始终满足契约 schema 约束（结构可判定）。
  - 解释结论（决策/解释结构）与证据对齐引用（`chain_id`/锚点集合）SHALL 在本 spec 定义的等价范围内一致。

### 等价范围（最小）

- 允许的非确定性字段/差异 MUST 被显式标注并可审计：
  - `created_at` 等时间戳
  - 对齐引用集合的无语义排序差异（若可判定为等价集合）
- 除上述显式允许项外，解释结论/证据对齐/回放输入集差异 MUST 视为偏差。

### 偏差检测与解释（MUST）

- 系统 MUST 能检测解释输出偏差（例如同一回放输入集在同版本下产生不同的证据对齐或违反 schema）。
- 偏差事件 MUST 至少包含：`engine_id`、`version_id`、`corpus_release_id`、`decision_id`（若适用）、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）

- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：证据不可解析、schema 不满足、回放输入集不一致（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）

- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于证据不可解析（`CITATION_NOT_RESOLVABLE`）或 schema 不满足（`OUTPUT_SCHEMA_INVALID`），系统 MUST 阻断并产出可行动整改线索（最小：失败原因 + 关联标识符 + 证据路径）。
- 对于回放输入集缺失/不一致，系统 MUST 阻断并记录可审计事件（`VALIDATION_FAILED`）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）

- metrics：解释请求计数、阻断原因分布、证据解析失败计数、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `engine_id/version_id/corpus_release_id/decision_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/偏差检测必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）

- **Shadow**：不影响对外行为的前提下并行生成解释记录与证据对齐校验，仅记录差异与审计，用于校准契约与对齐规则。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 或内部调用方生效，监控偏差事件、证据可解析性与延迟。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）

- 偏差事件（`DEVIATION_DETECTED`）异常上升 MUST 触发回滚或阻断。
- 证据不可解析失败率上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **无证据/错证据解释**：解释结论缺失可解析证据或对齐不一致  
   - 缓解：引用可解析性阻断（本文件/`data_dictionary.md`）+ 引用协议（`citations-evidence-protocol`）+ Gate-2 阻断策略（`acceptance.md`）

2) **不可复现回放**：相同回放输入集在同版本下产生不同解释或偏差不可解释  
   - 缓解：确定性边界与偏差检测（本文件）+ 回放输入集契约（`contract/*.json`）+ Gate-2 阻断策略（`acceptance.md`）

3) **隐私泄露**：日志/审计包含敏感原文或可推断用户内容  
   - 缓解：最小化/脱敏（`security.md`/`audit_log.md`）+ 标签约束（`observability.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
