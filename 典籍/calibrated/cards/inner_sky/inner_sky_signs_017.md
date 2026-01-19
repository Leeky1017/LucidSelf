## A - Entry Metadata

- `card_id`: `inner_sky_signs_017`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:820`
- `source_text`:
  > Turn to the Gemini chapter of any sun-sign book. Somewhere in the first paragraph you will read the word communication. Speaking and listening are certainly key issues for the Twins, but to understand
  > them, we must go further. The psychic process to which Gemini refers includes much more. It is the
  > whole issue of perception, the way the world communicates with us. The way we see, feel, hear, and smell
  > all the phantasmagoria that surrounds us. Listening to words is just one thread in that much vaster
  > tapestry. Gemini is born to perceive, to gorge itself with observations. The stasis so characteristic of
  > Taurus is antithetical to the Twins. This sign must remain in motion all the time. There is so much to
  > see and know. Not a minute to waste. Like a child suddenly granted ten minutes to pillage a toy store,
  > Gemini rushes through experience, sometimes franti c, often without any apparent master plan, but
  > always with gusto. Alert intelligence is basic to th e Twins. But concentrating on intelligence clouds our
  > understanding of what is born here. To Gemini, th inking is epiphenomenal, just a side-effect. The
  > thrust of the sign is not intellection. It is raw pe rception. Not thinking, but seeing. Gemini is not so
  > much a philosopher as a journalist. The undigested fact s of perception, not their meaning, are its food. It
  > only wants to see, to witness the world. Ideas and understanding may arise, but they are not the point. *. To unravel the secret of the world. To gather all the clues. To see everything. That is Gemini’s endpoint.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Gemini (sign) | sign_gemini | existing | 结构 | astro | sign |
| Air element energy | element_air_energy | existing | 能量 | astro | element |
| Mutable mode energy | mode_mutable_energy | existing | 能量 | astro | mode |
| Clarity of thinking/judgment | clarity_index | existing | 能量 | astro | cognition |
| Raw perception drive | astro_raw_perception_drive | new_candidate | 状态 | astro | core_theme |
| Motion compulsion | astro_motion_compulsion | new_candidate | 状态 | astro | behavioral_tone |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_gemini_see_over_think` | If `Gemini (sign)` is active and `Raw perception drive` is high | Prioritize witnessing over conclusion-making; treat thinking as a byproduct of observation, not its goal | 心理 | 中性 | 高 | `Not thinking, but seeing.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_017` | sign_gemini AND astro_raw_perception_drive | You move like a reporter with a hungry notebook—eyes, ears, skin collecting facts faster than meaning can form, refusing to miss a single clue. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:820` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Gemini as perception-hunger and constant motion | metal_presence | sign_gemini, element_air_energy, mode_mutable_energy, astro_raw_perception_drive | tarot_suit_swords | dream_setting |  | neutral_timing_fast |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Raw perception | 原始感知 | Direct noticing of sensory and situational facts before interpretation or meaning-making. | 在“理解/评价”之前先看见：让事实与细节直接进入意识，允许暂时不下结论。 | astro_raw_perception_drive | new_candidate |

