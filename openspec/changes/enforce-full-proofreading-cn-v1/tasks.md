# Tasks — Enforce Full Proofreading Coverage (CN First) (v1)

> 目标：中文典籍（不含记纂渊海）在 QA 阶段实现 100% 覆盖的精校队列与可审计门禁；所有任务必须先落盘 Evidence 再勾选。

## 1) Change bootstrap
- [x] 1.1 创建 change 目录与 delta specs，并通过 `openspec validate enforce-full-proofreading-cn-v1 --strict --no-interactive`（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t01__openspec_validate_change.txt`）

## 2) Spec delta（proofreading-workflow-qa）
- [x] 2.1 为“全量精校覆盖（中文典籍）”补齐 delta Requirements + Scenarios（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t02__delta_spec_written.txt`）
- [x] 2.2 更新 `openspec/specs/proofreading-workflow-qa/acceptance.md`：加入全量覆盖验收命令与通过标准（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t03__acceptance_updated.txt`）

## 3) Implementation（CN 全量覆盖）
- [x] 3.1 升级 `scripts/text_normalization_alignment/run_pipeline.py` 支持“max_nodes_per_book=0 表示全量”，并在 Gate 调用侧落地中文典籍范围（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t04__asset_gate_corpus_run.txt`）
- [x] 3.2 升级 `scripts/proofreading_qa/run_workflow.py` 支持：scope（include/exclude）、full coverage、覆盖证据（counts + digest）（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t05__proofreading_qa_run.txt`）
- [x] 3.3 新增策略文件 `data/proofreading_qa/qa_policy.v2.zh_full.yaml` 并在 Gate-2 引用（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t06__gate2_run.txt`）

## 4) Final verification + evidence
- [x] 4.1 运行并落盘：`openspec validate --specs --strict --no-interactive`（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t07__openspec_validate_specs_strict.txt`）
- [ ] 4.2 运行并落盘：`pytest -q`（若仓库已有测试）（evidence: `openspec/changes/enforce-full-proofreading-cn-v1/evidence/t08__pytest.txt`；当前 pytest collection 存在既有 ImportError，未在本次范围内修复）
