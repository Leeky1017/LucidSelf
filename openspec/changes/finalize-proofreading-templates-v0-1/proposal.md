# Proposal: Finalize Proofreading Templates V0.1

## Why

- `典籍/精校模板_L1L2.md` 与 `典籍/texts/Western_Texts_Template.md` 当前存在口径差异，并混用 `vX.Y` 版本标记，影响上线前的唯一终版定义与引用一致性。
- `典籍/Schema工程说明.md`、`典籍/典籍结构化作业手册.md` 等文档存在对模板版本与路径的历史引用，容易造成执行偏差。

## What Changes

- **MODIFIED**：统一两份精校模板的口径（字段名、结构、约束说明），并将版本标识统一为 `V0.1`（上线前终版）。
- **MODIFIED**：移除模板及其引用处所有 `vX.Y` 字样，仅保留 `V0.1` 作为版本标识。
- **MODIFIED**：同步修正文档中对模板的引用（路径与版本标识一致）。

## Impact

- Affected assets:
  - `典籍/精校模板_L1L2.md`
  - `典籍/texts/Western_Texts_Template.md`
  - `典籍/Schema工程说明.md`
  - `典籍/典籍结构化作业手册.md`
- Breaking change: NO（文档与模板口径统一；不引入运行时代码/数据结构变更）
- Risks: 误改历史说明导致信息缺失；模板口径不一致导致执行歧义
- Rollback: 回滚以上文件到变更前版本

## Acceptance

- `openspec validate finalize-proofreading-templates-v0-1 --strict --no-interactive`

