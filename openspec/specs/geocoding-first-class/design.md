# 地理编码一等公民 Design

## 设计意图
本设计文档用于固定「地理编码一等公民」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`text-normalization-alignment`, `observability-slos`

## 必备标识符（最小集）
- `version_id`, `user_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）

- 地理编码产物中若包含证据链字段（例如 `chain_id` 或等价字段），其值 MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE` 或 `VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）

- 系统 MUST 定义确定性的去重键，以避免重复地理实体、重复精度/置信度元数据、重复回退记录或重复指标报表导致审计链路漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 标准化地理实体：`geo_entity_id`
  - 精度/置信度元数据：`confidence_id`
  - 回退记录：`fallback_id`
  - 指标报表：`report_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）

- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）

- 在相同输入（含 `user_id/version_id` 以及相关配置版本）下重复地理编码时：
  - 输出 MUST 始终满足契约 schema 约束（结构可判定）。
  - 标准化地理实体（`normalized_name`/坐标/精度枚举）SHALL 在本 spec 定义的等价范围内一致。

### 等价范围（最小）

- 允许的非确定性字段/差异 MUST 被显式标注并可审计：
  - `created_at` 等时间戳
- 除上述显式允许项外，标准化结果/精度枚举/回退策略差异 MUST 视为偏差。

### 偏差检测与解释（MUST）

- 系统 MUST 能检测地理编码输出偏差（例如同一输入在同版本下产生不同坐标或不同精度/回退策略）。
- 偏差事件 MUST 至少包含：`user_id`、`version_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）

- **拒绝（DENY）**：标识符缺失/非法、越权等（通常不可重试）。
- **回退（FALLBACK）**：精度不足或不确定性过高（返回更粗粒度结果并记录回退）。
- **阻断（BLOCK）**：schema 不满足、关键字段不可判定（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）

- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于精度/置信度不足，系统 SHOULD 触发回退策略并生成 `FallbackRecord`；回退策略与原因 MUST 可审计。
- 对于 schema 不满足（`OUTPUT_SCHEMA_INVALID`）或关键字段不一致（`VALIDATION_FAILED`），系统 MUST 阻断并产出可行动整改线索（最小：失败原因 + 关联标识符 + 证据路径）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。

### 信号产物（最小）

- metrics：请求计数、回退率、阻断原因分布、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `user_id/version_id/request_id`（若适用）定位。
- audit：对关键拒绝/回退/阻断必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）

- **Shadow**：不影响对外行为的前提下并行执行地理编码并记录结果/回退/审计，用于校准归一化与精度阈值。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 生效，监控回退率、精度分布与延迟。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）

- 回退率（`ls_geocoding_fallbacks_total`）异常上升 MUST 触发回滚或阻断扩量。
- 精度分布异常漂移（例如 `precision=UNKNOWN` 比例上升）MUST 触发回滚或阻断扩量。
- 审计记录不可用/不可导出 MUST 视为 Gate-3 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **错误地理编码**：坐标/精度错误导致下游解释或用户体验受损  
   - 缓解：精度/置信度元数据契约（`data_dictionary.md`）+ 回退策略审计（本文件/`audit_log.md`）+ Gate-3 阻断策略（`acceptance.md`）

2) **隐私泄露**：位置相关数据在日志/审计中泄露  
   - 缓解：最小化/脱敏（`security.md`/`audit_log.md`）+ 标签约束（`observability.md`）

3) **成本不可控**：外部解析或重试导致成本飙升  
   - 缓解：成本阈值与告警（`cost.md`）+ 回滚触发条件（本文件）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
