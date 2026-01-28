## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_009`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 即以木论，甲乙者，木之阴阳也。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 木行（木气/木类） | wood_presence | existing | 能量 | bazi | 五行 |
| 阴阳（两极框架） | common_yin_yang | new_candidate | 结构 | common | 基底两极 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_wood_stems_encode_polarity` | 若讨论「木行（木气/木类）」的阴阳分判 | 则可用「天干（甲/乙取值）」来编码其阴阳两面 | 运势 | 中性 | 高 | 甲乙者，木之阴阳也 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_009` | wood_presence AND year_stem | 木分甲乙，阴阳各司其位。 | 条件分支 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 甲乙（木之阴阳） | year_stem, wood_presence |  |  |  |  | neutral_emotional_harmony |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 甲乙 | Jia/Yi (Wood Stems) | 天干中属木的两干，用以分木之阴阳。 | The two Wood-related heavenly stems used to encode polarity within the Wood phase in traditional Chinese systems. | year_stem | existing |
