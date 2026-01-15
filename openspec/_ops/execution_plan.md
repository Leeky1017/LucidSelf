# OpenSpec Execution Plan (DAG + Priority)

本文件给出 `openspec/SPECS_INDEX.md` 定义的 26 个 specs 的**最终执行序列**（单线程、可回归、可审计），并为每个 spec 列出依赖摘要与 Gate 归属。

## 排序规则（来源：SPECS_INDEX）

- 依赖必须先完成（DAG 拓扑序）。
- 在“可执行（依赖已清零）”的候选中，优先级按：P0 → P1 → P2 → 资产门禁。
- 若高优先级 spec 被低优先级依赖阻断，则先执行其依赖 spec 以解阻断。

## 最终执行序列（Spec Slug）

1. engine-id-governance
2. identity-and-data-isolation
3. observability-slos
4. security-privacy-compliance
5. versioning-and-deviation-detection
6. production-defaults-no-mock
7. bootability-and-regression-baseline
8. corpus-governance
9. citations-evidence-protocol
10. golden-sets-and-regression
11. semantic-layer-core
12. text-normalization-alignment
13. cross-book-consistency-conflicts
14. semantic-extraction-quality-gates
15. billing-and-entitlements
16. deployment-release
17. abuse-and-rate-limits
18. playbook-and-action-loop
19. knowledge-graph-runtime-semanticquery
20. corpus-release-pipeline
21. llm-narrative-layer
22. fusion-engine-explainability
23. seven-engine-pipeline-e2e
24. geocoding-first-class
25. commercial-readiness-gates
26. proofreading-workflow-qa

## 依赖摘要与 Gate 归属

| Spec | 优先级 | Gate | 依赖（必须先完成） |
| --- | --- | --- | --- |
| engine-id-governance | P0 | Gate-0 | 无 |
| identity-and-data-isolation | P0 | Gate-0 | 无 |
| observability-slos | P0 | Gate-0 | 无 |
| security-privacy-compliance | P0 | Gate-0 | 无 |
| versioning-and-deviation-detection | P0 | Gate-0 | engine-id-governance |
| production-defaults-no-mock | P0 | Gate-0 | identity-and-data-isolation, security-privacy-compliance |
| bootability-and-regression-baseline | P0 | Gate-1 | observability-slos |
| corpus-governance | 资产层 | 资产门禁 | 无 |
| citations-evidence-protocol | P0 | Gate-1 | corpus-governance, versioning-and-deviation-detection |
| golden-sets-and-regression | P0 | Gate-1 | bootability-and-regression-baseline, observability-slos |
| semantic-layer-core | P0 | Gate-1 | engine-id-governance, identity-and-data-isolation, citations-evidence-protocol |
| text-normalization-alignment | 资产层 | 资产门禁 | corpus-governance |
| cross-book-consistency-conflicts | 资产层 | 资产门禁 | corpus-governance |
| semantic-extraction-quality-gates | P1 | Gate-1 | text-normalization-alignment, corpus-governance |
| billing-and-entitlements | P1 | Gate-3 | identity-and-data-isolation |
| deployment-release | P1 | Gate-2 | production-defaults-no-mock, bootability-and-regression-baseline, observability-slos |
| abuse-and-rate-limits | P1 | Gate-2 | identity-and-data-isolation, observability-slos |
| playbook-and-action-loop | P1 | Gate-2 | observability-slos |
| knowledge-graph-runtime-semanticquery | P1 | Gate-2 | semantic-layer-core, observability-slos |
| corpus-release-pipeline | P1 | Gate-2 | corpus-governance, semantic-extraction-quality-gates, cross-book-consistency-conflicts |
| llm-narrative-layer | P2 | Gate-2 | citations-evidence-protocol, observability-slos |
| fusion-engine-explainability | P0 | Gate-2 | llm-narrative-layer, citations-evidence-protocol |
| seven-engine-pipeline-e2e | P0 | Gate-2 | engine-id-governance, semantic-layer-core, corpus-release-pipeline, observability-slos |
| geocoding-first-class | P2 | Gate-3 | text-normalization-alignment, observability-slos |
| commercial-readiness-gates | P1 | Gate-3 | deployment-release, security-privacy-compliance, billing-and-entitlements |
| proofreading-workflow-qa | 资产层 | 资产门禁 | semantic-extraction-quality-gates |

