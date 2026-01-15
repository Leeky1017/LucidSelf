# Spec Amendment Tasks — openspec validate command (non-interactive)

> 目标：修订门禁/验收命令口径，使其在非交互环境可执行且可审计；所有任务必须落盘 Evidence 后才可勾选。

## 文档口径修订

- [x] 修订 `openspec/QUALITY_GATES.md`：将 `openspec validate --strict` 替换为 `openspec validate --specs --strict --no-interactive`（并保留 Gate-1/2 的 list 命令） (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t01__quality_gates_updated.txt)
- [x] 修订 `openspec/SPECS_INDEX.md`：统一门禁命令口径为 `openspec validate --specs --strict --no-interactive` (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t02__specs_index_updated.txt)
- [x] 批量修订 26 个 spec 的 `acceptance.md`：将验收命令替换为 `openspec validate --specs --strict --no-interactive` (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t03__acceptance_updated_all.txt)
- [x] 批量修订 26 个 spec 的 `tasks.md`：对齐“校验通过”类任务描述为 `openspec validate --specs --strict --no-interactive`（不改变任务编号与 Evidence 指针策略） (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t04__tasks_updated_all.txt)

## 验证与落盘

- [x] 重新执行并落盘：`openspec validate --specs --strict --no-interactive` + `openspec list --specs` + `openspec list --changes` (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t05__post_amendment_validation.txt)
- [x] 用新口径重跑并落盘 `dashboard_after_citations-evidence-protocol.txt` (evidence: openspec/changes/spec-amendment-2025-12-24-openspec-validate-command/evidence/t06__dashboard_after_citations_rerun.txt)
