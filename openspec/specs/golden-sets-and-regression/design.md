# Golden Set与回归评测 Design

## 设计意图
本设计文档用于固定「Golden Set与回归评测」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`bootability-and-regression-baseline`, `observability-slos`

## 必备标识符（最小集）
- `version_id`, `corpus_release_id`, `engine_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `CoverageReport.golden_set_id` / `RegressionThreshold.golden_set_id` / `RegressionRunResult.golden_set_id` / `DriftAlert.golden_set_id` MUST 可解析到同版本语义下的 `GoldenSetDefinition.golden_set_id`；不可解析 MUST 阻断并返回确定性拒绝原因（`INVALID_GOLDEN_SET_ID` 或 `VALIDATION_FAILED`）。
- `RegressionThreshold.metric_name` MUST 属于本 spec 固定的可评测指标集合；不在集合内 MUST 被拒绝（`VALIDATION_FAILED`）。
- `RegressionThreshold.comparator` MUST 属于枚举（>=/>/<=/<）；否则 MUST 被拒绝（`THRESHOLD_INVALID`）。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复写入造成评测记录漂移；去重键仅允许由契约字段构成（禁止隐式外部状态）。
- 约定的最小去重键（规格级语义）：
  - golden set 定义：`golden_set_id` + `version_id`
  - 覆盖率报告：`coverage_report_id`
  - 阈值定义：`threshold_id`
  - 回归运行结果：`run_id`
  - 漂移告警：`alert_id`
- 对相同去重键的重复提交：
  - 若提交内容等价（在本 spec 定义的等价范围内）SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`VALIDATION_FAILED` 或 `THRESHOLD_INVALID`）。

### 冲突处理（MUST）
- 冲突的判定与拒绝原因 MUST 可复现、确定性（相同输入得到相同拒绝代码）。
- 冲突 MUST 记录审计事件，且审计记录必须遵循最小化/脱敏原则。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `golden_set_id`/`version_id`/`corpus_release_id`/`engine_id`）与相同评测口径下重复执行时：
  - 评测结论（PASS/FAIL、阈值对比结果）在本 spec 定义的等价范围内 SHALL 一致。
  - 拒绝原因代码（若适用）SHALL 确定性一致。

### 等价范围（最小）
- 允许的非确定性字段（若存在）MUST 被显式标注并可审计，例如：
  - `created_at/started_at/finished_at` 时间戳
  - 系统生成的 `run_id/coverage_report_id/alert_id`（若未由调用方提供）
- 除上述显式允许项外，输出差异 MUST 视为偏差。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测评测漂移（例如同一 `golden_set_id` 在同版本语义下得到不同 PASS/FAIL 结论或覆盖率显著变化）。
- 偏差事件 MUST 至少包含：`golden_set_id`、`version_id`、`corpus_release_id`、`engine_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 失败分类（最小）
- **拒绝（DENY）**：输入缺失/非法、指标名不支持、阈值非法等（通常不可重试）。
- **阻断（BLOCK）**：门禁检查失败、关键依赖不可用导致无法保证一致性/审计（通常需要人工整改或回滚）。
- **内部错误（INTERNAL_ERROR）**：非预期异常（可能可重试）。

### 策略（MUST/SHALL）
- 对于拒绝与冲突，系统 MUST 返回确定性的拒绝原因代码（见契约 `rejection_reasons`）并写入审计记录。
- 对于内部错误，系统 SHOULD 标记 `retryable=true` 并允许上游按策略重试；重复失败 MUST 触发阻断信号。
- 对于阻断场景，系统 MUST 形成可行动的整改项线索（最小：失败类别、影响面、关联标识符）。

### 信号产物（最小）
- metrics：评测请求计数、阈值失败计数、漂移事件计数（见 `observability.md`）。
- logs/traces：可按 `golden_set_id`/`version_id`/`engine_id`/`request_id`（若适用）定位。
- audit：对关键拒绝/阻断必须生成审计记录（见 `audit_log.md`）。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外行为的前提下并行运行评测与阈值判定，验证覆盖率/通过率分布与漂移告警质量。
- **Canary**：仅对一小部分 golden set 或内部调用方生效，监控阈值失败率/漂移告警率与审计可用性。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 阈值失败率或漂移告警率超过阈值（例如 `ls_golden_sets_threshold_failures_total` 激增）MUST 触发回滚或阻断。
- 回归运行失败（不可重试错误）持续上升且无法在短期内修复 MUST 触发回滚或降级到只生成报告不阻断（若允许）。
- 审计记录不可用/不可导出 MUST 视为 Gate-1 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **阈值口径漂移导致误判**：指标名/口径变化导致 PASS/FAIL 不可比  
   - 缓解：阈值字段级约束（`data_dictionary.md`）+ 指标名固定与拒绝策略（本文件）+ 审计记录（`audit_log.md`）

2) **覆盖率不足导致回归无效**：golden set 覆盖不足仍允许晋级  
   - 缓解：覆盖率指标与 SLO（`observability.md`）+ Gate-1 失败阻断策略（`acceptance.md`）

3) **高基数可观测导致成本失控**：将 `golden_set_id/version_id` 作为 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

4) **越权/隔离失效**：非授权主体触发回归或读取评测结果  
   - 缓解：访问控制/隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）

5) **审计缺失导致不可追责**：阈值阻断未形成审计链路  
   - 缓解：审计字段契约（`audit_log.md`）+ Gate-1 阻断策略（`acceptance.md`）

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。
