## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_010`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > `甲者，乙之气；乙者，甲之质。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 气（运行/生发） | common_qi | new_candidate | 能量 | common | 气象维度 |
| 质（形质/承载） | common_substance_form | new_candidate | 结构 | common | 形质维度 |
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_jia_qi_yi_form` | 若在同一类（木）内区分「气（运行/生发）」与「质（形质/承载）」 | 则可把甲偏向“气”，乙偏向“质”作为解释口径 | 运势 | 中性 | 中 | `甲者，乙之气；乙者，甲之质` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_010` | common_qi AND common_substance_form AND year_stem | 甲主生气流行，乙主形质承载。 | 主干依赖 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 气与质（同类内部分工） | wood_presence, wood_strength |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 质 | Substrate/Form (Zhi) | 相对于“气”的形质与承载面，着于成形与稳固。 | The more tangible, form-bearing aspect contrasted with qi—how a quality becomes embodied, sustained, and stabilized. | common_substance_form | new_candidate |

