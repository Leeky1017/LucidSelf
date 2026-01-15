# 跨书一致性与冲突 Design

## 设计意图
本设计文档用于固定「跨书一致性与冲突」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`corpus-governance`

## 必备标识符（最小集）
- `corpus_release_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `SourceCitation.asset_id` MUST 可解析到 `corpus-governance` 的资产登记；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `SourceCitation.anchor_id` 若存在，MUST 可解析到 `citations-evidence-protocol` 的锚点集合；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `ConflictDecision.conflict_id` / `ExceptionApproval.conflict_id` MUST 可解析到 `ConflictRecord.conflict_id`；不可解析 MUST 阻断（`CONFLICT_NOT_FOUND`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复冲突记录与重复批准造成审计噪音与状态漂移；去重键仅允许由契约字段构成。
- 约定的最小去重键（规格级语义）：
  - 冲突记录：`conflict_id` + `version_id`
  - 来源引用：`citation_id`
  - 决策记录：`decision_id`
  - 例外批准：`approval_id`
  - 冲突报表：`report_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`INVALID_CONFLICT_RECORD` 或 `VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `corpus_release_id/version_id`）与相同一致性判定规则视图下重复执行冲突检测时：
  - 冲突发现结果在本 spec 定义的等价范围内 SHALL 一致。
  - 决策与例外批准的拒绝原因代码（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at` 等时间戳
  - 系统生成的 `report_id`（若未由调用方提供）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测冲突发现漂移（例如同一输入在同版本语义下产生不同冲突集合）。
- 偏差事件 MUST 至少包含：`corpus_release_id`、`version_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：输入缺失/非法、引用不可解析、冲突记录非法等（通常不可重试）。
- **阻断（BLOCK）**：门禁检查失败、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符）。

### 信号产物（最小）
- metrics：冲突计数、例外批准计数、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `corpus_release_id`/`version_id`/`request_id`（若适用）定位。
- audit：对关键拒绝/阻断必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外行为的前提下并行运行冲突检测与报表生成，验证冲突率、例外清单与审计可用性。
- **Canary**：仅对小范围资产/内部调用方生效，监控冲突/漂移趋势与审计导出能力。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 冲突发现结果显著漂移（例如冲突计数异常激增）MUST 触发回滚或阻断发布。
- 例外批准链路不可用或审计记录不可用/不可导出 MUST 视为资产门禁阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **一致性判定口径漂移**：规则变化导致冲突集合不可比  
   - 缓解：确定性边界与偏差检测（本文件）+ 报表口径固定（`data_dictionary.md`）+ 审计记录（`audit_log.md`）

2) **引用不可解析导致误判**：来源引用无法解析到资产/锚点  
   - 缓解：引用可解析性阻断（本文件/`data_dictionary.md`）+ 资产门禁阻断策略（`acceptance.md`）

3) **许可/约束未执行导致合规风险**：未经授权的资产被用于对外输出  
   - 缓解：上游许可治理依赖（`corpus-governance`）+ 审计导出可追责（`audit_log.md`）+ 合规留存（`compliance.md`）

4) **高基数可观测导致成本失控**：将 asset_id/anchor_id 作为 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

5) **审计缺失导致不可追责**：冲突决策/例外批准未形成审计链路  
   - 缓解：审计字段契约（`audit_log.md`）+ 资产门禁阻断策略（`acceptance.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
