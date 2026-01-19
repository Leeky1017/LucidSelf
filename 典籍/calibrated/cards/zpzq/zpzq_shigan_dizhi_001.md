## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_001`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > 天地之间，一气而已。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天地框架（上/下两极） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |
| 气（运行之力） | common_qi | new_candidate | 能量 | common | 基底能量 |
| 一气（同源统一） | common_qi_unity | new_candidate | 状态 | common | 基底假设 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_qi_unity_root` | 若采用「一气（同源统一）」解释万物根源 | 则阴阳/五行/干支可被视为同一气的分化表达 | 运势 | 中性 | 中 | 天地之间，一气而已 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_001` | common_qi_unity | 万象同源，一气贯通天地。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 一气（同源统一） | harmony_score |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 一气 | Unified Qi (Primordial Vital Force) | 天地万物同出于一，根源为气。 | A single underlying vital force used as a baseline to explain how all phenomena arise through differentiation. | common_qi_unity | new_candidate |
