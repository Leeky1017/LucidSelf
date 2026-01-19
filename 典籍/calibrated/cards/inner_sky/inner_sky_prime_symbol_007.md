## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_007`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:472`
- `source_text`:
  > It is the same with the solar system. The sun, for our purposes, is stationary. We move around it like a photographer searching for the right angle. Ye t our perceptions tell us we are standing still and
  > that the sun is in motion. Why? Because the sun’s starry background changes as we swing through our orbit, just as our friend appeared to be standing agai nst a bookcase, then against a wall, even though she
  > never moved. Earth’s “hunt for the right angle” is constant; our orbit never varies. And so the sun’s apparent
  > “orbit” around us never varies either. It travels from constellation to constellation in an endless, orderly
  > progression. The path it follows has been mapped since antiquity. In modern times we call it the ecliptic,
  > but it has a far more ancient name: the zodiac.
  > The zodiac is a two-dimensional transl ation of astrology’s prime symbol, the sky itself. Like the
  > sky, this circle is a metaphor for the eternal and the infinite, simpler than the sphere but still far too all-
  > encompassing to be of any practical value. We are left with a classic problem: Where does the circle begin? How can we break it down? The solution lies where it always must in astrology: with our eyes, our hearts, and our common sense. Earth’s orbit is visible to us through the varying relation of the sun to the background stars. But
  > that’s fairly subtle. Astronomer-priests might notice it. Sailors would too. But the rest of us need not
  > have such an eye for detail. The year hits us over the head in a way that is harder to ignore. The
  > weather turns freezing cold. Then it gets blazing ho t. Seasons change. And those changes are propelled
  > by our yearly trajectory around the sun. An astronomical “crisis” marks the outset of each season. And those four “crises” carry us
  > beyond the prime symbol. They begin to break down the Absolute, to make it accessible. Through them we divide the circle. Winter brings a low sun, short days, and long nights. In the summer this is reversed. If we
  > follow the variations in light throughout the year, a distinct pattern emerges. At one point the length of
  > the day and the length of the night are equal. Th en the day begins growing. Precisely three months
  > later we reach a crisis. Day is in the ascendancy; nigh t is at its weakest. But darkness rallies and slowly
  > begins to erode the day. Gradually the two move back toward equilibrium. This balancing takes another
  > three months. When it is complete, day and night are again equal. Over the next three months, darkness continues to overwhelm light. Then another crisis is reached; day begins to fight back. It is feeble at first, but the momentum has shifted. In three months
  > light equals darkness and we are back where we began. This slow breathing of the earth’s li ght is the rudimentary astrological rhythm; without it, we
  > could go no further than the abstraction of the prime symbol.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Ecliptic path | astro_ecliptic_path | new_candidate | 结构 | astro | path |
| Zodiac circle | astro_zodiac_circle | new_candidate | 结构 | astro | circle |
| Seasonal “crisis” markers | astro_seasonal_crisis_markers | new_candidate | 时间 | astro | seasonal_turning_points |
| Light–dark equilibrium points | astro_light_dark_equilibrium | new_candidate | 时间 | astro | rhythm_anchor |
| “Breathing” light rhythm | astro_earth_light_rhythm | new_candidate | 时间 | astro | rhythm |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_zodiac_divide_circle` | If `Zodiac circle` is interpreted through `Seasonal “crisis” markers` | Divide the symbolic circle using seasonal turning points; treat the “breathing” of light as the operational rhythm behind sign symbolism | 心理 | 中性 | 高 | `An astronomical “crisis” marks the outset of each season.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_007` | astro_zodiac_circle AND astro_seasonal_crisis_markers | As the year swings between equal light and equal dark, the circle breaks into seasons; each turning point becomes a doorway where meaning changes. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:472` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Zodiac as a symbolic circle divided by seasonal turning points | month_branch, solar_term | astro_zodiac_circle, astro_seasonal_crisis_markers, astro_earth_light_rhythm | tarot_wheel_of_fortune | dream_time_context |  | neutral_timing_slow |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Zodiac | 黄道十二宫（黄道带） | The ecliptic circle used symbolically to divide the year into meaningful phases. | 把一年轨迹投影成圆环，用季节节律分段并承载十二段性格/成长过程的象征。 | astro_zodiac_circle | new_candidate |

