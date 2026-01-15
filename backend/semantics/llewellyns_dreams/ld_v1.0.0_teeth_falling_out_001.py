"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386981
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="ld_v1.0.0_teeth_falling_out_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class TeethFallingOut(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Teeth Falling | Power/co...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Teeth Falling | Power/confidence loss | Universal anxiety |
| Ability to Bite | Assertion/defense | Social power |
| Communication Loss | Unable to express | Powerlessness |
| Rotten Teeth | Self-neglect | Warning sign |

**Source Text** (Paraphrased):
> "Teeth falling out represents loss of power/confidence, communication issues. Teeth = ability to 'bite' (assert), speak clearly, show strength. Losing teeth = feeling powerless, unable to communicate needs effectively, loss of confidence or social power. One of most common anxiety dreams worldwide."

**English Paraphrase**:
**Teeth falling out**: **loss of power/confidence, communication issues**. Teeth = ability to **"bite"** (assert, defend, attack), speak clearly, show strength/confidence. **Losing teeth** = feeling powerless, inability to communicate needs, social embarrassment, loss of confidence. **Variations**: All teeth = total powerlessness; Front teeth = public image loss; Rotten teeth = neglected self (before falling). One of most **common anxiety dreams** worldwide (cross-cultural).

**Complete Chinese Interpretation**:
**牙齿脱落**：**失去力量/自信、沟通问题**。牙齿=能力**"咬"**（坚持、防御、攻击）、清晰说话、展示力量/自信。**失去牙齿**=感觉无力、无法沟通需求、社交尴尬、失去自信。**变体**：所有牙齿=完全无力；门牙=公众形象丧失；腐烂牙齿=被忽视自我（脱落前）。最**常见焦虑梦**之一全球（跨文化）。

#### Core Points

- **Power/Confidence Loss**: Teeth falling out represents loss of power/confidence.
- **Communication Issues**: Teeth enable "biting" (asserting) and speaking clearly—loss = communication difficulty.
- **Universal Anxiety Dream**: One of the most common anxiety dreams worldwide (cross-cultural).
- **Variations**: All teeth = total powerlessness; Front teeth = public image; Rotten = self-neglect.
- **Social Power**: Ability to "bite" = assert, defend, stand one's ground.

#### Detailed Explanation

Teeth falling out represents loss of power/confidence and communication issues. Teeth = ability to "bite" (assert, defend, attack), speak clearly, show strength/confidence. Losing teeth = feeling powerless, inability to communicate needs, social embarrassment, loss of confidence. Variations: All teeth = total powerlessness; Front teeth = public image loss; Rotten teeth = neglected self (before falling). One of the most common anxiety dreams worldwide (cross-cultural).

**L2 Semantic Extraction**:
- **Theme**: Power/confidence loss, communication difficulty
- **Natural Attributes**: Teeth = tools for asserting (biting), speaking, showing strength; loss = powerlessness/vulnerability
- **Functional Symbolism**: Reveals feeling powerless, unable to communicate effectively, loss of social confidence; shows self-neglect (rotten teeth before falling); very common anxiety dream
- **Conditional Structure**: Common during periods of powerlessness, communication difficulty, social anxiety, self-neglect; all teeth = total loss; front teeth = public image; rotten = neglected self
- **Multi-layered Interpretation**: Physical (literal teeth) → Assertion (ability to "bite"/defend) → Communication (speak clearly) → Power (social confidence) → Self-care (rotten = neglect)
- **Integration**: Lennox (power/communication loss) ← Universal anxiety dream (cross-cultural) ← Eastern (牙齿脱落=失力/失言/沟通障碍)

**L2-Term Glossary**:

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Teeth Falling Out | 牙齿脱落 | Symbol of power/confidence loss, communication difficulty | 力量/自信丧失、沟通困难的象征 | dream_symbol_teeth | new_candidate |
| Ability to Bite | 咬的能力 | Assertiveness, ability to defend/attack, stand one's ground | 坚定性，防御/攻击能力，坑住立场 | psych_ability_to_bite | new_candidate |
| Communication Powerlessness | 沟通无力 | Unable to express needs effectively, social embarrassment | 无法有效表达需求，社交尴尬 | psych_comm_powerlessness | new_candidate |
| Rotten Teeth | 腐烂牙齿 | Self-neglect before loss, ignored self-care | 丧失前的自我忽视，被忽略的自我照顾 | dream_rotten_teeth | new_candidate |

**Factor Layer**:

<!-- L2_END -->
<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Teeth Falling Out | dream_symbol_teeth | new_candidate | Anxiety Dream | Power/communication loss | dream_semantic | Universal dream |
| Functional | Ability to Bite | psych_ability_to_bite | new_candidate | Assertion | Defend/attack/stand ground | dream_semantic | Social power |
| State | Communication Loss | psych_comm_loss | new_candidate | Powerlessness | Unable to express needs | dream_semantic | Social anxiety |
| State | Rotten Teeth | dream_rotten_teeth | new_candidate | Self-neglect | Ignored self-care before loss | dream_semantic | Warning sign |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_lennox_teeth_001 | dream_symbol_relation | teeth_falling | power_loss | Action-meaning | When teeth falling universal anxiety reveals power loss | revealing | Lennox #Sym22 |
| rel_lennox_teeth_002 | dream_symbol_relation | ability_to_bite | assertion_capacity | Body-function | When ability to bite diagnoses assertion capacity social power | diagnostic | Lennox #Sym22 |
| rel_lennox_teeth_003 | dream_symbol_relation | rotten_teeth | self_neglect | State-cause | When rotten teeth before falling warns of self neglect | warning | Lennox #Sym22 |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_lennox_teeth_001 | "Teeth falling out represents loss of power/confidence, communication issues" | teeth_falling, power_loss | Teeth fall → power/confidence lost → social anxiety revealed | Teeth loss = power loss | High | ✅ | rule_teeth_power |
| evi_lennox_teeth_002 | "Teeth = ability to 'bite' (assert), speak clearly, show strength" | teeth_function, assertion | Teeth assessed → assertion capacity recognized → social power revealed | Teeth = assertion ability | High | ✅ | rule_teeth_assertion |
| evi_lennox_teeth_003 | "Rotten teeth = neglected self before falling" | rotten_teeth, neglect | Rotten condition → self-neglect indicated → warning sign identified | Rotten = self-neglect | High | ✅ | rule_rotten_teeth |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_power_loss | Loss of social strength and confidence | 失势/失地 | Debilitated Mars | teeth_falling | Ego weakness | Universal anxiety |
| concept_assertion_capacity | Ability to defend and express needs | 比劫有力 | Mars/1st house | ability_to_bite | Ego strength | Social power |
| concept_self_neglect | Ignored self-care leading to deterioration | 日主受克 | 6th house neglect | rotten_teeth | Self-abandonment | Warning pattern |
<!-- L2.5_END -->

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Teeth falling = power/confidence loss, communication difficulty. One of most common anxiety dreams worldwide (cross-cultural). Ability to "bite" = assert/defend. Rotten teeth = self-neglect before loss.
- **中文**: 牙齿脱落=力量/自信丧失、沟通困难。全球最常见焦虑梦之一(跨文化)。"咬"的能力=坚持/防御。腐烂牙齿=丢失前自我忽视。

**Narrative Snippets**:
- `[ns_llewellyn_051]` `[trigger: teeth_power]` `[factor_trigger: dream_symbol_teeth]` `[role: 主干]` Teeth falling out represents loss of power/confidence—teeth = ability to "bite" (assert), speak clearly, show strength. → Source Text
- `[ns_llewellyn_052]` `[trigger: teeth_universal]` `[factor_trigger: psych_comm_loss]` `[role: 总结]` One of most common anxiety dreams worldwide (cross-cultural)—indicates powerlessness, communication difficulty. → Source Text
- `[ns_llewellyn_126]` `[trigger: ability_to_bite]` `[factor_trigger: psych_ability_to_bite]` `[role: 主干依赖]` Ability to bite: teeth enable assertion, defense, attack—standing one's ground and expressing power. → English Paraphrase
- `[ns_llewellyn_127]` `[trigger: assertion_capacity]` `[factor_trigger: psych_ability_to_bite]` `[role: 主干依赖]` Assertion capacity: teeth symbolize ability to defend, attack, assert needs—social power and confidence. → English Paraphrase
- `[ns_llewellyn_128]` `[trigger: rotten_teeth]` `[factor_trigger: dream_rotten_teeth]` `[role: 条件分支]` Rotten teeth: self-neglect before loss—ignored self-care leading to deterioration of power/confidence. → English Paraphrase
- `[ns_llewellyn_129]` `[trigger: self_worth_fear]` `[factor_trigger: dream_symbol_teeth]` `[role: 条件分支]` Self-worth fear: teeth falling connects to abandonment anxiety—loss of social power triggering primitive fears. → English Paraphrase
- `[ns_llewellyn_130]` `[trigger: emotional_state]` `[factor_trigger: psych_comm_loss]` `[role: 总结]` Emotional state: teeth dreams reveal current emotional condition—anxiety, powerlessness, communication difficulty. → English Paraphrase

---

---

## PART 3: Complete A-Z Symbol Index (989 Symbols)

原文包含989个梦境符号条目，以下为完整双语索引。

### A (47 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Abandonment | Self-worth fears, primitive anxiety | 自我价值恐惧，原始焦虑 |
| Abdomen | Emotions, gut feelings, self-nourishment | 情绪，直觉，自我滋养 |
| Abortion | Eliminating potential, ending gestation | 消除潜能，终止孕育 |
| Abscess | Hidden problem needing attention | 需要关注的隐藏问题 |
| Abyss | Unknown depths, risk-taking edge | 未知深处，冒险边缘 |
| Accelerator | Increasing efforts, speed control | 增加努力，速度控制 |
| Accident | Sudden course correction | 突然路线修正 |
| Acid | Corrosive feelings eating away | 腐蚀性感受侵蚀 |
| Acorn | Potential, small idea becoming great | 潜能，小想法变伟大 |
| Acrobat | Mental agility, flexibility | 思维敏捷，灵活性 |
| Actor | Role-playing, inauthenticity | 角色扮演，不真实 |
| Acupuncture | Energy healing, meridian balance | 能量疗愈，经络平衡 |
| Addict | Escapism, loss of control | 逃避，失控 |
| Affair | See Infidelity | 见不忠 |
| Age | Past exploration, time of emergence | 过去探索，出现时间 |
| Airplane | Rapid life transition | 快速生活转变 |
| Alcohol | See Drinks/Drinking | 见饮酒 |
| Alien | Foreign self-aspect, unknown | 陌生自我面向，未知 |
| Alligator | Primitive instincts, emotional danger | 原始本能，情感危险 |
| Ambulance | Rescue, healing transport | 救援，疗愈运输 |
| Amethyst | Higher consciousness, healing | 更高意识，疗愈 |
| Anchor | Staying grounded in emotions | 情感中保持稳定 |
| Angel | Divine guidance, protection | 神圣指引，保护 |
| Animals | Instincts, specific traits | 本能，特定特质 |
| Ant | Anxiety, pervasive thoughts | 焦虑，弥漫思绪 |
| Anteater | Feeding off anxiety | 以焦虑为食 |
| Apple | Abundance, temptation, wisdom | 丰富，诱惑，智慧 |
| Arrow | Aim, penetrating idea | 瞄准，穿透性想法 |
| Art | Creative expression, past passion | 创造表达，过去激情 |
| Artist | Creative self-aspect | 创造性自我面向 |
| Ashes | Transformation residue, endings | 转化残余，结束 |
| Attic | Higher consciousness, stored memories | 更高意识，储存记忆 |
| Aunt | Extended family dynamics | 延展家庭动态 |
| Aura | Energy field, spiritual presence | 能量场，灵性存在 |
| Automobile | Life path movement | 人生道路移动 |

### B (63 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Baby | New beginning, vulnerability, potential | 新开始，脆弱性，潜能 |
| Backpack | Carrying responsibilities, preparedness | 承担责任，准备就绪 |
| Badger | Persistence, determination | 坚持，决心 |
| Bag | Containment, carrying burdens | 容纳，承担负担 |
| Ball | Wholeness, play, childhood | 完整，玩耍，童年 |
| Ballerina | Grace, discipline, femininity | 优雅，纪律，女性气质 |
| Banana | Sensuality, nourishment, humor | 感官，滋养，幽默 |
| Bank | Security, resources, abundance | 安全，资源，丰富 |
| Bar | Social interaction, escapism | 社交互动，逃避 |
| Barefoot | Grounding, vulnerability | 接地，脆弱 |
| Barn | Storage, productivity, rural life | 储存，生产力，乡村生活 |
| Bartender | Social mediator, listener | 社交调解者，倾听者 |
| Baseball | Competition, teamwork, American culture | 竞争，团队合作，美国文化 |
| Basement | Unconscious, hidden aspects | 无意识，隐藏面向 |
| Basket | Containment, gathering | 容纳，收集 |
| Bass | Deep emotions, rhythm | 深层情感，节奏 |
| Bat | Rebirth, intuition, night vision | 重生，直觉，夜视 |
| Bathroom | Privacy, cleansing, elimination | 隐私，净化，排除 |
| Bathtub | Emotional cleansing, relaxation | 情感净化，放松 |
| Battery | Energy reserves, power source | 能量储备，动力源 |
| Battle | Inner conflict, struggle | 内在冲突，斗争 |
| Beach | Conscious/unconscious boundary | 意识/无意识边界 |
| Bear | Strength, introspection, protection | 力量，内省，保护 |
| Beard | Masculinity, wisdom, hiding | 男性气质，智慧，隐藏 |
| Beast | Primal instincts, wild nature | 原始本能，野性 |
| Beaver | Industry, building, persistence | 勤劳，建设，坚持 |
| Bed | Rest, intimacy, vulnerability | 休息，亲密，脆弱 |
| Bedroom | Privacy, sexuality, rest | 隐私，性欲，休息 |
| Bee | Industry, community, productivity | 勤劳，社区，生产力 |
| Beehive | Collective effort, organization | 集体努力，组织 |
| Beer | Relaxation, social bonding | 放松，社交联系 |
| Belly | Emotional center, vulnerability | 情感中心，脆弱 |
| Bellybutton | Original connection, center | 原始连接，中心 |
| Belt | Restraint, security, discipline | 约束，安全，纪律 |
| Bible | Spiritual guidance, moral code | 灵性指引，道德准则 |
| Bicycle | Balance, personal effort, journey | 平衡，个人努力，旅程 |
| Bills | Financial stress, obligations | 财务压力，义务 |
| Birds | Freedom, transcendence, messages | 自由，超越，信息 |
| Birthday | Celebration, new cycle, identity | 庆祝，新周期，身份 |
| Black | Mystery, unknown, potential | 神秘，未知，潜能 |
| Blanket | Security, comfort, protection | 安全，舒适，保护 |
| Blood | Life force, passion, sacrifice | 生命力，激情，牺牲 |
| Blue | Communication, truth, calm | 沟通，真理，平静 |
| Blueprint | Life plan, structure, design | 人生计划，结构，设计 |
| Boat | Emotional journey, navigation | 情感旅程，导航 |
| Bobcat | Stealth, independence | 隐秘，独立 |
| Bomb | Explosive emotions, sudden change | 爆炸性情感，突然变化 |
| Bones | Foundation, hidden structure | 基础，隐藏结构 |
| Book | Knowledge, learning, life story | 知识，学习，生命故事 |
| Bottle | Containment, preservation | 容纳，保存 |
| Box | Compartmentalizing, containing | 分隔，容纳 |
| Bracelet | Self-expression, creativity | 自我表达，创造力 |
| Breasts | Nurturance, femininity, self-care | 养育，女性气质，自我照顾 |
| Bridge | Transition, connection | 过渡，连接 |
| Briefcase | Work responsibilities, obligations | 工作责任，义务 |
| Broom | Cleaning up, magical thinking | 清理，魔法思维 |
| Brother | See Siblings | 见兄弟姐妹 |
| Brown | Earthiness, dullness, grounding | 土气，沉闷，接地 |
| Buddha | Enlightenment, inner peace | 开悟，内在平静 |
| Buffalo | Gratitude, abundance, provision | 感恩，丰富，供应 |
| Bugs | See Insects | 见昆虫 |
| Bull | Strength, stillness, prosperity | 力量，静止，繁荣 |
| Bus | Slow transition, collective journey | 缓慢过渡，集体旅程 |
| Butterfly | Transformation, rebirth | 转化，重生 |

### C (52 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Cactus | Thriving despite challenges | 尽管挑战仍繁荣 |
| Cage | Restriction, imprisonment | 限制，监禁 |
| Cake | Celebration, indulgence | 庆祝，放纵 |
| Calendar | Time awareness, planning | 时间意识，规划 |
| Calf | Young potential, vulnerability | 年轻潜能，脆弱 |
| Callus | Toughened from experience | 经验磨砺 |
| Camel | Endurance, patience | 耐力，耐心 |
| Camera | Capturing moments, observation | 捕捉瞬间，观察 |
| Camping | Back to nature, simplicity | 回归自然，简朴 |
| Can | Preservation, containment | 保存，容纳 |
| Candle | Illumination, hope, spirit | 照明，希望，精神 |
| Candy | Pleasure, reward, childishness | 快乐，奖赏，幼稚 |
| Cap | Informal identity, youth | 非正式身份，青春 |
| Car | Life path, personal control | 人生道路，个人控制 |
| Card | Communication, luck, chance | 沟通，运气，机会 |
| Carnival | Celebration, chaos, fun | 庆祝，混乱，乐趣 |
| Carpet | Foundation, luxury, covering | 基础，奢华，覆盖 |
| Casket | Death, endings, burial | 死亡，结束，埋葬 |
| Cat | Independence, intuition, femininity | 独立，直觉，女性气质 |
| Caterpillar | Pre-transformation state | 转化前状态 |
| Celebrities | Aspirational qualities | 渴望的品质 |
| Centaur | Human/animal integration | 人/动物整合 |
| Chair | Rest, authority, support | 休息，权威，支持 |
| Chakras | Energy centers, spiritual balance | 能量中心，灵性平衡 |
| Chased | Running from self-aspect | 逃避自我面向 |
| Cheerleader | Support, enthusiasm | 支持，热情 |
| Cheetah | Speed, quick action | 速度，快速行动 |
| Chicken | Fear, cowardice, nourishment | 恐惧，胆怯，滋养 |
| Children | Inner child, innocence | 内在小孩，纯真 |
| Choking | Communication blockage | 沟通阻塞 |
| Church | Spirituality, community | 灵性，社区 |
| Circus | Chaos, entertainment, spectacle | 混乱，娱乐，奇观 |
| Climbing | Ambition, effort, progress | 野心，努力，进步 |
| Closet | Hidden aspects, secrets | 隐藏面向，秘密 |
| Clothes | Self-expression, persona | 自我表达，人格面具 |
| Clowns | Humor, hiding sadness | 幽默，隐藏悲伤 |
| Coat | Protection, identity layer | 保护，身份层 |
| Cobra | Danger, transformation | 危险，转化 |
| Cockatoo | Communication, exotic | 沟通，异国情调 |
| Coffin | Death, ending, finality | 死亡，结束，终结 |
| Coin | Value, choice, luck | 价值，选择，运气 |
| Colors | Emotions, energy states | 情绪，能量状态 |
| Computer | Intellect, processing | 智力，处理 |
| Cookies | Comfort, childhood | 舒适，童年 |
| Cougar | Feminine power, stealth | 女性力量，隐秘 |
| Cow | Nurturance, abundance | 养育，丰富 |
| Cowboy | Independence, masculinity | 独立，男性气质 |
| Crab | Protection, sideways approach | 保护，侧面方法 |
| Criminal | Shadow aspect, rule-breaking | 阴影面向，破坏规则 |
| Crocodile | Hidden danger, primitive | 隐藏危险，原始 |
| Cross | Faith, sacrifice, burden | 信仰，牺牲，负担 |
| Crows | Magic, transformation, death | 魔法，转化，死亡 |
| Crying | Emotional release, grief | 情感释放，悲伤 |
| Crystal | Clarity, purity, healing | 清晰，纯净，疗愈 |
| Cup | Containment, emotions | 容纳，情感 |
| Cupcake | Small pleasure, indulgence | 小快乐，放纵 |
| Cutting | Separation, self-harm, release | 分离，自我伤害，释放 |

### D (62 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Dagger | Betrayal, precision, danger | 背叛，精确，危险 |
| Dance | Expression, joy, rhythm | 表达，快乐，节奏 |
| Dancing | Movement, celebration | 移动，庆祝 |
| Dandruff | Self-image concerns | 自我形象担忧 |
| Darkness | Unknown, shadow, mystery | 未知，阴影，神秘 |
| Date | Romantic potential, time | 浪漫潜能，时间 |
| Daycare | Nurturing, responsibility | 养育，责任 |
| Deaf | Not hearing truth | 听不到真相 |
| Death | Transformation, endings | 转化，结束 |
| Deer | Gentleness, grace, sensitivity | 温柔，优雅，敏感 |
| Defecation | Releasing unwanted | 释放不想要的 |
| Defibrillator | Reviving passion | 复苏激情 |
| Delivery | Receiving, bringing forth | 接收，产生 |
| Demon | Shadow, fear, inner struggle | 阴影，恐惧，内在斗争 |
| Desert | Emotional drought, solitude | 情感干旱，孤独 |
| Desk | Work, organization | 工作，组织 |
| Dessert | Reward, pleasure | 奖赏，快乐 |
| Detective | Seeking truth, investigation | 寻求真相，调查 |
| Detergent | Cleansing, purification | 清洁，净化 |
| Devil | Shadow, temptation | 阴影，诱惑 |
| Dew | Fresh start, purity | 新开始，纯净 |
| Diamond | Value, permanence, clarity | 价值，永恒，清晰 |
| Diaper | Basic needs, vulnerability | 基本需求，脆弱 |
| Diarrhea | Emotional release, urgency | 情感释放，紧急 |
| Dice | Chance, risk, luck | 机会，风险，运气 |
| Diet | Self-control, restriction | 自我控制，限制 |
| Digging | Uncovering, searching | 发掘，搜索 |
| Dildo | Sexual self-sufficiency | 性自给自足 |
| Diploma | Achievement, recognition | 成就，认可 |
| Disability | Limitation, adaptation | 限制，适应 |
| Dishes | Cleanup, daily tasks | 清理，日常任务 |
| Ditch | Obstacle, escape route | 障碍，逃生路线 |
| Diving | Going deep emotionally | 深入情感 |
| Divorce | Separation, ending union | 分离，结束联合 |
| Doctor | Healing, authority | 疗愈，权威 |
| Dog | Loyalty, friendship, instincts | 忠诚，友谊，本能 |
| Doll | Childhood, false self | 童年，虚假自我 |
| Dollar | Value, worth | 价值，值得 |
| Dolphin | Intelligence, playfulness | 智慧，玩乐 |
| Donkey | Stubbornness, service | 固执，服务 |
| Door | Opportunity, transition | 机会，过渡 |
| Doorbell | Opportunity announcing | 机会宣告 |
| Doormat | Being walked over | 被踩踏 |
| Dove | Peace, love, spirit | 和平，爱，精神 |
| Down | Descent, depression | 下降，沮丧 |
| Dragon | Power, magic, transformation | 力量，魔法，转化 |
| Dragonfly | Change, illusion | 变化，幻觉 |
| Drain | Releasing, energy loss | 释放，能量流失 |
| Drapes | Privacy, covering | 隐私，覆盖 |
| Drawbridge | Selective access | 选择性进入 |
| Drawing | Creative expression | 创造表达 |
| Dress | Femininity, self-expression | 女性气质，自我表达 |
| Driving | Life control, direction | 生活控制，方向 |
| Drowning | Overwhelmed by emotions | 被情感淹没 |
| Drugs | Escapism, alteration | 逃避，改变 |
| Drugstore | Healing resources | 疗愈资源 |
| Drum | Rhythm, heartbeat, communication | 节奏，心跳，沟通 |
| Drunk | Loss of control, escapism | 失控，逃避 |
| Dryer | Processing, completion | 处理，完成 |
| Duck | Emotional adaptability | 情感适应性 |
| Dumpster | Discarding, waste | 丢弃，浪费 |
| Dungeon | Imprisonment, shadow | 监禁，阴影 |
| Dust | Neglect, passage of time | 忽视，时间流逝 |
| Dynamite | Explosive potential | 爆炸潜能 |

### E (47 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Eagle | Vision, power, spirituality | 视野，力量，灵性 |
| Earrings | Self-expression, femininity | 自我表达，女性气质 |
| Ears | Listening, receptivity | 倾听，接受性 |
| Earth | Grounding, stability | 接地，稳定 |
| Earthquake | Fundamental change, instability | 根本变化，不稳定 |
| Earwax | Blocked listening | 阻塞倾听 |
| Eating | Nourishment, taking in | 滋养，吸收 |
| Echo | Reflection, repetition | 反映，重复 |
| Eclipse | Temporary shadow, transformation | 暂时阴影，转化 |
| Egg | Potential, new life | 潜能，新生命 |
| Eggshells | Fragility, sensitivity | 脆弱，敏感 |
| Eight | Abundance, infinity | 丰富，无限 |
| Ejaculation | Creative release | 创造释放 |
| Electricity | Energy, vitality, shock | 能量，活力，震惊 |
| Elephant | Memory, wisdom, power | 记忆，智慧，力量 |
| Elevator | Consciousness levels, rapid change | 意识层次，快速变化 |
| Elf | Magical help, mischief | 魔法帮助，恶作剧 |
| Elk | Strength, stamina | 力量，耐力 |
| Emerald | Heart healing, love | 心灵疗愈，爱 |
| Engagement | Commitment, promise | 承诺，诺言 |
| Engine | Power source, motivation | 动力源，动机 |
| Envelope | Message, communication | 信息，沟通 |
| Eraser | Correction, starting over | 修正，重新开始 |
| Erection | Sexual energy, power | 性能量，力量 |
| Escalator | Effortless transition | 轻松过渡 |
| Exams | Testing, self-evaluation | 测试，自我评估 |
| Executions | Ending aspects, sacrifice | 结束面向，牺牲 |
| Exes | Past relationships, lessons | 过去关系，教训 |
| Explosion | Sudden release, transformation | 突然释放，转化 |
| Eyes | Perception, awareness, insight | 感知，觉察，洞见 |

### F (49 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Face | Identity, persona | 身份，人格面具 |
| Facebook | Social connection, public self | 社交连接，公众自我 |
| Faceless | Unknown identity | 未知身份 |
| Facelift | Identity change | 身份改变 |
| Factory | Productivity, routine | 生产力，例程 |
| Fair | Celebration, assessment | 庆祝，评估 |
| Fairy | Magic, wishes, feminine | 魔法，愿望，女性 |
| Falcon | Focus, precision | 聚焦，精确 |
| Falling | Loss of control, failure fear | 失控，失败恐惧 |
| Family | Core relationships, dynamics | 核心关系，动态 |
| Fan | Cooling emotions, admiration | 冷却情绪，钦佩 |
| Fangs | Aggression, danger | 攻击，危险 |
| Farm | Productivity, provision | 生产力，供应 |
| Fart | Release, embarrassment | 释放，尴尬 |
| Fat | Abundance, protection, excess | 丰富，保护，过度 |
| Father | Authority, structure | 权威，结构 |
| Faucet | Emotional flow control | 情感流控制 |
| Feather | Lightness, spirit, flight | 轻盈，精神，飞行 |
| Feces | Releasing unwanted, shame | 释放不想要，羞耻 |
| Feet | Grounding, direction | 接地，方向 |
| Fence | Boundaries, protection | 边界，保护 |
| Ferry | Emotional crossing | 情感穿越 |
| Festival | Celebration, community | 庆祝，社区 |
| Fetus | Potential, gestation | 潜能，孕育 |
| Fight | Conflict, struggle | 冲突，斗争 |
| Files | Information, organization | 信息，组织 |
| Filling | Repair, restoration | 修复，恢复 |
| Film | Life story, memories | 生命故事，记忆 |
| Fingernails | Protection, aggression | 保护，攻击 |
| Fingerprints | Identity, uniqueness | 身份，独特性 |
| Fingers | Dexterity, pointing | 灵巧，指向 |
| Fire | Passion, transformation, destruction | 激情，转化，毁灭 |
| Firefighter | Protection, courage | 保护，勇气 |
| Firefly | Light in darkness, magic | 黑暗中的光，魔法 |
| Fireplace | Warmth, home, heart | 温暖，家，心 |
| Fish | Ideas, unconscious content | 想法，无意识内容 |
| Fishing | Seeking unconscious ideas | 寻求无意识想法 |
| Fist | Aggression, determination | 攻击，决心 |
| Five | Change, freedom | 变化，自由 |
| Flag | Identity, patriotism | 身份，爱国 |
| Flame | Passion, spirit | 激情，精神 |
| Flamingo | Balance, beauty | 平衡，美丽 |
| Flashlight | Illuminating darkness | 照亮黑暗 |
| Flies | Annoyance, decay | 烦恼，衰败 |
| Flood | Emotional overwhelm | 情感淹没 |
| Floors | Foundation, levels | 基础，层次 |
| Flowers | Beauty, growth, transience | 美丽，成长，短暂 |
| Flying | Transcendence, freedom | 超越，自由 |
| Fog | Confusion, unclear | 困惑，不清晰 |
| Food | Nourishment, sustenance | 滋养，维持 |
| Football | Competition, strategy | 竞争，策略 |
| Fork | Choice, direction | 选择，方向 |
| Fountain | Emotional source, abundance | 情感源，丰富 |
| Four | Stability, foundation | 稳定，基础 |
| Fox | Cunning, adaptability | 狡猾，适应性 |
| Frog | Transformation, cleansing | 转化，清洁 |
| Fruit | Abundance, reward | 丰富，奖赏 |
| Funeral | Endings, grief, transformation | 结束，悲伤，转化 |
| Furniture | Comfort, stability | 舒适，稳定 |

### G (45 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Gagging | Communication blocked | 沟通被阻 |
| Galaxy | Infinite potential, vastness | 无限潜能，广阔 |
| Gang | Group identity, shadow collective | 群体身份，阴影集体 |
| Garage | Storage, projects, transition | 储存，项目，过渡 |
| Garbage | Discarded aspects, waste | 被丢弃面向，浪费 |
| Garden | Cultivation, growth, creation | 培养，成长，创造 |
| Gargoyle | Protection, shadow guardian | 保护，阴影守护者 |
| Gasoline | Energy, fuel, volatility | 能量，燃料，挥发性 |
| Gate | Entry, opportunity, boundary | 入口，机会，边界 |
| Gazelle | Grace, speed, vulnerability | 优雅，速度，脆弱 |
| Gemstone | Value, inner beauty | 价值，内在美 |
| Genie | Wishes, magical help | 愿望，魔法帮助 |
| Ghost | Past issues, unresolved | 过去问题，未解决 |
| Giant | Overwhelming, inflated | 压倒性，膨胀 |
| Gifts | Unknown joy, blessings | 未知喜悦，祝福 |
| Giraffe | Higher perspective | 更高视角 |
| Girdle | Constriction, superficiality | 束缚，肤浅 |
| Glacier | Frozen emotions, slow change | 冻结情感，缓慢变化 |
| Glass | See Cup | 见杯子 |
| Glasses | Perception, viewpoint | 感知，观点 |
| Gloves | Protection, hiding expression | 保护，隐藏表达 |
| Glue | Joining, sticking together | 连接，粘合 |
| Gold | Highest value, love | 最高价值，爱 |
| Goldfish | Simple ideas, visibility | 简单想法，可见性 |
| Golf | Leisure, patience | 休闲，耐心 |
| Google | Instant knowledge access | 即时知识获取 |
| Gorilla | Power, aggression, posturing | 力量，攻击，姿态 |
| Graduation | Achievement, completion | 成就，完成 |
| Grain | Basic sustenance, abundance | 基本食粮，丰富 |
| Grandparents | Family dynamics, wisdom | 家庭动态，智慧 |
| Grapes | Prosperity, cultivation | 繁荣，培养 |
| Grass | Nature connection, grounding | 自然连接，接地 |
| Grave | Past identity, endings | 过去身份，结束 |
| Gray | Lack of vibrancy, aging | 缺乏活力，老化 |
| Green | Heart, healing, growth | 心，疗愈，成长 |
| Groceries | Abundance, sustenance | 丰富，维持 |
| Gryphon | Power, treasure guardian | 力量，财宝守护者 |
| Guard | Protection, vigilance | 保护，警惕 |
| Guitar | Creativity, passion, sexuality | 创造力，激情，性欲 |
| Gum | Communication obstacles | 沟通障碍 |
| Gums | Self-care, nurturing | 自我照顾，养育 |
| Gun | Power over others, masculine | 对他人的权力，男性 |
| Gym | Building strength, effort | 建立力量，努力 |

### H (49 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Hair | Strength, attractiveness | 力量，吸引力 |
| Haircut | Diminished power, change | 削弱力量，变化 |
| Hallway | Transition, passage | 过渡，通道 |
| Hammer | Building, forcing | 建设，强迫 |
| Hammock | Relaxation, nature | 放松，自然 |
| Handcuffs | Restriction, consequence | 限制，后果 |
| Hands | Creativity, expression | 创造力，表达 |
| Hanging | Death/transformation, sacrifice | 死亡/转化，牺牲 |
| Harbor | Emotional receptivity | 情感接受性 |
| Harp | Aspiration, spiritual | 抱负，灵性 |
| Harvest | Reaping rewards | 收获奖赏 |
| Hat | Thoughts, protection | 思想，保护 |
| Hawk | Vision, messages | 视野，信息 |
| Head | Thoughts, thinking | 思想，思考 |
| Headlights | Seeing in darkness | 在黑暗中看见 |
| Headstone | See Tombstone | 见墓碑 |
| Heart | Love, passion, center | 爱，激情，中心 |
| Heights | Higher consciousness, risk | 更高意识，风险 |
| Helicopter | Observation, swift movement | 观察，快速移动 |
| Hell | Separation, disconnection | 分离，断开 |
| Helmet | Protection, ideas safety | 保护，想法安全 |
| Heroin | Escapism, addiction cycle | 逃避，成瘾循环 |
| Hieroglyphics | Hidden wisdom, encoded | 隐藏智慧，编码 |
| Hike | Exploring off-path | 探索偏离道路 |
| Hill | Effort, challenge | 努力，挑战 |
| Hippo | Hidden emotions, aggression | 隐藏情感，攻击 |
| Hockey | Aggression, fast pace | 攻击，快节奏 |
| Hole | Something missing | 缺失某物 |
| Hologram | Illusion, projection | 幻觉，投射 |
| Homosexuality | Shadow integration | 阴影整合 |
| Honeycomb | Sweet rewards, structure | 甜蜜奖赏，结构 |
| Hood | Concealment, anonymity | 隐藏，匿名 |
| Hoodie | Casual identity, hiding | 随意身份，隐藏 |
| Hooks | Attachment, entanglement | 依附，纠缠 |
| Horizon | Future possibilities | 未来可能性 |
| Horse | Power, freedom, drives | 力量，自由，驱力 |
| Horseshoe | Luck, protection | 运气，保护 |
| Hose | Emotional flow direction | 情感流方向 |
| Hospital | Healing needed | 需要疗愈 |
| Hotel | Temporary identity | 临时身份 |
| House | Self, psyche structure | 自我，心理结构 |
| Humming | Unconscious communication | 无意识沟通 |
| Hummingbird | Joy, agility | 快乐，敏捷 |
| Hurricane | Overwhelming emotions | 压倒性情感 |

### I-J-K (65 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Ice | Frozen emotions, coldness | 冻结情感，冷漠 |
| Iceberg | Hidden emotions | 隐藏情感 |
| Icing | Surface sweetness | 表面甜蜜 |
| Identification | Identity proof | 身份证明 |
| Incest | Taboo integration | 禁忌整合 |
| Incubus | Sexual shadow | 性阴影 |
| Infidelity | Trust betrayal | 信任背叛 |
| Infinity | Endless potential | 无尽潜能 |
| Injection | External influence | 外部影响 |
| Insects | Pervasive thoughts | 弥漫思绪 |
| Instrument | Creative expression | 创造表达 |
| Intercourse | Integration, union | 整合，结合 |
| Internet | Connection, information | 连接，信息 |
| Iron | Strength, resolve | 力量，决心 |
| Island | Isolation, self-sufficiency | 孤立，自给自足 |
| Itch | Irritation, need attention | 刺激，需要关注 |
| Jackass | Stubbornness, foolishness | 固执，愚蠢 |
| Jacket | Identity layer, protection | 身份层，保护 |
| Jackhammer | Breaking through | 突破 |
| Jaguar | Power, stealth | 力量，隐秘 |
| Jail | Restriction, limitation | 限制，局限 |
| Janitor | Cleanup, maintenance | 清理，维护 |
| Jar | Containment, preservation | 容纳，保存 |
| Jaw | Power, determination | 力量，决心 |
| Jeans | Casual identity | 随意身份 |
| Jeep | Rugged journey | 崎岖旅程 |
| Jester | Humor, wisdom in folly | 幽默，愚行中的智慧 |
| Jet | Fast travel, ambition | 快速旅行，野心 |
| Jewelry | Value, adornment | 价值，装饰 |
| Jewels | Inner treasures | 内在宝藏 |
| Joint | Relaxation, connection | 放松，连接 |
| Journal | Self-reflection, recording | 自我反思，记录 |
| Judge | Inner critic, assessment | 内在批评者，评估 |
| Juice | Vitality, essence | 活力，本质 |
| Jungle | Untamed unconscious | 未驯服的无意识 |
| Jury | Collective judgment | 集体判断 |
| Kangaroo | Protection, leaping | 保护，跳跃 |
| Karaoke | Public expression | 公开表达 |
| Kayak | Personal emotional journey | 个人情感旅程 |
| Key | Solution, access | 解决方案，进入 |
| Keyboard | Communication, expression | 沟通，表达 |
| Kidnap | Loss of control | 失控 |
| King | Authority, masculine power | 权威，男性力量 |
| Kiss | Love, connection | 爱，连接 |
| Kitchen | Nurturance, self-care | 养育，自我照顾 |
| Kite | Freedom with connection | 有连接的自由 |
| Kitten | Innocence, playfulness | 纯真，玩乐 |
| Knife | Separation, precision | 分离，精确 |
| Knight | Protection, chivalry | 保护，骑士精神 |
| Knot | Complexity, binding | 复杂，绑定 |
| Koran | Spiritual guidance | 灵性指引 |

### L-M (78 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Label | Identity, categorization | 身份，分类 |
| Laboratory | Experimentation | 实验 |
| Labyrinth | Complex journey | 复杂旅程 |
| Lace | Delicate, feminine | 精致，女性 |
| Ladder | Progress, ascension | 进步，上升 |
| Ladybug | Good luck, protection | 好运，保护 |
| Lake | Contained emotions | 被包含情感 |
| Lamb | Innocence, sacrifice | 纯真，牺牲 |
| Lamp | Illumination, guidance | 照明，指引 |
| Land | Consciousness, grounding | 意识，接地 |
| Languages | Communication barriers | 沟通障碍 |
| Lap | Nurturance, comfort | 养育，舒适 |
| Laptop | Portable intellect | 便携智力 |
| Laryngitis | Voice loss | 失声 |
| Laughter | Joy, release | 快乐，释放 |
| Laundry | Cleaning up | 清理 |
| Lava | Intense emotions | 强烈情感 |
| Lawn | Public image | 公众形象 |
| Lawyer | Justice, advocacy | 正义，辩护 |
| Leak | Energy loss | 能量流失 |
| Leash | Control, restriction | 控制，限制 |
| Leaves | Change, letting go | 变化，放手 |
| Ledge | Risk, edge | 风险，边缘 |
| Leeches | Energy drain | 能量消耗 |
| Legs | Movement, support | 移动，支持 |
| Leopard | Stealth, beauty | 隐秘，美丽 |
| Letter | Communication | 沟通 |
| Levitation | Transcendence | 超越 |
| Library | Knowledge repository | 知识库 |
| Light | Consciousness, truth | 意识，真理 |
| Lighthouse | Guidance, warning | 指引，警告 |
| Lightning | Sudden insight | 突然洞见 |
| Lingerie | Sexuality, intimacy | 性欲，亲密 |
| Lion | Courage, authority | 勇气，权威 |
| Lips | Communication, sensuality | 沟通，感官 |
| Lipstick | Feminine expression | 女性表达 |
| Lizard | Primitive instincts | 原始本能 |
| Lobby | Public transition | 公共过渡 |
| Lobster | Protection, hidden | 保护，隐藏 |
| Lock | Security, restriction | 安全，限制 |
| Lollipop | Pleasure, childishness | 快乐，幼稚 |
| Luggage | Emotional baggage | 情感包袱 |
| Lynx | Secrets, vision | 秘密，视野 |
| Machete | Cutting through | 切穿 |
| Magazine | Public information | 公开信息 |
| Maggots | Decay, transformation | 衰败，转化 |
| Magic | Transformation power | 转化力量 |
| Magician | Manifestation | 显化 |
| Magnet | Attraction | 吸引 |
| Maid | Service, cleaning | 服务，清洁 |
| Mail | Messages coming | 信息到来 |
| Makeup | Persona, covering | 人格面具，遮盖 |
| Mall | Consumerism, choices | 消费主义，选择 |
| Mammogram | Health concern | 健康担忧 |
| Manatee | Gentleness, peace | 温柔，和平 |
| Mandala | Wholeness, integration | 完整，整合 |
| Manicure | Self-care details | 自我照顾细节 |
| Map | Direction, planning | 方向，规划 |
| Marching | Discipline, collective | 纪律，集体 |
| Market | Exchange, opportunity | 交换，机会 |
| Marriage | Union, commitment | 结合，承诺 |
| Mask | Hiding identity | 隐藏身份 |
| Massage | Healing touch | 疗愈触摸 |
| Mastectomy | Loss of femininity | 失去女性气质 |
| Masturbation | Self-pleasure | 自我愉悦 |
| Matches | Potential for fire | 火的潜能 |
| Math | Logic, calculation | 逻辑，计算 |
| Measurements | Assessment, judgment | 评估，判断 |
| Meat | Primal nourishment | 原始滋养 |
| Mechanic | Fixing, repair | 修复，修理 |
| Meeting | Communication, planning | 沟通，规划 |
| Menstruation | Feminine cycle | 女性周期 |
| Mermaid | Feminine unconscious | 女性无意识 |
| Microphone | Amplified voice | 放大的声音 |
| Microwave | Quick transformation | 快速转化 |
| Military | Structure, discipline | 结构，纪律 |
| Milk | Nurturance, mother | 养育，母亲 |
| Mine | Hidden resources | 隐藏资源 |
| Minister | Spiritual guidance | 灵性指引 |
| Mirror | Self-reflection | 自我反映 |
| Miscarriage | Lost potential | 失去潜能 |
| Mistress | Shadow feminine | 阴影女性 |
| Model | Ideal image | 理想形象 |
| Mold | Decay, neglect | 衰败，忽视 |
| Monastery | Spiritual retreat | 灵性退修 |
| Money | Value, worth | 价值，值得 |
| Monkey | Playfulness, mischief | 玩乐，恶作剧 |
| Monuments | Lasting memory | 持久记忆 |
| Moose | Strength, self-esteem | 力量，自尊 |
| Morning | New beginning | 新开始 |
| Mosque | Spiritual devotion | 灵性奉献 |
| Mosquito | Annoyance, drain | 烦恼，消耗 |
| Moth | Attraction to light | 被光吸引 |
| Mother | Nurturance, feminine | 养育，女性 |
| Motorcycle | Freedom, risk | 自由，风险 |
| Mountain | Challenge, achievement | 挑战，成就 |
| Mouse | Timidity, detail | 胆怯，细节 |
| Movies | Life story viewing | 观看生命故事 |
| Moving | Life transition | 生活过渡 |
| Mug | Comfort, containment | 舒适，容纳 |
| Muscles | Strength, effort | 力量，努力 |
| Music | Emotional expression | 情感表达 |

### N-O (66 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Nails | Protection, aggression | 保护，攻击 |
| Naked | Vulnerability, exposure | 脆弱，暴露 |
| Navel | Center, origin | 中心，起源 |
| Nazi | Shadow, oppression | 阴影，压迫 |
| Neck | Communication bridge | 沟通桥梁 |
| Necklace | Self-expression | 自我表达 |
| Needle | Precision, pain | 精确，疼痛 |
| Nephew | Family extension | 家庭延展 |
| Nest | Home, security | 家，安全 |
| Net | Entrapment, catching | 陷阱，捕获 |
| Newspaper | Current events | 时事 |
| Niece | Family extension | 家庭延展 |
| Nightmares | Shadow calling | 阴影呼唤 |
| Nighttime | Unconscious | 无意识 |
| Nine | Completion, wisdom | 完成，智慧 |
| Nipples | Nurturance, sensitivity | 养育，敏感 |
| Noose | Restriction, danger | 限制，危险 |
| Nose | Intuition, curiosity | 直觉，好奇 |
| Numbers | Meaning, order | 含义，秩序 |
| Numbness | Disconnection | 断开连接 |
| Nun | Devotion, celibacy | 奉献，独身 |
| Nurse | Care, healing | 照顾，疗愈 |
| Oasis | Relief, resource | 缓解，资源 |
| Obelisk | Masculine power | 男性力量 |
| Obesity | Excess, protection | 过度，保护 |
| Obstacles | Challenges | 挑战 |
| Ocean | Collective unconscious | 集体无意识 |
| Octopus | Multitasking | 多任务 |
| Office | Work, productivity | 工作，生产力 |
| Oil | Wealth, lubrication | 财富，润滑 |
| Old | Wisdom, past | 智慧，过去 |
| Olympics | Achievement, competition | 成就，竞争 |
| One | Unity, beginning | 统一，开始 |
| Onions | Layers, tears | 层次，眼泪 |
| Operation | Major change | 重大变化 |
| Orange | Creativity, vitality | 创造力，活力 |
| Oranges | Health, sunshine | 健康，阳光 |
| Orbs | Spirit presence | 精神存在 |
| Orchestra | Harmony, cooperation | 和谐，合作 |
| Organ | Vital function | 重要功能 |
| Organs | Body systems | 身体系统 |
| Orgasm | Release, pleasure | 释放，快乐 |
| Orgy | Multiple integration | 多重整合 |
| Origami | Transformation, patience | 转化，耐心 |
| Orphan | Abandonment, independence | 被遗弃，独立 |
| Ostrich | Avoidance, denial | 回避，否认 |
| Otter | Playfulness, feminine | 玩乐，女性 |
| Outlet | Energy release | 能量释放 |
| Ovaries | Feminine creativity | 女性创造力 |
| Oven | Transformation, creation | 转化，创造 |
| Owl | Wisdom, night vision | 智慧，夜视 |

### P-Q (82 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Pacifier | Comfort, silencing | 舒适，沉默 |
| Package | Gift, unknown | 礼物，未知 |
| Packing | Preparation, organizing | 准备，组织 |
| Pageant | Competition, display | 竞争，展示 |
| Paint | Expression, covering | 表达，覆盖 |
| Painting | Creative vision | 创造视野 |
| Palace | Grandeur, aspiration | 宏伟，抱负 |
| Panda | Gentleness, balance | 温柔，平衡 |
| Pants | Covering, identity | 覆盖，身份 |
| Paparazzi | Intrusion, exposure | 侵入，暴露 |
| Paper | Communication, fragility | 沟通，脆弱 |
| Parachute | Safety, rescue | 安全，救援 |
| Parade | Celebration, display | 庆祝，展示 |
| Paralyzed | Stuck, powerless | 卡住，无力 |
| Parents | Authority, origins | 权威，起源 |
| Park | Recreation, nature | 娱乐，自然 |
| Parrot | Imitation, communication | 模仿，沟通 |
| Party | Celebration, social | 庆祝，社交 |
| Passport | Identity, permission | 身份，许可 |
| Path | Direction, journey | 方向，旅程 |
| Paycheck | Value, reward | 价值，奖赏 |
| Peacock | Beauty, display | 美丽，展示 |
| Pearl | Wisdom from pain | 从痛苦中获得智慧 |
| Pebble | Small foundation | 小基础 |
| Pen | Communication power | 沟通力量 |
| Pencil | Temporary expression | 临时表达 |
| Penis | Masculine power | 男性力量 |
| Pentagram | Spiritual protection | 灵性保护 |
| Phone | Communication need | 沟通需求 |
| Phosphorescence | Inner light | 内在光 |
| Piano | Emotional expression | 情感表达 |
| Picnic | Relaxed nourishment | 放松的滋养 |
| Piercing | Penetration, expression | 穿透，表达 |
| Pig | Abundance, greed | 丰富，贪婪 |
| Pills | Quick fix, healing | 快速修复，疗愈 |
| Pink | Love, femininity | 爱，女性气质 |
| Pipe | Flow, direction | 流动，方向 |
| Platypus | Uniqueness, oddity | 独特，奇特 |
| Playground | Inner child, play | 内在小孩，玩耍 |
| Pointing | Direction, accusation | 方向，指控 |
| Poison | Toxicity, danger | 毒性，危险 |
| Poker | Strategy, risk | 策略，风险 |
| Police | Authority, protection | 权威，保护 |
| Pond | Small emotions | 小情感 |
| Pool | Contained emotions | 被包含情感 |
| Porch | Transition space | 过渡空间 |
| Porn | Sexual shadow | 性阴影 |
| Posture | Attitude, presentation | 态度，呈现 |
| Pregnancy | Creative potential | 创造潜能 |
| Present | Gift, now | 礼物，现在 |
| Press | Pressure, publicity | 压力，公开 |
| Priest | Spiritual authority | 灵性权威 |
| Prison | Restriction, consequence | 限制，后果 |
| Prostitute | Shadow sexuality | 阴影性欲 |
| Pumpkin | Harvest, transformation | 收获，转化 |
| Puppet | Control, manipulation | 控制，操纵 |
| Puppy | Playfulness, innocence | 玩乐，纯真 |
| Purple | Spirituality, royalty | 灵性，皇室 |
| Purse | Identity, resources | 身份，资源 |
| Pyramids | Ancient wisdom | 古老智慧 |
| Quarry | Mining resources | 开采资源 |
| Quartet | Harmony, four | 和谐，四 |
| Quartz | Clarity, amplification | 清晰，放大 |
| Queen | Feminine power | 女性力量 |
| Quicksand | Stuck, sinking | 卡住，下沉 |
| Quilt | Warmth, piecing together | 温暖，拼凑 |
| Quiz | Testing, evaluation | 测试，评估 |

### R-S (124 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Rabbi | Spiritual teacher | 灵性老师 |
| Rabbit | Fertility, fear | 生育，恐惧 |
| Raccoon | Curiosity, mischief | 好奇，恶作剧 |
| Radiator | Warmth source | 温暖源 |
| Radio | Messages, communication | 信息，沟通 |
| Railing | Support, boundary | 支持，边界 |
| Railroad | Destiny path | 命运道路 |
| Rain | Cleansing, release | 净化，释放 |
| Rainbow | Promise, hope | 承诺，希望 |
| Rainforest | Unconscious abundance | 无意识丰富 |
| Ramp | Gradual transition | 渐进过渡 |
| Rape | Violation, powerlessness | 侵犯，无力 |
| Rapids | Emotional turbulence | 情感动荡 |
| Rash | Irritation, reaction | 刺激，反应 |
| Rats | Survival, shadow | 生存，阴影 |
| Red | Passion, anger | 激情，愤怒 |
| Refrigerator | Preservation, cooling | 保存，冷却 |
| Rehearsal | Preparation, practice | 准备，练习 |
| Reporter | Truth seeking | 寻求真相 |
| Reptile | Primitive instincts | 原始本能 |
| Reservoir | Stored emotions | 储存情感 |
| Resort | Relaxation, escape | 放松，逃避 |
| Restaurant | Nourishment, social | 滋养，社交 |
| Resurrection | Rebirth, renewal | 重生，更新 |
| Revolution | Major change | 重大变化 |
| Rhino | Power, protection | 力量，保护 |
| Ribbon | Decoration, gift | 装饰，礼物 |
| Ring | Commitment, wholeness | 承诺，完整 |
| Rip | Damage, separation | 损坏，分离 |
| Ritual | Sacred practice | 神圣实践 |
| River | Life flow, emotions | 生命流，情感 |
| Road | Life path | 人生道路 |
| Roadkill | Stopped progress | 停止进步 |
| Robots | Automation, soulless | 自动化，无灵魂 |
| Rocks | Stability, obstacles | 稳定，障碍 |
| Roof | Protection, limits | 保护，限制 |
| Rooster | Awakening, masculinity | 觉醒，男性气质 |
| Rope | Connection, binding | 连接，绑定 |
| Roses | Love, beauty | 爱，美丽 |
| Rug | Comfort, covering | 舒适，覆盖 |
| Running | Escaping, pursuing | 逃避，追求 |
| Sacrifice | Letting go, devotion | 放手，奉献 |
| Safari | Adventure, wild | 冒险，野性 |
| Safe | Security, protection | 安全，保护 |
| Salesperson | Persuasion, exchange | 说服，交换 |
| Salon | Self-care, transformation | 自我照顾，转化 |
| Sand | Instability, time | 不稳定，时间 |
| Sandals | Casual grounding | 随意接地 |
| Sandstorm | Confusion, obscuring | 困惑，遮蔽 |
| Satellite | Communication, observation | 沟通，观察 |
| Saw | Cutting, division | 切割，分裂 |
| Scaffolding | Temporary support | 临时支持 |
| Scarf | Protection, expression | 保护，表达 |
| Scars | Past wounds visible | 过去伤口可见 |
| School | Learning, development | 学习，发展 |
| Scorpion | Danger, transformation | 危险，转化 |
| Scrubs | Medical, cleaning | 医疗，清洁 |
| Sculpture | Formed creativity | 形成的创造力 |
| Seagulls | Messages, shore | 信息，海岸 |
| Seatbelt | Safety, restraint | 安全，约束 |
| Seeds | Potential, beginning | 潜能，开始 |
| Seizure | Confusion, chaos | 困惑，混乱 |
| Semen | Creative potential | 创造潜能 |
| Seminar | Learning gathering | 学习聚会 |
| Sentencing | Consequences | 后果 |
| Sequins | Attention seeking | 寻求关注 |
| Seven | Spirituality | 灵性 |
| Sewer | Hidden waste | 隐藏废物 |
| Sewing | Joining, creating | 连接，创造 |
| Sex | Integration, union | 整合，结合 |
| Shadows | Rejected aspects | 被拒面向 |
| Shark | Fear, power | 恐惧，力量 |
| Shaving | Softening, grooming | 软化，梳理 |
| Sheep | Following, innocence | 跟随，纯真 |
| Shelf | Storage, display | 储存，展示 |
| Ship | Emotional journey | 情感旅程 |
| Shipwreck | Emotional disaster | 情感灾难 |
| Shirt | Self-expression | 自我表达 |
| Shoes | Life walk, grounding | 生活行走，接地 |
| Shopping | Self-care, needs | 自我照顾，需求 |
| Shower | Cleansing | 清洁 |
| Shrinking | Diminishing | 缩小 |
| Siblings | Family dynamics | 家庭动态 |
| Sidewalk | Social path | 社交道路 |
| Silver | Secondary value | 次要价值 |
| Silverware | Civilization | 文明 |
| Singing | Passionate expression | 激情表达 |
| Sink | Emotional release | 情感释放 |
| Sister | See Siblings | 见兄弟姐妹 |
| Six | Partnership | 伙伴关系 |
| Skateboard | Youth, speed | 青春，速度 |
| Skeleton | Hidden structure | 隐藏结构 |
| Skin | Protection, vulnerability | 保护，脆弱 |
| Skunk | Defense, reputation | 防御，名誉 |
| Sky | Aspiration, limitless | 抱负，无限 |
| Skydiving | Risk, letting go | 风险，放手 |
| Skyscraper | High consciousness | 高意识 |
| Slave | Bondage, overwork | 束缚，过度工作 |
| Slavery | Oppression | 压迫 |
| Sled | Movement on cold | 在冷中移动 |
| Sleeping | Unconsciousness | 无意识 |
| Slide | Release, play | 释放，玩耍 |
| Slippers | Relaxation | 放松 |
| Slum | Neglected area | 被忽视区域 |
| Smells | Memory, sense | 记忆，感觉 |
| Smile | Joy, connection | 快乐，连接 |
| Smoke | Obscuring, change | 遮蔽，变化 |
| Smoking | Unhealthy choices | 不健康选择 |
| Snail | Slow pace | 缓慢步伐 |
| Snake | Transformation, healing | 转化，疗愈 |
| Sneakers | Readiness, effort | 准备，努力 |
| Snow | Frozen emotions | 冻结情感 |
| Soap | Cleansing | 清洁 |
| Soldier | Protection, sacrifice | 保护，牺牲 |
| Soup | Nourishment, comfort | 滋养，舒适 |
| Spark | Potential, ignition | 潜能，点燃 |
| Speech | Expression, authority | 表达，权威 |
| Speeding | Rushing, urgency | 匆忙，紧急 |
| Speedometer | Pace awareness | 步伐意识 |
| Sperm | Creative potential | 创造潜能 |
| Spider | Creativity, fate | 创造力，命运 |
| Spine | Support, backbone | 支持，骨干 |
| Spiral | Evolution, cycles | 进化，周期 |
| Splinter | Small irritation | 小刺激 |
| Sponge | Absorption | 吸收 |
| Spoon | Nourishment | 滋养 |
| Spotlight | Attention, exposure | 关注，暴露 |
| Sprinklers | Emotional distribution | 情感分配 |
| Squirrel | Preparation, storing | 准备，储存 |
| Stabbing | Betrayal, aggression | 背叛，攻击 |
| Stadium | Collective event | 集体事件 |
| Stage | Performance, display | 表演，展示 |
| Stain | Permanent mark | 永久标记 |
| Stairs | Progress, levels | 进步，层次 |
| Stars | Aspiration, guidance | 抱负，指引 |
| Statue | Permanence, memory | 永恒，记忆 |
| Stealing | Taking what's not yours | 拿走不属于你的 |
| Stepfamily | Blended dynamics | 混合动态 |
| Stepparents | Secondary authority | 次要权威 |
| Stepsiblings | Extended family | 延展家庭 |
| Stigmata | Spiritual suffering | 灵性苦难 |
| Stockings | Femininity, sexuality | 女性气质，性欲 |
| Stones | Foundation, obstacles | 基础，障碍 |
| Store | Resources, abundance | 资源，丰富 |
| Storm | Emotional turmoil | 情感动荡 |
| Stove | Transformation, nourishment | 转化，滋养 |
| Stranger | Unknown self-aspect | 未知自我面向 |
| Strangling | Communication cut | 沟通切断 |
| Street | Public path | 公共道路 |
| Stroke | Sudden change | 突然变化 |
| Submarine | Deep unconscious | 深层无意识 |
| Subway | Underground journey | 地下旅程 |
| Succubus | Sexual shadow | 性阴影 |
| Suit | Professional identity | 专业身份 |
| Suitcase | Emotional baggage | 情感包袱 |
| Sun | Consciousness, vitality | 意识，活力 |
| Surgery | Major change | 重大变化 |
| Sweat | Effort, anxiety | 努力，焦虑 |
| Sweating | Release, worry | 释放，担忧 |
| Swimming | Emotional navigation | 情感导航 |
| Swimsuit | Exposed vulnerability | 暴露的脆弱 |
| Swings | Back and forth | 来回摆动 |

### T-Z (95 symbols)

| Symbol | English Meaning | Chinese 含义 |
|--------|----------------|--------------|
| Table | Foundation, gathering | 基础，聚会 |
| Tadpoles | Pre-transformation | 转化前 |
| Tail | Instinct, balance | 本能，平衡 |
| Tampon | Feminine cycle | 女性周期 |
| Tape | Binding, repair | 绑定，修复 |
| Tapestry | Woven story | 编织的故事 |
| Tar | Stuck, slow | 卡住，缓慢 |
| Tarot | Divination, insight | 占卜，洞见 |
| Tattoo | Permanent expression | 永久表达 |
| Taxes | Obligations | 义务 |
| Taxi | Directed journey | 被引导的旅程 |
| Tea | Comfort, ritual | 舒适，仪式 |
| Teacher | Wisdom, learning | 智慧，学习 |
| Teeth | Power, communication | 力量，沟通 |
| Telephone | Communication | 沟通 |
| Television | Passive viewing | 被动观看 |
| Temple | Spiritual space | 灵性空间 |
| Termite | Hidden destruction | 隐藏破坏 |
| Terrorist | Shadow fear | 阴影恐惧 |
| Test | Evaluation | 评估 |
| Testicles | Masculine power | 男性力量 |
| Texting | Brief communication | 简短沟通 |
| Theater | Performance, life stage | 表演，生命舞台 |
| Therapist | Healing guide | 疗愈指引 |
| Three | Creativity, expression | 创造力，表达 |
| Throat | Communication center | 沟通中心 |
| Thunder | Powerful message | 有力信息 |
| Tick | Draining, time | 消耗，时间 |
| Ticket | Permission, access | 许可，进入 |
| Tie | Professional restraint | 专业约束 |
| Tiger | Power, passion | 力量，激情 |
| Tightrope | Balance, risk | 平衡，风险 |
| Tiptoe | Caution, secrecy | 小心，秘密 |
| Tires | Movement support | 移动支持 |
| Toes | Balance, details | 平衡，细节 |
| Toilet | Releasing | 释放 |
| Tomb | Death, endings | 死亡，结束 |
| Tombstone | Memorial, past | 纪念，过去 |
| Tongue | Expression, taste | 表达，品味 |
| Tools | Capabilities | 能力 |
| Toothbrush | Self-care detail | 自我照顾细节 |
| Toothpaste | Cleansing, freshness | 清洁，新鲜 |
| Top | Achievement, peak | 成就，顶峰 |
| Torch | Illumination, guidance | 照明，指引 |
| Tornado | Overwhelming change | 压倒性变化 |
| Torture | Suffering, shadow | 苦难，阴影 |
| Tour | Exploration | 探索 |
| Tower | Isolation, perspective | 孤立，视角 |
| Toys | Childhood, play | 童年，玩耍 |
| Tractor | Work, productivity | 工作，生产力 |
| Traffic | Life congestion | 生活拥堵 |
| Trail | Journey path | 旅程道路 |
| Trailer | Temporary home | 临时家 |
| Train | Collective journey | 集体旅程 |
| Transsexual | Gender integration | 性别整合 |
| Traveling | Life journey | 生命旅程 |
| Treadmill | Going nowhere | 原地踏步 |
| Tree | Growth, life, roots | 成长，生命，根 |
| Trial | Testing, judgment | 测试，判断 |
| Truck | Heavy carrying | 沉重承载 |
| Tsunami | Overwhelming emotions | 压倒性情感 |
| Tumor | Hidden growth | 隐藏生长 |
| Tunnel | Transition, passage | 过渡，通道 |
| Turkey | Abundance, gratitude | 丰富，感恩 |
| Turtle | Protection, patience | 保护，耐心 |
| Two | Partnership, duality | 伙伴关系，二元 |
| Ukulele | Light expression | 轻松表达 |
| Umbrella | Protection from emotions | 免受情感 |
| Uncle | Extended family | 延展家庭 |
| Undertow | Hidden current | 隐藏潮流 |
| Underwater | Deep unconscious | 深层无意识 |
| Underwear | Hidden identity | 隐藏身份 |
| Undress | Vulnerability, exposure | 脆弱，暴露 |
| Unicorn | Magic, purity | 魔法，纯净 |
| Uniform | Group identity | 群体身份 |
| Uphill | Effort, challenge | 努力，挑战 |
| Upstairs | Higher consciousness | 更高意识 |
| Urinal | Public release | 公开释放 |
| Urination | Release | 释放 |
| Usher | Guide, direction | 指引，方向 |
| Uvula | Communication detail | 沟通细节 |
| Vacation | Rest, escape | 休息，逃避 |
| Vaccine | Protection, prevention | 保护，预防 |
| Vacuum | Emptiness, cleaning | 空虚，清洁 |
| Vagina | Feminine power | 女性力量 |
| Valentine | Love expression | 爱的表达 |
| Valet | Service, trust | 服务，信任 |
| Valley | Low point, shelter | 低点，庇护 |
| Vampire | Energy drain | 能量消耗 |
| Van | Collective transport | 集体运输 |
| Vase | Containment, beauty | 容纳，美丽 |
| Vault | Security, secrets | 安全，秘密 |
| Vegetables | Health, growth | 健康，成长 |
| Veil | Hiding, mystery | 隐藏，神秘 |
| Ventriloquist | Hidden voice | 隐藏声音 |
| Vest | Protection layer | 保护层 |
| Veterinarian | Animal healing | 动物疗愈 |
| Video | Recording life | 记录生活 |
| Viking | Warrior, adventure | 战士，冒险 |
| Vineyard | Cultivation, prosperity | 培养，繁荣 |
| Violet | Spirituality | 灵性 |
| Vitamins | Self-care | 自我照顾 |
| Volcano | Explosive emotions | 爆炸性情感 |
| Vomiting | Rejection, release | 拒绝，释放 |
| Voodoo | Magic, manipulation | 魔法，操纵 |
| Voting | Choice, voice | 选择，声音 |
| Vulture | Death, transformation | 死亡，转化 |
| Wading | Testing emotions | 测试情感 |
| Wagon | Early journey | 早期旅程 |
| Waiter | Service, waiting | 服务，等待 |
| Wake | After death, awareness | 死后，觉察 |
| Wall | Barrier, protection | 障碍，保护 |
| Wallet | Identity, resources | 身份，资源 |
| Wallpaper | Surface covering | 表面覆盖 |
| Wand | Magic power | 魔法力量 |
| War | Conflict, struggle | 冲突，斗争 |
| Warehouse | Storage, resources | 储存，资源 |
| Warts | Imperfections | 不完美 |
| Washing | Cleansing | 清洁 |
| Wasp | Aggression, sting | 攻击，刺痛 |
| Watch | Time awareness | 时间意识 |
| Water | Emotions, unconscious | 情感，无意识 |
| Waves | Emotional movement | 情感移动 |
| Wedding | Union, commitment | 结合，承诺 |
| Weeds | Unwanted growth | 不想要的生长 |
| Weights | Burden, strength | 负担，力量 |
| Well | Deep resources | 深层资源 |
| Welts | Visible wounds | 可见伤口 |
| Werewolf | Shadow transformation | 阴影转化 |
| Whale | Deep emotions, wisdom | 深层情感，智慧 |
| Wheel | Cycles, movement | 周期，移动 |
| Wheelchair | Limited mobility | 有限移动 |
| Whirlpool | Emotional vortex | 情感漩涡 |
| Whisper | Secret communication | 秘密沟通 |
| White | Purity, potential | 纯净，潜能 |
| Wig | False identity | 虚假身份 |
| Will | Legacy, endings | 遗产，结束 |
| Wind | Change, thoughts | 变化，思想 |
| Window | Perspective, opportunity | 视角，机会 |
| Wine | Celebration, spirit | 庆祝，精神 |
| Wings | Transcendence, freedom | 超越，自由 |
| Witch | Magic, shadow feminine | 魔法，阴影女性 |
| Wizard | Magic, transformation | 魔法，转化 |
| Wolf | Instincts, belonging | 本能，归属 |
| Womb | Gestation, creation | 孕育，创造 |
| Wood | Nature, building | 自然，建设 |
| Work | Responsibilities | 责任 |
| Wreath | Cycles, continuity | 周期，连续 |
| Yard | Public/private boundary | 公共/私人边界 |
| Yarmulke | Devotion, identity | 奉献，身份 |
| Yelling | Anger, urgency | 愤怒，紧急 |
| Yellow | Emotions, caution | 情绪，谨慎 |
| Yoga | Integration, discipline | 整合，纪律 |
| Yogurt | Transformation benefit | 转化益处 |
| Zebra | Individuality | 个性 |
| Zero | Emptiness, potential | 空虚，潜能 |
| Zipper | Control, release | 控制，释放 |
| Zodiac | Archetypes | 原型 |
| Zombie | Lifeless, unconscious | 无生气，无意识 |
| Zoo | Repressed instincts | 被压抑本能 |

---

## PART 4: Symbol Category Cross-Reference

### By Psychological Function

| Function | Symbols | 心理功能 |
|----------|---------|----------|
| **Self-Worth** | Abandonment, Teeth, Nakedness, Money | 自我价值 |
| **Transformation** | Death, Snake, Fire, Butterfly | 转化 |
| **Emotions** | Water, Ocean, Flood, Rain, Drowning | 情感 |
| **Unconscious** | Basement, Ocean, Forest, Night | 无意识 |
| **Power/Control** | Flying, Falling, Chase, Car, Teeth | 力量/控制 |
| **Relationships** | Mother, Father, Marriage, Baby | 关系 |
| **Life Path** | Road, Car, Train, Bridge, Door | 人生道路 |
| **Growth** | Tree, Flower, Stairs, Ladder | 成长 |
| **Shadow** | Chase, Nightmare, Shadow Figure, Vampire | 阴影 |
| **Spirituality** | Angel, Church, Light, Sun, Sky | 灵性 |

### By Element Correspondence

| Element | Symbols | 五行对应 |
|---------|---------|----------|
| **Water (情感)** | Ocean, Lake, Rain, Flood, Fish | 水 |
| **Fire (激情)** | Fire, Sun, Volcano, Candle | 火 |
| **Earth (稳定)** | Mountain, House, Tree, Stone | 土 |
| **Air (思维)** | Flying, Bird, Wind, Sky | 气/风 |

---

## Final Completion Summary

### Coverage Statistics

| Category | Full L1+L2+Factor | Index Entry | Total |
|----------|-------------------|-------------|-------|
| **Framework Concepts** | 7 | - | 7 |
| **Core Symbols** | 15 | - | 15 |
| **A-Z Index Symbols** | - | **989** | **989** |
| **Cross-References** | - | 50+ | 50+ |

### Content Summary

**完成条目**: 22个完整精校条目 (L1+L2+Factor+L2.5) + **989个**索引条目

**叙事素材**: ns_llewellyn_001 - ns_llewellyn_052 (**52个**)

**双语术语**: 1000+个 (每个符号英中双语)

**覆盖内容**:
- ✅ 荣格理论框架 (7概念完整L1+L2+Factor+L2.5)
- ✅ 核心梦境象征 (15符号完整L1+L2+Factor+L2.5)
- ✅ **完整A-Z象征索引 (989个符号全覆盖)**
- ✅ 象征分类交叉引用 (心理功能、元素对应)

**原文覆盖**: 1478行原文/989符号 → 3400+行精校 = **100%完整覆盖**

### East-West Integration

| Lennox Concept | 东方对应 |
|----------------|----------|
| Collective Unconscious | 共同心象/藏识 |
| Character Aspects | 梦中人物映射自我 |
| Shadow | 噩梦/魔障 |
| Masculine/Feminine | 阴阳平衡 |
| Universal Meanings | 通用吉凶 |
| Inner Circle | 向内求/内观 |

---

**文件状态**: Llewellyn's Complete Dictionary of Dreams - 精校完成 ✅  
**完成日期**: 2025-11-29  
**模板**: Western Texts v2.1 Bilingual  
**作者**: Dr. Michael Lennox  
**精校标准**: 按Western_Texts_Template.md逐条对齐"""
    normalized_text_zh: str = """"""
    subject: str = "Teeth Falling Out"
    factor_refs: list = ['source_ref']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="llewellyns_dreams",
        chapter="",
        l1_anchor="ld_v1.0.0_teeth_falling_out_001_L1",
    )
    version: str = "1.0.0"
