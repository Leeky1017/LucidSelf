## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_009`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:509`
- `source_text`:
  > Seasonal changes, then, not stars, are at the heart of sign symbolism. Through variations in the
  > length of night, we mark four critical points that he lp us divide the circle. Infinity is broken down into
  > four finite phases, each with its own distinctive character.
  > We call these four phases elements.
  > The Dance of the Elements
  > Fire, Earth, Air, and Water. The elements. Images fr om antiquity. Four primal states of being. Four
  > faces of the universe. Within us they exist as stat es of consciousness. Beyond us they function as
  > templates for all physical and metaphysical proc esses. How are they connected with seasons?
  > The first element arises in the equilibrium of light and dark, but at a time when light has the
  > momentum, when light is increasing. Astronomically, this moment is called the vernal equinox, but most
  > of us know it simply as the first day of spring. Astr ologically, the vernal equinox symbolizes the birth of
  > the element
  > Fire. This is the principle of action. Like springtime, its spirit is one of out-rushing energy,
  > charging into the cosmos, shattering all that stands in its way. Uncompromising invincibility of
  > purpose—that is fire. Soon we will see how it come s to permeate the signs Aries, Leo, and Sagittarius.
  > Earth follows fire in the traditional order of the elements. This second life principle emerges out
  > of the heart of night. It is associated with the winter solstice, the point in the yearly cycle at which
  > darkness reaches maximum power. Winter time. All t hrough nature we see a spirit of grim, enduring
  > determination. Earth symbolizes stability and continuit y. Its emphasis is on making peace with a hard,
  > unyielding world. Practicality and resourcefulness arise here. Earth is the sustainer, the giver and
  > maintainer of form. Embodied in Taurus, Virgo, and Capricorn, it is endlessly building, crystallizing,
  > and perfecting. After earth comes
  > Air. Air appears at another equilibrium point in the cycle of light and darkness.
  > This time night is in the ascendancy, getting ready to overwhelm day. We call the moment the
  > autumnal equinox. It marks the beginning of fall. In anticipation of winter, there is a feeling of
  > foreboding in the autumn atmosphere. All creatures sense the coming of darkness. They sense death,
  > and its specter heightens their alertness. In air, we find perceiving, reasoning, connecting— the mental
  > functions. Its tone is one of unending curiosity, of detachment and clarity of perception. More than any
  > other element, air is aware that beyond itself lies the unknown. The questing spirit of air animates Gemini,
  > Libra, and Aquarius.
  > Water is the last of the elements. It arises when light attains maximum power, the first day of
  > summer. Astronomers call this moment the summer solstice. In summer, the land itself seems to favor life.
  > Nature becomes «a protective womb. Even weak life forms are granted a few unharried moments.
  > Water is the principle of nurturance and protection. Outwardly, its spirit is one of warmth; inwardly, of
  > imagination and intuition. With its penetrating, sensitive quality, water’s prime function is to feel. Cancer,
  > Scorpio, and Pisces are the signs conditioned by water.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Fire element energy | element_fire_energy | existing | 能量 | astro | element |
| Earth element energy | element_earth_energy | existing | 能量 | astro | element |
| Air element energy | element_air_energy | existing | 能量 | astro | element |
| Water element energy | element_water_energy | existing | 能量 | astro | element |
| Elements as states of consciousness | astro_elements_consciousness_states | new_candidate | 结构 | astro | framework |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_fire_action` | If `Fire element energy` is predominant | Expect an emphasis on action: out-rushing energy and invincibility of purpose are psychologically available | 心理 | 中性 | 中 | `Fire. This is the principle of action.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_009` | element_fire_energy OR element_earth_energy OR element_air_energy OR element_water_energy | When fire rises in you, you charge forward and shatter obstacles; when earth speaks, you build and endure; air thinks; water feels and protects. | 主干依赖 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:509` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Four elements (Fire/Earth/Air/Water) as symbolic life-states | fire_presence, earth_presence, metal_presence, water_presence | element_fire_energy, element_earth_energy, element_air_energy, element_water_energy | tarot_suit_wands, tarot_suit_pentacles, tarot_suit_swords, tarot_suit_cups | dream_symbol_fire, dream_symbol_water |  | neutral_emotional_harmony |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Elements | 四元素 | Four fundamental symbolic phases used to divide the circle into distinct qualities. | 用来把“圆”拆成四种可感知的性质：行动（火）、稳定（土）、理性（风）、滋养（水），便于落到具体体验。 | astro_elements_consciousness_states | new_candidate |

