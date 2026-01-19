## A - Entry Metadata

- `card_id`: `inner_sky_signs_015`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:731`
- `source_text`:
  > Exhausted by the fiery furnace of Aries, consciousness seeks pools of cool water, the solace of ancient
  > stones, the healing rustle of birdsong among green leav es. It seeks peace. It trades the harangue for the
  > symphony, passion for silence. No longer incandescent with the fire of battle, spirit reaches gnarled
  > hands into the earth, feeling for seeds, fo r clay, for the flesh of the planet itself.
  > The symbol is a bull. Not the enraged monster furious at the red flag of the matador. Not the ferocious bull. But rather the tranquil one, standin g solitary beneath a spreading April oak, quietly
  > surveying grass and sun, cattle and earth. Nothing fr ightens him. Gone is the fearsome posturing of the
  > Ram. The Bull is so in control of his world, so far beyond fear that fearlessness itself has become
  > meaningless to him. The Arian war has been won. Taurus is at peace.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Taurus (sign) | sign_taurus | existing | 结构 | astro | sign |
| Earth element energy | element_earth_energy | existing | 能量 | astro | element |
| Fixed mode energy | mode_fixed_energy | existing | 能量 | astro | mode |
| Seeking peace | astro_seek_peace | new_candidate | 状态 | astro | core_theme |
| Earth-contact grounding | astro_earth_contact_grounding | new_candidate | 关系 | astro | grounding |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_taurus_seek_peace` | If `Taurus (sign)` is activated and `Seeking peace` is prioritized | Move from battle intensity toward calm stability; grounding through physical contact with the material world supports peace | 心理 | 中性 | 高 | `It seeks peace.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_015` | sign_taurus AND astro_seek_peace | Under an April oak, the bull stands alone—unhurried, unflinching. Your nervous system remembers that nothing needs to be fought right now. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:731` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Taurus as peace through earth-grounding | earth_presence | sign_taurus, element_earth_energy, mode_fixed_energy, astro_seek_peace | tarot_suit_pentacles | dream_resolution_sense |  | neutral_emotional_harmony, neutral_timing_slow |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Peace | 宁静 | A calm state where fear and agitation subside into stable presence. | 一种可持续的安稳感：不是麻木，而是身体与环境重新对齐后产生的放松与不急于反击。 | astro_seek_peace | new_candidate |

