# Proposal — Enforce Full Proofreading Coverage (CN First) (v1)

## Why

当前 `proofreading-workflow-qa` 的工程实现以“按书抽样”为默认策略（`per_book`），导致中文典籍的大部分条目不会进入精校队列，从而无法满足“典籍必须全部精校”的资产门禁要求。

本 change 的目标是在不改变 OpenSpec 资产门禁/审计约束的前提下，把“精校”从抽样升级为 **全量覆盖**（100% coverage），并先在中文典籍范围内落地；后续再扩展到西方典籍。

## Scope

### In scope（本次变更）
- **范围**：中文典籍（`典籍/中文典籍` 对应的逻辑链路条目），排除 `记纂渊海`（已归档/不在当前发布范围）。
- **覆盖口径**：在给定 `version_id` + `corpus_release_id` 下，精校队列 MUST 覆盖该范围内 `normalized_entries.jsonl` 的全部条目（100%）。
- **可审计性**：QA 队列与报告 MUST 记录 scope（包含/排除清单）、覆盖率证据（按书计数 + digest）以及关键标识符（`version_id`, `corpus_release_id`）。
- **门禁**：覆盖缺失 MUST 视为资产门禁失败并阻断（与“是否人工复核完成”解耦）。

### Out of scope（后续变更）
- 将同样的“全量精校覆盖”扩展到西方典籍（`典籍/texts`）并纳入默认 Gate 流程。

## Planned artifacts
- 新增/升级策略文件：`data/proofreading_qa/qa_policy.v2.zh_full.yaml`
- 升级 QA workflow 工具链以支持“全量覆盖 + scope 过滤 + 覆盖证据”：`scripts/proofreading_qa/run_workflow.py`
- 调整资产门禁产物生成，使中文典籍进入 QA 输入集合：`scripts/gates/asset_gate_corpus.sh` 与 `scripts/text_normalization_alignment/run_pipeline.py`
- 更新 Gate-2 入口引用新的 policy：`scripts/gates/gate2_proofreading_and_corpus_release.sh`
- 更新 `openspec/specs/proofreading-workflow-qa/*` 的验收口径（acceptance）以覆盖新模式

## Acceptance
- `openspec validate enforce-full-proofreading-cn-v1 --strict --no-interactive`
- `openspec validate --specs --strict --no-interactive`
- `bash scripts/gates/asset_gate_corpus.sh --skip-openspec` 产出中文典籍的 `normalized_entries.jsonl`
- `PYTHONPATH=. .venv/bin/python scripts/proofreading_qa/run_workflow.py run --policy data/proofreading_qa/qa_policy.v2.zh_full.yaml --output-dir artifacts/proofreading_qa`

## Risks
- **性能与体量**：全量队列会显著增加任务数与工件大小；缓解：保持确定性生成、按书聚合指标、避免泄露敏感原文。
- **人工复核现实约束**：CI 无法执行真实人工精校；缓解：把“覆盖缺失阻断”与“人工复核完成阻断”拆开口径，先保证 100% 覆盖可生成与可审计。

## Rollback
- 回滚 Gate-2 的 policy 引用到 `qa_policy.v1.yaml`，恢复抽样模式。
- 保留全量策略与工具链作为 shadow 工具，不阻断现有发布流程。

