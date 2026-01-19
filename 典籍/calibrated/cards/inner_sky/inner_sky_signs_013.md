## A - Entry Metadata

- `card_id`: `inner_sky_signs_013`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:658`
- `source_text`:
  > Courage must be scared into a person. It cannot be attained through any other means. Stress and
  > courage are a matched pair. Scary situations will no t always make us braver, but we can never become
  > braver without them. Aries seeks courage. Thus, it is a magnet for stress. How the Ra m faces that stress cannot be
  > predetermined. He may respond creatively and with de termination. Or he may run like a rabbit fleeing a
  > bulldozer. All we know in advance is that the stress will be there. Crisis follows Aries like a shadow. The boldness to do exactly what one pleases is hard to attain, and the crises it creates are fierce ones, Friends are often alienated. Figures of authority may crack
  > down. Many times we must sneak up on existential cour age, practicing it first in safer, less threatening
  > ways. We are talking about adventures. Let’s imagine we are hanging by a rope halfway up the side of a sheer granite face. If the rope
  > has no internal defects and is well anchored and if we make no mistakes, we have a reasonable chance of
  > being alive that evening. In such a situation, if we are not frightened, we are stupid. Most mountain climbers, I suspect, would agree with that. Yet the mountain climber learns to control fear, to work
  > efficiently in spite of the emotional static that his sport produces. In other words, he develops courage.
  > To scale a peak takes nerve. No question there. But that is a static statement. It captures none of
  > the developmental dynamics of the process. The as trologer would express it differently. He or she
  > would say that to climb a mountain evokes courage. Natural emotions are overcome; the structure of
  > consciousness is altered. And all that is brought ab out through the classic Arian evolutionary strategy:
  > the intentional selection of a crisis. By whatever means they are attained , such transformations are the essence of growth. Mountain
  > climbing is the paradigm, but each of us chooses his own mountain. For one, it may be learning to swim.
  > For another, it may be a confrontation with an ov erbearing boss. For a third, quitting smoking may be
  > the issue. Whether or not the Ram is willing to pick up the gauntlet, life will make the identity of the
  > mountain plain enough. Then it is up to him to start climbing. The Ram wants something. Certain expe riences, usually risky, haunt it, tug at it like sunrise
  > after a long, cold night. That desire, whatever it ma y be, is hidden. It is wrapped in veils of fear. The
  > Arian strategy is to unveil the need, however fearsome it might be. And then to satisfy it, at whatever
  > price. To live in the presence of fears, but to ac t clearly and decisively anyway—that is the Ram’s art.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Aries (sign) | sign_aries | existing | 结构 | astro | sign |
| Stress / emotional tension | emotional_tension | existing | 能量 | astro | pressure |
| Fear intensity (dream affect proxy) | dream_fear_level | existing | 能量 | dream | affect |
| Intentional crisis selection | astro_intentional_crisis_selection | new_candidate | 状态 | astro | strategy |
| Courage forged through stress | astro_courage_through_stress | new_candidate | 状态 | astro | growth_mechanism |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_aries_select_crisis` | If `Intentional crisis selection` is practiced under `Aries (sign)` | Use chosen challenges to evoke courage; expect stress as the training ground (not a sign of failure) | 心理 | 混合 | 高 | `the intentional selection of a crisis.` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_013` | sign_aries AND astro_intentional_crisis_selection | You pick a mountain on purpose. Your hands shake, your gut tightens—then you climb anyway, and fear turns into usable nerve. | 条件分支 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:658` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Crisis evokes courage (chosen challenge) | bazi_qisha | sign_aries, astro_intentional_crisis_selection, emotional_tension | tarot_chariot | dream_fear_level |  | neutral_emotional_tension, neutral_authority_challenge |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Intentional selection of a crisis | 主动选取危机 | Deliberately choosing a challenge that forces growth and evokes courage. | 不是被动倒霉，而是主动把自己放进“会害怕但可承受”的局面，让勇气被逼出来并形成新能力。 | astro_intentional_crisis_selection | new_candidate |

