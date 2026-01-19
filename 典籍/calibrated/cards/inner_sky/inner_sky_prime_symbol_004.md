## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_004`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:449`
- `source_text`:
  > The power of the astrological language lies in its particularity, the way it addresses the uniqueness of
  > each individual’s personal reality. This, rather than metaphysics, must always be its focus. Yet, per-
  > meating the system we find the scent of that most pr imal of human perceptions: a sense of the presence
  > of the Absolute, a sense of the possibility of self-transcendence. Heady stuff! To make the prime symbol relevant to everyday life, we must step down its voltage. We must
  > break it up into smaller pieces more suited to the narrow scope of our daily experience. Our first effort
  > in this direction is to reduce our imagery from three dimensions to two, from the sphere to the circle.
  > The Circle of the Year
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Personal particularity focus | astro_personal_particularity_focus | new_candidate | 状态 | astro | focus |
| Sense of self-transcendence possibility | astro_transcendence_sense | new_candidate | 状态 | astro | intuition |
| Abstraction voltage step-down | astro_abstraction_voltage_stepdown | new_candidate | 状态 | astro | method |
| Sphere→circle reduction | astro_sphere_to_circle_reduction | new_candidate | 结构 | astro | transformation |
| Circle-symbol (cross-system proxy) | tarot_wheel_of_fortune | existing | 结构 | tarot | symbol |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_stepdown_sphere_to_circle` | If `Abstraction voltage step-down` is applied to `Sphere→circle reduction` | Translate overwhelming metaphysical awe into interpretable, everyday-scale symbols without losing the sense of depth | 心理 | 中性 | 高 | `from the sphere to the circle.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_004` | astro_abstraction_voltage_stepdown AND astro_sphere_to_circle_reduction | When the infinite sky is too loud to live with, you turn it into a circle—small enough to hold in your hands, strong enough to change a day. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:449` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Step down abstraction into usable symbols | bazi_shishen | astro_abstraction_voltage_stepdown, astro_sphere_to_circle_reduction | tarot_wheel_of_fortune | dream_symbolic_motif |  | neutral_transformation_opportunity |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Self-transcendence | 自我超越 | A felt possibility of moving beyond the usual limits of the self. | 在不否认现实的前提下，意识能超出惯性自我与偏见，看见更大的选择与意义。 | astro_transcendence_sense | new_candidate |

