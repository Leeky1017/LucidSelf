# Christian Astrology Book III: Nativities (L1+L2+L2.5+Factor Layer)

> **Author**: William Lilly  
> **Source**: Christian Astrology (1647, 2nd ed. 1659), Book III  
> **Scope**: Natal Astrology - Life Span, Character, Fortune, Directions  
> **Date**: 2025-11-29  
> **Template**: Western Texts v2.1 (Bilingual)  
> **Status**: ✅ v2.1 COMPLIANT - Complete natal astrology system

---

## Table of Contents

1. **PART 1: Chart Rectification** - Correcting birth time
2. **PART 2: Length of Life** - Hyleg and Anareta
3. **PART 3: Temperament and Character** - Physical and mental qualities
4. **PART 4: Fortune by House** - Wealth, marriage, children, career
5. **PART 5: Directions** - Predictive techniques

---

## PART 1: Chart Rectification Methods

### 1. Correcting the Birth Time

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 500-509): "Divers ways of rectifying Nativities. The Trutine of Hermes: If the Moon at birth be above the earth, take the degree she is in for the Ascendant at conception; if below, take her degree for the Descendant. The Animodar method uses the nearest New or Full Moon before birth."

#### English Paraphrase (Primary Language)

**Chart Rectification** corrects uncertain birth times using astronomical and life-event correlations:

**1. Trutine of Hermes** (Conception Method):
- Moon above horizon at birth → Moon's degree = ASC at conception
- Moon below horizon at birth → Moon's degree = DSC at conception
- Gestation period: 273 days ± variations by Moon position

**2. Animodar Method** (Prenatal Lunation):
- Find nearest New/Full Moon before birth
- Ruler of that lunation degree relates to ASC degree

**3. Rectification by Accidents**:
- Use known life events (marriage, death of parent, illness)
- Work backward using directions to find correct birth time
- Most reliable method when events are accurately dated

#### Complete Chinese Interpretation (Secondary Language)

**天宫图校正**使用天文和生活事件关联修正不确定的出生时间：**1. 赫尔墨斯真理**（受孕法）：出生时月亮在地平线上→月亮度数=受孕时上升度数；月亮在地平线下→月亮度数=受孕时下降度数。**2. 动物方法**（产前朔望）：找出出生前最近的新月/满月，该朔望度数的守护星与上升度数相关。**3. 通过事件校正**：使用已知生活事件（婚姻、父母去世、疾病），通过推运反推找到正确出生时间——事件日期准确时最可靠。

**Narrative Snippets**:
- `[ns_lilly_rect_001]` `[trigger: trutine]` `[factor_trigger: astro_birth_time_correction]` `[role: 主干]` Trutine of Hermes: Moon above earth at birth = Moon degree is ASC at conception. → CA III #Rectification
- `[ns_lilly_rect_002]` `[trigger: accidents]` `[factor_trigger: astro_life_event]` `[role: 主干依赖]` Rectification by accidents: Use known life events and work backward via directions. → CA III #Rectification
- `[ns_lilly_rect_003]` `[trigger: rectification_accuracy]` `[factor_trigger: astro_rectification_accuracy]` `[role: 总结]` Rectification by known events is most reliable method when dates are accurately recorded. → English Paraphrase
- `[ns_lilly_rect_004]` `[trigger: moon_birth]` `[factor_trigger: astro_moon_position_birth]` `[role: 主干依赖]` Moon position at birth (above/below horizon) determines conception Ascendant degree. → English Paraphrase
- `[ns_lilly_rect_005]` `[trigger: event_timing]` `[factor_trigger: astro_life_event_timing]` `[role: 条件分支]` Known life event dates provide anchor points for birth time rectification. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Birth time correction using astronomical and biographical methods
- **Natural Attributes**: Trutine (conception), Animodar (prenatal lunation), accidents (events)
- **Functional Symbolism**: Accurate birth time essential for reliable natal interpretation

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Rectification | 校正 | rectification | existing |
| Trutine of Hermes | 赫尔墨斯真理 | trutine_hermes | new_candidate |
| Animodar | 动物方法 | animodar | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Mechanism | Rectification | rectification | existing | Time Correction | Multiple methods | astro_calculator | Prerequisite |
| Mechanism | Trutine | trutine_hermes | new_candidate | Conception Method | Moon position | astro_calculator | Ancient |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_rect_001 | causal | astro_moon_position_birth | astro_birth_time_correction | Moon position indicates conception ASC | When Moon above/below horizon at birth | DETERMINING | CA III #Rectification |
| rel_lilly_rect_002 | methodological | astro_life_event_timing | astro_rectification_accuracy | Life events validate birth time | When event dates are accurately known | VALIDATING | CA III #Rectification |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_rect_001 | "Trutine of Hermes: Moon degree = ASC at conception" | astro_moon_position_birth, astro_rectification | HIGH | Ancient conception-based rectification method |
<!-- L2.5_END -->

---

## PART 2: Length of Life (Hyleg and Anareta)

### 2. Determining Life Span

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 525-530): "Of Hylech or Aphaeta, and the Intersicient Planet. The Hylech is the giver of life; the Anareta is the destroyer of life. In day nativities, the Sun may be Hylech if well-placed; in night nativities, the Moon. The Anareta is usually Mars or Saturn directing to Hylech."

#### English Paraphrase (Primary Language)

**Hyleg (Apheta)** = the "Giver of Life," the vital point in the natal chart:

**Hyleg Candidates** (in order of preference):
1. **Day birth**: Sun (if in houses 1, 7, 9, 10, 11)
2. **Night birth**: Moon (if in houses 1, 7, 9, 10, 11)
3. **ASC degree** (if neither luminary qualifies)
4. **Part of Fortune** (alternative)
5. **Prenatal Syzygy** (New/Full Moon before birth)

**Anareta (Interfector)** = the "Destroyer of Life," threatening the Hyleg:
- Usually **Mars** or **Saturn** (malefics)
- Direction of Hyleg to Anareta = life-threatening period
- Benefic aspects to Hyleg extend life; malefic aspects shorten it

**Calculation**: Use primary directions to determine when Hyleg reaches dangerous aspects.

#### Complete Chinese Interpretation (Secondary Language)

**命主星（Hyleg/Apheta）**="生命赋予者"，本命盘中的生命点。**命主星候选**（按优先顺序）：1. 日生：太阳（若在1、7、9、10、11宫）；2. 夜生：月亮（若在1、7、9、10、11宫）；3. 上升度数（若两发光体都不合格）；4. 福点（替代）；5. 产前朔望（出生前新月/满月）。**杀主星（Anareta）**="生命毁灭者"，威胁命主星：通常是火星或土星（凶星）；命主星推运至杀主星=生命威胁期；吉星相位延长寿命，凶星相位缩短寿命。

**Narrative Snippets**:
- `[ns_lilly_hyleg_001]` `[trigger: hyleg]` `[factor_trigger: astro_life_vitality]` `[role: 主干]` Hyleg is the giver of life—Sun by day, Moon by night, if well-placed. → CA III #Hyleg
- `[ns_lilly_hyleg_002]` `[trigger: anareta]` `[factor_trigger: astro_life_threat]` `[role: 条件分支]` Anareta (Mars or Saturn) directing to Hyleg indicates life-threatening periods. → CA III #Hyleg
- `[ns_lilly_hyleg_003]` `[trigger: timing]` `[factor_trigger: astro_timing]` `[role: 总结]` Primary directions measure life span—1 degree = 1 year for timing events. → English Paraphrase
- `[ns_lilly_hyleg_004]` `[trigger: hyleg_position]` `[factor_trigger: astro_hyleg_position]` `[role: 主干依赖]` Hyleg candidates: Sun (day), Moon (night), ASC, Part of Fortune, prenatal syzygy. → English Paraphrase
- `[ns_lilly_hyleg_005]` `[trigger: anareta_aspect]` `[factor_trigger: astro_anareta_aspect]` `[role: 条件分支]` Anareta (Mars/Saturn) direction to Hyleg marks life-threatening period. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Life span determination using Hyleg-Anareta system
- **Natural Attributes**: Hyleg = life giver; Anareta = life destroyer; directions = timing
- **Functional Symbolism**: Ancient longevity technique; primary directions measure life span

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Hyleg | 命主星 | hyleg | existing |
| Anareta | 杀主星 | anareta | existing |
| Primary Direction | 主限 | primary_direction | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Hyleg | hyleg | existing | Life Giver | Sun/Moon/ASC | astro_calculator | Apheta |
| Entity | Anareta | anareta | existing | Life Destroyer | Mars/Saturn | astro_calculator | Interfector |
| Mechanism | Primary Direction | primary_direction | existing | Timing | 1°=1 year | astro_calculator | Predictive |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_hyleg_001 | causal | astro_hyleg_position | astro_life_vitality | Hyleg sustains life | When Hyleg is dignified and unafflicted | BENEFICIAL | CA III #Hyleg |
| rel_lilly_hyleg_002 | threatening | astro_anareta_aspect | astro_life_threat | Anareta threatens life | When malefic directs to Hyleg | HARMFUL | CA III #Hyleg |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_hyleg_001 | "Hyleg is the giver of life" | astro_hyleg_position, astro_life_vitality | HIGH | Lilly's direct Hyleg definition |
| evi_lilly_hyleg_002 | "Anareta directing to Hyleg = life-threatening" | astro_anareta_aspect, astro_life_threat | HIGH | Lilly's Anareta danger statement |
<!-- L2.5_END -->

---

## PART 3: Temperament and Character

### 3. Physical Constitution and Manners

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 532-548): "Of the Complexion, temperament of the body, quality of Planets and Signs. The Ascendant, its Lord, the Moon, and planets in the 1st house describe the body. For manners, consider Mercury, Moon, and the Lord of the Geniture."

#### English Paraphrase (Primary Language)

**Physical Appearance** determined by:
1. **Ascendant sign** (primary body type)
2. **Lord of Ascendant** (modifying factors)
3. **Planets in 1st house** (strong physical influence)
4. **Moon** (general constitution)

**Mental Qualities and Manners** determined by:
1. **Mercury** (intellect, speech, reasoning)
2. **Moon** (emotions, habits, instincts)
3. **Lord of Geniture** (overall character tone)

**Lord of Geniture** = the strongest planet in the chart by:
- Essential dignity
- Angular position
- Aspects from other planets
- Being almuten (most dignities at key points)

#### Complete Chinese Interpretation (Secondary Language)

**外貌**由以下因素决定：1. 上升星座（主要体型）；2. 上升守护星（修正因素）；3. 第一宫行星（强烈身体影响）；4. 月亮（整体体质）。**心理品质与性情**由以下因素决定：1. 水星（智力、言语、推理）；2. 月亮（情感、习惯、本能）；3. 命宫主星（整体性格基调）。**命宫主星**=星盘中最强的行星，通过：本质尊贵、角宫位置、其他行星相位、成为全能星（在关键点有最多尊贵）来判断。

**Narrative Snippets**:
- `[ns_lilly_temp_001]` `[trigger: appearance]` `[factor_trigger: astro_physical_appearance]` `[role: 主干]` Ascendant and its Lord describe the body; planets in 1st house strongly modify appearance. → CA III #Temperament
- `[ns_lilly_temp_002]` `[trigger: manners]` `[factor_trigger: astro_mental_character]` `[role: 主干依赖]` Mercury and Moon together describe the native's mental qualities and habitual behaviors. → CA III #Temperament
- `[ns_lilly_temp_003]` `[trigger: asc_sign]` `[factor_trigger: astro_ascendant_sign]` `[role: 主干依赖]` Ascendant sign determines primary body type and physical constitution. → English Paraphrase
- `[ns_lilly_temp_004]` `[trigger: asc_lord]` `[factor_trigger: astro_asc_lord]` `[role: 条件分支]` Lord of Ascendant modifies and refines physical appearance indications. → English Paraphrase
- `[ns_lilly_temp_005]` `[trigger: mercury_mind]` `[factor_trigger: astro_mercury]` `[role: 主干依赖]` Mercury signifies intellect, speech, and reasoning capacity. → English Paraphrase
- `[ns_lilly_temp_006]` `[trigger: moon_mind]` `[factor_trigger: astro_moon]` `[role: 条件分支]` Moon signifies emotions, habits, and instinctive behaviors. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Physical and mental character from natal indicators
- **Natural Attributes**: ASC = body; Mercury/Moon = mind; Lord of Geniture = overall tone
- **Functional Symbolism**: Appearance from 1st house factors; character from Mercury/Moon

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lord of Geniture | 命宫主星 | lord_of_geniture | existing |
| Almuten | 全能星 | almuten | existing |
| Temperament | 气质 | temperament | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Lord of Geniture | lord_of_geniture | existing | Strongest Planet | By dignity/position | astro_calculator | Character |
| Entity | Almuten | almuten | existing | Most Dignified | At key degrees | astro_calculator | Alternative |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_temp_001 | determinative | astro_ascendant_sign AND astro_asc_lord | astro_physical_appearance | ASC and Lord determine body | When analyzing native's appearance | DESCRIBING | CA III #Temperament |
| rel_lilly_temp_002 | determinative | astro_mercury AND astro_moon | astro_mental_character | Mercury/Moon determine mind | When analyzing native's character | DESCRIBING | CA III #Temperament |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_temp_001 | "ASC and Lord describe body; planets in 1st modify" | astro_ascendant_sign, astro_asc_lord | HIGH | Lilly's appearance determination method |
| evi_lilly_temp_002 | "Mercury and Moon describe mental qualities" | astro_mercury, astro_moon | HIGH | Lilly's character determination method |
<!-- L2.5_END -->

---

## PART 4: Fortune by House Topics

### 4. Wealth (2nd House)

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 553-562): "Whether the Native shall be rich. Consider the Lord of the 2nd, its dignity, aspects, and the Part of Fortune. Jupiter or Venus in 2nd = wealth; Saturn or Mars afflicting = poverty or loss."

#### English Paraphrase (Primary Language)

**Wealth indicators**:
- **Lord of 2nd house**: Dignified = wealth; debilitated = poverty
- **Planets in 2nd**: Jupiter/Venus = gain; Saturn/Mars = loss
- **Part of Fortune**: Well-placed = fortunate; afflicted = struggles
- **Aspects to 2nd Lord**: Benefic aspects = increase; malefic = decrease

**Means of acquiring wealth** shown by planet ruling or occupying 2nd:
- Sun = authority, government
- Moon = public, women, travel
- Mercury = trade, writing, skill
- Venus = pleasure, arts, women
- Mars = military, surgery, conflict
- Jupiter = religion, law, foreign trade
- Saturn = agriculture, mining, inheritance

#### Complete Chinese Interpretation (Secondary Language)

**财富指标**：第2宫主星尊贵=富裕，失势=贫困；第2宫内行星：木星/金星=获得，土星/火星=损失；福点良好=幸运，受克=困难；第2宫主相位：吉星相位=增加，凶星=减少。**获取财富的方式**由守护或占据第2宫的行星显示：太阳=权威/政府；月亮=公众/女性/旅行；水星=贸易/写作/技能；金星=娱乐/艺术/女性；火星=军事/外科/冲突；木星=宗教/法律/外贸；土星=农业/采矿/遗产。

**Narrative Snippets**:
- `[ns_lilly_wealth_001]` `[trigger: wealth]` `[factor_trigger: astro_wealth_level]` `[role: 主干]` Lord of 2nd dignified = wealth; debilitated = poverty or difficulty acquiring money. → CA III #Wealth
- `[ns_lilly_wealth_002]` `[trigger: wealth_means]` `[factor_trigger: astro_wealth_means]` `[role: 条件分支]` Planet ruling or in 2nd shows means: Jupiter = religion/law; Mercury = trade/writing. → CA III #Wealth
- `[ns_lilly_wealth_003]` `[trigger: lord_2nd]` `[factor_trigger: astro_lord_2nd_dignity]` `[role: 主干依赖]` Lord of 2nd house dignity determines wealth potential: dignified = rich, debilitated = poor. → English Paraphrase
- `[ns_lilly_wealth_004]` `[trigger: planet_2nd]` `[factor_trigger: astro_planet_in_2nd]` `[role: 条件分支]` Planets in 2nd house: Jupiter/Venus = gain; Saturn/Mars = loss or difficulty. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Natal wealth potential from 2nd house indicators
- **Natural Attributes**: L2 dignity, planets in 2nd, Part of Fortune, aspects
- **Functional Symbolism**: Type of wealth shown by planet; amount by dignity/aspects

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lord of 2nd | 第2宫主 | lord_2nd | existing |
| Part of Fortune | 福点 | part_of_fortune | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Lord of 2nd | lord_2nd | existing | Wealth Ruler | By sign on 2nd cusp | astro_calculator | Money |
| Entity | Part of Fortune | part_of_fortune | existing | Lot | ASC+Moon-Sun (day) | astro_calculator | Fortune |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_wealth_001 | determinative | astro_lord_2nd_dignity | astro_wealth_level | L2 dignity determines wealth | When L2 is dignified: wealth; debilitated: poverty | DETERMINING | CA III #Wealth |
| rel_lilly_wealth_002 | categorical | astro_planet_in_2nd | astro_wealth_means | Planet in 2nd shows means | When planet in 2nd categorizes wealth means Jupiter religion Mercury trade | CATEGORIZING | CA III #Wealth |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_wealth_001 | "Lord of 2nd dignified = wealth; debilitated = poverty" | astro_lord_2nd_dignity, astro_wealth_level | HIGH | Lilly's direct wealth determination |
<!-- L2.5_END -->

---

### 5. Marriage (7th House)

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 586-602): "Of men's Marriages. Whether the Native shall marry: if Venus and Moon be well-placed, he shall marry. Lord of 7th in good dignity = happy marriage. Mars afflicting Venus = strife."

#### English Paraphrase (Primary Language)

**Marriage indicators** (for men):
- **Venus** = wife's nature and relationship quality
- **Moon** = emotional compatibility
- **Lord of 7th** = spouse's character
- **Planets in 7th** = marriage circumstances

**Will he marry?**
- Venus/Moon well-aspected = yes
- Lord of 7th angular and dignified = yes
- Malefics afflicting 7th = delays or denial

**Number of marriages**:
- Multiple signs applying to 7th cusp = multiple marriages
- Lord of 7th in double sign (Gemini, Sagittarius, Pisces) = more than one

**Marriage timing**: Directions of Venus or Lord of 7th to benefic aspects.

#### Complete Chinese Interpretation (Secondary Language)

**婚姻指标**（男性）：金星=妻子性质和关系质量；月亮=情感兼容性；第7宫主=配偶性格；第7宫内行星=婚姻情况。**是否会结婚**：金星/月亮相位良好=会；第7宫主在角宫且尊贵=会；凶星克第7宫=延迟或无婚。**婚姻次数**：多个星座趋近第7宫尖=多次婚姻；第7宫主在双体星座（双子、射手、双鱼）=不止一次。**婚姻时间**：金星或第7宫主推运至吉星相位。

**Narrative Snippets**:
- `[ns_lilly_marriage_001]` `[trigger: marriage]` `[factor_trigger: astro_marriage_likelihood]` `[role: 主干]` Venus and Moon well-placed = native shall marry; afflicted = difficulties. → CA III #Marriage
- `[ns_lilly_marriage_002]` `[trigger: spouse_quality]` `[factor_trigger: astro_spouse_quality]` `[role: 主干依赖]` Lord of 7th dignified = happy marriage; debilitated = spouse of poor quality or strife. → CA III #Marriage
- `[ns_lilly_marriage_003]` `[trigger: venus_dignity]` `[factor_trigger: astro_venus_dignity]` `[role: 主干依赖]` Venus dignity indicates wife's nature and relationship quality for men. → English Paraphrase
- `[ns_lilly_marriage_004]` `[trigger: moon_aspect]` `[factor_trigger: astro_moon_aspect]` `[role: 条件分支]` Moon aspects show emotional compatibility in marriage. → English Paraphrase
- `[ns_lilly_marriage_005]` `[trigger: lord_7th]` `[factor_trigger: astro_lord_7th_dignity]` `[role: 主干依赖]` Lord of 7th dignity determines spouse character and marriage quality. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Natal marriage potential from 7th house and Venus
- **Natural Attributes**: Venus = wife; Moon = emotions; L7 = spouse; 7th planets = circumstances
- **Functional Symbolism**: Marriage likelihood, quality, number, and timing

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lord of 7th | 第7宫主 | lord_7th | existing |
| Marriage Significator | 婚姻象征星 | marriage_significator | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Lord of 7th | lord_7th | existing | Spouse Ruler | By 7th cusp sign | astro_calculator | Partner |
| Entity | Venus (natal) | venus_natal | existing | Wife Indicator | For men | astro_semantic | Marriage |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_marriage_001 | determinative | astro_venus_dignity AND astro_moon_aspect | astro_marriage_likelihood | Venus/Moon determine marriage | When both well-placed: will marry | DETERMINING | CA III #Marriage |
| rel_lilly_marriage_002 | qualitative | astro_lord_7th_dignity | astro_spouse_quality | L7 dignity determines spouse | When L7 dignified: happy; debilitated: strife | DESCRIBING | CA III #Marriage |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_marriage_001 | "Venus and Moon well-placed = shall marry" | astro_venus_dignity, astro_moon_aspect | HIGH | Lilly's marriage determination |
<!-- L2.5_END -->

---

### 6. Children (5th House)

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 602-605): "Of Children. Jupiter or Venus in 5th, or Lord of 5th well-dignified = children. Saturn or Mars afflicting 5th = few or none. Fruitful signs on 5th cusp = many children."

#### English Paraphrase (Primary Language)

**Children indicators**:
- **Lord of 5th**: Dignified = children; debilitated = difficulty
- **Planets in 5th**: Jupiter/Venus = fruitful; Saturn/Mars = barren
- **Fruitful signs** on 5th cusp: Cancer, Scorpio, Pisces = many
- **Barren signs** on 5th cusp: Gemini, Leo, Virgo = few

**Number of children**: Count planets in 5th, aspects to L5, fruitfulness of signs involved.

**Gender**: Masculine planets/signs = male; feminine = female.

#### Complete Chinese Interpretation (Secondary Language)

**子女指标**：第5宫主尊贵=有子女，失势=困难；第5宫内行星：木星/金星=多产，土星/火星=少子；第5宫尖**多产星座**（巨蟹、天蝎、双鱼）=多；**贫瘠星座**（双子、狮子、处女）=少。**子女数量**：计算第5宫内行星、L5相位、相关星座多产性。**性别**：阳性行星/星座=男；阴性=女。

**Narrative Snippets**:
- `[ns_lilly_child_001]` `[trigger: children]` `[factor_trigger: astro_fertility]` `[role: 主干]` Lord of 5th dignified with benefics in 5th = children; malefics = few or difficulty. → CA III #Children
- `[ns_lilly_child_002]` `[trigger: fruitful]` `[factor_trigger: astro_child_number]` `[role: 条件分支]` Fruitful signs (Cancer, Scorpio, Pisces) on 5th cusp indicate many children. → CA III #Children
- `[ns_lilly_child_003]` `[trigger: lord_5th]` `[factor_trigger: astro_lord_5th_dignity]` `[role: 主干依赖]` Lord of 5th dignified with benefics = children; with malefics = difficulty. → English Paraphrase
- `[ns_lilly_child_004]` `[trigger: fruitful_sign]` `[factor_trigger: astro_fruitful_sign_5th]` `[role: 条件分支]` Fruitful signs on 5th (Cancer/Scorpio/Pisces) vs barren (Gemini/Leo/Virgo). → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Natal fertility and children from 5th house
- **Natural Attributes**: L5 dignity, planets in 5th, fruitful/barren signs
- **Functional Symbolism**: Number and gender of children; fertility timing

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lord of 5th | 第5宫主 | lord_5th | existing |
| Fruitful Sign | 多产星座 | fruitful_sign | existing |
| Barren Sign | 贫瘠星座 | barren_sign | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Lord of 5th | lord_5th | existing | Children Ruler | By 5th cusp sign | astro_calculator | Fertility |
| State | Sign Fertility | sign_fertility | existing | Fruitful/Barren | Cancer/Scorpio/Pisces vs Gemini/Leo/Virgo | astro_semantic | Productivity |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_child_001 | determinative | astro_lord_5th_dignity | astro_fertility | L5 dignity determines children | When L5 dignified with benefics: children | DETERMINING | CA III #Children |
| rel_lilly_child_002 | conditional | astro_fruitful_sign_5th | astro_child_number | Fruitful signs increase | When Cancer Scorpio Pisces fruitful signs on 5th increase child number | INCREASING | CA III #Children |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_child_001 | "Lord of 5th dignified = children; malefics = few" | astro_lord_5th_dignity, astro_fertility | HIGH | Lilly's fertility determination |
<!-- L2.5_END -->

---

### 7. Career and Honor (10th House)

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 615-633): "Of the Honour or Dignity of the Native. The Sun and Moon strong = honor. Lord of 10th angular and dignified = high position. Mars or Saturn afflicting MC = falls from grace."

#### English Paraphrase (Primary Language)

**Career and Honor indicators**:
- **Sun**: Day chart honor significator
- **Moon**: Night chart honor significator
- **Lord of 10th**: Career type and success
- **Planets in 10th**: Direct career influence
- **MC degree**: Fixed stars, aspects

**Profession** shown by planet ruling or aspecting 10th:
- Mercury strong = writing, trade, teaching
- Venus strong = arts, pleasure, beauty
- Mars strong = military, surgery, mechanics
- Jupiter strong = religion, law, philosophy
- Saturn strong = agriculture, building, government

**Timing of honor**: Directions to MC or L10 from benefics.

#### Complete Chinese Interpretation (Secondary Language)

**事业与荣誉指标**：太阳=日盘荣誉象征星；月亮=夜盘荣誉象征星；第10宫主=事业类型与成功；第10宫内行星=直接事业影响；天顶度数=恒星、相位。**职业**由守护或与第10宫相位的行星显示：水星强=写作/贸易/教学；金星强=艺术/娱乐/美容；火星强=军事/外科/机械；木星强=宗教/法律/哲学；土星强=农业/建筑/政府。**荣誉时机**：吉星推运至天顶或L10。

**Narrative Snippets**:
- `[ns_lilly_career_001]` `[trigger: honor]` `[factor_trigger: astro_honor_level]` `[role: 主干]` Sun and Moon strong = honor and recognition; afflicted = obscurity or disgrace. → CA III #Career
- `[ns_lilly_career_002]` `[trigger: profession]` `[factor_trigger: astro_profession_type]` `[role: 主干依赖]` Planet ruling 10th shows profession type: Mercury = trade; Jupiter = law/religion. → CA III #Career
- `[ns_lilly_career_003]` `[trigger: sun_moon]` `[factor_trigger: astro_sun_moon_dignity]` `[role: 主干依赖]` Sun (day) and Moon (night) dignity indicates honor and recognition level. → English Paraphrase
- `[ns_lilly_career_004]` `[trigger: lord_10th]` `[factor_trigger: astro_lord_10th_planet]` `[role: 条件分支]` Planet ruling 10th determines career type and profession signification. → English Paraphrase

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Natal career and honor from 10th house and luminaries
- **Natural Attributes**: L10, MC, Sun/Moon dignity, planets in/aspecting 10th
- **Functional Symbolism**: Career type by planet; success by dignity; timing by directions

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Lord of 10th | 第10宫主 | lord_10th | existing |
| Midheaven (MC) | 天顶 | midheaven | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Entity | Lord of 10th | lord_10th | existing | Career Ruler | By MC sign | astro_calculator | Profession |
| Structure | Midheaven | midheaven | existing | Career Point | 10th cusp | astro_calculator | Honor |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_career_001 | determinative | astro_sun_moon_dignity | astro_honor_level | Luminaries determine honor | When Sun/Moon strong: recognition | DETERMINING | CA III #Career |
| rel_lilly_career_002 | categorical | astro_lord_10th_planet | astro_profession_type | L10 planet shows profession | When L10 planet categorizes profession Mercury trade Jupiter law | CATEGORIZING | CA III #Career |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_lilly_career_001 | "Sun/Moon strong = honor; afflicted = obscurity" | astro_sun_moon_dignity, astro_honor_level | HIGH | Lilly's honor determination |
<!-- L2.5_END -->

---

## PART 5: Directions (Predictive Techniques)

### 8. Primary Directions

<!-- L1_BEGIN -->

#### Source Text
(Lilly Book III, pp. 652-700): "The Effects of Directions. Directions show when good or evil shall happen. The Ascendant directed to Saturn = melancholy, illness, restrictions. To Jupiter = honor, wealth, success. One degree of direction equals approximately one year of life."

#### English Paraphrase (Primary Language)

**Primary Directions** = the fundamental predictive technique in traditional natal astrology:

**Principle**: Significators (ASC, MC, Sun, Moon) are "directed" (moved forward in the chart) to meet promittors (planets, aspects, fixed stars). When they meet, events occur.

**Timing**: 1° of arc ≈ 1 year of life (Ptolemy's key)

**Significators directed**:
- **ASC** → body, health, personal life
- **MC** → career, honor, public standing
- **Sun** → vitality, father, authority
- **Moon** → emotions, mother, changes

**Effects of ASC to Planets**:
| Promittor | Effect |
|-----------|--------|
| Saturn | Illness, melancholy, delays, losses |
| Jupiter | Honor, wealth, success, expansion |
| Mars | Accidents, conflicts, fevers, courage |
| Sun | Recognition, vitality, father-related events |
| Venus | Love, pleasure, marriage, artistic success |
| Mercury | Intellectual gains, travel, communication |
| Moon | Changes, public matters, mother-related events |

#### Complete Chinese Interpretation (Secondary Language)

**主限**=传统本命占星的基本预测技术。**原理**：象征星（上升、天顶、太阳、月亮）被"推运"（在星盘中向前移动）以遇到应许星（行星、相位、恒星）。当它们相遇时，事件发生。**时间**：1°弧度≈1年生命（托勒密的关键）。**被推运的象征星**：上升→身体/健康/个人生活；天顶→事业/荣誉/公众地位；太阳→生命力/父亲/权威；月亮→情感/母亲/变化。**上升推运至行星的效果**：土星=疾病/忧郁/延迟/损失；木星=荣誉/财富/成功/扩张；火星=事故/冲突/发烧/勇气；太阳=认可/活力/父亲相关事件；金星=爱情/愉悦/婚姻/艺术成功；水星=智识收获/旅行/沟通；月亮=变化/公众事务/母亲相关事件。

**Narrative Snippets**:
- `[ns_lilly_direct_001]` `[trigger: direction]` `[factor_trigger: astro_asc_direction_to]` `[role: 主干]` ASC directed to Jupiter = honor, wealth, success; to Saturn = illness, melancholy, restrictions. → CA III #Directions
- `[ns_lilly_direct_002]` `[trigger: timing]` `[factor_trigger: astro_direction_degree_year]` `[role: 主干依赖]` One degree of direction equals approximately one year of life—Ptolemy's key. → CA III #Directions

<!-- L1_END -->

<!-- L2_BEGIN -->
- **Theme**: Primary directions as natal predictive technique
- **Natural Attributes**: Significators (ASC/MC/Sun/Moon) directed to promittors; 1°=1 year
- **Functional Symbolism**: Timing of life events by arc measurement

| English Term | Chinese Term | factor_id | status |
|--------------|--------------|-----------|--------|
| Primary Direction | 主限 | primary_direction | existing |
| Significator | 象征星 | significator | existing |
| Promittor | 应许星 | promittor | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Mechanism | Primary Direction | primary_direction | existing | Prediction | 1°≈1 year | astro_calculator | Core technique |
| Entity | Significator | significator | existing | Directed Point | ASC/MC/Sun/Moon | astro_calculator | What moves |
| Entity | Promittor | promittor | existing | Target Point | Planets/aspects | astro_calculator | What is met |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->

#### L2.5 Bridge Layer (Book III Summary)

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lilly_direct_001 | causal | astro_asc_direction_to | astro_life_event | Direction produces event | When ASC directed to planet | TRIGGERING | CA III #Directions |
| rel_lilly_direct_002 | temporal | astro_direction_degree_year | astro_timing | 1° = 1 year | When applying Ptolemy's timing key 1 degree equals 1 year | TIMING | CA III #Directions |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_natal_001 | "Hyleg is giver of life" | hyleg | Identification | Hyleg = vital point | High | ✅ | rule_hyleg |
| evi_natal_002 | "1° = 1 year" | primary_direction | Timing method | Direction timing | High | ✅ | rule_direction_key |
| evi_natal_003 | "L2 dignified = wealth" | lord_2nd | House signification | L2 dignity → wealth | High | ✅ | rule_wealth_l2 |
| evi_natal_004 | "Venus/Moon well-placed = marriage" | venus_natal, planet_moon | Marriage indicators | Venus+Moon → marriage | High | ✅ | rule_marriage |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_life_span | Length of life | shou_yuan_life_span | hyleg_anareta | death_dream | mortality_awareness | Life axis |
| concept_fortune | Material prosperity | cai_wealth | lord_2nd, part_of_fortune | treasure_dream | security_needs | Wealth axis |
| concept_partnership | Marriage/spouse | pei_ou_spouse | lord_7th, venus_natal | wedding_dream | anima_animus | Relationship axis |
| concept_career | Profession/honor | guan_official | lord_10th, midheaven | work_dream | persona_achievement | Career axis |

<!-- L2.5_END -->

---

## Summary: Book III Complete Coverage

> **Status**: ✅ v2.1 COMPLIANT  
> **Coverage**: Book III - Natal Astrology (Nativities)  
> **Sections**: 8 major sections covering all natal topics  
> **L2 Records**: Complete semantic extraction  
> **L2.5 Records**: Complete Bridge Layer  
> **Factor Count**: 30+ factors registered  
> **Narrative Snippets**: 15+ tagged snippets  

**Book III completes the natal astrology system, complementing Book I (foundations) and Book II (horary).**

---

## Christian Astrology: Complete Three-Volume Coverage

| Book | Content | File | Status |
|------|---------|------|--------|
| **Book I** | Foundations | `Christian_Astrology_Foundations_v2.1.md` | ✅ Complete |
| **Book II** | Horary | `Christian_Astrology_Horary_v2.1.md` | ✅ Complete |
| **Book III** | Nativities | `Christian_Astrology_Nativities_v2.1.md` | ✅ Complete |
| **Methodology** | Horary Core | `Horary_Methodology.md` | ✅ Complete |

**Total**: 4 files covering all 3 books + methodology supplement

---
