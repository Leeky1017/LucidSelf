## A - 条目元信息（Entry Metadata）

- `card_id`: `zpzq_shigan_dizhi_020`
- `source_anchor`: `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:21`
- `source_text`:
  > `欲学命者，必须先知干支之说，然后可以入门。`
- `priority`: `P0`

---

## B - 因子提取（Factor Extraction）

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| 十干（以年干示例） | year_stem | existing | 结构 | bazi | 天干 |
| 十二支（以年支示例） | year_branch | existing | 结构 | bazi | 地支 |
| 干支体系（抽象结构） | common_stem_branch_system | new_candidate | 结构 | common | 干支系统 |
| 入门先修（知识前置） | common_prerequisite_knowledge | new_candidate | 状态 | common | 学习路径 |

---

## C - 规则草案（Rule Drafts）

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_zpzq_stem_branch_prereq_for_learning` | 若以「入门先修（知识前置）」规划命理学习路径 | 则必须先掌握「干支体系（抽象结构）」后，才进入后续判读与推演 | 心理 | 中性 | 高 | `必须先知干支之说` |

---

## D - 叙事素材（Narrative Snippets）

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_zpzq_020` | common_stem_branch_system AND common_prerequisite_knowledge | 先通干支，方可入命理之门。 | 总结 | `典籍/中文典籍/子平真诠/原文/子平真诠原文.md:21` |

---

## E - 跨体系映射（Cross-System Mapping）

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| 干支入门（先修路径） | year_stem, year_branch |  |  |  |  | neutral_transformation_opportunity |

---

## F - 术语对齐（Term Alignment）

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| 干支之说 | Stems-and-Branches Fundamentals | 干支为命理基础符号系统，先明其理，方可继续深入。 | Foundational principles of the stems-and-branches framework; treated as prerequisite knowledge before advanced interpretation. | common_stem_branch_system | new_candidate |

