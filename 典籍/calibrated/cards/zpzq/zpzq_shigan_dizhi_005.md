## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_005`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15`
- `source_text`:
  > `有是四象，而五行具于其中矣。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 四象（相位体系） | common_four_images | new_candidate | 结构 | common | 阴阳相位 |
| 五行（相位内之分化） | common_five_elements | new_candidate | 结构 | common | 基本相类 |
| 具于其中（内含关系） | common_containment | new_candidate | 关系 | common | 结构关系 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_four_images_contain_five_elements` | 若采用「四象（相位体系）」作为上层框架 | 则「五行（相位内之分化）」可被视为其内含的进一步分解 | 运势 | 中性 | 中 | `有是四象，而五行具于其中矣` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_005` | common_four_images AND common_five_elements | 四象为骨，五行在其中运转。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:15` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 四象内含五行 | wood_presence, fire_presence, earth_presence, metal_presence, water_presence |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 五行 | Five Phases (Wuxing) | 水、火、木、金、土五类基本相，作为万物变化的分类体系。 | A five-phase classification used to describe patterned change (not “elements” as substances), widely applied in Chinese metaphysical reasoning. | common_five_elements | new_candidate |

