## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_016`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19`
- `source_text`:
  > `以寅卯而阴阳，则寅为阳，卯为阴，木之存乎地而为阴阳者也。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 地支（寅/卯取值） | month_branch | existing | 结构 | bazi | 地支 |
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |
| 天地框架（地之层面） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_branches_polarity_on_earth` | 若在“地”的层面用「地支（寅/卯取值）」分判阴阳 | 则可取“寅为阳、卯为阴”的解释口径，表木之存乎地的两面 | 运势 | 中性 | 高 | `寅为阳，卯为阴` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_016` | month_branch AND common_heaven_earth_frame | 寅阳卯阴，地上木形亦分阴阳。 | 条件分支 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 寅为阳、卯为阴（地层木之阴阳） | month_branch, wood_presence |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 地支 | Earthly Branch | 十二支之总称，用以表“地”的承载与成形层面，并可分判阴阳。 | One of the two pillars of the stems-and-branches framework; used to encode grounded, form-taking qualities on the “earthly” layer. | month_branch | existing |

