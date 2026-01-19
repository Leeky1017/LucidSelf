## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_017`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19`
- `source_text`:
  > `以甲乙寅卯而统分阴阳，则甲乙为阳寅卯为阴，木之在天成象而在地成形者也。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 地支（寅/卯取值） | month_branch | existing | 结构 | bazi | 地支 |
| 天地框架（天象/地形） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_stems_yang_branches_yin` | 若把甲乙与寅卯合并为一套统分体系 | 则可取“甲乙为阳、寅卯为阴”，并用“天成象/地成形”表其分工 | 运势 | 中性 | 中 | `甲乙为阳寅卯为阴` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_017` | year_stem AND month_branch AND common_heaven_earth_frame | 天成象，地成形：干支分掌阴阳。 | 总结 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 天成象/地成形（干支分工） | year_stem, month_branch |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 成象／成形 | Image vs. Form (Xiang/Xing) | 天成象，地成形：在天为可感知之象，在地为可承载之形。 | A conceptual split between “image” (abstract pattern, sign) and “form” (embodied structure), used to explain how qualities manifest across layers. | common_heaven_earth_frame | new_candidate |

