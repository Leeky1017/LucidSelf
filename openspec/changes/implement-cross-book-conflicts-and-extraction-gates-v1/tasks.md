# Tasks — Implement Cross-Book Conflicts + Semantic Extraction Quality Gates (v1)

> 目标：冲突与质量门禁可跑、可审计、可阻断；所有任务必须先落盘 Evidence 再勾选。

## 1) Change bootstrap
- [x] 创建 change 目录与 delta specs，并通过 `openspec validate implement-cross-book-conflicts-and-extraction-gates-v1 --strict --no-interactive`（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t01__openspec_validate_change.txt）

## 2) Cross-book conflicts (report + block)
- [x] 定义冲突门禁策略（阈值/例外格式/输出路径）（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t02__conflict_policy.txt）
- [x] 实现冲突检测报告生成（JSON+MD），并支持例外/白名单应用（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t03__conflict_report.txt）
- [x] 实现“可阻断化”：阈值越界退出码非 0，输出可行动证据（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t04__conflict_blocking.txt）

## 3) Semantic extraction quality gates (rules + block)
- [x] 定义质量门禁规则版本（最低阻断集合 + 阈值）（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t05__quality_rules.txt）
- [x] 实现质量校验报告生成（JSON），并支持例外/白名单（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t06__quality_report.txt）
- [x] 实现“失败必须阻断”的最低集合（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t07__quality_blocking.txt）

## 4) Acceptance + wiring
- [x] 升级两份 spec 的 `acceptance.md`：加入实际脚本命令、报告路径、阈值口径与阻断策略（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t08__acceptance_updated.txt）
- [x] 提供门禁入口脚本并接入 CI workflow（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t09__ci_wiring.txt）
- [x] 更新 `openspec/SPECS_INDEX.md` 对应两行状态（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t10__specs_index_updated.txt）

## 5) Final verification + evidence
- [x] 运行并落盘：门禁脚本 + `openspec validate --specs --strict --no-interactive`（evidence: openspec/changes/implement-cross-book-conflicts-and-extraction-gates-v1/evidence/t11__final_validation.txt）
