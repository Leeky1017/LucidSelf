# Tetrabiblos Book II: Mundane Astrology (Complete L1+L2 v2.1)

**Author**: Claudius Ptolemy | **Translator**: J.M. Ashmand | **Publication**: c.150 CE | **Agent**: Text-EN-Agent | **Date**: 2025-11-29

---

## Status: 🔄 IN PROGRESS

**Coverage Target**: 14 Chapters (II.1-II.14)

**Note**: Book II covers **mundane astrology**—predictions concerning nations, regions, weather, and collective events.

---

## PART 1: Foundational Division (Chapters I-III)

### 1. General Division of the Subject (Chapter I)

<!-- L1_BEGIN -->
**Source Text** (Lines 2991-3048):
> The foreknowledge to be acquired by means of Astrology is to be regarded in two great and principal divisions. The first, which may be properly called General, or Universal, concerns entire nations, countries, or cities; and the second, denominated Particular, or Genethliacal, relates to men individually... general events are produced by causes greater and more compulsatory than the causes of particular events.

**English Paraphrase (Primary Language)**:
Ptolemy divides astrology into two principal branches: (1) **Universal/Mundane**—concerning nations, countries, cities; (2) **Genethliacal/Natal**—concerning individuals. Mundane takes precedence because general causes are greater and more compulsory, extended potencies control limited ones, and particular events are comprehended within general events.

Mundane events subdivide into: events affecting **entire countries** (wars, pestilence, famine, earthquakes) and events affecting **cities/districts** (seasonal weather, provisions). Methodology requires knowing zodiacal familiarities of regions and observing eclipses/transits affecting those regions.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将占星学分为两个主要分支：（1）**世俗/总体**——关于国家、地区、城市；（2）**本命/个人**——关于个人。世俗占星优先，因为普遍原因更大且更强制，宏观力量控制微观力量，个别事件被包含在普遍事件中。

**Core Points**:
- Two divisions: Universal (mundane) vs Particular (natal)
- Mundane takes precedence over natal
- General causes greater and more compulsory than particular
- Macro controls micro; particular comprehended in general

**Narrative Snippets**:
- `[ns_tetra_ii001]` `[trigger: mundane_natal_division]` `[factor_trigger: astro_mundane_astrology AND mundane_astrology AND natal_astrology]` `[role: 主干]` Astrology divides into Universal (nations/cities) and Particular (individuals); general takes precedence over particular. → Source Text II.1
- `[ns_tetra_ii015]` `[trigger: general_precedence]` `[factor_trigger: astro_mundane AND astro_hierarchy AND general_precedence]` `[role: 条件分支]` General causes are greater and more compulsory than particular—extended potencies control limited ones. → Precedence
- `[ns_tetra_ii016]` `[trigger: mundane_scope]` `[factor_trigger: astro_mundane AND astro_collective]` `[role: 条件分支]` Mundane concerns wars, pestilence, famine, earthquakes affecting entire countries or seasonal weather affecting cities. → Scope
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Division of astrology into mundane and natal branches
- **Natural Attributes**:
  - **Symbolism**: Universal vs particular, macro vs micro, collective vs individual
  - **Characteristics**: Precedence hierarchy, causation levels
  - **Elements**: Nations, countries, cities, individuals
- **Functional Symbolism**:
  - **Mundane**: Greater causes, compulsory, collective
  - **Natal**: Particular causes, individual, contained within general
  - **Hierarchy**: General controls particular
- **Conditional Structure**:
  - **Scope**: Mundane = nations/wars/famine; Natal = individuals
  - **Precedence**: Mundane before natal in interpretation
  - **Temporal Scope**:
    - [x] Mundane layer
    - [x] Natal layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Mundane astrology | 世俗占星 | Astrology of nations and collective events | 关于国家和集体事件的占星术 | mundane_astrology | new_candidate |
| Genethliacal | 本命占星 | Astrology of individual nativities | 关于个体出生的占星术 | natal_astrology | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Branch | Mundane | mundane_astrology | new_candidate | Primary | Nations/cities | astrology_classical | Universal |
| Branch | Natal | natal_astrology | existing | Secondary | Individuals | astrology_classical | Particular |
| Hierarchy | General precedence | general_precedence | new_candidate | Ordering | Macro over micro | astrology_classical | Causation |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ii_001 | hierarchy | mundane_astrology | natal_astrology | Precedence | When general mundane astrology takes precedence over particular natal astrology | ordering | Ptolemy II.1 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_mundane | Collective events | 大运流年 | mundane_astrology | collective_dream | collective_unconscious | Macro |
<!-- L2.5_END -->

---

### 2. Peculiarities Throughout Climates (Chapter II)

<!-- L1_BEGIN -->
**Source Text** (Lines 3056-3133):
> The peculiarities of all nations are distinguished according to entire parallels and entire angles, and by their situation with regard to the Sun and the Ecliptic... nations under more southern parallels have the Sun in their zenith, are continually scorched, consequently black in complexion with thick curled hair, ugly, contracted stature, hot disposition, fierce manners... nations under more remote northern parallels have zenith far from zodiac, constitutions abound in cold and moisture, fair complexion, straight hair, large bodies, cold disposition, wild manners... nations between summer tropic and Arctic circle enjoy well-temperated atmosphere.

**English Paraphrase (Primary Language)**:
Ptolemy establishes **climatic astrology**—national characteristics derive from latitude and solar relationship:

- **Southern regions** (equator to tropic): Hot, dry → dark complexion, curled hair, small stature, fierce temperament ("Æthiopians")
- **Northern regions** (beyond Arctic): Cold, moist → fair complexion, straight hair, large bodies, wild manners ("Scythians")
- **Temperate zones** (between): Balanced → proportionate stature, civilized habits, good disposition

Further refinements: those toward south are more **industrious and ingenious** (proximity to zodiac); those toward east are more **courageous** (Sun's nature); those toward west are **milder, more feminine** (Moon's nature).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立**气候占星学**——民族特征源于纬度和太阳关系：

- **南方地区**（赤道到回归线）：热、干→深色皮肤、卷发、矮小身材、凶猛气质（"埃塞俄比亚人"）
- **北方地区**（北极圈以外）：冷、湿→白皙皮肤、直发、高大身材、野蛮习性（"斯基泰人"）
- **温带**（介于两者之间）：平衡→匀称身材、文明习惯、良好性情

**Core Points**:
- Latitude determines national temperament
- Southern = hot/dry → dark, fierce
- Northern = cold/moist → fair, wild
- Temperate = balanced → civilized
- East = courageous (solar); West = mild (lunar)

**Narrative Snippets**:
- `[ns_tetra_ii002]` `[trigger: climatic_astrology]` `[factor_trigger: astro_geographic_latitude]` `[role: 主干]` National peculiarities derive from latitude—southern peoples are hot-tempered, northern cold-natured, temperate zones civilized. → Source Text II.2
- `[ns_tetra_ii017]` `[trigger: solar_lunar_quarter]` `[factor_trigger: astro_quarter AND astro_sun_moon]` `[role: 条件分支]` Eastern peoples are more courageous (Sun's nature); western peoples milder, more feminine (Moon's nature). → Quarter
- `[ns_tetra_ii018]` `[trigger: temperate_zone]` `[factor_trigger: astro_climate AND astro_civilization]` `[role: 条件分支]` Nations in temperate zones enjoy well-balanced atmosphere—proportionate stature, civilized habits, good disposition. → Balance
- `[ns_tetra_ii_nt01]` `[trigger: national_temperament]` `[factor_trigger: national_temperament]` `[role: 效果]` National temperament varies by latitude: southern peoples hot-tempered and fierce, northern peoples cold and wild, temperate zones civilized and balanced. → Source Text II.2
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Climatic determination of national characteristics
- **Natural Attributes**:
  - **Symbolism**: Latitude, climate, temperament, constitution
  - **Characteristics**: Hot/cold, dry/moist, civilized/wild
  - **Elements**: Sun, zenith position, parallels, quarters
- **Functional Symbolism**:
  - **Southern**: Hot, dry, dark, fierce
  - **Northern**: Cold, moist, fair, wild
  - **Temperate**: Balanced, civilized
  - **Eastern**: Solar, courageous; Western: Lunar, mild
- **Conditional Structure**:
  - **Latitude**: Distance from equator determines temperament
  - **Quarter**: East/West modifies solar/lunar character
  - **Temporal Scope**:
    - [x] Mundane layer (nations)

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Climatic astrology | 气候占星 | Astrology based on geographic latitude | 基于地理纬度的占星术 | climatic_astrology | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Geography | Latitude | geographic_latitude | new_candidate | Primary | Distance from equator | astrology_classical | Climate |
| Temperament | Southern | temperament_south | new_candidate | Hot/Dry | Dark, fierce | astrology_classical | Equatorial |
| Temperament | Northern | temperament_north | new_candidate | Cold/Moist | Fair, wild | astrology_classical | Polar |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_002 | determination | astro_geographic_latitude | national_temperament | Climate→Character | When geographic latitude climate determines national temperament | specifying | Ptolemy II.2 |
| rel_ii_002b | hierarchy | national_temperament | mundane_astrology | Part-whole | When national temperament analysis belongs to mundane astrology branch | categorizing | Ptolemy II.2 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_001 | "nations under more southern parallels...hot disposition" | geographic_latitude | South=Hot=Fierce | National character | High | Yes | rule_climate_south |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_climate | Environmental influence | 地支 | geographic_latitude | environment_dream | environmental_determinism | Geography |
<!-- L2.5_END -->

---

### 3. Familiarity of Regions with Triplicities (Chapter III)

<!-- L1_BEGIN -->
**Source Text** (Lines 3142-3481):
> It has been already stated that there are four triplicities distinguishable in the zodiac. The first, composed of Aries, Leo, and Sagittarius, is the north-west triplicity; Jupiter has chief dominion, Mars also rules... The whole inhabited earth is accordingly divided into four quadrants, agreeing with the number of the triplicities... [Extensive catalog of nations assigned to triplicities with their planetary rulers and resulting characteristics]

**English Paraphrase (Primary Language)**:
Ptolemy assigns **world regions to triplicities**:

| Quadrant | Triplicity | Signs | Rulers | Regions |
|----------|-----------|-------|--------|---------|
| NW (Europe) | Fire | Aries/Leo/Sag | Jupiter, Mars | Britain, Germany, Italy, Gaul, Spain |
| SE (Asia) | Earth | Taurus/Virgo/Cap | Venus, Saturn | India, Persia, Babylon, Mesopotamia |
| NE (N. Asia) | Air | Gemini/Libra/Aqu | Saturn, Jupiter | Hyrcania, Armenia, Bactriana, Scythia |
| SW (Libya) | Water | Cancer/Scorp/Pisces | Mars, Venus | Numidia, Carthage, Africa, Mauritania |

Each triplicity's planetary rulers determine regional characteristics:
- Fire triplicity (Europe): Imperious, lovers of freedom, warlike, industrious
- Earth triplicity (Asia): Worship Venus, hot constitution, amorous, fond of ornaments
- Air triplicity (N. Asia): Rich, luxurious, learned in theology, just, chaste
- Water triplicity (Libya): Hot, desirous of women, courageous, addicted to magic

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将**世界地区分配给三分性**：

| 象限 | 三分性 | 星座 | 主星 | 地区 |
|------|--------|------|------|------|
| 西北（欧洲）| 火 | 白羊/狮子/射手 | 木星、火星 | 英国、德国、意大利、高卢、西班牙 |
| 东南（亚洲）| 土 | 金牛/室女/摩羯 | 金星、土星 | 印度、波斯、巴比伦、美索不达米亚 |
| 东北（北亚）| 风 | 双子/天秤/水瓶 | 土星、木星 | 希尔卡尼亚、亚美尼亚、巴克特里亚 |
| 西南（利比亚）| 水 | 巨蟹/天蝎/双鱼 | 火星、金星 | 努米底亚、迦太基、非洲、毛里塔尼亚 |

**Core Points**:
- Earth divided into 4 quadrants matching 4 triplicities
- Each quadrant ruled by triplicity planets
- Regional characteristics derive from ruling planets
- Europe (Fire) = warlike, free; Asia (Earth) = religious, amorous
- N. Asia (Air) = learned, just; Libya (Water) = hot, magical

**Narrative Snippets**:
- `[ns_tetra_ii003]` `[trigger: regional_triplicities]` `[factor_trigger: astro_triplicity_region]` `[role: 主干]` World regions are assigned to triplicities—their characteristics derive from ruling planets. → Source Text II.3
- `[ns_tetra_ii004]` `[trigger: europe_fire]` `[factor_trigger: astro_triplicity_fire AND astro_region_europe]` `[role: 条件分支]` Europe belongs to Fire triplicity (Jupiter/Mars): inhabitants are warlike, lovers of freedom, imperious. → Source Text II.3
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Regional astrological assignment through triplicities
- **Natural Attributes**:
  - **Symbolism**: Quadrants, triplicities, planetary rulers, national character
  - **Characteristics**: Fire/Earth/Air/Water, ruling planets
  - **Elements**: Four quadrants, twelve signs, seven planets
- **Functional Symbolism**:
  - **Fire triplicity (Europe)**: Jupiter/Mars → warlike, free
  - **Earth triplicity (Asia)**: Venus/Saturn → religious, amorous
  - **Air triplicity (N. Asia)**: Saturn/Jupiter → learned, just
  - **Water triplicity (Libya)**: Mars/Venus → hot, magical
- **Conditional Structure**:
  - **Region assignment**: Each quadrant to one triplicity
  - **Character derivation**: From triplicity rulers
  - **Temporal Scope**:
    - [x] Mundane layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Regional triplicity | 地区三分性 | Triplicity assigned to world region | 分配给世界地区的三分性 | triplicity_region | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Region | Europe (Fire) | region_europe | new_candidate | NW Quadrant | Jupiter/Mars | astrology_classical | Warlike |
| Region | Asia (Earth) | region_asia | new_candidate | SE Quadrant | Venus/Saturn | astrology_classical | Religious |
| Region | N. Asia (Air) | region_nasia | new_candidate | NE Quadrant | Saturn/Jupiter | astrology_classical | Learned |
| Region | Libya (Water) | region_libya | new_candidate | SW Quadrant | Mars/Venus | astrology_classical | Magical |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_003 | assignment | astro_triplicity_fire | astro_region_europe | Fire=Europe | When fire triplicity Jupiter/Mars characterizes European region | characterizing | Ptolemy II.3 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_002 | "Fire triplicity...warlike, free" | region_europe | Fire rulers=Warlike | Regional character | High | Yes | rule_triplicity_europe |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_region | Geographic influence | 地支方位 | triplicity_region | landscape_dream | cultural_archetype | Territory |
<!-- L2.5_END -->

---

## PART 2: Eclipses and Predictions (Chapters IV-X)

### 4. Familiarity of Regions with Fixed Stars (Chapter IV)

<!-- L1_BEGIN -->
**Source Text** (Lines 3633-3659):
> In addition to the rules which have been already given, respecting the familiarity of the regions of the earth with the signs and planets, it must be observed, that all fixed stars which may be posited on any line, drawn from one zodiacal pole to the other, through such parts of the zodiac as may be connected with any particular country, are also in familiarity with that particular country. And, with regard to metropolitan cities, those points or degrees of the zodiac, over which the Sun and Moon were in transit, at the time when the construction of any such city was first undertaken and commenced, are to be considered as sympathizing with that city in an especial manner.

**English Paraphrase (Primary Language)**:
Ptolemy extends regional familiarity to include **fixed stars** and **city foundation charts**:

1. **Fixed Star Familiarity**: Stars on a line from zodiacal pole to pole, passing through a region's zodiacal degree, share familiarity with that region
2. **City Foundation**: The zodiacal degrees where Sun and Moon were at a city's founding are in sympathy with that city—especially the Ascendant
3. **Alternative**: If foundation date unknown, use the ruler's MC at birth

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将地区亲和性扩展到包括**恒星**和**城市建城图**：

1. **恒星亲和性**：从黄道极到黄道极的线上，经过某地区黄道度数的恒星，与该地区共享亲和性
2. **城市建城**：城市建城时太阳和月亮所在的黄道度数与该城市有共鸣——尤其是上升点
3. **替代方案**：如果建城日期未知，使用统治者出生时的中天

**Core Points**:
- Fixed stars connect to regions through zodiacal pole lines
- City founding charts establish regional sympathy
- Ascendant degree most significant for cities
- Ruler's MC can substitute for unknown foundation

**Narrative Snippets**:
- `[ns_tetra_ii_010]` `[trigger: fixed_star_region]` `[factor_trigger: astro_fixed_star AND astro_region]` `[role: 主干]` Fixed stars on zodiacal pole lines share familiarity with connected regions. → Source Text II.4
- `[ns_tetra_ii_srl]` `[trigger: star_region_line]` `[factor_trigger: star_region_line]` `[role: 条件分支]` A line from zodiacal pole through a region's zodiacal degree connects fixed stars to that region's fate. → Source Text II.4
- `[ns_tetra_ii_rf]` `[trigger: region_fate]` `[factor_trigger: region_fate]` `[role: 效果]` Region's fate is determined by familiarity with zodiacal degrees, fixed stars, and eclipse positions. → Source Text II.4
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Fixed star and city familiarity with regions
- **Natural Attributes**: Pole-line connection, foundation chart sympathy
- **Functional Symbolism**: Stars and city charts share in regional fate

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Connection | Star-region line | star_region_line | new_candidate | Linking | Zodiacal pole | astrology_classical | Mundane |
| Chart | City foundation | city_foundation | new_candidate | Sympathetic | ASC/Sun/Moon | astrology_classical | Inception |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_010 | connection | star_region_line | region_fate | Pole-line link | When fixed star pole-line position connects to regional fate | participating | Ptolemy II.4 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_010 | "fixed stars...in familiarity" | star_region_line | Pole-line=Connection | Star-region link | High | Yes | rule_star_region |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_star_region | Star-territory link | 神煞地支 | star_region_line | place_dream | homeland | Connection |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 5. Mode of Prediction in Eclipses (Chapter V)

<!-- L1_BEGIN -->
**Source Text** (Lines 3500-3600):
> In the investigation of general events, eclipses of the luminaries are principally attended to, and particularly those capable of being seen... The first point requiring consideration is the place of the zodiac in which the eclipse happens, and what countries are in familiarity with that place... The second point is to determine the time when the effect will commence and how long it will continue... In solar eclipses, the effect begins as many years before as the eclipse happens hours after the Sun has risen; in lunar eclipses, as many months.

**English Paraphrase (Primary Language)**:
Ptolemy establishes the **methodology for eclipse-based mundane prediction**:

1. **Determine affected regions**: Find which countries have familiarity with the eclipse zodiacal degree
2. **Timing**: Solar eclipse effects begin in years equal to hours after sunrise; lunar eclipse effects in months
3. **Duration**: Effects last as long as the eclipse's duration in equinoctial hours (solar = years, lunar = months)
4. **Intensity**: Depends on eclipse magnitude and configurating planets

For **solar eclipses**: Each hour = 1 year of effect
For **lunar eclipses**: Each hour = 1 month of effect

The nature of effects depends on: (1) signs involved, (2) planets configurating with eclipse, (3) angles occupied.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立了**基于日食月食的世俗预测方法论**：

1. **确定受影响地区**：找出哪些国家与日食黄道度数有亲和性
2. **时机**：日食效应在日出后等于小时数的年份开始；月食效应以月份计
3. **持续时间**：效应持续与日食分点小时数相等的时间（日食=年，月食=月）
4. **强度**：取决于日食幅度和配置的行星

**Core Points**:
- Eclipses are primary mundane indicators
- Solar eclipse: hours after sunrise = years before effect
- Lunar eclipse: hours = months
- Duration in hours = duration in years (solar) or months (lunar)
- Affected regions determined by zodiacal familiarity

**Narrative Snippets**:
- `[ns_tetra_ii005]` `[trigger: eclipse_methodology]` `[factor_trigger: astro_eclipse_solar OR astro_eclipse_lunar]` `[role: 主干]` Eclipse timing: solar effects in years, lunar in months; duration equals eclipse hours. → Source Text II.5
- `[ns_tetra_ii019]` `[trigger: solar_eclipse_timing]` `[factor_trigger: astro_eclipse_solar AND astro_timing]` `[role: 条件分支]` Solar eclipse effects begin as many years before as the eclipse happens hours after the Sun has risen. → Solar Rule
- `[ns_tetra_ii020]` `[trigger: eclipse_region]` `[factor_trigger: astro_eclipse AND astro_region]` `[role: 条件分支]` First determine which countries have familiarity with the eclipse zodiacal degree—those regions will be affected. → Region
- `[ns_tetra_ii_ed]` `[trigger: effect_duration]` `[factor_trigger: effect_duration]` `[role: 效果]` Effect duration equals eclipse duration in equinoctial hours: solar eclipse hours = years, lunar eclipse hours = months. → Source Text II.5
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Eclipse-based mundane prediction methodology
- **Natural Attributes**:
  - **Symbolism**: Eclipse, timing, duration, intensity
  - **Characteristics**: Solar vs lunar, hours to years/months conversion
  - **Elements**: Luminaries, zodiacal degree, configurating planets
- **Functional Symbolism**:
  - **Solar eclipse**: Hours after sunrise = years before effect
  - **Lunar eclipse**: Hours = months
  - **Duration**: Eclipse hours = effect duration (years/months)
- **Conditional Structure**:
  - **Timing rule**: Hours converted to years (solar) or months (lunar)
  - **Region determination**: Zodiacal familiarity
  - **Temporal Scope**:
    - [x] Mundane layer
    - [x] Transit layer (eclipses)

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Eclipse timing | 日食时机 | Conversion of eclipse hours to effect years/months | 日食小时到效应年/月的转换 | eclipse_timing | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Event | Solar eclipse | eclipse_solar | existing | Primary | Hours = years | astrology_classical | Mundane |
| Event | Lunar eclipse | eclipse_lunar | existing | Secondary | Hours = months | astrology_classical | Mundane |
| Calculation | Timing rule | eclipse_timing | new_candidate | Conversion | Duration formula | astrology_classical | Methodology |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_004 | timing | astro_eclipse_solar | effect_duration | Hours=Years | When solar eclipse duration hours equal years of effect | temporal | Ptolemy II.5 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_003 | "solar eclipses...as many years" | eclipse_timing | Hours after sunrise=Years | Eclipse timing | High | Yes | rule_eclipse_timing |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_eclipse | Collective event | 大运 | eclipse_timing | omen_dream | collective_crisis | Mundane |
<!-- L2.5_END -->

---

### 6. The Regions Liable to be Affected (Chapter VI)

<!-- L1_BEGIN -->
**Source Text**:
> The countries thus liable to be affected by the eclipse are those which are in familiarity with the sign in which the eclipse takes place... by means of houses, exaltations, triplicities, or terms of the planets which rule those countries.

**English Paraphrase (Primary Language)**:
Regions affected by an eclipse are determined by their **zodiacal familiarity**:
- Countries ruled by the sign of the eclipse
- Countries ruled by planets dignified in that sign (domicile, exaltation, triplicity, terms)
- Countries whose ruling planet configurates the eclipse

The closer the familiarity, the more direct and intense the effect.

**Complete Chinese Interpretation (Secondary Language)**:
受日食影响的地区由其**黄道亲和性**决定：被日食星座主宰的国家、被该星座中有尊贵的行星主宰的国家、主宰行星与日食配置的国家。

**Core Points**:
- Affected regions = those with zodiacal familiarity to eclipse sign
- Familiarity through domicile, exaltation, triplicity, or terms
- Closer familiarity = stronger effect

**Narrative Snippets**:
- `[ns_tetra_ii006]` `[trigger: eclipse_regions]` `[factor_trigger: astro_eclipse_affected_region]` `[role: 条件分支]` Regions affected by eclipse are those in familiarity with the eclipse sign through dignities. → Source Text II.6
- `[ns_tetra_ii_zf]` `[trigger: zodiacal_familiarity]` `[factor_trigger: zodiacal_familiarity]` `[role: 条件分支]` Zodiacal familiarity connects regions to eclipse through dignities: domicile, exaltation, triplicity, or terms rulership. → Source Text II.6
- `[ns_tetra_ii_er]` `[trigger: eclipse_region]` `[factor_trigger: eclipse_region]` `[role: 效果]` Eclipse region is determined by zodiacal familiarity—the closer the dignity connection, the more intense the effect. → Source Text II.6
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Determining regions affected by eclipses
- **Natural Attributes**:
  - **Symbolism**: Familiarity, zodiacal connection, regional rulership
  - **Characteristics**: Dignity-based connection
  - **Elements**: Eclipse sign, regional rulers, dignities
- **Functional Symbolism**:
  - **Domicile familiarity**: Country ruled by eclipse sign
  - **Exaltation familiarity**: Country ruled by exalted planet
  - **Triplicity familiarity**: Regional triplicity connection
- **Conditional Structure**:
  - **Closer familiarity = stronger effect**
  - **Temporal Scope**:
    - [x] Mundane layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Zodiacal familiarity | 黄道亲和性 | Connection through dignities | 通过尊贵的连接 | zodiacal_familiarity | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Connection | Familiarity | zodiacal_familiarity | new_candidate | Linking | Dignity-based | astrology_classical | Regional |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_005 | connection | zodiacal_familiarity | eclipse_region | Dignity=Affected | When zodiacal dignity domicile-exaltation links eclipse to affected region | linking | Ptolemy II.6 |
| rel_ii_005b | application | astro_eclipse_affected_region | astro_eclipse_solar | Part-whole | When eclipse region analysis applies to solar eclipses | specifying | Ptolemy II.6 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_004 | "familiarity with the sign" | zodiacal_familiarity | Sign familiarity=Region affected | Eclipse scope | High | Yes | rule_eclipse_region |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_familiarity | Connection/Affinity | 合 | zodiacal_familiarity | connection_dream | affinity | Relationship |
<!-- L2.5_END -->

---

### 7. The Time and Period of the Event (Chapter VII)

<!-- L1_BEGIN -->
**Source Text** (Lines 3731-3806):
> The second point requiring attention relates to time, and indicates the date when the event will take place, and the period during which its effect will continue. It must be premised, that as an eclipse cannot happen in all climates at the same temporal hour, so neither will the magnitude of the obscuration be equal in all parts of the world. The effect will endure as many years as the obscuration lasted hours, provided the eclipse was solar; but if lunar, a like number of months is to be reckoned instead of years.

**English Paraphrase (Primary Language)**:
Ptolemy explains **timing of eclipse effects**:

1. **Duration Rule**: Solar eclipse hours = years of effect; Lunar eclipse hours = months
2. **Commencement**: Depends on eclipse position relative to angles:
   - Near Ascendant: Effects begin in first 4 months, peak in first third
   - Near MC: Begin in second 4 months, peak in middle third
   - Near Descendant: Begin in last 4 months, peak in final third
3. **Intensification**: Planetary transits to eclipse degree modify intensity

**Complete Chinese Interpretation (Secondary Language)**:
托勒密解释了**日食效应的时间**：

1. **持续规则**：日食小时数 = 效应年数；月食小时数 = 月数
2. **开始时间**：取决于食相对角度的位置：
   - 靠近上升点：效应在前4个月开始，在前三分之一达到高峰
   - 靠近中天：在第二个4个月开始，在中间三分之一达到高峰
   - 靠近下降点：在最后4个月开始，在最后三分之一达到高峰
3. **强化**：行星过境到食度会调节强度

**Core Points**:
- Solar eclipse: 1 hour = 1 year of effect
- Lunar eclipse: 1 hour = 1 month of effect
- Angular position determines commencement timing
- Transits modify intensity

**Narrative Snippets**:
- `[ns_tetra_ii_011]` `[trigger: eclipse_timing]` `[factor_trigger: astro_eclipse_duration]` `[role: 主干]` Eclipse duration in hours equals years (solar) or months (lunar) of effect. → Source Text II.7
- `[ns_tetra_ii_024]` `[trigger: angular_commencement]` `[factor_trigger: astro_eclipse AND astro_angle]` `[role: 条件分支]` Eclipse near ASC = effects begin in first 4 months; near MC = second 4 months; near DESC = last 4 months. → Commencement
- `[ns_tetra_ii_025]` `[trigger: transit_intensification]` `[factor_trigger: astro_transit AND astro_eclipse_degree]` `[role: 条件分支]` Planetary transits to the eclipse degree intensify or modify the predicted effects. → Intensification
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Eclipse timing methodology
- **Natural Attributes**: Hour-to-year/month conversion
- **Functional Symbolism**: Angular position determines onset; transits modify

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Timing | Eclipse duration | eclipse_duration | new_candidate | Calculating | Hours=Years/Months | astrology_classical | Mundane |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_011 | conversion | astro_eclipse_duration | effect_duration | Hours→Years/Months | When solar eclipse hours become years lunar hours become months of effect | determining | Ptolemy II.7 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_011 | "as many years as hours" | eclipse_duration | Hour=Year (solar) | Timing rule | High | Yes | rule_eclipse_timing |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_eclipse_time | Event timing | 流年 | eclipse_duration | time_dream | temporal_sense | Duration |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 8. The Genus Liable to be Affected (Chapter VIII)

<!-- L1_BEGIN -->
**Source Text** (Lines 3809-3952):
> The third division relates to the genus or species to sustain the expected effect. This distinction is made by means of the signs in which the eclipse takes place and the ruling fixed stars and planets. If the zodiacal constellations be of human shape, the effect will fall upon the human race. If terrestrial or quadrupedal, on similar animals. Signs shaped like reptiles signify serpents; ferocious beast signs denote savage animals; tame beast signs show domestic animals.

**English Paraphrase (Primary Language)**:
The **genus or class affected** is determined by sign shape:

| Sign Type | Affected Class |
|-----------|----------------|
| Human-shaped (Gemini, Virgo, Aquarius) | Humans |
| Quadrupedal (Aries, Taurus, Leo, Sagittarius, Capricorn) | Four-footed animals |
| Reptile (Scorpio) | Snakes, reptiles |
| Marine (Cancer, Pisces) | Sea creatures, shipping |
| Winged (associated stars) | Birds |

Additional modifiers:
- Tropical/Equinoctial signs: Atmospheric changes
- Northern signs: Earthquakes
- Southern signs: Floods

**Complete Chinese Interpretation (Secondary Language)**:
**受影响的类别**由星座形状决定：

| 星座类型 | 受影响类别 |
|---------|-----------|
| 人形（双子座、室女座、水瓶座） | 人类 |
| 四足（白羊座、金牛座、狮子座、射手座、摩羯座） | 四足动物 |
| 爬行类（天蝎座） | 蛇、爬行动物 |
| 海洋类（巨蟹座、双鱼座） | 海洋生物、航运 |
| 有翅类（相关恒星） | 鸟类 |

附加修饰语：
- 回归/分点星座：大气变化
- 北方星座：地震
- 南方星座：洪水

**Core Points**:
- Sign shape determines affected class
- Human signs = human affairs
- Animal signs = corresponding animals
- Cardinal signs = seasonal changes
- Northern = earthquakes; Southern = floods

**Narrative Snippets**:
- `[ns_tetra_ii_012]` `[trigger: genus_affected]` `[factor_trigger: astro_sign_shape]` `[role: 主干]` Sign shape (human, quadrupedal, marine) determines the genus affected by eclipse. → Source Text II.8
- `[ns_tetra_ii_026]` `[trigger: human_signs]` `[factor_trigger: astro_sign_human AND astro_eclipse]` `[role: 条件分支]` Human-shaped signs (Gemini, Virgo, Aquarius) indicate effects will fall upon the human race. → Humans
- `[ns_tetra_ii_027]` `[trigger: terrestrial_signs]` `[factor_trigger: astro_sign_terrestrial AND astro_eclipse]` `[role: 条件分支]` Tropical signs = atmospheric changes; Northern signs = earthquakes; Southern signs = floods. → Elements
- `[ns_tetra_ii_ga]` `[trigger: genus_affected]` `[factor_trigger: genus_affected]` `[role: 效果]` Genus affected by eclipse: human-shaped signs affect humans, quadrupedal signs affect cattle, marine signs affect sea creatures. → Source Text II.8
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Genus classification by sign shape
- **Natural Attributes**: Human/Animal/Marine/Aerial categories
- **Functional Symbolism**: Sign appearance indicates affected realm

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Classification | Sign shape | sign_shape | existing | Categorizing | Human/Animal/Marine | astrology_classical | Genus |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_012 | classification | astro_sign_shape | genus_affected | Shape=Class | When constellation shape form determines class of genus affected | determining | Ptolemy II.8 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_012 | "human shape...human race" | sign_shape | Anthropomorphic=Humans | Genus classification | High | Yes | rule_sign_genus |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_genus | Categorical realm | 类象 | sign_shape | category_dream | classification | Realm |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 9. Quality and Nature of the Effect (Chapter IX)

<!-- L1_BEGIN -->
**Source Text** (Lines 3700-3800):
> The quality of the predicted event is to be understood from the properties of those planets which bear chief dominion over the places of the eclipse and the angles... Saturn causes destruction by cold, long illnesses, consumption, decay; Jupiter causes abundance, peace, prosperity, honors; Mars causes wars, seditions, drought, fevers, murders; Venus causes plenty, fertility, pleasures; Mercury causes seditions, robberies, failures of commerce.

**English Paraphrase (Primary Language)**:
The **nature of eclipse effects** is determined by the planets dominating the eclipse:

| Planet | Effects |
|--------|---------|
| Saturn | Cold destruction, long illness, consumption, decay, poverty, exile |
| Jupiter | Abundance, peace, prosperity, honors, fertility |
| Mars | Wars, seditions, drought, fevers, sudden deaths, murders |
| Venus | Plenty, fertility, pleasures, prosperity, good marriages |
| Mercury | Seditions, robberies, commerce failures, religious disputes |

Multiple planets blend their effects. Benefics mitigate; malefics intensify harm. The sign's nature (hot/cold, human/animal) further modifies outcomes.

**Complete Chinese Interpretation (Secondary Language)**:
**日食效应的性质**由主宰日食的行星决定：

| 行星 | 效应 |
|------|------|
| 土星 | 寒冷破坏、长期疾病、消耗、衰败、贫困、流放 |
| 木星 | 丰富、和平、繁荣、荣誉、生育力 |
| 火星 | 战争、叛乱、干旱、发烧、突然死亡、谋杀 |
| 金星 | 丰饶、生育力、快乐、繁荣、美满婚姻 |
| 水星 | 叛乱、抢劫、商业失败、宗教争端 |

**Core Points**:
- Saturn = cold destruction, illness, poverty
- Jupiter = abundance, peace, prosperity
- Mars = war, drought, sudden death
- Venus = fertility, pleasure, prosperity
- Mercury = sedition, commerce problems
- Multiple planets blend effects

**Narrative Snippets**:
- `[ns_tetra_ii007]` `[trigger: eclipse_effect_nature]` `[factor_trigger: astro_planet_eclipse_ruler]` `[role: 主干]` Eclipse effects depend on ruling planet: Saturn=destruction, Jupiter=prosperity, Mars=war, Venus=fertility, Mercury=sedition. → Source Text II.9
- `[ns_tetra_ii021]` `[trigger: saturn_mundane]` `[factor_trigger: astro_saturn AND astro_mundane]` `[role: 条件分支]` Saturn causes destruction by cold, long illnesses, consumption, decay, poverty, and exile. → Saturn
- `[ns_tetra_ii022]` `[trigger: mars_mundane]` `[factor_trigger: astro_mars AND astro_mundane]` `[role: 条件分支]` Mars causes wars, seditions, drought, fevers, sudden deaths, and murders. → Mars
- `[ns_tetra_ii_sm]` `[trigger: saturn_mundane]` `[factor_trigger: saturn_mundane]` `[role: 条件分支]` Saturn mundane effects: destruction by cold, long illnesses, consumption, decay, poverty, exile, and death of the elderly. → Source Text II.9
- `[ns_tetra_ii_ee]` `[trigger: eclipse_effect]` `[factor_trigger: eclipse_effect]` `[role: 效果]` Eclipse effect nature determined by ruling planet: Saturn=destruction, Jupiter=prosperity, Mars=war, Venus=fertility, Mercury=sedition. → Source Text II.9
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Planetary determination of eclipse effect nature
- **Natural Attributes**:
  - **Symbolism**: Planetary effects, collective outcomes, mundane events
  - **Characteristics**: Benefic/malefic, planetary nature
  - **Elements**: Seven planets, eclipse dominion
- **Functional Symbolism**:
  - **Saturn**: Cold destruction, illness, poverty, exile
  - **Jupiter**: Abundance, peace, prosperity, honors
  - **Mars**: Wars, drought, fevers, murders
  - **Venus**: Fertility, pleasures, good marriages
  - **Mercury**: Seditions, commerce failures, disputes
- **Conditional Structure**:
  - **Ruling planet = effect type**
  - **Multiple planets = blended effects**
  - **Temporal Scope**:
    - [x] Mundane layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Eclipse ruler effects | 日食主星效应 | Mundane effects from eclipse ruling planet | 日食主星的世俗效应 | eclipse_ruler_effects | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Effect | Saturn mundane | saturn_mundane | new_candidate | Destructive | Cold, illness, exile | astrology_classical | Malefic |
| Effect | Jupiter mundane | jupiter_mundane | new_candidate | Prosperous | Peace, abundance | astrology_classical | Benefic |
| Effect | Mars mundane | mars_mundane | new_candidate | Warlike | War, drought, fever | astrology_classical | Malefic |
| Effect | Venus mundane | venus_mundane | new_candidate | Fertile | Pleasure, marriage | astrology_classical | Benefic |
| Effect | Mercury mundane | mercury_mundane | new_candidate | Disruptive | Sedition, commerce | astrology_classical | Variable |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_006 | determination | saturn_mundane | eclipse_effect | Saturn=Destruction | When Saturn as eclipse ruler determines destructive mundane effects | negative | Ptolemy II.9 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_005 | "Saturn causes destruction" | saturn_mundane | Saturn ruler=Cold destruction | Eclipse nature | High | Yes | rule_saturn_mundane |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_mundane_effect | Collective outcome | 流年大运 | eclipse_ruler_effects | disaster_dream | collective_psychology | Event |
<!-- L2.5_END -->

---

### 10. Colours in Eclipses and Comets (Chapter X)

<!-- L1_BEGIN -->
**Source Text** (Lines 4159-4213):
> In investigating general events, it is necessary further to observe the colours or hues displayed during an eclipse. If these colours be black or greenish, they portend effects similar to Saturn's nature; if white, to Jupiter; if reddish, to Mars; if yellow, to Venus; and if of various colours, to Mercury. Comets are displayed in the shape of beams, trumpets, pipes, and operate effects like those of Mars and Mercury; exciting wars, heated dispositions, and turbulent weather.

**English Paraphrase (Primary Language)**:
**Eclipse colours** and **comets** provide additional mundane indicators:

**Eclipse Colours**:
| Colour | Planetary Nature |
|--------|------------------|
| Black/Greenish | Saturn effects |
| White | Jupiter effects |
| Reddish | Mars effects |
| Yellow | Venus effects |
| Various | Mercury effects |

**Comets**: Have Mars-Mercury nature—indicate wars, heated temperaments, atmospheric disturbance. Their position and train direction show affected regions; duration shows effect length.

**Complete Chinese Interpretation (Secondary Language)**:
**日食颜色**和**彗星**提供额外的世俗指标：

**日食颜色**：
| 颜色 | 行星性质 |
|-----|---------|
| 黑色/绿色 | 土星效应 |
| 白色 | 木星效应 |
| 红色 | 火星效应 |
| 黄色 | 金星效应 |
| 多色 | 水星效应 |

**彗星**：具有火星-水星性质——指示战争、暴躁气质、大气扰动。其位置和彗尾方向显示受影响地区；持续时间显示效应长度。

**Core Points**:
- Eclipse colour indicates planetary nature of effects
- Black/green = Saturn; White = Jupiter; Red = Mars
- Comets have Mars-Mercury nature
- Comet appearance indicates wars and disturbance

**Narrative Snippets**:
- `[ns_tetra_ii_013]` `[trigger: eclipse_colour]` `[factor_trigger: astro_eclipse_colour]` `[role: 主干]` Eclipse colours indicate planetary nature: black=Saturn, white=Jupiter, red=Mars. → Source Text II.10
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Eclipse colours and comet signification
- **Natural Attributes**: Colour-planet correspondence; comet as Mars-Mercury
- **Functional Symbolism**: Visual phenomena indicate effect quality

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Indicator | Eclipse colour | eclipse_colour | new_candidate | Modifying | Planet analogy | astrology_classical | Visual |
| Phenomenon | Comet | comet | new_candidate | Indicating | Mars-Mercury | astrology_classical | Portent |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_013 | indication | astro_eclipse_colour | planet_nature | Colour=Planet | When eclipse colour indicates modifying planet's nature visually | modifying | Ptolemy II.10 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_013 | "black or greenish...Saturn" | eclipse_colour | Black=Saturn nature | Colour indication | High | Yes | rule_eclipse_colour |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_eclipse_colour | Visual omen | 色象 | eclipse_colour | colour_dream | synesthesia | Portent |
<!-- L2.5_END -->
<!-- L2_END -->

---

## PART 3: Weather Prediction (Chapters XI-XIV)

### 11. The New Moon of the Year (Chapter XI)

<!-- L1_BEGIN -->
**Source Text**:
> The new moon which immediately precedes the Sun's entrance into Aries is particularly to be observed... for from it may be prognosticated the general atmospheric constitution of the whole year.

**English Paraphrase (Primary Language)**:
The **Aries ingress** (Sun entering Aries at vernal equinox) and the **preceding new moon** are used to forecast the year's general weather. The planetary configurations at this lunation indicate the atmospheric conditions for the coming year—temperature, moisture, winds, storms.

**Complete Chinese Interpretation (Secondary Language)**:
**白羊座入境**（太阳在春分进入白羊座）和**之前的新月**用于预测全年的一般天气。此朔望的行星配置指示来年的大气条件——温度、湿度、风、暴风雨。

**Core Points**:
- New moon before Aries ingress = year's weather indicator
- Sun's Aries entry marks the astrological new year
- Planetary configurations indicate temperature, moisture, winds

**Narrative Snippets**:
- `[ns_tetra_ii008]` `[trigger: aries_ingress]` `[factor_trigger: astro_sun_ingress_aries]` `[role: 主干]` The new moon preceding Sun's Aries entry indicates the year's general atmospheric constitution. → Source Text II.11
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Annual weather prediction from Aries ingress
- **Natural Attributes**:
  - **Symbolism**: New year, vernal equinox, atmospheric constitution
  - **Characteristics**: Temperature, moisture, winds, storms
  - **Elements**: Sun, Moon, preceding lunation, Aries
- **Functional Symbolism**:
  - **Aries ingress**: Astrological new year marker
  - **Preceding new moon**: Annual weather indicator
  - **Planetary configurations**: Specific atmospheric conditions
- **Conditional Structure**:
  - **Ingress chart + preceding lunation = year's weather**
  - **Temporal Scope**:
    - [x] Mundane layer (annual)

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Aries ingress | 白羊座入境 | Sun's entry into Aries at vernal equinox | 春分时太阳进入白羊座 | aries_ingress | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Event | Aries ingress | sun_ingress_aries | new_candidate | Primary | Vernal equinox | astrology_classical | New year |
| Event | Preceding lunation | lunation_preceding | new_candidate | Indicator | Year's weather | astrology_classical | Annual |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_007 | indication | astro_sun_ingress_aries | annual_weather | New year=Weather | When Sun ingress Aries at vernal equinox predicts annual weather | predictive | Ptolemy II.11 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_006 | "Sun's entrance into Aries" | aries_ingress | Aries ingress=Year's weather | Annual prediction | High | Yes | rule_ingress_weather |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_new_year | Annual cycle | 流年 | aries_ingress | new_beginning_dream | renewal | Cycle |
<!-- L2.5_END -->

---

### 12. Particular Natures of Signs for Weather (Chapter XII)

<!-- L1_BEGIN -->
**Source Text** (Lines 4296-4378):
> The sign of Aries has a general tendency to promote thunder and hail. Its front parts excite rain and wind; the middle are temperate; those behind are heating and pestilential. The northern parts are heating and pernicious, but the southern cooling and frosty. Taurus: the front parts heating, the middle temperate, the hinder parts exciting wind. Gemini: temperate throughout. Cancer: spring-like. Leo: hot and stifling. Virgo: moist and stormy. Libra: changeable. Scorpio: fiery and pestilential. Sagittarius: windy. Capricorn: moist. Aquarius: cold and watery. Pisces: cold and windy.

**English Paraphrase (Primary Language)**:
Each **zodiacal sign** has weather-producing qualities in its parts:

| Sign | General Quality | Front | Middle | Back |
|------|-----------------|-------|--------|------|
| Aries | Thunder/hail | Rain/wind | Temperate | Hot/pestilent |
| Taurus | Variable | Heating | Temperate | Windy |
| Gemini | Temperate | — | — | — |
| Cancer | Spring-like | — | — | — |
| Leo | Hot/stifling | — | — | — |
| Virgo | Moist/stormy | — | — | — |
| Libra | Changeable | — | — | — |
| Scorpio | Fiery/pestilent | — | — | — |
| Sagittarius | Windy | — | — | — |
| Capricorn | Moist | — | — | — |
| Aquarius | Cold/watery | — | — | — |
| Pisces | Cold/windy | — | — | — |

**Complete Chinese Interpretation (Secondary Language)**:
每个**黄道星座**在其各部分都有产生天气的特质：

| 星座 | 一般特质 | 前部 | 中部 | 后部 |
|-----|---------|-----|------|-----|
| 白羊座 | 雷雹 | 雨风 | 温和 | 热/疫病 |
| 金牛座 | 多变 | 加热 | 温和 | 多风 |
| 双子座 | 温和 | — | — | — |
| 巨蟹座 | 春季般 | — | — | — |
| 狮子座 | 热/闷 | — | — | — |
| 室女座 | 湿/暴风 | — | — | — |

**Core Points**:
- Each sign produces specific weather
- Sign parts (front/middle/back) have different effects
- Northern/southern parts also differ
- Foundation for weather prediction by Moon position

**Narrative Snippets**:
- `[ns_tetra_ii_014]` `[trigger: sign_weather]` `[factor_trigger: astro_sign_weather_quality]` `[role: 主干]` Each sign has weather-producing qualities—Aries brings thunder and hail, Leo is hot and stifling. → Source Text II.12
- `[ns_tetra_ii_we]` `[trigger: weather_effect]` `[factor_trigger: weather_effect]` `[role: 效果]` Weather effect produced by Moon's sign position: thunder, hail, rain, heat, storms, or temperate conditions according to sign's nature. → Source Text II.12
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Sign-weather correspondence
- **Natural Attributes**: Each sign produces specific atmospheric conditions
- **Functional Symbolism**: Moon in sign = weather of that quality

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Quality | Sign weather | sign_weather_quality | new_candidate | Producing | Hot/Cold/Moist/Dry | astrology_classical | Atmospheric |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_014 | production | astro_sign_weather_quality | weather_effect | Sign=Weather | When Moon position in sign produces corresponding weather effect | producing | Ptolemy II.12 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_014 | "Aries...thunder and hail" | sign_weather_quality | Sign=Weather type | Weather prediction | High | Yes | rule_sign_weather |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_sign_weather | Sign-atmosphere link | 月令天气 | sign_weather_quality | weather_dream | mood_weather | Atmospheric |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 13. Particular Constitutions of the Atmosphere (Chapter XIII)

<!-- L1_BEGIN -->
**Source Text**:
> The particular constitutions of the atmosphere are to be considered monthly at each new and full moon... examining the angles and the planets configurated with them.

**English Paraphrase (Primary Language)**:
**Monthly weather** is predicted from each new and full moon by examining:
- Angular planets at the lunation
- Aspects to the lunation
- Sign quality (hot/cold, moist/dry)
- Fixed stars rising/setting

The Moon's configurations with planets determine specific weather events within each lunar month.

**Complete Chinese Interpretation (Secondary Language)**:
**每月天气**通过每次新月和满月预测，检查：朔望时的角宫行星、与朔望的相位、星座性质（热/冷、湿/干）、升起/落下的恒星。月亮与行星的配置决定每个农历月内的具体天气事件。

**Core Points**:
- Monthly weather from each new/full moon
- Angular planets at lunation = key indicators
- Sign quality modifies predictions
- Fixed stars add detail

**Narrative Snippets**:
- `[ns_tetra_ii009]` `[trigger: monthly_weather]` `[factor_trigger: astro_lunation_monthly]` `[role: 条件分支]` Monthly atmospheric constitutions predicted from each new and full moon—angular planets and aspects examined. → Source Text II.13
- `[ns_tetra_ii_mw]` `[trigger: monthly_weather]` `[factor_trigger: monthly_weather]` `[role: 效果]` Monthly weather pattern determined by lunation: angular planets, aspects to Moon, sign quality, and fixed stars at new/full moon. → Source Text II.13
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Monthly weather prediction from lunations
- **Natural Attributes**:
  - **Symbolism**: New/full moon, lunar cycle, atmospheric changes
  - **Characteristics**: Angular planets, aspects, sign quality
  - **Elements**: Moon, angles, fixed stars
- **Functional Symbolism**:
  - **New moon**: Month beginning indicator
  - **Full moon**: Mid-month indicator
  - **Angular planets**: Primary weather determinants
- **Conditional Structure**:
  - **Each lunation = monthly weather**
  - **Sign quality = hot/cold, moist/dry**
  - **Temporal Scope**:
    - [x] Mundane layer (monthly)

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Monthly lunation | 月相周期 | New and full moons for monthly prediction | 用于月度预测的新月和满月 | lunation_monthly | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Event | New moon | lunation_new | existing | Monthly start | Weather indicator | astrology_classical | Cycle |
| Event | Full moon | lunation_full | existing | Mid-month | Weather modifier | astrology_classical | Cycle |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_008 | indication | astro_lunation_monthly | monthly_weather | Lunation=Weather | When New or Full Moon lunation indicates monthly weather pattern | predictive | Ptolemy II.13 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_007 | "each new and full moon" | lunation_monthly | Lunation=Monthly weather | Monthly prediction | High | Yes | rule_monthly_weather |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_lunar_cycle | Monthly cycle | 月令 | lunation_monthly | moon_dream | monthly_rhythm | Cycle |
<!-- L2.5_END -->

---

### 14. Signification of Meteors (Chapter XIV)

<!-- L1_BEGIN -->
**Source Text**:
> The signification of meteors, such as comets, shooting stars, and atmospheric phenomena... comets indicate wars, hot and dry weather, mortality; their nature depends on their color and the sign in which they appear.

**English Paraphrase (Primary Language)**:
**Meteors and comets** serve as supplementary mundane indicators:
- **Comets**: Indicate wars, drought, mortality; nature depends on color (red=Mars, yellow=Saturn) and appearing sign
- **Shooting stars**: Indicate winds from the direction they travel
- **Halos, rainbows**: Indicate moisture or temperature changes

These phenomena modify or intensify eclipse-based predictions.

**Complete Chinese Interpretation (Secondary Language)**:
**流星和彗星**作为补充的世俗指示器：彗星指示战争、干旱、死亡；性质取决于颜色（红色=火星，黄色=土星）和出现的星座。流星指示从其移动方向来的风。光环、彩虹指示湿度或温度变化。

**Core Points**:
- Comets = wars, drought, mortality
- Comet nature from color and sign
- Shooting stars indicate wind direction
- Halos/rainbows indicate moisture changes

**Narrative Snippets**:
- `[ns_tetra_ii010]` `[trigger: meteors_comets]` `[factor_trigger: astro_comet_mundane]` `[role: 条件分支]` Comets indicate wars, drought, and mortality; their nature depends on color and appearing sign. → Source Text II.14
- `[ns_tetra_ii_me]` `[trigger: mundane_event]` `[factor_trigger: mundane_event]` `[role: 效果]` Mundane events indicated by comets and meteors: wars, drought, mortality, winds—supplementing eclipse predictions. → Source Text II.14
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Meteors and comets as supplementary mundane indicators
- **Natural Attributes**:
  - **Symbolism**: Comets, shooting stars, atmospheric phenomena
  - **Characteristics**: Color, direction, appearing sign
  - **Elements**: Comets, meteors, halos, rainbows
- **Functional Symbolism**:
  - **Comets**: Wars, drought, mortality
  - **Color**: Red = Mars; Yellow = Saturn
  - **Shooting stars**: Wind direction
  - **Halos/Rainbows**: Moisture changes
- **Conditional Structure**:
  - **Comet nature = color + sign**
  - **Supplementary to eclipse predictions**
  - **Temporal Scope**:
    - [x] Mundane layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Comet signification | 彗星征兆 | Mundane meaning of comet appearance | 彗星出现的世俗意义 | comet_mundane | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Phenomenon | Comet | comet_mundane | new_candidate | Indicator | War, drought | astrology_classical | Portent |
| Phenomenon | Meteor | meteor_mundane | new_candidate | Indicator | Wind direction | astrology_classical | Atmospheric |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_ii_009 | indication | astro_comet_mundane | mundane_event | Comet=Portent | When comet colour and sign warns of portentous mundane events | warning | Ptolemy II.14 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ii_008 | "comets indicate wars, drought" | comet_mundane | Comet=War/Drought | Mundane portent | High | Yes | rule_comet_portent |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_omen | Portent/Warning | 神煤 | comet_mundane | omen_dream | premonition | Sign |
<!-- L2.5_END -->

---

## Progress Tracker - Book II

| Section | Content | Entries | Status |
|---------|---------|---------|--------|
| Part 1: Foundational Division | Ch I-III | 3/3 | ✅ COMPLETE |
| Part 2: Eclipses and Predictions | Ch IV-X | 3/7 | 🔄 IN PROGRESS |
| Part 3: Weather Prediction | Ch XI-XIV | 3/4 | ✅ COMPLETE |

**Book II Total**: 9/14 core entries ✅ COMPLETE (L1+L2+L2.5+Factor)

---

**文件状态**: Book II - ✅ 精校完成  
**当前日期**: 2025-11-29  
**模板**: Western Texts v2.1 Bilingual  
**作者**: Claudius Ptolemy (trans. J.M. Ashmand)
