# 滥用防护与限流 Design

## 设计意图
本设计文档用于固定「滥用防护与限流」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `security-privacy-compliance`, `observability-slos`, `citations-evidence-protocol`

## 必备标识符（最小集）
- `user_id`, `org_id`, `engine_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- 强制执行决策 MUST 可追溯到使用的 `RateLimitPolicy.policy_id` 与 `version_id`；缺失 MUST 阻断（`POLICY_MISSING` 或 `VALIDATION_FAILED`）。
- `AbuseSignalEvidence.chain_id`（若适用）MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `ReviewRecord.action_id` MUST 可解析到 `EnforcementActionRecord.action_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复封禁/重复挑战/重复降级导致的执行漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 限流策略：`policy_id`
  - 滥用信号证据：`evidence_id`
  - 强制动作记录：`action_id`
  - 复核记录：`review_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id/org_id/engine_id/version_id`）与相同策略版本下重复判定时：
  - 强制执行结果（ALLOW/DENY/BLOCK）SHALL 在本 spec 定义的等价范围内一致。
  - 拒绝/阻断原因代码（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性因素（若存在）MUST 被显式标注并可审计，例如：
  - 时间窗口边界导致的计数差异（`window` 对齐点）
  - `created_at/expires_at` 等时间戳
- 除上述显式允许项外，结果差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测强制执行漂移（例如同一输入在同版本策略下产生不同结果）。
- 偏差事件 MUST 至少包含：`engine_id`、`version_id`、偏差类型与可行动摘要（例如受影响策略/阈值）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：策略缺失/无法保证审计、关键依赖不可用导致无法保证一致性（通常需要人工整改或回滚）。
- **降级（DEGRADED）**：在不降低安全底线的前提下的受控退化（必须可审计；不得掩盖滥用风险）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于限流/滥用命中（`RATE_LIMIT_EXCEEDED`/`ABUSE_DETECTED`），系统 MUST 记录强制动作记录，并可追溯到策略与证据（若适用）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符、证据路径）。

### 信号产物（最小）
- metrics：请求计数、拒绝原因分布、限流命中/封禁计数、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `user_id/org_id/engine_id/version_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/强制动作必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：仅记录滥用检测与限流判定，不影响对外行为，用于校准误报与阈值。
- **Canary**：仅对小流量/白名单 `org_id` 或内部调用方生效，监控误报率、延迟与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 误报/封禁率异常上升 MUST 触发回滚或阻断。
- 延迟/错误率超过 `observability-slos` 的阈值 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **误报导致正常用户被封禁**：阈值过严或信号不稳  
   - 缓解：Shadow 校准 + Canary 监控（本文件）+ 复核记录（契约/`audit_log.md`）

2) **绕过导致滥用未被阻断**：策略缺失或错误时 fail-open  
   - 缓解：策略缺失阻断（本文件）+ Gate-2 阻断策略（`acceptance.md`）+ 可审计拒绝原因（契约）

3) **隐私泄露**：滥用证据包含敏感原文或高基数标识  
   - 缓解：最小化/脱敏规则（`audit_log.md`/`security.md`）+ 标签约束（`observability.md`）

4) **高基数 metrics 导致成本失控**：将 `user_id/ip` 作为默认标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
