# Tasks — Implement Proofreading Workflow QA + Corpus Release Pipeline (v1)

> 目标：QA workflow 与发布流水线可跑、可审计、可复现、可回滚；所有任务必须先落盘 Evidence 再勾选。

## 1) Change bootstrap
- [x] 创建 change 目录与 delta specs，并通过 `openspec validate implement-proofreading-and-corpus-release-v1 --strict --no-interactive`（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t01__openspec_validate_change.txt）

## 2) Proofreading workflow QA (workflow + report)
- [x] 定义 QA workflow 策略（抽样/状态/阈值/例外）（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t02__qa_policy.txt）
- [x] 实现 QA workflow 工具链（队列/状态/复核/例外）并产出 QA 报告（JSON+MD）（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t03__qa_report.txt）

## 3) Corpus release pipeline (publish + validate + rollback)
- [x] 定义发布包工件结构（manifest + hashes + reports）与回滚策略（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t04__release_design.txt）
- [x] 实现发布/校验/回滚脚本（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t05__release_pipeline_run.txt）

## 4) Acceptance + wiring
- [x] 升级两份 spec 的 `acceptance.md`：加入一键发布/校验/回滚命令与通过标准（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t06__acceptance_updated.txt）
- [x] 提供 Gate-2 入口脚本并接入 CI workflow（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t07__ci_wiring.txt）
- [x] 更新 `openspec/SPECS_INDEX.md` 对应两行状态（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t08__specs_index_updated.txt）

## 5) Final verification + evidence
- [x] 运行并落盘：Gate-2 脚本 + `openspec validate --specs --strict --no-interactive`（evidence: openspec/changes/implement-proofreading-and-corpus-release-v1/evidence/t09__final_validation.txt）
