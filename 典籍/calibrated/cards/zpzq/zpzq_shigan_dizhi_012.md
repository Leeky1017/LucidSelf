## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_012`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 又细分之，生气之散布者，甲之甲，而生气之凝成者，甲之乙；万木之所以有枝叶者，乙之甲，而万木之枝枝叶叶者，乙之乙也。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 生气（生发之气） | common_vital_qi | new_candidate | 能量 | common | 气象维度 |
| 细分（散布/凝成） | common_differentiation | new_candidate | 关系 | common | 演化机制 |
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_qi_dispersion_condensation` | 若对「生气（生发之气）」作“散布/凝成”的更细分判 | 则可用“散布→发用、凝成→成质”的两态口径解释木之生长与成形差异 | 运势 | 中性 | 中 | 生气之散布者，甲之甲，而生气之凝成者，甲之乙 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_012` | common_vital_qi AND common_differentiation | 散则为发，凝则为成：气有两态。 | 条件分支 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 生气之散布/凝成 | wood_presence, wood_strength |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 凝成 | Condensation into Form | 生气由散而凝，聚而成质，转入可承载之形。 | A process of concentrating diffuse vitality into a stable, form-bearing state; used here as a structural metaphor for manifestation. | common_differentiation | new_candidate |
