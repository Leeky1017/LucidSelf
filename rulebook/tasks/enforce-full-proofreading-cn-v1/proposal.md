# Proposal: enforce-full-proofreading-cn-v1

## Why
当前 `proofreading-workflow-qa` 默认按书抽样（`per_book`），无法满足“中文典籍必须全部精校”的资产门禁目标；需要将 QA 队列升级为全量覆盖（100%）。

## What Changes
- 新增中文典籍全量精校 policy：`data/proofreading_qa/qa_policy.v2.zh_full.yaml`
- 升级 QA workflow：支持 scope(include/exclude) + full coverage 证据（counts + digest）
- 调整资产门禁调用：`scripts/gates/asset_gate_corpus.sh` 生成中文典籍全量 `normalized_entries.jsonl`
- Gate-2 改为使用新 policy：`scripts/gates/gate2_proofreading_and_corpus_release.sh`
- OpenSpec change：`openspec/changes/enforce-full-proofreading-cn-v1/`

## Impact
- Affected specs: `openspec/specs/proofreading-workflow-qa/*`
- Affected code: `scripts/proofreading_qa/run_workflow.py`, `scripts/text_normalization_alignment/run_pipeline.py`, `scripts/gates/*`
- Breaking change: NO (新增 policy，原 v1 policy 仍保留；但默认 Gate-2 policy 已切换)
- User benefit: 中文典籍精校队列可审计地全量覆盖，覆盖缺失可直接阻断资产门禁晋级/发布
