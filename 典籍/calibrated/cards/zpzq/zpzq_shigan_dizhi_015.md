## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_015`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19`
- `source_text`:
  > `以甲乙而分阴阳，则甲为阳，乙为阴，木之行于天而为阴阳者也。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |
| 天地框架（天之层面） | common_heaven_earth_frame | new_candidate | 结构 | common | 宇宙框架 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_stems_polarity_in_heaven` | 若以「天干（甲/乙取值）」在天的层面分判阴阳 | 则甲可取“阳”、乙可取“阴”的解释口径，用以描述木之行于天的两面 | 运势 | 中性 | 高 | `甲为阳，乙为阴` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_015` | year_stem AND common_heaven_earth_frame | 甲阳乙阴，天上木气分两途。 | 条件分支 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 甲为阳、乙为阴（天层木之阴阳） | year_stem, wood_presence |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 天干 | Heavenly Stem | 十干之总称，用以表气之运行与分判阴阳。 | One of the two pillars of the stems-and-branches framework; used to encode dynamic qualities and polarity on the “heavenly” layer of the model. | year_stem | existing |

