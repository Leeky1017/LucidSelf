# 校对工作流与QA Design

## 设计意图
本设计文档用于固定「校对工作流与QA」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`semantic-extraction-quality-gates`

## 必备标识符（最小集）
- `corpus_release_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）

- `DefectRecord.chain_id`（若适用）MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。

### 幂等 / 去重（MUST）

- 系统 MUST 定义确定性的去重键，以避免重复校对任务、重复缺陷、重复批准记录或重复指标报表导致审计链路漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 校对任务：`task_id`
  - 缺陷记录：`defect_id`
  - 批准记录：`approval_id`
  - QA 指标报表：`report_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）

- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）

- 在相同输入（含 `corpus_release_id/version_id` 与同一缺陷/批准快照）下重复评估时：
  - 输出 MUST 始终满足契约 schema 约束（结构可判定）。
  - QA 指标报表与门禁结论 SHALL 在本 spec 定义的等价范围内一致。

### 等价范围（最小）

- 允许的非确定性字段/差异 MUST 被显式标注并可审计：
  - `created_at` 等时间戳
- 除上述显式允许项外，缺陷统计/批准结论/门禁判定差异 MUST 视为偏差。

### 偏差检测与解释（MUST）

- 系统 MUST 能检测 QA 结果偏差（例如同一语料版本在同输入快照下产生不同的缺陷统计或批准结论）。
- 偏差事件 MUST 至少包含：`corpus_release_id`、`version_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）

- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：证据不可解析、schema 不满足、审批链不完整（通常需要整改或补齐复核）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）

- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于证据不可解析（`CITATION_NOT_RESOLVABLE`）或 schema 不满足（`OUTPUT_SCHEMA_INVALID`），系统 MUST 阻断资产晋级并产出可行动整改线索（最小：失败原因 + 关联标识符 + 证据路径）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）

- metrics：校对任务计数、缺陷分布、批准率、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `corpus_release_id/version_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/批准决策必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）

- **Shadow**：不影响资产发布的前提下并行执行 QA/校对门禁评估，仅记录差异与审计，用于校准缺陷分类与门禁阈值。
- **Canary**：仅对小范围语料发布/内部发布生效，监控缺陷分布、批准链完整性与导出可用性。
- **Gradual**：逐步扩大适用范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）

- P0 缺陷或高严重度缺陷异常上升 MUST 阻断资产晋级或触发回滚。
- 审计导出不可用/失败 MUST 视为资产门禁阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **缺陷漏检**：校对覆盖不足导致错误资产进入发布  
   - 缓解：缺陷度量与门禁阈值（`observability.md`）+ 审计导出（`audit_log.md`）+ 资产门禁阻断策略（`acceptance.md`）

2) **批准链不可追责或被绕过**：缺失批准记录或权限越权  
   - 缓解：批准记录契约（`contract/*.json`/`data_dictionary.md`）+ 访问控制（`security.md`）+ 资产门禁阻断策略（`acceptance.md`）

3) **敏感信息泄露**：缺陷描述或证据包含敏感原文  
   - 缓解：最小化/脱敏（`security.md`/`audit_log.md`）+ 证据链引用（`citations-evidence-protocol`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
