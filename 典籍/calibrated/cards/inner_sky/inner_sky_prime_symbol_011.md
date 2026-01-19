## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_011`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:590`
- `source_text`:
  > But it is a two-way street. Signs are avenues of expression, but they are also roads back to the
  > source, back to the prime symbol. They offer effective descriptions of personality. They form a useful
  > catalog of human character types. But they are also evolutionary methods, ways of growing.
  > Read signs as a typology and we are back to square one. We are still telling fortunes. “You are
  > an Aries. That means you are brave and advent uresome.” Read them as methods of growth and
  > everything is transformed. We add the spice of possibi lity, of a larger destiny. “You are an Aries. You
  > must become more courageous. You have come into the world to strengthen the power of your will.
  > Challenging, frightening experiences have pursued you since you were born. They will pursue you until you die. Facing them bravely is your destiny. You must rise and meet them. Fail and you will meet only terror.” Growth. Risk. The uncertainty of the sti ll-unresolved battle. That is evolutionary astrology. No
  > one is simply an Aries. That is a myth. Signs are psychological processes common to all of us. Each one of us embodies all twelve. We differ only in the degree to which they are emphasized. Again, the prime symbol is a circle. Every birthchart is a circle—the same circle. In some way each sign is activated in
  > every one of us. Fully to grasp even one sign strains the intellect. Yet, compared to people, signs are as one-dimensional as Batman and Robin. Each of us is a synthesis of all twelve. To imagine a person with no
  > Arian energy, for example, is like imagining someon e with no emotions. An impossibility. People may
  > be born without arms and legs; they are still un questionably human. But to be born without some
  > Taurean qualities or some Geminian ones—that would make us as otherworldly as a creature stepping
  > out of a flying saucer. The process we call Leo may dominate someone’s personality. But the other
  > processes are there. Cancer may lurk in the shado ws, never visible. Pisces may seem completely
  > absent—until money matters hit a snag or until the pe rson falls in love. Each sign is always present,
  > awaiting the right trigger.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Signs-as-growth-methods reading | astro_signs_as_growth_methods | new_candidate | 状态 | astro | interpretive_frame |
| Signs as psychological processes | astro_signs_as_psych_processes | new_candidate | 结构 | astro | process_model |
| Sign activation trigger | astro_sign_activation_trigger | new_candidate | 关系 | astro | trigger |
| Sun sign indicator | sun_sign | existing | 结构 | astro | sign |
| Birthchart as a circle | astro_birthchart_circle | new_candidate | 结构 | astro | geometry |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_signs_as_processes` | If signs are read through `Signs as psychological processes` (not fixed typology) | Treat each sign as a growth method available to everyone; look for `Sign activation trigger` instead of locking identity to a single type | 心理 | 中性 | 高 | `Signs are psychological processes common to all of us.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_011` | sun_sign AND astro_signs_as_growth_methods AND astro_sign_activation_trigger | No part of you is missing; every sign is waiting. When money snags or love strikes, a “hidden” process wakes up and demands its next lesson. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:590` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Signs as processes: all twelve present, activated by triggers | day_master | astro_signs_as_psych_processes, astro_sign_activation_trigger, sun_sign | tarot_world | dream_primary_pattern |  | neutral_transformation_opportunity |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Typology | 类型学式分类 | A system that classifies people into fixed types. | 把人归入固定类型的分类法：便于速记与自我标签，但容易牺牲复杂性与成长维度。 | astro_signs_as_growth_methods | new_candidate |

