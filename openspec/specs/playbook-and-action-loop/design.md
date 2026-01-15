# Playbook与行动闭环 Design

## 设计意图
本设计文档用于固定「Playbook与行动闭环」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`identity-and-data-isolation`, `security-privacy-compliance`, `observability-slos`, `versioning-and-deviation-detection`

## 必备标识符（最小集）
- `user_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `ExecutionRecord.playbook_id` MUST 可解析到 `PlaybookDefinition.playbook_id`；不可解析 MUST 阻断（`PLAYBOOK_NOT_FOUND`）。
- `ApprovalRecord.execution_id` MUST 可解析到 `ExecutionRecord.execution_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `RollbackRecord.execution_id` MUST 可解析到 `ExecutionRecord.execution_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复执行/重复审批/重复回滚导致的闭环漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - playbook 定义：`playbook_id`
  - 执行记录：`execution_id`
  - 审批记录：`approval_id`
  - 回滚记录：`rollback_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id/version_id`）与相同 playbook 定义下重复执行时：
  - 执行状态迁移（`ExecutionRecord.status`）SHALL 在本 spec 定义的等价范围内一致。
  - 审批/回滚决策（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at/started_at/finished_at` 等时间戳
  - 系统生成的 `execution_id`（若未由调用方提供）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测闭环漂移（例如同一输入在同版本下得到不同审批/回滚结果）。
- 偏差事件 MUST 至少包含：`user_id`、`version_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：审批未通过、回滚不可用、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于需要审批的行动，未获批准 MUST 阻断执行（`APPROVAL_REQUIRED`/`APPROVAL_DENIED`）并产出可行动整改线索。
- 对于回滚失败（`ROLLBACK_FAILED`），系统 MUST 阻断晋级并形成可审计事件。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：执行/审批/回滚计数、拒绝原因分布、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `user_id/version_id/execution_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/审批/回滚必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：仅记录执行计划与审批链路，不影响真实动作执行，用于校准权限与审计口径。
- **Canary**：仅对小流量/白名单 `user_id` 或内部调用方生效，监控失败率与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 执行失败率异常上升 MUST 触发回滚或阻断。
- 审批链路不可用或审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **未授权执行导致越权操作**：权限校验或审批链缺失  
   - 缓解：访问控制与审批记录（契约/`security.md`/`audit_log.md`）+ Gate-2 阻断策略（`acceptance.md`）

2) **回滚不可用导致无法闭环**：失败后无法恢复到安全状态  
   - 缓解：回滚记录契约（契约）+ 回滚触发条件（本文件）+ 审计可用性（`audit_log.md`）

3) **审计缺失导致不可追责**：关键步骤未形成审计链路  
   - 缓解：审计字段契约（`audit_log.md`）+ Gate-2 阻断策略（`acceptance.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
