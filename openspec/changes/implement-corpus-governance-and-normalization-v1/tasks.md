# Tasks — Implement Corpus Governance + Text Normalization/Alignment (v1)

> 目标：把 `corpus-governance` 与 `text-normalization-alignment` 从“验文档”升级为“验工程产物”，并提供资产门禁可执行入口；所有任务必须先落盘 Evidence 再勾选。

## 1) Change bootstrap
- [x] 创建 change 目录与 delta specs，并通过 `openspec validate implement-corpus-governance-and-normalization-v1 --strict --no-interactive`（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t01__openspec_validate_change.txt）

## 2) Corpus governance manifest
- [x] 新增 `data/governance/corpus_manifest.v1.yaml`（最小：清单/许可/来源/血缘/版本字段）并提供生成脚本（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t02__manifest_files_added.txt）
- [x] 实现 manifest 校验脚本（字段/引用/路径可解析，失败可阻断）（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t03__manifest_validation.txt）

## 3) Text normalization + alignment
- [x] 实现归一化产物生成（统一字段、输出目录、可重复）并落盘（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t04__normalization_artifacts.txt）
- [x] 产出对齐报告（JSON+MD），至少可定位到书/段落/条目（book_id/node_id/snippet_ids）（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t05__alignment_report.txt）

## 4) Acceptance upgrade + gate wiring
- [x] 升级两份 spec 的 `acceptance.md`：加入实际脚本命令、报告路径、阈值口径与阻断策略（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t06__acceptance_updated.txt）
- [x] 提供资产门禁入口 `scripts/gates/asset_gate_corpus.sh`（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t07__asset_gate_script.txt）
- [x] 接入 CI gate（workflow）并明确 artifact 上传路径（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t08__ci_workflow.txt）
- [x] 更新 `openspec/SPECS_INDEX.md`：两条 spec 状态推进（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t09__specs_index_updated.txt）

## 5) Final verification + evidence
- [x] 运行并落盘：资产门禁脚本 + `openspec validate --specs --strict --no-interactive`（evidence: openspec/changes/implement-corpus-governance-and-normalization-v1/evidence/t10__final_validation.txt）
