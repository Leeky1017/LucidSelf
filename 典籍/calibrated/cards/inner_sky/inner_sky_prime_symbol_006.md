## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_006`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:459`
- `source_text`:
  > If we wake each day before dawn an d study the sky, we quickly notice a pattern. Every morning
  > the sun rises into a patch of stars. Over several week s we see that while the sun keeps rising in the east,
  > the stars that its light first touches are gradually ch anging. On a particular morning it rises into one
  > constellation. A month later it rises into another, then another, and so on until a year elapses and it is
  > back where it started.
  > Objective reality is very different, bu t those are the facts of perception. That is what we see.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Dawn observation pattern | astro_dawn_observation_pattern | new_candidate | 时间 | astro | observation |
| Yearly star-backdrop shift | astro_yearly_star_backdrop_shift | new_candidate | 时间 | astro | sky_pattern |
| Perception-as-foundation model | astro_perception_facts_model | new_candidate | 状态 | astro | epistemic_stance |
| Clarity of thinking/judgment | clarity_index | existing | 能量 | astro | cognition |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_perception_facts` | If `Perception-as-foundation model` is adopted | Use repeatable, observable patterns (what we see) as the operational basis for symbolism, even when the underlying mechanics are abstract | 心理 | 中性 | 中 | `those are the facts of perception. That is what we see.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_006` | astro_perception_facts_model AND clarity_index | You watch dawn after dawn until the stars behind the Sun quietly change; what you see becomes the grammar of a symbol, even when the mechanics are invisible. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:459` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Perception-based patterns as symbolic foundation | month_branch | astro_perception_facts_model, astro_yearly_star_backdrop_shift | tarot_moon | dream_time_context |  | neutral_timing_slow |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Facts of perception | 感知事实 | The observable patterns we directly experience, regardless of deeper mechanics. | 不依赖理论解释、只凭肉眼与体验可反复确认的模式；它是符号语言的起点。 | astro_perception_facts_model | new_candidate |

