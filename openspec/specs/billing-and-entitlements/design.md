# 计费与权益 Design

## 设计意图
本设计文档用于固定「计费与权益」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `citations-evidence-protocol`, `versioning-and-deviation-detection`

## 必备标识符（最小集）
- `user_id`, `org_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- 权益校验时，`EntitlementDefinition.entitlement_id` MUST 可解析；不可解析 MUST 拒绝（`ENTITLEMENT_NOT_FOUND`）。
- `DisputeEvidenceChain.billing_record_id` MUST 可解析到 `BillingRecord.billing_record_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- `DisputeEvidenceChain.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复计费、重复入账或重复争议记录；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 权益定义：`entitlement_id`
  - 用量事件：`usage_event_id`（或 `idempotency_key`，若由调用方提供并被声明为去重键）
  - 计费记录：`billing_record_id`
  - 争议证据链：`dispute_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`USAGE_EVENT_DUPLICATE` 或 `BILLING_RECORD_CONFLICT` 或 `VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id/org_id/version_id`）、相同计费规则版本与相同用量事件集合下重复计算时：
  - `BillingRecord.amount` 与 `status` SHALL 在本 spec 定义的等价范围内一致。
  - 用量事件去重后的计量结果（例如计数/汇总）SHALL 一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at/occurred_at` 等时间戳
  - 系统生成的记录标识（若未由调用方提供）
- 除上述显式允许项外，金额/计量结果差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测计费漂移（例如同一计费周期在同版本规则下生成不同 `amount`）。
- 偏差事件 MUST 至少包含：`user_id`、`org_id`、`version_id`、偏差类型与可行动摘要（例如受影响周期/金额差异）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、权益不存在、越权等（通常不可重试）。
- **阻断（BLOCK）**：计费规则/用量数据不一致、无法保证审计/争议证据链完整（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符、证据路径）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：权益校验/用量入账/账单生成计数、拒绝原因分布、计费漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `user_id/org_id/version_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/账单生成必须生成审计记录（见 `audit_log.md`）。
- evidence：争议证据链（`DisputeEvidenceChain.chain_id`）必须可解析并可导出。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外收费行为的前提下并行生成账单，比较差异并校准规则。
- **Canary**：仅对小流量/白名单 `org_id` 或内部调用方生效，监控计费漂移/争议率与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 计费漂移事件持续上升 MUST 触发回滚或阻断。
- 争议率异常上升（例如 `ls_billing_disputes_total` 激增）MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-3 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **重复计费/重复扣费**：用量事件重复入账或去重失效导致多收  
   - 缓解：幂等/去重语义（本文件）+ 冲突拒绝原因（契约）+ 审计记录（`audit_log.md`）

2) **漏计/少计导致收入流失**：用量事件丢失或计量口径不一致  
   - 缓解：字段级约束与完整性校验（`data_dictionary.md`）+ 计费漂移检测（本文件）+ 指标与告警（`observability.md`）

3) **越权/隔离失效**：跨 `user_id/org_id` 读取/写入计费与争议数据  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

4) **争议不可审计**：缺失证据链或证据不可解析导致无法追责  
   - 缓解：证据链可解析性阻断（本文件/`data_dictionary.md`）+ Gate-3 阻断策略（`acceptance.md`）

5) **高基数可观测导致成本失控**：将 `user_id/billing_record_id` 作为默认 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
