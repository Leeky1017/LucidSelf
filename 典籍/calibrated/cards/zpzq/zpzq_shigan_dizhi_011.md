## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_011`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 在天为生气，而流行于万物者，甲也；在地为万物，而承兹生气者，乙也。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天地框架（天/地分位） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |
| 生气（生发之气） | common_vital_qi | new_candidate | 能量 | common | 气象维度 |
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_heaven_qi_earth_form` | 若在「天地框架（天/地分位）」中区分“生气流行”与“万物承载” | 则可用甲偏指天上生气之流行，乙偏指地上万物之承受与成形 | 运势 | 中性 | 中 | 在天为生气，而流行于万物者，甲也 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_011` | common_heaven_earth_frame AND common_vital_qi | 天为生气之路，地为万物之器。 | 主干依赖 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 天为生气，地承其气 | year_stem, year_branch |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 生气 | Generative Qi | 在天流行、生发并推动万物生长的气。 | A generative, animating force that circulates and enables growth; used here as a functional description rather than a medical term. | common_vital_qi | new_candidate |
