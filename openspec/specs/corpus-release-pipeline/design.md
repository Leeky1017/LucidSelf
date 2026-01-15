# 语料发布流水线 Design

## 设计意图
本设计文档用于固定「语料发布流水线」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`corpus-governance`, `semantic-extraction-quality-gates`, `cross-book-consistency-conflicts`

## 必备标识符（最小集）
- `corpus_release_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- 每次发布阶段与校验报告 MUST 可追溯到同一 `corpus_release_id` 与 `version_id`；不可追溯 MUST 阻断（`VALIDATION_FAILED`）。
- release artifacts MUST 可追溯到 `corpus_release_id`，且在晋级前 MUST 完整可用；缺失 MUST 阻断（`ARTIFACT_MISSING`）。
- 回滚记录 MUST 可追溯到被回滚与回滚目标 `corpus_release_id`；不可追溯 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复发布阶段/重复校验/重复回滚导致发布状态漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 发布阶段记录：`stage_id`
  - 校验报告：`report_id`
  - release artifact：`artifact_id`
  - 回滚记录：`rollback_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入语料、相同 `corpus_release_id` 与相同规则版本（`version_id`）下重复执行流水线时：
  - 阶段判定（成功/失败）与校验结论（`overall_pass`）SHALL 在本 spec 定义的等价范围内一致。
  - release artifacts 的最小可审计摘要（例如类型/数量/校验和）SHALL 一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at/started_at/finished_at` 等时间戳
  - 系统生成的记录标识（若未由调用方提供）
- 除上述显式允许项外，差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测发布漂移（例如同一 `corpus_release_id` 在同版本规则下生成不同 artifacts/校验结论）。
- 偏差事件 MUST 至少包含：`corpus_release_id`、`version_id`、偏差类型与可行动摘要（例如受影响阶段/产物类型）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：校验失败、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于校验失败（`VALIDATION_FAILED`）或产物缺失（`ARTIFACT_MISSING`），系统 MUST 阻断晋级，并产出可行动整改线索（最小：失败阶段 + 关联标识符 + 证据路径）。
- 对于回滚失败（`ROLLBACK_FAILED`），系统 MUST 阻断并形成可审计事件。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：流水线阶段计数、失败原因分布、漂移事件计数、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `corpus_release_id`/`version_id`/阶段/任务标识（若适用）定位。
- audit：对关键拒绝/阻断/回滚必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：不影响对外引用的前提下并行执行流水线与校验，仅记录结果与审计，用于校准阈值与冲突处置。
- **Canary**：仅对小范围语料集或内部环境生效，监控失败率、漂移事件与审计可用性。
- **Gradual**：逐步扩大语料范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 校验失败或冲突处置失败 MUST 触发回滚或阻断。
- 漂移/偏差事件持续上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **低质语料被发布**：校验口径不足或被绕过  
   - 缓解：校验失败阻断（本文件）+ 质量门禁依赖（`semantic-extraction-quality-gates`）+ Gate-2 阻断策略（`acceptance.md`）

2) **回滚不可用导致对外持续污染**：发布后无法恢复  
   - 缓解：回滚记录契约（契约）+ 回滚触发条件（本文件）+ 审计可用性（`audit_log.md`）

3) **发布漂移导致不可复现**：同一 release 在同版本下产物不同  
   - 缓解：确定性边界与漂移检测（本文件）+ 产物摘要/校验和约束（`data_dictionary.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
