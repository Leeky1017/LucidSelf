# 部署与发布 Design

## 设计意图
本设计文档用于固定「部署与发布」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`production-defaults-no-mock`, `bootability-and-regression-baseline`, `observability-slos`

## 必备标识符（最小集）
- `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- 晋级与验证必须可追溯到 `ReleaseArtifactManifest`；缺失 MUST 阻断（`RELEASE_MANIFEST_MISSING`）。
- `PromotionRecord.version_id` MUST 与其所验证的 `ReleaseVerificationReport.version_id` 一致；不一致 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复晋级、重复验证或重复回滚；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 发布产物清单：`manifest_id`
  - 晋级记录：`promotion_id`
  - 发布验证报告：`report_id`
  - 回滚记录：`rollback_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `version_id`）、相同环境上下文与相同验证口径下重复执行时：
  - 晋级判定（`PromotionRecord.result`）与发布验证判定（`ReleaseVerificationReport.overall_pass`）SHALL 在本 spec 定义的等价范围内一致。
  - 晋级阻断的 `rejection_reason_code`（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at` 等时间戳
  - 系统生成的记录标识（若未由调用方提供）
- 除上述显式允许项外，判定结果差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测发布验证漂移（例如同一 `version_id` 在同环境下验证结果不同）。
- 偏差事件 MUST 至少包含：`version_id`、环境上下文、偏差类型与可行动摘要（例如失败检查项摘要）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：发布验证失败、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于发布验证失败（`VERIFICATION_FAILED`）与晋级阻断（`PROMOTION_BLOCKED`），系统 MUST 产出可行动的整改线索（最小：失败类别、影响面、关联标识符、验证报告路径/摘要）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：晋级/验证/回滚计数、失败原因分布、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `version_id/request_id/trace_id`（若适用）定位。
- audit：对关键拒绝/阻断/回滚必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外流量的前提下并行执行发布验证与配置校验，仅记录结果与审计，用于校准门禁口径。
- **Canary**：仅对小流量/白名单环境或节点生效，监控 SLO、错误率与回滚可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 发布验证失败或 Gate-0/Gate-1 最小回归失败 MUST 触发回滚或阻断。
- 关键 SLO 异常（见 `observability-slos`）持续上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **发布产物不可追溯**：缺失清单导致无法审计与回滚  
   - 缓解：发布产物清单强制（契约/`data_dictionary.md`）+ Gate-2 阻断策略（本文件/`acceptance.md`）

2) **回滚不可用或不完整**：失败后无法恢复到稳定版本  
   - 缓解：回滚记录契约（契约）+ 回滚触发条件（本文件）+ 审计可用性（`audit_log.md`）

3) **环境漂移导致验证不可信**：同版本在不同节点表现不一致  
   - 缓解：确定性边界与漂移检测（本文件）+ 指标与日志定位（`observability.md`）

4) **越权发布/晋级**：未授权主体推进到高环境  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
