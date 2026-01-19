## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_014`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19`
- `source_text`:
  > `何以复有寅卯者，又与甲乙分阴阳天地而言之者也。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 地支（寅/卯取值） | month_branch | existing | 结构 | bazi | 地支 |
| 天地框架（天/地分位） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_branch_added_for_earth_layer` | 若需把木之阴阳同时放到「天地框架（天/地分位）」中表达 | 则除甲乙外，还需用寅卯在“地”的层面承接与呈现阴阳 | 运势 | 中性 | 中 | `何以复有寅卯者` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_014` | common_heaven_earth_frame AND year_stem AND month_branch | 天以干显气，地以支成形。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 甲乙与寅卯（天干/地支分层） | year_stem, month_branch |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 寅卯 | Yin/Mao (Wood Branches) | 地支中属木的两支，用以在地的层面分判阴阳与承接天干之气。 | The two Wood-related earthly branches used to encode how Wood-phase qualities take shape and are “received” on the earthly layer of the model. | month_branch | existing |

