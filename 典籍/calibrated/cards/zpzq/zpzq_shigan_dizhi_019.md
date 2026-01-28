## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_019`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:21`
- `source_text`:
  > 甲乙在天，故动而不居。建寅之月，岂必当甲？建卯之月，岂必当乙？寅卯在地，故止而不迁。
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 天干之动（动而不居） | common_stem_mobility | new_candidate | 状态 | common | 干之特性 |
| 地支之定（止而不迁） | common_branch_stability | new_candidate | 状态 | common | 支之特性 |
| 月干（递易） | month_stem | existing | 结构 | bazi | 月干 |
| 月支（建月） | month_branch | existing | 结构 | bazi | 月令 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_stem_rotates_branch_fixed_for_months` | 若区分「天干之动（动而不居）」与「地支之定（止而不迁）」 | 则建月以地支为定标，而月干可递易不必固定对齐某一支 | 运势 | 中性 | 中 | 甲乙在天，故动而不居 |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_019` | common_stem_mobility AND common_branch_stability AND month_branch | 天干流转，地支定月，时序由此可循。 | 主干 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:21` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 动而不居／止而不迁（干动支定） | month_stem, month_branch |  |  |  |  | neutral_timing_fast, neutral_timing_slow |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 建寅 | Jian-Yin Month | 以寅为建月之支，月干可递易，不必固定为甲。 | A lunar month designated by the branch Yin as its anchor; the stem overlay can vary rather than being fixed to Jia. | month_branch | existing |
