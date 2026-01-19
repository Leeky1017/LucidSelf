## A - Entry Metadata

- `card_id`: `inner_sky_signs_020`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:918`
- `source_text`:
  > An automated bathysphere. Its purpose? To map the seabed four miles below the ocean’s surface. To
  > extract samples from the sediment. And to return intact to the mother ship. One strategy supersedes all others: The bathysphere must survive. The sea presses at it,
  > sounding the walls for any weakness, any flaw. In th at unmitigatedly hostile environment, defense is
  > everything. Without armor, the delicate sensing devices within the vessel would be crushed in a
  > microsecond. Yet, there must be gaps in the defens e. A solid wall of steel two feet thick would protect the ship
  > perfectly. Too perfectly. Without breaks in the ar mor, the bathysphere could not interact with the
  > environment it was designed to explore. There must be windows for the cameras. Wires must run from
  > the interior brain to the exterior eyes and ears. There must be internal storage bays for material
  > gathered from outside. The bathysphere’s designers face a diffi cult problem: if they defend the machinery too well, the
  > ship will not do the work for which it was created. And if they do not defend it well enough, the vessel will be destroyed by the environment it was designed to penetrate. It is the same with the Crab. Cancer’s “sensing devices” are the most delicate in the zodiac. No sign feels with such intensity.
  > And feeling is what life is all about for the Crab. But those emotional circuits can be overloaded. They
  > can burn out. Life must be let in slowly, in a controlled way. Simply to drop all defenses would be
  > suicidal. Cancer’s goal is to maximize the intensity of its interactions with the world, while simultaneously protecting its finely tuned emotional sensibilities. To surround them in a shell of steel
  > would allow the fragile mechanisms to endure. But li fe is more than endurance. The Crab’s strategy’ is
  > to create the minimal defenses consistent with survival. .
  > Shyness is one such defense. Especially in early life, daydreams and reticence are Cancer’s cloak.
  > The person initiates only the most barely essential in teractions with the world. A mask is worn, a mask
  > of anonymity and disinformation. Like an Apache in the desert, we can look straight at such an indi-
  > vidual and see nothing but chaparral. Later the defenses may become more so phisticated. The Crab learns to project a plausible, three-
  > dimensional hologram of a human personality into th e social arena. Perhaps even a gregarious one.
  > Within that disguise he lurks like a spy, snapping X-ray photographs, secretly penetrating the souls of
  > those around him. To wear a mask or to stand naked an d revealed: Cancer has little choice. His inner processes are
  > so delicate and life is so jarring that without insu lation his nervous system would shatter. The danger is
  > that the defenses can become too efficient, that sa fety can be put ahead of everything, even growth.
  > For the Crab to evolve he must shed his shell. But the shedding must be calculated. No one touched by this sign needs to stand on a soapbox during rush hour and pull down his psychological pants. The audience must be carefully selected and timing must be flawless. With his extreme
  > vulnerability the Crab is playing for high stakes.
  > But he must play. He must open up. He must trust. Love is always a gamble, and that is a risk
  > Cancer must learn to take.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Cancer (sign) | sign_cancer | existing | 结构 | astro | sign |
| Water element energy | element_water_energy | existing | 能量 | astro | element |
| Anxiety intensity (dream affect proxy) | dream_anxiety_level | existing | 能量 | dream | affect |
| Minimal defenses strategy | astro_minimal_defenses_strategy | new_candidate | 状态 | astro | strategy |
| Calibrated vulnerability | astro_calibrated_vulnerability | new_candidate | 状态 | astro | strategy |
| Trust-as-risk skill | astro_trust_as_risk_skill | new_candidate | 状态 | astro | relationship_skill |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_cancer_let_life_in_slowly` | If `Cancer (sign)` sensitivity is high and `Calibrated vulnerability` is pursued | Let life in slowly and intentionally; build minimal defenses that keep the system alive while still allowing contact, trust, and love | 关系 | 混合 | 高 | `Life must be let in slowly, in a controlled way.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_020` | sign_cancer AND astro_minimal_defenses_strategy AND astro_calibrated_vulnerability | Like a bathysphere, you need armor and windows. You let the ocean in through chosen openings—slowly—so you can feel without breaking. | 条件分支 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:918` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Minimal defenses + calculated opening up (trust as gamble) | bazi_zhengyin | sign_cancer, astro_minimal_defenses_strategy, astro_calibrated_vulnerability, astro_trust_as_risk_skill | tarot_suit_cups | dream_anxiety_level |  | neutral_relationship_harmony, neutral_emotional_tension |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Bathysphere | 深海探测舱 | A deep-sea vessel designed to survive pressure while still observing and sampling its environment. | 一种“既要防护又要接触”的心理隐喻：保持边界来活下去，同时留出窗口让体验进入，才有真实成长。 | common_bathysphere_metaphor | new_candidate |

