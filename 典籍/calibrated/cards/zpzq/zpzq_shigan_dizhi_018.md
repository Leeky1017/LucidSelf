## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_018`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19`
- `source_text`:
  > 甲乙行乎天，而寅卯受之；寅卯存乎也，而甲乙施焉。是故甲乙如官长，寅卯如该管地方。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干（甲/乙取值） | year_stem | existing | 结构 | bazi | 天干 |
| 地支（寅/卯取值） | month_branch | existing | 结构 | bazi | 地支 |
| 天地框架（施/受之分） | common_heaven_earth_frame | new_candidate | 关系 | common | 宇宙框架 |
| 官长/地方类比（治理模型） | common_governance_analogy | new_candidate | 结构 | common | 类比结构 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_stems_govern_branches_receive` | 若以「官长/地方类比（治理模型）」理解干支关系 | 则天干偏“施/行”，地支偏“受/存”，可用于解释“气之下达与成形承载”的分工 | 运势 | 中性 | 中 | 甲乙如官长，寅卯如该管地方 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_018` | year_stem AND month_branch AND common_governance_analogy | 天干施令如官长，地支承受如地方。 | 主干依赖 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:19` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 官长／地方（施令与承受） | year_stem, month_branch |  |  |  |  | neutral_career_support |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 官长 | Governing Authority (Analogy) | 以官长类比天干之施行与统摄。 | A governance metaphor used to clarify how a “driving” layer sets direction or initiates action in a two-layer model. | common_governance_analogy | new_candidate |
