# Tasks: Finalize Proofreading Templates V0.1

> 目标：将两份精校模板统一为 `V0.1`（上线前终版），并修复引用一致性；所有任务完成后必须通过 OpenSpec 严格校验并落盘证据。

## 1. Template Unification
- [ ] 1.1 更新 `典籍/精校模板_L1L2.md`：统一版本标识为 `V0.1`，移除 `vX.Y` 字样并对齐结构口径
- [ ] 1.2 更新 `典籍/texts/Western_Texts_Template.md`：统一版本标识为 `V0.1`，移除 `vX.Y` 字样并对齐结构口径

## 2. Reference Consistency
- [ ] 2.1 更新 `典籍/Schema工程说明.md`：模板引用路径与版本标识统一为 `V0.1`
- [ ] 2.2 更新 `典籍/典籍结构化作业手册.md`：模板引用路径与版本标识统一为 `V0.1`

## 3. Validation Evidence
- [ ] 3.1 运行并落盘：`openspec validate finalize-proofreading-templates-v0-1 --strict --no-interactive`（evidence: `openspec/changes/finalize-proofreading-templates-v0-1/evidence/openspec_validate.txt`）

