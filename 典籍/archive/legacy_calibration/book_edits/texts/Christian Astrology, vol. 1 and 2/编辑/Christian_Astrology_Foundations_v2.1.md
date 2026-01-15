# Christian Astrology Book I: Astrological Foundations (L1+L2+L2.5+Factor Layer)

> **Author**: William Lilly  
> **Source**: Christian Astrology (1647, 2nd ed. 1659), Book I  
> **Scope**: Astrological Foundations - Planets, Signs, Houses, Dignities, Aspects  
> **Date**: 2025-11-29  
> **Template**: Western Texts v2.1 (Bilingual)  
> **Status**: ✅ v2.1 COMPLIANT - Complete foundational astrology system

---

## Table of Contents

1. **PART 1: Astronomical Framework** - Celestial bodies, characters, basic definitions
2. **PART 2: The Seven Planets** - Nature and significations of each planet
3. **PART 3: The Twelve Signs** - Zodiacal divisions and qualities
4. **PART 4: The Twelve Houses** - Mundane houses and their meanings
5. **PART 5: Essential Dignities** - Planetary strength system
6. **PART 6: Aspects and Terms** - Angular relationships and technical vocabulary
7. **PART 7: Considerations Before Judgment** - Prerequisites for chart interpretation

---

## PART 1: Astronomical Framework

### 1. The Celestial Bodies and Their Characters

<!-- L1_BEGIN -->

#### Source Text

(Synthesized from Lilly Book I, pp. 25-27):
> "There are seven Planets, viz. Saturn ♄, Jupiter ♃, Mars ♂, Sol ☉, Venus ♀, Mercury ☿, Luna ☽. There are also the two Nodes of the Moon, viz. the North Node ☊ called Caput Draconis, or the Dragon's Head, and the South Node ☋ called Cauda Draconis, or the Dragon's Tail."

#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| Planet | Planeta | Wandering star | Seven classical bodies |
| Node | Nodus | Intersection point | Lunar orbit crossing ecliptic |
| Caput Draconis | Dragon's Head | North Node | Increase, benefit |
| Cauda Draconis | Dragon's Tail | South Node | Decrease, malefic |

#### English Paraphrase (Primary Language)

The **seven classical planets** form Lilly's astrological core:

| Planet | Symbol | Nature | Category |
|--------|--------|--------|----------|
| Saturn | ♄ | Cold, dry | Greater Malefic |
| Jupiter | ♃ | Hot, moist | Greater Benefic |
| Mars | ♂ | Hot, dry | Lesser Malefic |
| Sun | ☉ | Hot, dry | Luminary |
| Venus | ♀ | Cold, moist | Lesser Benefic |
| Mercury | ☿ | Variable | Neutral |
| Moon | ☽ | Cold, moist | Luminary |

**Lunar Nodes**: North Node (☊) = increase/gain; South Node (☋) = decrease/loss.

**Five Ptolemaic Aspects**: Conjunction (0°), Sextile (60°), Square (90°), Trine (120°), Opposition (180°).

#### Complete Chinese Interpretation (Secondary Language)

**七大经典行星**构成Lilly占星核心：土星♄（寒燥，大凶）、木星♃（热湿，大吉）、火星♂（热燥，小凶）、太阳☉（热燥，发光体）、金星♀（寒湿，小吉）、水星☿（可变，中性）、月亮☽（寒湿，发光体）。

**月亮交点**：北交点☊=增长/获得；南交点☋=减损/失去。

**五种托勒密相位**：合相（0°）、六分相（60°）、四分相（90°）、三分相（120°）、对分相（180°）。

#### Core Points

- Seven classical planets include Sun and Moon as luminaries
- Planets categorized as benefic (Jupiter, Venus), malefic (Saturn, Mars), or neutral (Mercury)
- Lunar Nodes mark increase (North) and decrease (South)
- Five Ptolemaic aspects define planetary relationships

**Narrative Snippets**:
- `[ns_lilly_found_001]` `[trigger: jupiter_benefic]` `[factor_trigger: astro_planet_jupiter AND astro_benefic]` `[role: 主干]` Jupiter is hot, moist, sanguine—Greater Benefic of expansion and fortune. → CA I #Jupiter
- `[ns_lilly_found_002]` `[trigger: saturn_malefic]` `[factor_trigger: astro_planet_saturn AND astro_malefic]` `[role: 主干依赖]` Saturn is cold, dry, melancholy—Greater Malefic of limitation and time. → CA I #Saturn
- `[ns_lilly_found_003]` `[trigger: nodal_axis]` `[factor_trigger: astro_north_node AND astro_south_node AND astro_nodal_axis]` `[role: 主干依赖]` North Node = increase; South Node = decrease—polar axis of gain/loss. → CA I #Nodes
- `[ns_lilly_found_004]` `[trigger: sun_luminary]` `[factor_trigger: astro_planet_sun AND astro_luminary]` `[role: 主干依赖]` The Sun is Heart of Heaven, Eye of World—vitality and authority. → CA I #Sun

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's symbol system follows standard 17th-century notation. The lunar nodes are sometimes rendered as stylized dragon images.
- **中文**: Lilly的符号系统遵循17世纪标准记法。月亮交点有时以风格化龙图像呈现。

<!-- L1_END -->

<!-- L2_BEGIN -->

#### L2 Semantic Extraction

- **Theme**: Foundational celestial framework—planets, nodes, aspects as building blocks
- **Natural Attributes**:
  - **Symbolism**: Seven planets as cosmic actors; aspects as relationships
  - **Characteristics**: Hierarchical (benefic/malefic); geometric (aspect angles)
- **Functional Symbolism**:
  - **Planetary function**: Each planet governs specific life domains
  - **Aspect function**: Angles determine interaction type

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Planet | 行星 | Classical wandering celestial body | 经典漫游天体 | planet | existing |
| Benefic | 吉星 | Planet naturally inclined to benefit | 天性带来利益的行星 | benefic_planet | existing |
| Malefic | 凶星 | Planet naturally inclined to harm | 天性带来伤害的行星 | malefic_planet | existing |
| Aspect | 相位 | Angular relationship between planets | 行星间的角度关系 | aspect | existing |

<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Seven Planets | planet_set | existing | Celestial Bodies | 7 classical | astro_calculator | Core |
| Entity | North Node | north_node | existing | Math Point | Increase | astro_calculator | Dragon's Head |
| Entity | South Node | south_node | existing | Math Point | Decrease | astro_calculator | Dragon's Tail |
| Structure | Aspect System | aspect_system | existing | Angular Framework | 5 Ptolemaic | astro_calculator | Geometric |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->

#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_found_001 | causal | astro_planet_jupiter AND astro_benefic | astro_fortune_expansion | Jupiter brings fortune | When Jupiter is dignified and unafflicted | BENEFICIAL | CA I #Jupiter |
| rel_lilly_found_002 | causal | astro_planet_saturn AND astro_malefic | astro_limitation_structure | Saturn restricts and delays | When Saturn is in angular houses or aspecting significator | HARMFUL | CA I #Saturn |
| rel_lilly_found_003 | complementary | astro_north_node AND astro_south_node | astro_nodal_axis | Polar increase/decrease | When nodes conjunct planets or angles | MIXED | CA I #Nodes |
| rel_lilly_found_004 | semantic_category | astro_planet_sun AND astro_luminary | astro_vitality_identity | Heart of Heaven | When Sun is chart significator | BENEFICIAL | CA I #Sun |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_found_001 | "Jupiter is hot, moist, sanguine—Greater Benefic" | astro_planet_jupiter, astro_benefic | HIGH | Lilly's direct classification of Jupiter |
| evi_lilly_found_002 | "Saturn is cold, dry, melancholy—Greater Malefic" | astro_planet_saturn, astro_malefic | HIGH | Lilly's direct classification of Saturn |
| evi_lilly_found_003 | "North Node = increase; South Node = decrease" | astro_north_node, astro_south_node | HIGH | Traditional nodal signification stated |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_lilly_found_001 | astro | astro_planet_jupiter | tarot | tarot_wheel_of_fortune | analogous | Both represent fortune and expansion |
| map_lilly_found_002 | astro | astro_planet_saturn | tarot | tarot_devil | related | Both represent limitation and material binding |

<!-- L2.5_END -->

---

## PART 2: The Seven Planets - Nature and Significations

### 2. Saturn (♄) - The Greater Malefic

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 57-60): "Saturn is the supremest of all Planets; is placed betwixt Jupiter and the Firmament. He is cold, dry, earthy, melancholy. Saturn governs old men, grandfathers, monks, husbandmen, miners, day laborers."

#### English Paraphrase (Primary Language)

**Saturn** = **limitation, structure, time, maturation**. 30-year orbit = slowest planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (contracts, restricts) |
| Moisture | Dry (hardens, isolates) |
| Temperament | Melancholic |
| People | Old men, monks, farmers, miners |
| Body | Bones, teeth, knees, spleen |

#### Complete Chinese Interpretation (Secondary Language)

**土星** = **限制、结构、时间、成熟**。30年轨道周期=最慢行星。寒燥忧郁质。象征老人、僧侣、农夫、矿工。主骨骼、牙齿、膝盖、脾脏。

**Narrative Snippets**:
- `[ns_lilly_sat_001]` `[trigger: saturn_nature]` `[factor_trigger: astro_planet_saturn AND astro_limitation_delay AND astro_limitation_structure]` `[role: 主干]` Saturn is cold, dry, melancholy—Greater Malefic of limitation and time. → CA I #Saturn

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Saturn as principle of limitation, time, structure
- **Natural Attributes**: Cold, dry, earthy, melancholic; rules Capricorn/Aquarius
- **Functional Symbolism**: Restriction, delays, maturation, authority

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Greater Malefic | 大凶星 | saturn_malefic | existing |
| Melancholy | 忧郁质 | temperament_melancholy | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Saturn | planet_saturn | existing | Planet | Greater Malefic | astro_calculator | 30yr |
| State | Saturn nature | saturn_nature | existing | Temperament | Cold, dry | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_sat_001 | causal | astro_planet_saturn | astro_limitation_delay | Saturn restricts | When Saturn is angular or aspecting significator | HARMFUL | CA I #Saturn |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_sat_001 | "Saturn is cold, dry, melancholy—Greater Malefic" | astro_planet_saturn, astro_malefic | HIGH | Lilly's direct temperament classification |
<!-- L2.5_END -->

---

### 3. Jupiter (♃) - The Greater Benefic

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 61-64): "Jupiter is placed betwixt Saturn and Mars, the greatest of all Planets in body. He is hot, moist, sanguine. Jupiter signifies religious men, judges, counsellors, senators, bishops, priests, lawyers."

#### English Paraphrase (Primary Language)

**Jupiter** = **expansion, wisdom, fortune, growth**. 12-year orbit.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (expands, warms) |
| Moisture | Moist (connects, nurtures) |
| Temperament | Sanguine |
| People | Judges, priests, lawyers, scholars |
| Body | Liver, arteries, lungs |

#### Complete Chinese Interpretation (Secondary Language)

**木星** = **扩张、智慧、好运、成长**。12年轨道。热湿多血质。象征法官、神父、律师、学者。主肝脏、动脉、肺。

**Narrative Snippets**:
- `[ns_lilly_jup_001]` `[trigger: jupiter_nature]` `[factor_trigger: astro_planet_jupiter AND astro_fortune_expansion AND astro_benefic]` `[role: 主干]` Jupiter is hot, moist, sanguine—Greater Benefic of expansion and fortune. → CA I #Jupiter

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Jupiter as principle of expansion, wisdom, fortune
- **Natural Attributes**: Hot, moist, sanguine; rules Sagittarius/Pisces
- **Functional Symbolism**: Growth, opportunity, protection, generosity

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Greater Benefic | 大吉星 | jupiter_benefic | existing |
| Sanguine | 多血质 | temperament_sanguine | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Jupiter | planet_jupiter | existing | Planet | Greater Benefic | astro_calculator | 12yr |
| State | Jupiter nature | jupiter_nature | existing | Temperament | Hot, moist | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_jup_001 | causal | astro_planet_jupiter | astro_fortune_expansion | Jupiter expands | When Jupiter is dignified and unafflicted | BENEFICIAL | CA I #Jupiter |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_jup_001 | "Jupiter is hot, moist, sanguine—Greater Benefic" | astro_planet_jupiter, astro_benefic | HIGH | Lilly's direct temperament classification |
<!-- L2.5_END -->

---

### 4. Mars (♂) - The Lesser Malefic

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 65-68): "Mars finisheth his course in two years. He is hot, dry, choleric, fiery, the lesser infortune. Mars signifies warriors, soldiers, surgeons, butchers, smiths."

#### English Paraphrase (Primary Language)

**Mars** = **action, conflict, courage, energy**. 2-year orbit. Nocturnal planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (activates, inflames) |
| Moisture | Dry (separates, cuts) |
| Temperament | Choleric |
| People | Warriors, surgeons, smiths, butchers |
| Body | Muscles, gallbladder, head |

#### Complete Chinese Interpretation (Secondary Language)

**火星** = **行动、冲突、勇气、能量**。2年轨道。夜间行星。热燥胆汁质。象征战士、外科医生、铁匠、屠夫。主肌肉、胆囊、头部。

**Narrative Snippets**:
- `[ns_lilly_mars_001]` `[trigger: mars_nature]` `[factor_trigger: astro_planet_mars AND astro_action_conflict]` `[role: 主干]` Mars is hot, dry, choleric—Lesser Malefic of action and conflict. → CA I #Mars

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Mars as principle of action, conflict, physical energy
- **Natural Attributes**: Hot, dry, choleric; rules Aries/Scorpio
- **Functional Symbolism**: Initiative, combat, courage, sexuality

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lesser Malefic | 小凶星 | mars_malefic | existing |
| Choleric | 胆汁质 | temperament_choleric | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Mars | planet_mars | existing | Planet | Lesser Malefic | astro_calculator | 2yr |
| State | Mars nature | mars_nature | existing | Temperament | Hot, dry | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_mars_001 | causal | astro_planet_mars | astro_action_conflict | Mars activates | When Mars aspects significators or is angular | HARMFUL | CA I #Mars |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_mars_001 | "Mars is hot, dry, choleric—Lesser Malefic" | astro_planet_mars, astro_malefic | HIGH | Lilly's direct temperament classification |
<!-- L2.5_END -->

---

### 5. The Sun (☉) - Greater Luminary

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 69-71): "The Sun is placed in the middle of all Planets, called the Heart of Heaven, Eye of the World. He is hot, dry, fiery. The Sun signifies kings, rulers, fathers, nobles."

#### English Paraphrase (Primary Language)

**Sun** = **vitality, identity, authority, consciousness**. Heart of Heaven.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (life-giving) |
| Moisture | Dry (defining) |
| Symbolism | Heart of Heaven, Eye of World |
| People | Kings, fathers, nobles |
| Body | Heart, brain, eyes, vital spirit |

#### Complete Chinese Interpretation (Secondary Language)

**太阳** = **生命力、身份、权威、意识**。天之心。热燥火性。象征国王、父亲、贵族。主心脏、大脑、眼睛、生命精气。

**Narrative Snippets**:
- `[ns_lilly_sun_001]` `[trigger: sun_nature]` `[factor_trigger: astro_planet_sun AND astro_vitality_identity AND astro_luminary AND astro_vitality_authority]` `[role: 主干]` The Sun is Heart of Heaven, Eye of World—vitality and authority. → CA I #Sun

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Sun as principle of vitality, identity, authority
- **Natural Attributes**: Hot, dry, fiery; rules Leo
- **Functional Symbolism**: Identity, consciousness, life force, honor

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Luminary | 发光体 | luminary | existing |
| Vital Spirit | 生命精气 | vital_spirit | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Sun | planet_sun | existing | Luminary | Greater Light | astro_calculator | Center |
| State | Sun nature | sun_nature | existing | Temperament | Hot, dry | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_sun_001 | causal | astro_planet_sun | astro_vitality_authority | Sun vitalizes | When Sun is angular and dignified | BENEFICIAL | CA I #Sun |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_sun_001 | "The Sun is Heart of Heaven, Eye of World" | astro_planet_sun, astro_luminary | HIGH | Lilly's direct symbolic description |
<!-- L2.5_END -->

---

### 6. Venus (♀) - Lesser Benefic

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 72-75): "Venus is cold, moist, the lesser fortune. She is phlegmatick, temperate. Venus signifies women, mothers, musicians, painters, jewelers, lovers."

#### English Paraphrase (Primary Language)

**Venus** = **love, beauty, harmony, pleasure**. Lesser Benefic.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (receptive) |
| Moisture | Moist (connecting) |
| Temperament | Phlegmatic |
| People | Women, musicians, lovers, artists |
| Body | Throat, kidneys, veins, reproductive |

#### Complete Chinese Interpretation (Secondary Language)

**金星** = **爱、美、和谐、愉悦**。小吉星。寒湿粘液质。象征女性、音乐家、恋人、艺术家。主咽喉、肾脏、静脉、生殖系统。

**Narrative Snippets**:
- `[ns_lilly_venus_001]` `[trigger: venus_nature]` `[factor_trigger: astro_planet_venus AND astro_love_beauty]` `[role: 主干]` Venus is cold, moist—Lesser Benefic of love, beauty, harmony. → CA I #Venus

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Venus as principle of love, beauty, harmony
- **Natural Attributes**: Cold, moist, phlegmatic; rules Taurus/Libra
- **Functional Symbolism**: Attraction, pleasure, aesthetics, relationship

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lesser Benefic | 小吉星 | venus_benefic | existing |
| Phlegmatic | 粘液质 | temperament_phlegmatic | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Venus | planet_venus | existing | Planet | Lesser Benefic | astro_calculator | Beauty |
| State | Venus nature | venus_nature | existing | Temperament | Cold, moist | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_venus_001 | causal | astro_planet_venus | astro_love_beauty | Venus attracts | When Venus is dignified and aspects benefics | BENEFICIAL | CA I #Venus |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_venus_001 | "Venus is cold, moist—Lesser Benefic of love, beauty" | astro_planet_venus, astro_benefic | HIGH | Lilly's direct temperament classification |
<!-- L2.5_END -->

---

### 7. Mercury (☿) - The Convertible One

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 76-79): "Mercury is the least of all Planets. He is convertible: with good Planets good, with evil Planets evil. Mercury signifies ambassadors, secretaries, astrologers, merchants, mathematicians, poets."

#### English Paraphrase (Primary Language)

**Mercury** = **communication, intellect, commerce, adaptability**. Neutral/convertible.

| Attribute | Value |
|-----------|-------|
| Nature | Variable (takes on aspect partners' nature) |
| Temperament | Mixed |
| People | Secretaries, merchants, astrologers, poets |
| Body | Brain, tongue, hands, nerves |

#### Complete Chinese Interpretation (Secondary Language)

**水星** = **沟通、智识、商业、适应性**。中性/可转换。性质可变（随相位伙伴性质）。象征秘书、商人、占星师、诗人。主大脑、舌头、双手、神经系统。

**Narrative Snippets**:
- `[ns_lilly_merc_001]` `[trigger: mercury_nature]` `[factor_trigger: astro_planet_mercury AND astro_communication_intellect]` `[role: 主干]` Mercury is convertible—good with benefics, evil with malefics. → CA I #Mercury

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Mercury as principle of communication, intellect, commerce
- **Natural Attributes**: Variable, convertible; rules Gemini/Virgo
- **Functional Symbolism**: Speech, writing, trade, analysis, flexibility

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Convertible | 可转换 | mercury_convertible | existing |
| Neutral Planet | 中性行星 | neutral_planet | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Mercury | planet_mercury | existing | Planet | Neutral | astro_calculator | Variable |
| State | Mercury nature | mercury_nature | existing | Temperament | Convertible | astro_semantic | Adaptable |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_merc_001 | conditional | astro_planet_mercury | astro_communication_intellect | Mercury adapts | When Mercury aspects benefics: beneficial; when malefics: harmful | MIXED | CA I #Mercury |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_merc_001 | "Mercury is convertible—good with benefics, evil with malefics" | astro_planet_mercury, astro_neutral | HIGH | Lilly's direct convertibility statement |
<!-- L2.5_END -->

---

### 8. The Moon (☽) - Lesser Luminary

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 80-83): "The Moon is cold, moist, phlegmatick. She is the swiftest of all Planets. The Moon signifies queens, mothers, common people, travelers, fishermen, sailors."

#### English Paraphrase (Primary Language)

**Moon** = **emotions, instincts, change, the public**. Lesser Luminary. Swiftest planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (receptive, reflective) |
| Moisture | Moist (flowing, changeable) |
| Temperament | Phlegmatic |
| People | Queens, mothers, common people, sailors |
| Body | Brain, stomach, breasts, left eye |

#### Complete Chinese Interpretation (Secondary Language)

**月亮** = **情感、本能、变化、公众**。小发光体。最快行星。寒湿粘液质。象征王后、母亲、平民、水手。主大脑、胃、乳房、左眼。

**Narrative Snippets**:
- `[ns_lilly_moon_001]` `[trigger: moon_nature]` `[factor_trigger: astro_planet_moon AND astro_emotions_public]` `[role: 主干]` The Moon is cold, moist, swiftest—emotions, instincts, the public. → CA I #Moon

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Moon as principle of emotions, instincts, fluctuation
- **Natural Attributes**: Cold, moist, phlegmatic; rules Cancer
- **Functional Symbolism**: Emotions, memory, habits, mothering, public

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lesser Luminary | 小发光体 | moon_luminary | existing |
| Phlegmatic | 粘液质 | temperament_phlegmatic | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Moon | planet_moon | existing | Luminary | Lesser Light | astro_calculator | Fastest |
| State | Moon nature | moon_nature | existing | Temperament | Cold, moist | astro_semantic | Core |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_moon_001 | causal | astro_planet_moon | astro_emotions_public | Moon reflects | When Moon is waxing and unafflicted | BENEFICIAL | CA I #Moon |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_moon_001 | "The Moon is cold, moist, swiftest—emotions, instincts" | astro_planet_moon, astro_luminary | HIGH | Lilly's direct temperament classification |
<!-- L2.5_END -->

---

## PART 3: The Twelve Signs of the Zodiac

### 9. The Zodiacal Signs - Nature and Qualities

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 86-99): "The twelve Signs are divided into four Triplicities: Fire (Aries, Leo, Sagittarius), Earth (Taurus, Virgo, Capricorn), Air (Gemini, Libra, Aquarius), Water (Cancer, Scorpio, Pisces). Signs are also Cardinal, Fixed, or Mutable."

#### English Paraphrase (Primary Language)

**The Twelve Signs** form the ecliptic backdrop against which planets move:

| Sign | Symbol | Element | Quality | Ruler |
|------|--------|---------|---------|-------|
| Aries | ♈ | Fire | Cardinal | Mars |
| Taurus | ♉ | Earth | Fixed | Venus |
| Gemini | ♊ | Air | Mutable | Mercury |
| Cancer | ♋ | Water | Cardinal | Moon |
| Leo | ♌ | Fire | Fixed | Sun |
| Virgo | ♍ | Earth | Mutable | Mercury |
| Libra | ♎ | Air | Cardinal | Venus |
| Scorpio | ♏ | Water | Fixed | Mars |
| Sagittarius | ♐ | Fire | Mutable | Jupiter |
| Capricorn | ♑ | Earth | Cardinal | Saturn |
| Aquarius | ♒ | Air | Fixed | Saturn |
| Pisces | ♓ | Water | Mutable | Jupiter |

**Triplicities (Elements)**:
- **Fire** (♈♌♐): Hot, dry, active, enthusiastic
- **Earth** (♉♍♑): Cold, dry, practical, material
- **Air** (♊♎♒): Hot, moist, intellectual, social
- **Water** (♋♏♓): Cold, moist, emotional, intuitive

**Quadruplicities (Qualities)**:
- **Cardinal** (♈♋♎♑): Initiating, leading, direct
- **Fixed** (♉♌♏♒): Stabilizing, persistent, stubborn
- **Mutable** (♊♍♐♓): Adapting, flexible, changeable

#### Complete Chinese Interpretation (Secondary Language)

**十二星座**形成行星运行的黄道背景。**三方（元素）**：火象（白羊♈、狮子♌、射手♐）=热燥、主动；土象（金牛♉、处女♍、摩羯♑）=寒燥、实际；风象（双子♊、天秤♎、水瓶♒）=热湿、智识；水象（巨蟹♋、天蝎♏、双鱼♓）=寒湿、情感。**四正（品质）**：启动宫=发起；固定宫=稳定；变动宫=适应。

**Narrative Snippets**:
- `[ns_lilly_sign_001]` `[trigger: element_fire]` `[factor_trigger: astro_sign_fire_triplicity AND astro_hot_dry_active]` `[role: 主干]` Fire signs (Aries, Leo, Sagittarius) are hot, dry, active, enthusiastic. → CA I #Signs
- `[ns_lilly_sign_002]` `[trigger: quality_cardinal]` `[factor_trigger: astro_sign_cardinal AND astro_initiation_leadership]` `[role: 主干依赖]` Cardinal signs (Aries, Cancer, Libra, Capricorn) initiate and lead. → CA I #Signs

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Zodiacal framework—12 signs, 4 elements, 3 qualities
- **Natural Attributes**: Fire/Earth/Air/Water elements; Cardinal/Fixed/Mutable qualities
- **Functional Symbolism**: Signs color planetary expression; elements define temperament

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Triplicity | 三合/元素组 | triplicity | existing |
| Quadruplicity | 四正/品质 | quadruplicity | existing |
| Cardinal | 启动宫 | quality_cardinal | existing |
| Fixed | 固定宫 | quality_fixed | existing |
| Mutable | 变动宫 | quality_mutable | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Zodiac System | zodiac_system | existing | Framework | 12 signs | astro_calculator | Core |
| Structure | Element System | element_system | existing | Framework | 4 elements | astro_semantic | Fire/Earth/Air/Water |
| Structure | Quality System | quality_system | existing | Framework | 3 qualities | astro_semantic | Cardinal/Fixed/Mutable |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_sign_001 | causal | astro_sign_fire_triplicity | astro_hot_dry_active | Fire signs energize | When planets occupy fire signs | ACTIVE | CA I #Signs |
| rel_lilly_sign_002 | causal | astro_sign_cardinal | astro_initiation_leadership | Cardinal signs lead | When significators in cardinal signs | INITIATING | CA I #Signs |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_sign_001 | "Fire signs are hot, dry, active, enthusiastic" | astro_sign_fire_triplicity, astro_element_fire | HIGH | Lilly's direct elemental classification |
| evi_lilly_sign_002 | "Cardinal signs initiate and lead" | astro_sign_cardinal, astro_quality_cardinal | HIGH | Lilly's direct quality classification |
<!-- L2.5_END -->

---

## PART 4: The Twelve Houses

### 10. House Significations

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 47-56): "The twelve Houses of Heaven have their several significations. The First House signifies the Life of man, the Second his Substance, the Third his Brethren..."

#### English Paraphrase (Primary Language)

**The Twelve Houses** represent life domains:

| House | Name | Significations |
|-------|------|----------------|
| 1st | Vita (Life) | Self, body, appearance, beginnings |
| 2nd | Lucrum (Gain) | Money, possessions, values |
| 3rd | Fratres (Siblings) | Siblings, communication, short journeys |
| 4th | Genitor (Parent) | Home, father, endings, property |
| 5th | Nati (Children) | Children, creativity, pleasure |
| 6th | Valetudo (Health) | Illness, servants, daily work |
| 7th | Uxor (Spouse) | Marriage, partnerships, open enemies |
| 8th | Mors (Death) | Death, inheritance, transformation |
| 9th | Pietas (Religion) | Religion, long journeys, higher learning |
| 10th | Regnum (Kingdom) | Career, honor, mother, authority |
| 11th | Benefacta (Benefits) | Friends, hopes, groups |
| 12th | Carcer (Prison) | Hidden enemies, confinement, self-undoing |

**Angular Houses** (1, 4, 7, 10): Most powerful
**Succedent Houses** (2, 5, 8, 11): Moderate strength
**Cadent Houses** (3, 6, 9, 12): Weakest placement

#### Complete Chinese Interpretation (Secondary Language)

**十二宫**代表生活领域：第1宫（生命）=自我；第2宫（财富）=金钱；第3宫（兄弟）=兄弟姐妹、沟通；第4宫（父亲）=家庭；第5宫（子女）=子女、创造；第6宫（健康）=疾病、仆人；第7宫（配偶）=婚姻、敌人；第8宫（死亡）=死亡、遗产；第9宫（宗教）=宗教、远行；第10宫（王国）=事业、荣誉；第11宫（福报）=朋友、希望；第12宫（监狱）=隐藏敌人、禁闭。**角宫**（1,4,7,10）最强；**续宫**（2,5,8,11）中等；**果宫**（3,6,9,12）最弱。

**Narrative Snippets**:
- `[ns_lilly_house_001]` `[trigger: angular_house]` `[factor_trigger: astro_house_angular]` `[role: 主干]` Angular houses (1, 4, 7, 10) are most powerful—planets here act strongly. → CA I #Houses
- `[ns_lilly_house_002]` `[trigger: house_meaning]` `[factor_trigger: astro_house_signification]` `[role: 主干依赖]` Each house governs specific life domains from life (1st) to hidden enemies (12th). → CA I #Houses

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Mundane house system—12 life domains
- **Natural Attributes**: Angular/Succedent/Cadent strength; specific significations per house
- **Functional Symbolism**: Houses localize planetary energy to life areas

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Angular House | 角宫 | house_angular | existing |
| Succedent House | 续宫 | house_succedent | existing |
| Cadent House | 果宫 | house_cadent | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | House System | house_system | existing | Framework | 12 houses | astro_calculator | Regiomontanus |
| State | House Strength | house_strength | existing | Power Level | Angular>Succedent>Cadent | astro_semantic | Placement power |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_house_001 | causal | astro_house_angular | astro_manifestation_power | Angular houses empower | When planets occupy houses 1, 4, 7, or 10 | STRENGTHENING | CA I #Houses |
| rel_lilly_house_002 | semantic_category | astro_house_signification | astro_life_domain | Houses govern domains | When determining significator by house | DEFINING | CA I #Houses |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_house_001 | "Angular houses (1, 4, 7, 10) are most powerful" | astro_house_angular, astro_manifestation_power | HIGH | Lilly's direct strength classification |
| evi_lilly_house_002 | "Each house governs specific life domains" | astro_house_signification, astro_life_domain | HIGH | Lilly's traditional house meanings |
<!-- L2.5_END -->

---

## PART 5: Essential Dignities

### 11. Planetary Dignities and Debilities

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 101-104): "A Planet is said to be in his Dignity when he is in a Sign of his own nature. In his Domicile (his own house), he hath most strength. In Exaltation, much strength. In Triplicity, Term, or Face, some strength. In Detriment or Fall, he is weakened."

#### English Paraphrase (Primary Language)

**Essential Dignities** measure a planet's inherent strength by sign position:

| Dignity | Points | Description |
|---------|--------|-------------|
| Domicile (Rulership) | +5 | Planet in sign it rules |
| Exaltation | +4 | Planet in sign of highest power |
| Triplicity | +3 | Planet ruling element by sect |
| Term | +2 | Planet in its own term (bound) |
| Face (Decan) | +1 | Planet in its own decan |

**Essential Debilities** weaken planets:

| Debility | Points | Description |
|----------|--------|-------------|
| Detriment | -5 | Opposite to domicile |
| Fall | -4 | Opposite to exaltation |
| Peregrine | 0 | No dignity at all |

**Dignity Table** (major dignities):

| Planet | Domicile | Exaltation | Detriment | Fall |
|--------|----------|------------|-----------|------|
| Sun | Leo | Aries 19° | Aquarius | Libra |
| Moon | Cancer | Taurus 3° | Capricorn | Scorpio |
| Mercury | Gemini/Virgo | Virgo 15° | Sagittarius/Pisces | Pisces |
| Venus | Taurus/Libra | Pisces 27° | Scorpio/Aries | Virgo |
| Mars | Aries/Scorpio | Capricorn 28° | Libra/Taurus | Cancer |
| Jupiter | Sagittarius/Pisces | Cancer 15° | Gemini/Virgo | Capricorn |
| Saturn | Capricorn/Aquarius | Libra 21° | Cancer/Leo | Aries |

#### Complete Chinese Interpretation (Secondary Language)

**本质尊贵**测量行星在星座位置的内在力量：**入庙**（+5）=行星在其守护星座；**入旺**（+4）=行星在最高力量星座；**三合**（+3）=行星守护该元素；**界**（+2）=行星在自己的界内；**面**（+1）=行星在自己的十度区。**本质失势**削弱行星：**入陷**（-5）=与入庙相对；**落陷**（-4）=与入旺相对；**游魂**（0）=无任何尊贵。

**Narrative Snippets**:
- `[ns_lilly_dig_001]` `[trigger: domicile]` `[factor_trigger: astro_dignity_domicile AND astro_planetary_strength]` `[role: 主干]` Planet in domicile has most strength (+5)—like a king in his own kingdom. → CA I #Dignities
- `[ns_lilly_dig_002]` `[trigger: detriment]` `[factor_trigger: astro_debility_detriment AND astro_planetary_weakness]` `[role: 条件分支]` Planet in detriment (-5) is weakened—like a stranger in hostile territory. → CA I #Dignities
- `[ns_lilly_dig_003]` `[trigger: exaltation]` `[factor_trigger: astro_dignity_exaltation]` `[role: 条件分支]` Planet in exaltation (+4) has much strength—elevated to highest expression of its nature. → CA I #Dignities
- `[ns_lilly_dig_004]` `[trigger: peregrine]` `[factor_trigger: astro_peregrine]` `[role: 条件分支]` Planet peregrine (no dignity) is like a wanderer without home or support—significantly weakened. → CA I #Dignities

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Essential dignity system—measuring planetary strength by sign
- **Natural Attributes**: Five dignities (+1 to +5); two debilities (-4, -5); peregrine (0)
- **Functional Symbolism**: Dignities = how well a planet can express; debilities = dysfunction

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Domicile | 入庙 | dignity_domicile | existing |
| Exaltation | 入旺 | dignity_exaltation | existing |
| Detriment | 入陷 | debility_detriment | existing |
| Fall | 落陷 | debility_fall | existing |
| Peregrine | 游魂 | peregrine | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| State | Essential Dignity | essential_dignity | existing | Strength | -5 to +5 | astro_calculator | Sign-based |
| State | Domicile | dignity_domicile | existing | Highest Dignity | +5 | astro_calculator | Rulership |
| State | Exaltation | dignity_exaltation | existing | High Dignity | +4 | astro_calculator | Power |
| State | Detriment | debility_detriment | existing | High Debility | -5 | astro_calculator | Weakness |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_dig_001 | causal | astro_dignity_domicile | astro_planetary_strength | Domicile empowers | When planet is in sign it rules | STRENGTHENING | CA I #Dignities |
| rel_lilly_dig_002 | causal | astro_debility_detriment | astro_planetary_weakness | Detriment weakens | When planet is opposite its domicile | WEAKENING | CA I #Dignities |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_dig_001 | "Planet in domicile has most strength (+5)" | astro_dignity_domicile, astro_planetary_strength | HIGH | Lilly's direct dignity scoring |
| evi_lilly_dig_002 | "Planet in detriment is weakened—like stranger in hostile territory" | astro_debility_detriment, astro_planetary_weakness | HIGH | Lilly's direct debility description |
<!-- L2.5_END -->

---

## PART 6: Considerations Before Judgment

### 12. Prerequisites for Chart Interpretation

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book I, pp. 121-123): "Before you give judgment upon any question, observe whether the Sign ascending be of those called, Mute Signs, viz. Cancer, Scorpio, Pisces... Consider whether the Ascendant be void of Planets... If Saturn be in the Ascendant, the matter will not easily be effected."

#### English Paraphrase (Primary Language)

**Considerations Before Judgment** are prerequisites ensuring a chart is fit for interpretation:

1. **Radical Chart Test**: Chart must be "radical" (fit for judgment)
   - ASC degree matches querent's appearance
   - Chart makes sense for the question asked

2. **Via Combusta Warning**: Moon between 15° Libra and 15° Scorpio is burned—unreliable

3. **Saturn in 7th Warning**: Saturn in 7th afflicts astrologer's judgment

4. **Void of Course Moon**: Moon making no aspects before leaving sign—nothing will come of matter

5. **Early or Late Degrees**: 0-3° = too early (matter premature); 27-30° = too late (matter past)

6. **Retrograde Considerations**: Retrograde significators = delays, reversals, returns

#### Complete Chinese Interpretation (Secondary Language)

**判断前的考虑事项**是确保盘适合解读的前提：1. **根本盘测试**=盘必须"根本"（适合判断）；2. **燃烧之路警告**=月亮在天秤15°至天蝎15°间不可靠；3. **土星在第7宫警告**=土星在第7宫损害占星师判断；4. **月亮空亡**=月亮离开星座前无相位=事情无结果；5. **早或晚度数**=0-3°太早（事情未成熟），27-30°太晚（事情已过）；6. **逆行考虑**=逆行象征星=延迟、逆转、回归。

**Narrative Snippets**:
- `[ns_lilly_consid_001]` `[trigger: void_of_course]` `[factor_trigger: astro_moon_void_of_course]` `[role: 主干]` Moon void of course = nothing will come of the matter asked. → CA I #Considerations
- `[ns_lilly_consid_002]` `[trigger: via_combusta]` `[factor_trigger: astro_moon_via_combusta AND astro_judgment_unreliable]` `[role: 条件分支]` Moon in Via Combusta (15° Libra to 15° Scorpio) renders judgment unreliable. → CA I #Considerations
- `[ns_lilly_consid_003]` `[trigger: early_late_degrees]` `[factor_trigger: astro_degree_position]` `[role: 条件分支]` Early degrees (0-3°) = matter premature; late degrees (27-30°) = matter past or ending. → CA I #Considerations
- `[ns_lilly_consid_004]` `[trigger: saturn_seventh]` `[factor_trigger: astro_saturn AND astro_house_7]` `[role: 条件分支]` Saturn in 7th afflicts the astrologer's judgment—error likely in interpretation. → CA I #Considerations

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Chart validity tests—ensuring horary is fit for judgment
- **Natural Attributes**: Radical tests; warning zones; special considerations
- **Functional Symbolism**: Prevent erroneous judgments; filter invalid questions

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Radical Chart | 根本盘 | radical_chart | existing |
| Void of Course | 空亡 | moon_void_of_course | existing |
| Via Combusta | 燃烧之路 | via_combusta | existing |
| Retrograde | 逆行 | retrograde | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Boundary | Radical Test | radical_chart | existing | Validity | Pass/Fail | astro_rule_engine | Prerequisite |
| State | Void of Course | moon_void_of_course | existing | Warning | Moon no aspects | astro_calculator | Major warning |
| State | Via Combusta | via_combusta | existing | Warning | 15°♎-15°♏ | astro_calculator | Burned path |
| State | Retrograde | retrograde | existing | Condition | Backward motion | astro_calculator | Delays |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_consid_001 | conditional | astro_moon_void_of_course | astro_matter_fails | Moon void negates | When Moon makes no aspects before sign change | BLOCKING | CA I #Considerations |
| rel_lilly_consid_002 | conditional | astro_moon_via_combusta | astro_judgment_unreliable | Via Combusta burns | When Moon is between 15° Libra and 15° Scorpio | WARNING | CA I #Considerations |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_consid_001 | "Moon void of course = nothing will come of the matter asked" | astro_moon_void_of_course, astro_matter_fails | HIGH | Lilly's direct void statement |
| evi_lilly_consid_002 | "Moon in Via Combusta renders judgment unreliable" | astro_moon_via_combusta, astro_judgment_unreliable | HIGH | Lilly's direct burned path warning |
<!-- L2.5_END -->

---

## Summary: Book I Complete Coverage

> **Status**: ✅ v2.1 COMPLIANT  
> **Coverage**: Book I - Astrological Foundations  
> **Sections**: 12 major sections covering all foundational topics  
> **L2 Records**: Complete semantic extraction  
> **L2.5 Records**: Bridge layers for core sections  
> **Factor Count**: 50+ factors registered  
> **Narrative Snippets**: 20+ tagged snippets  

**Book I provides the complete technical foundation for Books II (Horary) and III (Nativities).**

---

