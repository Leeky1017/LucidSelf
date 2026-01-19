## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_010`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:558`
- `source_text`:
  > The Modes
  > Everything born must die. Life teaches no more pr imary law, nor one more inviolable. An unstable
  > atom is created in a particle accelerator. In a millis econd it breaks down. So fleeting is its existence that
  > we know of it only through conjectural evidence. A child is born. Seven decades pass. An old man’s
  > body is buried in the ground. Pyramids are raised; a civilization is created in the Nile valley. Over three millennia it lives and bears its fruit. Gradually it decays. Atoms, people, cultures—what is the difference? Only time. The core features of any life cycle
  > are identical. Something is born. Something exists for measurable time in some relatively distinct form.
  > And something dies. These three archetypal phases of any life cycle constitute another essential ingredient in astrology’s symbolism: the modes.
  > The first mode is called
  > Cardinal . It refers to birth, the beginning of a cycle. Cardinality is the
  > principle of initiation. Out of nothingness, something ar ises. It is the creative push that allows fresh life
  > to manifest itself in a universe th at may already be stable and closed.
  > Once existence is achieved, life cycles move into their second phase. Astrologers call this the
  > Fixed mode. Fixity has a spirit of solidarity and continuity. While in this mode, an entity is most
  > recognizable. It is in its maturity. But fixity can also refer to stubbornness or unresponsiveness. It is the
  > antithesis of change and the quintessence of strength.
  > Such stability may endure for an instant or for an aeon, but never for eternity. Life is corrosive.
  > Bodies die. Metals rust. Civilizations become co rrupt. The final mode, which astrologers call Mutable ,
  > reigns over the ending of life cycles. Its spirit is one of change and adjustment, many times of utter
  > dissolution. Mutability has one paramount virtue: it is adaptable. It can respond to a changing
  > environment by changing its own form. The price it pa ys for this capacity is that it can lose all
  > definition, become shapeless. It can die.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Cardinal mode energy | mode_cardinal_energy | existing | 能量 | astro | mode |
| Fixed mode energy | mode_fixed_energy | existing | 能量 | astro | mode |
| Mutable mode energy | mode_mutable_energy | existing | 能量 | astro | mode |
| Modes as lifecycle phases | astro_modes_lifecycle_phases | new_candidate | 结构 | astro | framework |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_mutable_adaptation_risk` | If `Mutable mode energy` is dominant in a cycle | Emphasize adaptation and change; warn that definition can dissolve when flexibility becomes shapelessness | 心理 | 混合 | 中 | `Mutability has one paramount virtue: it is adaptable.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_010` | mode_cardinal_energy OR mode_fixed_energy OR mode_mutable_energy | A cycle is born, holds its shape, and dissolves; cardinal pushes into life, fixed consolidates, mutable adapts—until the old form finally lets go. | 主干依赖 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:558` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Modes (Cardinal/Fixed/Mutable) as life-cycle phases | birth_season | mode_cardinal_energy, mode_fixed_energy, mode_mutable_energy | tarot_wheel_of_fortune | dream_primary_pattern |  | neutral_transformation_opportunity |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Mutable (mode) | 变动模式 | The phase of a cycle oriented toward change, adjustment, and dissolution. | 生命周期的收束与变形阶段：强调适应与调整，也可能因过度流动而失去边界与定型。 | mode_mutable_energy | existing |

