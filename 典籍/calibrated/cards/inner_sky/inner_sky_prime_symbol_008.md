## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_008`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:494`
- `source_text`:
  > Astrology really has nothing to do with the stars them selves. It is based solely on these variations in
  > light, or, more simply, on the seasons. But what about Aries and Taurus and Capricorn? Those are
  > constellations. They are stars. If they really have nothing to do with astrology, why do we talk about
  > them? Millennia ago, astronomer-priests noti ced that on the morning of the day when light at last
  > began to make inroads into the darkness, the sun ro se into the stars of Capricorn. The constellation
  > served as a convenient visual marker for the location of the sun along the ecliptic. Such knowledge helped our forebears in practical ways, such as timi ng the planting season. The convenience turned out
  > to be temporary. Due to a slow wobble in the earth’s axis, the position of the sun on the first day of winter gradually shifted backward through Capricorn towa rd the constellation Sagittarius. Traditions die
  > slowly, though. The priests were accustomed to sayi ng that when earth entered winter, the sun entered
  > Capricorn. They kept right on saying it, even wh en Sagittarius was truly the winter’s constellation.
  > This slip-up produced no serious prob lem for astrology itself, but it has been hard on public
  > relations. Astronomers are fond of saying, “Even if there were something to astrology, all you Arians
  > were really born with the sun in Aquarius, so you’ re reading the wrong sign.” The problem here is one
  > of communication. When an astronomer says “Aries,” he or she means a certain group of stars. To the
  > astrologer, Aries means something entirely different. It refers to a certain phase in earths orbit around
  > the sun, or, more simply, to a certain season.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Light-variation basis | astro_light_variation_basis | new_candidate | 时间 | astro | mechanism |
| Season-based sign meaning | astro_season_based_sign_meaning | new_candidate | 结构 | astro | sign_basis |
| Axial wobble / precession | astro_precession_axis_wobble | new_candidate | 时间 | astro | long_cycle |
| Constellation vs sign term gap | astro_constellation_vs_sign_term_gap | new_candidate | 关系 | astro | terminology |
| Aries (as sign, not constellation) | sign_aries | existing | 结构 | astro | sign |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_seasons_not_stars` | If `Season-based sign meaning` is used when explaining a sign | Define signs as seasonal/light phases rather than star groups; address “wrong sign” objections as a communication mismatch | 心理 | 中性 | 高 | `Astrology really has nothing to do with the stars them selves.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_008` | astro_season_based_sign_meaning AND astro_light_variation_basis | You stop arguing about star maps and start watching the seasons; Aries becomes a phase of light, a mood in the year, not a fixed cluster of dots. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:494` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Seasonal zodiac vs constellations (public misconception) | month_branch | astro_season_based_sign_meaning, astro_precession_axis_wobble, sign_aries | tarot_wheel_of_fortune | dream_time_context |  | neutral_timing_slow |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Constellation | 星座（恒星群） | A group of stars used as a visual marker in the sky. | 天空中被连成图案的一组恒星，用于定位与记忆；不等同于占星中的黄道十二宫。 | astro_constellation_vs_sign_term_gap | new_candidate |

