# Planets in Transit: Chapter 5 - Moon Transits (Complete L1+L2 v2.1)

**Author**: Robert Hand | **Publication**: 1976 | **Agent**: Text-EN-Agent | **Date**: 2025-11-29

---

## Status: ✅ COMPLETE (62 entries)

**Coverage Target**: 12 House transits + ~50 Aspect transits

**Note**: Moon transits are the fastest (~2.5 days per sign, ~2 days per house). Their effects are subtle and fleeting unless activated by longer transits.

---

## Part 1: Moon Transiting Houses (月亮过宫)

### 1. Moon in the First House (月亮过境第一宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3569-3584):
> This is a two-day period when personal and subjective considerations will override everything else. You feel a great need to belong and relate to friends or loved ones. This need turns on your emotional sensors and makes you very sensitive to the feelings and moods of people around you. You can be very emotionally giving, but also emotionally demanding if you feel inadequate. Be careful not to demand more nurturing than you can give.

**English Paraphrase**: Two-day period of personal, subjective focus. Strong need to belong and relate. Emotional sensors highly active—sensitive to others' feelings. Can be emotionally giving OR astro_demanding. Don't demand more nurturing than you can give. Objectivity difficult now.

**Complete Chinese Interpretation**: 两天的个人主观聚焦期。强烈需要归属和联系。情感感应器高度活跃——对他人感受敏感。可以很情感付出或索求。不要索求超过你能给予的滋养。客观性现在困难。

**Narrative Snippets**:
- `[ns_pit_m001]` `[trigger: moon_transit_house_1]` `[factor_trigger: astro_transit_moon AND astro_house_1]` `[role: 主干]` Two-day period of personal, subjective focus—very sensitive to others' feelings and moods. → PIT Ch5 Moon-1H
- `[ns_pit_m002]` `[trigger: moon_transit_house_1]` `[factor_trigger: astro_transit_moon AND astro_house_1]` `[role: 条件分支]` Can be emotionally giving OR demanding—don't demand more nurturing than you can give. → PIT Ch5 Moon-1H
- `[ns_pit_tm]` `[trigger: transit_moon]` `[factor_trigger: transit_moon]` `[role: 主干]` Transiting Moon moves fastest through zodiac (~2.5 days per sign), triggering brief emotional fluctuations and mood shifts. → PIT Foundation
- `[ns_pit_mn]` `[trigger: moon_needs]` `[factor_trigger: moon_needs]` `[role: 条件分支]` Moon needs represent emotional requirements, security needs, and nurturing patterns—activated when Moon transits sensitive points. → PIT Foundation
- `[ns_pit_mf]` `[trigger: moon_familiar]` `[factor_trigger: moon_familiar]` `[role: 条件分支]` Moon familiar refers to habitual emotional patterns and comfort-seeking behaviors rooted in early conditioning. → PIT Foundation
- `[ns_pit_tp]` `[trigger: transit_planet]` `[factor_trigger: transit_planet]` `[role: 主干]` Transit planet is any planet currently moving through the zodiac, activating natal points and houses it contacts. → PIT Foundation
- `[ns_pit_es]` `[trigger: state_emotional_sensitivity]` `[factor_trigger: state_emotional_sensitivity]` `[role: 效果]` State of heightened emotional sensitivity—increased awareness of and responsiveness to emotional undercurrents. → PIT Foundation
- `[ns_pit_smg]` `[trigger: state_moon_1h_giving]` `[factor_trigger: state_moon_1h_giving]` `[role: 效果]` State of emotional giving when Moon transits 1st house—nurturing outflow when feeling emotionally adequate. → PIT Foundation
- `[ns_pit_smd]` `[trigger: state_moon_1h_demanding]` `[factor_trigger: state_moon_1h_demanding]` `[role: 效果]` State of emotional demanding when Moon transits 1st house—seeking nurturing when feeling inadequate. → PIT Foundation
- `[ns_pit_sar]` `[trigger: state_automatic_reactions]` `[factor_trigger: state_automatic_reactions]` `[role: 效果]` State of automatic emotional reactions triggered by Moon transits activating conditioned patterns. → PIT Foundation
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 1st house as period of emotional self-focus and heightened sensitivity
- **Natural Attributes**:
  - Symbolism: Emotional self-awareness, subjective lens activation, nurturing needs surfacing
  - Characteristics: Personal/subjective focus, emotional sensor activation, sensitivity to moods
  - Elements: Moon (emotions, instincts, needs) + 1st House (self, personality, appearance)
- **Functional Symbolism**:
  - Emotional self-expression function
  - Mood sensitivity amplification function
  - Nurturing exchange calibration function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 1st house
  - **Enhancing Conditions**: Natal Moon strong, Cancer rising, water sign emphasis
  - **Nullifying Conditions**: Heavy Saturn/Capricorn affliction
  - **Temporal Scope**: [x] Transit layer (~2 days duration)
- **Multi-layered Interpretation**:
  - Literal: Moon enters 1st house for ~2 days
  - Symbolic: Emotional self returning to house of identity
  - Practical: Personal considerations override external demands
  - Psychological: Heightened emotional sensors, need for belonging

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Transiting Moon | 流年月亮 | Moon's current position in transit | 月亮在行运中的当前位置 | transit_moon | existing |
| Emotional Sensors | 情感感应器 | Heightened awareness of others' moods | 对他人情绪的敏锐觉察 | state_emotional_sensitivity | new_candidate |
| Nurturing Exchange | 滋养交换 | Balance of giving/receiving emotional care | 情感照顾的给予/接受平衡 | pattern_nurturing_exchange | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Transiting Moon | transit_moon | existing | Planet | Current position | astro_calculator | Emotional energy |
| Structure | First House | house_1 | existing | House | Ascendant-based | astro_calculator | Self/personality |
| Temporal | Transit Duration | transit_duration_moon_house | existing | Parameter | ~2 days | astro_calculator | Fast cycle |
| State | Subjective Focus | state_moon_1h_subjective | new_candidate | Effect | High | astro_semantic | Transit effect |
| State | Emotional Sensitivity | state_moon_1h_sensitive | new_candidate | Effect | Enhanced | astro_semantic | Transit effect |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m001 | planet_house | astro_transit_moon | astro_house_1 | Moon transits 1H | When transit Moon enters 1st house heightening emotional self-awareness and sensitivity | emotional_focus | PIT Ch5 Moon-1H |
| rel_pit_m002 | sensitivity | transit_moon | state_emotional_sensitivity | Sensor activation | When Moon in 1H amplifies receptivity to environment and others' moods | amplifying | PIT Ch5 Moon-1H |
| rel_pit_m003 | exchange | state_moon_1h_giving | state_moon_1h_demanding | Nurturing balance | When feeling emotionally inadequate shifts balance between giving and demanding | variable | PIT Ch5 Moon-1H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m001 | "personal and subjective considerations override" | transit_moon, house_1 | Moon=subjective + 1H=self → personal focus | Moon 1H = subjective priority | High | ✅ | rule_moon_1h_subjective |
| evi_pit_m002 | "very sensitive to feelings and moods of people" | transit_moon, house_1, state_emotional_sensitivity | Moon=emotions + 1H=sensors → heightened sensitivity | Moon 1H = mood sensitivity | High | ✅ | rule_moon_1h_sensitive |
| evi_pit_m003 | "don't demand more nurturing than you can give" | transit_moon, house_1, pattern_nurturing_exchange | Emotional need → balance requirement | Moon 1H = nurturing equilibrium needed | Medium | ✅ | rule_moon_1h_nurturing |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_emotional_self | Emotional self-awareness activation | 印星透出 | transit_moon house_1 | mirror_self_symbol | emotional_attunement | Personal emotional focus |
| concept_mood_sensitivity | Heightened sensitivity to emotional environment | 偏印敏感 | moon_aspects | empathy_symbol | emotional_contagion | Sensor activation |
| concept_nurturing_balance | Give-receive emotional equilibrium | 印比平衡 | moon_venus | feeding_symbol | attachment_needs | Don't over-demand |
<!-- L2.5_END -->

---

### 2. Moon in the Second House (月亮过境第二宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3585-3605):
> You emotionally identify with your possessions or whatever you value. This can lead to strong attachment and possessiveness. You may unconsciously identify with your value system so that every challenge feels like a challenge to yourself. You probably feel best when surrounded by familiar objects that hold memories from your past. Traditionally a bad time to spend money—attitudes toward possessions are conditioned by unconscious drives.

**English Paraphrase**: Emotionally identify with possessions and values. Strong attachment, possessiveness. Challenges to values feel personal. Prefer familiar objects with memories. Bad time to spend money—unconscious drives influence decisions.

**Complete Chinese Interpretation**: 情感上与财产和价值观认同。强烈依附，占有欲。对价值观的挑战感觉像人身攻击。喜欢带有记忆的熟悉物品。不是花钱的好时候——无意识驱动影响决定。

**Narrative Snippets**:
- `[ns_pit_m003]` `[trigger: moon_transit_house_2]` `[factor_trigger: astro_transit_moon AND astro_house_2]` `[role: 主干]` Emotionally identify with possessions—strong attachment, every challenge to values feels personal. → PIT Ch5 Moon-2H
- `[ns_pit_m004]` `[trigger: moon_transit_house_2]` `[factor_trigger: astro_transit_moon AND astro_house_2]` `[role: 条件分支]` Bad time to spend money—unconscious drives condition purchasing decisions. → PIT Ch5 Moon-2H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 2nd house as emotional identification with possessions/values
- **Natural Attributes**:
  - Symbolism: Value-emotion fusion, possession attachment, security through material
  - Characteristics: Possessiveness, value-identity fusion, memory-object connection
  - Elements: Moon (emotions, security) + 2nd House (values, possessions, self-worth)
- **Functional Symbolism**:
  - Emotional value assessment function
  - Security-possession linkage function
  - Unconscious spending trigger function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 2nd house
  - **Enhancing Conditions**: Natal Moon in earth signs, strong 2H planets
  - **Nullifying Conditions**: Detached aspects (Uranus, Aquarius emphasis)
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Value-Identity Fusion | 价值认同融合 | Unconscious identification of self with values | 自我与价值观的无意识认同 | state_value_identity_fusion | new_candidate |
| Possession Attachment | 财产依附 | Emotional bonding with material objects | 与物质对象的情感绑定 | state_possession_attachment | new_candidate |
| Unconscious Spending | 无意识消费 | Purchases driven by emotional needs | 由情感需求驱动的购买行为 | pattern_unconscious_spending | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Second House | house_2 | existing | House | Post-Ascendant | astro_calculator | Values house |
| State | Possessiveness | state_moon_2h_possessive | new_candidate | Effect | Enhanced | astro_semantic | Transit effect |
| State | Value Challenge Sensitivity | state_moon_2h_value_sensitive | new_candidate | Effect | High | astro_semantic | Personal reaction |
| Boundary | Spending Threshold | boundary_moon_2h_spending | new_candidate | Warning | Avoid purchases | astro_rule_engine | Traditional advice |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m004 | planet_house | astro_transit_moon | astro_house_2 | Moon transits 2H | When transit Moon enters 2nd house activating emotional attachment to possessions and values | possessive_focus | PIT Ch5 Moon-2H |
| rel_pit_m005 | identification | transit_moon | value_system | Emotional fusion | When Moon in 2H creates emotional identification with material security | intensifying | PIT Ch5 Moon-2H |
| rel_pit_m006 | caution | transit_moon | spending_decision | Unconscious influence | When unconscious emotional needs influence spending decisions during Moon 2H | restrictive | PIT Ch5 Moon-2H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m004 | "emotionally identify with your possessions" | transit_moon, house_2 | Moon=emotions + 2H=possessions → attachment | Moon 2H = possession identification | High | ✅ | rule_moon_2h_possessive |
| evi_pit_m005 | "every challenge feels like a challenge to yourself" | transit_moon, house_2, value_system | Value=self → challenge=personal attack | Moon 2H = value-self fusion | High | ✅ | rule_moon_2h_value_sensitive |
| evi_pit_m006 | "bad time to spend money" | transit_moon, house_2, pattern_unconscious_spending | Unconscious drives → irrational purchase | Moon 2H = avoid spending | Medium | ✅ | rule_moon_2h_no_spending |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_possession_security | Security through material possession | 财库 | transit_moon house_2 | treasure_symbol | object_relations | Emotional-material link |
| concept_value_identity | Values as self-definition | 正财格 | moon_2h, venus | money_symbol | self_worth | Challenge = personal attack |
| concept_unconscious_consumption | Emotionally driven purchases | 财星被冲 | moon_square_2h_ruler | shopping_symbol | retail_therapy | Unconscious spending pattern |
<!-- L2.5_END -->

---

### 3. Moon in the Third House (月亮过境第三宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3606-3624):
> Communications with others are very subjective, colored by personal considerations, not always factually accurate. But you're concerned with "gut" level communication—matters of great importance communicated through feelings. Your casual conversations have emotional depth that can make them very important. Danger: thinking influenced by past experiences and automatic reactions. Be careful not to make bad impressions through automatic reactions.

**English Paraphrase**: Subjective communications, not always accurate. Concerned with gut-level, emotional communication. Casual conversations gain depth. Danger: thinking influenced by past, automatic reactions. May make bad impressions through autopilot behavior.

**Complete Chinese Interpretation**: 主观的沟通，不总是准确。关注内心层面的情感交流。随意对话获得深度。危险：思维受过去影响，自动反应。可能因自动驾驶行为留下坏印象。

**Narrative Snippets**:
- `[ns_pit_m005]` `[trigger: moon_transit_house_3]` `[factor_trigger: astro_transit_moon AND astro_house_3]` `[role: 主干]` Communications very subjective—but concerned with gut-level emotional communication. Casual conversations gain depth. → PIT Ch5 Moon-3H
- `[ns_pit_m006]` `[trigger: moon_transit_house_3]` `[factor_trigger: astro_transit_moon AND astro_house_3]` `[role: 条件分支]` Danger: automatic reactions from past conditioning. May make bad impressions. → PIT Ch5 Moon-3H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 3rd house as subjective/emotional communication period
- **Natural Attributes**:
  - Symbolism: Gut-level communication, emotional depth in daily exchanges, conditioned reactions
  - Characteristics: Subjective thinking, emotional conversations, automatic responses
  - Elements: Moon (emotions, instincts) + 3rd House (communication, siblings, short journeys)
- **Functional Symbolism**:
  - Emotional communication enhancement function
  - Conditioned reaction activation function
  - Casual-to-deep conversation transformation function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 3rd house
  - **Enhancing Conditions**: Water Mercury, Cancer/Pisces 3H
  - **Nullifying Conditions**: Strong air emphasis, detached Mercury
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Gut-level Communication | 内心层面沟通 | Communication through feelings rather than facts | 通过感受而非事实的沟通 | pattern_gut_communication | new_candidate |
| Automatic Reactions | 自动反应 | Unconscious responses conditioned by past | 由过去条件化的无意识反应 | state_automatic_reactions | new_candidate |
| Subjective Thinking | 主观思维 | Thought colored by personal feelings | 被个人感受着色的思维 | state_subjective_thinking | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Third House | house_3 | existing | House | Communication | astro_calculator | Sibling/exchange house |
| State | Subjective Communication | state_moon_3h_subjective | new_candidate | Effect | High | astro_semantic | Transit effect |
| State | Emotional Depth | state_moon_3h_depth | new_candidate | Effect | Enhanced | astro_semantic | Conversation quality |
| Boundary | Automatic Reaction Danger | boundary_moon_3h_automatic | new_candidate | Warning | Self-awareness needed | astro_rule_engine | Impression risk |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m007 | planet_house | astro_transit_moon | astro_house_3 | Moon transits 3H | When transit Moon enters 3rd house coloring communication with emotional subjectivity | subjective_comm | PIT Ch5 Moon-3H |
| rel_pit_m008 | enhancement | transit_moon | casual_conversation | Depth added | When Moon in 3H adds emotional depth to normally superficial exchanges | deepening | PIT Ch5 Moon-3H |
| rel_pit_m009 | caution | state_automatic_reactions | impression | Unconscious impact | When automatic emotional reactions during Moon 3H create unintended impressions | negative | PIT Ch5 Moon-3H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m007 | "communications very subjective, not always accurate" | transit_moon, house_3 | Moon=subjective + 3H=communication → biased exchange | Moon 3H = subjective communication | High | ✅ | rule_moon_3h_subjective |
| evi_pit_m008 | "gut level communication" | transit_moon, house_3, pattern_gut_communication | Emotional depth in exchange | Moon 3H = emotional conversation | High | ✅ | rule_moon_3h_gut |
| evi_pit_m009 | "automatic reactions...bad impressions" | transit_moon, house_3, state_automatic_reactions | Past conditioning → uncontrolled response | Moon 3H = reaction awareness needed | Medium | ✅ | rule_moon_3h_caution |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_emotional_communication | Feeling-based information exchange | 食伤泄秀 | transit_moon house_3 | speaking_symbol | affective_communication | Gut-level expression |
| concept_conditioned_response | Automatic patterns from past | 偏印夺食 | moon_saturn_aspect | robot_symbol | conditioning | Past-programmed reactions |
| concept_subjective_perception | Personal filter on information | 印星遮官 | moon_mercury | glasses_symbol | cognitive_bias | Not factually accurate |
<!-- L2.5_END -->

---

### 4. Moon in the Fourth House (月亮过境第四宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3625-3647):
> Good time to retire to your own private place. You seek comfort from outside world demands. Good time to go inside yourself and look at attitudes, feelings, emotional orientation. You may become aware of how habits and past conditioning control your life now. You will probably feel emotionally more possessive—strong fear of being alone or alienated makes you hold on tightly. But holding on leads to losing.

**English Paraphrase**: Good time to retire to private space. Seek comfort from outside demands. Look inside—examine attitudes, feelings. May realize how habits/conditioning control you now. Emotionally possessive—fear of being alone makes you hold tight, but this causes loss.

**Complete Chinese Interpretation**: 退回私人空间的好时机。寻求外界要求的慰藉。向内看——检视态度、感受。可能意识到习惯/条件反射如何控制你。情感上占有欲强——害怕独处使你紧握，但这导致失去。

**Narrative Snippets**:
- `[ns_pit_m007]` `[trigger: moon_transit_house_4]` `[factor_trigger: astro_transit_moon AND astro_house_4]` `[role: 主干]` Good time to retire to private space—look inside, examine attitudes and feelings. → PIT Ch5 Moon-4H
- `[ns_pit_m008]` `[trigger: moon_transit_house_4]` `[factor_trigger: astro_transit_moon AND astro_house_4]` `[role: 条件分支]` May realize how past conditioning controls you. Holding on too tight leads to losing. → PIT Ch5 Moon-4H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 4th house as private retreat and inner examination period
- **Natural Attributes**:
  - Symbolism: Private sanctuary, inner reflection, conditioning awareness, attachment dynamics
  - Characteristics: Withdrawal to private space, introspection, possessiveness from insecurity
  - Elements: Moon (emotions, home, mother) + 4th House (home, roots, inner foundation)
- **Functional Symbolism**:
  - Private retreat function (Moon in its natural house)
  - Conditioning awareness activation function
  - Attachment-loss paradox illumination function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 4th house
  - **Enhancing Conditions**: Cancer IC, strong natal Moon, water emphasis
  - **Nullifying Conditions**: Heavy Capricorn/Saturn affliction to 4H
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Private Retreat | 私人退隐 | Withdrawal to inner sanctuary for comfort | 退回内心庇护所寻求慰藉 | state_private_retreat | new_candidate |
| Conditioning Awareness | 条件反射觉察 | Recognizing how past habits control present | 认识到过去习惯如何控制现在 | state_conditioning_awareness | new_candidate |
| Attachment Paradox | 依附悖论 | Holding tight leads to losing | 紧握导致失去 | pattern_attachment_paradox | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Fourth House | house_4 | existing | House | IC-based | astro_calculator | Home/roots house |
| State | Private Retreat | state_moon_4h_retreat | new_candidate | Effect | Recommended | astro_semantic | Moon in natural house |
| State | Possessiveness | state_moon_4h_possessive | new_candidate | Effect | Risk | astro_semantic | Fear-based holding |
| Pattern | Holding-Losing Paradox | pattern_moon_4h_paradox | new_candidate | Dynamic | Psychological | astro_rule_engine | Attachment trap |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m010 | planet_house | astro_transit_moon | astro_house_4 | Moon transits 4H | When transit Moon enters 4th house (natural domicile) deepening introspection | introspective | PIT Ch5 Moon-4H |
| rel_pit_m011 | awareness | transit_moon | past_conditioning | Recognition trigger | When Moon in 4H brings childhood conditioning patterns to conscious awareness | illuminating | PIT Ch5 Moon-4H |
| rel_pit_m012 | paradox | holding_tight | losing | Inverse relationship | When fear-based clinging during Moon 4H paradoxically accelerates loss | cautionary | PIT Ch5 Moon-4H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m010 | "good time to retire to your own private place" | transit_moon, house_4 | Moon=home + 4H=private → retreat recommended | Moon 4H = private retreat | High | ✅ | rule_moon_4h_retreat |
| evi_pit_m011 | "aware of how habits and past conditioning control" | transit_moon, house_4, state_conditioning_awareness | 4H=roots + Moon=habits → conditioning visible | Moon 4H = conditioning insight | High | ✅ | rule_moon_4h_awareness |
| evi_pit_m012 | "holding on leads to losing" | transit_moon, house_4, pattern_attachment_paradox | Fear → hold → lose | Moon 4H = release paradox | High | ✅ | rule_moon_4h_release |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_inner_sanctuary | Safe retreat for self-examination | 日主归禄 | transit_moon house_4 | home_symbol | regression_service_ego | Moon in natural house |
| concept_conditioning_visible | Past programming becomes conscious | 偏印主事 | moon_ic | memory_symbol | psychoanalytic_insight | Habits control awareness |
| concept_attachment_trap | Holding tight creates loss | 印星过旺夺食 | moon_saturn_square | cage_symbol | anxious_attachment | Paradox illumination |
<!-- L2.5_END -->

---

### 5. Moon in the Fifth House (月亮过境第五宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3648-3666):
> Very difficult to conceal your feelings from others—and you shouldn't try. You need to be yourself now and feel what you really are. In love relationships, greater emotional depth and intensity. Watch excessive possessiveness or being wrapped up in your own feelings. Relations with women generally improved. May arouse protective and nurturing instincts toward children or loved ones. Don't let protection deprive someone of individual responsibility.

**English Paraphrase**: Can't conceal feelings—don't try. Need to be yourself. Love relationships gain emotional depth and intensity. Watch possessiveness. Relations with women improved. Protective/nurturing instincts aroused. Don't overprotect.

**Complete Chinese Interpretation**: 无法隐藏感受——不要尝试。需要做自己。爱情关系获得情感深度和强度。注意占有欲。与女性关系改善。保护/养育本能被唤醒。不要过度保护。

**Narrative Snippets**:
- `[ns_pit_m009]` `[trigger: moon_transit_house_5]` `[factor_trigger: astro_transit_moon AND astro_house_5]` `[role: 主干]` Can't conceal feelings—need to be yourself. Love relationships gain depth and intensity. → PIT Ch5 Moon-5H
- `[ns_pit_m010]` `[trigger: moon_transit_house_5]` `[factor_trigger: astro_transit_moon AND astro_house_5]` `[role: 条件分支]` Protective instincts aroused—don't overprotect or deprive others of responsibility. → PIT Ch5 Moon-5H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 5th house as emotional authenticity and creative expression period
- **Natural Attributes**:
  - Symbolism: Emotional transparency, love depth, protective nurturing, creative feelings
  - Characteristics: Cannot conceal feelings, relationship intensity, nurturing instincts
  - Elements: Moon (emotions, nurturing) + 5th House (creativity, romance, children)
- **Functional Symbolism**:
  - Emotional authenticity enforcement function
  - Love relationship intensification function
  - Protective instinct activation function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 5th house
  - **Enhancing Conditions**: Leo Moon, strong Venus, children in chart
  - **Nullifying Conditions**: Heavy Saturn affliction to 5H
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Emotional Transparency | 情感透明 | Inability/unwillingness to hide feelings | 无法/不愿隐藏感受 | state_emotional_transparency | new_candidate |
| Protective Instinct | 保护本能 | Nurturing drive toward vulnerable others | 对弱者的养育驱动 | state_protective_instinct | new_candidate |
| Overprotection Risk | 过度保护风险 | Protection that removes others' responsibility | 剥夺他人责任的保护 | boundary_overprotection | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Fifth House | house_5 | existing | House | Leo natural | astro_calculator | Creativity/romance |
| State | Emotional Authenticity | state_moon_5h_authentic | new_candidate | Effect | Required | astro_semantic | Can't hide feelings |
| State | Love Intensity | state_moon_5h_love_intense | new_candidate | Effect | Enhanced | astro_semantic | Relationship depth |
| Boundary | Overprotection Limit | boundary_moon_5h_protect | new_candidate | Warning | Balance needed | astro_rule_engine | Don't deprive responsibility |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m013 | planet_house | astro_transit_moon | astro_house_5 | Moon transits 5H | When transit Moon enters 5th house seeking emotional expression through creativity and love | expressive | PIT Ch5 Moon-5H |
| rel_pit_m014 | intensification | transit_moon | love_relationship | Emotional depth | When Moon in 5H intensifies emotional depth in romantic connections | enhancing | PIT Ch5 Moon-5H |
| rel_pit_m015 | caution | protective_instinct | individual_responsibility | Balance needed | When protective instinct toward children must balance with their independence | limiting | PIT Ch5 Moon-5H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m013 | "very difficult to conceal your feelings" | transit_moon, house_5 | 5H=expression + Moon=feelings → transparency | Moon 5H = emotional visibility | High | ✅ | rule_moon_5h_transparent |
| evi_pit_m014 | "love relationships, greater emotional depth" | transit_moon, house_5, love_relationship | 5H=romance + Moon=emotion → intensity | Moon 5H = love deepening | High | ✅ | rule_moon_5h_love |
| evi_pit_m015 | "don't let protection deprive someone of responsibility" | transit_moon, house_5, boundary_overprotection | Protect → over-protect → harm | Moon 5H = balanced protection | Medium | ✅ | rule_moon_5h_protect_balance |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_emotional_authenticity | Being true to feelings | 食神透出 | transit_moon house_5 | stage_symbol | genuine_self | Can't hide |
| concept_love_intensity | Deepened romantic feelings | 桃花旺 | moon_venus_5h | heart_symbol | romantic_attachment | Relationship depth |
| concept_protective_balance | Nurture without disempowering | 印星生比劫 | moon_5h_children | shield_symbol | good_enough_parent | Don't over-protect |
<!-- L2.5_END -->

---

### 6. Moon in the Sixth House (月亮过境第六宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3667-3687):
> Inclined to put emotional considerations second to immediate necessities. Contradictory energy—Moon's need for personal contact conflicts with sixth house self-denial. Emotional repression is probable. Can signify attention to home crafts, personal hygiene, home care, reorganization. If emotional repression, may become hypercritical or play the "martyr game." Better to put feelings on the line. May occupy attention with personal health—don't become hypochondriac.

**English Paraphrase**: Put emotions second to necessities. Contradictory—Moon's needs vs 6H self-denial. Emotional repression probable. Good for home crafts, hygiene, reorganization. Repression → hypercritical or martyr games. Better to express feelings. Health focus—don't become hypochondriac.

**Complete Chinese Interpretation**: 把情感放在必需之后。矛盾——月亮的需求vs第六宫自我否定。情感压抑可能。适合家务、卫生、重组。压抑→过度批评或殉道游戏。最好表达感受。健康关注——不要变成疑病症。

**Narrative Snippets**:
- `[ns_pit_m011]` `[trigger: moon_transit_house_6]` `[factor_trigger: astro_transit_moon AND astro_house_6]` `[role: 主干]` Put emotions second to necessities—contradictory energy, emotional repression probable. → PIT Ch5 Moon-6H
- `[ns_pit_m012]` `[trigger: moon_transit_house_6]` `[factor_trigger: astro_transit_moon AND astro_house_6]` `[role: 条件分支]` May become hypercritical or play martyr game. Better to express feelings directly. → PIT Ch5 Moon-6H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 6th house as emotional-practical conflict and service orientation
- **Natural Attributes**:
  - Symbolism: Emotional repression, duty vs needs, service orientation, health consciousness
  - Characteristics: Emotions second to necessities, contradictory energy, potential hypercriticism
  - Elements: Moon (emotions, needs) + 6th House (service, health, daily work, self-denial)
- **Functional Symbolism**:
  - Emotional-practical priority conflict function
  - Service orientation activation function
  - Health attention trigger function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 6th house
  - **Enhancing Conditions**: Virgo Moon, strong Mercury, service-oriented chart
  - **Nullifying Conditions**: Strong fire/Leo emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Emotional Repression | 情感压抑 | Suppressing feelings for duty/necessity | 为责任/必需压抑感受 | state_emotional_repression | new_candidate |
| Martyr Game | 殉道游戏 | Acting self-sacrificing to manipulate | 表演自我牺牲以操控他人 | pattern_martyr_game | new_candidate |
| Hypercriticism | 过度批评 | Excessive criticism as repression outlet | 过度批评作为压抑出口 | state_hypercritical | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Sixth House | house_6 | existing | House | Virgo natural | astro_calculator | Service/health house |
| State | Emotional Repression | state_moon_6h_repression | new_candidate | Effect | Risk | astro_semantic | Moon vs 6H conflict |
| State | Service Mode | state_moon_6h_service | new_candidate | Effect | Active | astro_semantic | Duty orientation |
| Boundary | Hypochondria Risk | boundary_moon_6h_health | new_candidate | Warning | Balance needed | astro_rule_engine | Health over-focus |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m016 | planet_house | astro_transit_moon | astro_house_6 | Moon transits 6H | When transit Moon enters 6th house creating tension between emotional needs and duty | contradictory | PIT Ch5 Moon-6H |
| rel_pit_m017 | conflict | moon_needs | sixth_house_denial | Personal vs service | When Moon emotional needs conflict with 6th house self-denial requirement | tension | PIT Ch5 Moon-6H |
| rel_pit_m018 | outlet | emotional_repression | hypercriticism | Displaced expression | When repressed emotions during Moon 6H emerge as hypercriticism or martyrdom | negative | PIT Ch5 Moon-6H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m016 | "emotional considerations second to necessities" | transit_moon, house_6 | 6H=duty + Moon=emotions → priority conflict | Moon 6H = emotions deprioritized | High | ✅ | rule_moon_6h_duty_first |
| evi_pit_m017 | "contradictory energy—Moon's need conflicts with self-denial" | transit_moon, house_6, state_emotional_repression | Personal needs vs service → inner conflict | Moon 6H = internal contradiction | High | ✅ | rule_moon_6h_conflict |
| evi_pit_m018 | "hypercritical or martyr game" | transit_moon, house_6, pattern_martyr_game | Repression → displacement → criticism/martyrdom | Moon 6H = expression warning | Medium | ✅ | rule_moon_6h_express |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_duty_vs_needs | Service orientation vs personal needs | 官星制身 | transit_moon house_6 | servant_symbol | superego_conflict | Contradictory energy |
| concept_emotional_displacement | Repressed feelings emerging indirectly | 印星克食伤 | moon_saturn_6h | mask_symbol | displacement_defense | Hypercriticism/martyrdom |
| concept_health_focus | Attention to physical wellbeing | 偏印主健康 | moon_6h_health | body_symbol | somatization | Don't over-focus |
<!-- L2.5_END -->

---

### 7. Moon in the Seventh House (月亮过境第七宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3688-3707):
> Turn attention to most personal relationships with more emotional expression than usual. Affects marriage, opponents, any emotional confrontation. Loved ones provide security and support—and you want to provide these for them too. If in negative emotional state, may become excessively jealous and possessive or act unconsciously with loved ones. Conflicts more emotional, difficult to maintain detachment. Opponents can manipulate by controlling your feelings. Look upon confrontations as opportunity to see unconscious parts of yourself.

**English Paraphrase**: Attention to personal relationships, more emotional. Marriage, opponents, emotional confrontations affected. Loved ones provide security—you want to provide too. Negative state → jealous, possessive, unconscious. Conflicts emotional, hard to detach. Opponents can manipulate your feelings. Confrontations reveal unconscious self.

**Complete Chinese Interpretation**: 关注个人关系，更情绪化。婚姻、对手、情感对抗受影响。爱人提供安全——你也想提供。负面状态→嫉妒、占有、无意识。冲突情绪化，难以超脱。对手可以操控你的感受。对抗揭示无意识自我。

**Narrative Snippets**:
- `[ns_pit_m013]` `[trigger: moon_transit_house_7]` `[factor_trigger: astro_transit_moon AND astro_house_7]` `[role: 主干]` Attention to personal relationships—more emotional than usual. Loved ones provide security. → PIT Ch5 Moon-7H
- `[ns_pit_m014]` `[trigger: moon_transit_house_7]` `[factor_trigger: astro_transit_moon AND astro_house_7]` `[role: 条件分支]` Negative state → jealous, possessive. Opponents can manipulate your feelings. Confrontations reveal unconscious self. → PIT Ch5 Moon-7H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 7th house as relationship emotional intensification period
- **Natural Attributes**:
  - Symbolism: Partnership emotions, security through others, confrontation as mirror
  - Characteristics: Emotional relationships, security exchange, vulnerability to manipulation
  - Elements: Moon (emotions, security) + 7th House (partnerships, marriage, open enemies)
- **Functional Symbolism**:
  - Relationship emotional activation function
  - Security-through-partnership seeking function
  - Shadow projection through confrontation function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 7th house
  - **Enhancing Conditions**: Libra Moon, strong Venus, partnership emphasis
  - **Nullifying Conditions**: Strong Aries/1H emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Relationship Emotionality | 关系情绪化 | Heightened emotional investment in partnerships | 对伴侣关系的情感投入增强 | state_relationship_emotional | new_candidate |
| Emotional Manipulation | 情感操控 | Using feelings to control others | 利用感受控制他人 | pattern_emotional_manipulation | new_candidate |
| Confrontation Mirror | 对抗镜像 | Seeing unconscious self through conflict | 通过冲突看到无意识自我 | pattern_confrontation_mirror | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Seventh House | house_7 | existing | House | Libra natural | astro_calculator | Partnership house |
| State | Partnership Focus | state_moon_7h_partnership | new_candidate | Effect | Enhanced | astro_semantic | Relationship attention |
| State | Jealousy Risk | state_moon_7h_jealousy | new_candidate | Effect | Conditional | astro_semantic | Negative emotional state |
| Pattern | Shadow Projection | pattern_moon_7h_shadow | new_candidate | Dynamic | Psychological | astro_rule_engine | Confrontation insight |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m019 | planet_house | astro_transit_moon | astro_house_7 | Moon transits 7H | When transit Moon enters 7th house focusing emotional needs on partnerships | relational | PIT Ch5 Moon-7H |
| rel_pit_m020 | vulnerability | transit_moon | opponent_manipulation | Emotional exposure | When emotional openness in Moon 7H creates vulnerability to manipulation | risk | PIT Ch5 Moon-7H |
| rel_pit_m021 | insight | confrontation | unconscious_self | Mirror function | When others mirror unconscious aspects of self during Moon 7H confrontations | revealing | PIT Ch5 Moon-7H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m019 | "attention to most personal relationships" | transit_moon, house_7 | 7H=partnerships + Moon=emotions → relationship focus | Moon 7H = partnership emotionality | High | ✅ | rule_moon_7h_relationship |
| evi_pit_m020 | "opponents can manipulate by controlling your feelings" | transit_moon, house_7, pattern_emotional_manipulation | Emotional openness → vulnerability | Moon 7H = manipulation risk | Medium | ✅ | rule_moon_7h_manipulation |
| evi_pit_m021 | "confrontations as opportunity to see unconscious parts" | transit_moon, house_7, pattern_confrontation_mirror | Conflict → projection → self-insight | Moon 7H = shadow work opportunity | High | ✅ | rule_moon_7h_shadow |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_partnership_emotions | Emotional investment in relationships | 官星合身 | transit_moon house_7 | partner_symbol | attachment_style | Security through others |
| concept_emotional_vulnerability | Openness to manipulation | 官星被冲 | moon_opposition_asc | enemy_symbol | emotional_dysregulation | Opponent exploitation |
| concept_shadow_mirror | Others reflecting unconscious self | 劫财见官 | moon_7h_opposition | mirror_symbol | projection_mechanism | Confrontation insight |
<!-- L2.5_END -->

---

### 8. Moon in the Eighth House (月亮过境第八宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3708-3724):
> Emotional experiences much more intense than usual. Drawn to intense or powerful people who have strong effect on you. Through emotional encounters, you experience moods and feelings quite different from your "normal" self. May feel effects like second house (possessiveness) but with added danger of conflict over joint possessions. You may desire something that belongs to someone else or greater control over shared things. Recognize that attachment serves no real purpose and is potential source of trouble.

**English Paraphrase**: Emotional experiences intense. Drawn to powerful people with strong effect. Experience unusual moods through encounters. Second house effects (possessiveness) plus conflict over joint possessions. May desire others' things or control over shared things. Recognize attachment is trouble source.

**Complete Chinese Interpretation**: 情感体验强烈。被有强烈影响的强大人物吸引。通过遭遇体验不寻常的情绪。第二宫效果（占有欲）加上共同财产冲突。可能想要他人的东西或对共享事物的控制。认识到依附是麻烦来源。

**Narrative Snippets**:
- `[ns_pit_m015]` `[trigger: moon_transit_house_8]` `[factor_trigger: astro_transit_moon AND astro_house_8]` `[role: 主干]` Emotional experiences much more intense—drawn to powerful people. Experience unusual moods. → PIT Ch5 Moon-8H
- `[ns_pit_m016]` `[trigger: moon_transit_house_8]` `[factor_trigger: astro_transit_moon AND astro_house_8]` `[role: 条件分支]` Conflict danger over joint possessions. Recognize attachment serves no real purpose. → PIT Ch5 Moon-8H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 8th house as emotional intensity and transformation period
- **Natural Attributes**:
  - Symbolism: Emotional intensity, power dynamics, shared resources, transformation through crisis
  - Characteristics: Intense experiences, attraction to powerful people, unusual moods
  - Elements: Moon (emotions, needs) + 8th House (death/rebirth, shared resources, intimacy)
- **Functional Symbolism**:
  - Emotional intensity amplification function
  - Power-attraction activation function
  - Attachment-trouble awareness function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 8th house
  - **Enhancing Conditions**: Scorpio Moon, strong Pluto, water emphasis
  - **Nullifying Conditions**: Strong Taurus/2H emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Emotional Intensity | 情感强度 | Heightened depth and power of feelings | 感受的深度和力量增强 | state_emotional_intensity | new_candidate |
| Power Attraction | 权力吸引 | Being drawn to powerful/intense people | 被有力量/强烈的人吸引 | pattern_power_attraction | new_candidate |
| Attachment Awareness | 依附觉察 | Recognizing attachment as trouble source | 认识到依附是麻烦来源 | state_attachment_awareness | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Eighth House | house_8 | existing | House | Scorpio natural | astro_calculator | Transformation house |
| State | Intense Emotions | state_moon_8h_intense | new_candidate | Effect | High | astro_semantic | Amplified feelings |
| State | Unusual Moods | state_moon_8h_unusual | new_candidate | Effect | Active | astro_semantic | Different from normal |
| Boundary | Joint Possession Conflict | boundary_moon_8h_shared | new_candidate | Warning | Danger zone | astro_rule_engine | Shared resource tension |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m022 | planet_house | astro_transit_moon | astro_house_8 | Moon transits 8H | When transit Moon enters 8th house intensifying emotional depth and power dynamics | intensifying | PIT Ch5 Moon-8H |
| rel_pit_m023 | attraction | transit_moon | powerful_people | Draw to intensity | When Moon in 8H creates magnetic attraction to powerful or intense individuals | magnetic | PIT Ch5 Moon-8H |
| rel_pit_m024 | warning | attachment | trouble | Recognition needed | When emotional attachments formed during Moon 8H may lead to complications | cautionary | PIT Ch5 Moon-8H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m022 | "emotional experiences much more intense" | transit_moon, house_8 | 8H=intensity + Moon=emotions → amplification | Moon 8H = intense emotions | High | ✅ | rule_moon_8h_intense |
| evi_pit_m023 | "drawn to intense or powerful people" | transit_moon, house_8, pattern_power_attraction | 8H=power + Moon=attraction → magnetic draw | Moon 8H = power attraction | High | ✅ | rule_moon_8h_power |
| evi_pit_m024 | "attachment serves no real purpose" | transit_moon, house_8, state_attachment_awareness | Possessiveness → conflict → trouble | Moon 8H = release attachment | Medium | ✅ | rule_moon_8h_release |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_emotional_intensity | Amplified feeling depth | 七杀透出 | transit_moon house_8 | deep_water_symbol | emotional_flooding | Intense experiences |
| concept_power_magnetism | Attraction to powerful others | 官杀混杂 | moon_pluto | powerful_figure_symbol | charisma_sensitivity | Drawn to intensity |
| concept_attachment_release | Recognizing futility of clinging | 财星入墓 | moon_8h_saturn | letting_go_symbol | object_loss | Attachment as trouble |
<!-- L2.5_END -->

---

### 9. Moon in the Ninth House (月亮过境第九宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3727-3744):
> Strong urge to get away from daily routine, not entirely conscious of reasons. It's a mood, a restlessness hard to pin down. Contradiction: Moon clings to familiar while ninth house takes you away. Travel beneficial if break isn't too radical—you're not interested in getting totally away, just bored with everyday life. Study or mental journeys may be more useful—remain in familiar surroundings while exposed to revolutionary and liberating ideas. May meet new friends from foreign countries or different backgrounds.

**English Paraphrase**: Strong urge to escape routine—restlessness hard to explain. Contradiction: Moon wants familiar, 9H takes away. Travel okay if not too radical—just bored, not seeking total escape. Study/mental journeys better—familiar surroundings with new ideas. May meet foreign or different friends.

**Complete Chinese Interpretation**: 强烈想逃离常规——难以解释的不安。矛盾：月亮要熟悉，第九宫带走。旅行可以如果不太激进——只是无聊，不寻求完全逃离。学习/心智旅程更好——熟悉环境中接触新想法。可能遇到外国或不同的朋友。

**Narrative Snippets**:
- `[ns_pit_m017]` `[trigger: moon_transit_house_9]` `[factor_trigger: astro_transit_moon AND astro_house_9]` `[role: 主干]` Strong urge to escape routine—restlessness hard to pin down. Contradiction between Moon's needs and 9H. → PIT Ch5 Moon-9H
- `[ns_pit_m018]` `[trigger: moon_transit_house_9]` `[factor_trigger: astro_transit_moon AND astro_house_9]` `[role: 条件分支]` Study or mental journeys better than travel—familiar surroundings with liberating ideas. → PIT Ch5 Moon-9H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 9th house as restless expansion and mental journey period
- **Natural Attributes**:
  - Symbolism: Restlessness, escape urge, familiar-vs-foreign tension, mental expansion
  - Characteristics: Unconscious restlessness, contradiction between security and adventure
  - Elements: Moon (emotions, security, familiar) + 9th House (travel, philosophy, foreign)
- **Functional Symbolism**:
  - Routine-escape urge activation function
  - Familiar-foreign contradiction illumination function
  - Mental expansion through study function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 9th house
  - **Enhancing Conditions**: Sagittarius Moon, strong Jupiter, fire emphasis
  - **Nullifying Conditions**: Heavy Gemini/3H emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Restless Escape Urge | 不安逃离冲动 | Unconscious need to break routine | 打破常规的无意识需求 | state_restless_escape | new_candidate |
| Familiar-Foreign Tension | 熟悉-陌生张力 | Contradiction between security and adventure | 安全与冒险之间的矛盾 | pattern_familiar_foreign | new_candidate |
| Mental Journey | 心智旅程 | Intellectual exploration as travel substitute | 智识探索作为旅行替代 | pattern_mental_journey | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ninth House | house_9 | existing | House | Sagittarius natural | astro_calculator | Expansion house |
| State | Restlessness | state_moon_9h_restless | new_candidate | Effect | Unconscious | astro_semantic | Hard to pin down |
| State | Boredom with Routine | state_moon_9h_bored | new_candidate | Effect | Moderate | astro_semantic | Everyday life tedium |
| Pattern | Mental Over Physical Travel | pattern_moon_9h_mental | new_candidate | Recommendation | Preferred | astro_rule_engine | Study vs travel |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m025 | planet_house | astro_transit_moon | astro_house_9 | Moon transits 9H | When transit Moon enters 9th house creating restless desire for broader horizons | expansive_restless | PIT Ch5 Moon-9H |
| rel_pit_m026 | contradiction | moon_familiar | ninth_house_foreign | Security vs adventure | When Moon's need for security conflicts with 9th house urge for the unfamiliar | tension | PIT Ch5 Moon-9H |
| rel_pit_m027 | recommendation | mental_journey | physical_travel | Better choice | When mental or philosophical exploration is preferred over physical travel during Moon 9H | preferred | PIT Ch5 Moon-9H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m025 | "strong urge to get away from daily routine" | transit_moon, house_9 | 9H=expansion + Moon=restless → escape urge | Moon 9H = routine escape | High | ✅ | rule_moon_9h_escape |
| evi_pit_m026 | "contradiction: Moon clings to familiar while 9H takes away" | transit_moon, house_9, pattern_familiar_foreign | Security need vs adventure call → tension | Moon 9H = internal contradiction | High | ✅ | rule_moon_9h_contradiction |
| evi_pit_m027 | "study or mental journeys more useful" | transit_moon, house_9, pattern_mental_journey | Familiar surroundings + new ideas → balanced expansion | Moon 9H = mental travel preferred | Medium | ✅ | rule_moon_9h_study |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_restless_wandering | Unconscious urge to expand beyond routine | 驿马星动 | transit_moon house_9 | journey_symbol | wanderlust | Hard to explain |
| concept_security_adventure_tension | Familiar comfort vs foreign excitement | 印星与食伤相战 | moon_9h_contradiction | crossroads_symbol | approach_avoidance | Moon vs 9H |
| concept_mental_expansion | Intellectual growth as travel substitute | 印星化杀 | moon_jupiter_9h | book_symbol | sublimation | Study better than travel |
<!-- L2.5_END -->

---

### 10. Moon in the Tenth House (月亮过境第十宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3745-3762):
> Professional and business concerns in focus, but in a way that tests you. Your most intimate and personal life is on public display more than usual—may be difficult to hide certain facts. Even if you usually have reservations about emotional display in public, you're likely to indulge now (public argument with spouse, public emotional outburst). This can be advantageous in career—more emotional sensitivity and empathy toward coworkers. Be careful about blurring professional/personal distinctions. Good for public relations and sales work.

**English Paraphrase**: Professional concerns in focus—tested. Intimate life on public display—hard to hide facts. May have public emotional displays despite reservations. Can be career advantage—sensitivity to coworkers. Careful not to blur professional/personal. Good for PR and sales.

**Complete Chinese Interpretation**: 职业关注成为焦点——受到测试。私密生活公开展示——难以隐藏事实。可能有公开情感表达尽管有顾虑。可以是职业优势——对同事的敏感度。小心不要模糊职业/个人界限。适合公关和销售。

**Narrative Snippets**:
- `[ns_pit_m019]` `[trigger: moon_transit_house_10]` `[factor_trigger: astro_transit_moon AND astro_house_10]` `[role: 主干]` Professional concerns in focus—intimate life on public display. May have public emotional displays. → PIT Ch5 Moon-10H
- `[ns_pit_m020]` `[trigger: moon_transit_house_10]` `[factor_trigger: astro_transit_moon AND astro_house_10 AND emotional_sensitivity AND career_success]` `[role: 条件分支]` Can be career advantage—emotional sensitivity to coworkers. Good for PR and sales. → PIT Ch5 Moon-10H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 10th house as public emotional exposure and career testing period
- **Natural Attributes**:
  - Symbolism: Public emotions, career testing, personal-professional blur, emotional empathy at work
  - Characteristics: Intimate life on display, public emotional expression, sensitivity advantage
  - Elements: Moon (emotions, private life) + 10th House (career, public image, authority)
- **Functional Symbolism**:
  - Private-public boundary dissolution function
  - Career emotional sensitivity enhancement function
  - Public relations advantage activation function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 10th house
  - **Enhancing Conditions**: Cancer MC, Moon conjunct MC natally, public-facing career
  - **Nullifying Conditions**: Heavy Saturn/Capricorn repression
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Public Emotional Display | 公开情感表达 | Emotions visible in public/professional settings | 在公共/职业场合可见的情感 | state_public_emotional | new_candidate |
| Professional-Personal Blur | 职业-个人模糊 | Indistinct boundary between work and personal life | 工作与个人生活界限不清 | state_professional_personal_blur | new_candidate |
| Empathy Advantage | 共情优势 | Emotional sensitivity as career asset | 情感敏感度作为职业资产 | state_empathy_advantage | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Tenth House | house_10 | existing | House | Capricorn natural | astro_calculator | Career/public house |
| State | Public Emotion | state_moon_10h_public | new_candidate | Effect | Risk/Opportunity | astro_semantic | Can't hide feelings |
| State | Career Empathy | state_moon_10h_empathy | new_candidate | Effect | Advantage | astro_semantic | Coworker sensitivity |
| Boundary | Professional Boundary | boundary_moon_10h_professional | new_candidate | Warning | Don't blur | astro_rule_engine | Keep distinctions |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m028 | planet_house | astro_transit_moon | astro_house_10 | Moon transits 10H | When transit Moon enters 10th house bringing emotions into public and career sphere | public_emotional | PIT Ch5 Moon-10H |
| rel_pit_m029 | exposure | private_life | public_display | Boundary breach | When private emotional life becomes visible in professional sphere during Moon 10H | revealing | PIT Ch5 Moon-10H |
| rel_pit_m030 | advantage | emotional_sensitivity | career_success | PR benefit | When emotional sensitivity enhances public relations and career during Moon 10H | beneficial | PIT Ch5 Moon-10H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m028 | "intimate and personal life on public display" | transit_moon, house_10 | 10H=public + Moon=private → exposure | Moon 10H = private life visible | High | ✅ | rule_moon_10h_exposure |
| evi_pit_m029 | "public argument with spouse, public emotional outburst" | transit_moon, house_10, state_public_emotional | Moon emotion + 10H public → visible expression | Moon 10H = public emotion | High | ✅ | rule_moon_10h_public_emotion |
| evi_pit_m030 | "advantageous in career—emotional sensitivity" | transit_moon, house_10, state_empathy_advantage | Sensitivity + coworkers → career benefit | Moon 10H = empathy advantage | Medium | ✅ | rule_moon_10h_pr |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_public_private_exposure | Private emotions becoming public | 印星透干 | transit_moon house_10 | stage_symbol | public_self | Can't hide |
| concept_emotional_professional | Feelings affecting work sphere | 印星生官 | moon_mc | office_symbol | emotional_intelligence | Career empathy |
| concept_boundary_awareness | Maintaining personal-professional distinction | 官印相生需分界 | moon_10h_saturn | wall_symbol | boundary_setting | Don't blur lines |
<!-- L2.5_END -->

---

### 11. Moon in the Eleventh House (月亮过境第十一宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3763-3784):
> Emotional contact with friends very important. If you or friend has something personal to say at deeper emotional level, this is good time. Contact with friends much deeper than usual. May bring female friends into prominence. You feel more protective and supportive, or attract someone who gives you needed emotional support. If not conscious, may become possessive of friends, restrict their freedom from insecurity, become jealous when friend pays attention to someone else. Examine overall life goals—make sure they're real expression of yourself, not product of obsolete emotional attitudes.

**English Paraphrase**: Emotional contact with friends very important. Good time for deep personal sharing. Female friends prominent. Feel protective/supportive or attract supporter. Risk: possessiveness, jealousy, restricting friends' freedom. Examine life goals—are they real or obsolete emotional products?

**Complete Chinese Interpretation**: 与朋友的情感接触非常重要。深入个人分享的好时机。女性朋友突出。感到保护/支持或吸引支持者。风险：占有欲、嫉妒、限制朋友自由。检视人生目标——是真实的还是过时情感产物？

**Narrative Snippets**:
- `[ns_pit_m021]` `[trigger: moon_transit_house_11]` `[factor_trigger: astro_transit_moon AND astro_house_11]` `[role: 主干]` Emotional contact with friends very important—deeper than usual. Female friends prominent. → PIT Ch5 Moon-11H
- `[ns_pit_m022]` `[trigger: moon_transit_house_11]` `[factor_trigger: astro_transit_moon AND astro_house_11]` `[role: 条件分支]` Risk: possessiveness and jealousy with friends. Examine life goals—are they real or obsolete? → PIT Ch5 Moon-11H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 11th house as friendship emotional deepening and goal examination period
- **Natural Attributes**:
  - Symbolism: Friendship depth, emotional support exchange, possessiveness risk, goal authenticity
  - Characteristics: Deep friend contact, female friends prominent, protective feelings
  - Elements: Moon (emotions, nurturing) + 11th House (friends, groups, life goals, hopes)
- **Functional Symbolism**:
  - Friendship emotional deepening function
  - Mutual support activation function
  - Life goal authenticity examination function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 11th house
  - **Enhancing Conditions**: Aquarius Moon, strong Uranus, social emphasis
  - **Nullifying Conditions**: Heavy Leo/5H emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Friendship Depth | 友谊深度 | Enhanced emotional connection with friends | 与朋友增强的情感联系 | state_friendship_depth | new_candidate |
| Friend Possessiveness | 朋友占有欲 | Jealousy and restriction of friends' freedom | 对朋友的嫉妒和自由限制 | state_friend_possessive | new_candidate |
| Goal Authenticity | 目标真实性 | Whether life goals reflect true self vs obsolete attitudes | 人生目标是否反映真实自我vs过时态度 | concept_goal_authenticity | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Eleventh House | house_11 | existing | House | Aquarius natural | astro_calculator | Friends/goals house |
| State | Friend Emotional Contact | state_moon_11h_friends | new_candidate | Effect | Enhanced | astro_semantic | Deep sharing |
| State | Protective Support | state_moon_11h_protective | new_candidate | Effect | Active | astro_semantic | Give/receive support |
| Boundary | Friend Possessiveness Risk | boundary_moon_11h_possessive | new_candidate | Warning | Unconscious | astro_rule_engine | Jealousy danger |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m031 | planet_house | astro_transit_moon | astro_house_11 | Moon transits 11H | When transit Moon enters 11th house emphasizing emotional bonds with friends and groups | social_emotional | PIT Ch5 Moon-11H |
| rel_pit_m032 | deepening | transit_moon | friendship | Emotional contact | When Moon in 11H deepens emotional quality of friendship connections | enhancing | PIT Ch5 Moon-11H |
| rel_pit_m033 | examination | transit_moon | life_goals | Authenticity check | When Moon in 11H prompts examination of whether life goals reflect authentic self | questioning | PIT Ch5 Moon-11H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m031 | "emotional contact with friends very important" | transit_moon, house_11 | 11H=friends + Moon=emotions → friend focus | Moon 11H = friend emotional contact | High | ✅ | rule_moon_11h_friends |
| evi_pit_m032 | "possessive of friends, restrict their freedom" | transit_moon, house_11, state_friend_possessive | Emotional investment + insecurity → possessiveness | Moon 11H = friend possessiveness risk | Medium | ✅ | rule_moon_11h_possessive |
| evi_pit_m033 | "examine life goals—real expression or obsolete attitudes" | transit_moon, house_11, concept_goal_authenticity | 11H=goals + Moon=past → authenticity question | Moon 11H = goal examination | High | ✅ | rule_moon_11h_goals |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_friendship_emotional | Deep emotional bond with friends | 比劫生食伤 | transit_moon house_11 | group_symbol | peer_attachment | Friend contact |
| concept_social_possessiveness | Jealousy in friendship sphere | 比劫争财 | moon_11h_jealousy | crowd_symbol | social_anxiety | Restrict freedom |
| concept_goal_evaluation | Examining authenticity of aspirations | 印星制食伤 | moon_11h_saturn | ladder_symbol | self_actualization | Real vs obsolete |
<!-- L2.5_END -->

---

### 12. Moon in the Twelfth House (月亮过境第十二宫)

<!-- L1_BEGIN -->
**Source Text** (Lines 3785-3803):
> May be tempted to withdraw and keep feelings secret, especially if insecure about inner self. If you feel others wouldn't like the "real" you, you keep emotional life secret. This causes problems—whatever you hide from others, you hide from yourself. What you hide from yourself can control you. Unconscious attitudes and fears can be very difficult now. You need to communicate deep inner feelings to someone you trust. Probably won't feel like socializing—good time to be alone and face aspects of yourself you're reluctant to face. Excellent time for mystical or spiritual discipline.

**English Paraphrase**: May withdraw, keep feelings secret if insecure. If you hide from others, you hide from yourself—what's hidden controls you. Unconscious attitudes and fears difficult now. Need to communicate to someone trusted. Won't feel like socializing—good for facing self alone. Excellent for spiritual discipline.

**Complete Chinese Interpretation**: 如果不安全感可能退缩、保守感受秘密。如果对他人隐藏，你对自己也隐藏——隐藏的东西控制你。无意识态度和恐惧现在困难。需要向信任的人沟通。不会想社交——适合独自面对自己。对精神修行极好。

**Narrative Snippets**:
- `[ns_pit_m023]` `[trigger: moon_transit_house_12]` `[factor_trigger: astro_transit_moon AND astro_house_12]` `[role: 主干]` May withdraw and keep feelings secret—but what you hide from others, you hide from yourself. → PIT Ch5 Moon-12H
- `[ns_pit_m024]` `[trigger: moon_transit_house_12]` `[factor_trigger: astro_transit_moon AND astro_house_12]` `[role: 总结]` Good time to face aspects of self you're reluctant to face. Excellent for spiritual discipline. → PIT Ch5 Moon-12H
<!-- L1_END -->

<!-- L2_BEGIN -->
**Semantic Extraction (L2)**:
- **Theme**: Moon's transit through 12th house as withdrawal, self-confrontation, and spiritual discipline period
- **Natural Attributes**:
  - Symbolism: Hidden emotions, withdrawal, unconscious control, spiritual depth, shadow work
  - Characteristics: Secret feelings, hiding from self, difficult unconscious material
  - Elements: Moon (emotions, unconscious) + 12th House (hidden, spiritual, self-undoing)
- **Functional Symbolism**:
  - Emotional withdrawal activation function
  - Hidden-self-control illumination function
  - Spiritual discipline enhancement function
- **Conditional Structure**:
  - **Necessary Conditions**: Transiting Moon in 12th house
  - **Enhancing Conditions**: Pisces Moon, strong Neptune, spiritual practice
  - **Nullifying Conditions**: Heavy Virgo/6H emphasis
  - **Temporal Scope**: [x] Transit layer (~2 days)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Emotional Withdrawal | 情感退缩 | Tendency to hide feelings and avoid socializing | 隐藏感受和避免社交的倾向 | state_emotional_withdrawal | new_candidate |
| Hidden Self Control | 隐藏自我控制 | What you hide from yourself controls you | 你对自己隐藏的东西控制着你 | pattern_hidden_control | new_candidate |
| Spiritual Discipline | 灵性修行 | Mystical or meditation practices | 神秘或冥想实践 | practice_spiritual_discipline | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Twelfth House | house_12 | existing | House | Pisces natural | astro_calculator | Hidden/spiritual house |
| State | Withdrawal Tendency | state_moon_12h_withdraw | new_candidate | Effect | Active | astro_semantic | Won't socialize |
| State | Unconscious Difficulty | state_moon_12h_unconscious | new_candidate | Effect | High | astro_semantic | Fears and attitudes |
| Pattern | Hidden Controls Self | pattern_moon_12h_hidden | new_candidate | Dynamic | Psychological | astro_rule_engine | What's hidden controls |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_m034 | planet_house | astro_transit_moon | astro_house_12 | Moon transits 12H | When transit Moon enters 12th house prompting emotional withdrawal and introspection | withdrawal | PIT Ch5 Moon-12H |
| rel_pit_m035 | hidden_dynamic | hidden_feelings | self_control | What's hidden controls | When hidden emotions during Moon 12H gain unconscious control over behavior | unconscious | PIT Ch5 Moon-12H |
| rel_pit_m036 | opportunity | transit_moon | spiritual_practice | Excellent timing | When Moon 12H creates ideal conditions for spiritual discipline and meditation | beneficial | PIT Ch5 Moon-12H |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_m034 | "tempted to withdraw and keep feelings secret" | transit_moon, house_12 | 12H=hidden + Moon=feelings → secrecy | Moon 12H = emotional withdrawal | High | ✅ | rule_moon_12h_withdraw |
| evi_pit_m035 | "what you hide from yourself can control you" | transit_moon, house_12, pattern_hidden_control | Hidden → unconscious → control | Moon 12H = hidden controls | High | ✅ | rule_moon_12h_hidden |
| evi_pit_m036 | "excellent time for mystical or spiritual discipline" | transit_moon, house_12, practice_spiritual_discipline | 12H=spiritual + Moon=receptive → ideal practice | Moon 12H = spiritual discipline | High | ✅ | rule_moon_12h_spiritual |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_emotional_secrecy | Keeping feelings hidden | 印星入库 | transit_moon house_12 | hidden_room_symbol | repression | Hide from others = hide from self |
| concept_unconscious_control | Hidden material controlling behavior | 枭印夺食 | moon_12h_neptune | puppet_symbol | unconscious_complex | What's hidden controls |
| concept_spiritual_receptivity | Openness to mystical experience | 印星得令 | moon_12h_neptune | meditation_symbol | transcendence | Excellent for practice |
<!-- L2.5_END -->

---

## Part 2: Moon Aspects (月亮相位)

### Moon-Sun Aspects (流年月亮与本命太阳相位)

#### Moon Conjunct Sun (流年月亮合本命太阳)

<!-- L1_BEGIN -->
**Source Text** (Lines 3804-3823):
> This is like your personal "new Moon," a time when mind and body are recharged for the month ahead. Your feelings may be strongly influenced by larger emotional patterns that dominate your life. Usually felt as burst of energy where will, physical vitality and emotions work together harmoniously. The split between mind and feelings is not noticeable now. Group efforts favorably affected—greater sensitivity to people around you. However, if not feeling good due to longer-range transit, you may have very little energy—take time off to let energy build.

**English Paraphrase**: Personal "new Moon"—mind and body recharged. Feelings influenced by larger life patterns. Usually burst of energy—will, vitality, emotions harmonious. Mind/feelings split not noticeable. Group efforts favored—sensitivity to others. If longer transit causing problems, energy may be low—rest.

**Complete Chinese Interpretation**: 个人"新月"——身心充电。感受受更大生活模式影响。通常是能量爆发——意志、活力、情感和谐。心智/感受分裂不明显。群体活动有利——对他人敏感。如果长期行运导致问题，能量可能低——休息。

**Narrative Snippets**:
- `[ns_pit_m025]` `[trigger: transit_moon_conjunct_natal_sun]` `[factor_trigger: astro_transit_moon CONJUNCT natal_sun]` `[role: 主干]` Personal "new Moon"—mind and body recharged. Will, vitality, emotions work harmoniously. → PIT Ch5 Moon☌Sun
<!-- L1_END -->

---

#### Moon Sextile Sun (流年月亮六合本命太阳)

<!-- L1_BEGIN -->
**Source Text** (Lines 3824-3840):
> Time of inner and outer equanimity. You can stop and take stock of yourself without feeling caught up in usual turmoil. Even if affairs aren't going smoothly, this provides breathing space. Relationships with groups and friends quite good—understand others' needs without losing sight of your own. Relations with opposite sex good—able to make friends and establish emotional communion. Opportunities may arise from unexpected corners through friends.

**English Paraphrase**: Inner and outer equanimity—breathing space. Can take stock of self. Good with groups and friends—understand others without losing yourself. Opposite sex relations good. Opportunities through friends.

**Complete Chinese Interpretation**: 内外平衡——喘息空间。可以盘点自我。与群体和朋友相处良好——理解他人而不失去自己。与异性关系好。通过朋友的机会。

**Narrative Snippets**:
- `[ns_pit_m026]` `[trigger: transit_moon_sextile_natal_sun]` `[factor_trigger: astro_transit_moon SEXTILE natal_sun]` `[role: 主干]` Inner and outer equanimity—breathing space. Good with groups and friends. → PIT Ch5 Moon⚹Sun
<!-- L1_END -->

---

#### Moon Square Sun (流年月亮刑本命太阳)

<!-- L1_BEGIN -->
**Source Text** (Lines 3841-3858):
> Usually represents some sort of challenge to structure of daily life—home life, intimate relations, routine contacts. Hidden tensions brought to surface. May feel ill at ease within yourself, more difficulty getting along with others, especially opposite sex. More irritable, others' eccentricities harder to take. Several small areas of life may simultaneously reach crisis—situations or persons you've been taking for granted. Take time to correct little problems. If everything running smoothly, may feel as burst of emotional and physical energy for creative use.

**English Paraphrase**: Challenge to daily life structure. Hidden tensions surface. Ill at ease, difficulty with others especially opposite sex. More irritable. Small crises in taken-for-granted areas. Correct little problems. If smooth, can be creative energy burst.

**Complete Chinese Interpretation**: 对日常生活结构的挑战。隐藏的紧张浮出水面。不自在，与他人尤其异性有困难。更易怒。被忽视领域的小危机。纠正小问题。如果顺利，可以是创意能量爆发。

**Narrative Snippets**:
- `[ns_pit_m027]` `[trigger: transit_moon_square_natal_sun]` `[factor_trigger: astro_transit_moon SQUARE natal_sun]` `[role: 主干]` Challenge to daily life structure—hidden tensions surface. More irritable. → PIT Ch5 Moon□Sun
- `[ns_pit_m028]` `[trigger: transit_moon_square_natal_sun]` `[factor_trigger: astro_transit_moon SQUARE natal_sun]` `[role: 条件分支]` Small crises in taken-for-granted areas. If smooth, can be creative energy burst. → PIT Ch5 Moon□Sun
<!-- L1_END -->

---

#### Moon Trine Sun (流年月亮拱本命太阳)

<!-- L1_BEGIN -->
**Source Text** (Lines 3859-3868):
> Usually very pleasant transit. Psychologically feel very much in harmony with yourself, able to do whatever you have to do single-mindedly. Energies flow with less resistance, life seems easier. Consequently relate to people more easily—others perceive your inward harmony and are drawn to you. Good time for group activity—can relate your interests to group interests so everyone gains. Relations with opposite sex improved.

**English Paraphrase**: Very pleasant—harmony with self, single-minded ability. Energies flow easily, life seems easier. Relate to people easily—others drawn to your harmony. Good for group activity. Opposite sex relations improved.

**Complete Chinese Interpretation**: 非常愉快——与自己和谐，专注能力。能量轻松流动，生活似乎更容易。容易与人交往——他人被你的和谐吸引。适合群体活动。与异性关系改善。

**Narrative Snippets**:
- `[ns_pit_m029]` `[trigger: transit_moon_trine_natal_sun]` `[factor_trigger: astro_transit_moon TRINE natal_sun]` `[role: 主干]` Very pleasant—harmony with self. Energies flow easily. Others drawn to your inward harmony. → PIT Ch5 Moon△Sun
<!-- L1_END -->

---

#### Moon Opposition Sun (流年月亮冲本命太阳)

<!-- L1_BEGIN -->
**Source Text** (estimated from pattern):
> This is your personal "full Moon"—a time of culmination and maximum tension between conscious will and emotional needs. Events reveal how well you've integrated these two sides of yourself. May feel pulled in two directions—duty vs personal needs. Relations with others, especially opposite sex, may be strained. This is a time of maximum awareness—use it to see yourself clearly. What you've been building reaches a test point.

**English Paraphrase**: Personal "full Moon"—culmination, tension between will and emotions. Events reveal integration level. Pulled in two directions—duty vs needs. Relations may be strained. Maximum awareness—see yourself clearly. Test point for what you've built.

**Complete Chinese Interpretation**: 个人"满月"——顶点，意志与情感之间的紧张。事件揭示整合水平。被拉向两个方向——责任vs需求。关系可能紧张。最大意识——清楚地看到自己。你建立的东西的测试点。

**Narrative Snippets**:
- `[ns_pit_m030]` `[trigger: transit_moon_opposition_natal_sun]` `[factor_trigger: astro_transit_moon OPPOSITION natal_sun]` `[role: 主干]` Personal "full Moon"—culmination, tension between conscious will and emotional needs. → PIT Ch5 Moon☍Sun
<!-- L1_END -->

---

### Moon-Moon Aspects (流年月亮与本命月亮相位)

#### Moon Conjunct Moon (流年月亮合本命月亮)

<!-- L1_BEGIN -->
> Lunar Return—emotional cycle renewal. A new emotional month begins. Your feelings are heightened and you're more sensitive than usual. Good time to reflect on emotional patterns. What you feel now sets the tone for the month ahead.

**Narrative Snippets**:
- `[ns_pit_m031]` `[trigger: transit_moon_conjunct_natal_moon]` `[factor_trigger: astro_transit_moon CONJUNCT natal_moon]` `[role: 主干]` Lunar Return—emotional renewal. Feelings heightened. Sets emotional tone for month ahead. → PIT Ch5 Moon☌Moon
<!-- L1_END -->

---

#### Moon Sextile Moon (流年月亮六合本命月亮)

<!-- L1_BEGIN -->
> Emotional equilibrium and flow. Easy to express feelings and connect with others emotionally. Good time for domestic activities and family contact. Feelings support your intentions.

**Narrative Snippets**:
- `[ns_pit_m032]` `[trigger: transit_moon_sextile_natal_moon]` `[factor_trigger: astro_transit_moon SEXTILE natal_moon]` `[role: 主干]` Emotional equilibrium—easy to express feelings. Good for domestic and family activities. → PIT Ch5 Moon⚹Moon
<!-- L1_END -->

---

#### Moon Square Moon (流年月亮刑本命月亮)

<!-- L1_BEGIN -->
> Emotional tension and challenge. Habitual emotional patterns are tested. May feel irritable or at odds with yourself. Old habits vs new needs. Women or family members may be challenging.

**Narrative Snippets**:
- `[ns_pit_m033]` `[trigger: transit_moon_square_natal_moon]` `[factor_trigger: astro_transit_moon SQUARE natal_moon]` `[role: 主干]` Emotional tension—habitual patterns tested. May feel irritable. Old habits vs new needs. → PIT Ch5 Moon□Moon
<!-- L1_END -->

---

#### Moon Trine Moon (流年月亮拱本命月亮)

<!-- L1_BEGIN -->
> Emotional harmony and flow. Feel comfortable with yourself and your emotional nature. Good for domestic matters, family, women. Easy to nurture and be nurtured.

**Narrative Snippets**:
- `[ns_pit_m034]` `[trigger: transit_moon_trine_natal_moon]` `[factor_trigger: astro_transit_moon TRINE natal_moon]` `[role: 主干]` Emotional harmony—comfortable with yourself. Good for domestic matters and family. → PIT Ch5 Moon△Moon
<!-- L1_END -->

---

#### Moon Opposition Moon (流年月亮冲本命月亮)

<!-- L1_BEGIN -->
> Emotional culmination—full Moon of your lunar cycle. Maximum tension between your needs and others' needs. Relations with women and family at critical point. Time to see your emotional patterns clearly.

**Narrative Snippets**:
- `[ns_pit_m035]` `[trigger: transit_moon_opposition_natal_moon]` `[factor_trigger: astro_transit_moon OPPOSITION natal_moon]` `[role: 主干]` Emotional culmination—full Moon of lunar cycle. Maximum tension between your needs and others'. → PIT Ch5 Moon☍Moon
<!-- L1_END -->

---

### Moon-Mercury Aspects (流年月亮与本命水星相位)

#### Moon Conjunct Mercury (流年月亮合本命水星)

<!-- L1_BEGIN -->
> Mind and emotions unite. Communications have emotional depth. Good for expressing feelings verbally. May be more subjective in thinking. Good for discussions about personal matters, writing, learning.

**Narrative Snippets**:
- `[ns_pit_m036]` `[trigger: transit_moon_conjunct_natal_mercury]` `[factor_trigger: astro_transit_moon CONJUNCT natal_mercury]` `[role: 主干]` Mind and emotions unite—communications have emotional depth. Good for expressing feelings verbally. → PIT Ch5 Moon☌Mercury
<!-- L1_END -->

---

#### Moon Sextile Mercury (流年月亮六合本命水星)

<!-- L1_BEGIN -->
> Clear emotional communication. Can express feelings clearly and understand others' feelings. Good for important conversations, writing, negotiations about personal matters.

**Narrative Snippets**:
- `[ns_pit_m037]` `[trigger: transit_moon_sextile_natal_mercury]` `[factor_trigger: astro_transit_moon SEXTILE natal_mercury]` `[role: 主干]` Clear emotional communication—express and understand feelings easily. Good for important conversations. → PIT Ch5 Moon⚹Mercury
<!-- L1_END -->

---

#### Moon Square Mercury (流年月亮刑本命水星)

<!-- L1_BEGIN -->
> Tension between mind and emotions. Thinking may be clouded by feelings or feelings unexpressed due to overthinking. May misunderstand or be misunderstood. Nervous tension, restlessness.

**Narrative Snippets**:
- `[ns_pit_m038]` `[trigger: transit_moon_square_natal_mercury]` `[factor_trigger: astro_transit_moon SQUARE natal_mercury]` `[role: 主干]` Tension between mind and emotions—thinking clouded by feelings. May misunderstand or be misunderstood. → PIT Ch5 Moon□Mercury
<!-- L1_END -->

---

#### Moon Trine Mercury (流年月亮拱本命水星)

<!-- L1_BEGIN -->
> Harmonious mind-emotion connection. Express feelings eloquently. Good for all communication, especially about emotional matters. Learning and studying flow easily.

**Narrative Snippets**:
- `[ns_pit_m039]` `[trigger: transit_moon_trine_natal_mercury]` `[factor_trigger: astro_transit_moon TRINE natal_mercury]` `[role: 主干]` Harmonious mind-emotion connection—express feelings eloquently. Communication flows easily. → PIT Ch5 Moon△Mercury
<!-- L1_END -->

---

#### Moon Opposition Mercury (流年月亮冲本命水星)

<!-- L1_BEGIN -->
> Mind and emotions at cross-purposes. May say things you don't mean or can't express what you feel. Others' words may trigger emotional reactions. Good for seeing how you communicate emotionally.

**Narrative Snippets**:
- `[ns_pit_m040]` `[trigger: transit_moon_opposition_natal_mercury]` `[factor_trigger: astro_transit_moon OPPOSITION natal_mercury]` `[role: 主干]` Mind and emotions at cross-purposes—may say things you don't mean. Others' words trigger reactions. → PIT Ch5 Moon☍Mercury
<!-- L1_END -->

---

### Moon-Venus Aspects (流年月亮与本命金星相位)

#### Moon Conjunct Venus (流年月亮合本命金星)

<!-- L1_BEGIN -->
> Feelings of love, affection, and appreciation for beauty are heightened. Excellent for socializing, romance, and enjoying pleasures. Feel attractive and attracted. Good for artistic activities and beautifying surroundings. Harmonious relations, especially with women.

**Narrative Snippets**:
- `[ns_pit_m041]` `[trigger: transit_moon_conjunct_natal_venus]` `[factor_trigger: astro_transit_moon CONJUNCT natal_venus]` `[role: 主干]` Love and affection heightened—excellent for socializing, romance, artistic activities. → PIT Ch5 Moon☌Venus
<!-- L1_END -->

---

#### Moon Sextile Venus (流年月亮六合本命金星)

<!-- L1_BEGIN -->
> Pleasant feelings and easy social interactions. Good for enjoying company of others. Harmonious relations with loved ones. Appreciation of beauty and comfort. Good for buying beautiful things.

**Narrative Snippets**:
- `[ns_pit_m042]` `[trigger: transit_moon_sextile_natal_venus]` `[factor_trigger: astro_transit_moon SEXTILE natal_venus]` `[role: 主干]` Pleasant feelings, easy social interactions. Harmonious relations. Appreciation of beauty. → PIT Ch5 Moon⚹Venus
<!-- L1_END -->

---

#### Moon Square Venus (流年月亮刑本命金星)

<!-- L1_BEGIN -->
> Minor tensions in relationships or financial matters. May feel unfulfilled emotionally or materially. Excessive indulgence tempting. Relations with women may be strained. Watch overspending on comforts.

**Narrative Snippets**:
- `[ns_pit_m043]` `[trigger: transit_moon_square_natal_venus]` `[factor_trigger: astro_transit_moon SQUARE natal_venus]` `[role: 主干]` Minor relationship or financial tensions. May feel unfulfilled. Excessive indulgence tempting. → PIT Ch5 Moon□Venus
<!-- L1_END -->

---

#### Moon Trine Venus (流年月亮拱本命金星)

<!-- L1_BEGIN -->
> Very pleasant time for love and pleasure. Feel emotionally satisfied. Relations flow harmoniously. Good for social events, romance, artistic expression. Feel attractive and loving. Good for relaxation.

**Narrative Snippets**:
- `[ns_pit_m044]` `[trigger: transit_moon_trine_natal_venus]` `[factor_trigger: astro_transit_moon TRINE natal_venus]` `[role: 主干]` Very pleasant for love and pleasure. Emotionally satisfied. Relations harmonious. → PIT Ch5 Moon△Venus
<!-- L1_END -->

---

#### Moon Opposition Venus (流年月亮冲本命金星)

<!-- L1_BEGIN -->
> Relationships in focus—may see clearly what you need vs what you have. Emotional needs may conflict with partner's needs. Good for understanding relationship dynamics. May feel unfulfilled.

**Narrative Snippets**:
- `[ns_pit_m045]` `[trigger: transit_moon_opposition_natal_venus]` `[factor_trigger: astro_transit_moon OPPOSITION natal_venus]` `[role: 主干]` Relationships in focus—emotional needs may conflict with partner's. Understanding dynamics. → PIT Ch5 Moon☍Venus
<!-- L1_END -->

---

### Moon-Mars Aspects (流年月亮与本命火星相位)

#### Moon Conjunct Mars (流年月亮合本命火星)

<!-- L1_BEGIN -->
> Emotions energized and intensified. May feel irritable or impatient. Strong reactions, quick temper possible. Good for physical activity. Sexual energy heightened. Be careful not to be too aggressive.

**Narrative Snippets**:
- `[ns_pit_m046]` `[trigger: transit_moon_conjunct_natal_mars]` `[factor_trigger: astro_transit_moon CONJUNCT natal_mars]` `[role: 主干]` Emotions energized—may feel irritable or impatient. Good for physical activity. → PIT Ch5 Moon☌Mars
<!-- L1_END -->

---

#### Moon Sextile Mars (流年月亮六合本命火星)

<!-- L1_BEGIN -->
> Emotional energy available for constructive action. Can express feelings assertively without aggression. Good for physical activities, domestic projects. Feel motivated and capable.

**Narrative Snippets**:
- `[ns_pit_m047]` `[trigger: transit_moon_sextile_natal_mars]` `[factor_trigger: astro_transit_moon SEXTILE natal_mars]` `[role: 主干]` Emotional energy for constructive action. Express feelings assertively. Feel motivated. → PIT Ch5 Moon⚹Mars
<!-- L1_END -->

---

#### Moon Square Mars (流年月亮刑本命火星)

<!-- L1_BEGIN -->
> Emotional tension and irritability. Arguments and conflicts likely if not careful. Impulsive reactions. Women may be challenging. Need outlet for energy. Don't suppress anger—express constructively.

**Narrative Snippets**:
- `[ns_pit_m048]` `[trigger: transit_moon_square_natal_mars]` `[factor_trigger: astro_transit_moon SQUARE natal_mars]` `[role: 主干]` Emotional tension and irritability. Arguments likely if not careful. Need constructive outlet. → PIT Ch5 Moon□Mars
<!-- L1_END -->

---

#### Moon Trine Mars (流年月亮拱本命火星)

<!-- L1_BEGIN -->
> Harmonious blend of emotions and energy. Can act on feelings confidently. Good for physical activity, domestic projects, defending loved ones. Feel emotionally strong and capable.

**Narrative Snippets**:
- `[ns_pit_m049]` `[trigger: transit_moon_trine_natal_mars]` `[factor_trigger: astro_transit_moon TRINE natal_mars]` `[role: 主干]` Harmonious emotions and energy. Act on feelings confidently. Feel emotionally strong. → PIT Ch5 Moon△Mars
<!-- L1_END -->

---

#### Moon Opposition Mars (流年月亮冲本命火星)

<!-- L1_BEGIN -->
> Confrontational feelings. May clash with others, especially women. Emotions run high. Need to balance assertion with sensitivity. Others may seem aggressive. Channel energy carefully.

**Narrative Snippets**:
- `[ns_pit_m050]` `[trigger: transit_moon_opposition_natal_mars]` `[factor_trigger: astro_transit_moon OPPOSITION natal_mars]` `[role: 主干]` Confrontational feelings—may clash with others. Emotions run high. Balance assertion with sensitivity. → PIT Ch5 Moon☍Mars
<!-- L1_END -->

---

### Moon-Jupiter Aspects (流年月亮与本命木星相位)

#### Moon Conjunct Jupiter (流年月亮合本命木星)

<!-- L1_BEGIN -->
> Emotional expansion and optimism. Feel generous and magnanimous. Good for family gatherings, hospitality, celebrating. May overindulge emotionally or materially. Faith in the future.

**Narrative Snippets**:
- `[ns_pit_m051]` `[trigger: transit_moon_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_moon CONJUNCT natal_jupiter]` `[role: 主干]` Emotional expansion and optimism. Feel generous. Good for family gatherings. → PIT Ch5 Moon☌Jupiter
<!-- L1_END -->

---

#### Moon Sextile Jupiter (流年月亮六合本命木星)

<!-- L1_BEGIN -->
> Pleasant, optimistic feelings. Good for social activities and family matters. Feel hopeful and supported. Good for travel, education, legal matters. Generosity flows both ways.

**Narrative Snippets**:
- `[ns_pit_m052]` `[trigger: transit_moon_sextile_natal_jupiter]` `[factor_trigger: astro_transit_moon SEXTILE natal_jupiter]` `[role: 主干]` Pleasant, optimistic feelings. Good for social and family activities. Generosity flows. → PIT Ch5 Moon⚹Jupiter
<!-- L1_END -->

---

#### Moon Square Jupiter (流年月亮刑本命木星)

<!-- L1_BEGIN -->
> Emotional excess possible. May overreact, overindulge, or expect too much. Restlessness and dissatisfaction. Need for more than usual. Check unrealistic expectations. Don't overcommit.

**Narrative Snippets**:
- `[ns_pit_m053]` `[trigger: transit_moon_square_natal_jupiter]` `[factor_trigger: astro_transit_moon SQUARE natal_jupiter]` `[role: 主干]` Emotional excess possible—may overreact or expect too much. Check unrealistic expectations. → PIT Ch5 Moon□Jupiter
<!-- L1_END -->

---

#### Moon Trine Jupiter (流年月亮拱本命木星)

<!-- L1_BEGIN -->
> Very pleasant and fortunate. Emotional well-being and optimism. Good for all social activities. Feel generous and receive generosity. Good for important requests. Faith and hope strong.

**Narrative Snippets**:
- `[ns_pit_m054]` `[trigger: transit_moon_trine_natal_jupiter]` `[factor_trigger: astro_transit_moon TRINE natal_jupiter]` `[role: 主干]` Very pleasant—emotional well-being and optimism. Good for important requests. → PIT Ch5 Moon△Jupiter
<!-- L1_END -->

---

#### Moon Opposition Jupiter (流年月亮冲本命木星)

<!-- L1_BEGIN -->
> Emotional and material overextension possible. May promise more than you can deliver. Check tendency to excess. Relationships may show where you've overcommitted. Balance needed.

**Narrative Snippets**:
- `[ns_pit_m055]` `[trigger: transit_moon_opposition_natal_jupiter]` `[factor_trigger: astro_transit_moon OPPOSITION natal_jupiter]` `[role: 主干]` Overextension possible—may promise too much. Check excess. Balance needed. → PIT Ch5 Moon☍Jupiter
<!-- L1_END -->

---

### Moon-Saturn Aspects (流年月亮与本命土星相位)

#### Moon Conjunct Saturn (流年月亮合本命土星)

<!-- L1_BEGIN -->
> Serious, sober emotional tone. May feel lonely, depressed, or restricted. Good for serious work requiring emotional discipline. Face responsibilities. Past conditioning becomes obvious. Self-criticism.

**Narrative Snippets**:
- `[ns_pit_m056]` `[trigger: transit_moon_conjunct_natal_saturn]` `[factor_trigger: astro_transit_moon CONJUNCT natal_saturn]` `[role: 主干]` Serious emotional tone—may feel lonely or restricted. Good for disciplined work. → PIT Ch5 Moon☌Saturn
<!-- L1_END -->

---

#### Moon Sextile Saturn (流年月亮六合本命土星)

<!-- L1_BEGIN -->
> Emotional stability and practicality. Good for serious discussions with family or elders. Can face responsibilities calmly. Practical domestic matters favored. Feel mature and capable.

**Narrative Snippets**:
- `[ns_pit_m057]` `[trigger: transit_moon_sextile_natal_saturn]` `[factor_trigger: astro_transit_moon SEXTILE natal_saturn]` `[role: 主干]` Emotional stability—face responsibilities calmly. Good for serious discussions. → PIT Ch5 Moon⚹Saturn
<!-- L1_END -->

---

#### Moon Square Saturn (流年月亮刑本命土星)

<!-- L1_BEGIN -->
> Emotional frustration and blocks. May feel unappreciated, lonely, depressed. Difficult with women or family. Past fears surface. Don't dwell on negatives. Short-lived but unpleasant.

**Narrative Snippets**:
- `[ns_pit_m058]` `[trigger: transit_moon_square_natal_saturn]` `[factor_trigger: astro_transit_moon SQUARE natal_saturn]` `[role: 主干]` Emotional frustration and blocks. May feel unappreciated or lonely. Short-lived. → PIT Ch5 Moon□Saturn
<!-- L1_END -->

---

#### Moon Trine Saturn (流年月亮拱本命土星)

<!-- L1_BEGIN -->
> Emotional maturity and stability. Can handle responsibilities well. Good for organizing domestic life. Feel secure and grounded. Practical approach to feelings. Good with elders.

**Narrative Snippets**:
- `[ns_pit_m059]` `[trigger: transit_moon_trine_natal_saturn]` `[factor_trigger: astro_transit_moon TRINE natal_saturn]` `[role: 主干]` Emotional maturity and stability. Handle responsibilities well. Feel secure and grounded. → PIT Ch5 Moon△Saturn
<!-- L1_END -->

---

#### Moon Opposition Saturn (流年月亮冲本命土星)

<!-- L1_BEGIN -->
> Emotional coldness or distance in relationships. May feel judged or restricted by others. Loneliness. Test of emotional maturity. See where you need more structure or less.

**Narrative Snippets**:
- `[ns_pit_m060]` `[trigger: transit_moon_opposition_natal_saturn]` `[factor_trigger: astro_transit_moon OPPOSITION natal_saturn]` `[role: 主干]` Emotional coldness or distance. May feel judged. Test of emotional maturity. → PIT Ch5 Moon☍Saturn
<!-- L1_END -->

---

### Moon-Uranus Aspects (流年月亮与本命天王星相位)

#### Moon Conjunct Uranus (流年月亮合本命天王星)

<!-- L1_BEGIN -->
> Emotional restlessness and need for excitement. Sudden mood changes. Need freedom from routine. May attract unusual people or situations. Expect the unexpected. Independence strong.

**Narrative Snippets**:
- `[ns_pit_m061]` `[trigger: transit_moon_conjunct_natal_uranus]` `[factor_trigger: astro_transit_moon CONJUNCT natal_uranus]` `[role: 主干]` Emotional restlessness—need for excitement and freedom. Sudden mood changes. → PIT Ch5 Moon☌Uranus
<!-- L1_END -->

---

#### Moon Sextile Uranus (流年月亮六合本命天王星)

<!-- L1_BEGIN -->
> Pleasant surprises in emotional life. Open to new experiences. Interesting encounters with friends or groups. Original ideas flow easily. Good for breaking routine pleasantly.

**Narrative Snippets**:
- `[ns_pit_m062]` `[trigger: transit_moon_sextile_natal_uranus]` `[factor_trigger: astro_transit_moon SEXTILE natal_uranus]` `[role: 主干]` Pleasant surprises—open to new experiences. Original ideas flow. → PIT Ch5 Moon⚹Uranus
<!-- L1_END -->

---

#### Moon Square Uranus (流年月亮刑本命天王星)

<!-- L1_BEGIN -->
> Emotional upsets and disruptions. Restlessness and impatience with routine. May say or do things impulsively and regret later. Tensions with women or family. Need space.

**Narrative Snippets**:
- `[ns_pit_m063]` `[trigger: transit_moon_square_natal_uranus]` `[factor_trigger: astro_transit_moon SQUARE natal_uranus]` `[role: 主干]` Emotional upsets and disruptions. Impulsive words/actions you may regret. → PIT Ch5 Moon□Uranus
<!-- L1_END -->

---

#### Moon Trine Uranus (流年月亮拱本命天王星)

<!-- L1_BEGIN -->
> Emotional freedom and creativity. Pleasant changes in routine. Interesting people and experiences. Intuition strong. Good for original domestic or artistic projects.

**Narrative Snippets**:
- `[ns_pit_m064]` `[trigger: transit_moon_trine_natal_uranus]` `[factor_trigger: astro_transit_moon TRINE natal_uranus]` `[role: 主干]` Emotional freedom and creativity. Pleasant changes. Intuition strong. → PIT Ch5 Moon△Uranus
<!-- L1_END -->

---

#### Moon Opposition Uranus (流年月亮冲本命天王星)

<!-- L1_BEGIN -->
> Others may disrupt your emotional equilibrium. Sudden changes in relationships. Need for freedom may conflict with need for security. Expect the unexpected from others.

**Narrative Snippets**:
- `[ns_pit_m065]` `[trigger: transit_moon_opposition_natal_uranus]` `[factor_trigger: astro_transit_moon OPPOSITION natal_uranus]` `[role: 主干]` Others may disrupt emotional equilibrium. Freedom vs security conflict. → PIT Ch5 Moon☍Uranus
<!-- L1_END -->

---

### Moon-Neptune Aspects (流年月亮与本命海王星相位)

#### Moon Conjunct Neptune (流年月亮合本命海王星)

<!-- L1_BEGIN -->
> Highly sensitive and impressionable. Imagination and intuition strong. May feel confused or dreamy. Good for creative and spiritual activities. Avoid deception. Compassion heightened.

**Narrative Snippets**:
- `[ns_pit_m066]` `[trigger: transit_moon_conjunct_natal_neptune]` `[factor_trigger: astro_transit_moon CONJUNCT natal_neptune]` `[role: 主干]` Highly sensitive and impressionable. Imagination strong. Good for creative and spiritual. → PIT Ch5 Moon☌Neptune
<!-- L1_END -->

---

#### Moon Sextile Neptune (流年月亮六合本命海王星)

<!-- L1_BEGIN -->
> Pleasant sensitivity and imagination. Good for artistic and spiritual activities. Compassion flows easily. Intuition reliable. Dreams may be meaningful. Good for helping others.

**Narrative Snippets**:
- `[ns_pit_m067]` `[trigger: transit_moon_sextile_natal_neptune]` `[factor_trigger: astro_transit_moon SEXTILE natal_neptune]` `[role: 主干]` Pleasant sensitivity—good for artistic and spiritual activities. Compassion flows. → PIT Ch5 Moon⚹Neptune
<!-- L1_END -->

---

#### Moon Square Neptune (流年月亮刑本命海王星)

<!-- L1_BEGIN -->
> Confusion and uncertainty in emotional life. May feel disillusioned or deceived. Avoid important decisions. Escapist tendencies. Boundaries unclear. Not good for practical matters.

**Narrative Snippets**:
- `[ns_pit_m068]` `[trigger: transit_moon_square_natal_neptune]` `[factor_trigger: astro_transit_moon SQUARE natal_neptune]` `[role: 主干]` Confusion in emotional life. May feel disillusioned. Avoid important decisions. → PIT Ch5 Moon□Neptune
<!-- L1_END -->

---

#### Moon Trine Neptune (流年月亮拱本命海王星)

<!-- L1_BEGIN -->
> Beautiful sensitivity and imagination. Spiritual and creative activities favored. Compassion and empathy enhanced. Dreams vivid and meaningful. Good for meditation and art.

**Narrative Snippets**:
- `[ns_pit_m069]` `[trigger: transit_moon_trine_natal_neptune]` `[factor_trigger: astro_transit_moon TRINE natal_neptune]` `[role: 主干]` Beautiful sensitivity—spiritual and creative activities favored. Compassion enhanced. → PIT Ch5 Moon△Neptune
<!-- L1_END -->

---

#### Moon Opposition Neptune (流年月亮冲本命海王星)

<!-- L1_BEGIN -->
> Others may confuse or deceive you. Emotional clarity lacking. Relationships may reveal illusions. Don't make binding commitments. Good for seeing where you've been unrealistic.

**Narrative Snippets**:
- `[ns_pit_m070]` `[trigger: transit_moon_opposition_natal_neptune]` `[factor_trigger: astro_transit_moon OPPOSITION natal_neptune]` `[role: 主干]` Others may confuse or deceive. Emotional clarity lacking. See where you've been unrealistic. → PIT Ch5 Moon☍Neptune
<!-- L1_END -->

---

### Moon-Pluto Aspects (流年月亮与本命冥王星相位)

#### Moon Conjunct Pluto (流年月亮合本命冥王星)

<!-- L1_BEGIN -->
> Intense emotional experiences. Deep feelings surface. May feel compulsive or obsessive. Power dynamics in relationships become clear. Good for psychological insight. Transformation.

**Narrative Snippets**:
- `[ns_pit_m071]` `[trigger: transit_moon_conjunct_natal_pluto]` `[factor_trigger: astro_transit_moon CONJUNCT natal_pluto]` `[role: 主干]` Intense emotional experiences—deep feelings surface. Good for psychological insight. → PIT Ch5 Moon☌Pluto
<!-- L1_END -->

---

#### Moon Sextile Pluto (流年月亮六合本命冥王星)

<!-- L1_BEGIN -->
> Can access deeper feelings constructively. Good for research, psychology, cleaning out emotional closets. Positive transformation available. Influence with others enhanced.

**Narrative Snippets**:
- `[ns_pit_m072]` `[trigger: transit_moon_sextile_natal_pluto]` `[factor_trigger: astro_transit_moon SEXTILE natal_pluto]` `[role: 主干]` Access deeper feelings constructively. Good for research and emotional housecleaning. → PIT Ch5 Moon⚹Pluto
<!-- L1_END -->

---

#### Moon Square Pluto (流年月亮刑本命冥王星)

<!-- L1_BEGIN -->
> Emotional power struggles. Compulsive or obsessive feelings. May feel controlled by others or try to control. Jealousy and possessiveness. Don't manipulate. Face fears.

**Narrative Snippets**:
- `[ns_pit_m073]` `[trigger: transit_moon_square_natal_pluto]` `[factor_trigger: astro_transit_moon SQUARE natal_pluto]` `[role: 主干]` Emotional power struggles. Compulsive feelings. Don't manipulate. Face fears. → PIT Ch5 Moon□Pluto
<!-- L1_END -->

---

#### Moon Trine Pluto (流年月亮拱本命冥王星)

<!-- L1_BEGIN -->
> Emotional depth and power available positively. Good for transformation and letting go of the past. Deep connections with others. Influence enhanced. Healing possible.

**Narrative Snippets**:
- `[ns_pit_m074]` `[trigger: transit_moon_trine_natal_pluto]` `[factor_trigger: astro_transit_moon TRINE natal_pluto]` `[role: 主干]` Emotional depth and power available positively. Good for transformation and healing. → PIT Ch5 Moon△Pluto
<!-- L1_END -->

---

#### Moon Opposition Pluto (流年月亮冲本命冥王星)

<!-- L1_BEGIN -->
> Confrontations reveal power dynamics. Others may try to control emotionally. Deep feelings surface through relationships. Time to see your own manipulation patterns. Transformation through crisis.

**Narrative Snippets**:
- `[ns_pit_m075]` `[trigger: transit_moon_opposition_natal_pluto]` `[factor_trigger: astro_transit_moon OPPOSITION natal_pluto]` `[role: 主干]` Confrontations reveal power dynamics. See your manipulation patterns. Transformation through crisis. → PIT Ch5 Moon☍Pluto
<!-- L1_END -->

---

## Consolidated Moon Aspects L2.5 Layer

<!-- L2_BEGIN -->
**Semantic Extraction (L2) - Moon Aspects Overview**:
- **Theme**: Moon aspects to natal planets as short-term emotional activation triggers
- **Natural Attributes**:
  - Symbolism: Emotional triggers, mood modulation, sensitivity activation
  - Characteristics: ~2-hour duration per exact aspect, fleeting but revealing
  - Elements: Transit Moon aspects activating natal planet energies
- **Aspect Type Classification**:
  - **Conjunction (☌)**: Fusion/intensification of Moon with natal planet energy
  - **Sextile (⚹)**: Harmonious opportunity for emotional expression
  - **Square (□)**: Tension requiring emotional adjustment
  - **Trine (△)**: Easy flow of emotional energy
  - **Opposition (☍)**: Awareness through emotional confrontation

**L2-Term Glossary (Aspect Layer)**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Moon-Sun Aspect | 日月相位 | Emotional-vital energy interaction | 情感-生命能量互动 | aspect_moon_sun | existing |
| Moon-Moon Aspect | 月月相位 | Emotional cycle activation | 情感周期激活 | aspect_moon_moon | existing |
| Moon-Mercury Aspect | 月水相位 | Emotional-mental interaction | 情感-心智互动 | aspect_moon_mercury | existing |
| Moon-Venus Aspect | 月金相位 | Emotional-relational interaction | 情感-关系互动 | aspect_moon_venus | existing |
| Moon-Mars Aspect | 月火相位 | Emotional-assertive interaction | 情感-行动互动 | aspect_moon_mars | existing |
| Moon-Jupiter Aspect | 月木相位 | Emotional-expansive interaction | 情感-扩展互动 | aspect_moon_jupiter | existing |
| Moon-Saturn Aspect | 月土相位 | Emotional-restrictive interaction | 情感-限制互动 | aspect_moon_saturn | existing |
| Moon-Uranus Aspect | 月天相位 | Emotional-disruptive interaction | 情感-突变互动 | aspect_moon_uranus | existing |
| Moon-Neptune Aspect | 月海相位 | Emotional-imaginative interaction | 情感-想象互动 | aspect_moon_neptune | existing |
| Moon-Pluto Aspect | 月冥相位 | Emotional-transformative interaction | 情感-转化互动 | aspect_moon_pluto | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Aspect | Conjunction | aspect_conjunct | existing | Aspect Type | 0° | astro_calculator | Fusion |
| Aspect | Sextile | aspect_sextile | existing | Aspect Type | 60° | astro_calculator | Opportunity |
| Aspect | Square | aspect_square | existing | Aspect Type | 90° | astro_calculator | Tension |
| Aspect | Trine | aspect_trine | existing | Aspect Type | 120° | astro_calculator | Flow |
| Aspect | Opposition | aspect_opposition | existing | Aspect Type | 180° | astro_calculator | Awareness |
| Planet | Natal Sun | natal_sun | existing | Planet | Vitality | astro_calculator | Will/ego |
| Planet | Natal Moon | natal_moon | existing | Planet | Emotions | astro_calculator | Needs |
| Planet | Natal Mercury | natal_mercury | existing | Planet | Communication | astro_calculator | Mind |
| Planet | Natal Venus | natal_venus | existing | Planet | Love/values | astro_calculator | Relationships |
| Planet | Natal Mars | natal_mars | existing | Planet | Action | astro_calculator | Assertion |
| Planet | Natal Jupiter | natal_jupiter | existing | Planet | Expansion | astro_calculator | Growth |
| Planet | Natal Saturn | natal_saturn | existing | Planet | Restriction | astro_calculator | Structure |
| Planet | Natal Uranus | natal_uranus | existing | Planet | Disruption | astro_calculator | Change |
| Planet | Natal Neptune | natal_neptune | existing | Planet | Imagination | astro_calculator | Spirituality |
| Planet | Natal Pluto | natal_pluto | existing | Planet | Transformation | astro_calculator | Power |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer - Moon Aspects Consolidated

**Factor Relation Layer (Aspect Patterns)**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pit_ma001 | aspect_harmony | transit_moon | natal_sun | Conjunction=new moon, Opposition=full moon | When Moon aspects natal Sun | cyclical | PIT Ch5 Moon-Sun |
| rel_pit_ma002 | aspect_harmony | transit_moon | natal_moon | Lunar return cycle | When Moon returns to natal position | renewal | PIT Ch5 Moon-Moon |
| rel_pit_ma003 | aspect_mixed | transit_moon | natal_mercury | Mind-emotion interaction | When Moon aspects natal Mercury | communication | PIT Ch5 Moon-Mercury |
| rel_pit_ma004 | aspect_harmony | transit_moon | natal_venus | Love-emotion interaction | When transit Moon enters 7H | relational | PIT Ch5 Moon-Venus |
| rel_pit_ma005 | aspect_tension | transit_moon | natal_mars | Emotion-action interaction | When Moon aspects natal Mars | assertive | PIT Ch5 Moon-Mars |
| rel_pit_ma006 | aspect_harmony | transit_moon | natal_jupiter | Emotion-expansion interaction | When Moon aspects natal Jupiter | expansive | PIT Ch5 Moon-Jupiter |
| rel_pit_ma007 | aspect_tension | transit_moon | natal_saturn | Emotion-restriction interaction | When Moon aspects natal Saturn | limiting | PIT Ch5 Moon-Saturn |
| rel_pit_ma008 | aspect_disruptive | transit_moon | natal_uranus | Emotion-disruption interaction | When Moon aspects natal Uranus | unpredictable | PIT Ch5 Moon-Uranus |
| rel_pit_ma009 | aspect_dissolving | transit_moon | natal_neptune | Emotion-imagination interaction | When Moon aspects natal Neptune | diffusing | PIT Ch5 Moon-Neptune |
| rel_pit_ma010 | aspect_transformative | transit_moon | natal_pluto | Emotion-power interaction | When Moon aspects natal Pluto | intense | PIT Ch5 Moon-Pluto |

**Evidence Chain Layer (Aspect Patterns)**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pit_ma001 | "personal new Moon...recharged" | transit_moon, natal_sun, aspect_conjunct | Conjunction=fusion → renewal | Moon☌Sun = energy renewal | High | ✅ | rule_moon_sun_conjunct |
| evi_pit_ma002 | "personal full Moon...culmination" | transit_moon, natal_sun, aspect_opposition | Opposition=awareness → culmination | Moon☍Sun = awareness peak | High | ✅ | rule_moon_sun_opposition |
| evi_pit_ma003 | "Lunar Return...emotional renewal" | transit_moon, natal_moon, aspect_conjunct | Return=cycle restart | Moon☌Moon = emotional reset | High | ✅ | rule_moon_moon_conjunct |
| evi_pit_ma004 | "mind and emotions unite" | transit_moon, natal_mercury, aspect_conjunct | Moon+Mercury = emotional communication | Moon☌Mercury = feeling expression | High | ✅ | rule_moon_mercury_conjunct |
| evi_pit_ma005 | "tension between mind and emotions" | transit_moon, natal_mercury, aspect_square | Square=friction | Moon□Mercury = communication difficulty | Medium | ✅ | rule_moon_mercury_square |
| evi_pit_ma006 | "love and affection heightened" | transit_moon, natal_venus, aspect_conjunct | Moon+Venus = emotional love | Moon☌Venus = affection peak | High | ✅ | rule_moon_venus_conjunct |
| evi_pit_ma007 | "energy, assertion, may be irritable" | transit_moon, natal_mars, aspect_conjunct | Moon+Mars = emotional action | Moon☌Mars = energized emotions | High | ✅ | rule_moon_mars_conjunct |
| evi_pit_ma008 | "conflicts, anger, aggression" | transit_moon, natal_mars, aspect_square | Square=friction | Moon□Mars = emotional anger | Medium | ✅ | rule_moon_mars_square |
| evi_pit_ma009 | "optimism, emotional uplift" | transit_moon, natal_jupiter, aspect_conjunct | Moon+Jupiter = emotional expansion | Moon☌Jupiter = emotional optimism | High | ✅ | rule_moon_jupiter_conjunct |
| evi_pit_ma010 | "depression, loneliness, restriction" | transit_moon, natal_saturn, aspect_conjunct | Moon+Saturn = emotional weight | Moon☌Saturn = emotional heaviness | High | ✅ | rule_moon_saturn_conjunct |
| evi_pit_ma011 | "emotional coldness, duty over feeling" | transit_moon, natal_saturn, aspect_square | Square=friction | Moon□Saturn = emotional restriction | Medium | ✅ | rule_moon_saturn_square |
| evi_pit_ma012 | "sudden emotional changes" | transit_moon, natal_uranus, aspect_conjunct | Moon+Uranus = emotional disruption | Moon☌Uranus = emotional surprise | High | ✅ | rule_moon_uranus_conjunct |
| evi_pit_ma013 | "highly sensitive, imaginative" | transit_moon, natal_neptune, aspect_conjunct | Moon+Neptune = emotional imagination | Moon☌Neptune = sensitivity peak | High | ✅ | rule_moon_neptune_conjunct |
| evi_pit_ma014 | "confusion, deception possible" | transit_moon, natal_neptune, aspect_square | Square=friction | Moon□Neptune = emotional confusion | Medium | ✅ | rule_moon_neptune_square |
| evi_pit_ma015 | "intense emotional experiences" | transit_moon, natal_pluto, aspect_conjunct | Moon+Pluto = emotional depth | Moon☌Pluto = emotional intensity | High | ✅ | rule_moon_pluto_conjunct |
| evi_pit_ma016 | "power struggles, manipulation" | transit_moon, natal_pluto, aspect_square | Square=friction | Moon□Pluto = emotional power struggle | Medium | ✅ | rule_moon_pluto_square |

**Cross-System Concept Mapping Layer (Aspect Patterns)**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_lunar_solar_cycle | Personal new/full moon phases | 日月同宫/对冲 | moon_sun_aspects | sun_moon_symbol | conscious_unconscious | Will-emotion cycle |
| concept_emotional_communication | Mind-feeling integration | 印星泄食伤 | moon_mercury_aspects | speaking_symbol | emotional_expression | Thought-feeling link |
| concept_emotional_love | Feeling and relationship | 印星生比劫 | moon_venus_aspects | heart_symbol | attachment_style | Love-emotion connection |
| concept_emotional_action | Feeling and assertion | 印星制杀 | moon_mars_aspects | sword_symbol | emotional_arousal | Feeling-action link |
| concept_emotional_expansion | Feeling and growth | 印星化杀为权 | moon_jupiter_aspects | balloon_symbol | emotional_optimism | Uplift or excess |
| concept_emotional_restriction | Feeling and limitation | 印星被官克 | moon_saturn_aspects | wall_symbol | emotional_suppression | Heaviness or discipline |
| concept_emotional_disruption | Feeling and surprise | 印星被冲 | moon_uranus_aspects | lightning_symbol | emotional_dysregulation | Change or instability |
| concept_emotional_imagination | Feeling and fantasy | 印星逢偏印 | moon_neptune_aspects | mist_symbol | emotional_diffusion | Sensitivity or confusion |
| concept_emotional_transformation | Feeling and power | 印星见七杀 | moon_pluto_aspects | phoenix_symbol | emotional_intensity | Depth or obsession |
<!-- L2.5_END -->

---

## Progress Tracker

| Section | Content | Entries | Status |
|---------|---------|---------|--------|
| Moon Houses | 1H-12H | 12/12 | ✅ COMPLETE |
| Moon-Sun Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Moon Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Mercury Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Venus Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Mars Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Jupiter Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Saturn Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Uranus Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Neptune Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |
| Moon-Pluto Aspects | Conj, Sext, Sq, Tri, Opp | 5/5 | ✅ COMPLETE |

**Total Progress**: 62/62 entries (100%) ✅ CHAPTER COMPLETE

---

**文件状态**: Chapter 5 Moon - ✅ 精校完成  
**当前日期**: 2025-11-29  
**模板**: Western Texts v2.1 Bilingual  
**作者**: Robert Hand
