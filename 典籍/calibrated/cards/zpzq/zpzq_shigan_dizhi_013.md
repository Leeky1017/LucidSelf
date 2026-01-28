## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_013`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 方其为甲，而乙之气已备；及其为乙，而甲之质乃坚。有是甲乙，而木之阴阳具矣。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 气（运行/生发） | common_qi | new_candidate | 能量 | common | 气象维度 |
| 质（形质/承载） | common_substance_form | new_candidate | 结构 | common | 形质维度 |
| 阴阳互根（相含） | common_yin_yang | new_candidate | 关系 | common | 两极互根 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_polarity_mutual_containment` | 若认为甲乙分别偏于「气」与「质」但彼此相含（引用「阴阳互根（相含）」） | 则木之阴阳不作截然二分，而以“互根互用”作为解释口径 | 运势 | 中性 | 中 | 有是甲乙，而木之阴阳具矣 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_013` | common_yin_yang AND year_stem | 甲中有乙气，乙中有甲质，阴阳互根。 | 总结 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 阴阳互根（相含） | harmony_score |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 互根 | Mutual Rooting | 阴阳两面彼此具备其端，互为根源而不相离。 | A principle that opposite aspects co-arise and contain each other’s seeds, functioning as a stable explanatory rule rather than a literal biology claim. | common_yin_yang | new_candidate |
