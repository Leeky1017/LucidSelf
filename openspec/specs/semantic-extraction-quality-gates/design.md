# 语义抽取质量门禁 Design

## 设计意图
本设计文档用于固定「语义抽取质量门禁」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`engine-id-governance`, `identity-and-data-isolation`, `citations-evidence-protocol`
- 上游依赖：`text-normalization-alignment`, `corpus-governance`

## 必备标识符（最小集）
- `engine_id`, `user_id`, `org_id`, `version_id`, `corpus_release_id`

## 关键决策（非实现）
- 所有门禁判定必须可追溯到 `version_id` 与 `corpus_release_id`（以及 `engine_id/user_id/org_id` 责任边界），并可审计复现。
- 门禁失败 MUST 阻断 Gate-1 晋级/发布/对外开放，并产出可行动的整改线索（最小：失败原因 + 关联标识符 + 失败样本/证据路径）。
- 可观测与审计字段是契约的一部分，必须被一致执行（见 `observability.md` / `audit_log.md`）。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `QualityThresholdConfig.metric_name` MUST 可解析到 `QualityMetricDefinition.metric_name`；不可解析 MUST 阻断（`METRIC_DEFINITION_INVALID`）。
- `FailureSample.reference_id` 若被声明为 `citations-evidence-protocol` 的 `CitationAnchor.anchor_id`，则 MUST 可解析；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE`）。
- `FailureSample.chain_id`（若适用）MUST 可解析到 `citations-evidence-protocol` 的 `EvidenceChain.chain_id`；不可解析 MUST 阻断（`CITATION_NOT_RESOLVABLE` 或 `VALIDATION_FAILED`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复写入导致门禁判定漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - 指标定义：`metric_id`
  - 阈值配置：`threshold_id`
  - 门禁运行结果：`gate_run_id`
  - 失败样本：`sample_id`
  - 复检记录：`recheck_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `engine_id/user_id/org_id/version_id/corpus_release_id`）、相同阈值配置版本与相同度量口径下重复评估时：
  - `QualityGateRunResult.overall_pass` 与 `result` SHALL 在本 spec 定义的等价范围内一致。
  - `rejection_reason_code`（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at/started_at/finished_at` 等时间戳
  - 系统生成的 `gate_run_id`（若未由调用方提供）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测门禁判定漂移（例如同一输入在同阈值配置版本下得到不同判定）。
- 偏差事件 MUST 至少包含：`engine_id`、`version_id`、`corpus_release_id`、偏差类型与可行动摘要（例如受影响指标/阈值）。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：输入缺失/非法、引用不可解析、越权等（通常不可重试）。
- **阻断（BLOCK）**：门禁阈值未满足、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **降级（DEGRADED）**：非关键指标缺失或次要校验失败时的受控退化（必须可审计；不得掩盖门禁失败）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于门禁阈值失败（`QUALITY_GATE_FAILED`），系统 MUST 产出失败样本清单（最小：指标名/严重度/可解析引用或证据链）。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符、证据路径）。

### 信号产物（最小）
- metrics：门禁评估计数、拒绝原因分布、漂移事件计数、审计记录写入计数（见 `observability.md`）。
- logs/traces：可按 `engine_id/version_id/corpus_release_id/request_id/trace_id`（若适用）定位。
- audit：对关键拒绝/阻断/阈值失败必须生成审计记录（见 `audit_log.md`）。
- artifacts：失败样本清单（`FailureSample`）与复检记录（`RecheckRecord`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：不影响对外行为的前提下并行评估门禁，仅记录判定/失败样本/审计，用于校准阈值与误报。
- **Canary**：仅对小流量/白名单 `user_id/org_id` 或内部调用方生效，监控阻断率/误报率与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 阻断率异常上升（例如 `ls_semantic_extraction_quality_gate_requests_total{result="BLOCK"}` 激增）MUST 触发回滚或阻断。
- 漂移/偏差事件持续上升 MUST 触发回滚或阻断。
- 审计记录不可用/不可导出 MUST 视为 Gate-1 阻断条件。
- 成本超预算阈值（见 `cost.md`）MUST 触发回滚或限流/降级。

## Top 风险与缓解（写入门禁/证据/回退）

1) **阈值误报导致不必要阻断**：对外质量门禁过严影响可用性  
   - 缓解：Shadow 校准 + Canary 监控（本文件）+ 阻断率指标（`observability.md`）+ 复检记录（`audit_log.md`/`RecheckRecord`）

2) **门禁漏报导致“低质输出”进入下游**：阈值/口径不完整或被绕过  
   - 缓解：指标口径/阈值配置字段级约束（`data_dictionary.md`）+ 失败样本清单强制产出（本文件）+ Gate-1 阻断策略（`acceptance.md`）

3) **引用不可解析导致证据链断裂**：失败样本无法定位到语料/锚点  
   - 缓解：引用可解析性阻断（本文件/`data_dictionary.md`）+ 引用协议（`citations-evidence-protocol`）+ 审计导出校验（`audit_log.md`）

4) **越权/隔离失效**：跨 `user_id/org_id` 读取/写入门禁产物  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

5) **高基数可观测导致成本失控**：将 `user_id/version_id` 作为默认 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
