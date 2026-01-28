# Proposal: issue-3-zpzq-shigan-dizhi-p0-b01

## Why
为《子平真诠》建立可追溯的 P0「精校卡」资产：把“十干十二支”这一基础章节直接沉淀为可复用因子/规则草案/叙事素材/跨体系映射/术语对齐，便于后续引擎消费与跨书互证。

## What Changes
- 新增 20 张 P0 精校卡（扁平产出），落盘到 `典籍/calibrated/cards/zpzq/`（`zpzq_shigan_dizhi_001`–`020`）。
- 每张卡均引用原文行号锚点与逐字 `source_text`，并对齐现有因子本体；无法对齐的以 `new_candidate` 提供候选 ID（不改本体文件）。
- 补充本 Issue 的运行记录与 Rulebook 任务清单，保证可审计与可复现。

## Impact
- Affected specs: 无（遵循 `典籍/CALIBRATION_TEMPLATE_CN.md` 与 `典籍/CALIBRATION_STRATEGY.md`）
- Affected code: 无
- Breaking change: NO
- User benefit: 提供可直接复用的结构化资产（因子/规则/叙事/映射/术语），并具备逐条可追溯的证据链
