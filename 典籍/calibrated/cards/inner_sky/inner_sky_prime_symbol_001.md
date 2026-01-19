## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_001`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:428`
- `source_text`:
  > The sky. That is astrology’s prime symbol. The sky is the bedrock from which the elaborate language of
  > the birthchart arises.
  > But what does it mean? To the astr onomer, the question doesn’t make sense. He or she can say
  > what the sky is. But what it means —that is something for poets and philosophers to dwell on, not
  > astronomers. Burn away all the name calling, an d the difference between astrologers and astronomers
  > boils down to this: astronomers seek to know the form of the heavens, while astrologers pursue their
  > meaning. Astrology is the poetry of astronomy. It is not so much a study of structure as of significance.
  > Not what the sky is. But what it says to us.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Prime Symbol (Sky) | astro_prime_symbol_sky | new_candidate | 结构 | astro | symbol |
| Meaning-over-Form stance | astro_symbolic_meaning_focus | new_candidate | 状态 | astro | mindset |
| Birthchart (as symbolic language) | astro_birthchart | new_candidate | 结构 | astro | chart |
| Clarity of thinking/judgment | clarity_index | existing | 能量 | astro | cognition |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_prime_symbol_poetry` | If `Meaning-over-Form stance` is held while reading `Prime Symbol (Sky)` | Interpret the birthchart as a language of significance (poetry), not as a measurement of celestial structure | 心理 | 中性 | 高 | `Astrology is the poetry of astronomy.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_001` | astro_prime_symbol_sky AND astro_symbolic_meaning_focus | You stop measuring the heavens and start listening to them; the chart becomes a poem, and your choices are the verbs that give it meaning. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:428` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Astrology as meaning-making (poetry of astronomy) | bazi_shishen | astro_prime_symbol_sky, astro_symbolic_meaning_focus | tarot_magician | dream_symbolic_motif, dream_setting |  | neutral_transformation_opportunity |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Prime symbol | 核心象征 | A foundational image that carries the deepest meaning of a symbolic system. | 在符号语言里最底层、最能承载总体意义的象征意象，用来统一理解后续符号。 | astro_prime_symbol_sky | new_candidate |

