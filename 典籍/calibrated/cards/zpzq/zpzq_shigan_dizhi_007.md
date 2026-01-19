## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_007`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17`
- `source_text`:
  > 有是五行，何以又有十干十二支乎？
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 十干（以年干示例） | year_stem | existing | 结构 | bazi | 天干 |
| 十二支（以年支示例） | year_branch | existing | 结构 | bazi | 地支 |
| 月令（以月支示例） | month_branch | existing | 结构 | bazi | 月令 |
| 干支体系（抽象结构） | common_stem_branch_system | new_candidate | 结构 | common | 干支系统 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_need_stem_branch_system` | 若以「五行」作为分类基础仍不足以表达运行细节 | 则引入「干支体系（抽象结构）」以承载更细的时间/位置信息 | 运势 | 中性 | 中 | 何以又有十干十二支乎 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_007` | common_five_elements AND common_stem_branch_system | 五行要落地，干支才成坐标。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:17` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 十干十二支（干支体系） | year_stem, year_branch, month_branch |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 十干十二支 | Heavenly Stems & Earthly Branches | 十天干与十二地支组成的符号系统，用于表达时间与气的运行秩序。 | A cyclic symbolic framework used to encode time, phase dynamics, and positional relations in Chinese metaphysical systems. | common_stem_branch_system | new_candidate |
