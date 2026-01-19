## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_003`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > `有老少，遂分四象。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 老少（极/初之分） | common_old_young | new_candidate | 状态 | common | 阴阳细分轴 |
| 四象（太阴太阳少阴少阳） | common_four_images | new_candidate | 结构 | common | 阴阳相位 |
| 分化（由二而四） | common_differentiation | new_candidate | 关系 | common | 演化机制 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_old_young_four_images` | 若在阴阳之内进一步区分「老少（极/初之分）」 | 则形成「四象（太阴太阳少阴少阳）」的更细框架 | 运势 | 中性 | 高 | `有老少，遂分四象` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_003` | common_four_images AND common_old_young | 阴阳再细，四象定势。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 四象（阴阳分相） | birth_season, solar_term |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 四象 | Four Images (Yin-Yang Phases) | 阴阳因老少而细分成四个相位：太阴、太阳、少阴、少阳。 | A four-phase refinement of yin-yang describing extremes and beginnings of motion/stillness in a cyclical model. | common_four_images | new_candidate |

