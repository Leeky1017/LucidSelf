# 知识图谱运行时语义查询 Design

## 设计意图
本设计文档用于固定「知识图谱运行时语义查询」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `semantic-layer-core`, `observability-slos`, `citations-evidence-protocol`

## 必备标识符（最小集）
- `user_id`, `engine_id`, `version_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败 MUST 阻断晋级，并产出可行动的整改项清单（最小：失败原因 + 关联标识符 + 证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `SemanticQueryResponse.query_id` MUST 可解析到 `SemanticQueryRequest.query_id`；不可解析 MUST 阻断（`VALIDATION_FAILED`）。
- 查询结果（若包含引用锚点/证据链字段）MUST 能解析到引用协议（`citations-evidence-protocol`）；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE` 或 `VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复查询写入/缓存污染导致结果漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 查询请求：`query_id`
  - 查询响应：`response_id`
  - 一致性声明：`declaration_id`
  - 延迟 SLO：`slo_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id/engine_id/version_id`）与相同索引视图下重复查询时：
  - 查询结果集合在本 spec 定义的等价范围内 SHALL 一致。
  - 拒绝/阻断原因代码（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at` 等时间戳
  - 系统生成的 `response_id/query_id`（若未由调用方提供）
  - 结果排序的等价规则（例如允许同分并列的稳定排序差异）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测运行时查询漂移（例如同一 `query_key` 在同版本下返回不同结果集合）。
- 偏差事件 MUST 至少包含：`user_id`、`engine_id`、`version_id`、偏差类型与可行动摘要（例如受影响查询键）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：输入缺失/非法、越权等（通常不可重试）。
- **阻断（BLOCK）**：漂移检测触发、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于漂移检测（`DRIFT_DETECTED`），系统 MUST 阻断并产出可行动整改线索（最小：偏差类型 + 关联标识符 + 证据路径）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）
- metrics：查询请求计数、拒绝原因分布、漂移事件计数、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `user_id/engine_id/version_id/query_id/request_id`（若适用）定位。
- audit：对关键拒绝/阻断必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外行为的前提下并行执行查询与漂移检测，仅记录差异与审计，用于校准等价范围与 SLO。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 或内部调用方生效，监控漂移事件与延迟 SLO。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 漂移/偏差事件持续上升 MUST 触发回滚或阻断。
- 延迟超过 SLO 阈值（见 `observability.md`/`performance.md`）持续上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-2 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **结果漂移导致不可复现**：同一查询在同版本下返回不同结果集合  
   - 缓解：确定性边界与漂移检测（本文件）+ 漂移事件指标（`observability.md`）+ 审计导出（`audit_log.md`）

2) **延迟超标影响用户体验**：运行时查询 p95/p99 不稳定  
   - 缓解：延迟 SLO 与性能目标（`observability.md`/`performance.md`）+ 回滚触发条件（本文件）

3) **越权/隔离失效**：跨 `user_id/org_id` 读取图谱数据  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
