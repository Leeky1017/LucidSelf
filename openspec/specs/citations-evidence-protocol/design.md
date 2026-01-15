# 引用与证据协议 Design

## 设计意图
本设计文档用于固定「引用与证据协议」在规格层面的设计立场：契约、数据完整性、门禁与审计。禁止写实现细节。

## 依赖关系
- 上游依赖：`corpus-governance`, `versioning-and-deviation-detection`

## 必备标识符（最小集）
- `corpus_release_id`, `version_id`, `user_id`

## 关键决策（非实现）
- 所有用户可见结论必须可追溯到 `version_id` 与证据链（如适用）。
- 门禁失败必须阻断晋级，并产出可行动的整改项清单。
- 可观测与审计字段是契约的一部分，必须被一致执行。

## 数据完整性语义（规格层）

### 引用可解析性（MUST）
- `CitationAnchor.asset_id` MUST 可解析到语料治理（`corpus-governance`）的资产登记；不可解析 MUST 阻断并返回确定性拒绝原因（`CITATION_NOT_RESOLVABLE`）。
- `CitationAnchor.corpus_release_id` MUST 与证据链的 `corpus_release_id` 一致或可判定兼容；不一致 MUST 阻断。
- `ProvenanceRecord.chain_id` 与 `AuditExportBundle.chain_id` MUST 可解析到 `EvidenceChain.chain_id`；不可解析 MUST 阻断。

### 幂等 / 去重（MUST）
- 系统 MUST 定义确定性的去重键，以避免重复证据链/引用产生漂移；去重键仅允许由契约字段构成。
- 约定的最小去重键（规格级语义）：
  - 引用锚点：`anchor_id`
  - 证据链：`chain_id`
  - 溯源记录：`provenance_id`
  - 审计导出包：`bundle_id`
- 对相同去重键的重复提交：
  - 若提交内容等价 SHALL 视为幂等成功。
  - 若提交内容不等价 MUST 视为冲突并拒绝（`EVIDENCE_CHAIN_INVALID` 或 `VALIDATION_FAILED`）。

## 运行时确定性与偏差口径（规格层）

### 确定性边界（SHALL）
- 在相同输入（含 `user_id`/`version_id`/`corpus_release_id`）与相同语料版本语义下重复生成证据链时：
  - 证据链的引用锚点集合在等价范围内 SHALL 一致。
  - 引用不可解析/缺失标识符的拒绝原因代码 SHALL 确定性一致。

### 偏差检测与解释（MUST）
- 系统 MUST 能检测证据链漂移（例如同一输入在同版本语义下产出不同引用集合）。
- 偏差事件 MUST 至少包含：`user_id`、`version_id`、`corpus_release_id`、偏差类型与可行动摘要。

## 失败处理策略与信号产物（规格层）

### 策略（最小）
- 引用不可解析或缺失关键标识符 MUST 被拒绝并阻断进入 Gate-1。
- 拒绝/阻断 MUST 形成审计记录，并可导出。

## 非目标
- 不规定具体存储/消息队列/监控方案。
- 不包含任何代码路径、伪代码或接口实现。

## 发布策略（Rollout）与回滚触发（规格层）

### 分阶段 rollout（最小）
- **Shadow**：在不影响对外行为的前提下并行生成证据链校验与审计记录，用于验证可解析性与拒绝原因分布。
- **Canary**：仅对一小部分请求生效（例如内部调用方/白名单范围），监控拒绝率/阻断率/漂移事件。
- **Gradual**：逐步扩大生效范围直至全量；扩容步骤 MUST 可审计（记录 rollout 阶段与范围）。

### 回滚触发条件（MUST）
- 引用不可解析失败率超过阈值（例如 `ls_citations_evidence_anchor_resolution_failures_total` 激增）MUST 触发回滚或阻断。
- 漂移/偏差事件持续上升且无法在短期内修复 MUST 触发回滚或降级到只校验不生成（若允许）。
- 审计记录不可用/不可导出 MUST 视为 Gate-1 阻断条件。

## Top 风险与缓解（写入门禁/证据/回退）

1) **引用不可解析导致“无证据输出”**：LLM 或上游输出缺少可定位锚点  
   - 缓解：引用可解析性阻断（本文件）+ 字段级约束（`data_dictionary.md`）+ 失败阻断策略（`acceptance.md`）

2) **证据链漂移导致不可复现**：同一输入在同版本语义下产出不同引用集合  
   - 缓解：确定性边界（本文件）+ 偏差检测指标（`observability.md`）+ 可审计偏差事件（`audit_log.md`）

3) **高基数可观测导致成本失控**：将 `user_id/version_id/chain_id` 作为 metric 标签  
   - 缓解：标签约束（`observability.md`）+ 成本阈值与告警（`cost.md`）

4) **隐私/合规风险**：审计导出或日志包含不必要敏感原文  
   - 缓解：脱敏与最小化（`audit_log.md`/`security.md`）+ 留存期限与删除口径（`compliance.md`）

5) **越权导出/跨边界访问**：非授权主体读取/导出他人证据链  
   - 缓解：访问控制与隔离边界（`security.md`）+ 越权拒绝审计（`audit_log.md`）
