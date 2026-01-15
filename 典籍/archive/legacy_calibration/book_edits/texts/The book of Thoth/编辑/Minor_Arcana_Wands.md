# The Book of Thoth - Minor Arcana: Suit of Wands (权杖)

> **Refinement Status**: Batch 1 (Ace to 7 of Wands)
> **Progress**: 7/14 cards in Suit of Wands
> **L1+L2 Version**: v2.1

---

## Ace of Wands (权杖一)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kether in Fire | Crown in Fire element | Primordial spark |
| Solar-phallic | Sun/masculine eruption | Creative force origin |
| Yod | Hebrew letter "Hand/Seed" | Divine fire seeds |
| Root of Fire | Fire signs foundation | Aries/Leo/Sagittarius |

**Title**: The Root of the Powers of Fire (火之力量的根源)
**Qabalistic**: Kether in Fire (火中之冠)
**Astrological**: Root of Fire signs (Aries, Leo, Sagittarius)

**Source Text**:
> "This card represents the essence of the element of Fire in its inception. It is a solar-phallic outburst of flame from which spring lightnings in every direction. These flames are Yods, arranged in the form of the Tree of Life. ... It is the primordial Energy of the Divine manifesting in Matter, at so early a stage that it is not yet definitely formulated as Will."

**English Paraphrase**:
**Primordial Fire Essence** - This card embodies the pure, initial spark of the Fire element. It is a potent **solar-phallic eruption**, sending lightning bolts (Yods/Seeds) outward in the pattern of the Tree of Life. It represents **Divine Energy** just beginning to manifest in the material world—raw, unshaped, and prior to the formation of specific Will. It is the blind force of creation.

**Core**: **Primordial Energy** - The initial spark, the raw urge to create, the essence of fire before it takes form.

**Chinese Explanation**:
**权杖一**代表火元素的**原始本质**。它是**太阳-阳具式**（solar-phallic）的火焰爆发，向四面八方射出闪电。这些火焰是**Yod**（希伯来字母"手"/种子），按生命之树的形状排列。它象征着**神圣能量**在物质中的初次显化，处于非常早期的阶段，尚未明确形成具体的"意志"。它是纯粹的动力和创造的盲目力量。

**In Readings**: Raw energy, new beginnings, creative impulse, initial spark, force without direction, masculine potential.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ace of Wands emphasizes Fire's primordial essence before Will forms. Solar-phallic imagery represents masculine creative principle. Yods arranged as Tree of Life show divine structure. Harris depicts explosive flame eruption.
- **中文**: Crowley的权杖一强调意志形成前火的原始本质。太阳-阳具意象代表男性创造原则。Yod按生命之树排列显示神圣结构。Harris描绘爆发性火焰喷发。

**Narrative Snippets**:
- `[ns_thoth_wands_001]` `[trigger: ace_wands_thoth]` `[factor_trigger: thoth_wands_ace]` `[role: 主干]` Ace of Wands = Fire in its inception—solar-phallic eruption; divine energy manifesting before Will forms. → Core
- `[ns_thoth_wands_002]` `[trigger: yods_tree_life]` `[factor_trigger: thoth_wands_ace AND symbol_yod]` `[role: 条件分支]` Flames are Yods arranged as Tree of Life—divine fire seeds springing outward in every direction. → Visual
- `[ns_thoth_wands_003]` `[trigger: primordial_force]` `[factor_trigger: thoth_wands_ace AND state_inception]` `[role: 条件分支]` Primordial Energy of Divine manifesting in Matter—so early not yet formulated as Will; blind force. → State

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Primordial Essence of Fire (Inception).
- **Natural Attributes**:
  - *Element*: Fire (Raw, explosive).
  - *Symbolism*: Solar-phallic flame, Yods (seeds), Tree of Life pattern.
  - *State*: Unformulated, early stage manifestation.
- **Functional Symbolism**:
  - *Creation*: The source of all fiery energy (Will, passion, spirit).
  - *Manifestation*: Divine energy entering matter (blind force).
- **Conditional Structure**:
  - *Prerequisite*: Needs direction (Will) to become effective; otherwise, it is just potential.
  - *Context*: The "Root" from which the other Wands cards derive.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Ace of Wands | 权杖一 | Card representing the primordial essence of Fire as the root of the Wands suit | 代表火元素原始本质、作为权杖花色根源的牌 |
| Solar-phallic Flame | 太阳-阳具之火焰 | Explosive solar creative fire that erupts as the first seed of all later fiery forms | 作为一切后续火之形态最初种子的爆发性太阳创造之火 |
| Yod | Yod（种子） | Smallest Hebrew letter, used here as seed-points of divine fire arranged in the Tree of Life pattern | 希伯来字母中最小的一字，在此代表按生命之树格局排列的神圣火种 |
| Tree of Life Pattern | 生命之树格局 | Qabalistic arrangement of the Yods that maps the structure of creation | 通过 Yod 的分布呈现创造结构的卡巴拉图式 |
| Primordial Energy | 原始能量 | Undifferentiated creative force of Fire before it crystallizes into specific Will or intention | 在凝聚为具体意志或目标之前的未分化火之创造力 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Element | Fire |  | new_candidate | Essence/Root | Inception/Outburst | Primordial |
| Symbol | Solar-phallic |  | new_candidate | Source | Generate | Creative |
| Component | Yods |  | new_candidate | Tree of Life form | Spring forth | Manifesting |
| Concept | Primordial Energy |  | new_candidate | Divine | Manifesting | Early stage |
| State | Not yet Will |  | new_candidate | Pre-formulation | Potential | Blind Force |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_ace_001 | causal | tarot_wands_ace AND tarot_fire_essence | tarot_primordial_force | Fire root births energy | When spiritual will is ignited | BENEFICIAL | Crowley #Wands |
| rel_wands_ace_002 | complementary | tarot_solar_phallic AND tarot_yods | tarot_creative_seed | Divine sparks manifest | When Tree of Life pattern activates | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_ace_001 | "This card represents the element of Fire in its inception" | tarot_wands_ace, tarot_fire_essence | HIGH | Crowley's direct statement of Ace meaning |
| evi_wands_ace_002 | "solar-phallic outburst of flame" | tarot_solar_phallic | HIGH | Key symbolic description |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_ace_001 | tarot | tarot_wands_ace | astro | astro_fire_signs | equivalent | Both represent primordial fire energy |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Two of Wands: Dominion (权杖二：统治)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chokmah in Fire | Wisdom in Fire | Exalted Will |
| Mars in Aries | Planet in home sign | Maximum initiative |
| Dorje | Tibetan thunderbolt | Destroy to create |
| Pure Will | Objectless intention | Thelemic ideal |

**Title**: Lord of Dominion (统治之主)
**Qabalistic**: Chokmah in Fire (火中之智慧)
**Astrological**: Mars in Aries (火星入白羊座)

**Source Text**:
> "This card, pertaining to Chokmah in the suit of Fire, represents the Will in its most exalted form. It is an ideal Will, independent of any given object. ... The background of this card shows the power of the planet Mars in his own sign Aries... initiating a Current of Force. The pictorial representation is two Dorjes crossed. The Dorje is the Tibetan symbol of the thunderbolt... Destruction may be regarded as the first step in the creative process."

**English Paraphrase**:
**Exalted Will** - Corresponding to Chokmah (Wisdom/Force) in Fire, this card symbolizes **Will in its highest, most ideal form**—pure purpose independent of a specific target. Ruled by **Mars in Aries** (its home sign), it represents energy initiating a current of force. The symbol is two crossed **Dorjes** (Tibetan thunderbolts), representing celestial power in its destructive/creative aspect. Destruction here is the necessary first step of creation ("The virgin ovum must be broken").

**Core**: **Pure Will** - Authority, boldness, and the energy to initiate. Will unassuaged of purpose.

**Chinese Explanation**:
**权杖二（统治）**对应火元素中的Chokmah（智慧），代表**最高形式的意志**。这是一种理想的意志，独立于任何具体对象。背景显示**火星在白羊座**（其本位星座）的力量，代表启动一股力量流。图像是两个交叉的**金刚杵**（Dorje，西藏雷电符号），象征天界力量，兼具破坏与创造性。在此，破坏被视为创造过程的第一步（如打破卵子以受精）。它代表纯粹的、无所畏惧的启动力量。

**In Readings**: Authority, boldness, taking initiative, exerting will, conquering, destruction as creation, fierce independence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Two of Wands shows "pure Will unassuaged of purpose" (Thelemic formula). Mars in Aries gives maximum aggressive initiative. Crossed Dorjes symbolize destruction as creation's first step. Chokmah provides ideal Will.
- **中文**: Crowley的权杖二展示"纯粹意志不受目的约束"（泰勒玛公式）。火星入白羊赋予最大攻击性主动。交叉金刚杵象征破坏作为创造的第一步。Chokmah提供理想意志。

**Narrative Snippets**:
- `[ns_thoth_wands_004]` `[trigger: two_wands_dominion]` `[factor_trigger: thoth_wands_two]` `[role: 主干]` Two of Wands = Lord of Dominion—Will in most exalted form; pure, ideal, independent of any object. → Core
- `[ns_thoth_wands_005]` `[trigger: crossed_dorjes]` `[factor_trigger: thoth_wands_two AND symbol_dorje]` `[role: 条件分支]` Two crossed Dorjes (Tibetan thunderbolts)—celestial power; destruction as first step of creation. → Visual
- `[ns_thoth_wands_006]` `[trigger: mars_aries_home]` `[factor_trigger: thoth_wands_two AND planet_mars_aries]` `[role: 条件分支]` Mars in Aries (home sign)—initiating current of force; maximum aggressive initiative. → Astrological

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Exalted Will and Dominion.
- **Natural Attributes**:
  - *Astrology*: Mars in Aries (Energy, aggression, initiative).
  - *Symbolism*: Crossed Dorjes (Thunderbolts), destructive/creative power.
- **Functional Symbolism**:
  - *Initiation*: Starting a current of force.
  - *Process*: Destruction as the prerequisite for creation (breaking the container).
- **Conditional Structure**:
  - *State*: "Pure will, unassuaged of purpose" (Thelemic ideal).
  - *Outcome*: Dominion, control, established power.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Two of Wands | 权杖二 | Card of Dominion expressing exalted Will in the suit of Fire | 表达崇高意志、主题为统治的权杖花色之牌 |
| Dominion | 统治 | Established authority and control that flow from pure, objectless Will | 源自纯粹且不依附具体对象之意志的确立权威与控制 |
| Mars in Aries | 火星入白羊 | Astrological configuration of aggressive initiating fire, ruling this card | 代表强力发动与攻击性的火象组合，是本牌的占星配置 |
| Dorje | 金刚杵 | Tibetan thunderbolt symbol of destructive/creative spiritual power | 西藏象征雷电的法器，代表兼具破坏与创造的精神力量 |
| Chokmah in Fire | 火中之智慧 | Placement of the sephirah Chokmah in the element of Fire, source of ideal Will | 生命之树上智慧之位在火元素中的对应，作为理想意志的源头 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Quality | Exalted Will |  | new_candidate | Ideal/Pure | Independent | Chokmah/Fire |
| Astro | Mars in Aries |  | new_candidate | Ruler/Home | Initiate Force | Energy |
| Symbol | Dorje |  | new_candidate | Tibetan symbol | Destroy/Create | Celestial |
| Process | Destruction as first step of creation |  | new_candidate | First step | Fertilize | Creative transformation of matter ("virgin ovum must be broken") |
| Concept | Dominion |  | new_candidate | Authority | Govern | Result of pure Will in Fire |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_two_001 | causal | tarot_wands_two AND tarot_dominion | tarot_exalted_will | Pure Will establishes authority | When Mars in Aries is activated | BENEFICIAL | Crowley #Wands |
| rel_wands_two_002 | causal | tarot_dorje AND tarot_destruction | tarot_creation_first_step | Destruction enables creation | When initiating new ventures | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_two_001 | "This card represents the Will in its most exalted form" | tarot_wands_two, tarot_exalted_will | HIGH | Crowley's direct definition |
| evi_wands_two_002 | "Destruction may be regarded as the first step in the creative process" | tarot_destruction, tarot_creation_first_step | HIGH | Key philosophical statement |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_two_001 | tarot | tarot_wands_two | astro | astro_mars_aries | equivalent | Both represent aggressive initiative |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Three of Wands: Virtue (权杖三：美德)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Binah in Fire | Understanding in Fire | Mother receives Will |
| Sun in Aries | Exalted Sun position | Spring vitality |
| Virtue | Power/efficacy (Latin vir) | Masculine force |
| Lotus Wands | Blossoming symbols | Harmonious growth |

**Title**: Lord of Virtue (美德之主)
**Qabalistic**: Binah in Fire (火中之理解)
**Astrological**: Sun in Aries (太阳入白羊座)

**Source Text**:
> "This card refers to Binah in the suit of Fire, and so represents the establishment of primeval Energy. The Will has been transmitted to the Mother, who conceives, prepares, and gives birth to, its manifestation. It refers to the Sun in Aries... The meaning is harmonious, for this is the beginning of Spring. ... The Sun has enkindled the Great Mother."

**English Paraphrase**:
**Established Energy** - Corresponds to Binah (Understanding/Mother) in Fire. The primeval energy/Will (from the Two) is now **transmitted to the Mother**, who gives it form and birth. Ruled by the **Sun in Aries** (exalted), it represents harmony and the **beginning of Spring**. The wands take the form of blossoming Lotuses. It is the "Virtue" (manhood/power) of the Sun enkindling the Great Mother, representing successful establishment and initial fruition.

**Core**: **Harmonious Success** - Energy finding form, integrity, beginning of manifestation, self-assertion with dignity.

**Chinese Explanation**:
**权杖三（美德）**对应火元素中的Binah（理解/母亲），代表原始能量的**确立**。意志已被传达给母亲，由她孕育、准备并赋予其显化。对应**太阳在白羊座**（旺相），象征和谐与**春天的开始**。权杖呈现为盛开的莲花形状。这是太阳点燃了伟大的母亲，代表能量成功转化为形式，具有"美德"（Virtue，源自拉丁语Vir，意为男性的力量/效能）。

**In Readings**: Established strength, success, integrity, new beginnings (Spring), harmony, fruition of will, confidence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Three of Wands represents Will transmitted to Mother (Binah) for manifestation. Sun in Aries (exalted) marks spring's beginning. "Virtue" derives from Latin vir (man/power), meaning efficacy not morality. Harris depicts blossoming lotus wands.
- **中文**: Crowley的权杖三代表意志传递给母亲（Binah）以实现显化。太阳入白羊（旺相）标志春天开始。"美德"源自拉丁语vir（男性/力量），意为效能而非道德。Harris描绘盛开的莲花权杖。

**Narrative Snippets**:
- `[ns_thoth_wands_007]` `[trigger: three_wands_virtue]` `[factor_trigger: thoth_wands_three]` `[role: 主干]` Three of Wands = Lord of Virtue—Will transmitted to Mother (Binah) who conceives and gives birth. → Core
- `[ns_thoth_wands_008]` `[trigger: sun_aries_exalted]` `[factor_trigger: thoth_wands_three AND planet_sun_aries]` `[role: 条件分支]` Sun in Aries (exalted)—beginning of Spring; Sun enkindling Great Mother; harmony. → Astrological
- `[ns_thoth_wands_009]` `[trigger: lotus_wands]` `[factor_trigger: thoth_wands_three AND symbol_lotus_wand]` `[role: 条件分支]` Blossoming lotus wands—established primeval energy finding harmonious form; Virtue as power/efficacy. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Establishment and Fruition of Energy.
- **Natural Attributes**:
  - *Astrology*: Sun in Aries (Exalted, spring, vitality).
  - *Symbolism*: Lotus wands (blossoming), Sun enkindling Mother.
- **Functional Symbolism**:
  - *Transmission*: Will (2) → Mother (3) → Manifestation.
  - *Harmony*: Orderly establishment, unlike the raw force of the Ace or 2.
- **Conditional Structure**:
  - *Meaning*: Virtue as "power/efficacy" rather than moral good.
  - *State*: Early success, promising beginning.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Three of Wands | 权杖三 | Card where primeval Fire energy becomes established and begins to bear fruit | 展示原始火之能量被确立并开始结果的权杖花色之牌 |
| Virtue | 美德（效能） | Here meaning power or efficacy of the Sun’s force rather than moral goodness | 此处指太阳之力的效能与力量，而非单纯道德上的善良 |
| Sun in Aries | 太阳入白羊 | Exalted Sun position marking spring’s beginning and vital, initiating fire | 代表春天开端与强劲发动之火的旺相太阳位置 |
| Binah in Fire | 火中之理解 | Placement of the Mother-sephirah Binah in Fire, receiving and shaping Will | 代表母性 Sephirah Binah 在火元素中的位置，承担接受并塑形意志的功能 |
| Lotus Wands | 莲花权杖 | Blossoming wand-forms showing harmonious, established fiery growth | 呈现和谐而已被确立的火之成长状态的莲花形权杖 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Process | Establishment |  | new_candidate | Primeval Energy | Manifest | Binah/Fire |
| Astro | Sun in Aries |  | new_candidate | Exalted | Enkindle | Spring |
| Symbol | Lotus wands |  | new_candidate | Blossom | Show Harmony | Form |
| Interaction | Transmitted to Mother |  | new_candidate | Will/Binah | Conceive/Birth | Manifestation |
| Concept | Virtue |  | new_candidate | Power/Efficacy | Succeed | Harmonious |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_three_001 | causal | tarot_wands_three AND tarot_virtue | tarot_established_energy | Will transmitted to form | When Sun in Aries is exalted | BENEFICIAL | Crowley #Wands |
| rel_wands_three_002 | complementary | tarot_binah_fire AND tarot_mother | tarot_manifestation | Mother receives and shapes Will | When creative process is orderly | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_three_001 | "The Will has been transmitted to the Mother, who conceives, prepares, and gives birth" | tarot_wands_three, tarot_virtue | HIGH | Core transmission concept |
| evi_wands_three_002 | "The Sun has enkindled the Great Mother" | tarot_binah_fire, tarot_mother | HIGH | Key symbolic statement |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_three_001 | tarot | tarot_wands_three | astro | astro_sun_aries | equivalent | Both represent spring vitality and establishment |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Four of Wands: Completion (权杖四：完成)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chesed in Fire | Mercy in Fire | Manifested power |
| Venus in Aries | Gentleness + fire | Tact in force |
| Circle boundary | Ring-pass-not | Completion limit |
| Order/Law | Solid system | Government structure |

**Title**: Lord of Completion (完成之主)
**Qabalistic**: Chesed in Fire (火中之仁慈)
**Astrological**: Venus in Aries (金星入白羊座)

**Source Text**:
> "This card refers to Chesed in the suit of Fire. Being below the Abyss, it is the Lord of all manifested active Power. The original Will... is now built up into a solid system: Order, Law, Government. It is also referred to Venus in Aries... One cannot establish one's work without tact and gentleness. ... The ends of the wands touch a circle, showing the completion and limitation of the original work."

**English Paraphrase**:
**Systematized Order** - Corresponds to Chesed (Mercy/Structure) in Fire. It represents **manifested active power** solidified into a system: **Order, Law, Government**. Ruled by **Venus in Aries**, indicating that establishing work requires tact and gentleness alongside force. The wands touch a circle, symbolizing **completion and limitation**. The work is finished and balanced ("four double flames"), but this limitation ("ring-pass-not") inherently contains the seeds of eventual disorder/decay.

**Core**: **Perfected Structure** - Success, settlement, order, completion of a phase, but with the restriction of finality.

**Chinese Explanation**:
**权杖四（完成）**对应火元素中的Chesed（仁慈/构建）。作为深渊之下的第一张牌，它是所有显化活动力量的主宰。原始意志被构建成一个稳固的系统：**秩序、法律、政府**。对应**金星在白羊座**，暗示建立工作需要机智与温柔。权杖末端接触一个圆环，显示原始工作的**完成与限制**。在圆环内火焰平衡，不再扩大范围。虽然代表完美，但这种限制本身也埋下了未来混乱的种子。

**In Readings**: Completion, settlement, successful conclusion, order, structure, marriage (Venus), stability, limitation.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Four of Wands shows Will systematized into Order/Law/Government. Venus in Aries adds tact to establishment. Circle boundary represents completion but also limitation (seeds of decay). First card "below the Abyss" in manifested realm.
- **中文**: Crowley的权杖四展示意志被系统化为秩序/法律/政府。金星入白羊为建立增添机智。圆环边界代表完成但也是限制（衰败的种子）。显化领域中"深渊之下"的第一张牌。

**Narrative Snippets**:
- `[ns_thoth_wands_010]` `[trigger: four_wands_completion]` `[factor_trigger: thoth_wands_four]` `[role: 主干]` Four of Wands = Lord of Completion—Will built into solid system: Order, Law, Government. → Core
- `[ns_thoth_wands_011]` `[trigger: venus_aries_tact]` `[factor_trigger: thoth_wands_four AND planet_venus_aries]` `[role: 条件分支]` Venus in Aries—establishing work requires tact and gentleness alongside force. → Astrological
- `[ns_thoth_wands_012]` `[trigger: circle_boundary]` `[factor_trigger: thoth_wands_four AND symbol_circle]` `[role: 条件分支]` Wands touch circle—completion and limitation; ring-pass-not; contains seeds of disorder. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Structural Completion and Order.
- **Natural Attributes**:
  - *Astrology*: Venus in Aries (Socializing fire, tact).
  - *Symbolism*: Circle (Limit/Completion), Ram (Aries), Doves (Venus).
- **Functional Symbolism**:
  - *Systematization*: Will becoming Law/Government.
  - *Limitation*: Defining the scope, stopping expansion.
- **Conditional Structure**:
  - *State*: "Below the Abyss" (Manifested).
  - *Risk*: Limitation implies eventual stagnation or disorder.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Four of Wands | 权杖四 | Card of Completion where fiery work is structured into stable order | 表示火之工作被构造成稳定秩序、主题为完成的权杖牌 |
| Completion | 完成 | State where an original work has reached structural perfection and limitation | 原初工作在结构上达到完满并因此受到限制的状态 |
| Venus in Aries | 金星入白羊 | Configuration blending tact and gentleness with initiating fire | 将机智温柔与主动火能量结合的占星配置 |
| Circle / Ring-Pass-Not | 圆环／不可逾越之环 | Limiting boundary that both protects and confines a finished system | 既保护又限制完工体系的边界象征 |
| Chesed in Fire | 火中之仁慈 | Sephirothic placement expressing Law, Order and government in the element of Fire | 在火元素中体现法律、秩序与统治结构的 Chesed 位置 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Completion |  | new_candidate | Circle/System | Limit/Finish | Chesed/Fire |
| System | Solid System |  | new_candidate | Order/Law | Govern | Manifested |
| Astro | Venus in Aries |  | new_candidate | Tact/Gentleness | Establish | Harmony |
| Symbol | Circle |  | new_candidate | Boundary | Enclose | Limitation |
| Implication | Seeds of disorder |  | new_candidate | Limitation | Decay | Future |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_four_001 | causal | tarot_wands_four AND tarot_completion | tarot_solid_system | Will becomes Order/Law | When Venus in Aries brings tact | BENEFICIAL | Crowley #Wands |
| rel_wands_four_002 | conditional | tarot_completion AND tarot_limitation | tarot_seeds_of_disorder | Completion contains decay | When system becomes too rigid | MIXED | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_four_001 | "The original Will is now built up into a solid system: Order, Law, Government" | tarot_wands_four, tarot_completion | HIGH | Direct statement of card meaning |
| evi_wands_four_002 | "The ends of the wands touch a circle, showing the completion and limitation" | tarot_completion, tarot_limitation | HIGH | Key visual symbolism explained |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_four_001 | tarot | tarot_wands_four | astro | astro_venus_aries | equivalent | Both represent structured establishment with grace |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Five of Wands: Strife (权杖五：冲突)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Geburah in Fire | Severity in Fire | Volcanic force |
| Saturn in Leo | Restriction + fire | Embittered energy |
| Adept Wands | Hierarchical symbols | Authority control |
| Volcanic Energy | Unlimited scope | Tameless force |

**Title**: Lord of Strife (冲突之主)
**Qabalistic**: Geburah in Fire (火中之严厉)
**Astrological**: Saturn in Leo (土星入狮子座)

**Source Text**:
> "This card is referred to Geburah of the suit of Fire. Geburah itself being fiery, it is a purely active force. It is ruled also by Saturn and Leo. ... Saturn tends to weigh it down and to embitter it. There is no limit to the scope of this volcanic energy. ... The symbol represents the wand of the Chief Adept... two wands of the Second... and two wands of the Third... This card would be thoroughly disastrous [without hierarchy]."

**English Paraphrase**:
**Volcanic Disturbance** - Corresponds to Geburah (Severity/Strength) in Fire, a purely active, potentially violent force. Ruled by **Saturn in Leo**: Saturn (restriction/weight) embitters the fiery nature of Leo, causing **volcanic energy** and strife. The symbol shows the wands of the Chief, Major, and Minor Adepts (Phoenix and Lotus wands), implying that this energy is **controlled by hierarchy**. Without this structure, the conflict would be disastrous. It represents struggle, tension, and the "tameless irrational energy" mitigated only by superior authority.

**Core**: **Restricted Energy** - Struggle, conflict, frustration, heavy energy (Saturn) trying to explode (Leo/Fire), necessary friction.

**Chinese Explanation**:
**权杖五（冲突）**对应火元素中的Geburah（严厉/力量）。由于Geburah本身属火，这是一种纯粹的主动力量。对应**土星在狮子座**：土星的沉重与限制使狮子座的火能量变得苦涩，导致**火山般的爆发力**。这代表没有限制的能量冲突。图像展示了最高、第二和第三级Adepts（大能者）的权杖（凤凰与莲花），暗示这种冲突通过**层级权威**来管理；若无此结构，将是灾难性的。它象征斗争、紧张以及被压抑的激烈能量。

**In Readings**: Conflict, struggle, hassle, frustration, volcanic energy, quarrel, competition, obstacles to be overcome.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Five of Wands shows Saturn embittering Leo's fire, creating volcanic strife. Geburah's severity adds fierce intensity. Adept wand hierarchy prevents total disaster. Energy is "tameless" but controlled by authority.
- **中文**: Crowley的权杖五展示土星使狮子之火变得苦涩，创造火山般冲突。Geburah的严厉增添猛烈强度。大能者权杖层级阻止全面灾难。能量"不可驯服"但受权威控制。

**Narrative Snippets**:
- `[ns_thoth_wands_013]` `[trigger: five_wands_strife]` `[factor_trigger: thoth_wands_five]` `[role: 主干]` Five of Wands = Lord of Strife—Geburah in Fire; purely active volcanic force; no limit to scope. → Core
- `[ns_thoth_wands_014]` `[trigger: saturn_leo_bitter]` `[factor_trigger: thoth_wands_five AND planet_saturn_leo]` `[role: 条件分支]` Saturn in Leo—weighs down and embitters fire; tameless irrational energy. → Astrological
- `[ns_thoth_wands_015]` `[trigger: adept_wands]` `[factor_trigger: thoth_wands_five AND symbol_adept_wands]` `[role: 条件分支]` Chief/Major/Minor Adept wands (Phoenix & Lotus)—hierarchy controls conflict; without it: disaster. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Volcanic Strife and Constrained Energy.
- **Natural Attributes**:
  - *Astrology*: Saturn in Leo (Heavy, embittered fire).
  - *Symbolism*: Chief/Major/Minor Adept wands (Hierarchy).
- **Functional Symbolism**:
  - *Conflict*: Purely active force meets restriction.
  - *Mitigation*: Authority/Hierarchy prevents total disaster.
- **Conditional Structure**:
  - *Nature*: "Tameless irrational energy".
  - *Dynamic*: Sexual cruelty/Nature (Pasht/Kali) aspect of Geburah.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Five of Wands | 权杖五 | Card of Strife showing volcanic, conflicted fire energy | 展示火山般冲突火能量、主题为冲突的权杖牌 |
| Strife | 冲突 | Violent clash of forces where pure active fire meets restriction | 纯粹主动作火与限制力量激烈碰撞的状态 |
| Saturn in Leo | 土星入狮子 | Heavy, embittering influence weighing down Leonine fire | 令狮子之火变得沉重苦涩的占星配置 |
| Adept Wands | 大能者权杖 | Wands of Chief, Major and Minor Adepts symbolizing hierarchical control | 代表分级权威控制力量流向的最高、中级与初级大能者权杖 |
| Geburah in Fire | 火中之严厉 | Placement of severity/strength Sephirah in Fire, producing fierce, potentially cruel force | 严厉与力量之 Sephirah 置于火元素中，产生猛烈甚至残酷的能量 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Strife |  | new_candidate | Volcanic energy | Erupt/Struggle | Geburah/Fire |
| Astro | Saturn in Leo |  | new_candidate | Heavy/bitter influence on Leonine fire | Weigh down | Restriction |
| Symbol | Adept wands |  | new_candidate | Hierarchical wands of Chief/Major/Minor Adepts | Control/Mitigate | Authority prevents total disaster |
| Dynamic | Active force |  | new_candidate | Pure fiery drive | Agitate | Untamed energy meeting limits |
| Analogy | Sexual cruelty / Nature |  | new_candidate | Pasht/Kali aspect | Devour/Create | Fierce natural force with cruel edge |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_five_001 | causal | tarot_wands_five AND tarot_strife | tarot_volcanic_energy | Geburah fire creates conflict | When Saturn in Leo restricts fire | HARMFUL | Crowley #Wands |
| rel_wands_five_002 | conditional | tarot_strife AND tarot_hierarchy | tarot_controlled_conflict | Authority mitigates disaster | When adept hierarchy is present | MIXED | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_five_001 | "Saturn tends to weigh it down and to embitter it" | tarot_wands_five, tarot_strife | HIGH | Direct statement of Saturn's influence |
| evi_wands_five_002 | "This card would be thoroughly disastrous [without hierarchy]" | tarot_strife, tarot_hierarchy | HIGH | Crowley's explicit warning |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_five_001 | tarot | tarot_wands_five | astro | astro_saturn_leo | equivalent | Both represent frustrated fiery energy |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Six of Wands: Victory (权杖六：胜利)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tiphareth in Fire | Beauty in Fire | Balanced success |
| Jupiter in Leo | Expansion + pride | Royal triumph |
| Phoenix Wands | Rebirth symbols | Transformation |
| Balanced Energy | Harmony achieved | Stable victory |

**Title**: Lord of Victory (胜利之主)
**Qabalistic**: Tiphareth in Fire (火中之美)
**Astrological**: Jupiter in Leo (木星入狮子座)

**Source Text**:
> "This card represents Tiphareth of the suit of Fire. This shows Energy in completely balanced manifestation. The Five has broken up the closed forces of the Four... and the result is the Son, and the Sun. The reference is also to Jupiter and Leo... benediction on the harmony and beauty of this arrangement. ... The flames themselves... burn steadily as in lamps."

**English Paraphrase**:
**Balanced Manifestation** - Corresponds to Tiphareth (Beauty/Balance) in Fire. Energy is **completely balanced**. The revolutionary strife of the Five has broken the stagnation of the Four, resulting in a marriage and the birth of the **Son/Sun**. Ruled by **Jupiter in Leo**, signifying a benediction of harmony and expansion. The wands are orderly, and the flames burn steadily like lamps (not explosive). It is the **stabilization of energy**, self-supporting like the Sun.

**Core**: **Triumph and Harmony** - Success after struggle, recognition, balanced leadership, self-confidence, steady burning energy.

**Chinese Explanation**:
**权杖六（胜利）**对应火元素中的Tiphareth（美/平衡）。这是能量的**完全平衡显化**。五号牌打破了四号牌的封闭力量，通过"革命热情"，两者结合诞生了**圣子/太阳**。对应**木星在狮子座**，象征对这种和谐与美丽的祝福。权杖排列有序，火焰像灯一样**稳定燃烧**（而非四散）。这代表能量的稳定化，像太阳一样自我支撑。

**In Readings**: Victory, success, pride, leadership, stability, achievement, confident energy, public recognition.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Six of Wands shows energy achieving complete balance after Five's strife. Jupiter in Leo brings royal benediction. Flames burn steadily like lamps, not explosive. Son/Sun born from Father-Mother union.
- **中文**: Crowley的权杖六展示能量在五的冲突后达到完全平衡。木星入狮子带来王者祝福。火焰像灯一样稳定燃烧而非爆发。子/太阳从父母结合中诞生。

**Narrative Snippets**:
- `[ns_thoth_wands_016]` `[trigger: six_wands_victory]` `[factor_trigger: thoth_wands_six]` `[role: 主干]` Six of Wands = Lord of Victory—Tiphareth in Fire; energy completely balanced after Five's strife. → Core
- `[ns_thoth_wands_017]` `[trigger: jupiter_leo_royal]` `[factor_trigger: thoth_wands_six AND planet_jupiter_leo]` `[role: 条件分支]` Jupiter in Leo—royal benediction on harmony; flames burn steadily like lamps. → Astrological
- `[ns_thoth_wands_018]` `[trigger: son_sun_synthesis]` `[factor_trigger: thoth_wands_six AND symbol_sun]` `[role: 条件分支]` Son and Sun born from Father-Mother union—self-supporting energy; stable triumph. → Symbolism

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Balanced Victory and Stabilization.
- **Natural Attributes**:
  - *Astrology*: Jupiter in Leo (Expansive, royal, benevolent fire).
  - *Symbolism*: Steady flames (Lamps), Nine flames (Yesod/Moon reflection).
- **Functional Symbolism**:
  - *Resolution*: Success following the strife of the Five.
  - *State*: Self-supporting, balanced, harmonious.
- **Conditional Structure**:
  - *Process*: 4 (Closed) → 5 (Breakup) → 6 (Synthesis/Victory).
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Six of Wands | 权杖六 | Card of Victory where fiery energy is harmonized and self-supporting | 展示火之能量被调和并自我支撑、主题为胜利的权杖牌 |
| Victory | 胜利 | Successful resolution of prior conflict resulting in balanced strength | 对先前冲突的成功化解并形成平衡力量的状态 |
| Jupiter in Leo | 木星入狮子 | Royal, generous fire that blesses and expands harmonious achievement | 为和谐成就带来祝福与扩展的王者之火配置 |
| Son and Sun | 子与日 | Symbolic marriage of Father and Mother producing the solar child of balanced fire | 父与母结合并诞生平衡之火圣子的象征性意象 |
| Tiphareth in Fire | 火中之美 | Sephirothic placement of Beauty in Fire, expressing central harmony and radiance | 表达火元素中心和谐与光辉的 Tiphareth 位置 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Victory |  | new_candidate | Balanced energy | Triumph | Tiphareth/Fire |
| Astro | Jupiter in Leo |  | new_candidate | Royal, benevolent fire | Bless | Harmony |
| Symbol | Steady flames |  | new_candidate | Lamp-like flames | Burn steadily | Image of stabilization after prior strife |
| Result | Son and Sun |  | new_candidate | Synthesis of Father and Mother | Manifest | Child/Sun born from union of 4 and 5 |
| State | Self-supporting |  | new_candidate | Solar state | Sustain | Independent, self-feeding fire |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_six_001 | causal | tarot_wands_six AND tarot_victory | tarot_balanced_energy | Tiphareth creates harmony | When Jupiter in Leo brings benediction | BENEFICIAL | Crowley #Wands |
| rel_wands_six_002 | complementary | tarot_son_sun AND tarot_synthesis | tarot_self_supporting | Father-Mother union produces child | When strife of Five is resolved | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_six_001 | "Energy in completely balanced manifestation" | tarot_wands_six, tarot_victory | HIGH | Direct statement of card meaning |
| evi_wands_six_002 | "The flames burn steadily as in lamps" | tarot_balanced_energy | HIGH | Key visual symbolism |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_six_001 | tarot | tarot_wands_six | astro | astro_jupiter_leo | equivalent | Both represent royal triumph and expansion |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Seven of Wands: Valour (权杖七：勇气)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Netzach in Fire | Victory in Fire | Departing balance |
| Mars in Leo | Aggression + pride | Brutal support |
| Soldiers' Battle | Individual combat | No central command |
| Crude Club | Improvised weapon | Last resort |

**Title**: Lord of Valour (勇气之主)
**Qabalistic**: Netzach in Fire (火中之胜利/情感)
**Astrological**: Mars in Leo (火星入狮子座)

**Source Text**:
> "This card derives from Netzach (Victory) in the suit of Fire. But the Seven is a weak, earthy, feminine number... departure from the balance... loss of confidence. Fortunately, the card is also attributed to Mars in Leo. ... The wavering fire summoned the brutal energy of Mars to its support. ... The army has been thrown into disorder; if victory is to be won, it will be by dint of individual valour-a 'soldiers' battle'."

**English Paraphrase**:
**Desperate Courage** - Corresponds to Netzach (Victory) in Fire, but the number Seven (earthy/feminine) implies a **departure from balance** and loss of confidence. Ruled by **Mars in Leo**: The wavering fire summons the **brutal energy of Mars** to survive. It depicts an army in disorder; victory is no longer strategic but depends on **individual valour** (a "soldiers' battle"). The main wand is a crude club, representing the last resort. It is the fight against overwhelming odds.

**Core**: **Individual Struggle** - Fighting against the odds, courage in desperation, last stand, chaotic energy requiring personal bravery.

**Chinese Explanation**:
**权杖七（勇气）**对应火元素中的Netzach（胜利/情感）。但数字7（土相/阴性）在生命之树上较低，暗示**偏离平衡**和失去信心。对应**火星在狮子座**：摇摆不定的火焰召唤火星的**残暴能量**来支撑自己。这像是一支陷入混乱的军队；如果要获胜，只能靠**个人的勇气**（"士兵的战役"）。前方是一根粗糙的大棒（权杖），是手头的最后武器。象征在绝境中的挣扎和背水一战。

**In Readings**: Courage against odds, struggle, fighting back, precarious position, individual effort needed, disorder.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Seven of Wands shows departure from Six's balance. Mars in Leo provides brutal energy to wavering fire. "Soldiers' battle" requires individual valour when command fails. Crude club is last-resort weapon.
- **中文**: Crowley的权杖七展示偏离六的平衡。火星入狮子为摇摆的火提供残暴能量。"士兵战役"在指挥失败时需要个人勇气。粗糙棍棒是最后武器。

**Narrative Snippets**:
- `[ns_thoth_wands_019]` `[trigger: seven_wands_valour]` `[factor_trigger: thoth_wands_seven]` `[role: 主干]` Seven of Wands = Lord of Valour—Netzach in Fire; departure from balance; loss of confidence. → Core
- `[ns_thoth_wands_020]` `[trigger: mars_leo_brutal]` `[factor_trigger: thoth_wands_seven AND planet_mars_leo]` `[role: 条件分支]` Mars in Leo—wavering fire summons brutal energy; "soldiers' battle" without command. → Astrological
- `[ns_thoth_wands_021]` `[trigger: crude_club]` `[factor_trigger: thoth_wands_seven AND symbol_club]` `[role: 条件分支]` Crude club as main weapon—last resort; army in disorder; individual valour required. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Individual Valour in Disorder.
- **Natural Attributes**:
  - *Astrology*: Mars in Leo (Aggressive defense, decaying solar strength).
  - *Symbolism*: Crude club (unsatisfactory weapon), disordered flames.
- **Functional Symbolism**:
  - *Degeneration*: Departure from the balance of the Six.
  - *Response*: Summoning brutal energy to counter weakness.
- **Conditional Structure**:
  - *Context*: "Soldiers' battle" (Strategic command lost).
  - *Requirement*: Personal bravery is the only hope.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Seven of Wands | 权杖七 | Card of Valour where chaotic conditions demand individual courage | 展示局势混乱却必须以个人勇气应对、主题为勇气的权杖牌 |
| Valour | 勇气 | Desperate personal bravery required when structure and confidence have broken down | 在结构与信心瓦解时仍被迫拿出绝境中勇气的品质 |
| Mars in Leo | 火星入狮子 | Brutal martian force summoned to support weakening solar fire | 被摇摆衰弱的太阳之火召唤来支撑的残暴火星力量 |
| Crude Club | 粗糙棍棒 | Last-resort weapon showing rough, improvised defense | 代表粗糙而临时的防御方式的最后武器 |
| Soldiers' Battle | 士兵的战役 | Conflict where victory depends on individual fighters rather than central command | 胜负取决于前线个体而非统帅指挥的战役类型 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Valour |  | new_candidate | Individual | Fight | Netzach/Fire |
| Astro | Mars in Leo |  | new_candidate | Brutal energy | Support | Decadence |
| Symbol | Crude Club |  | new_candidate | Weapon | Defend | Last resort |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_7_courage | desperation | valour | disorder | Individual response | When Seven of Wands courage arises from desperate disorder requiring bravery | Chaos→Bravery | Thoth Wands 7 |
| rel_wands_7_mars | energy | planet_mars_leo | wavering_fire | Brutal support | When Mars in Leo provides brutal force to support wavering fire survival | Force→Survival | Thoth Wands 7 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| wands_7_valour | Desperate courage | 劫财/比肩逆境 | Mars in Leo | 战斗/困境象征 | Fight-or-flight response | Last stand |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Eight of Wands: Swiftness (权杖八：迅速)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hod in Fire | Splendour in Fire | Subtilized energy |
| Mercury in Sagittarius | Communication + fire | Swift message |
| Electrical Rays | Light-speed force | Transformed wands |
| Rainbow Spectrum | Pure light | Mathematical physics |

**Title**: Lord of Swiftness (迅速之主)
**Qabalistic**: Hod in Fire (火中之光辉)
**Astrological**: Mercury in Sagittarius (水星入射手座)

**Source Text**:
> "The remaining three cards of the suit belong to Sagittarius... subtilizing of the Fiery energy. ... Mercury rules the card... message of the original Will. The card also refers to Hod, splendour, in the suit of Fire... speech, light, electricity. The pictorial representation... shows the Light-wands turned into electrical rays... energy of high velocity... master-key to modern mathematical physics."

**English Paraphrase**:
**High Velocity Energy** - Corresponds to Hod (Intellect/Splendour) in Fire, representing the **subtilization** of fiery energy into light and electricity. Ruled by **Mercury in Sagittarius**, it brings down the message of the original Will. The wands have transformed into **electrical rays**, vibrating with high velocity. Above shines a rainbow, symbolizing the spectrum of pure light. It represents speed, communication, and energy that has transcended mere flame to become **intelligible geometrical form** (mathematical physics).

**Core**: **Swift Communication** - Speed, electricity, light, rapid processing, intellectual fire, messages, lack of heat but high energy.

**Chinese Explanation**:
**权杖八（迅速）**对应火元素中的Hod（光辉/智力），代表火能量的**精微化**，转化为光和电。对应**水星在射手座**，传递原始意志的信息。权杖变成了**电射线**，以高速振动。上方闪耀着彩虹，象征纯光的光谱。它代表速度、交流以及超越了单纯火焰、变成**可理解的几何形式**（数学物理）的能量。这是没有热量但极具速度的高能状态。

**In Readings**: Swiftness, speed, rapid communication, electricity, sudden action, messages, travel, high-frequency energy.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Eight of Wands shows fire subtilized into electricity and light. Mercury in Sagittarius brings message of original Will. Wands become electrical rays. Rainbow represents modern mathematical physics.
- **中文**: Crowley的权杖八展示火被精微化为电和光。水星入射手带来原始意志的信息。权杖变成电射线。彩虹代表现代数学物理。

**Narrative Snippets**:
- `[ns_thoth_wands_022]` `[trigger: eight_wands_swiftness]` `[factor_trigger: thoth_wands_eight]` `[role: 主干]` Eight of Wands = Lord of Swiftness—Hod in Fire; fire subtilized into light and electricity. → Core
- `[ns_thoth_wands_023]` `[trigger: mercury_sagittarius]` `[factor_trigger: thoth_wands_eight AND planet_mercury_sagittarius]` `[role: 条件分支]` Mercury in Sagittarius—message of original Will; high-velocity energy transmission. → Astrological
- `[ns_thoth_wands_024]` `[trigger: electrical_rays]` `[factor_trigger: thoth_wands_eight AND symbol_electrical]` `[role: 条件分支]` Wands become electrical rays; rainbow spectrum above—mathematical physics; speed without heat. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: High Velocity and Subtilized Energy.
- **Natural Attributes**:
  - *Astrology*: Mercury in Sagittarius (Swift, communicative fire).
  - *Symbolism*: Electrical rays, Rainbow, Absence of flames.
- **Functional Symbolism**:
  - *Subtilization*: Fire becoming Light/Electricity.
  - *Transmission*: Mercury bringing the message of the Will.
- **Conditional Structure**:
  - *State*: "Intelligible geometrical form" (Structured energy).
  - *Quality*: Speed without mass/heat impediment.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Eight of Wands | 权杖八 | Card of Swiftness where fire is subtilized into light and electricity | 展示火被精微化为光与电、主题为迅速的权杖牌 |
| Swiftness | 迅速 | Extremely high-velocity movement of energy with little resistance | 在几乎无阻力条件下极高速流动的能量状态 |
| Mercury in Sagittarius | 水星入射手 | Astrological pattern of message-bearing, far‑reaching fiery intellect | 代表传递讯息与远射之火性心智的占星组合 |
| Electrical Rays | 电射线 | Wands transformed into rays of electricity, symbolizing subtilized fire | 被转化为电射线、象征被精微化之火能的权杖形象 |
| Rainbow Spectrum | 彩虹光谱 | Spread of pure light into many colours, key to modern physics symbolism | 纯光展开为多色光谱的形象，是现代物理象征的关键意象 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Swiftness |  | new_candidate | Electrical Rays | Move fast | Hod/Fire |
| Astro | Mercury in Sagittarius |  | new_candidate | Communicative fire | Transmit | Subtilized |
| Symbol | Rainbow |  | new_candidate | Spectrum | Bridge | Light |
| Analogy | Mathematical Physics |  | new_candidate | Geometrical formulation | Formulate | High velocity structured as intelligible form |
| State | Subtilized Energy |  | new_candidate | Ray‑like energy | Vibrate | No flame, high speed |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_eight_001 | causal | tarot_wands_eight AND tarot_swiftness | tarot_subtilized_energy | Hod transforms Fire into Light | When Mercury in Sagittarius brings message of Will | BENEFICIAL | Crowley #Wands |
| rel_wands_eight_002 | complementary | tarot_electrical_rays AND tarot_rainbow | tarot_high_velocity | Energy becomes intelligible form | When fire transcends crude flame | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_eight_001 | "The pictorial representation... shows the Light-wands turned into electrical rays" | tarot_wands_eight, tarot_swiftness | HIGH | Key transformation described |
| evi_wands_eight_002 | "energy of high velocity... master-key to modern mathematical physics" | tarot_high_velocity | HIGH | Nature of subtilized energy |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_eight_001 | tarot | tarot_wands_eight | astro | astro_mercury_sagittarius | equivalent | Both represent swift far-reaching communication |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Nine of Wands: Strength (权杖九：力量)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yesod in Fire | Foundation in Fire | Restored balance |
| Moon in Sagittarius | Double lunar | Change is Stability |
| Arrows | Directed force | Defensive aim |
| Fullest Development | Peak before descent | Maximum force |

**Title**: Lord of Strength (力量之主)
**Qabalistic**: Yesod in Fire (火中之基础)
**Astrological**: Moon in Sagittarius (月亮入射手座)

**Source Text**:
> "This card is referred to Yesod, the Foundation; this brings the Energy back into balance. ... The Nine represents always the fullest development of the Force... This card is also governed by the Moon in Sagittarius; so here is a double influence of the Moon on the Tree of Life. Hence the aphorism 'Change is Stability'. ... The Wands have now become arrows. ... The flames in the card are tenfold, implying that the Energy is directed downwards."

**English Paraphrase**:
**Stable Strength** - Corresponds to Yesod (Foundation) in Fire, bringing energy back into balance. It represents the **fullest development** of the force in relation to superiors. Ruled by the **Moon in Sagittarius**, creating a double Lunar influence (Yesod is Moon, plus Moon in sign). This leads to the paradox **"Change is Stability"**. The wands become **arrows** (directed force), with one master arrow connecting Sun and Moon. It signifies strength maintained through constant adjustment and defense.

**Core**: **Resilience and Defense** - Strength through stability, prepared defense, recovery of balance, successful maintenance of position.

**Chinese Explanation**:
**权杖九（力量）**对应火元素中的Yesod（基础），将能量带回平衡。代表力量在某种层面上达到了**最充分的发展**。对应**月亮在射手座**，加上Yesod本身的月亮属性，形成双重月亮影响，引出格言"**变化即稳定**"（Change is Stability）。权杖变成了**箭**（定向的力量），其中一支主箭连接日月。这象征通过不断的调整和防御来维持力量，是一种韧性与稳固。

**In Readings**: Strength, defense, resilience, holding one's ground, recovery, stability amidst change, preparedness.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Nine of Wands shows energy restored to balance through Yesod. Moon in Sagittarius creates "Change is Stability" paradox. Wands become arrows for directed defense. Fullest development before solidification.
- **中文**: Crowley的权杖九展示能量通过Yesod恢复平衡。月亮入射手创造"变化即稳定"悖论。权杖变成箭用于定向防御。固化前的最充分发展。

**Narrative Snippets**:
- `[ns_thoth_wands_025]` `[trigger: nine_wands_strength]` `[factor_trigger: thoth_wands_nine]` `[role: 主干]` Nine of Wands = Lord of Strength—Yesod in Fire; fullest development; energy back in balance. → Core
- `[ns_thoth_wands_026]` `[trigger: moon_sagittarius]` `[factor_trigger: thoth_wands_nine AND planet_moon_sagittarius]` `[role: 条件分支]` Moon in Sagittarius—double lunar; "Change is Stability" paradox; fluctuating directed force. → Astrological
- `[ns_thoth_wands_027]` `[trigger: arrows_defense]` `[factor_trigger: thoth_wands_nine AND symbol_arrows]` `[role: 条件分支]` Wands become arrows—directed force; master arrow linking Sun and Moon; defensive aim. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Strength through Stability and Change.
- **Natural Attributes**:
  - *Astrology*: Moon in Sagittarius (Fluctuating but directed fire).
  - *Symbolism*: Arrows (Direction), Ten flames (Directed downwards), Sun/Moon link.
- **Functional Symbolism**:
  - *Balance*: Yesod restoring equilibrium after the speed of the Eight.
  - *Paradox*: "Change is Stability" (Cyclic stability).
- **Conditional Structure**:
  - *State*: Fullest development before solidification.
  - *Role*: Defense and maintenance.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Nine of Wands | 权杖九 | Card of Strength showing resilient, defensive fire | 展示韧性防御之火、主题为力量的权杖牌 |
| Strength | 力量 | Stable, enduring force maintained through continual small adjustments | 通过持续微调而保持的稳定持久之力 |
| Moon in Sagittarius | 月亮入射手 | Double-lunar influence directing mutable fire toward a goal | 双重月亮影响下被导向目标的变动火能量配置 |
| Arrows | 箭矢 | Wands turned into focused missiles indicating directed, purposeful energy | 被转化为聚焦射出的飞矢，象征被定向的目的性能量 |
| Change is Stability | 变化即稳定 | Aphorism expressing cyclical change as the basis of lasting strength | 表达以周期性变化作为持续稳定基础的格言 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Strength |  | new_candidate | Foundation | Balance | Yesod/Fire |
| Astro | Moon in Sagittarius |  | new_candidate | Double Moon | Stabilize | Change |
| Symbol | Arrows |  | new_candidate | Directed | Aim | Defense |
| Maxim | Change is Stability |  | new_candidate | Cycle | Maintain | Paradox |
| Direction | Directed Downwards |  | new_candidate | Tenfold flames | Ground | Manifesting |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_nine_001 | causal | tarot_wands_nine AND tarot_strength | tarot_resilient_defense | Yesod restores balance | When Moon in Sagittarius creates Change is Stability | BENEFICIAL | Crowley #Wands |
| rel_wands_nine_002 | complementary | tarot_arrows AND tarot_directed_flames | tarot_fullest_development | Force reaches peak | When energy is directed before solidification | BENEFICIAL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_nine_001 | "The Nine represents always the fullest development of the Force" | tarot_wands_nine, tarot_strength | HIGH | Peak development stated |
| evi_wands_nine_002 | "Hence the aphorism 'Change is Stability'" | tarot_change_stability | HIGH | Key paradox explained |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_nine_001 | tarot | tarot_wands_nine | astro | astro_moon_sagittarius | equivalent | Both represent fluctuating but directed force |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Ten of Wands: Oppression (权杖十：压迫)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Malkuth in Fire | Kingdom in Fire | Detached force |
| Saturn in Sagittarius | Heavy + swift clash | Greatest antipathy |
| Blind Force | Spiritless will | Self-devouring |
| Prison Bars | Crossed wands | Oppression symbol |

**Title**: Lord of Oppression (压迫之主)
**Qabalistic**: Malkuth in Fire (火中之王国)
**Astrological**: Saturn in Sagittarius (土星入射手座)

**Source Text**:
> "The number Ten refers to Malkuth... detached from its spiritual sources. It is become a blind Force; so, the most violent form of that particular energy... The card also refers to the influence of Saturn in Sagittarius. Here is the greatest antipathy. ... The whole picture suggests Oppression and repression. It is a stupid and obstinate cruelty from which there is no escape. It is a Will which has not understood anything beyond its dull purpose..."

**English Paraphrase**:
**Overwhelming Burden** - Corresponds to Malkuth (Kingdom/Earth) in Fire. Here, the force is **detached from spiritual sources** and becomes a blind, violent energy. Ruled by **Saturn in Sagittarius**, creating the greatest antipathy (heavy/slow Saturn vs swift/light Sagittarius). The wands are crossed bars, looking like claws/prison bars. It represents **Oppression**, repression, and stupid, obstinate cruelty. It is Will that has become a burden to itself, "lust of result" leading to self-devouring.

**Core**: **Crushing Weight** - Force detached from source, burden, cruelty, overextension, will turning against itself, failure through success.

**Chinese Explanation**:
**权杖十（压迫）**对应火元素中的Malkuth（王国/物质）。在此，力量**与灵性源头脱节**，变成盲目、暴力的能量。对应**土星在射手座**，形成巨大的反差（土星的重/慢 vs 射手座的轻/快）。权杖变成了交叉的栅栏或爪子。这代表**压迫**、压抑以及愚蠢顽固的残酷。这是未能理解其目的之外任何事物的意志，因"对结果的贪欲"（lust of result）而自我吞噬。

**In Readings**: Oppression, heavy burden, overextension, cruelty, blocked energy, working too hard without spirit, blind force.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ten of Wands shows force completely detached from spiritual source. Saturn in Sagittarius creates greatest antipathy. Wands become prison bars/claws. "Lust of result" causes self-devouring. Malkuth in Fire is blind, violent energy.
- **中文**: Crowley的权杖十展示力量完全与灵性源头脱节。土星入射手创造最大对立。权杖变成监狱栏杆/爪子。"对结果的贪欲"导致自我吞噬。火中之Malkuth是盲目暴力能量。

**Narrative Snippets**:
- `[ns_thoth_wands_028]` `[trigger: ten_wands_oppression]` `[factor_trigger: thoth_wands_ten]` `[role: 主干]` Ten of Wands = Lord of Oppression—Malkuth in Fire; force detached from spiritual sources; blind. → Core
- `[ns_thoth_wands_029]` `[trigger: saturn_sagittarius]` `[factor_trigger: thoth_wands_ten AND planet_saturn_sagittarius]` `[role: 条件分支]` Saturn in Sagittarius—greatest antipathy; heavy restriction on swift fire; stupid cruelty. → Astrological
- `[ns_thoth_wands_030]` `[trigger: bars_claws]` `[factor_trigger: thoth_wands_ten AND symbol_bars]` `[role: 条件分支]` Wands as bars/claws—prison symbol; "lust of result" causes self-devouring; obstinate will. → Visual

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Blind Force and Oppression.
- **Natural Attributes**:
  - *Astrology*: Saturn in Sagittarius (Heavy restriction on swift fire).
  - *Symbolism*: Bars/Claws (Prison), Wild flames (Destructive).
- **Functional Symbolism**:
  - *Detachment*: Force separated from spiritual source (Malkuth).
  - *Antipathy*: Conflict between nature of planet and sign.
- **Conditional Structure**:
  - *Outcome*: Self-devouring ("lust of result").
  - *Quality*: Stupid, obstinate, cruel.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Ten of Wands | 权杖十 | Card of Oppression where fire becomes blind, crushing force | 展示火之能量沦为盲目压迫性力量、主题为压迫的权杖牌 |
| Oppression | 压迫 | Situation where force detached from spirit weighs down and imprisons | 与灵性源头脱节的力量变成沉重枷锁、压制与囚禁一切的状态 |
| Saturn in Sagittarius | 土星入射手 | Clash of heavy Saturn with swift Sagittarius producing maximal antipathy | 沉重土星与轻快射手强烈对冲、制造最大不和谐的占星配置 |
| Bars / Claws | 栅栏／爪子 | Image of crossed wands like prison bars or claws, symbolizing confinement | 交叉权杖如牢笼与爪牙的图像，象征被困与撕扯 |
| Lust of Result | 对结果的贪欲 | Obsessive clinging to outcome that turns Will into self-devouring burden | 对结果的执迷使意志变成自我吞噬的重负的心态 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Concept | Oppression |  | new_candidate | Blind Force | Crush | Malkuth/Fire |
| Astro | Saturn in Sagittarius |  | new_candidate | Antipathy | Restrict | Detached |
| Symbol | Bars/Claws |  | new_candidate | Prison | Confine | Cruelty |
| Cause | Detached from Source |  | new_candidate | Isolation | Devour self | Spiritual loss |
| Flaw | Lust of Result |  | new_candidate | Obsession | Blind | Stupid |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_ten_001 | causal | tarot_wands_ten AND tarot_oppression | tarot_blind_force | Malkuth detaches from spirit | When Saturn in Sagittarius creates maximum antipathy | HARMFUL | Crowley #Wands |
| rel_wands_ten_002 | complementary | tarot_bars_claws AND tarot_lust_result | tarot_self_devouring | Will becomes burden | When force loses spiritual source | HARMFUL | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_ten_001 | "detached from its spiritual sources. It is become a blind Force" | tarot_wands_ten, tarot_oppression | HIGH | Core degeneration described |
| evi_wands_ten_002 | "a Will which has not understood anything beyond its dull purpose" | tarot_lust_result | HIGH | Warning about obsessive will |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_ten_001 | tarot | tarot_wands_ten | astro | astro_saturn_sagittarius | equivalent | Both represent heavy restriction on swift energy |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Knight of Wands (权杖骑士)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire of Fire | Purest fire expression | Double intensity |
| Black Horse | Wild mount | Uncontrollable motion |
| Flaming Torch | Fire weapon | Lightning attack |
| Impetuosity | Rash action | No modification |

**Title**: The Prince of the Chariot of Fire (火之战车的王子)
**Elemental**: The Fiery part of Fire (火中之火)
**Zodiac**: 21° Scorpio to 20° Sagittarius

**Source Text**:
> "The Knight of Wands represents the fiery part of Fire... He is a warrior in complete armour. On his helmet for a crest he wears a black horse. In his hand he bears a flaming torch... The moral qualities... are activity, generosity, fierceness, impetuosity, pride, impulsiveness, swiftness... If wrongly energized, he is evil-minded, cruel, bigoted and brutal."

**English Paraphrase**:
**Fiery Impulse** - Represents the **Fiery part of Fire** (purest elemental expression). Rules from late Scorpio to Sagittarius. He is a warrior in armor with a black horse crest, riding a leaping black horse and carrying a flaming torch. Qualities: **Activity, fierceness, impetuosity, pride, swiftness**. He is the lightning flash. If ill-dignified, he becomes cruel, bigoted, and brutal—acting without modification or reflection.

**Core**: **Swift Action** - Impulsive energy, lightning speed, aggression, leadership, lack of endurance if blocked.

**Chinese Explanation**:
**权杖骑士**代表**火中之火**（元素的纯粹表达）。掌管天蝎座21度到射手座20度。他是全副武装的战士，头盔上有黑马饰章，骑着跳跃的黑马，手持火炬。道德品质：**活跃、猛烈、急躁、骄傲、冲动、迅速**。他是闪电。如果能量错误，他会变得邪恶、残酷、偏执和残暴——行动缺乏修正或反思。

**In Readings**: Swift action, impulsiveness, departure, aggression, creative flash, volatility, bold leadership.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Knight of Wands represents Fire of Fire (purest element). Black horse symbolizes wild, leaping motion. Flaming torch is weapon of lightning-like initiation. If wrongly energized: cruel, bigoted, brutal.
- **中文**: Crowley的权杖骑士代表火中之火（最纯元素）。黑马象征狂野跳跃运动。火炬是闪电般发动的武器。如果能量错误：残酷、偏执、野蛮。

**Narrative Snippets**:
- `[ns_thoth_wands_031]` `[trigger: knight_wands_thoth]` `[factor_trigger: thoth_wands_knight]` `[role: 主干]` Knight of Wands = Fire of Fire—fiery part of Fire; activity, fierceness, impetuosity, swiftness. → Core
- `[ns_thoth_wands_032]` `[trigger: black_horse_torch]` `[factor_trigger: thoth_wands_knight AND symbol_black_horse]` `[role: 条件分支]` Black horse crest, leaping mount; flaming torch weapon—lightning attack; no modification. → Visual
- `[ns_thoth_wands_033]` `[trigger: wrongly_energized]` `[factor_trigger: thoth_wands_knight AND state_ill_dignified]` `[role: 条件分支]` If wrongly energized: evil-minded, cruel, bigoted, brutal—fire without guidance. → Shadow

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Pure Fiery Impulse.
- **Natural Attributes**:
  - *Element*: Fire of Fire (Double Fire).
  - *Zodiac*: Scorpio/Sagittarius transition.
  - *Symbolism*: Black Horse, Torch, Lightning.
- **Functional Symbolism**:
  - *Action*: Swift, unpredictable onset.
  - *Nature*: Generosity mixed with fierceness.
- **Conditional Structure**:
  - *Weakness*: No means of modifying action; if he fails first, he has no resource.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Knight of Wands | 权杖骑士 | Court card expressing the Fiery part of Fire as impulsive attack | 表达火中之火、以冲动突击呈现的宫廷牌 |
| Fire of Fire | 火中之火 | Purest, most concentrated expression of the Fire element | 火元素最纯粹、最集中的表现形式 |
| Black Horse | 黑马 | Mount of the Knight symbolizing wild, leaping, uncontrollable motion | 代表狂跃而难以驾驭的运动之力的坐骑形象 |
| Flaming Torch | 火炬 | Weapon and emblem of lightning-like, initiating fire | 既是武器又是象征闪电般发动之火的火炬 |
| Fiery Impulse | 火焰式冲动 | Sudden burst of energy that acts before reflection or planning | 在尚未来得及反思或计划前就爆发的能量冲动 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Element | Fire of Fire |  | new_candidate | Pure element | Surge | Knight (fiery part of Fire) |
| Symbol | Black Horse |  | new_candidate | Leaping mount | Move swift | Image of wild, uncontrollable motion |
| Quality | Impetuosity |  | new_candidate | Character trait | Act suddenly | Moral tendency to rush before reflection |
| Astro | Scorpio/Sagittarius |  | new_candidate | Zodiac sector | Transition | Rules this Knight’s decan range |
| Shadow | Bigoted/Brutal |  | new_candidate | Ill‑dignified expression | Destroy | Wrong energy when fire is misdirected |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_knight_001 | causal | tarot_wands_knight AND tarot_fire_of_fire | tarot_fiery_impulse | Double Fire creates pure intensity | When swift action is needed | BENEFICIAL | Crowley #Wands |
| rel_wands_knight_002 | conditional | tarot_black_horse AND tarot_torch | tarot_lightning_attack | Impetuous charge | When ill-dignified becomes cruel and bigoted | MIXED | Crowley #Wands |

**Evidence Chain Layer**:

| Evidence ID | l1_anchor | involved_factors | confidence | reasoning_path |
|-------------|-----------|------------------|------------|----------------|
| evi_wands_knight_001 | "The moral qualities... are activity, generosity, fierceness, impetuosity, pride, impulsiveness, swiftness" | tarot_wands_knight, tarot_fire_of_fire | HIGH | Core character traits listed |
| evi_wands_knight_002 | "If wrongly energized, he is evil-minded, cruel, bigoted and brutal" | tarot_fiery_impulse | HIGH | Shadow aspect described |

**Cross-System Concept Mapping Layer**:

| mapping_id | source_system | source_factor | target_system | target_factor | mapping_type | notes |
|------------|---------------|---------------|---------------|---------------|--------------|-------|
| map_wands_knight_001 | tarot | tarot_wands_knight | astro | astro_sagittarius | analogous | Both represent swift, expansive fire energy |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Queen of Wands (权杖皇后)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Water of Fire | Fluid fire aspect | Adaptability |
| Leopard | Wild attendant | Grace + savagery |
| Pinecone Wand | Bacchic symbol | Ecstasy mysteries |
| Calm Authority | Radiant command | Magnetic presence |

**Title**: The Queen of the Thrones of Flame (火焰宝座的皇后)
**Elemental**: The Watery part of Fire (火中之水)
**Zodiac**: 21° Pisces to 20° Aries

**Source Text**:
> "The Queen of Wands represents the watery part of Fire, its fluidity and colour. ... Her crown is topped with the winged globe and rayed with flame. ... She bears a wand... topped with a cone suggestive of the mysteries of Bacchus. She is attended by a couchant leopard... Adaptability, persistent energy, calm authority... She is kindly and generous, but impatient of opposition."

**English Paraphrase**:
**Magnetic Authority** - Represents the **Watery part of Fire** (fluidity, color, reflection). Rules from late Pisces to Aries. She sits on a throne of flame, bearing a wand with a Bacchic cone (pinecone) and attended by a leopard. Qualities: **Adaptability, persistent energy, calm authority**, attractiveness. She has immense capacity for friendship and love but on her own terms. If ill-dignified: snobbery, vanity, brooding, and sudden savagery ("breaks her jaw" when she misses a bite).

**Core**: **Radiant Confidence** - Attraction, adaptability, social power, command through presence, steady fire.

**Chinese Explanation**:
**权杖皇后**代表**火中之水**（火的流动性和色彩）。掌管双鱼座21度到白羊座20度。她坐在火焰宝座上，手持顶端有松果（巴克斯奥秘）的权杖，身旁有一只卧着的豹子。品质：**适应性、持久的能量、冷静的权威**、吸引力。她有巨大的友谊和爱的能力，但必须由她主动。如果能量不佳：势利、虚荣、阴郁，以及突然的野蛮（"咬空时会咬碎自己的下巴"）。

**In Readings**: Independence, charm, adaptability, social success, authoritative woman, generosity, vanity.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Queen of Wands represents Water of Fire (fluidity, color). Leopard symbolizes wild grace and latent savagery. Pinecone wand hints at Bacchic ecstasy. Kindly but impatient of opposition.
- **中文**: Crowley的权杖皇后代表火中之水（流动性、色彩）。豹子象征野性优雅和潜伏野蛮。松果权杖暗示酒神式狂喜。亲切但对对立不耐烦。

**Narrative Snippets**:
- `[ns_thoth_wands_034]` `[trigger: queen_wands_thoth]` `[factor_trigger: thoth_wands_queen]` `[role: 主干]` Queen of Wands = Water of Fire—fluidity and color; adaptability, persistent energy, calm authority. → Core
- `[ns_thoth_wands_035]` `[trigger: leopard_pinecone]` `[factor_trigger: thoth_wands_queen AND symbol_leopard]` `[role: 条件分支]` Couchant leopard attendant; pinecone (Bacchic) wand—wild grace with latent savagery. → Visual
- `[ns_thoth_wands_036]` `[trigger: impatient_opposition]` `[factor_trigger: thoth_wands_queen AND state_character]` `[role: 条件分支]` Kindly and generous, but impatient of opposition—breaks her jaw when she misses a bite. → Character

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Fluid and Persistent Fire.
- **Natural Attributes**:
  - *Element*: Water of Fire (Reflected/Colored Fire).
  - *Zodiac*: Pisces/Aries transition.
  - *Symbolism*: Leopard, Pinecone Wand, Winged Globe.
- **Functional Symbolism**:
  - *Adaptability*: Fire that can flow and persist.
  - *Authority*: Calm command, magnetic attraction.
- **Conditional Structure**:
  - *Nature*: Kindly but impatient of opposition.
  - *Shadow*: Brooding leading to savagery.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Queen of Wands | 权杖皇后 | Court card of the Watery part of Fire, expressing radiant confidence | 表达火中之水与外放自信的宫廷牌——权杖皇后 |
| Water of Fire | 火中之水 | Aspect of Fire emphasizing fluidity, reflection and adaptability | 强调流动、映照与适应性的火之相位 |
| Leopard | 豹 | Animal attendant symbolizing wild grace, magnetism and latent savagery | 代表野性优雅、吸引力与潜伏野蛮性的随从动物 |
| Pinecone Wand | 松果权杖 | Bacchic wand whose cone hints at mysteries of ecstasy and fertility | 顶端松果暗示狂喜与生育秘义的酒神式权杖 |
| Radiant Confidence | 光辉自信 | Core quality of steady, attractive authority expressed by this Queen | 此皇后所体现的稳定而具吸引力的权威核心品质 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Element | Water of Fire |  | new_candidate | Fluidity | Adapt | Queen as watery part of Fire |
| Symbol | Leopard |  | new_candidate | Couchant attendant | Attend | Wild grace and latent savagery |
| Quality | Adaptability |  | new_candidate | Character | Persist | Moral capacity to adjust while holding authority |
| Object | Pinecone Wand |  | new_candidate | Bacchic wand | Rule | Hints at ecstasy and fertility mysteries |
| Shadow | Snobbery/Savagery |  | new_candidate | Ill‑dignified reaction | React | Wrong energy when opposition is met badly |


<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_thoth_wands_queen | card_element | thoth_wands_queen | suit_element | Elemental | When Queen of Wands expresses Water of Fire (adaptable passion, magnetic charm) | expressing | Crowley #Thoth |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_thoth_wands_queen | "Book of Thoth" | thoth_wands_queen | Card -> meaning | Card interpretation | High | Yes | rule_thoth_wands_queen |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_thoth_wands_queen | Minor Arcana card | | decan_zodiac | card_dream | archetype | Thoth system |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Prince of Wands (权杖王子)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Air of Fire | Expanding fire | Volatilization |
| Lion Chariot | Noble vehicle | Powerful charge |
| To Mega Therion | Great Beast sigil | Crowleyan current |
| Dramatic Energy | Expressive force | Romantic action |

**Title**: The Prince of the Chariot of Fire (火之战车的王子)
**Elemental**: The Airy part of Fire (火中之气)
**Zodiac**: 21° Cancer to 20° Leo

**Source Text**:
> "The Prince of Wands represents the airy part of Fire, with its faculty of expanding and volatilising. ... He is a warrior... his arms are bare... He wears a rayed crown surmounted by a lion's head winged... On his breast is the sigil of To Mega Therion. ... Swiftness and strength. ... He states a vigorous proposition for the sake of stating it. ... essentially just, but always feels that justice is not to be attained in the intellectual world."

**English Paraphrase**:
**Expansive Energy** - Represents the **Airy part of Fire** (expansion, volatilization). Rules from late Cancer to Leo. He rides a chariot drawn by a lion, wearing the sigil of **To Mega Therion** (The Great Beast). Qualities: **Swiftness, strength, intensity**. He is noble and generous but prone to boasting and elaborate pranks. He fights against odds and wins through endurance. He is "Air" (Intellect) applied to Fire, making him romantic, dramatic, and sometimes a "symbol of Terror" due to mystery.

**Core**: **Dynamic Expression** - Expansion, drama, assertion, creativity, endurance, unpredictability, noble but volatile.

**Chinese Explanation**:
**权杖王子**代表**火中之气**（火的扩展和挥发能力）。掌管巨蟹座21度到狮子座20度。他驾驶狮子战车，胸前佩戴**To Mega Therion**（大兽）的印记。品质：**迅速、力量、强度**。他高尚大方，但倾向于吹牛和恶作剧。他对抗逆境并通过耐力获胜。他是应用于火的"气"（智力），使他浪漫、戏剧化，有时因神秘感而成为"恐怖的象征"。

**In Readings**: Impulsive action, dramatic expression, swiftness, travel, creativity, unpredictability, intense loyalty/leadership.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Prince of Wands represents Air of Fire (expansion, volatilization). Lion chariot symbolizes noble forward charge. To Mega Therion sigil links to Crowleyan magic. Generous but prone to boasting.
- **中文**: Crowley的权杖王子代表火中之气（扩张、挥发）。狮子战车象征高贵向前冲锋。To Mega Therion印记连接Crowley魔法。慰慨但容易吹牛。

**Narrative Snippets**:
- `[ns_thoth_wands_037]` `[trigger: prince_wands_thoth]` `[factor_trigger: thoth_wands_prince]` `[role: 主干]` Prince of Wands = Air of Fire—expanding and volatilizing; swiftness, strength, dramatic energy. → Core
- `[ns_thoth_wands_038]` `[trigger: lion_chariot_mega]` `[factor_trigger: thoth_wands_prince AND symbol_lion_chariot]` `[role: 条件分支]` Lion-drawn chariot; To Mega Therion sigil on breast—noble forward charge; Crowleyan current. → Visual
- `[ns_thoth_wands_039]` `[trigger: romantic_endurance]` `[factor_trigger: thoth_wands_prince AND state_character]` `[role: 条件分支]` Romantic and generous but prone to boasting; fights against odds, wins through endurance. → Character

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Expansive and Volatile Fire.
- **Natural Attributes**:
  - *Element*: Air of Fire (Expanding Fire).
  - *Zodiac*: Cancer/Leo transition.
  - *Symbolism*: Lion Chariot, To Mega Therion Sigil.
- **Functional Symbolism**:
  - *Expression*: Vigorous statement, drama, expansion.
  - *Nature*: Romantic, generous, endurance.
- **Conditional Structure**:
  - *Mindset*: Essentially just but skeptical of intellectual justice.
  - *Risk*: Indecision in trifles, practical joking.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Prince of Wands | 权杖王子 | Court card of the Airy part of Fire, expressing expansive dramatic energy | 表达火中之气、张扬戏剧性能量的宫廷牌——权杖王子 |
| Air of Fire | 火中之气 | Aspect of Fire that expands, volatilizes and carries ideas | 代表扩张、挥发并承载理念的火之相位 |
| Lion Chariot | 狮子战车 | Vehicle drawn by lion, symbolizing noble, powerful forward charge | 由狮子拉动、象征高贵且强力冲锋的战车形象 |
| To Mega Therion Sigil | To Mega Therion 印记 | Mark of “The Great Beast”, linking the Prince to Crowleyan magical current | “大兽”之印记，将王子与 Crowley 魔法流派相连 |
| Expansive Energy | 扩张能量 | Dynamic, outward-rushing fire that seeks expression and adventure | 追求表现与冒险、向外奔涌的动态火能量 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Element | Air of Fire |  | new_candidate | Volatility | Expand | Prince as airy part of Fire |
| Symbol | Lion Chariot |  | new_candidate | Vehicle | Move | Powerfully forward under Leo energy |
| Sign | To Mega Therion |  | new_candidate | Sigil | Identify | Links Prince to Crowleyan current |
| Quality | Swiftness/Strength |  | new_candidate | Moral quality | Endure | Character of vigorous, dramatic action |
| Shadow | Empty boaster |  | new_candidate | Ill‑dignified pattern | Prank | Wrong energy of mere show without substance |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_prince_wands_air | elemental | air_of_fire | expansion | Volatilization | When Prince of Wands expresses Air of Fire (intellectual will, expansive action) | Intellect→Action | Thoth Prince Wands |
| rel_prince_wands_drama | expression | dramatic_energy | statement | Vigorous assertion | When Prince of Wands channels dramatic energy into vigorous noble assertion | Will→Impact | Thoth Prince Wands |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| prince_wands_expansion | Dynamic expression | 食伤生财/表达 | Cancer-Leo transition | 冲锋/表演象征 | Extraversion/Drama | Air of Fire |
<!-- L2.5_END -->

<!-- L2_END -->

---

## Princess of Wands (权杖公主)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Earth of Fire | Fire's fuel | Combustion source |
| Chemical Attraction | Irresistible bond | Fire's material |
| Nude Figure | Freedom to combine | Pure reactivity |
| Daring Passion | Vigorous beauty | Creative force |

**Title**: The Princess of the Shining Flame (闪耀火焰的公主)
**Elemental**: The Earthy part of Fire (火中之土)
**Rule**: Quadrant around North Pole (北极周围象限)

**Source Text**:
> "The Princess of Wands represents the earthy part of Fire; one might say, she is the fuel of Fire. ... irresistible chemical attraction of the combustible substance. ... She is unclothed... chemical action can only take place when the element is perfectly free... She is brilliant and daring. She creates her own beauty by her essential vigour... In anger or love she is sudden, violent, and implacable."

**English Paraphrase**:
**Fuel of Fire** - Represents the **Earthy part of Fire** (Fuel/Combustion). She is the **irresistible chemical attraction** that allows fire to burn. Depicted nude (freedom to combine) with plumes of justice like flames. Qualities: **Brilliance, daring, vigour**. She creates beauty through sheer energy. In love or anger, she is sudden, violent, and implacable. She represents the **materialization of fire**—enthusiasm, ambition, and the power to consume.

**Core**: **Daring Passion** - Vitality, sexual/chemical attraction, enthusiasm, ambition, suddenness, materialization of will.

**Chinese Explanation**:
**权杖公主**代表**火中之土**（火的燃料）。她是可燃物质的**不可抗拒的化学吸引力**。她裸体（为了自由结合），戴着像火焰一样的正义羽毛。品质：**辉煌、大胆、活力**。她通过本质的活力创造自己的美。在爱或愤怒中，她是突然、猛烈且无法平息的。她代表火的**物质化**——热情、野心以及吞噬的力量。

**In Readings**: Enthusiasm, daring, sexual attraction, ambition, sudden news, violent reaction, fearlessness.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Princess of Wands represents Earth of Fire (fuel/combustion). Nude figure shows freedom for chemical reaction. Irresistible attraction enables fire. In love or anger: sudden, violent, implacable.
- **中文**: Crowley的权杖公主代表火中之土（燃料/燃烧）。裸体人物显示化学反应的自由。不可抗拒的吸引力使火成为可能。在爱或怒中：突然、猛烈、无法平息。

**Narrative Snippets**:
- `[ns_thoth_wands_040]` `[trigger: princess_wands_thoth]` `[factor_trigger: thoth_wands_princess]` `[role: 主干]` Princess of Wands = Earth of Fire—fuel of Fire; irresistible chemical attraction of combustible. → Core
- `[ns_thoth_wands_041]` `[trigger: nude_freedom]` `[factor_trigger: thoth_wands_princess AND symbol_nude]` `[role: 条件分支]` Nude figure—chemical action requires element perfectly free; plumes of justice like flames. → Visual
- `[ns_thoth_wands_042]` `[trigger: sudden_violent]` `[factor_trigger: thoth_wands_princess AND state_passion]` `[role: 条件分支]` In anger or love: sudden, violent, implacable—creates beauty by essential vigour. → Character

<!-- L1_END -->

<!-- L2_BEGIN -->

**L2 Semantic Extraction**:
- **Theme**: Materialization and Fuel of Fire.
- **Natural Attributes**:
  - *Element*: Earth of Fire (Fuel).
  - *Symbolism*: Nude figure (Chemical freedom), Flame plumes, Tiger/Leopard.
- **Functional Symbolism**:
  - *Combustion*: The attraction that allows fire to exist.
  - *Expression*: Sudden, violent, implacable energy.
- **Conditional Structure**:
  - *Nature*: Creates beauty through vigour.
  - *Shadow*: Superficial, theatrical, faithless.
 
**L2-Term Glossary**:
| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Princess of Wands | 权杖公主 | Court card of the Earthy part of Fire, embodying fuel and daring passion | 体现火中之土、作为燃料与大胆激情的宫廷牌——权杖公主 |
| Earth of Fire | 火中之土 | Aspect of Fire that appears as combustible material or fuel | 以可燃物、燃料形态出现的火之相位 |
| Chemical Attraction | 化学吸引力 | Irresistible tendency of substances to combine and ignite | 物质之间不可抗拒地结合并点燃的趋势 |
| Flame Plumes | 火焰羽饰 | Plumed headdress like flames, showing justice and fiery vitality | 类似火焰的羽饰头冠，象征正义与炽烈生命力 |
| Daring Passion | 大胆激情 | Fearless, sudden, consuming enthusiasm in love or anger | 在爱或怒中表现为无畏、骤然且带有吞噬性的热情 |

**Factor Layer (7-Column)**:
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-------|
| Element | Earth of Fire |  | new_candidate | Fuel | Combust | Princess as earthy part of Fire |
| Concept | Chemical Attraction |  | new_candidate | Interaction | Combine | Irresistible drive that enables combustion |
| Quality | Daring/Brilliant |  | new_candidate | Character | Consume | Moral colouring of her bold, vivid energy |
| Symbol | Plumes of Justice |  | new_candidate | Headgear | Stream | Flame‑like feathers expressing fiery vitality and justice |
| Shadow | Theatrical/False |  | new_candidate | Ill‑dignified mask | Deceive | Wrong energy when passion becomes mere show |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|-----------|
| rel_princess_wands_earth | elemental | earth_of_fire | fuel | Combustion | When Princess of Wands expresses Earth of Fire (fuel for combustion, material ignition) | Substance→Ignition | Thoth Princess Wands |
| rel_princess_wands_passion | attraction | chemical_force | combination | Irresistible | When Princess of Wands channels irresistible chemical attraction into passionate reaction | Potential→Reaction | Thoth Princess Wands |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| princess_wands_fuel | Daring passion | 食伤/比劫激发 | North Pole quadrant | 燃烧/激情象征 | Libido/Passion | Earth of Fire |
<!-- L2.5_END -->

<!-- L2_END -->

---

**✅ WANDS SUIT COMPLETE (14/14)**

> **Batch 1**: Ace, 2, 3, 4, 5, 6, 7.
> **Batch 2 (Final)**: 8, 9, 10, Knight, Queen, Prince, Princess.
> **Total Status**: All 14 Wands cards fully refined with L1+L2 bilingual text, semantic extraction, and Elemental Dignities.
> **Next Phase**: Suit of Cups (Water).

---
