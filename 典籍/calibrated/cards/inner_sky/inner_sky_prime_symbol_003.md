## A - Entry Metadata

- `card_id`: `inner_sky_prime_symbol_003`
- `source_anchor`: `典籍/texts/The Inner Sky/原文/The Inner Sky.md:442`
- `source_text`:
  > Astrology’s prime symbol, the great sphe re of space that surrounds us, is a symbol of that awe
  > and reverence. We might choose to call it a symbol of God. It represents infinity and perfection,
  > timelessness and universality. Americans, Russians, Europeans, Africans—we all stand beneath the
  > same sky. Like breathing, like sex, like death, it binds us together. It reminds us of our common
  > humanity. The sky represents the vantage point deep within us from which we sit and watch, impersonally and indifferently, as our lives unfold. Close your eyes. Empty your mind. Go beyond habits, thoughts, prejudices. Feel that indefinable, vast awareness that marks you as human whether you are a Bantu tribesman or an
  > astronaut. You are experiencing the prime symbol: the undifferentiated background of consciousness
  > out of which emerges that far more fragile and arbitrary structure, the personality. We might call it our soul. But astrology is not a study of the soul. It is a study of the personality.
- `priority`: `P0`

---

## B - Factor Extraction

| factor_label | factor_id | status | factor_type | engine | role_position |
|---|---|---|---|---|---|
| Prime Symbol (Sky) | astro_prime_symbol_sky | new_candidate | 结构 | astro | symbol |
| Shared sky → common humanity | common_shared_sky_humanity | new_candidate | 关系 | common | social_bond |
| Inner witness awareness | common_inner_witness_awareness | new_candidate | 状态 | common | consciousness |
| Background consciousness (undifferentiated) | common_background_consciousness | new_candidate | 结构 | common | field |
| Personality focus (not “soul” study) | astro_personality_focus | new_candidate | 状态 | astro | interpretation_focus |

---

## C - Rule Drafts

| rule_id_draft | rule_condition | rule_conclusion | conclusion_dimension | conclusion_direction | confidence | evidence_quote |
|---|---|---|---|---|---|---|
| `rule_inner_sky_inner_witness_personality` | If `Inner witness awareness` is accessible while interpreting personality | Hold personality as a fragile structure emerging within a larger field of consciousness; observe life “impersonally and indifferently” without losing personal specificity | 心理 | 中性 | 高 | `the undifferentiated background of consciousness` |

---

## D - Narrative Snippets

| narrative_id | trigger_expr | snippet | logical_role | source_anchor |
|---|---|---|---|---|
| `ns_inner_sky_003` | common_inner_witness_awareness AND astro_personality_focus | Beneath the same sky, you watch your own life unfold like a film—quietly, impersonally—until personality feels like a small figure moving across a vast screen. | 主干 | `典籍/texts/The Inner Sky/原文/The Inner Sky.md:442` |

---

## E - Cross-System Mapping

| concept_in_book | bazi_factor_ids | astro_factor_ids | tarot_factor_ids | dream_factor_ids | psych_factor_ids | neutral_tags |
|---|---|---|---|---|---|---|
| Background consciousness vs personality | day_master | common_background_consciousness, common_inner_witness_awareness, astro_personality_focus | tarot_hermit | dream_time_context |  | neutral_emotional_harmony |

---

## F - Term Alignment

| source_term | target_term | source_definition | target_definition | factor_id | status |
|---|---|---|---|---|---|
| Personality | 人格（性格结构） | The relatively fragile, structured self that emerges within consciousness and interacts with life. | 个体在现实中运作的性格与行为结构，带着惯性与偏好，会在压力与关系里显形。 | astro_personality_focus | new_candidate |

