# LLM叙述层 Design

## 设计意图
本设计文档用于固定「LLM叙述层」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `citations-evidence-protocol`, `security-privacy-compliance`, `observability-slos`, `versioning-and-deviation-detection`

## 必备标识符（最小集）
- `user_id`, `engine_id`, `version_id`, `prompt_id`, `model_version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `CitationBinding.chain_id` MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- 叙述输出中声明的引用（若存在）MUST 与 `CitationBinding.chain_id` 所含引用锚点一致或可判定兼容；不一致 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复输出/重复绑定/重复安全审计导致审计链路漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 叙述输出：`output_id`
  - 引用绑定：`binding_id`
  - 内容安全审计：`safety_audit_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id/engine_id/version_id/prompt_id/model_version_id`）下重复生成时：
  - 输出 MUST 始终满足 `output_schema_version` 约束（结构可判定）。
  - 引用绑定（`chain_id`）与内容安全审计结论（ALLOW/BLOCK）SHALL 在本 spec 定义的等价范围内一致。

### 等价范围（最小）
- 由于 LLM 生成具有固有随机性，允许的非确定性字段/差异 MUST 被显式标注并可审计：
  - 自然语言措辞差异（在不改变结构化 schema 与引用/安全结论的前提下）
  - `created_at` 等时间戳
- 除上述显式允许项外，输出结构/引用/安全结论差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测叙述输出偏差（例如同一输入在同版本下产生不同的引用绑定或违反 schema）。
- 偏差事件 MUST 至少包含：`user_id`、`engine_id`、`version_id`、`prompt_id`、`model_version_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：内容安全违规、引用不可解析、schema 不满足（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于内容安全违规（`CONTENT_SAFETY_VIOLATION`），系统 MUST 阻断对外输出并形成可审计事件。
- 对于引用不可解析（`CITATION_NOT_RESOLVABLE`）或 schema 不满足（`OUTPUT_SCHEMA_INVALID`），系统 MUST 阻断并产出可行动整改线索（最小：失败原因 + 关联标识符 + 证据路径）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：叙述请求计数、阻断原因分布、引用绑定失败计数、安全阻断计数、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `user_id/engine_id/version_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断/安全审计必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：不影响对外行为的前提下并行生成叙述与安全/引用校验，仅记录差异与审计，用于校准 schema 与安全策略。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 或内部调用方生效，监控安全阻断率、引用可解析性与延迟。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 安全事件或安全阻断率异常上升 MUST 触发回滚或阻断。
- 引用不可解析失败率上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **幻觉/无证据叙述**：输出缺失可解析引用或引用不一致  
   - 缓解：引用可解析性阻断（本文件/`data_dictionary.md`）+ 引用协议（`citations-evidence-protocol`）+ Gate-2 阻断策略（`acceptance.md`）

2) **内容安全事故**：输出包含不合规/敏感内容  
   - 缓解：内容安全审计与阻断（本文件/契约）+ 审计导出（`audit_log.md`）+ 回滚触发条件（本文件）

3) **隐私泄露**：日志/审计包含用户自由文本或敏感原文  
   - 缓解：最小化/脱敏（`security.md`/`audit_log.md`）+ 标签约束（`observability.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
