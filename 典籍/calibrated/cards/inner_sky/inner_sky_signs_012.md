## A - Entry Metadata

- `card_id`: `inner_sky_signs_012`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:637`
- `source_text`:
  > The Aries Symbol
  > The Ram. Horns down, charging. Fierce. Unyielding. Will the Ram crack his skull? He doesn’t care.
  > Nothing can intimidate him. Nothing can force his will to swerve. Victory—or self-destruction in the effort to attain it: two destinies. One will claim him. Aries is the life force , the will to exist. First there is nothing. Then there is something. Life
  > thrusts itself out of nowhere, claiming a place in the void. The tone of the process is unflinching,
  > explosive, violent. It conjures up pictures of volcan oes, of white-hot stars bursting into tattered nebulas.
  > A rabid dog backs you up to a precip ice, fangs bared, mouth foaming. You have a hunting knife
  > in your hand. He moves in, growling, eyes glaring re d. You brace yourself. No more veneer of gentility
  > and education. No more language. Nothing left but the animal rage to survive. You scream. You drive
  > for the throat. You have found Aries. Aries teaches courage. It represents the ability of the will to triumph over any intimidation, any
  > obstacle, any doubt. The Ram is the part of us that does exactly what it wants to do. It chooses and it
  > acts. Nothing else matters. Wrestling crocodiles blindf olded? Yes — if that is what we want. But that
  > kind of activity is beside the point. Aries is the sign of daring, of any act of sheer adventurousness,
  > regardless of how smart the act might be. But its real meaning is deeper. It refers to existential courage.
  > What is that? In a word, it is selfi shness. A delicate art. Not insensitivity. Not narrowness. Not
  > manipulation. But the ability to say: “This is my life. I have the right to seek whatever experiences I
  > need to have. Nothing will stand between me and my growth. Not another person. Not any
  > circumstance. Not even my own fears.”
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Aries (sign) | sign_aries | existing | 结构 | astro | sign |
| Fire element energy | element_fire_energy | existing | 能量 | astro | element |
| Cardinal mode energy | mode_cardinal_energy | existing | 能量 | astro | mode |
| Existential courage | astro_existential_courage | new_candidate | 状态 | astro | core_theme |
| Will to exist (life-force drive) | astro_will_to_exist | new_candidate | 状态 | astro | drive |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_aries_courage` | If `Aries (sign)` is activated and `Existential courage` is cultivated | Prioritize decisive self-assertion: the will can act through fear and intimidation in service of growth | 心理 | 中性 | 高 | `Aries teaches courage.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_012` | sign_aries AND astro_existential_courage | Horns down, you choose the direct line—no excuses, no negotiations. The fear stays, but your will stays louder. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:637` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Aries as life-force + existential courage | fire_presence | sign_aries, element_fire_energy, mode_cardinal_energy, astro_existential_courage | tarot_chariot | dream_fear_level, dream_energy_level |  | neutral_vitality_high, neutral_timing_fast |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Existential courage | 存在性勇气 | Courage grounded in the right to exist and to pursue needed experience despite fear. | 不是逞强，而是在恐惧仍在时仍然敢于为“这是我的人生”承担选择与行动后果的勇气。 | astro_existential_courage | new_candidate |

