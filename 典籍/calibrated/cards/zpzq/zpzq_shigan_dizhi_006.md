## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_006`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > `水者，太阴也；火者，太阳也；木者，少阳也；金者，少阴也；土者，阴阳老少、木火金水冲气所结也。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 水行（太阴相） | water_presence | existing | 能量 | bazi | 五行 |
| 火行（太阳相） | fire_presence | existing | 能量 | bazi | 五行 |
| 木行（少阳相） | wood_presence | existing | 能量 | bazi | 五行 |
| 金行（少阴相） | metal_presence | existing | 能量 | bazi | 五行 |
| 土行（冲气所结） | earth_presence | existing | 能量 | bazi | 五行 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_wuxing_as_yinyang_phases` | 若把五行理解为阴阳相位在不同类中的呈现（引用「水行（太阴相）」「火行（太阳相）」等） | 则可用“太阴/太阳/少阴/少阳”的相位语言来解释五行偏性与组合倾向 | 运势 | 中性 | 中 | `水者，太阴也` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_006` | water_presence AND fire_presence | 水火分阴阳，五行各带相位之偏。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 五行与四象相位对照 | water_presence, fire_presence, wood_presence, metal_presence, earth_presence |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 土 | Earth Phase (Tu) | 由阴阳老少与木火金水冲气所结，承载与调和诸气。 | The “Earth phase” as an integrative category that stabilizes and mediates other phase dynamics, rather than a literal material element. | earth_presence | existing |

