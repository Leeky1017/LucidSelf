# Proposal — Add ZPZQ Calibration Cards (P0 Batch 01)

## Why

为《子平真诠》（`zpzq`）建立可审计、可追溯、可复用的 P0 精校卡资产：把“十干十二支”章节的关键语义单元直接沉淀为因子/规则草案/叙事素材/跨体系映射/术语对齐，供后续引擎消费与跨书互证。

## Scope

### In scope
- 仅覆盖 `典籍/中文典籍/子平真诠/原文/子平真诠原文.md` 的章节 `一．论十干十二支`（到 `二、论阴阳生克` 之前）。
- 产出 20 张精校卡：`典籍/calibrated/cards/zpzq/zpzq_shigan_dizhi_001.md` ~ `020.md`。
- 每张卡 MUST 按 `典籍/CALIBRATION_TEMPLATE_CN.md`（扁平产出）填充 A–F 全段并包含最小表行数。
- 因子对齐：优先对齐 `典籍/因子本体/**`；对齐失败以 `new_candidate` 给出候选 ID（不改本体文件）。

### Out of scope
- 不回写原文文件与典籍目录结构（仅新增精校卡资产）。
- 不新增/修改因子本体 YAML、不新增任何生成脚本。

## Planned artifacts
- 精校卡：`典籍/calibrated/cards/zpzq/zpzq_shigan_dizhi_001.md` ~ `020.md`
- 运行记录：`openspec/_ops/task_runs/ISSUE-3.md`

## Acceptance (minimum)
- `openspec validate add-zpzq-calibration-cards-p0-b01 --strict --no-interactive`
- `openspec validate --specs --strict --no-interactive`
- 对 20 张卡：
  - A 段 `source_anchor` 必须可定位到 `路径:行号`
  - A 段 `source_text` 必须逐字引用（不改字）
  - B 段因子表至少 3 行；对齐失败则 `new_candidate` 并提供候选 ID
  - C/D/E/F 段表格均至少 1 行

## Risks
- 段落行内包含多句，锚点同一行号可能覆盖多张卡；缓解：`source_text` 使用逐字短引，配合行号即可精确定位。
- 现有因子本体对“阴阳/四象”等基础概念覆盖不足；缓解：以 `new_candidate` 提供候选 ID，不在本变更内改本体。

## Rollback
- 本变更仅新增内容资产；回滚时删除本次新增的 20 张卡文件即可。

