## A - Entry Metadata

- `card_id`: `inner_sky_signs_019`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:896`
- `source_text`:
  > The Cancer Symbol
  > The Crab. A vulnerable creature. A succulent piece of meat. The food of gulls. How can he survive?
  > What hope is there for him? He is only a morsel awaiting the predator’s mouth. To live, the Crab must grow a shell. He must grow a wall between himself and nature. He is too
  > delicate to protect himself in any other way. With this armor, the Crab endures. He is at peace with his environment. But that success holds the seeds of a perilous transformation. The Crab eats . He matures. And soon he outgrows his shell. It
  > must be shed. If he is cunning and lucky, he may li ve to grow another one. One that is larger, more
  > suited to his expanded state. But only if he is cunning and lucky.
  > Cancer Endpoint
  > Dizzied by Gemini’s spinning carousel, confused by the chaos of life on the midway, awareness now turns inward, toward its roots. To the Twins, truth is “out there” somewhere. They search the world,
  > filling the psyche with alertness and wonder. And yet th e search yields nothing. Life is more mysterious
  > than ever, more full of loose ends and undigested details. Cancer sets out in a new direction . Instead of rifling through the universe, the Crab reaches
  > tendrils of consciousness inward, probing deeply into the underpinnings of experience, pressing toward the heart. The fabric of the world to Cancer is feelings. A mammoth subjectivity animates this phase of the
  > zodiac. The terse, journalistic awareness of Gemini gi ves way to a tapestry of impressions, of personal
  > responses. There is no longer an objective unive rse. All that remains is a pattern of reactions.
  > Those who are born under the mark of the Crab have come here to penetrate dimensions of
  > inner life inaccessible to any previous sign. They a rrive fluent in the language of the deep self, the
  > language of emotion. Fascinated by the reactive, su bjective aspects of the mind, their lifeblood is a
  > protracted process of psychoanal ysis, usually self-administered.
  > To feel consciousness. To feel every nuance of life. To shed the shell of numbness that armors us
  > against this slaughterhouse of a world. All that is the Crab’s work. Cancer’s endpoint? To see the
  > hellish discord of life. To see the cauldron within. And, against all odds, against all common sense, to
  > love, trust, and accept all that existence offers.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Cancer (sign) | sign_cancer | existing | 结构 | astro | sign |
| Water element energy | element_water_energy | existing | 能量 | astro | element |
| Cardinal mode energy | mode_cardinal_energy | existing | 能量 | astro | mode |
| Protective shell defense | astro_protective_shell_defense | new_candidate | 状态 | astro | defense |
| Feelings-as-world-fabric worldview | astro_feelings_world_fabric | new_candidate | 状态 | astro | worldview |
| Inward turn toward roots | astro_inward_turn_to_roots | new_candidate | 状态 | astro | direction |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_cancer_shell_then_shed` | If `Protective shell defense` is active under `Cancer (sign)` | Build enough protection to survive sensitivity, then plan for periodic shedding: the task is to feel more without collapsing into numbness | 心理 | 混合 | 高 | `To live, the Crab must grow a shell.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_019` | sign_cancer AND astro_protective_shell_defense AND astro_inward_turn_to_roots | You grow a shell to survive the gulls, then outgrow it. The real journey starts when attention turns inward and the world becomes feelings, raw and unavoidable. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:896` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Shell defense + inward emotional exploration | water_presence | sign_cancer, element_water_energy, astro_protective_shell_defense, astro_inward_turn_to_roots | tarot_suit_cups | dream_symbol_water |  | neutral_emotional_tension, neutral_relationship_harmony |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Deep self | 深层自我 | The inner emotional and subjective layer beneath surface reactions and social masks. | 不是“想法”，而是更底层的情绪与主观体验之流；它决定你会如何被触动、如何信任、如何退缩或敞开。 | astro_inward_turn_to_roots | new_candidate |

