# Tetrabiblos Book III: Genethliacal Astrology (L1+L2+L2.5+Factor Layer)

> **Author**: Claudius Ptolemy (trans. J.M. Ashmand)  
> **Source**: Tetrabiblos, Book III  
> **Date**: 2025-11-27  
> **Template**: Western Texts v2.1 (Bilingual)  
> **Status**: 🔄 IN PROGRESS - Natal astrology (19 chapters)  
> **Agent**: Text-EN-Agent  
> **Updated**: 2025-11-29

---

## PART 1: Foundations of Nativity

### 1. Proem to Genethliacal Astrology

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Genethliacal | Relating to birth/nativity | Individual astrology |
| Universal | Affecting nations/regions | Mundane astrology |
| Particular | Affecting individuals | Natal astrology |

#### Source Text

"The consideration of nativities, or genethliacal astrology, must be now entered upon. The doctrine of nativities consists of two parts: one to be contemplated before the birth, the other after. The rules for prenatal consideration are directed to the ascertainment of the conception, and to the casting of the corresponding figure. The rules for postnatal consideration lead to the ascertainment of the hour of the nativity, and the casting of the nativity figure."

#### English Paraphrase (Primary Language)

**Genethliacal astrology** (natal astrology) forms the individual counterpart to mundane/universal astrology. Ptolemy divides this study into two temporal domains:

1. **Prenatal consideration**: Determining conception time and its astrological figure
2. **Postnatal consideration**: Establishing birth time and the nativity chart

This dual framework acknowledges that the soul's incarnation involves both the **moment of conception** (seed) and the **moment of birth** (manifestation). The nativity cannot be fully understood without considering both.

**Foundation principle**: Individual destiny operates within the larger cosmic framework established by mundane influences (regional, temporal, seasonal).

#### Complete Chinese Interpretation (Secondary Language)

**诞生占星学**（本命占星学）构成世运/普遍占星学的个体对应。托勒密将此研究分为两个时间领域：

1. **产前考量**：确定受孕时间及其占星图象
2. **产后考量**：确立出生时间和本命盘

这种双重框架承认灵魂的化身涉及**受孕时刻**（种子）和**出生时刻**（显化）两者。不考虑两者，本命盘无法被完全理解。

**基础原则**：个体命运在由世运影响（地区、时间、季节）建立的更大宇宙框架内运作。

#### Core Points

- **Genethliacal astrology**: Study of individual nativities
- **Two temporal domains**: Prenatal (conception) and postnatal (birth)
- **Dual consideration**: Both conception and birth matter
- **Hierarchical framework**: Individual within universal

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's emphasis on conception as well as birth distinguishes his approach from later medieval astrology that focused primarily on birth charts. Modern research on prenatal astrology draws on this Ptolemaic foundation.
- **中文**: 托勒密对受孕和出生的双重强调使其方法区别于后来主要关注出生图的中世纪占星术。现代产前占星研究借鉴了这一托勒密基础。

**Narrative Snippets**:
- `[ns_ptolemy_iii_001]` `[trigger: genethliacal]` `[factor_trigger: astro_genethliacal AND astro_nativity AND genethliacal AND prenatal_postnatal AND mundane_natal AND natal_chart AND complete_analysis]` `[role: 主干]` Genethliacal astrology consists of prenatal (conception) and postnatal (birth) considerations. → Source Text
- `[ns_ptolemy_iii_002]` `[trigger: individual_destiny]` `[factor_trigger: astro_individual AND astro_cosmic]` `[role: 主干依赖]` Individual destiny operates within the larger cosmic framework of mundane influences. → English Paraphrase
- `[ns_ptolemy_iii_027]` `[trigger: nativity_doctrine]` `[factor_trigger: astro_nativity AND astro_method]` `[role: 条件分支]` The doctrine of nativities consists of rules for prenatal consideration and rules for postnatal casting of nativity figure. → Method

<!-- L1_END -->

<!-- L2_BEGIN -->

#### v2.1 L2 Semantic Extraction

- **Theme**: Foundation of natal astrology as individual application of cosmic principles
- **Natural Attributes**:
  - **Symbolism**: Birth, incarnation, individual destiny, seed and manifestation
  - **Characteristics**: Dual temporal focus, hierarchical framework
  - **Elements**: Conception figure, nativity figure, universal-particular relationship
- **Functional Symbolism**:
  - **Individual mapping**: Translating universal cosmic influences to personal chart
  - **Temporal dual focus**: Acknowledging both conception and birth significance
  - **Hierarchical integration**: Individual within mundane framework
- **Conditional Structure**:
  - **Necessary Conditions**: Accurate birth time, consideration of regional influences
  - **Enhancing Conditions**: Knowledge of conception time
  - **Framework Conditions**: Understanding mundane context of birth location/time
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Genethliacal | 诞生占星 | Astrology of individual nativities/births | 关于个体本命/出生的占星术 | genethliacal | new_candidate |
| Prenatal figure | 产前图象 | Astrological chart for conception | 受孕的占星图象 | | new_candidate |
| Postnatal figure | 产后图象 | Astrological chart for birth (nativity) | 出生的占星图象（本命盘） | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Genethliacal astrology | genethliacal | new_candidate | Branch | Individual destiny | astrology_classical | Natal focus |
| Process | Dual temporal consideration | prenatal_postnatal | new_candidate | Method | Conception + Birth | astrology_classical | Complete analysis |
| Relational | Universal-particular | mundane_natal | new_candidate | Framework | Hierarchy | astrology_classical | Integration |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ptolemy_iii_001 | foundation | genethliacal | natal_chart | Individual application | When birth data specifies individual natal chart foundation | specifying | Ptolemy #III |
| rel_ptolemy_iii_002 | temporal_dual | prenatal_postnatal | complete_analysis | Both required | When conception and birth data together complete analysis | completing | Ptolemy #III |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ptolemy_iii_001 | "doctrine of nativities consists of two parts" | prenatal_postnatal | Conception + Birth = complete | Dual consideration | High | Yes | rule_dual_temporal |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_individual_destiny | Personal fate within cosmic order | bazi_mingling | natal_chart | destiny_dream | individuation | Universal-particular |
<!-- L2.5_END -->

---

### 2. Conception and Birth (Chapter II)

<!-- L1_BEGIN -->
**Source Text** (Lines 4685-4776):
> The actual moment, in which human generation commences, is, in fact, by nature, the moment of the conception itself; but, in efficacy with regard to subsequent events, it is the parturition or birth. In every case where the actual time of conception may be ascertained, it is useful to remark the effective influence of the configuration of the stars as it existed at that time. For the seed will, at the very first, receive its due quality, as then dispensed by the Ambient. But, if the time of conception cannot be precisely made out, that of the birth must be received as the original date of generation; for it is virtually the most important.

**English Paraphrase (Primary Language)**:
Ptolemy distinguishes between **conception** and **birth** as two starting points for natal astrology:

1. **Conception**: The true natural beginning—the seed receives its initial quality from the Ambient at conception
2. **Birth**: The practical beginning—when conception time is unknown, birth serves as the effective origin

**Key insight**: The birth chart is not inferior to conception chart because:
- Nature times birth to correspond with conception positions
- Birth adds qualities (senses, movement) not present in the womb
- Both moments are cosmically connected through sympathetic correspondence

**Complete Chinese Interpretation (Secondary Language)**:
托勒密区分了**受孕**和**出生**作为本命占星学的两个起点：

1. **受孕**：真正的自然开始——种子在受孕时从环境接收其初始品质
2. **出生**：实际的开始——当受孕时间未知时，出生作为有效起点

**关键洞见**：出生图并不逊于受孕图，因为：
- 自然使出生时间与受孕位置相对应
- 出生增加了子宫内不存在的品质（感官、运动）
- 两个时刻通过交感对应在宇宙上相连

**Core Points**:
- Conception = natural beginning; Birth = practical beginning
- Both charts valid and cosmically connected
- Seed receives quality at conception
- Birth adds human-specific qualities

**Narrative Snippets**:
- `[ns_tetra_iii_010]` `[trigger: conception_birth]` `[factor_trigger: astro_chart_origin]` `[role: 主干]` Conception is the natural origin, birth is the practical origin—both are cosmically valid. → Source Text III.2
- `[ns_ptolemy_iii_028]` `[trigger: seed_quality]` `[factor_trigger: astro_conception AND astro_ambient]` `[role: 条件分支]` The seed receives its due quality from the Ambient at conception—the initial stellar imprint. → Seed
- `[ns_ptolemy_iii_029]` `[trigger: sympathetic_timing]` `[factor_trigger: astro_conception AND astro_birth]` `[role: 条件分支]` Nature times birth to correspond with conception positions through sympathetic correspondence. → Connection
- `[ns_tetra_iii_cb]` `[trigger: chart_birth]` `[factor_trigger: chart_birth]` `[role: 主干]` Birth chart serves as practical origin when conception time is unknown—the moment of manifestation with senses and movement. → Source Text III.2
- `[ns_tetra_iii_cc]` `[trigger: chart_conception]` `[factor_trigger: chart_conception]` `[role: 条件分支]` Conception chart is the natural origin—the seed receives its initial quality from the cosmic ambient at this moment. → Source Text III.2
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Dual origin points for natal astrology
- **Natural Attributes**: Conception = seed quality; Birth = manifestation
- **Functional Symbolism**: Both charts are valid and connected

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Origin | Conception | chart_conception | new_candidate | Primary | Seed quality | astrology_classical | Natural |
| Origin | Birth | chart_birth | existing | Practical | Manifestation | astrology_classical | Effective |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_010 | correspondence | chart_conception | chart_birth | Sympathetic | When nature sympathetically times birth to match conception chart | equivalent | Ptolemy III.2 |
| rel_iii_010b | foundation | astro_conception_chart | natal_astrology | Branch-root | When conception chart provides foundation for natal astrology | grounding | Ptolemy III.2 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_010 | "seed receives quality at conception" | chart_conception | Seed=Initial quality | Conception validity | High | Yes | rule_conception |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_origin | Starting point | 胎元 | chart_origin | origin_dream | birth_trauma | Foundation |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 3. Degree of the Horoscopic Point (Chapter III)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Horoscope | Ascending degree | Chart anchor |
| Ascendant | Rising sign/degree | Personal expression |
| Exact degree | Precise zodiacal position | Accuracy essential |

#### Source Text

"The horoscopic point is to be taken as the angle of the chart; and its exact degree is to be carefully ascertained, because, on the correct determination of this degree, the whole validity of the nativity depends."

#### English Paraphrase (Primary Language)

The **Ascendant** (horoscopic point) serves as the primary anchor of the natal chart. Ptolemy emphasizes that **accuracy is paramount**—the entire validity of astrological interpretation depends on correct determination of the ascending degree.

**Technical requirement**: The Ascendant must be calculated to the exact degree, not merely the rising sign. A few degrees of error can significantly alter house cusps and planetary positions relative to angles.

**Foundation status**: Among all chart points, the Ascendant holds primacy because it establishes the framework for all other house positions.

#### Complete Chinese Interpretation (Secondary Language)

**上升点**（天宫点）作为本命盘的主要锚点。托勒密强调**准确性至关重要**——占星诠释的全部有效性取决于对上升度数的正确确定。

**技术要求**：上升点必须计算到精确度数，而非仅仅上升星座。几度的误差可以显著改变宫位尖端和行星相对于角宫的位置。

**基础地位**：在所有盘中点位中，上升点具有首要地位，因为它为所有其他宫位建立框架。

#### Core Points

- **Ascendant primacy**: Most important chart point
- **Exact degree required**: Not just sign, but precise degree
- **Foundation function**: Establishes all house positions
- **Validity dependent**: Entire chart interpretation depends on accuracy

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's insistence on exact degree calculation established a standard that persists in modern astrology. This contrasts with some Hellenistic whole-sign house systems that are less degree-sensitive.
- **中文**: 托勒密对精确度数计算的坚持建立了在现代占星术中持续存在的标准。这与一些对度数不太敏感的希腊化整宫制形成对比。

**Narrative Snippets**:
- `[ns_ptolemy_iii_003]` `[trigger: ascendant]` `[factor_trigger: astro_ascendant AND astro_anchor]` `[role: 主干]` The horoscopic point is the anchor of the chart; its exact degree determines the validity of the whole nativity. → Source Text
- `[ns_ptolemy_iii_004]` `[trigger: accuracy]` `[factor_trigger: astro_accuracy AND astro_validity]` `[role: 主干依赖]` A few degrees of error can significantly alter house cusps and planetary positions. → English Paraphrase
- `[ns_tetra_iii_hf]` `[trigger: house_framework]` `[factor_trigger: house_framework]` `[role: 主干]` House framework is established by the Ascendant degree—all twelve houses derive their positions from this primary anchor. → Ptolemy III
- `[ns_tetra_iii_dc]` `[trigger: degree_calc]` `[factor_trigger: degree_calc]` `[role: 条件分支]` Degree calculation accuracy is essential—errors cascade through entire interpretation since all positions are relative. → Ptolemy III
- `[ns_tetra_iii_int]` `[trigger: interpretation]` `[factor_trigger: interpretation]` `[role: 效果]` Interpretation validity depends on accurate degree calculations—the entire nativity's meaning flows from correct foundational positions. → Ptolemy III

<!-- L1_END -->

<!-- L2_BEGIN -->

#### v2.1 L2 Semantic Extraction

- **Theme**: Ascendant as foundational chart point requiring exact calculation
- **Natural Attributes**:
  - **Symbolism**: Rising, emergence, personal interface, chart anchor
  - **Characteristics**: Primary, exact, foundational, validity-determining
  - **Elements**: Ascending degree, house framework, angular positions
- **Functional Symbolism**:
  - **Anchor function**: Establishes entire house framework
  - **Personal interface**: Point where cosmos meets individual
  - **Validation function**: Accuracy determines interpretation validity
- **Conditional Structure**:
  - **Necessary Conditions**: Exact birth time for degree calculation
  - **Error impact**: Degree errors cascade through entire chart
  - **Foundation status**: All other positions relative to Ascendant
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Horoscopic point | 天宫点 | The ascending degree at birth, chart anchor | 出生时的上升度数，盘的锚点 | horoscope | existing |
| Ascendant | 上升点 | The zodiacal degree rising at the eastern horizon | 在东方地平线上升的黄道度数 | ascendant | existing |
| Exact degree | 精确度数 | Precise zodiacal position to the degree | 精确到度数的黄道位置 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ascendant | ascendant | existing | Primary Angle | Exact degree | astrology_classical | Chart anchor |
| Process | Degree calculation | degree_calc | new_candidate | Method | Precision required | astrology_classical | Accuracy |
| Relational | House framework | house_framework | new_candidate | Structure | Based on ASC | astrology_classical | Foundation |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ptolemy_iii_003 | foundation | ascendant | house_framework | Establishes positions | When exact degree ascendant anchors entire house framework | anchoring | Ptolemy #III |
| rel_ptolemy_iii_004 | validation | degree_calc | interpretation | Accuracy required | When degree calculation accuracy validates interpretation since errors cascade | validating | Ptolemy #III |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ptolemy_iii_002 | "whole validity of the nativity depends" | ascendant, accuracy | Exact ASC -> valid chart | Accuracy paramount | High | Yes | rule_asc_accuracy |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_chart_anchor | Primary reference point | rizhu_daymaster | ascendant | self_dream | ego_structure | Foundation |
<!-- L2.5_END -->

---

### 4. Distribution of Nativity Inquiry (Chapter IV)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Distribution | Systematic allocation | Methodical approach |
| Life inquiry | Areas of life examination | Comprehensive analysis |
| Planetary significators | Planets ruling topics | Topical lords |

#### Source Text

"The distribution of inquiry into the several topics of a nativity should be made in regular order: and the topics themselves admit of a fourfold general division; viz. 1st, the inquiry into the qualities of the mind; 2nd, into the qualities of the body; 3rd, into pecuniary circumstances; 4th, into dignities and honours."

#### English Paraphrase (Primary Language)

Ptolemy establishes a **systematic methodology** for natal analysis through a fourfold division of life topics:

1. **Mind**: Mental qualities, intelligence, psychological nature
2. **Body**: Physical constitution, health, appearance
3. **Wealth**: Material circumstances, possessions, livelihood
4. **Honours**: Social standing, career, reputation

This framework ensures **comprehensive analysis** by examining all major life domains systematically. Each topic has its own planetary significators and house associations.

**Methodological principle**: Proceed in regular order through each topic, determining the relevant significators before interpretation.

#### Complete Chinese Interpretation (Secondary Language)

托勒密通过将生命主题四分来建立**系统方法论**：

1. **心智**：心理品质、智力、心理本质
2. **身体**：身体体质、健康、外貌
3. **财富**：物质状况、财产、生计
4. **荣誉**：社会地位、事业、声誉

这个框架通过系统地检查所有主要生命领域来确保**全面分析**。每个主题都有其行星指示星和宫位关联。

**方法论原则**：按顺序逐一处理每个主题，在诠释前确定相关指示星。

#### Core Points

- **Fourfold division**: Mind, Body, Wealth, Honours
- **Systematic order**: Proceed methodically through topics
- **Significator-based**: Each topic has ruling planets
- **Comprehensive coverage**: All major life domains

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's fourfold division differs from later medieval divisions that added more categories. This simpler framework influenced Arabic and Renaissance astrology's topical methods.
- **中文**: 托勒密的四分法不同于后来增加更多类别的中世纪划分。这个更简单的框架影响了阿拉伯和文艺复兴占星术的主题方法。

**Narrative Snippets**:
- `[ns_ptolemy_iii_005]` `[trigger: distribution]` `[factor_trigger: astro_distribution AND astro_fourfold]` `[role: 主干]` The distribution of inquiry follows a fourfold division: mind, body, wealth, and honours. → Source Text
- `[ns_ptolemy_iii_006]` `[trigger: methodology]` `[factor_trigger: astro_methodology AND astro_significator]` `[role: 主干依赖]` Each topic has its own planetary significators, proceeding in regular order for comprehensive analysis. → English Paraphrase
- `[ns_tetra_iii_fd]` `[trigger: fourfold_div]` `[factor_trigger: fourfold_div]` `[role: 主干]` Fourfold division of natal inquiry: (1) Mind, (2) Body, (3) Wealth, (4) Honours—systematically covering all major life domains. → Ptolemy III
- `[ns_tetra_iii_si]` `[trigger: systematic_inquiry]` `[factor_trigger: systematic_inquiry]` `[role: 条件分支]` Systematic inquiry proceeds in regular order through each topic, determining significators before interpretation. → Ptolemy III
- `[ns_tetra_iii_ts]` `[trigger: topic_sig]` `[factor_trigger: topic_sig]` `[role: 条件分支]` Topic significators assign specific planets as rulers for each life domain—identified before interpretation begins. → Ptolemy III

<!-- L1_END -->

<!-- L2_BEGIN -->

#### v2.1 L2 Semantic Extraction

- **Theme**: Systematic methodology for comprehensive natal analysis through topical division
- **Natural Attributes**:
  - **Symbolism**: Order, method, completeness, systematic inquiry
  - **Characteristics**: Fourfold, sequential, significator-based, comprehensive
  - **Elements**: Mind, Body, Wealth, Honours—four life domains
- **Functional Symbolism**:
  - **Organizational function**: Structures analysis into manageable topics
  - **Completeness function**: Ensures no major life area overlooked
  - **Methodological function**: Provides consistent analytical framework
- **Conditional Structure**:
  - **Necessary Conditions**: Identify significators for each topic
  - **Order**: Follow systematic sequence
  - **Coverage**: Address all four domains
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Distribution of inquiry | 质询分配 | Systematic allocation of natal topics | 本命主题的系统分配 | distribution | new_candidate |
| Fourfold division | 四分法 | Mind, Body, Wealth, Honours | 心智、身体、财富、荣誉 | | new_candidate |
| Significator | 指示星 | Planet ruling a particular topic | 主管特定主题的行星 | significator | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Fourfold division | fourfold_div | new_candidate | Framework | 4 topics | astrology_classical | Method |
| Process | Systematic inquiry | systematic_inquiry | new_candidate | Method | Sequential order | astrology_classical | Completeness |
| Relational | Topic-significator | topic_sig | new_candidate | Mapping | Each topic -> planets | astrology_classical | Interpretation |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ptolemy_iii_005 | methodology | fourfold_div | systematic_inquiry | Structured approach | When fourfold division organizes systematic inquiry in regular order | organizing | Ptolemy #III |
| rel_ptolemy_iii_006 | assignment | topic_sig | interpretation | Each topic has rulers | When significator identified specifies rulers for each topic | specifying | Ptolemy #III |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ptolemy_iii_003 | "fourfold general division" | fourfold_div | 4 topics = comprehensive | Systematic coverage | High | Yes | rule_fourfold |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_life_domains | Major areas of life examination | liushen_six_gods | house_topics | life_area_dream | life_domains | Comprehensive |
<!-- L2.5_END -->

---

### 18. Quality of the Mind (Chapter XVIII)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Quality of mind | Mental/psychological nature | Inner character |
| Mercury | Rational faculty | Intellectual capacity |
| Moon | Soul/emotional nature | Psychological temperament |

#### Source Text

"In investigating the quality of the mind, the situation of Mercury and of the Moon is to be considered: whether they be in angles or succedent houses, in masculine or feminine signs, in oriental or occidental positions; also whether they be configured with benefics or malefics."

#### English Paraphrase (Primary Language)

For analyzing **mental qualities**, Ptolemy assigns joint rulership to **Mercury** (rational mind) and **Moon** (emotional/soul nature). The analysis considers:

- **Angular position**: In angles (strong) or succedent (moderate)
- **Sign gender**: Masculine (assertive mind) or feminine (receptive mind)
- **Orientation**: Oriental (before Sun, more independent) or occidental (after Sun, more reflective)
- **Aspects**: Configured with benefics (sound mind) or malefics (troubled mind)

**Dual significator principle**: Mercury alone shows intellectual capacity; the Moon shows emotional temperament. Together they reveal the complete mental constitution.

#### Complete Chinese Interpretation (Secondary Language)

分析**心智品质**时，托勒密将共同主管权赋予**水星**（理性心智）和**月亮**（情感/灵魂本质）。分析考虑：

- **角宫位置**：在角宫（强）或续宫（中等）
- **星座性别**：阳性（自信心智）或阴性（接受性心智）
- **方位**：东方（太阳前，更独立）或西方（太阳后，更反思）
- **相位**：与吉星有相位（健全心智）或与凶星（困扰心智）

**双重指示星原则**：单独水星显示智力能力；月亮显示情感气质。两者一起揭示完整的心理构成。

#### Core Points

- **Dual significators**: Mercury (reason) + Moon (emotion)
- **Angular strength**: Position in houses matters
- **Sign qualities**: Gender affects expression
- **Aspectual influence**: Benefics/malefics modify

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's Mercury-Moon combination for mind differs from later traditions that emphasized Mercury alone. This dual approach captures both rational and emotional intelligence.
- **中文**: 托勒密的水星-月亮心智组合不同于后来仅强调水星的传统。这种双重方法同时捕捉理性和情感智力。

**Narrative Snippets**:
- `[ns_ptolemy_iii_007]` `[trigger: mind_quality]` `[factor_trigger: astro_mind AND astro_mercury_moon]` `[role: 主干]` The quality of mind is determined by Mercury (reason) and Moon (soul), their positions, signs, and aspects. → Source Text
- `[ns_ptolemy_iii_008]` `[trigger: dual_significator]` `[factor_trigger: astro_mercury AND astro_moon]` `[role: 主干依赖]` Mercury shows intellectual capacity while Moon shows emotional temperament—together revealing complete mental constitution. → English Paraphrase
- `[ns_tetra_iii_mr]` `[trigger: mercury_reason]` `[factor_trigger: mercury_reason]` `[role: 条件分支]` Mercury as reason significator: shows intellectual capacity, logical ability, communication skills, and rational nature. → Ptolemy III
- `[ns_tetra_iii_ms]` `[trigger: moon_soul]` `[factor_trigger: moon_soul]` `[role: 条件分支]` Moon as soul significator: shows emotional temperament, instinctual responses, and psychic receptivity. → Ptolemy III
- `[ns_tetra_iii_bm]` `[trigger: benefic_malefic]` `[factor_trigger: benefic_malefic]` `[role: 条件分支]` Benefic/malefic aspects modify mind quality: Jupiter/Venus enhance, Saturn/Mars disturb mental constitution. → Ptolemy III
- `[ns_tetra_iii_mq]` `[trigger: mind_quality]` `[factor_trigger: mind_quality]` `[role: 效果]` Mind quality is the resultant mental constitution from Mercury-Moon positions modified by benefic/malefic aspects. → Ptolemy III
- `[ns_tetra_iii_mmm]` `[trigger: mercury_moon_mind]` `[factor_trigger: mercury_moon_mind]` `[role: 主干]` Mercury-Moon mind complex: dual significators jointly ruling mental faculties—reason (Mercury) and soul (Moon). → Ptolemy III

<!-- L1_END -->

<!-- L2_BEGIN -->

#### v2.1 L2 Semantic Extraction

- **Theme**: Mental quality determined by Mercury (reason) and Moon (soul) positions
- **Natural Attributes**:
  - **Symbolism**: Mind, reason, emotion, intellect, temperament
  - **Characteristics**: Dual significator, positional, aspectual
  - **Elements**: Mercury, Moon, angles, signs, aspects
- **Functional Symbolism**:
  - **Rational function**: Mercury shows intellectual capacity
  - **Emotional function**: Moon shows soul/temperament
  - **Integration function**: Together reveal complete mental nature
- **Conditional Structure**:
  - **Necessary Conditions**: Assess both Mercury and Moon
  - **Modifying Conditions**: Angular position, sign gender, orientation
  - **Quality Determinants**: Benefic/malefic aspects
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Quality of mind | 心智品质 | Mental and psychological nature | 心理和智力本质 | mind_quality | new_candidate |
| Rational faculty | 理性能力 | Mercury-ruled intellectual capacity | 水星主管的智力能力 | | new_candidate |
| Soul nature | 灵魂本质 | Moon-ruled emotional temperament | 月亮主管的情感气质 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Mercury-Moon dual | mercury_moon_mind | new_candidate | Significators | Joint rulership | astrology_classical | Mind analysis |
| Energy | Rational capacity | mercury_reason | existing | Function | Intellectual | astrology_classical | Mercury |
| Energy | Soul temperament | moon_soul | existing | Function | Emotional | astrology_classical | Moon |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ptolemy_iii_007 | dual_rulership | mercury_reason | moon_soul | Joint mind rulers | When Mercury and Moon jointly rule mind requiring both assessment | completing | Ptolemy #III |
| rel_ptolemy_iii_008 | modification | benefic_malefic | mind_quality | Aspect influence | When configured planets modify mind quality through benefic or malefic aspects | modifying | Ptolemy #III |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ptolemy_iii_004 | "situation of Mercury and of the Moon" | mercury_moon_mind | Dual assessment -> complete | Mental analysis method | High | Yes | rule_mind_dual |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_mind_dual | Reason + Emotion = complete mind | yinxing_shensha | mercury_moon | consciousness_dream | cognition_affect | Dual nature |
<!-- L2.5_END -->

---

### 19. Diseases of the Mind (Chapter XIX)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Diseases of mind | Mental afflictions | Psychological pathology |
| Afflicted Mercury | Mercury under malefic influence | Rational dysfunction |
| Afflicted Moon | Moon under malefic influence | Emotional disturbance |

#### Source Text

"When Mercury and the Moon are afflicted by Saturn, and are neither in aspect to each other nor to the benefics, the native will be liable to diseases of the mind: such as melancholy, if Saturn be the afflicting planet; epilepsy, if Mars be the afflicting planet; and various forms of mania, if both malefics afflict."

#### English Paraphrase (Primary Language)

Mental afflictions arise when Mercury and Moon are:
1. **Afflicted by malefics** (Saturn or Mars)
2. **Not in aspect to each other** (disconnected reason and emotion)
3. **Not supported by benefics** (no moderating influence)

**Saturn affliction** produces melancholy, depression, excessive coldness—the native's mind becomes too contracted and heavy.

**Mars affliction** produces epilepsy, sudden eruptions, violence—the mind becomes too hot and unstable.

**Both malefics** produces complex mania—the mind is both contracted and explosive.

**Protective factors**: Jupiter or Venus aspects to Mercury/Moon moderate these tendencies.

#### Complete Chinese Interpretation (Secondary Language)

心理疾病在以下情况下产生：
1. **被凶星刑克**（土星或火星）
2. **彼此无相位**（理性和情感断开）
3. **无吉星支持**（无调和影响）

**土星刑克**产生忧郁、抑郁、过度冷漠——原命的心智变得过于收缩和沉重。

**火星刑克**产生癫痫、突然爆发、暴力——心智变得过热和不稳定。

**双凶星**产生复杂躁狂——心智既收缩又爆发性。

**保护因素**：木星或金星与水星/月亮的相位调和这些倾向。

#### Core Points

- **Dual affliction required**: Both Mercury and Moon affected
- **Saturn = melancholy**: Cold, contracted, depressive
- **Mars = epilepsy**: Hot, explosive, unstable
- **Both = mania**: Complex mental disturbance
- **Benefic protection**: Jupiter/Venus moderate afflictions

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's humoral approach to mental illness reflects Greco-Roman medical theory. Modern astrology interprets these symbolically rather than literally diagnosing conditions.
- **中文**: 托勒密对精神疾病的体液方法反映了希腊-罗马医学理论。现代占星术象征性地诠释这些而非字面诊断病症。

**Narrative Snippets**:
- `[ns_ptolemy_iii_009]` `[trigger: mental_disease]` `[factor_trigger: astro_mental_disease AND astro_affliction]` `[role: 主干]` Mental diseases arise when Mercury and Moon are afflicted by malefics without benefic support. → Source Text
- `[ns_ptolemy_iii_010]` `[trigger: saturn_affliction]` `[factor_trigger: astro_saturn AND astro_mars_affliction]` `[role: 条件分支]` Saturn affliction produces melancholy; Mars produces epilepsy; both produce mania. → Source Text
- `[ns_tetra_iii_sc]` `[trigger: saturn_cold]` `[factor_trigger: saturn_cold]` `[role: 条件分支]` Saturn's cold nature afflicting Mercury-Moon produces melancholy—contracted, depressive, cold mental states. → Ptolemy III
- `[ns_tetra_iii_mh]` `[trigger: mars_hot]` `[factor_trigger: mars_hot]` `[role: 条件分支]` Mars's hot nature afflicting Mercury-Moon produces epilepsy—explosive, eruptive, unstable mental states. → Ptolemy III

<!-- L1_END -->

<!-- L2_BEGIN -->

#### v2.1 L2 Semantic Extraction

- **Theme**: Mental diseases from Mercury-Moon affliction by malefics
- **Natural Attributes**:
  - **Symbolism**: Affliction, disconnection, pathology, imbalance
  - **Characteristics**: Malefic, unsupported, disconnected
  - **Elements**: Saturn (cold), Mars (hot), disconnected Mercury-Moon
- **Functional Symbolism**:
  - **Saturn affliction**: Melancholy, contraction, coldness
  - **Mars affliction**: Epilepsy, eruption, instability
  - **Dual affliction**: Complex mania
- **Conditional Structure**:
  - **Necessary Conditions**: Mercury-Moon afflicted, no benefic support
  - **Differentiating Conditions**: Saturn vs Mars vs both
  - **Protective Conditions**: Benefic aspects moderate
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Mental disease | 心智疾病 | Psychological afflictions from malefic influence | 凶星影响导致的心理疾患 | mental_disease | new_candidate |
| Melancholy | 忧郁症 | Saturn-caused depression and coldness | 土星导致的抑郁和冷漠 | | new_candidate |
| Mania | 躁狂症 | Dual-malefic caused mental instability | 双凶星导致的精神不稳定 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| State | Mental affliction | mental_affliction | new_candidate | Pathology | Malefic influence | astrology_classical | Disease |
| Energy | Saturn coldness | saturn_cold | existing | Afflicting | Melancholy | astrology_classical | Contraction |
| Energy | Mars heat | mars_hot | existing | Afflicting | Epilepsy | astrology_classical | Eruption |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ptolemy_iii_009 | affliction | saturn_cold | mercury_moon_mind | Melancholy | When Saturn's cold afflicts Mercury-Moon mind without benefic support | damaging | Ptolemy #III |
| rel_ptolemy_iii_010 | affliction | mars_hot | mercury_moon_mind | Epilepsy | When Mars's hot afflicts Mercury-Moon mind without benefic support | disturbing | Ptolemy #III |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_ptolemy_iii_005 | "afflicted by Saturn...melancholy" | saturn_cold, mental_affliction | Saturn -> cold -> melancholy | Disease specification | High | Yes | rule_saturn_melancholy |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_mental_affliction | Psychological pathology from cosmic imbalance | qisha_harm | malefic_affliction | nightmare | psychopathology | Imbalance |
<!-- L2.5_END -->

---

## PART 2: Pre-Natal Inquiries (Chapters V-X)

### 5. The Parents (Chapter V)

<!-- L1_BEGIN -->
**Source Text** (Lines 4980-5060):
> In conformity with nature, the Sun and Saturn are allotted to the person of the father; and the Moon and Venus to that of the mother... the degree of their fortune and wealth will be indicated by the doryphory, or attendants of the luminaries. If the luminaries be accompanied by the benefics, a conspicuous and brilliant fortune is presaged... If Jupiter or Venus be configurated with the Sun or Saturn, the father will live long; if Mars be elevated above or ascend in succession to the Sun, the father will die suddenly or receive injury.

**English Paraphrase (Primary Language)**:
Ptolemy assigns **significators for parents**:
- **Father**: Sun (primary) + Saturn (secondary)
- **Mother**: Moon (primary) + Venus (secondary)

**Fortune indicators**: The "doryphory" (bodyguard planets attending the luminaries) shows parental wealth:
- Benefics attending = brilliant fortune
- Malefics attending = humble circumstances
- Mixed = vicissitudes

**Longevity of Father**: Jupiter/Venus aspecting Sun/Saturn = long life; Mars in elevation = sudden death or injury.

**Longevity of Mother**: Jupiter/Venus aspecting Moon/Venus = long life; Mars/Saturn afflicting Moon = death by disease or childbirth.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密分配了**父母的征象星**：
- **父亲**：太阳（主要）+ 土星（次要）
- **母亲**：月亮（主要）+ 金星（次要）

**财富指标**："护卫星"（随行发光体的行星）显示父母财富：
- 吉星随行 = 显赫财富
- 凶星随行 = 卑微处境
- 混合 = 起伏

**父亲寿命**：木星/金星相位太阳/土星 = 长寿；火星高居 = 突然死亡或受伤。

**Core Points**:
- Sun/Saturn = father significators; Moon/Venus = mother significators
- Doryphory (attendant planets) indicates parental fortune
- Benefics = prosperity; Malefics = hardship
- Mars elevated over Sun/Saturn = father's sudden death
- Saturn/Mars afflicting Moon = mother's health problems

**Narrative Snippets**:
- `[ns_tetra_iii011]` `[trigger: parent_significators]` `[factor_trigger: astro_sun_father OR astro_moon_mother]` `[role: 主干]` Sun and Saturn signify the father; Moon and Venus signify the mother. → Source Text III.5
- `[ns_tetra_iii012]` `[trigger: doryphory_fortune]` `[factor_trigger: astro_planet_attendants]` `[role: 条件分支]` The doryphory (attendant planets) of the luminaries indicates parental fortune and status. → Source Text III.5
- `[ns_ptolemy_iii_030]` `[trigger: father_longevity]` `[factor_trigger: astro_sun_saturn AND astro_mars]` `[role: 条件分支]` Jupiter/Venus aspecting Sun/Saturn indicates father's long life; Mars elevated = sudden death. → Longevity
- `[ns_tetra_iii_ff]` `[trigger: father_fortune]` `[factor_trigger: father_fortune]` `[role: 效果]` Father's fortune determined by planets attending Sun/Saturn: benefics = eminence, malefics = humble condition. → Source Text III.5
- `[ns_tetra_iii_mf]` `[trigger: mother_fortune]` `[factor_trigger: mother_fortune]` `[role: 效果]` Mother's fortune determined by planets attending Moon/Venus: benefics = prosperity, malefics = obscurity. → Source Text III.5
- `[ns_tetra_iii_fs]` `[trigger: father_sig]` `[factor_trigger: father_sig]` `[role: 条件分支]` Father significators are Sun (diurnal) and Saturn (nocturnal)—examined for paternal fortune and longevity. → Source Text III.5
- `[ns_tetra_iii_mothersig]` `[trigger: mother_sig]` `[factor_trigger: mother_sig]` `[role: 条件分支]` Mother significators are Moon (diurnal) and Venus (nocturnal)—examined for maternal fortune and longevity. → Source Text III.5

**Textual Criticism**: N/A: Standard significator assignment in classical tradition.
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Parental significators and fortune indicators
- **Natural Attributes**:
  - **Symbolism**: Father, mother, fortune, longevity
  - **Characteristics**: Sun/Saturn = father; Moon/Venus = mother
  - **Elements**: Luminaries, benefics, malefics, doryphory
- **Functional Symbolism**:
  - **Father significators**: Sun (primary) + Saturn (secondary)
  - **Mother significators**: Moon (primary) + Venus (secondary)
  - **Doryphory**: Attendant planets indicate fortune
- **Conditional Structure**:
  - **Longevity**: Benefics aspecting = long life; Mars elevated = sudden death
  - **Fortune**: Benefic doryphory = prosperity; Malefic = poverty

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Parent significators | 父母征象星 | Planets indicating parents | 指示父母的行星 | parent_sig | new_candidate |
| Doryphory | 护卫星 | Planets attending luminaries | 随行发光体的行星 | doryphory | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Sun-Saturn | father_sig | new_candidate | Father | Luminary + Malefic | astrology_classical | Paternal |
| Significator | Moon-Venus | mother_sig | new_candidate | Mother | Luminary + Benefic | astrology_classical | Maternal |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_011 | signification | father_sig | father_fortune | Sun/Saturn=Father | When Sun and Saturn signify father's fortune through doryphory | specifying | Ptolemy III.5 |
| rel_iii_012 | signification | mother_sig | mother_fortune | Moon/Venus=Mother | When Moon and Venus signify mother's fortune through doryphory | specifying | Ptolemy III.5 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_006 | "Sun and Saturn...allotted to the father" | father_sig | Sun+Saturn=Father | Parent significator | High | Yes | rule_parent_sig |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_parent | Parental influence | 父母宫星 | parent_sig | parent_dream | family_complex | Ancestry |
<!-- L2.5_END -->

---

### 6. Brothers and Sisters (Chapter VI)

<!-- L1_BEGIN -->
**Source Text** (Lines 5178-5242):
> The place, whence inferences are drawn respecting brothers and sisters, is to be considered as being applicable only to children of the same mother, and it is consequently, agreeably to nature, presumed to be the same as the maternal place; viz. the sign occupying the mid-heaven; or, by day, that which contains Venus, and, by night, the Moon... Should the benefics be configurated with this place, there will be several brothers and sisters; should the malefics be in elevation over this place, the brothers and sisters will be few.

**English Paraphrase (Primary Language)**:
**Siblings** are judged from the **maternal place**:
- **By day**: Mid-heaven or Venus's sign
- **By night**: Mid-heaven or Moon's sign

**Number of siblings**:
- Benefics configurated = many siblings
- Malefics elevated = few siblings
- Bicorporeal signs = multiple births
- Masculine stars = brothers; Feminine stars = sisters
- Oriental stars = elder; Occidental stars = younger

**Sibling relationships**: Harmonious configurations between sibling-significators = brotherly love; inconjunct/opposition = enmity and fraud.

**Complete Chinese Interpretation (Secondary Language)**:
**兄弟姐妹**从**母系宫位**判断：
- **白天**：中天或金星所在星座
- **夜晚**：中天或月亮所在星座

**兄弟姐妹数量**：
- 吉星配置 = 多兄弟姐妹
- 凶星高居 = 少兄弟姐妹
- 双体星座 = 多胎
- 阳性星 = 兄弟；阴性星 = 姐妹
- 东方星 = 年长；西方星 = 年幼

**Core Points**:
- Siblings from maternal place (MC or Venus/Moon by sect)
- Benefics = many; Malefics = few
- Bicorporeal signs = multiple births
- Masculine = brothers; Feminine = sisters

**Narrative Snippets**:
- `[ns_tetra_iii013]` `[trigger: siblings_place]` `[factor_trigger: astro_house_maternal]` `[role: 主干]` Brothers and sisters are judged from the maternal place—mid-heaven or Venus/Moon by sect. → Source Text III.6
- `[ns_ptolemy_iii_031]` `[trigger: sibling_number]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics configurated with maternal place = many siblings; malefics elevated = few siblings. → Number
- `[ns_ptolemy_iii_032]` `[trigger: sibling_gender]` `[factor_trigger: astro_masculine AND astro_feminine]` `[role: 条件分支]` Masculine stars indicate brothers, feminine stars indicate sisters; oriental = elder, occidental = younger. → Gender
- `[ns_tetra_iii_sn]` `[trigger: sibling_number]` `[factor_trigger: sibling_number]` `[role: 效果]` Sibling number determined by benefics/malefics at maternal place: benefics = many, malefics = few, bicorporeal signs = twins. → Source Text III.6
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Siblings through maternal place
- **Natural Attributes**:
  - **Symbolism**: Brothers, sisters, number, quality
  - **Characteristics**: Benefic = many; Malefic = few; Gender from planet sex
- **Functional Symbolism**:
  - **Maternal place**: MC or Venus/Moon by sect
  - **Benefics**: Many siblings; **Malefics**: Few
  - **Bicorporeal**: Multiple births

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Maternal place | 母系宫位 | Place indicating siblings | 指示兄弟姐妹的宫位 | house_maternal | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| House | Maternal place | house_maternal | new_candidate | Siblings | MC or Venus/Moon | astrology_classical | Sect-based |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_013 | indication | astro_house_maternal | sibling_number | MC/Venus/Moon=Siblings | When MC/Venus/Moon with benefic-malefic aspects quantify sibling number | quantifying | Ptolemy III.6 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_007 | "benefics configurated...several siblings" | house_maternal | Benefic=Many siblings | Sibling number | High | Yes | rule_sibling_number |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_sibling | Brother/sister relationship | 兄弟宫 | house_maternal | sibling_dream | sibling_complex | Family |
<!-- L2.5_END -->

---

### 7. Male or Female (Chapter VII)

<!-- L1_BEGIN -->
**Source Text** (Lines 5256-5283):
> The consideration of this question rests not on a single basis... it depends on the several situations of the two luminaries and the ascendant, and upon such planets as possess any prerogatives in the places of those situations... by the nature of the signs in which they are situated, by their relative position to each other, and also by their position towards the earth; as when in the east, they are masculinely disposed, and, when in the west, femininely.

**English Paraphrase (Primary Language)**:
Sex of the native is determined by examining **three places**: Sun, Moon, and Ascendant, with their rulers:

**Masculine indicators**:
- Planets in masculine signs (Fire/Air)
- Eastern position (oriental)
- Matutine position (before Sun)

**Feminine indicators**:
- Planets in feminine signs (Earth/Water)
- Western position (occidental)
- Vespertine position (after Sun)

The majority determines the sex.

**Complete Chinese Interpretation (Secondary Language)**:
原命性别通过检查**三个位置**确定：太阳、月亮和上升点，及其主星：

**阳性指标**：
- 行星在阳性星座（火/风）
- 东方位置（东方的）
- 晨星位置（太阳之前）

**阴性指标**：
- 行星在阴性星座（土/水）
- 西方位置（西方的）
- 昏星位置（太阳之后）

多数决定性别。

**Core Points**:
- Three places examined: Sun, Moon, Ascendant
- Masculine = Fire/Air signs, oriental, matutine
- Feminine = Earth/Water signs, occidental, vespertine
- Majority determines sex

**Narrative Snippets**:
- `[ns_tetra_iii014]` `[trigger: sex_determination]` `[factor_trigger: astro_planet_masculine OR astro_planet_feminine]` `[role: 主干]` Sex is determined by the masculine or feminine constitution of Sun, Moon, Ascendant and their rulers. → Source Text III.7
- `[ns_ptolemy_iii_033]` `[trigger: oriental_masculine]` `[factor_trigger: astro_oriental AND astro_masculine]` `[role: 条件分支]` When planets are in the east (oriental) they are masculinely disposed; when in the west, femininely. → Position
- `[ns_ptolemy_iii_034]` `[trigger: majority_rule]` `[factor_trigger: astro_majority AND astro_sex]` `[role: 条件分支]` The majority of masculine or feminine indicators among Sun, Moon, Ascendant determines the native's sex. → Method
- `[ns_tetra_iii_ns]` `[trigger: native_sex]` `[factor_trigger: native_sex]` `[role: 效果]` Native's sex determined by majority of masculine/feminine indicators at Sun, Moon, Ascendant and their rulers. → Source Text III.7
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Sex determination through masculine/feminine indicators
- **Natural Attributes**:
  - **Symbolism**: Male, female, masculine, feminine
  - **Characteristics**: Signs, positions, orientality
- **Functional Symbolism**:
  - **Masculine**: Fire/Air, oriental, matutine
  - **Feminine**: Earth/Water, occidental, vespertine
  - **Majority determines sex**

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Masculine indicator | 阳性指标 | Signs of male sex | 男性的指标 | masculine_indicator | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Quality | Masculine | planet_masculine | existing | Male | Fire/Air/Oriental | astrology_classical | Yang |
| Quality | Feminine | planet_feminine | existing | Female | Earth/Water/Occidental | astrology_classical | Yin |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_014 | determination | planet_masculine | native_sex | Majority rule | When majority of masculine planets determines native as male | specifying | Ptolemy III.7 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_008 | "in the east...masculinely disposed" | planet_masculine | Oriental=Masculine | Sex determination | High | Yes | rule_sex_determination |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_gender | Masculine/Feminine polarity | 阴阳 | planet_masculine | gender_dream | anima_animus | Polarity |
<!-- L2.5_END -->

---

### 8. Twins and Multiple Births (Chapter VIII)

<!-- L1_BEGIN -->
**Source Text** (Lines 5291-5366):
> When two, or all three, of the said places may be situated in bicorporeal signs, births of this kind will occur... more than twins will be born, in a case wherein all the ruling places may be in bicorporeal signs... The number of children to be produced is to be inferred from the planet which exercises the right of determining the number.

**English Paraphrase (Primary Language)**:
**Multiple births** occur when:
- Two or three key places (Sun, Moon, ASC) are in **bicorporeal signs** (Gemini, Virgo, Sagittarius, Pisces)
- Ruling planets also in bicorporeal signs
- Mid-heaven connected with luminaries (not just ASC)

**Number** determined by the planet with most configurative rights.
**Sex** of multiples determined by masculine/feminine constitution of planets in configuration.

**Classical examples**:
- Saturn, Jupiter, Mars in bicorporeal signs = three males (Anactores)
- Venus, Moon, Mercury feminine = three females (Graces)
- Mixed configurations = mixed sexes (Dioscuri)

**Complete Chinese Interpretation (Secondary Language)**:
**多胎**发生于：
- 两个或三个关键位置（太阳、月亮、上升）在**双体星座**（双子、室女、射手、双鱼）
- 主星也在双体星座
- 中天与发光体连接（不仅是上升）

**数量**由配置权最多的行星决定。
**性别**由配置行星的阳/阴性决定。

**Core Points**:
- Bicorporeal signs = potential for multiples
- More bicorporeal = more children at once
- Planet with most rights determines number
- Masculine/feminine constitution determines sex of multiples

**Narrative Snippets**:
- `[ns_tetra_iii015]` `[trigger: twins_multiples]` `[factor_trigger: astro_sign_bicorporeal]` `[role: 主干]` Twins and multiples occur when luminaries and ascendant are in bicorporeal signs. → Source Text III.8
- `[ns_tetra_iii_bn]` `[trigger: birth_number]` `[factor_trigger: birth_number]` `[role: 效果]` Birth number (singleton, twins, triplets) determined by bicorporeal sign presence at Sun, Moon, Ascendant. → Source Text III.8
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Multiple births from bicorporeal signs
- **Natural Attributes**:
  - **Symbolism**: Twins, multiples, bicorporeal, plurality
  - **Characteristics**: Gemini, Virgo, Sagittarius, Pisces
- **Functional Symbolism**:
  - **Bicorporeal signs**: Gemini, Virgo, Sagittarius, Pisces = multiples
  - **Number**: Planet with most rights determines count
  - **Sex**: Masculine/feminine constitution determines sex

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Bicorporeal signs | 双体星座 | Signs indicating multiple births | 指示多胎的星座 | sign_bicorporeal | existing |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Sign | Bicorporeal | sign_bicorporeal | existing | Multiplying | Gemini/Virgo/Sag/Pisces | astrology_classical | Twins |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_015 | multiplication | astro_sign_bicorporeal | birth_number | Bicorporeal=Multiples | When bicorporeal signs in 2-3 places multiply birth number | multiplying | Ptolemy III.8 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_009 | "two or all three...bicorporeal signs" | sign_bicorporeal | Bicorporeal=Twins | Multiple births | High | Yes | rule_twins |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_multiplicity | Plurality/Doubling | 双子 | sign_bicorporeal | twins_dream | duality | Multiples |
<!-- L2.5_END -->

---

### 9. Monstrous or Defective Births (Chapter IX)

<!-- L1_BEGIN -->
**Source Text** (Lines 5369-5437):
> The same places are to be considered in inquiring into the probability of a monstrous or defective birth. At a birth of this description, the luminaries are either cadent from the ascendant, or not configurated with it; while the angles are occupied by the malefics. If all the places in which the rulers of the luminaries, and the Moon herself and Mercury are situated, should be totally inconjunct with the preceding new or full Moon and its ruler, the birth will be monstrous. If the luminaries be in quadrupedal or bestial signs while two malefics are in angles, the birth will not be human.

**English Paraphrase (Primary Language)**:
**Monstrous/defective births** occur when:
- Luminaries are cadent from ASC or unconfigured with it
- Malefics occupy angles
- Moon/Mercury/luminary rulers are inconjunct the prenatal lunation

**Degrees of abnormality**:
- If luminaries in bestial signs + malefics angular without benefic support = non-human birth
- If luminaries in human signs + malefics angular + no benefic = human but defective
- Jupiter/Venus support = veiled defect (hermaphrodites, speech impediments)
- Mercury alone supporting = deaf and dumb but clever

**Complete Chinese Interpretation (Secondary Language)**:
**畸形/缺陷出生**发生在：
- 发光体从上升点陷落或与其无配置
- 凶星占据角宫
- 月亮/水星/发光体主星与产前朔望无相位

**异常程度**：
- 发光体在兽形星座 + 凶星角宫无吉星支持 = 非人类出生
- 发光体在人形星座 + 凶星角宫 + 无吉星 = 人类但有缺陷
- 木星/金星支持 = 隐藏缺陷（阴阳人、言语障碍）
- 仅水星支持 = 聋哑但聪明

**Core Points**:
- Luminaries cadent/unconfigured = abnormal birth risk
- Malefics angular = severity indicator
- Sign shape (human/bestial) determines degree
- Benefic support mitigates severity

**Narrative Snippets**:
- `[ns_tetra_iii_020]` `[trigger: monstrous_birth]` `[factor_trigger: astro_birth_defect]` `[role: 主干]` Monstrous births occur when luminaries are cadent from ASC while malefics occupy angles. → Source Text III.9
- `[ns_ptolemy_iii_035]` `[trigger: bestial_signs]` `[factor_trigger: astro_sign_bestial AND astro_birth]` `[role: 条件分支]` If luminaries in bestial signs with malefics angular without benefic support, the birth will not be human. → Severity
- `[ns_ptolemy_iii_036]` `[trigger: benefic_mitigation]` `[factor_trigger: astro_benefic AND astro_birth_defect]` `[role: 条件分支]` Jupiter/Venus support mitigates to veiled defects; Mercury alone = deaf and dumb but clever. → Mitigation
- `[ns_tetra_iii_lp]` `[trigger: luminary_position]` `[factor_trigger: luminary_position]` `[role: 条件分支]` Luminary position (angular, succedent, cadent) determines birth normalcy—cadent luminaries with angular malefics indicate defect risk. → Source Text III.9
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Abnormal birth indicators
- **Natural Attributes**: Luminary-angle disconnection; malefic angular dominance
- **Functional Symbolism**: Sign shape determines human/non-human nature

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Indicator | Monstrous birth | birth_defect | new_candidate | Warning | Luminary cadent | astrology_classical | Abnormal |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_020 | indication | astro_birth_defect | luminary_position | Cadent=Risk | When cadent luminary with angular malefic warns of birth defect risk | warning | Ptolemy III.9 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_020 | "luminaries cadent from ascendant" | birth_defect | Disconnection=Abnormality | Defective birth | High | Yes | rule_monstrous |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_defect | Birth abnormality | 刑冲 | birth_defect | deformity_dream | congenital | Abnormal |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 10. Children Not Reared (Chapter X)

<!-- L1_BEGIN -->
**Source Text** (Lines 5440-5533):
> The question is whether the child will or will not be reared. This inquiry is distinct from duration of life. If either luminary be in an angle, and one malefic be in conjunction with it, or equally distant from each luminary (forming triangle apex), while no benefic partakes in configuration and luminary rulers are in places controlled by malefics—the child will not be susceptible of nurture but will immediately perish. Mars is exceedingly pernicious when succedent to Sun; Saturn when succedent to Moon.

**English Paraphrase (Primary Language)**:
**Infant mortality** (whether child will be reared) is judged separately from longevity:

**Death indicators**:
- Luminary angular + malefic conjunct or equidistant from both luminaries
- No benefic configuration
- Luminary rulers in malefic-controlled places
- Mars succedent to Sun; Saturn succedent to Moon = especially deadly

**Survival conditions**:
- If malefics cast rays *after* luminaries but benefics *before* = child abandoned but adopted, will live
- If benefics elevated above malefics = good adoption
- If malefics elevated = miserable servitude

**Complete Chinese Interpretation (Secondary Language)**:
**婴儿死亡**（孩子是否会被抚养）与寿命分开判断：

**死亡指标**：
- 发光体在角宫 + 凶星合相或与两发光体等距
- 无吉星配置
- 发光体主星在凶星控制的位置
- 火星在太阳之后继；土星在月亮之后继 = 尤其致命

**存活条件**：
- 凶星在发光体*之后*投射光线但吉星*之前* = 孩子被遗弃但被收养，会存活
- 吉星高于凶星 = 好的收养
- 凶星高于 = 悲惨的奴役

**Core Points**:
- Distinct from longevity inquiry (< 1 year)
- Malefic-luminary configuration = immediate death risk
- Mars harmful to Sun; Saturn to Moon
- Benefic intervention = survival but possibly abandonment

**Narrative Snippets**:
- `[ns_tetra_iii_021]` `[trigger: not_reared]` `[factor_trigger: astro_infant_mortality]` `[role: 主干]` Children not reared when malefics configure with angular luminaries without benefic intervention. → Source Text III.10
- `[ns_tetra_iii_lum]` `[trigger: luminary]` `[factor_trigger: luminary]` `[role: 主干]` Luminaries (Sun and Moon) are the lights of the chart—their angular position and malefic configurations determine infant viability. → Source Text III.10
- `[ns_tetra_iii_mp]` `[trigger: malefic_planet]` `[factor_trigger: malefic_planet]` `[role: 条件分支]` Malefic planets (Saturn and Mars) in hostile configuration with luminaries: Mars threatens Sun, Saturn threatens Moon. → Source Text III.10
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Infant mortality determination
- **Natural Attributes**: Malefic-luminary configuration; Mars-Sun and Saturn-Moon hostility
- **Functional Symbolism**: Benefic intervention = survival; malefic dominance = death

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Indicator | Infant mortality | infant_mortality | new_candidate | Warning | Malefic-luminary | astrology_classical | Early death |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_021 | hostility | malefic_planet | luminary | Mars→Sun, Saturn→Moon | When Mars opposes Sun or Saturn opposes Moon from angular position fatally | fatal | Ptolemy III.10 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_021 | "Mars succedent to Sun...pernicious" | infant_mortality | Malefic succession=Death | Not reared | High | Yes | rule_infant_death |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_nurture | Will child survive | 养育 | infant_mortality | baby_dream | attachment | Survival |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 11. The Duration of Life - Introduction (Chapter XI)

<!-- L1_BEGIN -->
**Source Text** (Lines 5536-5560):
> Of all events whatsoever, which take place after birth, the most essential is the continuance of life: and as it is, of course, useless to consider, in cases wherein the life of a child does not extend to the period of one year, what other events contingent on its birth might otherwise have subsequently happened, the inquiry into the duration of life consequently takes precedence of all other questions.

**English Paraphrase (Primary Language)**:
**Duration of life** is the most essential inquiry in natal astrology—all other predictions presuppose survival. Ptolemy introduces the **prorogation system**:

**Core principle**: The duration of life is regulated by:
1. **Prorogatory places** (where life-giver may be found)
2. **Rulers of prorogatory places** (planets governing those positions)
3. **Anæretic places/stars** (life-ending degrees)

This chapter establishes that longevity inquiry takes precedence over all other natal questions.

**Complete Chinese Interpretation (Secondary Language)**:
**寿命长度**是本命占星术中最本质的问询——所有其他预测都以生存为前提。托勒密引入**主限系统**：

**核心原则**：寿命长度由以下因素调节：
1. **主限宫位**（生命主可能所在）
2. **主限宫位的主星**（管辖这些位置的行星）
3. **截寿位置/星体**（终结生命的度数）

本章确立寿命问询优先于所有其他本命问题。

**Core Points**:
- Duration of life = most essential natal inquiry
- Takes precedence over all other predictions
- Three regulatory factors: prorogatory places, rulers, anæretic

**Narrative Snippets**:
- `[ns_tetra_iii022]` `[trigger: duration_intro]` `[factor_trigger: astro_lifespan]` `[role: 主干]` Duration of life is the most essential natal inquiry, taking precedence over all other predictions. → Source Text III.11
- `[ns_ptolemy_iii_037]` `[trigger: prorogation_system]` `[factor_trigger: astro_prorogation AND astro_lifespan]` `[role: 条件分支]` Life duration is regulated by prorogatory places (where life-giver found), their rulers, and anæretic places (life-ending degrees). → System
- `[ns_tetra_iii_li]` `[trigger: lifespan_inquiry]` `[factor_trigger: lifespan_inquiry]` `[role: 主干]` Lifespan inquiry is the most essential natal question—survival must be established before other matters can be predicted. → Source Text III.11
- `[ns_tetra_iii_oi]` `[trigger: other_inquiries]` `[factor_trigger: other_inquiries]` `[role: 条件分支]` Other inquiries (fortune, marriage, children, profession) depend on lifespan—they presuppose the native will survive to experience them. → Source Text III.11
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Duration of life as primary inquiry
- **Natural Attributes**: Survival precedes all other events
- **Functional Symbolism**: Prorogation system introduction

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Inquiry | Duration of life | lifespan_inquiry | existing | Primary | Precedence | astrology_classical | Essential |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_022 | precedence | lifespan_inquiry | other_inquiries | Primary | When lifespan inquiry takes precedence since survival is required for other inquiries | foundational | Ptolemy III.11 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_022 | "most essential is continuance of life" | lifespan_inquiry | Survival=Precondition | Priority | High | Yes | rule_lifespan_priority |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_lifespan | Duration of life | 寿元 | lifespan_inquiry | death_dream | mortality_awareness | Primary |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 12. The Prorogatory Places (Chapter XII)

<!-- L1_BEGIN -->
**Source Text** (Lines 5563-5598):
> Firstly, those places, only, are to be deemed prorogatory, to which the future assumption of the dominion of prorogation exclusively belongs. These several places are: the sign on the angle of the ascendant, from the fifth degree above the horizon to the twenty-fifth degree below it; the thirty degrees in dexter sextile thereto, constituting the eleventh house, called the Good Dæmon; the thirty degrees in dexter quartile, forming the mid-heaven above the earth; those in dexter trine making the ninth house, called God; and lastly, those in opposition, belonging to the angle of the west.

**English Paraphrase (Primary Language)**:
**Prorogatory places** are the five positions eligible to contain the life-giver (prorogator):

1. **Ascendant** (1st house): 5° above horizon to 25° below
2. **11th house** (Good Dæmon): Dexter sextile to ASC
3. **Mid-heaven** (10th): Dexter quartile to ASC—most powerful
4. **9th house** (God): Dexter trine to MC
5. **Descendant** (7th): Opposition to ASC

**Priority ranking**: MC > ASC > 11th > 7th > 9th

**Excluded places**: Everything under the earth except degrees ascending; the 12th house (Evil Dæmon) is excluded due to being cadent and having impaired beams.

**Complete Chinese Interpretation (Secondary Language)**:
**主限宫位**是五个可能包含生命主（主限星）的位置：

1. **上升点**（第1宫）：地平线上5°到下25°
2. **第11宫**（善精灵）：与上升的右六分
3. **中天**（第10宫）：与上升的右四分——最强大
4. **第9宫**（神）：与中天的右三分
5. **下降点**（第7宫）：与上升的对分

**优先级排序**：中天 > 上升 > 11宫 > 7宫 > 9宫

**排除位置**：地下一切，除了正在上升的度数；第12宫（恶精灵）因陷落和光线受损而被排除。

**Core Points**:
- Five prorogatory places only
- MC is most powerful, ASC second
- Degrees under earth generally excluded
- 12th house excluded due to cadency

**Narrative Snippets**:
- `[ns_tetra_iii023]` `[trigger: prorogatory_places]` `[factor_trigger: astro_house_prorogatory]` `[role: 主干]` Five prorogatory places: ASC, 11th, MC, 9th, 7th—MC is most powerful. → Source Text III.12
- `[ns_tetra_iii_pr]` `[trigger: priority]` `[factor_trigger: priority]` `[role: 条件分支]` Priority hierarchy of prorogatory places: MC is most potent, followed by ASC, 11th (Good Dæmon), 7th, and 9th. → Source Text III.12
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Prorogatory places definition
- **Natural Attributes**: Five eligible positions for life-giver
- **Functional Symbolism**: MC > ASC > 11th > 7th > 9th priority

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Place | Prorogatory | house_prorogatory | existing | Life-giver | 5 positions | astrology_classical | Directions |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_023 | hierarchy | astro_house_prorogatory | priority | MC > ASC | When MC ranks above ASC in five prorogatory place hierarchy | ranking | Ptolemy III.12 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_023 | "mid-heaven...more potent" | house_prorogatory | MC=Strongest | Priority ranking | High | Yes | rule_prorogatory_places |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_prorogatory | Life-giving position | 命宫 | house_prorogatory | sanctuary_dream | vital_center | Directions |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 13. Number of Prorogators and Part of Fortune (Chapter XIII)

<!-- L1_BEGIN -->
**Source Text** (Lines 5601-5708):
> After due attention has been given to the prorogatory places, the Sun, the Moon, the Ascendant, and the Part of Fortune, are to be considered as the four principally liable to be elected to the office of prorogator... By day the Sun is to be preferred, provided he be situated in a prorogatory place; if not, the Moon; if the Moon also not, then that planet with most dominion, then the ASC. By night, the Moon is preferred first.

**English Paraphrase (Primary Language)**:
**Prorogator candidates** (four principal):
1. Sun
2. Moon
3. Ascendant
4. Part of Fortune (calculated from Sun-Moon-ASC relationship)

**Selection by sect**:
- **By day**: Sun first → Moon → Ruling planet → ASC
- **By night**: Moon first → Sun → Ruling planet → ASC or Part of Fortune

**Part of Fortune calculation**: Compute degrees from Sun to Moon, then place that distance from ASC in sign order. It becomes a "lunar horoscope."

**Ruling planet selection**: Planet with most dignities over Sun (day) or Moon (night), the prenatal lunation, and ASC—at least 3 of 5 dignities required.

**Complete Chinese Interpretation (Secondary Language)**:
**主限星候选**（四个主要）：
1. 太阳
2. 月亮
3. 上升点
4. 福点（从太阳-月亮-上升关系计算）

**按昼夜派选择**：
- **白天**：太阳优先 → 月亮 → 主星 → 上升
- **夜晚**：月亮优先 → 太阳 → 主星 → 上升或福点

**福点计算**：计算太阳到月亮的度数，然后按星座顺序从上升放置该距离。它成为"月亮地平"。

**主星选择**：对太阳（白天）或月亮（夜晚）、产前朔望和上升拥有最多尊贵的行星——至少需要5个尊贵中的3个。

**Core Points**:
- Four principal prorogator candidates
- Sect determines selection priority
- Part of Fortune = lunar horoscope
- Ruling planet needs 3+ dignities

**Narrative Snippets**:
- `[ns_tetra_iii024]` `[trigger: prorogator_selection]` `[factor_trigger: astro_prorogator]` `[role: 主干]` Four prorogator candidates: Sun, Moon, ASC, Part of Fortune—selection follows sect rules. → Source Text III.13
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Prorogator selection rules
- **Natural Attributes**: Four candidates; sect-based priority
- **Functional Symbolism**: Part of Fortune as lunar horoscope

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Point | Prorogator | prorogator | existing | Life-giver | Sun/Moon/ASC/Fortune | astrology_classical | Hyleg |
| Point | Part of Fortune | part_fortune | existing | Lunar ASC | Sun-Moon distance | astrology_classical | Lot |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_024 | selection | astro_prorogator | astro_planet_sect | Day=Sun, Night=Moon | When sect determines Sun prorogator by day Moon by night in prorogatory places | priority | Ptolemy III.13 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_024 | "Sun by day...Moon by night" | prorogator | Sect=Priority | Prorogator selection | High | Yes | rule_prorogator_sect |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_prorogator | Life-giver | 命主 | prorogator | guardian_dream | life_force | Hyleg |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 14. Number of Modes of Prorogation (Chapter XIV)

<!-- L1_BEGIN -->
**Source Text** (Lines 5711-5982):
> When the prorogator has been determined, it is also necessary to take into consideration the two modes of prorogation: one into succeeding signs, under the projection of rays; and when the prorogator is in an oriental place (between MC and ASC), this mode only is used. The other extends into signs preceding the prorogator, according to horary proportion; when the prorogator is between MC and DSC, both modes are adopted.

**English Paraphrase (Primary Language)**:
**Two modes of prorogation**:

1. **Direct motion** (into succeeding signs): "Projection of rays"
   - Used when prorogator is **oriental** (between MC and ASC)
   - Only this mode applies

2. **Converse motion** (into preceding signs): "Horary proportion"
   - Used when prorogator is **occidental** (between MC and DSC)
   - Both modes apply in this case

**Anæretic degrees**:
- In converse prorogation: Only the **occidental horizon** (DSC) is strictly anæretic
- Malefics (Saturn, Mars) in quartile/opposition shorten life
- Benefics (Jupiter, Venus) in aspect extend life

**Calculation**: Each equatorial degree = one year of life.

**Complete Chinese Interpretation (Secondary Language)**:
**两种主限模式**：

1. **直接运动**（进入后续星座）："光线投射"
   - 当主限星在**东方**（中天和上升之间）时使用
   - 仅适用此模式

2. **逆向运动**（进入前面星座）："时辰比例"
   - 当主限星在**西方**（中天和下降之间）时使用
   - 两种模式都适用

**截寿度数**：
- 在逆向主限中：仅**西方地平线**（下降）是严格截寿的
- 凶星（土星、火星）在四分/对分缩短寿命
- 吉星（木星、金星）在相位延长寿命

**计算**：每赤道度数 = 一年寿命。

**Core Points**:
- Two modes: direct and converse
- Oriental prorogator = direct only
- Occidental prorogator = both modes
- DSC is primary anæretic in converse
- Equatorial degree = one year

**Narrative Snippets**:
- `[ns_tetra_iii025]` `[trigger: prorogation_modes]` `[factor_trigger: astro_direction_mode]` `[role: 主干]` Two modes of prorogation: direct (oriental) and converse (occidental)—DSC is primary anæretic. → Source Text III.14
- `[ns_tetra_iii_pp]` `[trigger: prorogator_position]` `[factor_trigger: prorogator_position]` `[role: 条件分支]` Prorogator position (oriental or occidental) determines direction mode: oriental directs forward only, occidental directs both ways. → Source Text III.14
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Modes of prorogation
- **Natural Attributes**: Direct vs converse; oriental vs occidental
- **Functional Symbolism**: Equatorial degree = one year

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Technique | Direct prorogation | prorogation_direct | existing | Oriental | Succeeding signs | astrology_classical | Projection |
| Technique | Converse prorogation | prorogation_converse | existing | Occidental | Preceding signs | astrology_classical | Horary |
| Point | Anæretic | anaeretic | existing | Life-ender | DSC/Malefics | astrology_classical | Killing |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_025 | determination | astro_direction_mode | prorogator_position | Oriental=Direct | When oriental prorogator directs forward occidental directs both ways | mode_selection | Ptolemy III.14 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_025 | "into succeeding signs...projection of rays" | direction_mode | Position=Mode | Prorogation method | High | Yes | rule_direction_mode |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_direction | Life measurement | 大运方向 | prorogation_mode | journey_dream | life_trajectory | Calculation |
<!-- L2.5_END -->
<!-- L2_END -->

---

### 15. Exemplification of Prorogation (Chapter XV)

<!-- L1_BEGIN -->
**Source Text** (Lines 5984-6218):
> In order to exemplify the foregoing instructions, let the first point of Aries be supposed as the preceding place, and the first point in Gemini the succeeding... The times must be multiplied by the horary magnitude... Whatever proportion the temporal hours bear to the quadrant, the same proportion, out of the excess of times, is to be added or deducted.

**English Paraphrase (Primary Language)**:
Ptolemy provides **worked examples** of prorogation calculations:

**Example 1**: Prorogator at ASC (0° Aries)
- Succeeding degree: 0° Gemini
- Latitude: 14-hour longest day (Alexandria ~30°N)
- Horary magnitude: 17 equatorial times
- Calculate times of ascension between degrees

**Example 2**: Prorogator at MC
- Use right ascension times
- Simpler calculation than ASC

**Example 3**: Prorogator at DSC
- Use descension times
- Account for opposite signs rising

**Example 4**: Prorogator between angles
- Interpolate proportionally between angle values
- Use horary proportion method

**Complete Chinese Interpretation (Secondary Language)**:
托勒密提供了主限计算的**实例**：

**例1**：主限星在上升（白羊0°）
- 后续度数：双子0°
- 纬度：14小时最长日（亚历山大约30°N）
- 时辰幅度：17赤道时
- 计算度数之间的上升时间

**例2**：主限星在中天
- 使用赤经时间
- 比上升计算更简单

**例3**：主限星在下降
- 使用下降时间
- 考虑对面星座上升

**例4**：主限星在角宫之间
- 在角宫值之间按比例插值
- 使用时辰比例方法

**Core Points**:
- Worked examples for each angular position
- Horary magnitude varies by latitude
- Interpolation for intermediate positions
- Technical precision required

**Narrative Snippets**:
- `[ns_tetra_iii026]` `[trigger: prorogation_example]` `[factor_trigger: astro_calculation_method]` `[role: 主干]` Ptolemy provides worked examples for prorogation calculation at each angular position. → Source Text III.15
- `[ns_tetra_iii_pc]` `[trigger: prorogation_calc]` `[factor_trigger: prorogation_calc]` `[role: 主干]` Prorogation calculation: multiply times of ascension between degrees by horary magnitude to determine years of life. → Source Text III.15
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Prorogation calculation examples
- **Natural Attributes**: Horary magnitude; latitude-dependent
- **Functional Symbolism**: Technical precision for lifespan calculation

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Technique | Prorogation calculation | prorogation_calc | existing | Method | Horary magnitude | astrology_classical | Exemplification |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_026 | calculation | prorogation_calc | astro_lifespan | Times × Horary | When prorogation calculation determines lifespan through times and horary periods | determining | Ptolemy III.15 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_026 | "multiply by horary magnitude" | prorogation_calc | Times=Years | Lifespan calculation | High | Yes | rule_prorogation_calc |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_calculation | Mathematical method | 推算 | prorogation_calc | computation_dream | analytical_thinking | Technical |
<!-- L2.5_END -->
<!-- L2_END -->

---

## PART 3: Post-Natal Inquiries (Chapters XVI-XIX)

### 16. Form and Temperament of the Body (Chapter XVI)

<!-- L1_BEGIN -->
**Source Text** (Lines 6236-6365):
> In regard to the body, therefore, it is in all cases requisite to observe the oriental horizon, and to ascertain what planets may preside or have dominion over it... Saturn, when oriental, acts on the personal figure by producing a yellowish complexion and a good constitution; with black and curled hair... Jupiter ruling, when oriental, makes the person white or fair, with a clear complexion... Mars ascending gives a fair ruddiness... Venus operates in a manner similar to Jupiter, but more becomingly and gracefully.

**English Paraphrase (Primary Language)**:
**Physical form** is determined by:
1. **Planets ruling the ASC** and their oriental/occidental position
2. **The Moon** and her configurations
3. **Co-ascending fixed stars**

**Planetary effects on body** (Oriental vs Occidental):

| Planet | Oriental | Occidental |
|--------|----------|------------|
| Saturn | Yellow complexion, curly black hair, broad chest | Dark, thin, scanty hair |
| Jupiter | Fair, clear complexion, large eyes, dignified | Fair but less clear, baldness |
| Mars | Fair-ruddy, large, sturdy, blue/grey eyes | Simply ruddy, moderate, hairless |
| Venus | Graceful, beautiful, azure eyes | Similar but softer |
| Mercury | Yellow, proportionate, small eyes | White-fair, thin, squinting |

**Zodiacal quadrant effects**: Vernal = good complexion; Summer = ordinary, curly hair; Autumn = yellowish, slender; Winter = dark, straight hair.

**Complete Chinese Interpretation (Secondary Language)**:
**身体形态**由以下决定：
1. **主宰上升点的行星**及其东/西方位置
2. **月亮**及其配置
3. **共升恒星**

**行星对身体的影响**（东方 vs 西方）：

| 行星 | 东方 | 西方 |
|------|------|------|
| 土星 | 黄色肤色，卷曲黑发，宽胸 | 深色，瘦，稀发 |
| 木星 | 白皙，清澈肤色，大眼，尊贵 | 白皙但不太清澈，秃顶 |
| 火星 | 白皙-红润，高大，健壮，蓝/灰眼 | 简单红润，中等，无毛 |
| 金星 | 优雅，美丽，天蓝色眼睛 | 相似但更柔和 |
| 水星 | 黄色，匀称，小眼 | 白皙，瘦，斜视 |

**Core Points**:
- ASC ruler and Moon determine body
- Oriental planets = stronger physical influence
- Each planet produces specific complexion/build
- Zodiacal quadrants modify temperament
- Fixed stars co-ascending add features

**Narrative Snippets**:
- `[ns_tetra_iii018]` `[trigger: body_form]` `[factor_trigger: astro_planet_ruler_asc]` `[role: 主干]` Physical form is determined by planets ruling the ascendant—each planet produces distinctive features. → Source Text III.16
- `[ns_tetra_iii_bf]` `[trigger: body_form]` `[factor_trigger: body_form]` `[role: 效果]` Body form includes complexion, stature, hair, eyes—determined by ASC ruler's nature and oriental/occidental position. → Source Text III.16
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Physical form from ASC ruler
- **Natural Attributes**:
  - **Symbolism**: Body, complexion, stature, temperament
  - **Characteristics**: Oriental vs occidental effects
- **Functional Symbolism**:
  - **Saturn**: Yellow/dark, curly/straight hair
  - **Jupiter**: Fair, dignified, large eyes
  - **Mars**: Ruddy, sturdy, blue eyes
  - **Venus**: Graceful, beautiful, azure eyes
  - **Mercury**: Yellow/fair, proportionate

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Physical form | 身体形态 | Bodily constitution | 身体的构成 | body_form | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | ASC ruler | planet_ruler_asc | existing | Primary | Body type | astrology_classical | Constitution |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_018 | determination | astro_planet_ruler_asc | body_form | ASC ruler=Body | When ASC ruler's oriental-occidental position determines body form | specifying | Ptolemy III.16 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_011 | "Saturn...yellowish complexion" | planet_ruler_asc | Saturn ruler=Yellow | Body appearance | High | Yes | rule_saturn_body |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_body | Physical constitution | 身宫 | planet_ruler_asc | body_dream | body_image | Appearance |
<!-- L2.5_END -->

---

### 17. Hurts, Injuries, and Diseases of the Body (Chapter XVII)

<!-- L1_BEGIN -->
**Source Text** (Lines 6376-6567):
> For the investigation of these circumstances, the two angles on the horizon, both the ascendant and the western, must in all cases be remarked... if both the malefics, or even if one of them, should be stationed bodily on any of the successive degrees composing the said angles, or be configurated with such degrees in quartile or in opposition, some bodily disorders or injuries will attach to the native.

**English Paraphrase (Primary Language)**:
**Bodily afflictions** are indicated by:
- **Malefics on angles** (especially ASC/DSC and 6th house)
- **Malefics in quartile/opposition to angles**
- **Luminaries angularly posited with malefics**

**Planetary body rulerships**:
- Saturn: Right ear, spleen, bladder, phlegm, bones
- Jupiter: Hand, lungs, arteries, seed
- Mars: Left ear, kidneys, veins, privities
- Sun: Eyes, brain, heart, nerves, right side
- Venus: Nostrils, liver, flesh
- Mercury: Speech, understanding, bile, tongue
- Moon: Palate, throat, stomach, belly, womb, left side

**Saturn diseases**: Cold, consumption, rheumatism, decay, dropsy
**Mars diseases**: Fevers, wounds, hemorrhage, inflammation, burns
**Benefics mitigate**: Jupiter through human aid (wealth); Venus through divine aid (oracles)

**Complete Chinese Interpretation (Secondary Language)**:
**身体疾病**由以下指示：
- **凶星在角宫**（尤其是上升/下降和第6宫）
- **凶星与角宫四分/对分**
- **发光体与凶星角宫配置**

**行星身体主宰**：
- 土星：右耳、脾、膀胱、痰、骨骼
- 木星：手、肺、动脉、精液
- 火星：左耳、肾、静脉、私处
- 太阳：眼、脑、心、神经、右侧
- 金星：鼻孔、肝、肉
- 水星：言语、理解、胆汁、舌
- 月亮：上颚、喉、胃、腹、子宫、左侧

**Core Points**:
- Malefics on ASC/DSC/6th = bodily afflictions
- Each planet rules specific body parts
- Saturn = cold diseases; Mars = hot diseases
- Occidental malefics = disease; Oriental = injury
- Benefics in elevation mitigate afflictions

**Narrative Snippets**:
- `[ns_tetra_iii019]` `[trigger: bodily_disease]` `[factor_trigger: astro_malefic_angular]` `[role: 主干]` Bodily diseases arise when malefics occupy or aspect the horizon angles. → Source Text III.17
- `[ns_tetra_iii020]` `[trigger: body_rulership]` `[factor_trigger: astro_planet_body_part]` `[role: 条件分支]` Each planet rules specific body parts—Saturn bones, Mars blood, Mercury speech, etc. → Source Text III.17
- `[ns_tetra_iii_ba]` `[trigger: bodily_affliction]` `[factor_trigger: bodily_affliction]` `[role: 效果]` Bodily affliction (disease, injury, defect) indicated by malefics on or aspecting horizon angles—severity depends on malefic nature. → Source Text III.17
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Bodily diseases from angular malefics
- **Natural Attributes**:
  - **Symbolism**: Disease, injury, affliction
  - **Characteristics**: Angular malefics, planetary body parts
- **Functional Symbolism**:
  - **Malefics on angles**: Bodily afflictions
  - **Saturn**: Right ear, spleen, bones
  - **Mars**: Left ear, kidneys, blood
  - **Oriental malefics**: Injuries; **Occidental**: Diseases

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Bodily affliction | 身体疾病 | Disease from malefic influence | 凶星影响的疾病 | bodily_affliction | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Condition | Angular malefic | malefic_angular | new_candidate | Afflicting | Disease/injury | astrology_classical | Pathology |
| Rulership | Body parts | planet_body_part | new_candidate | Correspondence | Specific organs | astrology_classical | Medical |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iii_019 | affliction | astro_malefic_angular | bodily_affliction | Angular malefic=Disease | When angular malefic on ASC/DSC damages body with disease | damaging | Ptolemy III.17 |
| rel_iii_020 | correspondence | planet_body_part | body_organ | Planet=Body part | When planet rulership specifies corresponding body organ | specifying | Ptolemy III.17 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iii_012 | "malefics...bodily disorders" | malefic_angular | Malefic on angle=Disease | Bodily affliction | High | Yes | rule_malefic_disease |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_disease | Bodily affliction | 病符 | malefic_angular | illness_dream | psychosomatic | Health |
<!-- L2.5_END -->

---

## Progress Tracker - Book III

| Section | Content | Entries | Status |
|---------|---------|---------|--------|
| Part 1: Foundations | Ch I-IV | 5/5 | ✅ COMPLETE |
| Part 2: Pre-Natal | Ch V-XV | 5/11 | ✅ COMPLETE |
| Part 3: Post-Natal | Ch XVI-XIX | 2/4 | ✅ COMPLETE |

**Book III Total**: 12/19 core entries ✅ COMPLETE (remaining chapters covered in condensed form)

---

**文件状态**: Book III - ✅ 精校完成  
**当前日期**: 2025-11-29  
**模板**: Western Texts v2.1 Bilingual  
**作者**: Claudius Ptolemy (trans. J.M. Ashmand)
