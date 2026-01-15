# The Book of Thoth - Appendices (L1+L2)

> **Author**: Aleister Crowley  
> **Source**: The Book of Thoth (1944), Appendices A & B  
> **Refinement Date**: 2025-11-30  
> **Template**: 典籍精校模板_L1L2_v2 + 西方文本模板  
> **Note**: Content paraphrased in modern language, preserving core concepts

---

## Appendix A: The Behaviour of the Tarot (塔罗牌的行为)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Behaviour | Card interaction patterns | Experiential knowledge |
| Divination | Practical card use | Primary learning method |
| Significator | Card representing Querent | Reading anchor |
| Operations | Divination stages | Five-step process |

**Source Text**:
> "The position of the student of the Tarot is very similar. In this essay, and in these designs, is given an analysis of the general character of each card; but he cannot reach any true appreciation of them without observing their behaviour over a long period; he can only come to an understanding of the Tarot through experience. It will not be sufficient for him to intensify his studies of the cards as objective things; he must use them; he must live with them. They, too, must live with him. A card is not isolated from its fellows. The reactions of the cards, their interplay with each other, must be built into the very life of the student."

**English Paraphrase**:

Crowley emphasizes that **intellectual study alone is insufficient**—the Tarot must be **experienced through use**:

**Core Principle**:
- Cards are **living entities** with distinct "behaviours"
- Understanding comes from **observing interactions** over time
- The student must **live with the cards**—they become part of daily consciousness
- **Divination is the practical method** for most students (vs. contemplation for advanced initiates)

**Why Divination?**
The ideal way to know the cards is through high-level contemplation, but this requires advanced initiation. For most people, **practical divination** is the accessible path. Through repeated readings, the cards reveal their characters through their **interactions and relationships**.

**完整中文诠释**：

Crowley强调**单纯的智力学习是不够的**——塔罗必须**通过使用来体验**：

**核心原则**：
- 牌是具有独特"行为"的**活体存在**
- 理解来自于长期**观察互动**
- 学生必须**与牌共同生活**——它们成为日常意识的一部分
- **占卜是实践方法**，适合大多数学生（而非高级启蒙者的冥想）

**为何占卜？**
认识牌的理想方式是通过高层次冥想，但这需要高级启蒙。对大多数人来说，**实践占卜**是可及的路径。通过反复的解读，牌通过它们的**互动和关系**展现其特性。

#### Core Points

- **Experiential learning**: Tarot cannot be mastered through intellectual study alone—practical use is essential.
- **Living entities**: Cards have distinct "behaviours" that reveal themselves through interaction.
- **Divination as method**: For most students, divination is the accessible path to understanding (vs. advanced contemplation).
- **Interplay**: A card's meaning emerges from its **relationships with other cards**, not in isolation.
- **Time requirement**: True appreciation requires observing card behaviour over a **long period**.

**Narrative Snippets**:
- `[ns_thoth_app_001]` `[trigger: card_behaviour]` `[factor_trigger: tarot_behaviour AND tarot_experience]` `[role: 主干]` The student cannot reach true appreciation of the cards without observing their behaviour over a long period through experience. → Source Text
- `[ns_thoth_app_002]` `[trigger: divination_method]` `[factor_trigger: tarot_divination AND tarot_learning]` `[role: 主干依赖]` The practical every-day commonplace way to learn the Tarot is divination. → Source Text
- `[ns_thoth_app_009]` `[trigger: living_cards]` `[factor_trigger: tarot_cards AND tarot_interaction]` `[role: 条件分支]` A card is not isolated from its fellows—the reactions and interplay of the cards must be built into the very life of the student. → Living Entities
- `[ns_thoth_app_010]` `[trigger: experiential_path]` `[factor_trigger: tarot_experience AND tarot_contemplation]` `[role: 条件分支]` Divination is the accessible path for most students; advanced contemplation requires higher initiation. → Levels

<!-- L1_END -->

<!-- L2_BEGIN -->

#### L2 Semantic Extraction
- **Theme**: Experiential learning through divination as the practical path to Tarot mastery
- **Natural Attributes**:
  - Symbolism: Cards as living beings with behaviours
  - Characteristics: Interactive, relational, time-requiring
  - Elements: Repeated use, pattern observation, intuitive integration
- **Functional Symbolism**:
  - Learning: Experience > Theory
  - Relationship: Student ↔ Cards (bidirectional)
  - Method: Divination as accessible contemplation
- **Multi-layered Interpretation**:
  - Practical Layer: Daily use, readings, record-keeping
  - Relational Layer: Card-to-card interactions, positional meanings
  - Psychological Layer: Building intuitive connection
  - Initiatory Layer: Divination as lesser mystery, contemplation as greater

<!-- L2_END -->

<!-- FACTOR_BEGIN -->

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Method | Divination | divination_method | existing | Learning path | Practical | tarot_calculator | Primary |
| Concept | Card Behaviour | card_behaviour | new_candidate | Observable | Interactive | tarot_semantic | Key insight |
| Process | Experiential Learning | exp_learning | new_candidate | Pedagogy | Time-based | tarot_semantic | Crowley emphasis |
| Relation | Card Interplay | card_interplay | new_candidate | Reading dynamics | Contextual | tarot_semantic | Essential |

<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_exp_div | method | exp_learning | divination_method | Implementation | When experiential learning bridges theoretical study to practical divination | Study→Practice | Thoth Appendix A |
| rel_behav_inter | manifestation | card_behaviour | card_interplay | Observable | When card behavior and interplay manifest observable patterns in reading | Character→Pattern | Thoth Appendix A |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| card_behaviour | Living symbolism | 神煞活性 | Planet behaviour | 活象征 | Active imagination | Experiential |
<!-- L2.5_END -->

---

## Appendix A: The Five Operations (五步操作法)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Significator | Querent's representative card | Reading anchor |
| YHVH Stacks | Four piles for IHVH | Question domain |
| Twelve Houses | Astrological divisions | Development context |
| Tree of Life | Ten Sephirotic piles | Final outcome |
| Counting | Card-to-card progression | Narrative building |

**Source Text**:
> "Choose a card to represent the Querent, using your knowledge or judgment of his character rather than dwelling on his physical characteristics. ... Hand the cards to Querent, and bid him think of the question attentively, and cut."

**English Paraphrase**:

The **Golden Dawn divination method** as taught by Crowley involves **Five Operations**:

**Preparation**:
1. **Choose a Significator**: Select a Court Card representing the Querent based on **character/personality**, not physical appearance
2. **Invocation**: "I invoke thee, I A O, that thou wilt send H R U, the great Angel..."
3. **Querent cuts**: While focusing on the question

**The Five Operations**:

**Operation I: The Situation**
- Cut into 4 stacks representing **YHVH** (from right to left)
- Find Significator—its stack reveals the **question's domain**:
  - **Yod (י)**: Work, business
  - **Heh (ה)**: Love, marriage, pleasure
  - **Vav (ו)**: Trouble, loss, quarrel
  - **Heh-final (ה)**: Money, material matters
- **Count and pair** cards around Significator to build the story

**Operation II: Development**
- Deal into **12 stacks** for the **12 astrological houses**
- Find Significator in expected house (7th for marriage, etc.)
- Read the stack's narrative

**Operation III: Further Development**
- Deal into **12 stacks** for the **12 zodiac signs**
- Continue the narrative

**Operation IV: Penultimate Aspects**
- Place Significator in center
- Form a **ring of 36 cards** (36 decans) around it
- Count and pair

**Operation V: Final Result**
- Deal into **10 piles** in the form of the **Tree of Life**
- Find Significator and read final outcome

**完整中文诠释**：

Crowley教授的**金色黎明占卜法**包含**五步操作**：

**准备**：
1. **选择Significator**：基于**性格/个性**而非外貌选择代表求问者的宫廷牌
2. **祈祷**："我召唤你，I A O，请派遣H R U，伟大的天使..."
3. **求问者切牌**：同时专注于问题

**五步操作**：

**操作一：情境**
- 切成4堆代表**YHVH**（从右到左）
- 找到Significator——其所在堆显示**问题的领域**：
  - **Yod（י）**：工作、事业
  - **Heh（ה）**：爱情、婚姻、愉悦
  - **Vav（ו）**：麻烦、损失、争吵
  - **Heh-final（ה）**：金钱、物质事务
- **计数并配对**Significator周围的牌以构建故事

**操作二：发展**
- 发成**12堆**对应**12占星宫位**
- 在预期宫位找Significator（婚姻找第7宫等）
- 阅读该堆的叙事

**操作三：进一步发展**
- 发成**12堆**对应**12星座**
- 继续叙事

**操作四：倒数第二面向**
- 将Significator放在中心
- 围绕它形成**36张牌的环**（36旬）
- 计数并配对

**操作五：最终结果**
- 发成**10堆**按**生命之树**形状
- 找到Significator并阅读最终结果

#### Core Points

- **Significator selection**: Based on **personality**, not physical appearance.
- **YHVH stacks** reveal the **domain** of the question (work/love/trouble/money).
- **Counting rules**: Knights/Queens/Princes=4, Princesses=7, Aces=11, Pips=number, Trumps=3/9/12 (elemental/planetary/zodiacal).
- **Five Operations** progressively deepen: Situation → Development → Further Development → Penultimate → Final.
- **Tree of Life spread** (Operation V) gives the **ultimate outcome**.

**Narrative Snippets**:
- `[ns_thoth_app_003]` `[trigger: significator]` `[factor_trigger: tarot_significator AND tarot_querent]` `[role: 主干]` Choose a Significator based on knowledge of the Querent's character rather than physical characteristics. → Source Text
- `[ns_thoth_app_004]` `[trigger: yhvh_stacks]` `[factor_trigger: tarot_yhvh AND tarot_domain]` `[role: 主干依赖]` The four stacks represent YHVH—Yod for work, Heh for love, Vav for trouble, Heh-final for money. → Source Text
- `[ns_thoth_app_011]` `[trigger: five_operations]` `[factor_trigger: tarot_divination AND tarot_progressive]` `[role: 条件分支]` Five Operations progressively deepen: Situation → Development → Further Development → Penultimate → Final Result. → Method
- `[ns_thoth_app_012]` `[trigger: tree_final]` `[factor_trigger: tarot_tree AND tarot_outcome]` `[role: 条件分支]` Operation V deals into 10 piles in the form of the Tree of Life—this gives the ultimate outcome. → Final

<!-- L1_END -->

<!-- L2_BEGIN -->

#### L2 Semantic Extraction
- **Theme**: Five-Operation divination method integrating YHVH, astrology, and Qabalah
- **Natural Attributes**:
  - Symbolism: YHVH stacks, 12 houses, 12 signs, 36 decans, Tree of Life
  - Characteristics: Progressive, integrative, multi-system
  - Elements: Significator, counting, pairing, storytelling
- **Functional Symbolism**:
  - Domain identification: YHVH → question type
  - Development tracking: Houses → Signs → Decans → Tree
  - Narrative building: Counting and pairing create story
- **Multi-layered Interpretation**:
  - Structural Layer: Five operations as progressive depth
  - Qabalistic Layer: YHVH, Tree of Life
  - Astrological Layer: 12 Houses, 12 Signs, 36 Decans
  - Practical Layer: Counting rules, pairing technique

<!-- L2_END -->

<!-- FACTOR_BEGIN -->

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Method | Five Operations | five_ops | new_candidate | Divination structure | Sequential | tarot_calculator | Golden Dawn |
| Spread | YHVH Stacks | yhvh_spread | new_candidate | Operation I | 4 piles | tarot_calculator | Domain |
| Spread | House Spread | house_spread | new_candidate | Operation II | 12 piles | tarot_calculator | Development |
| Spread | Tree Spread | tree_spread | new_candidate | Operation V | 10 piles | tarot_calculator | Final |
| Technique | Counting | counting_tech | new_candidate | Narrative | K/Q/Pr=4, etc. | tarot_calculator | Golden Dawn |

<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_ops_prog | sequence | five_ops | depth | Progressive | When five operations progress sequentially from surface to depth interpretation | Surface→Deep | Thoth Appendix A |
| rel_yhvh_domain | mapping | yhvh_spread | question_type | Correspondence | When YHVH spread maps question domains to Tetragrammaton letters | Stack→Meaning | Thoth Appendix A |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| five_operations | Divination method | 六爻起卦 | Horary method | 解梦步骤 | Structured inquiry | Golden Dawn |
<!-- L2.5_END -->

---

## Appendix A: General Characters of the Trumps in Use (大牌实用特性)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Spiritual matters | Higher/abstract interpretation | Card's essential meaning |
| Material matters | Practical/mundane interpretation | Everyday application |
| Dignified | Well-aspected | Positive expression |
| Ill-dignified | Badly-aspected | Negative/shadow expression |

**Source Text** (Selected Trumps):

**0 - The Fool**:
> "In spiritual matters, the Fool means idea, thought, spirituality, that which endeavours to transcend earth. In material matters, it may, if badly dignified, mean folly, eccentricity, or even mania. But the essential of this card is that it represents an original, subtle, sudden impulse or impact, coming from a completely strange quarter."

**I - The Magus**:
> "Skill, wisdom, adroitness, elasticity, craft, cunning, deceit, theft. Sometimes occult wisdom or power, sometimes a quick impulse, a 'brain-wave'. It may imply messages, business transactions, the interference of learning or intelligence with the matter in hand."

**II - The High Priestess**:
> "Pure, exalted and gracious influence enters the matter. Hence, change, alternation, increase and decrease, fluctuation. There is, however, a liability to be led away by enthusiasm; one may become 'moon-struck' unless careful balance is maintained."

**English Paraphrase**:

Crowley provides **practical divinatory meanings** for each Trump, distinguishing between **spiritual** and **material** contexts:

**Key Patterns**:
- Each card has an **essential character** (its core meaning)
- **Dignified** (well-placed): Positive expression of the card's energy
- **Ill-dignified** (badly-placed): Shadow/negative expression
- Context determines whether the spiritual or material meaning applies

**Selected Trump Meanings**:

| Atu | Dignified | Ill-Dignified | Essential |
|-----|-----------|---------------|-----------|
| 0 Fool | Idea, spirituality, transcendence | Folly, eccentricity, mania | Sudden impulse from strange quarter |
| I Magus | Skill, wisdom, occult power | Cunning, deceit, theft | Intelligence interfering with matter |
| II Priestess | Pure influence, change, grace | Moon-struck, imbalanced | Fluctuation, increase/decrease |
| III Empress | Love, beauty, happiness, pleasure | Dissipation, debauchery | Creative harmony |
| IV Emperor | War, conquest, ambition, energy | Stubbornness, ill-temper | Overweening confidence |
| V Hierophant | Teaching, endurance, goodness | Stubborn orthodoxy | Manifestation of wisdom |

**完整中文诠释**：

Crowley提供每张大牌的**实用占卜含义**，区分**精神**和**物质**语境：

**关键模式**：
- 每张牌都有**本质特性**（核心含义）
- **尊贵**（良好位置）：牌能量的正面表达
- **卑下**（不良位置）：阴影/负面表达
- 语境决定适用精神还是物质含义

**部分大牌含义**：

| Atu | 尊贵 | 卑下 | 本质 |
|-----|------|------|------|
| 0 愚者 | 想法、灵性、超越 | 愚蠢、怪癖、疯狂 | 来自陌生处的突然冲动 |
| I 魔术师 | 技巧、智慧、神秘力量 | 狡猾、欺骗、盗窃 | 智力干预事务 |
| II 女祭司 | 纯净影响、变化、优雅 | 月迷、失衡 | 波动、增减 |
| III 皇后 | 爱、美、快乐、愉悦 | 放纵、堕落 | 创造和谐 |
| IV 皇帝 | 战争、征服、野心、能量 | 固执、坏脾气 | 过度自信 |
| V 教皇 | 教导、忍耐、善良 | 顽固正统 | 智慧显化 |

#### Core Points

- **Dual interpretation**: Each Trump has both spiritual (abstract) and material (practical) meanings.
- **Dignity system**: Well-dignified = positive; Ill-dignified = shadow/negative.
- **Essential character**: The card's irreducible core meaning, independent of dignity.
- **Context sensitivity**: The same card means different things in different positions and combinations.
- **Practical focus**: These meanings are for **actual readings**, not just theoretical study.

**Narrative Snippets**:
- `[ns_thoth_app_005]` `[trigger: trump_use]` `[factor_trigger: tarot_trump AND tarot_dignity]` `[role: 主干]` Each Trump has an essential character plus dignified and ill-dignified expressions depending on context. → English Paraphrase
- `[ns_thoth_app_006]` `[trigger: fool_essential]` `[factor_trigger: tarot_fool AND tarot_essential]` `[role: 主干依赖]` The Fool's essential meaning is an original, subtle, sudden impulse or impact from a completely strange quarter. → Source Text
- `[ns_thoth_app_013]` `[trigger: magus_skill]` `[factor_trigger: tarot_magus AND tarot_practical]` `[role: 条件分支]` The Magus signifies skill, wisdom, adroitness—sometimes occult wisdom or power, sometimes a quick impulse, a 'brain-wave'. → Magus
- `[ns_thoth_app_014]` `[trigger: dignity_system]` `[factor_trigger: tarot_dignity AND tarot_shadow]` `[role: 条件分支]` Dignified = positive expression of card's energy; Ill-dignified = shadow/negative expression. Context determines which applies. → Dignity

<!-- L1_END -->

<!-- L2_BEGIN -->

#### L2 Semantic Extraction
- **Theme**: Practical divinatory meanings of Trumps with dignity considerations
- **Natural Attributes**:
  - Symbolism: Dignified/Ill-dignified polarity, Essential character
  - Characteristics: Dual (spiritual/material), Context-dependent
  - Elements: 22 Trump meanings, dignity system
- **Functional Symbolism**:
  - Reading: Apply appropriate meaning based on context and dignity
  - Polarity: Positive and shadow expressions of same energy
  - Essential: Core meaning that persists regardless of dignity
- **Multi-layered Interpretation**:
  - Practical Layer: Specific keywords for readings
  - Dignitary Layer: Well-placed vs poorly-placed
  - Essential Layer: Irreducible card character
  - Integrative Layer: Spiritual + Material contexts

<!-- L2_END -->

<!-- FACTOR_BEGIN -->

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| System | Dignity | dignity_system | existing | Card evaluation | Dignified/Ill-dignified | tarot_calculator | Positional |
| Concept | Essential Character | essential_char | new_candidate | Core meaning | Irreducible | tarot_semantic | Key |
| Context | Spiritual/Material | sp_mat_context | new_candidate | Interpretation domain | Abstract/Practical | tarot_semantic | Dual |

<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_dig_meaning | modification | dignity_system | card_meaning | Polarity | When dignity system modifies card meaning based on surrounding context | Positive↔Negative | Thoth Appendix A |
| rel_context_interp | selection | sp_mat_context | interpretation | Application | When spiritual vs material context determines interpretation register | Abstract↔Practical | Thoth Appendix A |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| dignity_system | Positional meaning | 喜忌用神 | Dignity/Debility | 吉凶象征 | Positive/Shadow | Universal |
<!-- L2.5_END -->

---

## Appendix B: Correspondences Overview (对应表概览)

<!-- L1_BEGIN -->

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Correspondences | Systematic symbol mapping | Integration framework |
| Key Scale | Master attribution table | Reference system |
| 777 | Crowley's correspondence tables | Standard reference |
| Liber DCCLXXVII | "Book 777" | Latin title |

**Source Text**:
> "Note that the Nature of each Decan is shown by the small card attributed to it, and by the symbols given in Liber DCCLXXVII, cols. 149-151."

**English Paraphrase**:

Crowley's **777 Tables** provide the **master key** to Tarot correspondences:

**The Key Scale**:
- **32 Rows**: 10 Sephiroth + 22 Paths
- **Columns**: Multiple symbol systems mapped to each row

**Major Correspondence Categories**:

| Category | Examples |
|----------|----------|
| **Qabalistic** | Hebrew letters, Sephiroth, Paths, Divine Names |
| **Astrological** | Planets, Signs, Houses, Decans |
| **Elemental** | Fire, Water, Air, Earth; Tattvas |
| **Mythological** | Egyptian, Greek, Roman, Hindu gods |
| **Color** | King Scale, Queen Scale, Prince Scale, Princess Scale |
| **Gemstone** | Precious stones per path |
| **Perfume** | Incenses and oils |
| **Magical** | Weapons, practices, formulas |
| **Anatomical** | Body parts |
| **Animal** | Sacred animals |
| **Plant** | Herbs and trees |

**Tarot Specific**:
- **22 Trumps** → 22 Hebrew Letters → 22 Paths
- **4 Suits** → 4 Elements → YHVH
- **10 Pips** → 10 Sephiroth
- **16 Court Cards** → YHVH × 4 Elements
- **36 Small Cards (2-10)** → 36 Decans

**完整中文诠释**：

Crowley的**777表格**提供塔罗对应的**总钥匙**：

**钥匙表**：
- **32行**：10个Sephiroth + 22条路径
- **列**：映射到每行的多个符号系统

**主要对应类别**：

| 类别 | 示例 |
|------|------|
| **卡巴拉** | 希伯来字母、Sephiroth、路径、神圣名字 |
| **占星** | 行星、星座、宫位、旬 |
| **元素** | 火、水、气、土；Tattvas |
| **神话** | 埃及、希腊、罗马、印度神祇 |
| **颜色** | 国王尺度、皇后尺度、王子尺度、公主尺度 |
| **宝石** | 每条路径的宝石 |
| **香料** | 熏香和油 |
| **魔法** | 武器、实践、公式 |
| **解剖** | 身体部位 |
| **动物** | 神圣动物 |
| **植物** | 草药和树木 |

**塔罗专属**：
- **22张大牌** → 22希伯来字母 → 22路径
- **4花色** → 4元素 → YHVH
- **10数字牌** → 10 Sephiroth
- **16宫廷牌** → YHVH × 4元素
- **36小牌（2-10）** → 36旬

#### Core Points

- **777 Tables**: Crowley's "Liber DCCLXXVII" is the **master reference** for all Tarot correspondences.
- **32-row Key Scale**: 10 Sephiroth + 22 Paths = complete framework.
- **Multi-system integration**: Qabalah, astrology, mythology, color, gemstone, perfume, etc.
- **36 Decans**: The 36 small cards (2-10 of each suit) correspond to the 36 zodiacal decans.
- **Four Color Scales**: King (Atziluth), Queen (Briah), Prince (Yetzirah), Princess (Assiah) = four worlds.

**Narrative Snippets**:
- `[ns_thoth_app_007]` `[trigger: 777_tables]` `[factor_trigger: tarot_777 AND tarot_correspondence]` `[role: 主干]` Liber DCCLXXVII (777) provides the master key to all Tarot correspondences through its 32-row Key Scale. → English Paraphrase
- `[ns_thoth_app_008]` `[trigger: decan_cards]` `[factor_trigger: tarot_decan AND tarot_small_cards]` `[role: 主干依赖]` The 36 small cards (2-10 of each suit) correspond to the 36 zodiacal decans as shown in 777. → Source Text
- `[ns_thoth_app_015]` `[trigger: trump_path]` `[factor_trigger: tarot_trump AND tarot_hebrew]` `[role: 条件分支]` 22 Trumps correspond to 22 Hebrew letters and 22 paths on the Tree of Life—the structural backbone of Thoth correspondences. → Trumps
- `[ns_thoth_app_016]` `[trigger: color_scales]` `[factor_trigger: tarot_color AND tarot_four_worlds]` `[role: 条件分支]` Four Color Scales (King/Queen/Prince/Princess) correspond to four Qabalistic worlds: Atziluth, Briah, Yetzirah, Assiah. → Colors

<!-- L1_END -->

<!-- L2_BEGIN -->

#### L2 Semantic Extraction
- **Theme**: 777 Tables as master key to Tarot correspondences
- **Natural Attributes**:
  - Symbolism: 32 rows (10+22), multiple columns per system
  - Characteristics: Systematic, comprehensive, integrative
  - Elements: Qabalah, astrology, mythology, color, etc.
- **Functional Symbolism**:
  - Reference: Look up any card's correspondences
  - Integration: Multiple symbol systems unified
  - Practice: Choose appropriate correspondences for magical work
- **Multi-layered Interpretation**:
  - Structural Layer: 32-row framework
  - Symbolic Layer: Each row = convergence point of all systems
  - Practical Layer: Reference for ritual, meditation, divination
  - Theoretical Layer: All systems are one system

<!-- L2_END -->

<!-- FACTOR_BEGIN -->

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| System | 777 Tables | 777_tables | existing | Master reference | 32 rows | qabalah_engine | Crowley |
| Structure | Key Scale | key_scale | existing | Framework | 10+22 | qabalah_engine | Standard |
| Mapping | Decan-Card | decan_card_map | existing | Correspondence | 36=36 | tarot_calculator | Small cards |
| System | Four Color Scales | four_scales | existing | World correspondences | K/Q/Pr/Ps | qabalah_engine | Atziluth-Assiah |

<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_777_tarot | reference | 777_tables | tarot_cards | Master key | When Liber 777 tables provide master correspondence key for each card | Table→Meaning | Thoth Appendix B |
| rel_decan_pip | mapping | decan_card_map | tarot_small_cards | Astrological | When astrological decans map to numbered Minor Arcana cards | Decan→Card | Thoth Appendix B |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| correspondence_system | Symbol integration | 万象对应 | Rulership/Dignity | 象征对照 | Amplification | Universal |
<!-- L2.5_END -->

---

## Completion Summary

**Status**: ✅ Appendices - Complete

**Achievements**:
- 4 appendix sections with L1+L2+Factor Layer+L2.5
- Complete bilingual structure (English + Chinese)
- Divination method fully documented
- Correspondence system overview

**Coverage**:
1. **Behaviour of the Tarot** - Experiential learning principle
2. **Five Operations** - Golden Dawn divination method
3. **Trump Characters** - Practical divinatory meanings
4. **Correspondences Overview** - 777 Tables reference

**Key Concepts Covered**:
- Card behaviour and living symbolism
- Significator selection and use
- YHVH spread and domain identification
- 12-house and 12-sign spreads
- Tree of Life spread
- Counting and pairing techniques
- Dignity system (dignified/ill-dignified)
- Essential character of Trumps
- 777 Tables and Key Scale
- Four Color Scales
- Decan correspondences

---
