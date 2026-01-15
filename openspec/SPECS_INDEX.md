# SPECS_INDEX（控制台中枢）

包含：规格清单（≈26）、优先级、门禁归属、依赖 DAG、验收口径、审计闭环方法。

## Specs Overview
ID | 名称 | 优先级 | Owner | 状态 | Gate
--- | --- | --- | --- | --- | ---
engine-id-governance | 引擎ID治理 | P0 | system | 进行中 | Gate-0
identity-and-data-isolation | 身份与数据隔离 | P0 | system | 进行中 | Gate-0
observability-slos | 可观测性与SLO | P0 | system | 进行中 | Gate-0
production-defaults-no-mock | 生产默认值（禁止Mock） | P0 | system | 未开始 | Gate-0
security-privacy-compliance | 安全/隐私/合规 | P0 | system | 进行中 | Gate-0
versioning-and-deviation-detection | 版本化与偏差检测 | P0 | system | 进行中 | Gate-0
bootability-and-regression-baseline | 启动性与回归基线 | P0 | system | 进行中 | Gate-1
citations-evidence-protocol | 引用与证据协议 | P0 | system | 未开始 | Gate-1
golden-sets-and-regression | Golden Set与回归评测 | P0 | system | 未开始 | Gate-1
semantic-layer-core | 语义层核心 | P0 | system | 未开始 | Gate-1
fusion-engine-explainability | 融合引擎可解释性 | P0 | system | 未开始 | Gate-2
seven-engine-pipeline-e2e | 七引擎流水线E2E | P0 | system | 未开始 | Gate-2
semantic-extraction-quality-gates | 语义抽取质量门禁 | P1 | system | 已完成 | Gate-1
abuse-and-rate-limits | 滥用防护与限流 | P1 | system | 未开始 | Gate-2
corpus-release-pipeline | 语料发布流水线 | P1 | system | 已完成 | Gate-2
deployment-release | 部署与发布 | P1 | system | 未开始 | Gate-2
knowledge-graph-runtime-semanticquery | 知识图谱运行时语义查询 | P1 | system | 未开始 | Gate-2
playbook-and-action-loop | Playbook与行动闭环 | P1 | system | 未开始 | Gate-2
billing-and-entitlements | 计费与权益 | P1 | system | 未开始 | Gate-3
commercial-readiness-gates | 商业化就绪门禁 | P1 | system | 未开始 | Gate-3
llm-narrative-layer | LLM叙述层 | P2 | system | 未开始 | Gate-2
geocoding-first-class | 地理编码一等公民 | P2 | system | 未开始 | Gate-3
corpus-governance | 语料治理 | 资产层 | system | 已完成 | 资产门禁
cross-book-consistency-conflicts | 跨书一致性与冲突 | 资产层 | system | 已完成 | 资产门禁
proofreading-workflow-qa | 校对工作流与QA | 资产层 | system | 已完成 | 资产门禁
text-normalization-alignment | 文本归一化与对齐 | 资产层 | system | 已完成 | 资产门禁

## 推荐推进顺序（先做谁 / 卡在哪里 / 何时算完成）
- 先 P0，先 Gate-0/1；资产门禁可并行但会阻断依赖它的下游。
- 阻断点：任一依赖 spec 未完成关键任务（按其 `tasks.md`）即视为阻断。
- 完成：依赖清零 + 关键任务完成 + `openspec validate --specs --strict --no-interactive` 通过 + 验收产物齐备。

### Gate-0
- `engine-id-governance`（P0）：依赖 无
- `identity-and-data-isolation`（P0）：依赖 无
- `observability-slos`（P0）：依赖 无
- `production-defaults-no-mock`（P0）：依赖 `identity-and-data-isolation`, `security-privacy-compliance`
- `security-privacy-compliance`（P0）：依赖 无
- `versioning-and-deviation-detection`（P0）：依赖 `engine-id-governance`

### Gate-1
- `bootability-and-regression-baseline`（P0）：依赖 `observability-slos`
- `citations-evidence-protocol`（P0）：依赖 `corpus-governance`, `versioning-and-deviation-detection`
- `golden-sets-and-regression`（P0）：依赖 `bootability-and-regression-baseline`, `observability-slos`
- `semantic-layer-core`（P0）：依赖 `engine-id-governance`, `identity-and-data-isolation`, `citations-evidence-protocol`
- `semantic-extraction-quality-gates`（P1）：依赖 `text-normalization-alignment`, `corpus-governance`

### Gate-2
- `fusion-engine-explainability`（P0）：依赖 `llm-narrative-layer`, `citations-evidence-protocol`
- `seven-engine-pipeline-e2e`（P0）：依赖 `engine-id-governance`, `semantic-layer-core`, `corpus-release-pipeline`, `observability-slos`
- `abuse-and-rate-limits`（P1）：依赖 `identity-and-data-isolation`, `observability-slos`
- `corpus-release-pipeline`（P1）：依赖 `corpus-governance`, `semantic-extraction-quality-gates`, `cross-book-consistency-conflicts`
- `deployment-release`（P1）：依赖 `production-defaults-no-mock`, `bootability-and-regression-baseline`, `observability-slos`
- `knowledge-graph-runtime-semanticquery`（P1）：依赖 `semantic-layer-core`, `observability-slos`
- `playbook-and-action-loop`（P1）：依赖 `observability-slos`
- `llm-narrative-layer`（P2）：依赖 `citations-evidence-protocol`, `observability-slos`

### Gate-3
- `billing-and-entitlements`（P1）：依赖 `identity-and-data-isolation`
- `commercial-readiness-gates`（P1）：依赖 `deployment-release`, `security-privacy-compliance`, `billing-and-entitlements`
- `geocoding-first-class`（P2）：依赖 `text-normalization-alignment`, `observability-slos`

### 资产门禁
- `corpus-governance`（资产层）：依赖 无
- `cross-book-consistency-conflicts`（资产层）：依赖 `corpus-governance`
- `proofreading-workflow-qa`（资产层）：依赖 `semantic-extraction-quality-gates`
- `text-normalization-alignment`（资产层）：依赖 `corpus-governance`

## Dependencies (Adjacency List)
- 本依赖图 MUST 无环；以 `openspec validate --specs --strict --no-interactive` 的校验结果为准。
- engine-id-governance: none
- identity-and-data-isolation: none
- observability-slos: none
- production-defaults-no-mock: identity-and-data-isolation, security-privacy-compliance
- security-privacy-compliance: none
- versioning-and-deviation-detection: engine-id-governance
- bootability-and-regression-baseline: observability-slos
- citations-evidence-protocol: corpus-governance, versioning-and-deviation-detection
- golden-sets-and-regression: bootability-and-regression-baseline, observability-slos
- semantic-layer-core: engine-id-governance, identity-and-data-isolation, citations-evidence-protocol
- fusion-engine-explainability: llm-narrative-layer, citations-evidence-protocol
- seven-engine-pipeline-e2e: engine-id-governance, semantic-layer-core, corpus-release-pipeline, observability-slos
- semantic-extraction-quality-gates: text-normalization-alignment, corpus-governance
- abuse-and-rate-limits: identity-and-data-isolation, observability-slos
- corpus-release-pipeline: corpus-governance, semantic-extraction-quality-gates, cross-book-consistency-conflicts
- deployment-release: production-defaults-no-mock, bootability-and-regression-baseline, observability-slos
- knowledge-graph-runtime-semanticquery: semantic-layer-core, observability-slos
- playbook-and-action-loop: observability-slos
- billing-and-entitlements: identity-and-data-isolation
- commercial-readiness-gates: deployment-release, security-privacy-compliance, billing-and-entitlements
- llm-narrative-layer: citations-evidence-protocol, observability-slos
- geocoding-first-class: text-normalization-alignment, observability-slos
- corpus-governance: none
- cross-book-consistency-conflicts: corpus-governance
- proofreading-workflow-qa: semantic-extraction-quality-gates
- text-normalization-alignment: corpus-governance

## Gate 归属
- engine-id-governance: Gate-0
- identity-and-data-isolation: Gate-0
- observability-slos: Gate-0
- production-defaults-no-mock: Gate-0
- security-privacy-compliance: Gate-0
- versioning-and-deviation-detection: Gate-0
- bootability-and-regression-baseline: Gate-1
- citations-evidence-protocol: Gate-1
- golden-sets-and-regression: Gate-1
- semantic-layer-core: Gate-1
- fusion-engine-explainability: Gate-2
- seven-engine-pipeline-e2e: Gate-2
- semantic-extraction-quality-gates: Gate-1
- abuse-and-rate-limits: Gate-2
- corpus-release-pipeline: Gate-2
- deployment-release: Gate-2
- knowledge-graph-runtime-semanticquery: Gate-2
- playbook-and-action-loop: Gate-2
- billing-and-entitlements: Gate-3
- commercial-readiness-gates: Gate-3
- llm-narrative-layer: Gate-2
- geocoding-first-class: Gate-3
- corpus-governance: 资产门禁
- cross-book-consistency-conflicts: 资产门禁
- proofreading-workflow-qa: 资产门禁
- text-normalization-alignment: 资产门禁

## 验收口径（命令 / 指标 / 产物）
ID | 验收命令（最小） | 可验证指标（最小） | 必须产物（最小）
--- | --- | --- | ---
engine-id-governance | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/engine-id-governance/`（spec/requirements/tasks/design/acceptance）
identity-and-data-isolation | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/identity-and-data-isolation/`（spec/requirements/tasks/design/acceptance）
observability-slos | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/observability-slos/`（spec/requirements/tasks/design/acceptance）
production-defaults-no-mock | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/production-defaults-no-mock/`（spec/requirements/tasks/design/acceptance）
security-privacy-compliance | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/security-privacy-compliance/`（spec/requirements/tasks/design/acceptance）
versioning-and-deviation-detection | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 身份隔离/安全/版本/生产默认值/可观测基线齐备；失败必须阻断晋级 | `openspec/specs/versioning-and-deviation-detection/`（spec/requirements/tasks/design/acceptance）
bootability-and-regression-baseline | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行 | `openspec/specs/bootability-and-regression-baseline/`（spec/requirements/tasks/design/acceptance）
citations-evidence-protocol | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行 | `openspec/specs/citations-evidence-protocol/`（spec/requirements/tasks/design/acceptance）
golden-sets-and-regression | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行 | `openspec/specs/golden-sets-and-regression/`（spec/requirements/tasks/design/acceptance）
semantic-layer-core | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行 | `openspec/specs/semantic-layer-core/`（spec/requirements/tasks/design/acceptance）
fusion-engine-explainability | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/fusion-engine-explainability/`（spec/requirements/tasks/design/acceptance）
seven-engine-pipeline-e2e | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/seven-engine-pipeline-e2e/`（spec/requirements/tasks/design/acceptance）
semantic-extraction-quality-gates | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 证据链可审计；语义层契约稳定；质量门禁阈值明确；回归基线可执行 | `openspec/specs/semantic-extraction-quality-gates/`（spec/requirements/tasks/design/acceptance）
abuse-and-rate-limits | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/abuse-and-rate-limits/`（spec/requirements/tasks/design/acceptance）
corpus-release-pipeline | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/corpus-release-pipeline/`（spec/requirements/tasks/design/acceptance）
deployment-release | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/deployment-release/`（spec/requirements/tasks/design/acceptance）
knowledge-graph-runtime-semanticquery | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/knowledge-graph-runtime-semanticquery/`（spec/requirements/tasks/design/acceptance）
playbook-and-action-loop | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/playbook-and-action-loop/`（spec/requirements/tasks/design/acceptance）
billing-and-entitlements | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 权益/计费/审批链/支持体系齐备；对外发布记录可审计 | `openspec/specs/billing-and-entitlements/`（spec/requirements/tasks/design/acceptance）
commercial-readiness-gates | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 权益/计费/审批链/支持体系齐备；对外发布记录可审计 | `openspec/specs/commercial-readiness-gates/`（spec/requirements/tasks/design/acceptance）
llm-narrative-layer | `openspec validate --specs --strict --no-interactive` + `openspec list --changes` | 端到端契约/交接校验明确；发布/回滚口径齐备；关键路径可观测 | `openspec/specs/llm-narrative-layer/`（spec/requirements/tasks/design/acceptance）
geocoding-first-class | `openspec validate --specs --strict --no-interactive` + `openspec list --specs` | 权益/计费/审批链/支持体系齐备；对外发布记录可审计 | `openspec/specs/geocoding-first-class/`（spec/requirements/tasks/design/acceptance）
corpus-governance | `openspec validate --specs --strict --no-interactive` | 许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计 | `openspec/specs/corpus-governance/`（spec/requirements/tasks/design/acceptance）
cross-book-consistency-conflicts | `openspec validate --specs --strict --no-interactive` | 许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计 | `openspec/specs/cross-book-consistency-conflicts/`（spec/requirements/tasks/design/acceptance）
proofreading-workflow-qa | `openspec validate --specs --strict --no-interactive` | 许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计 | `openspec/specs/proofreading-workflow-qa/`（spec/requirements/tasks/design/acceptance）
text-normalization-alignment | `openspec validate --specs --strict --no-interactive` | 许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计 | `openspec/specs/text-normalization-alignment/`（spec/requirements/tasks/design/acceptance）

## 审计问题闭环到 Spec 的映射策略
- 将问题映射到最小影响面（spec -> Requirement -> Scenario）。
- 为问题补齐/新增 Scenario，使其可复现、可判定；禁止用模糊叙述代替可执行判定。
- 在对应 spec 的 `tasks.md` 新增可验收任务，并写清通过标准与证据产物（日志/报表/门禁输出）。
- 若影响 Gate-0~3 或资产门禁，则把失败定义为阻断条件，直至任务完成。
- 跨多个 spec 或涉及行为改变时，必须创建/更新 `openspec/changes/<change-id>/`。

## 完成定义（何时算完成）
- 相关 spec 的关键任务完成 + 依赖清零 + `openspec validate --specs --strict --no-interactive` 通过 + 验收产物齐备。
