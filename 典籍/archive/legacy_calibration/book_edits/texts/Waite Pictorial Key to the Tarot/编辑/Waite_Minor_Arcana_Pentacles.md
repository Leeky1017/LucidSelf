# Waite Pictorial Key - Minor Arcana: Pentacles

**Book**: Waite Pictorial Key to the Tarot (1910)  
**Author**: Arthur Edward Waite  
**Suit**: Pentacles (Earth Element)  
**Agent**: Text-EN-Agent  
**Format**: L1+L2 Bilingual v2.1 (Simplified for Minor Arcana)

---

## Progress Tracker

**Pentacles Suit Status**: 14/14 complete ✅
- Number Cards: 10/10 (Ace-Ten) ✅
- Court Cards: 4/4 (Page, Knight, Queen, King) ✅
- L2.5 Bridge Layer: 14/14 ✅
- Factor Layer 8列: 14/14 ✅
- L2-Term Glossary 6列: 14/14 ✅

---

## Pentacles - Earth Element

**Element**: Earth  
**Keywords**: Material, practical, wealth, work, physical realm, manifestation, stability  
**Corresponds to**: Physical/material realm, money, career, health, tangible results  
**Waite's Note**: Originally "current coin, money, deniers" but pentagram symbolizes "correspondence of four elements in human nature and that by which they may be governed"

**Pentacles Suite Factor Definitions**:
- `[ns_waite_p2]` `[trigger: minor_pentacles_two]` `[factor_trigger: minor_pentacles_two]` `[role: 主干]` Two of Pentacles represents change, gaiety, recreation—juggler with infinity cord. → Waite Pentacles
- `[ns_waite_p3]` `[trigger: minor_pentacles_three]` `[factor_trigger: minor_pentacles_three]` `[role: 主干]` Three of Pentacles represents skilled work, métier, mastery of craft in monastery. → Waite Pentacles
- `[ns_waite_p4]` `[trigger: minor_pentacles_four]` `[factor_trigger: minor_pentacles_four]` `[role: 主干]` Four of Pentacles represents surety of possessions, gift, legacy—clinging to material. → Waite Pentacles
- `[ns_waite_p5]` `[trigger: minor_pentacles_five]` `[factor_trigger: minor_pentacles_five]` `[role: 主干]` Five of Pentacles represents material trouble, poverty—two paupers in snow. → Waite Pentacles
- `[ns_waite_p6]` `[trigger: minor_pentacles_six]` `[factor_trigger: minor_pentacles_six]` `[role: 主干]` Six of Pentacles represents gifts, alms, generosity—merchant with scales distributes wealth. → Waite Pentacles
- `[ns_waite_p7]` `[trigger: minor_pentacles_seven]` `[factor_trigger: minor_pentacles_seven]` `[role: 主干]` Seven of Pentacles represents patience, ingenuity, waiting for harvest. → Waite Pentacles
- `[ns_waite_p8]` `[trigger: minor_pentacles_eight]` `[factor_trigger: minor_pentacles_eight]` `[role: 主干]` Eight of Pentacles represents work, employment, craftsmanship, apprenticeship. → Waite Pentacles
- `[ns_waite_p9]` `[trigger: minor_pentacles_nine]` `[factor_trigger: minor_pentacles_nine]` `[role: 主干]` Nine of Pentacles represents prudence, safety, success—woman in vineyard with hooded bird. → Waite Pentacles
- `[ns_waite_p10]` `[trigger: minor_pentacles_ten]` `[factor_trigger: minor_pentacles_ten]` `[role: 主干]` Ten of Pentacles represents gain, riches, family matters, legacy—old patriarch with dogs. → Waite Pentacles
- `[ns_waite_pp]` `[trigger: minor_pentacles_page]` `[factor_trigger: minor_pentacles_page]` `[role: 主干]` Page of Pentacles represents application, study, scholarship, reflection. → Waite Pentacles
- `[ns_waite_pk]` `[trigger: minor_pentacles_knight]` `[factor_trigger: minor_pentacles_knight]` `[role: 主干]` Knight of Pentacles represents utility, serviceableness, patience, heavy horse. → Waite Pentacles
- `[ns_waite_pq]` `[trigger: minor_pentacles_queen]` `[factor_trigger: minor_pentacles_queen]` `[role: 主干]` Queen of Pentacles represents opulence, generosity, magnificence, security. → Waite Pentacles
- `[ns_waite_pki]` `[trigger: minor_pentacles_king]` `[factor_trigger: minor_pentacles_king]` `[role: 主干]` King of Pentacles represents valour, realizing intelligence, business aptitude. → Waite Pentacles

---

### Ace of Pentacles

**Source Text**:
> "A hand--issuing, as usual, from a cloud--holds up a pentacle. Divinatory Meanings: Perfect contentment, felicity, ecstasy; also speedy intelligence; gold. Reversed: The evil side of wealth, bad intelligence; also great riches. In any case it shews prosperity, comfortable material conditions, but whether these are of advantage to the possessor will depend on whether the card is reversed or not."

**Core**: **Perfect Contentment & Gold** – Divine hand holds pentacle. Perfect contentment, felicity, ecstasy; speedy intelligence; gold. **"Shews prosperity, comfortable material conditions"** always, but **"whether of advantage depends on reversed or not."** **Reversed**: Evil side of wealth, bad intelligence; but still great riches (wealth without wisdom).

**Chinese**: **完美满足与黄金**——神手持星币。完美满足、幸福、狂喜；快速智慧；黄金。**"显示繁荣、舒适物质条件"**总是，但**"是否有利取决于逆位否"**。**逆位**：财富邪恶面、坏智慧；但仍巨富（无智慧财富）。

**Narrative Snippets**:
- `[ns_waite_pent_001]` `[trigger: ace_pent_waite]` `[factor_trigger: waite_pentacles_ace AND minor_pentacles_ace AND perfect_contentment AND evil_side]` `[role: 主干]` Ace of Pentacles = divine hand holds pentacle; perfect contentment, felicity, gold. → Core
- `[ns_waite_pent_002]` `[trigger: prosperity_always]` `[factor_trigger: waite_pentacles_ace AND condition]` `[role: 条件分支]` "Shews prosperity always; whether of advantage depends on reversed or not." → Meaning
- `[ns_waite_pent_003]` `[trigger: evil_side_wealth]` `[factor_trigger: waite_pentacles_ace AND reversal]` `[role: 条件分支]` Reversed: evil side of wealth, bad intelligence; but still great riches. → Shadow

#### L2 Semantic Extraction

- **Theme**: Seed of material prosperity—earthly contentment and wealth whose value depends on how it is used
- **Natural Attributes**:
  - Symbolism: Hand issuing from a cloud holds up a pentacle, garden beneath with archway, path leading outward
  - Characteristics: Solid, golden, grounded; shows prosperity and comfortable material conditions by default
  - Elements: Perfect contentment, felicity, ecstasy, speedy intelligence, gold; always prosperity, but advantage depends on reversal
- **Functional Symbolism**:
  - Opens opportunities in money, work, health, and tangible resources
  - Includes speedy practical intelligence in handling material affairs
  - Whether the prosperity is truly advantageous depends on how it is used—upright blessing vs. reversed corruption
- **Conditional Structure**:
  - **Necessary Conditions**: A material opportunity, resource, or opening that can be grasped
  - **Enhancing Conditions**: Wisdom in handling wealth, gratitude, and alignment of material gain with higher purpose
  - **Nullifying Conditions**: Evil side of wealth—greed, bad intelligence, or riches that harm the possessor through misuse
- **Multi-layered Interpretation**:
  - Literal Layer: Financial opportunities, job offers, health improvements, gifts, inheritances, or tangible new beginnings
  - Symbolic Layer: Archetype of the golden seed—material potential that can grow into blessing or burden
  - Practical Layer: Encourages seizing material opportunities while being wise about their use and implications
  - Psychological Layer: Relationship to abundance, security, and the question of whether wealth serves or enslaves

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Ace of Pentacles | 星币王牌 | Seed of material prosperity and contentment | 物质繁荣与满足的种子 | minor_pentacles_ace | existing |
| Perfect Contentment | 完美满足 | Deep satisfaction grounded in material security | 建立在物质安全之上的深度满足 | | new_candidate |
| Prosperity Always | 总是繁荣 | Card always indicates prosperity and comfort | 该牌始终指向繁荣与舒适物质条件 | | new_candidate |
| Advantage Depends on Reversal | 有利取决逆位 | Benefit or harm depends on upright or reversed orientation | 是否真正有利取决于正位或逆位 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ace of Pentacles | minor_pentacles_ace | existing | Tarot Card | Earth seed | tarot_semantic | Earth of Earth |
| Functional | Material Prosperity | | new_candidate | Life Area | Money, assets | tarot_semantic | Comfort baseline |
| State | Wise vs Corrupt | | new_candidate | Condition | Contentment vs evil | tarot_semantic | Use vs misuse |
| Relational | Pentacle-Earth | | new_candidate | Symbol | Manifestation | tarot_semantic | Four elements |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_001 | prosperity_source | minor_pentacles_ace | perfect_contentment | Hand holds pentacle | When Ace of Pentacles divine hand offers perfect contentment and prosperity | grounding | Waite #Ace_Pentacles |
| rel_pent_002 | wealth_polarity | minor_pentacles_ace | evil_side | Same wealth | When Ace of Pentacles reversed reveals evil side of same wealth energy | determining | Waite #Ace_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_001 | "whether these are of advantage to the possessor will depend on whether the card is reversed or not" | minor_pentacles_ace | Prosperity -> reversal -> advantage | Ace = conditional wealth | High | Yes | rule_pent_ace_wealth |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_material_seed | Root of earthly prosperity | | sign_taurus, planet_venus | gold_dream, coin_dream | material_security | Depends on reversal |
<!-- L2.5_END -->

---

### Two of Pentacles

**Source Text**:
> "A young man, in the act of dancing, has a pentacle in either hand, and they are joined by that endless cord which is like the number 8 reversed. Divinatory Meanings: On the one hand it is represented as a card of gaiety, recreation and its connexions, which is the subject of the design; but it is read also as news and messages in writing, as obstacles, agitation, trouble, embroilment. Reversed: Enforced gaiety, simulated enjoyment, literal sense, handwriting, composition, letters of exchange."

**Core**: **Juggling & Infinity Loop** – Young man dancing, pentacle in each hand joined by **endless cord like number 8 reversed** (infinity symbol). Gaiety, recreation; but also news in writing, obstacles, agitation, trouble. **Reversed**: Enforced gaiety, simulated enjoyment, handwriting, letters of exchange.

**Chinese**: **杂耍与无限环**——年轻人跳舞，两手各持星币，由**像倒8的无尽绳连接**（无限符号）。欢乐、娱乐；但也指书面消息、障碍、焦躁、麻烦。**逆位**：强制欢乐、模拟享受、笔迹、汇票。

**Narrative Snippets**:
- `[ns_waite_pent_004]` `[trigger: two_pent_waite]` `[factor_trigger: waite_pentacles_two]` `[role: 主干]` Two of Pentacles = dancing juggler; endless cord like infinity; gaiety, recreation. → Core
- `[ns_waite_pent_005]` `[trigger: obstacles_agitation]` `[factor_trigger: waite_pentacles_two AND challenge]` `[role: 条件分支]` Also: news in writing, obstacles, agitation, trouble, embroilment. → Complexity
- `[ns_waite_pent_006]` `[trigger: enforced_gaiety]` `[factor_trigger: waite_pentacles_two AND reversal]` `[role: 条件分支]` Reversed: enforced gaiety, simulated enjoyment, handwriting, letters of exchange. → Shadow

#### L2 Semantic Extraction

- **Theme**: Juggling realities and flows—playful yet pressured management of multiple material or practical demands
- **Natural Attributes**:
  - Symbolism: Young man dancing with a pentacle in each hand, joined by an endless cord shaped like a reversed 8 (infinity symbol), ships on waves behind
  - Characteristics: Dynamic, rhythmic, cyclical; adapting to changing conditions with apparent ease
  - Elements: Gaiety, recreation; but also news in writing, obstacles, agitation, trouble, embroilment
- **Functional Symbolism**:
  - Indicates balancing finances, tasks, time, and communications—keeping multiple balls in the air
  - Shows adaptability to changing circumstances, managing fluctuations in resources or priorities
  - Reversed, it becomes enforced gaiety, simulated enjoyment, and stress around written exchanges or financial documents
- **Conditional Structure**:
  - **Necessary Conditions**: Multiple demands, resources, or concerns requiring simultaneous attention
  - **Enhancing Conditions**: Flexibility, good timing, genuine enjoyment of the juggling process, and skill developed through practice
  - **Nullifying Conditions**: Overwhelm, fake cheerfulness, agitation that disrupts rhythm, or too many balls dropping at once
- **Multi-layered Interpretation**:
  - Literal Layer: Balancing budgets, managing multiple jobs or projects, handling correspondence and financial paperwork
  - Symbolic Layer: Archetype of the cosmic juggler—life as dance requiring constant adaptation within endless cycles
  - Practical Layer: Encourages developing flexibility and rhythm in managing practical affairs; warns against overcommitment
  - Psychological Layer: Inner adaptability, playfulness under pressure, and the shadow of stress masked by forced gaiety

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Two of Pentacles | 星币二 | Dancer juggling two pentacles linked by infinity cord | 以无限绳连接两星币、边跳舞边杂耍的人物 | minor_pentacles_two | existing |
| Endless Cord / Infinity | 无尽绳 / 无限 | Cord shaped like reversed 8, symbol of ongoing cycles | 如倒八字、象征循环不息的绳索 | | new_candidate |
| Juggling / Balancing | 杂耍 / 平衡 | Managing more than one task, resource or concern | 同时管理多项任务、资源或议题的状态 | | new_candidate |
| Enforced Gaiety | 强制欢乐 | Forced or inauthentic enjoyment under pressure | 在压力下被迫或不真诚的"快乐"表现 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Two of Pentacles | minor_pentacles_two | existing | Tarot Card | Cyclical juggling | tarot_semantic | Earth in motion |
| Functional | Resource Balancing | | new_candidate | Life Area | Budgeting, time | tarot_semantic | Financial juggling |
| State | Flow vs Overload | | new_candidate | Condition | Agile vs agitation | tarot_semantic | Stress level |
| Relational | Infinity Loop | | new_candidate | Symbol | Endless cord | tarot_semantic | Cyclic patterns |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_003 | juggling_dance | minor_pentacles_two | infinity_cord | Young man dancing | When Two of Pentacles young man dances juggling with infinity cord | balancing | Waite #Two_Pentacles |
| rel_pent_004 | gaiety_axis | minor_pentacles_two | enforced_gaiety | Recreation | When Two of Pentacles shows genuine gaiety upright vs forced gaiety reversed | contrasting | Waite #Two_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_002 | "joined by that endless cord which is like the number 8 reversed" | minor_pentacles_two | Dance -> infinity cord -> cycles | Two = cyclical balance | High | Yes | rule_pent_two_juggling |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_cyclical_balance | Managing multiple demands in rhythm | | sign_gemini | juggling_dream, dance_dream | adaptive_flexibility | Infinity cord |
<!-- L2.5_END -->

---

### Three of Pentacles

**Source Text**:
> "A sculptor at his work in a monastery. Compare the design which illustrates the Eight of Pentacles. The apprentice or amateur therein has received his reward and is now at work in earnest. Divinatory Meanings: Métier, trade, skilled labour; usually, however, regarded as a card of nobility, aristocracy, renown, glory. Reversed: Mediocrity, in work and otherwise, puerility, pettiness, weakness."

**Core**: **Mastery & Monastery Work** – Sculptor at work in monastery. **"Apprentice (from Eight) has received reward, now at work in earnest."** (graduated to master). Métier, trade, skilled labor; but usually: nobility, aristocracy, renown, glory (recognition). **Reversed**: Mediocrity, puerility, pettiness.

**Chinese**: **精通与修道院工作**——雕刻家在修道院工作。**"学徒（来自八）已获奖励，现在认真工作"**（升为大师）。职业、行业、技能劳动；但通常：贵族、声望、荣耀（认可）。**逆位**：平庸、幼稚、渺小。

**Narrative Snippets**:
- `[ns_waite_pent_007]` `[trigger: three_pent_waite]` `[factor_trigger: waite_pentacles_three]` `[role: 主干]` Three of Pentacles = sculptor in monastery; apprentice now master; trade, skilled labour. → Core
- `[ns_waite_pent_008]` `[trigger: renown_glory]` `[factor_trigger: waite_pentacles_three AND recognition]` `[role: 条件分支]` Usually read as nobility, aristocracy, renown, glory—recognition for craft. → Meaning
- `[ns_waite_pent_009]` `[trigger: mediocrity]` `[factor_trigger: waite_pentacles_three AND reversal]` `[role: 条件分支]` Reversed: mediocrity, puerility, pettiness, weakness. → Shadow

#### L2 Semantic Extraction

- **Theme**: Mastery, vocation, and recognised work—craft that has moved beyond apprenticeship into earnest practice
- **Natural Attributes**:
  - Symbolism: Sculptor at work in a monastery, figures consulting or admiring, three pentacles integrated into the architecture
  - Characteristics: Structured, diligent, dedicated; labour linked with communal or sacred purpose
  - Elements: Métier, trade, skilled labour; but usually read as nobility, aristocracy, renown, glory—recognition for craft
- **Functional Symbolism**:
  - Speaks to professional craft, skilled trade, and the honour that accompanies true mastery of a métier
  - Shows the apprentice who has graduated (compare Eight of Pentacles) and is now working in earnest at a higher level
  - Reversed, it warns of mediocrity, puerility, pettiness, and failure to develop one's talents fully
- **Conditional Structure**:
  - **Necessary Conditions**: A context where skill, craft, or professional expertise is required and can be recognised
  - **Enhancing Conditions**: Dedication, training, mentorship, and environments that value quality work
  - **Nullifying Conditions**: Mediocrity, laziness, pettiness, or contexts that do not reward genuine craftsmanship
- **Multi-layered Interpretation**:
  - Literal Layer: Professional recognition, teamwork on skilled projects, architectural or artistic commissions, career advancement
  - Symbolic Layer: Archetype of the master craftsman—labour elevated to vocation, work that serves a higher purpose
  - Practical Layer: Encourages investing in skill development, collaboration, and seeking recognition for quality work
  - Psychological Layer: Sense of vocation and pride in craft; the shadow of mediocrity when effort is not sustained

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Three of Pentacles | 星币三 | Sculptor at work in a monastery | 在修道院中工作的雕刻师 | minor_pentacles_three | existing |
| Apprentice Graduated | 学徒升级 | Movement from apprenticeship to mastery | 从学徒阶段提升到大师水准 | | new_candidate |
| Monastery Work | 修道院工作 | Craft done in a sacred or communal setting | 在神圣或群体环境中从事的工艺工作 | | new_candidate |
| Renown / Glory | 声望 / 荣耀 | Public recognition for one's craft or status | 因工艺或身份而获得的公众认可与荣耀 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Three of Pentacles | minor_pentacles_three | existing | Tarot Card | Vocation, craft | tarot_semantic | Link to Eight |
| Functional | Craftsmanship | | new_candidate | Life Area | Skilled labour | tarot_semantic | Trade + nobility |
| State | Mastery vs Mediocrity | | new_candidate | Condition | Skill vs puerility | tarot_semantic | Quality |
| Relational | Apprentice-Master | | new_candidate | Process | Eight to Three | tarot_semantic | Narrative loop |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_005 | mastery_work | minor_pentacles_three | monastery | Sculptor at work | When Three of Pentacles shows sculptor earnestly crafting in monastery setting | crafting | Waite #Three_Pentacles |
| rel_pent_006 | apprentice_graduated | minor_pentacles_three | eight_pentacles | Received reward | When Three of Pentacles apprentice has graduated from Eight's training | progressing | Waite #Three_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_003 | "The apprentice or amateur therein has received his reward and is now at work in earnest" | minor_pentacles_three | Apprentice -> reward -> earnest | Three = mastery achieved | High | Yes | rule_pent_three_mastery |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_skilled_vocation | Craft elevated to mastery and recognition | | sign_virgo, planet_mercury | craft_dream, monastery_dream | competence_mastery | Apprentice graduated |
<!-- L2.5_END -->

---

### Four of Pentacles

**Source Text**:
> "A crowned figure, having a pentacle over his crown, clasps another with hands and arms; two pentacles are under his feet. He holds to that which he has. Divinatory Meanings: The surety of possessions, cleaving to that which one has, gift, legacy, inheritance. Reversed: Suspense, delay, opposition."

**Core**: **Hoarding & Clinging** – Crowned figure, pentacle on crown, clasps another, two under feet. **"He holds to that which he has."** Surety of possessions, cleaving to what one has, inheritance. **Reversed**: Suspense, delay, opposition (blocking flow).

**Chinese**: **囤积与紧抓**——戴冠人物，星币在冠上，紧抱另一个，两个在脚下。**"他紧持所拥有"**。财产确保、紧抓所有、继承。**逆位**：悬而未决、延迟、对立（阻碍流动）。

**Narrative Snippets**:
- `[ns_waite_pent_010]` `[trigger: four_pent_waite]` `[factor_trigger: waite_pentacles_four]` `[role: 主干]` Four of Pentacles = crowned figure holding pentacles; "holds to that which he has". → Core
- `[ns_waite_pent_011]` `[trigger: surety_possessions]` `[factor_trigger: waite_pentacles_four AND security]` `[role: 条件分支]` Surety of possessions, cleaving to what one has, gift, legacy, inheritance. → Meaning
- `[ns_waite_pent_012]` `[trigger: suspense_delay]` `[factor_trigger: waite_pentacles_four AND reversal]` `[role: 条件分支]` Reversed: suspense, delay, opposition—blocked material flow. → Shadow

#### L2 Semantic Extraction

- **Theme**: Possession, security, and clinging—holding tightly to what one owns, for better or worse
- **Natural Attributes**:
  - Symbolism: Crowned figure with pentacle on crown, clasping another to chest, two under feet; city in the background
  - Characteristics: Fixed, heavy, guarded; total occupation with material holding—on head, heart, and foundation
  - Elements: Surety of possessions, cleaving to that which one has, gift, legacy, inheritance
- **Functional Symbolism**:
  - Shows financial stability, surety of possessions, and the security that comes from holding assets
  - Indicates inheritance, legacy, or gifts that are held rather than circulated
  - Reversed, it highlights stuckness, delay, and opposition that arise from over‑attachment to material security
- **Conditional Structure**:
  - **Necessary Conditions**: Assets, resources, or position that can be held and protected
  - **Enhancing Conditions**: Prudent saving, responsible stewardship, and security that does not strangle generosity
  - **Nullifying Conditions**: Hoarding, miserliness, or clinging so tight that flow is blocked and growth is prevented
- **Multi-layered Interpretation**:
  - Literal Layer: Savings, property ownership, inheritances, or conservative financial management
  - Symbolic Layer: Archetype of the miser or guardian—one who holds to what he has, for security or from fear
  - Practical Layer: Encourages securing resources but warns against hoarding; balance between stability and flow
  - Psychological Layer: Attachment to security, fear of loss, and the question of whether possessions possess the possessor

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Four of Pentacles | 星币四 | Crowned figure holding and standing on pentacles | 头戴星币、抱持星币并脚踏星币的人物 | minor_pentacles_four | existing |
| Holds to What He Has | 紧持所有 | Refusal to release what is already possessed | 拒绝放手现有财物的态度 | | new_candidate |
| Cleaving | 紧抓 | Strong emotional and physical attachment to possessions | 对财物强烈的情感与身体抓握 | | new_candidate |
| Surety of Possessions | 财产确保 | Sense of security derived from what one owns | 从所拥有之物中获得的安全感 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Four of Pentacles | minor_pentacles_four | existing | Tarot Card | Fixed, possessive | tarot_semantic | Stability through holding |
| Functional | Security & Attachment | | new_candidate | Life Area | Savings, property | tarot_semantic | Fear of loss |
| State | Stability vs Stagnation | | new_candidate | Condition | Secure vs blocked | tarot_semantic | Flow vs hoarding |
| Relational | Flow of Resources | | new_candidate | Axis | Holding vs circulation | tarot_semantic | Bridge to Six charity |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_007 | hoarding | minor_pentacles_four | possessions | Crowned figure | When Four of Pentacles crowned figure hoards possessions tightly | securing | Waite #Four_Pentacles |
| rel_pent_008 | blocked_flow | minor_pentacles_four | suspense | Cleaving | When Four of Pentacles blocks material flow causing suspense and delay | opposing | Waite #Four_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_004 | "He holds to that which he has" | minor_pentacles_four | Crowned -> clasps -> holds | Four = possessive security | High | Yes | rule_pent_four_hoarding |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_possessive_security | Clinging to material for safety | | sign_taurus, planet_saturn | hoarding_dream, crown_dream | attachment_security | Holds to what he has |
<!-- L2.5_END -->

---

### Five of Pentacles

**Source Text**:
> "Two mendicants in a snow-storm pass a lighted casement. Divinatory Meanings: The card foretells material trouble above all, whether in the form illustrated--that is, destitution--or otherwise. For some cartomancists, it is a card of love and lovers-wife, husband, friend, mistress; also concordance, affinities. These alternatives cannot be harmonized. Reversed: Disorder, chaos, ruin, discord, profligacy."

**Core**: **Destitution Outside Lighted Window** – Two mendicants in snowstorm pass **lighted casement** (warmth/help nearby but missed). Material trouble, destitution. Alternative: love/lovers (unharmonizable). **Reversed**: Disorder, chaos, ruin, profligacy.

**Chinese**: **在亮窗外的贫困**——两乞丐在暴风雪中经过**亮窗**（温暖/帮助近在但错过）。物质困境、贫困。另解：爱/情人（无法协调）。**逆位**：混乱、毁坏、挥霍。

**Narrative Snippets**:
- `[ns_waite_pent_013]` `[trigger: five_pent_waite]` `[factor_trigger: waite_pentacles_five]` `[role: 主干]` Five of Pentacles = mendicants in snowstorm pass lighted window; material trouble. → Core
- `[ns_waite_pent_014]` `[trigger: help_nearby]` `[factor_trigger: waite_pentacles_five AND refuge]` `[role: 条件分支]` Lighted casement = warmth/help nearby but missed; destitution with refuge close. → Symbol
- `[ns_waite_pent_015]` `[trigger: disorder_ruin]` `[factor_trigger: waite_pentacles_five AND reversal]` `[role: 条件分支]` Reversed: disorder, chaos, ruin, discord, profligacy. → Shadow

#### L2 Semantic Extraction

- **Theme**: Material destitution and missed refuge—poverty outside a lighted window of help
- **Natural Attributes**:
  - Symbolism: Two mendicants in a snowstorm passing a lighted casement (church window), visibly cold and excluded, warmth nearby
  - Characteristics: Cold, exposed, wandering; yet visible warmth and security close at hand but not accessed
  - Elements: Material trouble, destitution; alternative reading as love/lovers cannot be harmonised; reversed = disorder, chaos, ruin, profligacy
- **Functional Symbolism**:
  - Foretells financial or physical hardship, exclusion, and the feeling of being left out in the cold
  - Shows help nearby (lighted window) that is either unseen, unavailable, or refused
  - Reversed, it deepens into disorder, chaos, ruin, and wasteful profligacy of whatever remains
- **Conditional Structure**:
  - **Necessary Conditions**: A situation of material lack, exclusion, or hardship
  - **Enhancing Conditions**: Isolation, pride, unawareness, or barriers that prevent accessing available help
  - **Nullifying Conditions**: Recognising and accepting the lighted window—turning toward available support, community, or charity
- **Multi-layered Interpretation**:
  - Literal Layer: Poverty, unemployment, illness, exclusion from institutions, or feeling like an outsider
  - Symbolic Layer: Archetype of the wanderer outside warmth—material suffering with refuge tantalisingly close
  - Practical Layer: Encourages looking for help that may be nearby; warns against pride or blindness that refuses aid
  - Psychological Layer: Inner sense of lack, exclusion, or unworthiness; the work of accepting support and belonging

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Five of Pentacles | 星币五 | Two mendicants in snow passing a lighted casement | 两乞丐于雪中路过亮窗的画面 | minor_pentacles_five | existing |
| Lighted Casement | 亮窗 | Window of light and warmth suggesting possible refuge | 代表光明与温暖、暗示可能庇护的窗户 | | new_candidate |
| Destitution | 贫困 | Condition of severe lack and material trouble | 严重匮乏与物质困境的状态 | | new_candidate |
| Help Nearby but Missed | 帮助近在但错过 | Aid present but unseen or unaccepted | 帮助近在眼前却未被看见或接纳 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Five of Pentacles | minor_pentacles_five | existing | Tarot Card | Hardship, exclusion | tarot_semantic | Poverty outside window |
| Functional | Material Trouble | | new_candidate | Life Area | Debt, unemployment | tarot_semantic | Foretells trouble |
| State | Lack vs Refuge | | new_candidate | Condition | Cold vs warmth | tarot_semantic | Window symbolism |
| Relational | Lighted Window | | new_candidate | Symbol | Charitable institutions | tarot_semantic | Bridge to Six |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_009 | destitution | minor_pentacles_five | lighted_window | Mendicants pass | When Five of Pentacles mendicants pass lighted window in snowstorm | excluding | Waite #Five_Pentacles |
| rel_pent_010 | missed_refuge | minor_pentacles_five | help_nearby | Window visible | When Five of Pentacles shows help nearby but unnoticed by those in need | ignoring | Waite #Five_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_005 | "Two mendicants in a snow-storm pass a lighted casement" | minor_pentacles_five | Snow -> pass window -> miss help | Five = poverty near refuge | High | Yes | rule_pent_five_destitution |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_missed_refuge | Help nearby but unseen or rejected | | sign_capricorn, planet_saturn | poverty_dream, snow_dream | learned_helplessness | Lighted casement |
<!-- L2.5_END -->

---

### Six of Pentacles

**Source Text**:
> "A person in the guise of a merchant weighs money in a pair of scales and distributes it to the needy and distressed. It is a testimony to his own success in life, as well as to his goodness of heart. Divinatory Meanings: Presents, gifts, gratification another account says attention, vigilance now is the accepted time, present prosperity, etc. Reversed: Desire, cupidity, envy, jealousy, illusion."

**Core**: **Charity & Just Scales** – Merchant **weighs money in scales**, distributes to needy. **"Testimony to his success and goodness of heart."** Presents, gifts, gratification; **"now is accepted time,"** present prosperity. **Reversed**: Desire, cupidity, envy, jealousy.

**Chinese**: **慈善与公正天平**——商人**在天平称钱**，分发给需要者。**"证明其成功与善心"**。礼物、感激；**"现在是被接受的时刻"**，当前繁荣。**逆位**：欲望、贪婪、嫉妒。

**Narrative Snippets**:
- `[ns_waite_pent_016]` `[trigger: six_pent_waite]` `[factor_trigger: waite_pentacles_six]` `[role: 主干]` Six of Pentacles = merchant weighs money in scales; distributes to needy. → Core
- `[ns_waite_pent_017]` `[trigger: success_goodness]` `[factor_trigger: waite_pentacles_six AND charity]` `[role: 条件分支]` "Testimony to his success and goodness of heart"; now is accepted time. → Meaning
- `[ns_waite_pent_018]` `[trigger: cupidity_envy]` `[factor_trigger: waite_pentacles_six AND reversal]` `[role: 条件分支]` Reversed: desire, cupidity, envy, jealousy, illusion. → Shadow

#### L2 Semantic Extraction

- **Theme**: Measured charity and reciprocal flow—success expressed through just giving
- **Natural Attributes**:
  - Symbolism: Merchant weighing money in a pair of scales, distributing coins to needy figures below, testimony to his success and goodness of heart
  - Characteristics: Balanced, weighing, distributive; scales emphasise proportion and fairness in material exchange
  - Elements: Presents, gifts, gratification, attention, vigilance; "now is the accepted time," present prosperity
- **Functional Symbolism**:
  - Indicates gifts, presents, aid, and attention stemming from prosperity and genuine benevolence
  - Shows the circulation of wealth—giving and receiving in just measure—as expression of success
  - Reversed, it exposes desire, cupidity, envy, and jealousy that distort the flow of resources
- **Conditional Structure**:
  - **Necessary Conditions**: Resources available for distribution and recipients in need of aid
  - **Enhancing Conditions**: Goodness of heart, wise timing ("now is the accepted time"), and fairness in measuring what is given
  - **Nullifying Conditions**: Greed, envy, jealousy, or giving that is manipulative rather than generous
- **Multi-layered Interpretation**:
  - Literal Layer: Charitable donations, loans, scholarships, fair business dealings, or receiving help from someone more prosperous
  - Symbolic Layer: Archetype of the just merchant—prosperity that circulates rather than hoards, measured by scales
  - Practical Layer: Encourages both giving and receiving with dignity; warns against envy and cupidity that corrupt generosity
  - Psychological Layer: Relationship to giving and receiving, power dynamics in charity, and the question of whether giving is genuine or controlling

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Six of Pentacles | 星币六 | Merchant weighing money and giving to the needy | 在天平称钱并施与穷人的商人 | minor_pentacles_six | existing |
| Weighs in Scales | 天平称 | Act of weighing to ensure just measure | 通过称量确保公正分配的动作 | | new_candidate |
| Now is Accepted Time | 现在是被接受时刻 | Moment when giving or receiving is especially timely | 给予或领受尤为适合的当下时机 | | new_candidate |
| Success and Goodness of Heart | 成功与善心 | Prosperity joined with genuine benevolence | 物质成功与真实善意的结合 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Six of Pentacles | minor_pentacles_six | existing | Tarot Card | Weighed giving | tarot_semantic | Merchant with scales |
| Functional | Charity & Redistribution | | new_candidate | Life Area | Donations, aid | tarot_semantic | Success expressed |
| State | Just Measure vs Cupidity | | new_candidate | Condition | Timely vs greedy | tarot_semantic | Moral tone |
| Relational | Scales & Justice | | new_candidate | Symbol | Libra imagery | tarot_semantic | Balance archetypes |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_011 | charitable_giving | minor_pentacles_six | scales | Merchant weighs | When Six of Pentacles merchant weighs and distributes charity to needy | sharing | Waite #Six_Pentacles |
| rel_pent_012 | success_testimony | minor_pentacles_six | goodness_heart | His success | When Six of Pentacles testifies to giver's success and goodness of heart | demonstrating | Waite #Six_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_006 | "It is a testimony to his own success in life, as well as to his goodness of heart" | minor_pentacles_six | Weighs -> distributes -> testimony | Six = generous success | High | Yes | rule_pent_six_charity |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_measured_charity | Just giving from prosperity | | sign_libra, planet_venus | scales_dream, giving_dream | generativity | Now is accepted time |
<!-- L2.5_END -->

---

### Seven of Pentacles

**Source Text**:
> "A young man, leaning on his staff, looks intently at seven pentacles attached to a clump of greenery on his right; one would say that these were his treasures and that his heart was there. Divinatory Meanings: These are exceedingly contradictory; in the main, it is a card of money, business, barter; but one reading gives altercation, quarrels--and another innocence, ingenuity, purgation. Reversed: Cause for anxiety regarding money which it may be proposed to lend."

**Core**: **Assessing Harvest** – Young man on staff looks at seven pentacles on greenery. **"These were his treasures, his heart was there."** Waite: **"Exceedingly contradictory"**: money/business/barter; or altercation/quarrels; or innocence/ingenuity/purgation. **Reversed**: Anxiety about lending money.

**Chinese**: **评估收获**——年轻人靠杖看七星币在绿植上。**"这些是其财宝，其心在此"**。韦特：**"极度矛盾"**：金钱/商业/交易；或争吵；或天真/独创/净化。**逆位**：关于借钱的焦虑。

**Narrative Snippets**:
- `[ns_waite_pent_019]` `[trigger: seven_pent_waite]` `[factor_trigger: waite_pentacles_seven]` `[role: 主干]` Seven of Pentacles = man gazing at pentacles on greenery; "his treasures, his heart was there". → Core
- `[ns_waite_pent_020]` `[trigger: contradictory_meanings]` `[factor_trigger: waite_pentacles_seven AND polyvalence]` `[role: 条件分支]` Waite: "Exceedingly contradictory"—money/barter/quarrels/innocence/purgation. → Complexity
- `[ns_waite_pent_021]` `[trigger: lending_anxiety]` `[factor_trigger: waite_pentacles_seven AND reversal]` `[role: 条件分支]` Reversed: cause for anxiety regarding money which may be proposed to lend. → Shadow

#### L2 Semantic Extraction

- **Theme**: Evaluating harvest and value—where one's treasures are, one's heart is also
- **Natural Attributes**:
  - Symbolism: Young man leaning on staff, looking intently at seven pentacles attached to greenery; his treasures and his heart are there
  - Characteristics: Paused, reflective, invested; focused on growth and what it is yielding
  - Elements: Money, business, barter; but also altercation, quarrels; or innocence, ingenuity, purgation—Waite notes these are "exceedingly contradictory"
- **Functional Symbolism**:
  - Concerns money, business, and barter—the practical assessment of what one has cultivated
  - Shows the mixed experiences that come with evaluating gains: satisfaction, quarrels, or unexpected innocence and purgation
  - Reversed, it highlights anxiety about lending money or extending resources to others
- **Conditional Structure**:
  - **Necessary Conditions**: Something planted or invested that has reached a stage where evaluation is meaningful
  - **Enhancing Conditions**: Patience, realistic assessment, and emotional investment aligned with practical results
  - **Nullifying Conditions**: Anxiety, quarrels, or distorted expectations that prevent clear-eyed evaluation of what has grown
- **Multi-layered Interpretation**:
  - Literal Layer: Reviewing investments, waiting for results, assessing business returns, or deciding whether to continue a project
  - Symbolic Layer: Archetype of the farmer at harvest—pause between planting and reaping, heart bound to the outcome
  - Practical Layer: Encourages honest assessment of what has been cultivated; patience before the final harvest
  - Psychological Layer: Emotional investment in outcomes, the anxiety of waiting, and the contradictory feelings that arise when evaluating what one has built

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Seven of Pentacles | 星币七 | Young man assessing seven pentacles on greenery | 靠杖凝视绿植上七枚星币的青年 | minor_pentacles_seven | existing |
| His Heart Was There | 其心在此 | Emotional investment focused where treasures lie | 情感投注集中于财宝所在之处 | | new_candidate |
| Exceedingly Contradictory | 极度矛盾 | Waite's note on multiple, divergent meanings | 韦伯特所述多重分歧含义的特征 | | new_candidate |
| Assessing Harvest | 评估收获 | Process of judging results and returns | 评估成果与回报的过程 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Seven of Pentacles | minor_pentacles_seven | existing | Tarot Card | Evaluation stage | tarot_semantic | Pause over coins |
| Functional | Investment & Evaluation | | new_candidate | Life Area | Savings, returns | tarot_semantic | Money/business axis |
| State | Content vs Anxiety | | new_candidate | Condition | Reflective vs anxious | tarot_semantic | Emotional tone |
| Relational | Contradictory Readings | | new_candidate | Note | Multiple meanings | tarot_semantic | Polyvalence |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_013 | heart_treasures | minor_pentacles_seven | greenery | Looks intently | When Seven of Pentacles farmer gazes at greenery where his heart's treasures lie | assessing | Waite #Seven_Pentacles |
| rel_pent_014 | contradictory | minor_pentacles_seven | meanings | Exceedingly | When Seven of Pentacles presents contradictory meanings requiring careful interpretation | complicating | Waite #Seven_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_007 | "one would say that these were his treasures and that his heart was there" | minor_pentacles_seven | Looks -> treasures -> heart | Seven = invested assessment | High | Yes | rule_pent_seven_harvest |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_harvest_assessment | Evaluating what has grown | | sign_virgo, planet_saturn | harvest_dream, garden_dream | delayed_gratification | His heart was there |
<!-- L2.5_END -->

---

### Eight of Pentacles

**Source Text**:
> "An artist in stone at his work, which he exhibits in the form of trophies. Divinatory Meanings: Work, employment, commission, craftsmanship, skill in craft and business, perhaps in the preparatory stage. Reversed: Voided ambition, vanity, cupidity, exaction, usury. It may also signify the possession of skill, in the sense of the ingenious mind turned to cunning and intrigue."

**Core**: **Craftsmanship & Apprenticeship** – Artist in stone at work, exhibits trophies. Work, employment, craftsmanship, **"perhaps in preparatory stage"** (still learning). **Reversed**: Voided ambition, vanity, usury; or **"skill turned to cunning and intrigue."**

**Chinese**: **工艺与学徒**——石艺术家工作，展示战利品。工作、雇佣、工艺，**"也许在准备阶段"**（仍在学习）。**逆位**：虚妄野心、虚荣、高利贷；或**"技能转为狡诈阴谋"**。

**Narrative Snippets**:
- `[ns_waite_pent_022]` `[trigger: eight_pent_waite]` `[factor_trigger: waite_pentacles_eight]` `[role: 主干]` Eight of Pentacles = artist at work exhibiting trophies; craftsmanship, preparatory stage. → Core
- `[ns_waite_pent_023]` `[trigger: skill_craft]` `[factor_trigger: waite_pentacles_eight AND diligence]` `[role: 条件分支]` Work, employment, commission, skill in craft and business—perhaps still learning. → Meaning
- `[ns_waite_pent_024]` `[trigger: skill_cunning]` `[factor_trigger: waite_pentacles_eight AND reversal]` `[role: 条件分支]` Reversed: voided ambition, vanity, usury; skill turned to cunning and intrigue. → Shadow

#### L2 Semantic Extraction

- **Theme**: Apprenticeship and diligent work—skill being honed through repeated practice
- **Natural Attributes**:
  - Symbolism: Artist in stone at work, exhibiting his crafted pentacles as trophies, focused on the task at hand
  - Characteristics: Focused, industrious, methodical; trophies show visible results but process and learning remain central
  - Elements: Work, employment, commission, craftsmanship, skill in craft and business—perhaps in the preparatory stage
- **Functional Symbolism**:
  - Points to employment, commissions, and craftsmanship, particularly at the learning or preparatory stage
  - Shows the value of repetition, practice, and incremental improvement in building real skill
  - Reversed, it warns of voided ambition, vanity, usury, and skill turned toward cunning and intrigue
- **Conditional Structure**:
  - **Necessary Conditions**: A craft, trade, or skill that can be developed through sustained, focused effort
  - **Enhancing Conditions**: Discipline, patience, good mentorship, and genuine engagement with the work
  - **Nullifying Conditions**: Voided ambition, vanity, greed (usury), or using skill for cunning and manipulation rather than honest craft
- **Multi-layered Interpretation**:
  - Literal Layer: Training, apprenticeships, skill-building work, commissions, or employment in a craft-based field
  - Symbolic Layer: Archetype of the apprentice—diligent repetition that transforms raw talent into mastery
  - Practical Layer: Encourages investing in skill development, accepting the preparatory stage, and producing quality work
  - Psychological Layer: Sense of purpose through productive work; shadow shown when ambition is hollow or skill is corrupted into manipulation

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Eight of Pentacles | 星币八 | Stone-worker exhibiting his crafted pentacles | 展示自己石制星币作品的工匠 | minor_pentacles_eight | existing |
| Preparatory Stage | 准备阶段 | Early phase of training and work | 学习与工作的早期阶段 | | new_candidate |
| Skill Turned to Cunning | 技能转狡诈 | Ability used for intrigue or manipulation | 被用于阴谋或操控的能力 | | new_candidate |
| Craftsmanship | 工艺技巧 | Careful, skilled making in a chosen field | 在某领域中细致而熟练的制作 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Eight of Pentacles | minor_pentacles_eight | existing | Tarot Card | Skill-building work | tarot_semantic | Links to Three |
| Functional | Work & Skill | | new_candidate | Life Area | Practice, apprenticeship | tarot_semantic | Commissioned tasks |
| State | Constructive vs Corrupt | | new_candidate | Condition | Learning vs cunning | tarot_semantic | Ethical direction |
| Relational | Trophies as Feedback | | new_candidate | Process | Finished coins | tarot_semantic | Visible milestones |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_015 | apprentice_work | minor_pentacles_eight | trophies | Artist at work | When Eight of Pentacles shows craftsman diligently perfecting skill through practice | crafting | Waite #Eight_Pentacles |
| rel_pent_016 | skill_corruption | minor_pentacles_eight | cunning | Reversed | When Eight of Pentacles reversed indicates skill corrupted into cunning or fraud | corrupting | Waite #Eight_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_008 | "perhaps in the preparatory stage" | minor_pentacles_eight | Artist -> trophies -> preparatory | Eight = learning craft | High | Yes | rule_pent_eight_apprentice |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_skill_building | Diligent practice building competence | | sign_virgo, planet_mercury | workshop_dream, craft_dream | deliberate_practice | Preparatory stage |
<!-- L2.5_END -->

---

### Nine of Pentacles

**Source Text**:
> "A woman, with a bird upon her wrist, stands amidst a great abundance of grapevines in the garden of a manorial house. It is a wide domain, suggesting plenty in all things. Possibly it is her own possession and testifies to material well-being. Divinatory Meanings: Prudence, safety, success, accomplishment, certitude, discernment. Reversed: Roguery, deception, voided project, bad faith."

**Core**: **Self-Sufficient Abundance** – Woman with bird in vineyard garden of manorial house. **"Wide domain, plenty in all things. Possibly her own possession,"** testifies to **material well-being**. Prudence, safety, success, accomplishment, certitude. **Reversed**: Roguery, deception, voided project.

**Chinese**: **自给自足的丰盛**——女子持鸟在庄园葡萄园中。**"广阔领地，一切充裕。可能是她自己的财产"**，证明**物质安康**。谨慎、安全、成功、完成、确信。**逆位**：无赖、欺骗、失败计划。

**Narrative Snippets**:
- `[ns_waite_pent_025]` `[trigger: nine_pent_waite]` `[factor_trigger: waite_pentacles_nine]` `[role: 主干]` Nine of Pentacles = woman with bird in vineyard; wide domain, plenty in all things. → Core
- `[ns_waite_pent_026]` `[trigger: material_wellbeing]` `[factor_trigger: waite_pentacles_nine AND independence]` `[role: 条件分支]` "Possibly her own possession, testifies to material well-being"; prudence, success. → Meaning
- `[ns_waite_pent_027]` `[trigger: roguery_deception]` `[factor_trigger: waite_pentacles_nine AND reversal]` `[role: 条件分支]` Reversed: roguery, deception, voided project, bad faith. → Shadow

#### L2 Semantic Extraction

- **Theme**: Self‑sufficient abundance and refined independence—material well‑being on one’s own domain
- **Natural Attributes**:
  - Symbolism: Woman with bird on wrist standing amid abundant grapevines in the garden of a manorial house; wide domain, plenty in all things
  - Characteristics: Quiet, ordered, cultivated; grapes and estate indicate established wealth, comfort, and self-reliance
  - Elements: Prudence, safety, success, accomplishment, certitude, discernment; possibly her own possession testifying to material well-being
- **Functional Symbolism**:
  - Describes prudence, safety, success and personal accomplishment achieved through one's own efforts
  - Shows the enjoyment of cultivated wealth and independence—the fruit of disciplined work and wise management
  - Reversed, it points to roguery, deception, bad faith, and voided projects that undermine apparent security
- **Conditional Structure**:
  - **Necessary Conditions**: Established resources, estate, or accomplishments that can be enjoyed independently
  - **Enhancing Conditions**: Prudence, discernment, and continued attention to what sustains the abundance
  - **Nullifying Conditions**: Deception, bad faith, or roguery—internal or external threats that void projects and undermine security
- **Multi-layered Interpretation**:
  - Literal Layer: Financial independence, comfortable retirement, successful solo ventures, or enjoying the fruits of one's labour
  - Symbolic Layer: Archetype of the lady of the manor—refined, independent, surrounded by the wealth she has cultivated
  - Practical Layer: Encourages building toward self-sufficiency and enjoying what has been earned; warns against complacency
  - Psychological Layer: Inner sense of self-reliance, accomplishment, and the capacity to enjoy solitude without loneliness

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Nine of Pentacles | 星币九 | Woman with bird amid abundant vineyard and estate | 在丰盛葡萄园与庄园中的持鸟女子 | minor_pentacles_nine | existing |
| Her Own Possession | 她自己财产 | Estate possibly belonging to the woman herself | 可能属于该女子本人的领地与财产 | | new_candidate |
| Material Well-Being | 物质安康 | Condition of secure, comfortable material life | 物质生活安稳、舒适的状态 | | new_candidate |
| Wide Domain | 广阔领地 | Large estate indicating plenty in all things | 在万事充裕意义上的广大地产 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Nine of Pentacles | minor_pentacles_nine | existing | Tarot Card | Independent abundance | tarot_semantic | Solo figure |
| Functional | Independence & Comfort | | new_candidate | Life Area | Self-reliance, prudence | tarot_semantic | Personal wealth |
| State | Prudence vs Roguery | | new_candidate | Condition | Secure vs dishonest | tarot_semantic | Integrity |
| Relational | Woman-and-Bird | | new_candidate | Symbol | Refinement, freedom | tarot_semantic | Cultivated solitude |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_017 | self_sufficient | minor_pentacles_nine | wide_domain | Woman with bird | When Nine of Pentacles shows self-sufficient woman flourishing in her domain | flourishing | Waite #Nine_Pentacles |
| rel_pent_018 | own_possession | minor_pentacles_nine | material_wellbeing | Possibly hers | When Nine of Pentacles demonstrates material wellbeing through personal achievement | demonstrating | Waite #Nine_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_009 | "Possibly it is her own possession and testifies to material well-being" | minor_pentacles_nine | Wide domain -> her own -> well-being | Nine = independent prosperity | High | Yes | rule_pent_nine_independence |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_self_sufficient_abundance | Prosperity through own effort and prudence | | sign_virgo, planet_venus | vineyard_dream, bird_dream | self_actualization | Her own possession |
<!-- L2.5_END -->

---

### Ten of Pentacles

**Source Text**:
> "A man and woman beneath an archway which gives entrance to a house and domain. They are accompanied by a child, who looks curiously at two dogs accosting an ancient personage seated in the foreground. The child's hand is on one of them. Divinatory Meanings: Gain, riches; family matters, archives, extraction, the abode of a family. Reversed: Chance, fatality, loss, robbery, games of hazard; sometimes gift, dowry, pension."

**Core**: **Family Legacy & Generational Wealth** – Man/woman/child at archway entrance, ancient personage seated, dogs. Gain, riches; **family matters, archives, extraction, abode of family** (generational continuity). **Reversed**: Chance, fatality, loss, robbery, gambling; or gift/dowry/pension.

**Chinese**: **家族遗产与世代财富**——男/女/孩在拱门入口，古老人物坐着，狗。收益、财富；**家族事务、档案、出身、家族住所**（世代延续）。**逆位**：机会、宿命、损失、抢劫、赌博；或礼物/嫁妆/养老金。

**Narrative Snippets**:
- `[ns_waite_pent_028]` `[trigger: ten_pent_waite]` `[factor_trigger: waite_pentacles_ten]` `[role: 主干]` Ten of Pentacles = family at archway; ancient personage; dogs; generational wealth. → Core
- `[ns_waite_pent_029]` `[trigger: family_legacy]` `[factor_trigger: waite_pentacles_ten AND lineage]` `[role: 条件分支]` Family matters, archives, extraction, abode of family—legacy and continuity. → Meaning
- `[ns_waite_pent_030]` `[trigger: chance_fatality]` `[factor_trigger: waite_pentacles_ten AND reversal]` `[role: 条件分支]` Reversed: chance, fatality, loss, robbery, games of hazard; or gift/dowry/pension. → Volatility

#### L2 Semantic Extraction

- **Theme**: Family legacy and generational continuity—wealth embedded in lineage, home, and archives
- **Natural Attributes**:
  - Symbolism: Man, woman, and child beneath an archway entrance to a house and domain; ancient personage seated in foreground with two dogs; child's hand on one dog
  - Characteristics: Multi-generational, domestic, rooted; dogs, child, and elder show continuity across time
  - Elements: Gain, riches, family matters, archives, extraction (lineage), the abode of a family
- **Functional Symbolism**:
  - Concerns gain, riches, family matters, ancestry, and the abode of the family—wealth that spans generations
  - Shows the archway as threshold between public and private, past and future, individual and lineage
  - Reversed, it swings toward chance, fatality, loss, robbery, or games of hazard that threaten inherited wealth
- **Conditional Structure**:
  - **Necessary Conditions**: Family, lineage, or community with resources that can be passed down or shared
  - **Enhancing Conditions**: Responsible stewardship, honouring elders, investing in the next generation
  - **Nullifying Conditions**: Gambling, robbery, loss, or fatality that disrupts the transmission of wealth and belonging
- **Multi-layered Interpretation**:
  - Literal Layer: Inheritances, family businesses, ancestral homes, pensions, or dowries that connect generations
  - Symbolic Layer: Archetype of the family estate—wealth not as individual possession but as lineage's treasure
  - Practical Layer: Encourages thinking about legacy, estate planning, and multi-generational wellbeing
  - Psychological Layer: Sense of belonging, roots, and continuity; shadow shown when inheritance becomes burden or conflict

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Ten of Pentacles | 星币十 | Family scene at archway with elder, couple, child and dogs | 拱门前有长者、夫妇、孩童与犬的家族场景 | minor_pentacles_ten | existing |
| Family Archives / Extraction | 家族档案 / 出身 | Records and lineage of a family over time | 家族随时间积累的记录与血统 | | new_candidate |
| Abode of Family | 家族住所 | House and domain where the family dwells | 家族居住的房屋与领地 | | new_candidate |
| Generational Wealth | 世代财富 | Riches and resources passed through generations | 代代相承的财富与资源 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ten of Pentacles | minor_pentacles_ten | existing | Tarot Card | Family domain | tarot_semantic | End of number cycle |
| Functional | Legacy & Inheritance | | new_candidate | Life Area | Estate, ancestry | tarot_semantic | Gain, riches |
| State | Stable Lineage vs Hazard | | new_candidate | Condition | Secure vs gambling | tarot_semantic | Fate vs stewardship |
| Relational | Generational Continuum | | new_candidate | Process | Child-parents-elder | tarot_semantic | Ancestry/karma |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_019 | family_legacy | minor_pentacles_ten | archway | Man woman child | When Ten of Pentacles shows family receiving legacy at entrance to ancestral domain | inheriting | Waite #Ten_Pentacles |
| rel_pent_020 | generational | minor_pentacles_ten | elder | Ancient personage | When Ten of Pentacles elder figure connects generations through inherited wealth | connecting | Waite #Ten_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_010 | "family matters, archives, extraction, the abode of a family" | minor_pentacles_ten | Archway -> family -> legacy | Ten = generational wealth | High | Yes | rule_pent_ten_legacy |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_family_legacy | Wealth embedded in lineage and home | | sign_capricorn, planet_saturn | family_dream, archway_dream | generational_transmission | Family archives |
<!-- L2.5_END -->

---

**✅ Pentacles Number Cards Complete (10/14)**

---

## Pentacles Court Cards

### Page of Pentacles

**Source Text**:
> "A youthful figure, looking intently at the pentacle which hovers over his raised hands. He moves slowly, insensible of that which is about him. Divinatory Meanings: Application, study, scholarship, reflection another reading says news, messages and the bringer thereof; also rule, management. Reversed: Prodigality, dissipation, liberality, luxury; unfavourable news."

**Core**: **Studious Focus** – Youth looks intently at pentacle hovering over raised hands. **"Moves slowly, insensible of that about him"** (absorbed). Application, study, scholarship, reflection; or news/messages; rule/management. **Reversed**: Prodigality, dissipation, luxury, unfavorable news.

**Chinese**: **好学专注**——青年专注看悬浮于举手上的星币。**"缓慢移动，对周围无感"**（沉浸）。应用、学习、奖学金、反思；或消息；规则/管理。**逆位**：挥霍、放荡、奢侈、不利消息。

**Narrative Snippets**:
- `[ns_waite_pent_031]` `[trigger: page_pent_waite]` `[factor_trigger: waite_pentacles_page]` `[role: 主干]` Page of Pentacles = youth looking at hovering pentacle; "insensible of surroundings". → Core
- `[ns_waite_pent_032]` `[trigger: application_study]` `[factor_trigger: waite_pentacles_page AND scholarship]` `[role: 条件分支]` Application, study, scholarship, reflection; also news, messages, rule, management. → Meaning
- `[ns_waite_pent_033]` `[trigger: prodigality]` `[factor_trigger: waite_pentacles_page AND reversal]` `[role: 条件分支]` Reversed: prodigality, dissipation, liberality, luxury; unfavourable news. → Shadow

#### L2 Semantic Extraction

- **Theme**: Focused study and practical application—attention fixed on a single material or learning goal
- **Natural Attributes**:
  - Symbolism: Youthful figure looking intently at a pentacle hovering over raised hands, moving slowly, insensible of surroundings
  - Characteristics: Slow, absorbed, grounded; moves carefully, so focused as to be unaware of distractions
  - Elements: Application, study, scholarship, reflection; also news, messages, and the bringer thereof; rule, management
- **Functional Symbolism**:
  - Represents a student, apprentice, or messenger concerned with study, scholarship, and management in the material world
  - Shows the value of deep concentration and practical application of knowledge
  - Reversed, it tips into prodigality, dissipation, luxury, and unfavourable or disappointing messages
- **Conditional Structure**:
  - **Necessary Conditions**: A subject, skill, or material matter worthy of concentrated study and application
  - **Enhancing Conditions**: Discipline, patience, and environments that support focused learning
  - **Nullifying Conditions**: Prodigality, dissipation, or distraction that scatters energy and leads to wasted potential
- **Multi-layered Interpretation**:
  - Literal Layer: Students, apprentices, scholarship applications, practical study, or news about material matters
  - Symbolic Layer: Archetype of the young scholar—absorbed in contemplation of practical mysteries
  - Practical Layer: Encourages deep focus, practical study, and patient application of knowledge
  - Psychological Layer: Capacity for concentration and absorption; shadow shown when focus becomes obsession or luxury scatters attention

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Page of Pentacles | 星币侍从 | Youth intently contemplating a hovering pentacle | 专注凝视悬浮星币的青年侍从 | minor_pentacles_page | existing |
| Insensible of Surroundings | 对周围无感 | So absorbed in focus as to ignore the environment | 因过度专注而几乎不觉周遭环境 | | new_candidate |
| Hovering Pentacle | 悬浮星币 | Pentacle suspended over raised hands, symbol of study-object | 悬于举起双手之上的星币，象征被专注研究的对象 | | new_candidate |
| Application & Study | 应用与学习 | Practical use of knowledge joined with disciplined learning | 知识的实际运用与有纪律的学习相结合 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Page of Pentacles | minor_pentacles_page | existing | Tarot Card | Young Earth student | tarot_semantic | Court Page |
| Functional | Study & Practical Learning | | new_candidate | Life Area | Education, training | tarot_semantic | Brings news |
| State | Focused vs Squandered | | new_candidate | Condition | Concentrated vs prodigal | tarot_semantic | Energy use |
| Relational | Earth Student Archetype | | new_candidate | Archetype | Diligent learner | tarot_semantic | Bridge to apprentices |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_021 | studious_focus | minor_pentacles_page | hovering_pentacle | Looks intently | When Page of Pentacles gazes intently at pentacle oblivious to surroundings | concentrating | Waite #Page_Pentacles |
| rel_pent_022 | application | minor_pentacles_page | study | Scholarship | When Page of Pentacles applies scholarship and reflection to practical learning | learning | Waite #Page_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_011 | "looking intently at the pentacle which hovers over his raised hands" | minor_pentacles_page | Looks -> hovers -> absorbed | Page = focused student | High | Yes | rule_pent_page_study |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_focused_study | Deep concentration on practical learning | | sign_virgo, planet_mercury | study_dream, coin_dream | flow_state | Insensible of surroundings |
<!-- L2.5_END -->

---

### Knight of Pentacles

**Source Text**:
> "He rides a slow, enduring, heavy horse, to which his own aspect corresponds. He exhibits his symbol, but does not look therein. Divinatory Meanings: Utility, serviceableness, interest, responsibility, rectitude-all on the normal and external plane. Reversed: inertia, idleness, repose of that kind, stagnation; also placidity, discouragement, carelessness."

**Core**: **Slow & Steady** – Rides **slow, enduring, heavy horse**, to which he corresponds. Exhibits pentacle but **"does not look therein"** (practical not visionary). Utility, serviceableness, responsibility, rectitude **"on normal and external plane."** **Reversed**: Inertia, idleness, stagnation, placidity, discouragement.

**Chinese**: **缓慢稳定**——骑**缓慢、持久、重马**，与其相应。展示星币但**"不看其中"**（实用非有远见）。实用、有用、责任、正直**"在正常外在层面"**。**逆位**：惰性、懒惰、停滞、平静、沮丧。

**Narrative Snippets**:
- `[ns_waite_pent_034]` `[trigger: knight_pent_waite]` `[factor_trigger: waite_pentacles_knight]` `[role: 主干]` Knight of Pentacles = slow, enduring, heavy horse; "does not look therein". → Core
- `[ns_waite_pent_035]` `[trigger: utility_rectitude]` `[factor_trigger: waite_pentacles_knight AND duty]` `[role: 条件分支]` Utility, serviceableness, responsibility, rectitude—"on normal and external plane". → Meaning
- `[ns_waite_pent_036]` `[trigger: inertia_stagnation]` `[factor_trigger: waite_pentacles_knight AND reversal]` `[role: 条件分支]` Reversed: inertia, idleness, stagnation, placidity, discouragement, carelessness. → Shadow

#### L2 Semantic Extraction

- **Theme**: Persistence and pragmatic service—slow, enduring effort on the external, practical plane
- **Natural Attributes**:
  - Symbolism: Knight riding a slow, enduring, heavy horse to which his own aspect corresponds; exhibits pentacle but does not look therein
  - Characteristics: Heavy, steady, methodical; more concerned with doing the work than with contemplating the symbol
  - Elements: Utility, serviceableness, interest, responsibility, rectitude—all on the normal and external plane
- **Functional Symbolism**:
  - Indicates responsibility, reliability, and usefulness in everyday matters—work, chores, routines
  - Shows practical service without vision or inspiration—getting the job done rather than seeking meaning in it
  - Reversed, it tips into inertia, idleness, stagnation, placidity, discouragement, and carelessness
- **Conditional Structure**:
  - **Necessary Conditions**: Tasks, duties, or responsibilities that require steady, reliable effort over time
  - **Enhancing Conditions**: Patience, endurance, and willingness to do unglamorous work without complaint
  - **Nullifying Conditions**: Inertia, idleness, stagnation, or discouragement that stops progress and wastes potential
- **Multi-layered Interpretation**:
  - Literal Layer: Reliable employees, steady workers, routine maintenance, or slow but sure progress on practical projects
  - Symbolic Layer: Archetype of the patient worker—the knight who advances through endurance rather than speed
  - Practical Layer: Encourages persistence, reliability, and acceptance of slow progress; warns against lethargy
  - Psychological Layer: Inner steadiness and capacity for sustained effort; shadow shown when patience becomes stagnation

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Knight of Pentacles | 星币骑士 | Rider on slow, enduring, heavy horse | 骑乘缓慢、持久、沉重之马的骑士 | minor_pentacles_knight | existing |
| Slow / Enduring / Heavy Horse | 缓慢 / 持久 / 重马 | Mount that emphasises patience and staying power | 象征耐心与持久力的坐骑 | | new_candidate |
| Does Not Look Therein | 不看其中 | Exhibits symbol without gazing into it (practical not visionary) | 展示符号却不凝视其中（重实用而非远见） | | new_candidate |
| Normal External Plane | 正常外在层面 | Ordinary, outer-world sphere of duties and utility | 日常外在事务与功用所在的层面 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Knight of Pentacles | minor_pentacles_knight | existing | Tarot Card | Patient worker | tarot_semantic | Court Knight |
| Functional | Duty & Practical Service | | new_candidate | Life Role | Obligations, labour | tarot_semantic | Reliability |
| State | Steady vs Stagnant | | new_candidate | Condition | Slow but sure vs idle | tarot_semantic | Pace |
| Relational | Earth Knight Archetype | | new_candidate | Archetype | Hard-working provider | tarot_semantic | Contrast to fiery |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_023 | slow_steady | minor_pentacles_knight | heavy_horse | Rides slow | When Knight of Pentacles rides slow heavy horse demonstrating patient persistence | persisting | Waite #Knight_Pentacles |
| rel_pent_024 | not_visionary | minor_pentacles_knight | does_not_look | Exhibits pentacle | When Knight of Pentacles focuses on practical execution not visionary contemplation | executing | Waite #Knight_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_012 | "He rides a slow, enduring, heavy horse, to which his own aspect corresponds" | minor_pentacles_knight | Slow -> enduring -> corresponds | Knight = patient worker | High | Yes | rule_pent_knight_steady |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_patient_service | Slow, reliable fulfilment of duties | | sign_taurus, planet_saturn | horse_dream, slow_dream | conscientiousness | Does not look therein |
<!-- L2.5_END -->

---

### Queen of Pentacles

**Source Text**:
> "The face suggests that of a dark woman, whose qualities might be summed up in the idea of greatness of soul; she has also the serious cast of intelligence; she contemplates her symbol and may see worlds therein. Divinatory Meanings: Opulence, generosity, magnificence, security, liberty. Reversed: Evil, suspicion, suspense, fear, mistrust."

**Core**: **Greatness of Soul & Worlds Therein** – Dark woman, **"greatness of soul,"** serious intelligence. **"Contemplates her symbol and may see worlds therein"** (visionary with material). Opulence, generosity, magnificence, security, liberty. **Reversed**: Evil, suspicion, fear, mistrust.

**Chinese**: **灵魂伟大与其中世界**——深色女性，**"灵魂伟大"**，严肃智慧。**"凝视其符号，可能在其中见世界"**（有物质的远见）。富裕、慷慨、壮丽、安全、自由。**逆位**：邪恶、怀疑、恐惧、不信任。

**Narrative Snippets**:
- `[ns_waite_pent_037]` `[trigger: queen_pent_waite]` `[factor_trigger: waite_pentacles_queen]` `[role: 主干]` Queen of Pentacles = dark woman; "greatness of soul"; "may see worlds therein". → Core
- `[ns_waite_pent_038]` `[trigger: opulence_generosity]` `[factor_trigger: waite_pentacles_queen AND abundance]` `[role: 条件分支]` Opulence, generosity, magnificence, security, liberty. → Meaning
- `[ns_waite_pent_039]` `[trigger: suspicion_mistrust]` `[factor_trigger: waite_pentacles_queen AND reversal]` `[role: 条件分支]` Reversed: evil, suspicion, suspense, fear, mistrust. → Shadow

#### L2 Semantic Extraction

- **Theme**: Greatness of soul in the material realm—seeing "worlds" within practical symbols and resources
- **Natural Attributes**:
  - Symbolism: Dark woman of greatness of soul with serious cast of intelligence, contemplating her symbol and perhaps seeing worlds therein
  - Characteristics: Warm, generous, intelligent; able to hold both opulence and security with inner depth and vision
  - Elements: Opulence, generosity, magnificence, security, liberty
- **Functional Symbolism**:
  - Symbolises a nurturing, materially capable woman (or attitude) who provides safety, liberty, and generosity
  - Shows the capacity to perceive deeper meaning in material resources—not just possessing but understanding
  - Reversed, it turns to evil, suspicion, suspense, fear, and mistrust about security and resources
- **Conditional Structure**:
  - **Necessary Conditions**: Material resources and the capacity for generous, intelligent stewardship
  - **Enhancing Conditions**: Greatness of soul, serious intelligence, and willingness to see worlds within the practical
  - **Nullifying Conditions**: Suspicion, fear, mistrust, or evil that corrupts generosity into hoarding or manipulation
- **Multi-layered Interpretation**:
  - Literal Layer: Generous benefactors, nurturing providers, successful businesswomen, or caretakers who offer security and liberty
  - Symbolic Layer: Archetype of the Earth Queen—magnanimous, visionary in the material realm, seeing worlds in her symbol
  - Practical Layer: Encourages generous, intelligent management of resources; warns against fear-based hoarding
  - Psychological Layer: Capacity for nurturing abundance and inner richness; shadow shown when fear corrupts generosity

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Queen of Pentacles | 星币王后 | Dark woman of greatness of soul contemplating her symbol | 凝视其符号、具灵魂伟大的深色王后 | minor_pentacles_queen | existing |
| Greatness of Soul | 灵魂伟大 | Magnanimity and depth of character expressed in care | 通过关照与承载体现出的宽广深厚品格 | | new_candidate |
| See Worlds Therein | 在其中见世界 | Capacity to perceive many worlds in a single symbol | 能在单一符号中看见多重世界的能力 | | new_candidate |
| Opulence & Security | 富裕与安全 | State of abundant yet stable material life | 既丰盛又稳固的物质生活状态 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Queen of Pentacles | minor_pentacles_queen | existing | Tarot Card | Nurturing abundance | tarot_semantic | Court Queen |
| Functional | Material Care & Generosity | | new_candidate | Life Role | Providing, hosting | tarot_semantic | Earth-mother |
| State | Trust vs Suspicion | | new_candidate | Condition | Generous vs fearful | tarot_semantic | Emotional stance |
| Relational | Worlds-in-Symbol | | new_candidate | Symbol | Matter to imagination | tarot_semantic | Visionary Earth |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_025 | greatness_soul | minor_pentacles_queen | contemplates | Dark woman | When Queen of Pentacles dark woman contemplates with serious nurturing intelligence | nurturing | Waite #Queen_Pentacles |
| rel_pent_026 | see_worlds | minor_pentacles_queen | tarot_infinity_symbol | May see | When Queen of Pentacles may perceive worlds within the pentacle symbol | visioning | Waite #Queen_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_013 | "she contemplates her symbol and may see worlds therein" | minor_pentacles_queen | Contemplates -> sees worlds -> visionary | Queen = visionary nurturer | High | Yes | rule_pent_queen_vision |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_nurturing_vision | Greatness of soul seeing worlds in matter | | sign_taurus, planet_venus | queen_dream, garden_dream | maternal_generosity | See worlds therein |
<!-- L2.5_END -->

---

### King of Pentacles

**Source Text**:
> "The figure calls for no special description the face is rather dark, suggesting also courage, but somewhat lethargic in tendency. The bull's head should be noted as a recurrent symbol on the throne. The sign of this suit is represented throughout as engraved or blazoned with the pentagram, typifying the correspondence of the four elements in human nature and that by which they may be governed. In many old Tarot packs this suit stood for current coin, money, deniers. I have not invented the substitution of pentacles and I have no special cause to sustain in respect of the alternative. But the consensus of divinatory meanings is on the side of some change, because the cards do not happen to deal especially with questions of money. Divinatory Meanings: Valour, realizing intelligence, business and normal intellectual aptitude, sometimes mathematical gifts and attainments of this kind; success in these paths. Reversed: Vice, weakness, ugliness, perversity, corruption, peril."

**Core**: **Bull Symbol & Governing Elements** – Dark face, courage but **"somewhat lethargic."** **Bull's head recurrent on throne**. Waite explains: **"Pentagram typifies correspondence of four elements in human nature and that by which they may be governed"** (not just money). Valour, **realizing intelligence**, business aptitude, mathematical gifts; success. **Reversed**: Vice, weakness, perversity, corruption.

**Chinese**: **公牛符号与治理元素**——深色脸，勇气但**"有些懒惰"**。**公牛头在王座反复出现**。韦特解释：**"五芒星象征人类本性中四元素对应及其治理之道"**（非仅金钱）。勇气、**实现智慧**、商业才能、数学天赋；成功。**逆位**：邪恶、软弱、变态、腐败。

**Narrative Snippets**:
- `[ns_waite_pent_040]` `[trigger: king_pent_waite]` `[factor_trigger: waite_pentacles_king]` `[role: 主干]` King of Pentacles = dark face, bull's head; pentagram governs four elements in human nature. → Core
- `[ns_waite_pent_041]` `[trigger: realizing_intelligence]` `[factor_trigger: waite_pentacles_king AND aptitude]` `[role: 条件分支]` Valour, realizing intelligence, business aptitude, mathematical gifts; success. → Meaning
- `[ns_waite_pent_042]` `[trigger: vice_corruption]` `[factor_trigger: waite_pentacles_king AND reversal]` `[role: 条件分支]` Reversed: vice, weakness, ugliness, perversity, corruption, peril. → Shadow

#### L2 Semantic Extraction

- **Theme**: Earthly rulership and governance of elements—material king who understands how four elements correspond in human nature
- **Natural Attributes**:
  - Symbolism: Dark-faced king with bull's head recurring on throne, holding pentacle, solid and somewhat heavy in aspect
  - Characteristics: Solid, courageous yet tending to lethargy; bull symbolism suggests strength, endurance, and earthly power
  - Elements: Valour, realizing intelligence, business and normal intellectual aptitude, mathematical gifts; pentagram typifies correspondence of four elements and their governance
- **Functional Symbolism**:
  - Represents valour, business, and intellectual aptitude, especially in mathematical or structural fields
  - Governs material systems, enterprises, and resources with "realizing intelligence"—the capacity to make plans real
  - Waite notes pentacles are not just about money but about the governance of elements in human nature
- **Conditional Structure**:
  - **Necessary Conditions**: Material domain, enterprise, or structure requiring wise governance and practical intelligence
  - **Enhancing Conditions**: Valour, business aptitude, mathematical or structural thinking, and steady application of power
  - **Nullifying Conditions**: Vice, corruption, weakness, perversity, or peril arising from misused material power
- **Multi-layered Interpretation**:
  - Literal Layer: Successful businessmen, property owners, financial managers, or those who govern material enterprises
  - Symbolic Layer: Archetype of the Earth King—bull-throned ruler who governs the four elements in human nature through realizing intelligence
  - Practical Layer: Encourages responsible, intelligent governance of material resources; warns against corruption and lethargy
  - Psychological Layer: Inner capacity for material mastery and self-governance; shadow shown when power becomes vice or strength becomes inertia

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| King of Pentacles | 星币国王 | Dark-faced king with bull motifs governing elements | 以公牛意象统摄元素的深色国王 | minor_pentacles_king | existing |
| Bull's Head | 公牛头 | Symbol of strength, endurance and earthy authority | 象征力量、持久与大地权威的牛头图像 | | new_candidate |
| Realizing Intelligence | 实现智慧 | Capacity to make plans and structures real in the world | 将计划与结构在现实中落实的智慧 | | new_candidate |
| Governing Four Elements | 治理四元素 | Pentagram's power to order Fire, Water, Air, Earth in human nature | 五芒星在人的本性中统摄火水气土的力量 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | King of Pentacles | minor_pentacles_king | existing | Tarot Card | Elemental governor | tarot_semantic | Court King |
| Functional | Governance & Realisation | | new_candidate | Life Role | Managing businesses | tarot_semantic | Realising intelligence |
| State | Steady Power vs Corruption | | new_candidate | Condition | Valour vs vice | tarot_semantic | Ethical quality |
| Relational | Pentagram-Four Elements | | new_candidate | Symbol | Elemental correspondence | tarot_semantic | Bridges philosophy |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_pent_027 | bull_authority | minor_pentacles_king | bull_head | Recurrent symbol | When King of Pentacles bull head motif grounds authority in Taurian earth | grounding | Waite #King_Pentacles |
| rel_pent_028 | four_elements | minor_pentacles_king | pentagram | Typifies correspondence | When King of Pentacles pentagram governs four elements in human nature | governing | Waite #King_Pentacles |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_pent_014 | "the pentagram, typifying the correspondence of the four elements in human nature and that by which they may be governed" | minor_pentacles_king | Pentagram -> four elements -> governed | King = elemental governor | High | Yes | rule_pent_king_governance |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_elemental_governance | Mastery over four elements in human nature | | sign_taurus, planet_saturn | king_dream, bull_dream | ego_mastery | Governing four elements |
<!-- L2.5_END -->

---

**🎉 PENTACLES SUIT COMPLETE (14/14)**

---

**🏆 WAITE PICTORIAL KEY TO THE TAROT 100% COMPLETE! 🏆**

> **Final Achievement**: 92/92张牌完成 (100%)  
> - ✅ Major Arcana: 22/22  
> - ✅ Minor Arcana Wands: 14/14  
> - ✅ Minor Arcana Cups: 14/14  
> - ✅ Minor Arcana Swords: 14/14  
> - ✅ Minor Arcana Pentacles: 14/14  
>  
> **Total Terms**: 272双语术语 (Major 110 + Minor 162)  
> **Format**: L1+L2 Bilingual v2.1  
> **Status**: Book COMPLETE - Ready for next book!

---
