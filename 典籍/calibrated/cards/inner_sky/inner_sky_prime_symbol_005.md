## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_005`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:456`
- `source_text`:
  > Two physical motions, both circular, lie at the roots of astrological symbolism. One is the rotation of
  > the earth on its axis. The second is the revolution of the earth in its orbit around the sun. The first motion produces the houses. We discuss those in a later chapter. The second circle gives rise to the
  > symbolism of the signs. And it is through the signs that the prime symbol comes down to earth.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Earth rotation (daily) | astro_earth_rotation | new_candidate | 时间 | astro | motion |
| House system (derived from rotation) | astro_house_system | new_candidate | 结构 | astro | house_framework |
| Example house: First House | house_1 | existing | 结构 | astro | house |
| Earth revolution (yearly) | astro_earth_revolution | new_candidate | 时间 | astro | motion |
| Sign system (derived from revolution) | astro_sign_system | new_candidate | 结构 | astro | sign_framework |
| Sun sign indicator | sun_sign | existing | 结构 | astro | sign |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_motion_to_symbols` | If `House system (derived from rotation)` and `Sign system (derived from revolution)` are used to interpret experience | Break down the prime symbol into interpretable arenas (houses) and seasonal phases (signs) for personality-level reading | 心理 | 中性 | 高 | `The first motion produces the houses.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_005` | astro_house_system AND astro_sign_system | A day spins into houses and a year circles into signs; together they turn the sky’s vastness into a map you can actually live inside. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:456` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Rotation→houses / Revolution→signs | day_branch, month_branch | astro_house_system, astro_sign_system | tarot_wheel_of_fortune | dream_time_context |  | neutral_timing_slow |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Houses | 宫位 | Twelve sectors derived from Earth’s rotation, used to map life arenas in a chart. | 把一天的地球自转投影成十二个领域分区，用来描述人生舞台（如自我、关系、事业等）的落点。 | house_1 | existing |

