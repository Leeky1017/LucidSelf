# 语义层核心 Design

## 设计意图
本设计文档用于固定「语义层核心」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `citations-evidence-protocol`

## 必备标识符（最小集）
- `engine_id`, `user_id`, `version_id`, `corpus_release_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `SemanticIndexEntry.semantic_entry_id` MUST 可解析到 `SemanticEntry.semantic_entry_id`；不可解析 MUST 阻断并返回确定性拒绝原因（`SEMANTIC_ENTRY_NOT_FOUND` 或 `VALIDATION_FAILED`）。
- `ProvenanceRecord.semantic_entry_id` MUST 可解析到 `SemanticEntry.semantic_entry_id`；不可解析 MUST 阻断。
- `CitationAnchorBinding.anchor_id` MUST 可解析到 `citations-evidence-protocol` 的 `CitationAnchor.anchor_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `CitationAnchorBinding.corpus_release_id` MUST 与语义条目上下文的 `corpus_release_id` 一致或可判定兼容；不一致 MUST 阻断（`VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复写入造成语义索引漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 语义条目：`semantic_entry_id`
  - 索引条目：`index_entry_id`
  - 溯源记录：`provenance_id`
  - 引用锚点绑定：`binding_id`
  - 查询响应：`response_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id`/`engine_id`/`version_id`/`corpus_release_id`）与相同索引视图下重复查询时：
  - 查询结果集合在本 spec 定义的等价范围内 SHALL 一致。
  - 引用锚点绑定的可解析性错误与拒绝原因代码（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at` 等时间戳
  - 系统生成的 `response_id/query_id`（若未由调用方提供）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测语义查询漂移（例如同一查询在同版本语义下返回不同结果集合）。
- 偏差事件 MUST 至少包含：`user_id`、`engine_id`、`version_id`、`corpus_release_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：输入缺失/非法、引用不可解析、越权等（通常不可重试）。
- **阻断（BLOCK）**：门禁检查失败、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符）。

### 信号产物（最小）
- metrics：查询请求计数、拒绝原因分布、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `user_id`/`engine_id`/`version_id`/`request_id`（若适用）定位。
- audit：对关键拒绝/阻断必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外行为的前提下并行执行语义查询与索引构建，用于验证结果一致性与引用锚点可解析性。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 或内部调用方生效，监控拒绝率/漂移事件与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 漂移/偏差事件持续上升（例如 `ls_semantic_layer_drift_events_total` 激增）MUST 触发回滚或阻断。
- 引用锚点绑定失败率超过阈值（例如 `ls_semantic_layer_anchor_binding_failures_total` 激增）MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-1 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **语义查询漂移导致不可复现**：同一输入在同版本语义下返回不同结果集合  
   - 缓解：确定性边界与偏差检测（本文件）+ 漂移事件指标（`observability.md`）+ 可审计偏差事件（`audit_log.md`）

2) **引用锚点不可解析导致“无证据输出”**：绑定的 anchor 无法解析到语料资产  
   - 缓解：引用可解析性阻断（本文件/`data_dictionary.md`）+ Gate-1 阻断策略（`acceptance.md`）

3) **越权/隔离失效**：跨 `user_id/org_id` 读取/写入语义条目或查询结果  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

4) **高基数可观测导致成本失控**：将 `user_id/query_id` 作为 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

5) **审计缺失导致不可追责**：关键拒绝/阻断未形成审计链路  
   - 缓解：审计字段契约（`audit_log.md`）+ Gate-1 阻断策略（`acceptance.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
