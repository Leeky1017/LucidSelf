## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_002`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:436`
- `source_text`:
  > Exactly what does it say? To answer th at we do not need to be an Aristotle or a William Butler
  > Yeats. All we have to do is look and think. Wh o can stare at the Milky Way on a moonless summer
  > evening, meteors streaking past Vega and Altair, without feeling a sense of wonder? Whatever cynics might say about this television-addled ag e, such dullness of heart remains rare.
  > In ancient times, the sky was sacred; people were sure God lived there. This sense of the sky’s
  > holiness is a nearly universal element in early reli gions. Our metaphysics may have matured, but our
  > hearts have changed little. The heavens still fill us with reverence and awe.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Wonder / Awe response | astro_wonder_awe | new_candidate | 状态 | astro | affect |
| Sacred-sky archetype | astro_sacred_sky_archetype | new_candidate | 结构 | astro | archetype |
| Joy intensity (dream affect proxy) | dream_joy_level | existing | 能量 | dream | affect |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_sky_evokes_awe` | If `Wonder / Awe response` is activated by the night sky | Treat symbolic language as emotionally grounded (reverence/awe are available as lived experience) | 心理 | 中性 | 高 | `The heavens still fill us with reverence and awe.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_002` | astro_wonder_awe | On a moonless night, the Milky Way knocks the cynicism out of you; reverence returns, and you remember why symbols matter. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:436` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Sky-wonder as an entry to symbolism | bazi_zhengyin | astro_wonder_awe, astro_sacred_sky_archetype | tarot_star | dream_setting, dream_joy_level |  | neutral_emotional_harmony |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Reverence | 敬畏 | A felt respect and awe toward something vast and sacred. | 面对宏大事物时自然升起的尊重与自我收束感，让人愿意谨慎、谦卑地对待意义。 | astro_wonder_awe | new_candidate |

