## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_004`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > `老者极动静之时，是为太阳太阴；少者初动初静之际，是为少阴少阳。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 四象（相位体系） | common_four_images | new_candidate | 结构 | common | 阴阳相位 |
| 太阳太阴（极动/极静） | common_taiyang_taiyin | new_candidate | 结构 | common | 极相位 |
| 少阴少阳（初静/初动） | common_shaoyin_shaoyang | new_candidate | 结构 | common | 初相位 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_four_images_extremes_beginnings` | 若以「动静」在程度上分为极与初 | 则四象可分别指向极端（太阳/太阴）与起始（少阳/少阴）两组相位 | 运势 | 中性 | 中 | `老者极动静之时，是为太阳太阴` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_004` | common_four_images | 极处成太阴太阳，初处成少阴少阳。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 太阴/太阳（极静/极动） | coldness_index, warmth_index |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 太阳太阴 | Taiyang/Taiyin (Greater Yang/Greater Yin) | 动静达到极端时的两种相位：极动为太阳，极静为太阴。 | The “greater” poles of a yin-yang phase model, used to describe peak motion (taiyang) and peak stillness (taiyin). | common_taiyang_taiyin | new_candidate |

