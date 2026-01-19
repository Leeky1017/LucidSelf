## A - Entry Metadata

- `card_id`: `inner_sky_signs_014`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:696`
- `source_text`:
  > blazing in our spirit. But what does the warrior do in time s of peace? He cannot maintain his self-image without some
  > form of resistance threatening him from the outside world. The soldier needs an adversary. Armies will
  > fight. If they are not challenged by a legitimate en emy, they find an illegitimate one, perhaps even
  > turning on the country they were instituted to protect. We find precisely the same phenomenon in the Ram. He will fight. That much is certain. But no one can say whether his battles serve the purpose of
  > evolutionary change or take the form of pointless confrontation. Fortunately, legitimate enemies abou nd. Again and again, Aries is confronted with frightening
  > roadblocks. They may be powerful people who atte mpt to wrest away the Ram’s freedom. They may be
  > adverse constellations of circumstance. Sometimes they are inner weaknesses. Often the roadblocks take
  > the form of interpersonal misperceptions, typicall y engendered by Aries’s own intensity—since that
  > quality often puts other people on the defensive. Whatever form the roadblocks take, they must be
  > faced. If there is a cardinal sin for the Ram, it is chickening out. Such battles hold ambiguous appeal. We may know that they help us grow. But perhaps we are
  > very tired. If Aries chooses to follow the path of leas t resistance, it is free to do so. The battle must be
  > willingly accepted. Either way, the Ram remains a magnet for stress. Choice lies only in selecting the form the
  > stress takes. It may be the meaningful stress of pe rsonal growth, of challenges accepted and mountains
  > conquered. Or it may be an endless parade of em pty, pointless hassles, largely brought about by the
  > Aries’s own boredom, touchiness, and frustratio n. Down that road lies the Ram’s shadow.
  > The warrior is full of the fire of battle . He needs it in order to accomplish what he came here to
  > do. But, should he turn away from an evolutionary crisis, that fire still remains. It cannot be
  > extinguished. Invariably it attacks some extraneous target with all the passion that might have been
  > appropriately applied to the real issue. Arguments may arise in which the emotional pitch seems out of proportion to the apparent content of the conflict. “Why do you insist on wearing that damned yellow shirt?”
  > All the fierceness, will, and courage of the Ram are then dissipated aimlessly. Friends are driven
  > away. Marriages fail. Careers are blown over petty issues. Nobody wins. That volatile, evolutionary
  > rocket fuel goes up like Fourth of July fireworks, full of hellfire and brimstone, empty of meaning.
  > The Arian who has taken that weaker pa th is left wounded, full of hunger and frustration. He
  > may be self-righteous. He may be self-pitying. But hi s question is always the same: “Why do I seem to
  > put everyone on the defensive?” And the answer? Simple. The warrior fought the wrong war.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Aries (sign) | sign_aries | existing | 结构 | astro | sign |
| Stress / emotional tension | emotional_tension | existing | 能量 | astro | pressure |
| Misdirected battle (wrong war) | astro_misdirected_battle | new_candidate | 状态 | astro | shadow_pattern |
| Interpersonal defensiveness trigger | astro_interpersonal_defensiveness_trigger | new_candidate | 关系 | astro | social_dynamic |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_aries_wrong_war` | If `Aries (sign)` energy is high and `Misdirected battle (wrong war)` is active | Expect conflicts to attach to extraneous targets; channel the “fire of battle” back toward the real developmental issue before relationships/career erode | 关系 | 凶 | 中 | `The warrior fought the wrong war.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_014` | sign_aries AND astro_misdirected_battle AND emotional_tension | The rocket fuel has to burn somewhere. If you dodge the real crisis, it explodes over a yellow shirt, and the room fills with fireworks and regret. | 例外处理 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:696` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| “Wrong war” shadow: energy attacks extraneous targets | bazi_qisha | sign_aries, astro_misdirected_battle, emotional_tension | tarot_tower | dream_conflict_tension, dream_anxiety_level |  | neutral_relationship_tension, neutral_emotional_tension |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Shadow | 阴影面 | A distorted pattern where the sign’s energy expresses in counterproductive ways. | 某种能量本来用于成长与突破，但因逃避真正课题而转向更安全/更无意义的出口，最终制造损耗。 | astro_misdirected_battle | new_candidate |

