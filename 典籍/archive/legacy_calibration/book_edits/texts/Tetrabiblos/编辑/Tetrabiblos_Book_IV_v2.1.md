# Tetrabiblos Book IV: Life Events & Predictions (Complete L1+L2 v2.1)

**Author**: Claudius Ptolemy | **Translator**: J.M. Ashmand | **Publication**: c.150 CE | **Agent**: Text-EN-Agent | **Date**: 2025-11-29

---

## Status: ✅ COMPLETE

**Coverage Target**: 10 Chapters (IV.1-IV.10)

**Note**: Book IV covers **life events** beyond duration—fortune, rank, profession, marriage, children, friends/enemies, travel, and manner of death.

---

## PART 1: Fortune and Rank (Chapters I-III)

### 1. Fortune and Wealth (Chapter I)

<!-- L1_BEGIN -->
**Source Text** (Lines 7100-7200):
> The consideration of fortune requires to be entered into with a view to ascertaining, whether it will be great or small, and from what sources it will be derived... The part of Fortune, and the places of its rulers, the Moon, and the planets configurated with them, are to be observed.

**English Paraphrase (Primary Language)**:
**Material fortune** is judged from:

1. **Part of Fortune** (Lot of Fortune) and its rulers
2. **Moon** and her configurations
3. **Planets aspectng Part of Fortune**

**Wealth indicators**:
- Benefics (Jupiter, Venus) ruling/aspecting Part of Fortune = prosperity
- Malefics (Saturn, Mars) afflicting = poverty, loss
- Part of Fortune in angles = prominent fortune
- Part of Fortune cadent = humble circumstances

**Sources of wealth** depend on the planet ruling Part of Fortune:
- Saturn: Agriculture, building, navigation
- Jupiter: Trusts, stewardships, priesthoods
- Mars: Military, command, fire-related
- Venus: Gifts, women, ornaments
- Mercury: Trade, commerce, rhetoric

**Complete Chinese Interpretation (Secondary Language)**:
**物质财富**从以下判断：

1. **福点**（命运之分）及其主星
2. **月亮**及其配置
3. **与福点相位的行星**

**财富指标**：
- 吉星（木星、金星）主宰/相位福点 = 繁荣
- 凶星（土星、火星）刑克 = 贫穷、损失
- 福点在角宫 = 显著财富
- 福点在果宫 = 卑微处境

**财富来源**取决于主宰福点的行星：
- 土星：农业、建筑、航海
- 木星：信托、管理、祭司
- 火星：军事、指挥、与火相关
- 金星：礼物、女性、装饰品
- 水星：贸易、商业、修辞

**Core Points**:
- Part of Fortune = primary wealth indicator
- Benefic rulers = prosperity; Malefic rulers = poverty
- Angular Part = prominent; Cadent Part = humble
- Ruling planet determines wealth source
- Moon configurations modify fortune

**Narrative Snippets**:
- `[ns_tetra_iv001]` `[trigger: fortune_wealth]` `[factor_trigger: astro_part_of_fortune AND pars_fortunae AND benefic_ruler AND malefic_ruler AND wealth_outcome]` `[role: 主干]` Material fortune is judged from the Part of Fortune, its rulers, and the Moon's configurations. → Source Text IV.1
- `[ns_tetra_iv002]` `[trigger: wealth_source]` `[factor_trigger: astro_planet_ruler_fortune]` `[role: 条件分支]` The ruling planet of Part of Fortune determines the source of wealth—Saturn agriculture, Jupiter trusts, Mars military. → Source Text IV.1

**Textual Criticism**: Part of Fortune calculation: Day = ASC + Moon - Sun; Night = ASC + Sun - Moon (some traditions reverse).
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Material fortune and wealth determination through Part of Fortune
- **Natural Attributes**:
  - **Symbolism**: Fortune, wealth, prosperity, abundance, poverty
  - **Characteristics**: Benefic/malefic, angular/cadent, ruling planet nature
  - **Elements**: Part of Fortune, Moon, ruling planets, house position
- **Functional Symbolism**:
  - **Part of Fortune angular**: Prominent, visible wealth
  - **Benefic rulers**: Prosperity, ease of acquisition
  - **Malefic rulers**: Poverty, loss, difficulty
  - **Ruling planet**: Source/means of wealth acquisition
- **Conditional Structure**:
  - **Necessary Conditions**: Part of Fortune placement, ruling planet identified
  - **Enhancing Conditions**: Benefics aspecting, angular position
  - **Diminishing Conditions**: Malefics afflicting, cadent position
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Part of Fortune | 福点 | Arabic lot indicating material fortune | 指示物质财富的阿拉伯点 | pars_fortunae | existing |
| Doryphory | 护卫星 | Planets attending the luminaries | 随行发光体的行星 | doryphory | new_candidate |
| Angular fortune | 角宫财富 | Prominent wealth from angular placement | 角宫位置带来的显著财富 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Part of Fortune | pars_fortunae | existing | Primary | Fortune indicator | astrology_classical | Ptolemaic lot |
| Condition | Benefic ruler | benefic_ruler | existing | Enhancing | Prosperity | astrology_classical | Jupiter/Venus |
| Condition | Malefic ruler | malefic_ruler | existing | Diminishing | Poverty | astrology_classical | Saturn/Mars |
| Position | Angular | house_angular | existing | Amplifying | Prominence | astrology_classical | 1/4/7/10 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_001 | determination | pars_fortunae | wealth_outcome | Fortune indicator | When Part of Fortune angular or cadent determines wealth positive or negative | positive/negative | Ptolemy IV.1 |
| rel_iv_002 | modification | benefic_ruler | pars_fortunae | Prosperity | When benefic ruler aspects Part of Fortune enhancing prosperity | enhancing | Ptolemy IV.1 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_001 | "Part of Fortune...benefics...prosperity" | pars_fortunae, benefic_ruler | Fortune + Benefic = Prosperity | Wealth indication | High | Yes | rule_fortune_benefic |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_fortune | Material prosperity | 财星 | pars_fortunae | treasure_dream | financial_security | Wealth |
<!-- L2.5_END -->

---

### 2. Rank and Dignity (Chapter II)

<!-- L1_BEGIN -->
**Source Text** (Lines 7250-7350):
> The inquiry into the degree of dignity, in any nativity, is to be accomplished by means of the situation of the luminaries, and the familiarity subsisting between them and their attendant stars... If both luminaries be in masculine signs, and either both or one of them angular, especially if also attended by the five planets in glory, the persons then born will be kings.

**English Paraphrase (Primary Language)**:
**Rank and dignity** are determined by:

1. **Luminaries** (Sun and Moon) in masculine/feminine signs
2. **Angular positions** of luminaries
3. **Doryphory** (attendant planets) of luminaries

**Royal nativity** indicators:
- Both luminaries in masculine signs
- Both or one angular
- Attended by all five planets in dignity
- Fixed stars of first magnitude rising

**Noble but not royal**:
- Luminaries angular but not all planets attending
- Some planets in dignity, others not

**Common nativity**:
- Luminaries cadent or afflicted
- Malefics elevated over luminaries
- No planetary attendance

**Complete Chinese Interpretation (Secondary Language)**:
**地位与尊贵**由以下决定：

1. **发光体**（太阳和月亮）在阳/阴性星座
2. **发光体的角宫位置**
3. **发光体的护卫星**

**王室本命**指标：
- 两发光体都在阳性星座
- 两者或其一在角宫
- 五颗行星都以尊贵伴随
- 一等恒星升起

**贵族但非王室**：
- 发光体在角宫但非所有行星伴随
- 一些行星有尊贵，其他没有

**平民本命**：
- 发光体果宫或受刑
- 凶星高居于发光体之上
- 无行星伴随

**Core Points**:
- Luminaries in masculine signs + angular = high rank
- Full doryphory (all planets attending) = kingship
- Partial doryphory = nobility
- No doryphory, cadent luminaries = common status
- Fixed stars of first magnitude add eminence

**Narrative Snippets**:
- `[ns_tetra_iv003]` `[trigger: rank_dignity]` `[factor_trigger: astro_luminary_angular AND house_angular]` `[role: 主干]` Rank is determined by the luminaries' angular position and their planetary attendants. → Source Text IV.2
- `[ns_tetra_iv004]` `[trigger: royal_nativity]` `[factor_trigger: astro_doryphory_complete]` `[role: 条件分支]` Royal nativity: both luminaries in masculine signs, angular, attended by all five planets in dignity. → Source Text IV.2
- `[ns_tetra_iv_sm]` `[trigger: sun_moon]` `[factor_trigger: sun_moon]` `[role: 主干]` Sun and Moon together (luminaries) are primary rank indicators—their angular position and planetary attendants determine eminence. → Source Text IV.2
- `[ns_tetra_iv_ro]` `[trigger: rank_outcome]` `[factor_trigger: rank_outcome]` `[role: 效果]` Rank outcome ranges from kingship (full doryphory) through nobility (partial) to common status (none). → Source Text IV.2
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Social rank and dignity through luminary placement and doryphory
- **Natural Attributes**:
  - **Symbolism**: Kingship, nobility, eminence, common status
  - **Characteristics**: Luminary strength, planetary attendance, angular position
  - **Elements**: Sun, Moon, five planets, fixed stars, masculine/feminine signs
- **Functional Symbolism**:
  - **Full doryphory**: All planets attending luminaries = kingship
  - **Partial doryphory**: Some planets attending = nobility
  - **No doryphory**: No planets attending = common status
  - **Masculine signs**: Active, prominent, commanding
- **Conditional Structure**:
  - **Necessary Conditions**: Luminary position assessed, doryphory evaluated
  - **Royal Conditions**: Both luminaries masculine, angular, full doryphory
  - **Noble Conditions**: Luminaries angular, partial doryphory
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Doryphory | 护卫星 | Planets attending luminaries in dignity | 以尊贵伴随发光体的行星 | doryphory | new_candidate |
| Royal nativity | 王室本命 | Chart indicating kingship | 指示王权的命盘 | | new_candidate |
| Eminence | 显赫 | High social standing | 崇高的社会地位 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Luminaries | sun_moon | existing | Primary | Rank indicators | astrology_classical | Sun+Moon |
| Condition | Full doryphory | doryphory_complete | new_candidate | Royal | All 5 planets | astrology_classical | Kingship |
| Position | Angular | house_angular | existing | Amplifying | Prominence | astrology_classical | 1/4/7/10 |
| Quality | Masculine signs | sign_masculine | existing | Enhancing | Active rank | astrology_classical | Fire/Air |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_003 | determination | sun_moon | rank_outcome | Rank indicator | When Sun/Moon angular with doryphory amplifies rank outcome | amplifying | Ptolemy IV.2 |
| rel_iv_004 | enhancement | astro_doryphory_complete | sun_moon | Royal status | When complete doryphory with all planets in dignity grants royal status | maximum | Ptolemy IV.2 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_002 | "both luminaries...angular...five planets" | sun_moon, doryphory | Luminaries + Doryphory = Kingship | Royal indication | High | Yes | rule_royal_nativity |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_rank | Social eminence | 官星 | luminary_doryphory | crown_dream | authority_complex | Status |
<!-- L2.5_END -->

---

### 3. Profession and Employment (Chapter III)

<!-- L1_BEGIN -->
**Source Text** (Lines 7400-7550):
> The lord of action or profession is to be ascertained from the planet which may be in familiarity with the place of the mid-heaven, and with the place of the lord of that place, and with the Moon and the part of Fortune... Mercury makes scribes, astronomers, geometricians, accountants, teachers... Venus makes musicians, players, painters, perfumers... Mars makes soldiers, hunters, founders, carpenters, physicians, surgeons.

**English Paraphrase (Primary Language)**:
**Profession** is determined by the planet ruling:
- **Mid-heaven** (MC)
- **Moon's position**
- **Part of Fortune**

**Planetary professions**:

| Planet | Professions |
|--------|-------------|
| Saturn | Agriculture, navigation, building, mining, undertaking |
| Jupiter | Government, law, priesthood, banking, philosophy |
| Mars | Military, surgery, smithing, hunting, athletics |
| Venus | Music, art, perfumery, jewelry, prostitution |
| Mercury | Writing, teaching, astronomy, commerce, interpretation |
| Sun | Kingship, leadership, public offices |
| Moon | Navigation, midwifery, embassy, trade in liquids |

**Multiple planets** = multiple professions or trades combining their natures.
**Benefic configuration** = honorable profession; **Malefic** = dishonorable.

**Complete Chinese Interpretation (Secondary Language)**:
**职业**由主宰以下位置的行星决定：
- **中天**（MC）
- **月亮位置**
- **福点**

**行星职业**：

| 行星 | 职业 |
|------|------|
| 土星 | 农业、航海、建筑、采矿、殡葬 |
| 木星 | 政府、法律、祭司、银行、哲学 |
| 火星 | 军事、外科、冶炼、狩猎、竞技 |
| 金星 | 音乐、艺术、香水、珠宝、娼妓 |
| 水星 | 写作、教学、天文、商业、翻译 |
| 太阳 | 王权、领导、公职 |
| 月亮 | 航海、助产、使节、液体贸易 |

**多行星** = 多职业或结合其性质的行业。
**吉星配置** = 尊贵职业；**凶星** = 卑贱职业。

**Core Points**:
- MC ruler = primary profession indicator
- Each planet governs specific trades
- Multiple ruling planets = multiple or combined professions
- Benefic aspects = honorable work; Malefic = dishonorable
- Moon adds navigation and public dealings

**Narrative Snippets**:
- `[ns_tetra_iv005]` `[trigger: profession]` `[factor_trigger: astro_planet_ruler_mc]` `[role: 主干]` Profession is determined by the planet ruling the mid-heaven—each planet governs specific trades. → Source Text IV.3
- `[ns_tetra_iv006]` `[trigger: mercury_professions]` `[factor_trigger: astro_planet_mercury AND astro_house_10]` `[role: 条件分支]` Mercury ruling MC: scribes, astronomers, accountants, teachers, interpreters. → Source Text IV.3
- `[ns_tetra_iv_pt]` `[trigger: profession_type]` `[factor_trigger: profession_type]` `[role: 效果]` Profession type determined by MC ruler: Saturn=agriculture/building, Jupiter=law/religion, Mars=military/surgery, Venus=art/music, Mercury=writing/commerce. → Source Text IV.3
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Profession and employment through MC ruler and planetary significations
- **Natural Attributes**:
  - **Symbolism**: Work, vocation, career, trade, skill
  - **Characteristics**: MC ruler nature, benefic/malefic quality, planetary trades
  - **Elements**: MC, Moon, Part of Fortune, ruling planets
- **Functional Symbolism**:
  - **Saturn MC**: Agriculture, building, undertaking
  - **Jupiter MC**: Law, government, priesthood
  - **Mars MC**: Military, surgery, smithing
  - **Venus MC**: Art, music, ornaments
  - **Mercury MC**: Writing, teaching, commerce
- **Conditional Structure**:
  - **Necessary Conditions**: MC ruler identified
  - **Honorable Work**: Benefics aspecting MC ruler
  - **Dishonorable Work**: Malefics afflicting
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Lord of action | 行动主 | Planet ruling profession | 主宰职业的行星 | lord_of_action | new_candidate |
| Planetary trades | 行星职业 | Professions governed by each planet | 各行星主宰的职业 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | MC ruler | planet_ruler_mc | existing | Primary | Profession type | astrology_classical | 10th house |
| Profession | Saturn trades | saturn_profession | new_candidate | Category | Agriculture/Building | astrology_classical | Cold/Structure |
| Profession | Jupiter trades | jupiter_profession | new_candidate | Category | Law/Religion | astrology_classical | Expansion |
| Profession | Mars trades | mars_profession | new_candidate | Category | Military/Surgery | astrology_classical | Action/Cutting |
| Profession | Venus trades | venus_profession | new_candidate | Category | Art/Music | astrology_classical | Beauty/Pleasure |
| Profession | Mercury trades | mercury_profession | new_candidate | Category | Writing/Commerce | astrology_classical | Communication |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_005 | determination | astro_planet_ruler_mc | profession_type | Trade indicator | When MC ruler planet nature determines specific profession type | specific | Ptolemy IV.3 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_003 | "Mercury makes scribes...Venus musicians" | planet_trades | Planet → Trade type | Profession specification | High | Yes | rule_planetary_profession |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_profession | Vocation/career | 官杀印食 | mc_ruler | work_dream | vocational_identity | Career |
<!-- L2.5_END -->

---

### 4. Quality of Employment (Chapter IV)

<!-- L1_BEGIN -->
**Source Text** (Lines 7201-7398):
> The dominion of the employment, or profession, is claimed in two quarters; viz. by the Sun, and by the sign on the mid-heaven. It is necessary to observe whether any planet may be making its oriental appearance nearest to the Sun, and whether any be posited in the mid-heaven; especially, when also receiving the application of the Moon. Mercury produces writers, accountants, teachers in the sciences, merchants and bankers, astrologers. Venus produces those engaged in perfumes, flowers, wines, colours, dyes. Mars produces soldiers, founders, carpenters, physicians, surgeons.

**English Paraphrase (Primary Language)**:
**Quality of employment** is determined by planets:
1. Making oriental appearance nearest to Sun
2. Posited in MC receiving Moon's application

**Planetary professions** (detailed):
- **Mercury**: Writers, accountants, teachers, merchants, astrologers, interpreters
  - +Saturn = dream interpreters, temple diviners
  - +Jupiter = orators, painters, lawyers
- **Venus**: Perfumers, florists, wine merchants, dyers, painters
  - +Saturn = entertainers, jugglers, sorcerers
  - +Jupiter = athletes, honorees through women
- **Mars**: Those working with fire—cooks, metalworkers
  - Separated from Sun = shipwrights, smiths, carpenters
  - +Saturn = miners, butchers, bath attendants
  - +Jupiter = soldiers, tax collectors

**Complete Chinese Interpretation (Secondary Language)**:
**职业质量**由行星决定：
1. 在太阳附近东方升起
2. 位于中天接收月亮的入相

**行星职业**（详细）：
- **水星**：作家、会计师、教师、商人、占星家、翻译
  - +土星 = 解梦者、神庙占卜师
  - +木星 = 演说家、画家、律师
- **金星**：香水商、花商、酒商、染工、画家
  - +土星 = 艺人、杂耍者、巫师
  - +木星 = 运动员、因女性而获荣誉者
- **火星**：使用火工作的人——厨师、金属工人
  - 与太阳分离 = 造船工、铁匠、木匠
  - +土星 = 矿工、屠夫、浴室服务员
  - +木星 = 士兵、税务员

**Core Points**:
- Employment determined by oriental planet or MC ruler
- Three key planets: Mercury, Venus, Mars
- Saturn/Jupiter modify the base profession
- No planet in position = occasional employment only

**Narrative Snippets**:
- `[ns_tetra_iv_010]` `[trigger: employment_quality]` `[factor_trigger: astro_planet_profession]` `[role: 主干]` Employment quality determined by oriental planet or MC ruler—Mercury for writing, Venus for arts, Mars for manual work. → Source Text IV.4
- `[ns_tetra_iv_eq]` `[trigger: employment_quality]` `[factor_trigger: employment_quality]` `[role: 效果]` Employment quality: the specific nature of profession determined by oriental planet or MC position—honorable if benefic, dishonorable if malefic. → Source Text IV.4
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Quality and nature of profession
- **Natural Attributes**: Oriental appearance; MC position; planetary nature
- **Functional Symbolism**: Mercury=intellectual, Venus=artistic, Mars=physical

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Indicator | Employment quality | employment_quality | new_candidate | Determining | Oriental/MC | astrology_classical | Profession |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iv_010 | specification | employment_quality | planet_nature | Profession type | When planet's oriental appearance determines employment quality and type | determining | Ptolemy IV.4 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_010 | "Mercury produces writers" | employment_quality | Planet=Trade type | Profession nature | High | Yes | rule_employment |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_trade | Specific profession | 十神职业 | employment_quality | career_dream | vocational_aptitude | Specificity |
<!-- L2.5_END -->
<!-- L2_END -->

---

## PART 2: Relationships (Chapters V-VII)

### 5. Marriage (Chapter V)

<!-- L1_BEGIN -->
**Source Text** (Lines 7560-7605):
> In the case of men, the Moon and Venus are to be observed; for if they be in mutual configuration, or counterchanging places, the native will be connected with one wife only, provided they be also in fixed signs. If in bicorporeal or tropical signs, he will have several wives. If Saturn be in configuration, the marriage will be with elderly women; if Jupiter, with women of rank or wealth; if Mars, with bold or violent women.

**English Paraphrase (Primary Language)**:
**Marriage** indicators differ by sex:

**For men** (observe Moon and Venus):
- Moon-Venus in mutual configuration = harmonious marriage
- Fixed signs = one wife
- Bicorporeal/tropical signs = multiple marriages
- Saturn aspecting = elderly wife
- Jupiter aspecting = wealthy/noble wife
- Mars aspecting = bold/violent wife

**For women** (observe Sun and Mars):
- Sun-Mars harmonious = good husband
- Fixed signs = one husband
- Bicorporeal = multiple husbands
- Saturn aspecting = elderly husband
- Jupiter aspecting = dignified husband
- Venus aspecting = handsome husband

**Sexual morality** also judged from Venus-Mars configurations.

**Complete Chinese Interpretation (Secondary Language)**:
**婚姻**指标因性别而异：

**对于男性**（观察月亮和金星）：
- 月-金相互配置 = 和谐婚姻
- 固定星座 = 一妻
- 双体/回归星座 = 多婚
- 土星相位 = 年长妻子
- 木星相位 = 富贵妻子
- 火星相位 = 大胆/暴力妻子

**对于女性**（观察太阳和火星）：
- 日-火和谐 = 好丈夫
- 固定星座 = 一夫
- 双体 = 多夫
- 土星相位 = 年长丈夫
- 木星相位 = 尊贵丈夫
- 金星相位 = 英俊丈夫

**Core Points**:
- Men: Moon-Venus = marriage significators
- Women: Sun-Mars = marriage significators
- Fixed signs = one spouse; Bicorporeal = multiple
- Aspecting planets modify spouse's character
- Venus-Mars configurations = sexual morality

**Narrative Snippets**:
- `[ns_tetra_iv007]` `[trigger: marriage_men]` `[factor_trigger: astro_moon_venus]` `[role: 主干]` For men, marriage is judged from Moon and Venus—their configuration shows marital harmony. → Source Text IV.5
- `[ns_tetra_iv008]` `[trigger: marriage_women]` `[factor_trigger: astro_sun_mars]` `[role: 条件分支]` For women, marriage is judged from Sun and Mars—their configuration shows husband's character. → Source Text IV.5
- `[ns_tetra_iv018]` `[trigger: marriage_number]` `[factor_trigger: astro_sign_fixed AND astro_sign_bicorporeal]` `[role: 条件分支]` Fixed signs = one spouse; bicorporeal or tropical signs = multiple marriages. → Number
- `[ns_tetra_iv019]` `[trigger: spouse_character]` `[factor_trigger: astro_saturn AND astro_jupiter AND astro_mars]` `[role: 条件分支]` Saturn aspect = elderly spouse; Jupiter = wealthy/noble; Mars = bold/violent. → Character
- `[ns_tetra_iv_sf]` `[trigger: spouse_female]` `[factor_trigger: spouse_female]` `[role: 效果]` Wife characteristics (for male natives) judged from Moon and Venus: their sign, aspects, and planetary configurations describe her nature. → Source Text IV.5
- `[ns_tetra_iv_sm2]` `[trigger: spouse_male]` `[factor_trigger: spouse_male]` `[role: 效果]` Husband characteristics (for female natives) judged from Sun and Mars: their sign, aspects, and planetary configurations describe his nature. → Source Text IV.5
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Marriage and spouse characteristics through gender-specific significators
- **Natural Attributes**:
  - **Symbolism**: Marriage, spouse, partnership, sexual morality
  - **Characteristics**: Fixed/mutable signs, planetary aspects, gender differentiation
  - **Elements**: Moon-Venus (men), Sun-Mars (women), aspecting planets
- **Functional Symbolism**:
  - **Fixed signs**: One spouse, stable marriage
  - **Bicorporeal signs**: Multiple marriages
  - **Saturn aspect**: Elderly spouse
  - **Jupiter aspect**: Wealthy/noble spouse
  - **Mars aspect**: Bold/violent spouse
- **Conditional Structure**:
  - **For men**: Moon-Venus configuration = marriage quality
  - **For women**: Sun-Mars configuration = husband quality
  - **Sign modality**: Fixed = one; Mutable = many
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Marriage significators | 婚姻征象星 | Planets indicating spouse | 指示配偶的行星 | marriage_sig | new_candidate |
| Spouse character | 配偶性格 | Nature of marriage partner | 婚姻伴侣的性质 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Moon-Venus (men) | moon_venus | existing | Primary | Wife indicator | astrology_classical | Male natives |
| Significator | Sun-Mars (women) | sun_mars | existing | Primary | Husband indicator | astrology_classical | Female natives |
| Condition | Fixed signs | sign_fixed | existing | Stabilizing | One spouse | astrology_classical | Fidelity |
| Condition | Bicorporeal signs | sign_bicorporeal | existing | Multiplying | Multiple spouses | astrology_classical | Plurality |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_006 | signification | astro_moon_venus | spouse_female | Wife indicator | When Moon and Venus describe wife characteristics for male native | descriptive | Ptolemy IV.5 |
| rel_iv_007 | signification | astro_sun_mars | spouse_male | Husband indicator | When Sun and Mars describe husband characteristics for female native | descriptive | Ptolemy IV.5 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_004 | "Moon and Venus...one wife...fixed signs" | moon_venus, sign_fixed | Fixed = One spouse | Marriage number | High | Yes | rule_marriage_number |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_marriage | Spousal partnership | 夫妻宫星 | moon_venus/sun_mars | wedding_dream | attachment_style | Partnership |
<!-- L2.5_END -->

---

### 6. Children (Chapter VI)

<!-- L1_BEGIN -->
**Source Text** (Lines 7645-7728):
> The Moon, Jupiter, and Venus are esteemed as givers of offspring; but the Sun, Mars, and Saturn are considered as denying children altogether, or as allowing but few... if prolific signs, such as Pisces, Cancer, and Scorpio, they will grant twins, or even more.

**English Paraphrase (Primary Language)**:
**Children** are judged from:
- **Mid-heaven** and **11th house** (Good Dæmon)
- Planets configurated with these places

**Child-giving planets**: Moon, Jupiter, Venus
**Child-denying planets**: Sun, Saturn, Mars
**Mercury**: Common—gives when oriental, denies when occidental

**Number of children**:
- Single = planets in signs of single form
- Twins/more = planets in bicorporeal or prolific signs (Pisces, Cancer, Scorpio)

**Health of children**:
- Benefics ruling = healthy, long-lived
- Malefics ruling = sickly, short-lived
- Malefics elevated over child-givers = children die young

**Complete Chinese Interpretation (Secondary Language)**:
**子女**从以下判断：
- **中天**和**第11宫**（善精灵）
- 与这些位置配置的行星

**赐子行星**：月亮、木星、金星
**无子行星**：太阳、土星、火星
**水星**：共通——东方时赐，西方时拒

**子女数量**：
- 单一 = 行星在单形星座
- 双胞胎/更多 = 行星在双体或多产星座（双鱼、巨蟹、天蝎）

**子女健康**：
- 吉星主宰 = 健康、长寿
- 凶星主宰 = 多病、短命
- 凶星高居于赐子星之上 = 子女夭折

**Core Points**:
- MC and 11th house = children places
- Moon/Jupiter/Venus = child-givers; Sun/Saturn/Mars = deniers
- Prolific signs = twins or more
- Malefics afflicting = sickly or dying children

**Narrative Snippets**:
- `[ns_tetra_iv009]` `[trigger: children_givers]` `[factor_trigger: astro_planet_fertile]` `[role: 主干]` Moon, Jupiter, and Venus are child-giving planets; Sun, Saturn, Mars deny or limit offspring. → Source Text IV.6
- `[ns_tetra_iv010]` `[trigger: prolific_signs]` `[factor_trigger: astro_sign_prolific]` `[role: 条件分支]` Prolific signs (Pisces, Cancer, Scorpio) indicate twins or multiple children. → Source Text IV.6
- `[ns_tetra_iv020]` `[trigger: children_health]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics ruling children places = healthy, long-lived; malefics elevated = sickly or die young. → Health
- `[ns_tetra_iv_co]` `[trigger: children_outcome]` `[factor_trigger: children_outcome]` `[role: 效果]` Children outcome: many/healthy if fertile planets (Moon/Jupiter/Venus) in 11th/MC; few/sickly if barren planets (Sun/Saturn/Mars). → Source Text IV.6
- `[ns_tetra_iv_pb]` `[trigger: planet_barren]` `[factor_trigger: planet_barren]` `[role: 条件分支]` Barren planets (Sun, Saturn, Mars) deny children or grant few—especially when in MC or 11th house. → Source Text IV.6
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Children through 11th house and fertility indicators
- **Natural Attributes**:
  - **Symbolism**: Offspring, fertility, barrenness, health of children
  - **Characteristics**: Child-giving vs denying planets, prolific signs
  - **Elements**: MC, 11th house, Moon, Jupiter, Venus, Saturn, Mars
- **Functional Symbolism**:
  - **Child-givers**: Moon, Jupiter, Venus = fertility
  - **Child-deniers**: Sun, Saturn, Mars = barrenness or few
  - **Prolific signs**: Pisces, Cancer, Scorpio = twins/more
  - **Malefics elevated**: Children sickly or die young
- **Conditional Structure**:
  - **Necessary Conditions**: 11th house/MC planets assessed
  - **Fertility Conditions**: Benefics ruling, prolific signs
  - **Barrenness Conditions**: Malefics ruling, barren signs
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Child-giving planets | 赐子行星 | Planets granting offspring | 赐予子女的行星 | planet_fertile | new_candidate |
| Prolific signs | 多产星座 | Signs indicating multiple births | 指示多胎的星座 | sign_prolific | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Child-givers | planet_fertile | new_candidate | Granting | Moon/Jupiter/Venus | astrology_classical | Fertility |
| Significator | Child-deniers | planet_barren | new_candidate | Denying | Sun/Saturn/Mars | astrology_classical | Barrenness |
| Sign | Prolific | sign_prolific | new_candidate | Multiplying | Pisces/Cancer/Scorpio | astrology_classical | Watery |
| House | 11th house | house_11 | existing | Children place | Good Dæmon | astrology_classical | Offspring |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_008 | granting | astro_planet_fertile | children_outcome | Fertility | When fertile planets in MC/11th grant positive children outcome | positive | Ptolemy IV.6 |
| rel_iv_009 | denying | planet_barren | children_outcome | Barrenness | When barren planets in MC/11th deny children with negative outcome | negative | Ptolemy IV.6 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_005 | "Moon, Jupiter, Venus...givers of offspring" | planet_fertile | Benefics = Fertility | Child granting | High | Yes | rule_child_givers |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_children | Offspring/fertility | 子女宫 | house_5_11 | baby_dream | generativity | Progeny |
<!-- L2.5_END -->

---

### 7. Friends and Enemies (Chapter VII)

<!-- L1_BEGIN -->
**Source Text** (Lines 7743-7864):
> Indications of great and lasting friendships, or enmities, may be perceived by observation of the ruling places, exhibited in the respective nativities of both the persons... should all these in both nativities be in the same signs, or should they be counterchanged in position, they will create fixed and indissoluble friendship.

**English Paraphrase (Primary Language)**:
**Friendships and enmities** are determined by comparing two nativities:

**Lasting friendship** indicators:
- Sun, Moon, ASC, Part of Fortune in same signs in both charts
- Or counterchanged (swapped positions)
- Ascendants within 17° of each other

**Lasting enmity** indicators:
- Above places in inconjunct signs
- Or in opposition

**Three types of friendship**:
1. **Spontaneous** (from luminaries): Pure goodwill
2. **Profit-based** (from Part of Fortune): Material benefit
3. **Pleasure/Pain** (from Ascendants): Emotional bond

**Casual friendships/strifes** arise from planetary ingresses between nativities.

**Complete Chinese Interpretation (Secondary Language)**:
**友谊和敌意**通过比较两个本命盘确定：

**持久友谊**指标：
- 太阳、月亮、上升、福点在两盘中同星座
- 或互换位置
- 上升点相距17°以内

**持久敌意**指标：
- 上述位置在不合星座
- 或在对分

**三种友谊类型**：
1. **自发的**（来自发光体）：纯粹善意
2. **利益导向**（来自福点）：物质利益
3. **快乐/痛苦**（来自上升点）：情感纽带

**Core Points**:
- Compare Sun, Moon, ASC, Part of Fortune between charts
- Same signs or counterchange = lasting friendship
- Inconjunct or opposition = lasting enmity
- Three friendship types: spontaneous, profit-based, emotional
- Planetary ingresses create temporary friendships/strifes

**Narrative Snippets**:
- `[ns_tetra_iv011]` `[trigger: synastry_friendship]` `[factor_trigger: astro_chart_comparison]` `[role: 主干]` Friendships are judged by comparing the Sun, Moon, ASC, and Part of Fortune between two nativities. → Source Text IV.7
- `[ns_tetra_iv021]` `[trigger: lasting_bond]` `[factor_trigger: astro_same_sign AND astro_counterchange]` `[role: 条件分支]` Same signs or counterchanged positions create fixed and indissoluble friendship; ASCs within 17° = strong bond. → Bond
- `[ns_tetra_iv022]` `[trigger: three_friendships]` `[factor_trigger: astro_luminaries AND astro_fortune AND astro_asc]` `[role: 条件分支]` Three types of friendship: spontaneous (from luminaries), profit-based (from Fortune), emotional (from ASC). → Types
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Synastry and relationship compatibility through chart comparison
- **Natural Attributes**:
  - **Symbolism**: Friendship, enmity, compatibility, discord
  - **Characteristics**: Same-sign placement, counterchange, inconjunct
  - **Elements**: Sun, Moon, ASC, Part of Fortune between charts
- **Functional Symbolism**:
  - **Same signs**: Lasting friendship from common resonance
  - **Counterchanged**: Deep bond from mutual exchange
  - **Inconjunct/Opposition**: Lasting enmity from discord
  - **Three types**: Spontaneous (luminaries), profit (Fortune), emotional (ASC)
- **Conditional Structure**:
  - **Friendship Conditions**: Same signs or counterchange, ASCs within 17°
  - **Enmity Conditions**: Inconjunct or opposition placements
  - **Casual Relations**: Planetary ingresses between charts
  - **Temporal Scope**:
    - [x] Natal layer (synastry)
    - [x] Transit layer (ingresses)
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Synastry | 合盘 | Chart comparison for relationships | 关系的命盘比较 | synastry | new_candidate |
| Counterchange | 互换 | Swapped placements between charts | 两盘之间的位置交换 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Technique | Synastry | synastry | new_candidate | Comparison | Chart to chart | astrology_classical | Relationships |
| Relation | Same sign | same_sign | new_candidate | Bonding | Friendship | astrology_classical | Compatibility |
| Relation | Inconjunct | inconjunct | existing | Severing | Enmity | astrology_classical | Discord |
| Relation | Counterchange | counterchange | new_candidate | Deep bond | Exchange | astrology_classical | Mutual |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_010 | comparison | chart_a_places | chart_b_places | Synastry | When chart places in same or opposite signs indicate friendship or enmity | friendship/enmity | Ptolemy IV.7 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_006 | "same signs...fixed and indissoluble friendship" | same_sign | Same sign = Lasting friendship | Synastry positive | High | Yes | rule_synastry_friend |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_friendship | Interpersonal bonds | 六合三合 | synastry | friend_dream | attachment | Relations |
<!-- L2.5_END -->

---

## PART 3: Events and Death (Chapters VIII-X)

### 8. Travelling (Chapter VIII)

<!-- L1_BEGIN -->
**Source Text** (Lines 7872-7937):
> The circumstances indicative of travel are to be considered by means of the situation held by both the luminaries, in respect to the angles... should she be descending, or cadent from the angles, she will cause journeys and changes of residence.

**English Paraphrase (Primary Language)**:
**Travel** is indicated by:
- **Moon cadent** from angles = journeys and relocations
- **Mars cadent** from zenith, in quartile/opposition to luminaries = same
- **Part of Fortune** in travel-producing signs

**Quality of travel**:
- Benefics supervising = honorable, profitable, safe return
- Malefics supervising = perilous, fruitless, difficult return

**Direction of travel**:
- Luminaries in oriental/cadent houses = east or south
- Luminaries in occidental = north or west

**Frequency**:
- Single-form signs = occasional travel
- Bicorporeal signs = constant travel

**Dangers**:
- Saturn/Mars in watery signs = shipwreck
- In fixed signs = precipices, winds
- In tropical = lack of necessities
- In human signs = robbery
- In terrestrial = wild beasts

**Complete Chinese Interpretation (Secondary Language)**:
**旅行**由以下指示：
- **月亮果宫**于角宫 = 旅行和搬迁
- **火星果宫**于天顶，与发光体四分/对分 = 同样
- **福点**在产生旅行的星座

**旅行质量**：
- 吉星监督 = 尊贵、有利、安全返回
- 凶星监督 = 危险、无果、艰难返回

**旅行方向**：
- 发光体在东方/果宫 = 东或南
- 发光体在西方 = 北或西

**Core Points**:
- Moon/Mars cadent = travel indicated
- Benefics = safe, profitable; Malefics = dangerous
- Sign type determines travel frequency and dangers
- Direction from luminary position

**Narrative Snippets**:
- `[ns_tetra_iv012]` `[trigger: travel_indicated]` `[factor_trigger: astro_moon_cadent]` `[role: 主干]` Travel is indicated when Moon is cadent from angles or Part of Fortune is in travel-producing signs. → Source Text IV.8
- `[ns_tetra_iv023]` `[trigger: travel_safety]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics supervising = honorable, profitable, safe return; malefics = perilous, fruitless, difficult return. → Safety
- `[ns_tetra_iv024]` `[trigger: travel_danger]` `[factor_trigger: astro_saturn AND astro_mars AND astro_sign]` `[role: 条件分支]` Saturn/Mars in watery signs = shipwreck; in fixed = precipices; in human = robbery; in terrestrial = wild beasts. → Dangers
- `[ns_tetra_iv_to]` `[trigger: travel_outcome]` `[factor_trigger: travel_outcome]` `[role: 效果]` Travel outcome: safe and profitable if benefics supervise; dangerous and fruitless if malefics supervise. → Source Text IV.8
- `[ns_tetra_iv_bs]` `[trigger: benefic_supervise]` `[factor_trigger: benefic_supervise]` `[role: 条件分支]` Benefic supervision (Jupiter/Venus aspecting travel indicators) produces honorable, profitable journeys with safe return. → Source Text IV.8
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Travel and foreign residence through cadent Moon and sign types
- **Natural Attributes**:
  - **Symbolism**: Journey, relocation, foreign lands, peril, return
  - **Characteristics**: Cadent positions, sign types, benefic/malefic supervision
  - **Elements**: Moon, Mars, Part of Fortune, luminaries, angles
- **Functional Symbolism**:
  - **Moon cadent**: Travel and changes of residence
  - **Benefics supervising**: Safe, profitable, quick return
  - **Malefics supervising**: Perilous, fruitless, difficult return
  - **Sign types**: Watery = shipwreck; Fixed = precipices; Human = robbery
- **Conditional Structure**:
  - **Travel Indicated**: Moon/Mars cadent, Part of Fortune in travel signs
  - **Safe Travel**: Benefics ruling/aspecting
  - **Dangerous Travel**: Malefics ruling/aspecting
  - **Temporal Scope**:
    - [x] Natal layer
    - [x] Transit layer (timing)
    - [ ] Progression layer

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Travel indicator | 旅行指标 | Configurations showing journeys | 显示旅行的配置 | travel_indicator | new_candidate |
| Travel-producing signs | 产生旅行的星座 | Signs that cause journeys | 导致旅行的星座 | | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Indicator | Moon cadent | moon_cadent | existing | Primary | Travel trigger | astrology_classical | Journeys |
| Condition | Benefic supervision | benefic_supervise | existing | Protective | Safe travel | astrology_classical | Protection |
| Condition | Malefic supervision | malefic_supervise | existing | Dangerous | Perilous travel | astrology_classical | Danger |
| Sign | Watery | sign_watery | existing | Danger type | Shipwreck | astrology_classical | Drowning |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_011 | indication | astro_moon_cadent | travel_outcome | Travel trigger | When cadent Moon from angles initiates travel indication | initiating | Ptolemy IV.8 |
| rel_iv_012 | modification | benefic_supervise | travel_outcome | Safe travel | When benefic planets supervising by aspect protect travel outcome | protective | Ptolemy IV.8 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_007 | "Moon...cadent...journeys and changes" | moon_cadent | Cadent Moon = Travel | Travel indication | High | Yes | rule_travel_moon |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_travel | Movement/journey | 驿马 | moon_cadent | journey_dream | wanderlust | Mobility |
<!-- L2.5_END -->

---

### 9. The Kind of Death (Chapter IX)

<!-- L1_BEGIN -->
**Source Text** (Lines 7946-8098):
> It now remains to treat of the kind and species of death... Hence, if it happen that Saturn be in fixed signs, and in quartile or opposition to the Sun, he will produce death by suffocation, occasioned either by multitudes of people, or by hanging or strangulation... Mars will produce death by slaughter, either in civil or foreign war, or by suicide.

**English Paraphrase (Primary Language)**:
**Manner of death** is determined by:
- The **anæretic place** (from duration of life analysis)
- **Planets in dominion** over that place
- **Sign characteristics** of the anæretic degree

**Planetary death types**:

| Planet | Natural Death | Violent Death |
|--------|---------------|---------------|
| Saturn | Lingering diseases, cold, consumption, dropsy | Suffocation, hanging, strangulation, drowning |
| Jupiter | Quinsy, lung inflammation, apoplexy | Wrath of kings, judicial condemnation |
| Mars | Fevers, hemorrhage, inflammation | Slaughter, war, suicide, fire, decapitation |
| Venus | Stomach/liver disorders, consumption | Poison, female treachery |
| Mercury | Fury, madness, epilepsy, dry diseases | Combined with malefics |

**Saturn violent indicators**:
- In fixed signs + quartile/opposition Sun = suffocation, hanging
- In bestial signs = wild beasts
- In watery signs + Moon = drowning
- In tropical signs + Sun = building collapse

**Mars violent indicators**:
- In human signs = slaughter, war, suicide
- Near Gorgon (Algol) = decapitation
- In Scorpio/Taurus = surgery, burning
- In mid-heaven = crucifixion

**Complete Chinese Interpretation (Secondary Language)**:
**死亡方式**由以下决定：
- **截寿位置**（来自寿命分析）
- **主宰该位置的行星**
- **截寿度数的星座特征**

**行星死亡类型**：

| 行星 | 自然死亡 | 暴力死亡 |
|------|----------|----------|
| 土星 | 慢性病、寒冷、消耗、水肿 | 窒息、绞刑、勒死、溺水 |
| 木星 | 喉痹、肺炎、中风 | 王怒、司法定罪 |
| 火星 | 发烧、出血、炎症 | 屠杀、战争、自杀、火、斩首 |
| 金星 | 胃/肝疾病、消耗 | 毒药、女性背叛 |
| 水星 | 狂怒、疯狂、癫痫、干燥疾病 | 与凶星结合 |

**Core Points**:
- Anæretic place and its ruler determine death manner
- Saturn = cold/lingering or suffocation/drowning
- Mars = hot/inflammatory or violent/war
- Sign type modifies death manner
- Both malefics in anæretic = body unburied

**Narrative Snippets**:
- `[ns_tetra_iv013]` `[trigger: death_manner]` `[factor_trigger: astro_planet_anaeretic]` `[role: 主干]` The manner of death is determined by the planet ruling the anæretic place—each planet produces distinctive death types. → Source Text IV.9
- `[ns_tetra_iv014]` `[trigger: saturn_death]` `[factor_trigger: astro_planet_saturn AND astro_place_anaeretic]` `[role: 条件分支]` Saturn in anæretic position: natural death by cold diseases; violent by suffocation, hanging, drowning. → Source Text IV.9
- `[ns_tetra_iv015]` `[trigger: mars_death]` `[factor_trigger: astro_planet_mars AND astro_place_anaeretic]` `[role: 条件分支]` Mars in anæretic position: natural death by fevers; violent by slaughter, war, fire, decapitation. → Source Text IV.9
- `[ns_tetra_iv025]` `[trigger: algol_decapitation]` `[factor_trigger: astro_mars AND astro_algol]` `[role: 条件分支]` Mars near Gorgon (Algol) indicates death by decapitation; both malefics in anæretic = body unburied. → Source Text IV.9
- `[ns_tetra_iv_dt]` `[trigger: death_type]` `[factor_trigger: death_type]` `[role: 效果]` Death type determined by anæretic ruler: Saturn=cold/suffocation, Mars=hot/violence, Jupiter=lung/judicial, Venus=poison, Mercury=madness. → Source Text IV.9
- `[ns_tetra_iv_dm]` `[trigger: dual_malefic]` `[factor_trigger: dual_malefic]` `[role: 条件分支]` Both malefics (Saturn and Mars) in anæretic position intensify to violent death with body unburied. → Source Text IV.9

**Textual Criticism**: This chapter is the most detailed in classical literature on manner of death; foundation for all subsequent medieval death-determination techniques.
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction

- **Theme**: Manner of death through anæretic ruler and sign characteristics
- **Natural Attributes**:
  - **Symbolism**: Death, ending, natural/violent, disease type
  - **Characteristics**: Anæretic ruler nature, sign type, malefic configurations
  - **Elements**: Saturn, Mars, Jupiter, Venus, Mercury, signs, fixed stars
- **Functional Symbolism**:
  - **Saturn anæretic**: Cold diseases (natural) or suffocation/drowning (violent)
  - **Mars anæretic**: Fevers/inflammation (natural) or war/fire/decapitation (violent)
  - **Jupiter anæretic**: Lung diseases or judicial condemnation
  - **Venus anæretic**: Stomach/liver or poison/treachery
  - **Mercury anæretic**: Madness/epilepsy or combined with malefics
- **Conditional Structure**:
  - **Natural Death**: Anæretic ruler without violent configurations
  - **Violent Death**: Both malefics in anæretic, luminary affliction
  - **Sign Modification**: Fixed = suffocation; Watery = drowning; Human = slaughter
  - **Temporal Scope**:
    - [x] Natal layer
    - [ ] Transit layer
    - [x] Progression layer (directions)

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Anæretic place | 截寿位置 | Life-ending degree in directions | 主限中终结生命的度数 | anaeretic | existing |
| Violent death | 暴死 | Death by external force | 外力导致的死亡 | violent_death | new_candidate |
| Natural death | 自然死亡 | Death by disease | 疾病导致的死亡 | natural_death | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Significator | Anæretic ruler | planet_anaeretic | existing | Primary | Death type | astrology_classical | Directions |
| Death Type | Saturn death | saturn_death | existing | Cold/Suffocation | Lingering/Hanging | astrology_classical | Cold |
| Death Type | Mars death | mars_death | existing | Hot/Violent | Fever/War | astrology_classical | Hot |
| Death Type | Jupiter death | jupiter_death | existing | Respiratory/Legal | Lung/Judicial | astrology_classical | Expansion |
| Condition | Both malefics | dual_malefic | existing | Violent | Unburied | astrology_classical | Extreme |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_iv_013 | determination | astro_planet_anaeretic | death_type | Death manner | When anaeretic planet nature specifies manner of death | specifying | Ptolemy IV.9 |
| rel_iv_014 | intensification | dual_malefic | death_type | Violent death | When both malefics in anaeretic position intensify to violent death | extreme | Ptolemy IV.9 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_008 | "Saturn...lingering diseases...suffocation" | saturn_death | Saturn → Cold/Suffocation | Death specification | High | Yes | rule_saturn_death |
| evi_iv_009 | "Mars...fevers...slaughter, war" | mars_death | Mars → Hot/Violence | Death specification | High | Yes | rule_mars_death |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_death | Life ending | 死绝 | anaeretic | death_dream | mortality_awareness | Ending |
<!-- L2.5_END -->

---

### 10. Periodical Divisions of Time (Chapter X)

<!-- L1_BEGIN -->
**Source Text** (Lines 8128-8280):
> Further attention is demanded with respect to the division of time. The mode of consideration applicable to human nature is universally one and the same; it is analogous to the arrangement of the seven planetary orbs. It commences with the first age of human life and the first sphere next above the earth, that of the Moon, and terminates with the final age of man and the last planetary sphere, that of Saturn.

**English Paraphrase (Primary Language)**:
**Periodical divisions of time** correlate life stages with planetary spheres:

| Planet | Age | Years | Characteristics |
|--------|-----|-------|-----------------|
| Moon | Infancy | 0-4 | Moist, rapid growth, variable |
| Mercury | Childhood | 4-14 | Learning, reason develops |
| Venus | Adolescence | 14-22 | Sexuality, passion |
| Sun | Adulthood | 22-41 | Authority, career, glory |
| Mars | Maturity | 41-56 | Austerity, vexation, care |
| Jupiter | Seniority | 56-68 | Gravity, prudence, honor |
| Saturn | Old age | 68+ | Coldness, mental slowness |

**Additional prorogations** for specific life domains:
- ASC prorogation = body and travel
- Part of Fortune = wealth
- Moon = mind and relationships
- Sun = dignities and glory
- MC = employment, friends, children

**Complete Chinese Interpretation (Secondary Language)**:
**时间的周期划分**将人生阶段与行星天体对应：

| 行星 | 年龄段 | 年份 | 特征 |
|-----|------|-----|-----|
| 月亮 | 婴儿期 | 0-4 | 潮湿、快速生长、多变 |
| 水星 | 童年期 | 4-14 | 学习、理性发展 |
| 金星 | 青春期 | 14-22 | 性欲、激情 |
| 太阳 | 成年期 | 22-41 | 权威、事业、荣耀 |
| 火星 | 壮年期 | 41-56 | 严肃、烦恼、忧虑 |
| 木星 | 老年前期 | 56-68 | 庄重、审慎、荣誉 |
| 土星 | 老年期 | 68+ | 寒冷、精神迟缓 |

**特定生活领域的附加推运**：
- 上升推运 = 身体和旅行
- 福点 = 财富
- 月亮 = 心智和关系
- 太阳 = 尊严和荣耀
- 中天 = 职业、朋友、子女

**Core Points**:
- Seven ages of man correspond to seven planets
- Each planet governs its appropriate life stage
- Multiple prorogations for different life areas
- Events may be mixed (good and bad simultaneously)

**Narrative Snippets**:
- `[ns_tetra_iv_020]` `[trigger: time_division]` `[factor_trigger: astro_planet_age]` `[role: 主干]` Seven ages of life correspond to seven planets—Moon for infancy, Mercury for childhood, through Saturn for old age. → Source Text IV.10
- `[ns_tetra_iv_ls]` `[trigger: life_stage]` `[factor_trigger: life_stage]` `[role: 效果]` Life stage governed by planetary period: Moon=0-4, Mercury=4-14, Venus=14-22, Sun=22-41, Mars=41-56, Jupiter=56-68, Saturn=68+. → Source Text IV.10
<!-- L1_END -->

<!-- L2_BEGIN -->
#### v2.1 L2 Semantic Extraction
- **Theme**: Planetary ages of life
- **Natural Attributes**: Moon=infancy through Saturn=old age
- **Functional Symbolism**: Each planet governs appropriate life stage

<!-- FACTOR_BEGIN -->
#### Factor Layer
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Timing | Planetary age | planet_age | new_candidate | Governing | Moon-Saturn sequence | astrology_classical | Life stages |
| Prorogation | Multiple lords | prorogation_multiple | new_candidate | Determining | ASC/Fortune/Moon/Sun/MC | astrology_classical | Life domains |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_iv_020 | correspondence | astro_planet_age | life_stage | Planet=Age | When planetary spheres sequentially govern corresponding life stages | governing | Ptolemy IV.10 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_iv_020 | "Moon...first age of infancy" | planet_age | Moon=Infancy | Age-planet link | High | Yes | rule_planet_age |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_life_stage | Developmental period | 大运 | planet_age | age_dream | developmental_stages | Temporal |
<!-- L2.5_END -->
<!-- L2_END -->

---

## Progress Tracker - Book IV

| Section | Content | Entries | Status |
|---------|---------|---------|--------|
| Part 1: Fortune & Rank | Ch I-IV | 4/4 | ✅ COMPLETE |
| Part 2: Relationships | Ch V-VII | 3/3 | ✅ COMPLETE |
| Part 3: Events & Death | Ch VIII-X | 3/3 | ✅ COMPLETE |

**Book IV Total**: 10/10 core entries ✅ COMPLETE

---

## Final Summary - Tetrabiblos Complete

### Coverage by Book

| Book | Topic | Chapters | Entries | Coverage |
|------|-------|----------|---------|----------|
| Book I | Foundational Theory | 27 | 27 | 100% ✅ |
| Book II | Mundane Astrology | 14 | 14 | 100% ✅ |
| Book III | Natal Astrology | 19 | 19 | 100% ✅ |
| Book IV | Life Events | 10 | 10 | 100% ✅ |

**Grand Total**: 70 core L1 entries covering 70 chapters = **100% COMPLETE**

### Key Doctrines Preserved

1. **Epistemological foundation**: Astrology as natural philosophy
2. **Tropical zodiac defense**: Signs from equinoctial points
3. **Essential dignities**: Domicile, exaltation, triplicity, terms, face
4. **Mundane methodology**: Eclipse prediction, regional astrology
5. **Prorogation system**: Primary directions for lifespan
6. **Natal delineation**: Parents, siblings, body, mind, fortune, profession, marriage, children, death

---

**文件状态**: Book IV - ✅ 精校完成  
**当前日期**: 2025-11-29  
**模板**: Western Texts v2.1 Bilingual  
**作者**: Claudius Ptolemy (trans. J.M. Ashmand)
