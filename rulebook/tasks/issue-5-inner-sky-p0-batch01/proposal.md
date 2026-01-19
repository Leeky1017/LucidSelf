# Proposal: issue-5-inner-sky-p0-batch01

## Why
需要为占星主干典籍《The Inner Sky》（book_abbr=inner_sky）沉淀可被引擎直接消费的“精校卡（扁平产出）”资产，优先覆盖 P0 主干语义（Prime Symbol + Signs）。

## What Changes
- 新增 20 张英文精校卡（priority=P0），范围：从标题行 `## The Prime Symbol` 开始，至 `## Planets` 之前结束
- 落盘位置严格限定为：`典籍/calibrated/cards/inner_sky/`
- 因子抽取对齐既有本体 `典籍/因子本体/**`；无法对齐的概念以 `new_candidate` 形式给出建议 `factor_id`（不回写本体）
- 跨体系映射仅使用 `典籍/因子本体/cross_system/neutral_tags.yaml` 中既有 `neutral_*` 标签

## Impact
- Affected specs: NONE
- Affected code: NONE
- Breaking change: NO
- User benefit: 为后续占星解释/叙事生成/跨体系对齐提供可追溯的语义资产（A–F 全量可验收）

