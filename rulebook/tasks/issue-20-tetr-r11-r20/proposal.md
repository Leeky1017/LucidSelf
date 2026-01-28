# Proposal: issue-20-tetr-r11-r20

## Why
执行 `典籍精校_轮次任务清单.md` 批次 2 对话框 C（英文｜Tetrabiblos｜`tetr`）的 R11-R20 轮次校准工作。《Tetrabiblos》是古典占星学的奠基文本之一，适合沉淀“占星学目的/行星性质/星座气质/相位与尊贵/地理气候/本命推断方法/关键点位/财富与荣誉”等可中性化语义节点，为 LucidSelf 的因子/规则草案、跨体系标签对齐与证据链可追溯提供稳定语料。

## What Changes
- 创建输出目录 `典籍/calibrated/cards/tetr/`
- 产出 10 张 Deep 深度校准卡（R11-R20），覆盖：
  - Book I：占星学目的与范围；行星性质（吉凶/质性）；星座性质（气质/temperaments）；相位/尊贵/terms
  - Book II：地理/气候与条件
  - Book III：本命推断方法总览；角宫/上升点等关键点位
  - Book IV：财富；品秩/荣誉；其他领域（婚姻/子女/疾病等选核心单元）
- 每张卡按 `典籍/CALIBRATION_TEMPLATE_EN_V3.md` 的 Deep 口径完成（字段齐全、包含可追溯 `source_range` 与不确定性标注/修订历史）

## Impact
- Affected specs: 无规格变更（纯数据资产产出）
- Affected code: 无代码变更
- Breaking change: NO
- User benefit: 为推理引擎提供古典占星学核心语义底座与术语对齐基线，支撑后续占星→叙事→行动建议链路的可解释与可复现

