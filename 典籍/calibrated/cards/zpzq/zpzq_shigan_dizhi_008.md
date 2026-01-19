## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_008`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 盖有阴阳，因生五行，而五行之中，各有阴阳。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |
| 五行（分类体系） | common_five_elements | new_candidate | 结构 | common | 基本相类 |
| 因生/各有（递归分化） | common_differentiation | new_candidate | 关系 | common | 演化机制 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_yinyang_generate_wuxing_recursive` | 若以「阴阳（两极框架）」解释世界运行 | 则「五行（分类体系）」由阴阳分化而生，且每一行内部仍可再分阴阳 | 运势 | 中性 | 高 | 盖有阴阳，因生五行 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_008` | common_yin_yang AND common_five_elements | 阴阳生五行，五行复含阴阳。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 五行之中各有阴阳 | wood_presence, fire_presence, earth_presence, metal_presence, water_presence |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 五行阴阳 | Yin-Yang Within Each Phase | 五行虽分五类，而每一类之中仍可再判阴阳。 | A recursive polarity principle: each phase/category can be further analyzed into yin and yang aspects rather than treated as uniform. | common_yin_yang | new_candidate |
