## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_002`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > 惟有动静，遂分阴阳。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 动静（变化/静定） | common_movement_stillness | new_candidate | 状态 | common | 基底动力 |
| 阴阳（两极分化） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |
| 分化（由一而二） | common_differentiation | new_candidate | 关系 | common | 演化机制 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_motion_stillness_yinyang` | 若出现「动静（变化/静定）」的对立与互用 | 则「阴阳（两极分化）」作为解释框架被引入 | 运势 | 中性 | 高 | 惟有动静，遂分阴阳 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_002` | common_movement_stillness AND common_yin_yang | 动静一开，阴阳自现。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 动静分阴阳 | conflict_intensity, harmony_score |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 阴阳 | Yin-Yang Polarity | 由动静分判而成的两极与互根结构。 | A paired polarity model describing complementary forces that differentiate from a shared source and remain interdependent. | common_yin_yang | new_candidate |
