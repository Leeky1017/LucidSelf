"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994528
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
    semantic_id="pt_v1.0.0_card_11__justice_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card11Justice(SemanticEntry):
    """
    ### Responsibility, Balance, and Response to Vision

#### Key Term Analysis

| Term | Definition | S...
    """
    
    original_text: str = """### Responsibility, Balance, and Response to Vision

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 11 | Midpoint of 22 | Balance center |
| No Blindfold | Must see truth | vs Legal Justitia |
| Self-Creation | Actions form character | Responsibility |
| Sword of Wisdom | Cuts through mystery | Understanding |

**Source Text**: Justice indicates an understanding of the vision shown in the Wheel of Fortune. The way to understanding lies in responsibility. As long as we believe that our past lives just happen, that we do not bring our own selves into existence through every thing we do, then the past remains a mystery, and the future an endlessly turning wheel, empty of meaning. But when we accept that every event in our lives has helped to form our characters, and that in the future we will continue to create ourselves through our actions, then the sword of wisdom cuts through the mystery.

**English Paraphrase**:

**Justice** = **Responsibility**, **Understanding**, **Conscious Response** — accepting that we create ourselves through our actions.

**Waite's Switch** (recap):
- **Traditional**: Justice = 8, Strength = 11
- **Waite/Golden Dawn**: Justice = 11, Strength = 8
- **Reason**: Initiation sequence requires Strength first (courage to begin), then Justice (response to vision)

**Core Symbolism**:
- **Number 11**: Adds to 2 (High Priestess), but higher version of 1 (Magician) and lesser version of 21 (World)
- **Center of Major Arcana**: Exact midpoint (card 11 of 22), balance point between past and future

**Visual Elements** (Rider-Waite-Smith):
- **Figure between two pillars** with veil = echo of High Priestess, but active not passive
- **No blindfold** (unlike legal Justitia) = must **see truth** to advance spiritually
- **Sword pointing up** = wisdom piercing illusion, resolve, two-edged choice
- **Balanced scales** = perfect equilibrium of past and future, not in time but in sight
- **Red robe** = action, passion (Magician quality)
- **Yellow crown/background** = mental force, thinking about life
- **Purple veil** = inner wisdom
- **Androgynous appearance** = union of masculine/feminine principles
- **One foot out, one hidden** = poised between stillness and action

**Philosophical Meaning**:

**Responsibility ≠ Control**:

**What it DOES mean**:
- Every event helps **form your character**
- You **create yourself** through actions
- Past actions become **part of you** (cannot be revoked)
- Future self formed by **actions taken now**
- Life demands **response** to every event (not moral requirement, just fact)

**What it DOES NOT mean**:
- **Not**: Invisible control over outer world (e.g., willing earthquake to destroy house)
- **Not**: Moral judgment or blame
- **Not**: Controlling what happens in vast, strange universe
- Understanding includes **accepting limitations** of physical existence

**The Freedom Paradox**:
- By accepting responsibility, we **paradoxically free ourselves** from past
- Like Buddha remembering all lives: **Only conscious awareness liberates**
- Otherwise, constantly **repeat past behavior**
- Ego-mask **controls us** as long as we won't admit forging it ourselves

**Action vs. Movement**:

**First line illusion**: Confuse **doing things** with **action**
- Active principle = pointless movement without understanding
- Pushed from event to event like **machines** (truly passive)

**Real action**:
- Arises from **understanding**
- Brings **meaning and value** to life
- Purpose of second line: Not abandon action but **awaken it**

**Magician + High Priestess United**:

**Complete synthesis**:
- **Digits**: 11 adds to 2 (High Priestess)
- **Visual**: Woman between pillars (High Priestess) in red robe, one arm up/down (Magician)
- **Truth**: Action arises from self-knowledge; wisdom arises from action
- **Inextricably combined** like:
  - Male/female snakes twined (kundalini, Hermes's caduceus)
  - Double helix of DNA

**Wisdom requires thinking**:
- Not spontaneous
- Must **think about lives** to understand
- But thinking goes nowhere without **clear vision of truth**

**Initiation Sequence**:

**Pattern** (all initiations follow):
1. **Strength (8)**: Courage to become neophyte, open channels to unconscious
2. **Hermit (9)**: Instruction, meditation, receptivity
3. **Wheel (10)**: Vision of cult's mysteries shown dramatically
4. **Justice (11)**: **Candidate must respond** ← Crucial moment!

**Grail initiation example**:
- Vision shown: Grail procession, wounded king, attendant symbols
- **Response required**: Question "What is meaning?" or "Whom does Grail serve?"
- Without question/response = **initiation cannot continue**
- Asking shows **recognition of being part of process**, responsible for outcome

**Psychological parallel**:
- Wheel = vision of your life (events, who you are, what you've made)
- Justice = **understanding** that vision through responsibility

**Free Will Reality Check**:

**Common mistake**:
- Tarot reading shows disaster likely
- Person says "My free will allows me to change it"
- Goes ahead, outcome exactly as predicted
- **"Free will" used as excuse** to ignore valid projection

**Truth**:
- Free will **certainly exists**
- But **we don't know how to use it**
- Not enough to foresee outcome
- Must **understand why it's coming**
- Must **work on causes within ourselves**
- **Most important Tarot lesson**: How little we exercise freedom

**Narrative Snippets**:
- `[ns_78deg_129]` `[trigger: justice_major]` `[factor_trigger: tarot_major_justice AND tarot_number_11 AND symbol_balanced_scales AND symbol_wisdom_sword AND symbol_no_blindfold]` `[role: 主干]` Justice indicates understanding of the vision shown in Wheel of Fortune—the way to understanding lies in responsibility for self-creation. → Source Text
- `[ns_78deg_130]` `[trigger: self_creation]` `[factor_trigger: principle_self_creation]` `[role: 主干]` We create ourselves through everything we do; every event in our lives helps to form our characters; past actions become part of us. → Source Text
- `[ns_78deg_131]` `[trigger: responsibility_distinction]` `[factor_trigger: principle_responsibility_distinction]` `[role: 条件分支]` Self-creation does not mean external control—we don't destroy houses by wishing; understanding includes accepting physical existence's limitations. → English Paraphrase
- `[ns_78deg_132]` `[trigger: libra_ruler]` `[factor_trigger: sign_libra]` `[role: 主干依赖]` Libra rules Justice—balance, equilibrium, weighing; the scales as symbol of perfect balance between past and future in vision. → English Paraphrase
- `[ns_78deg_133]` `[trigger: midpoint_framework]` `[factor_trigger: framework_midpoint]` `[role: 条件分支]` Justice at card 11 is exact midpoint of 22 Major Arcana—balance point between past and future, uniting Magician (1) and High Priestess (2). → English Paraphrase
- `[ns_78deg_382]` `[trigger: no_blindfold_justice]` `[factor_trigger: tarot_major_justice AND symbol_vision]` `[role: 条件分支]` No blindfold (unlike legal Justitia)—must see truth to advance spiritually; sword pointing up = wisdom piercing illusion; balanced scales = perfect equilibrium. → Visual Elements
- `[ns_78deg_383]` `[trigger: freedom_paradox]` `[factor_trigger: tarot_major_justice AND principle_freedom]` `[role: 条件分支]` Freedom paradox: by accepting responsibility we free ourselves from past; like Buddha remembering all lives, only conscious awareness liberates from repetition. → Philosophical Meaning
- `[ns_78deg_384]` `[trigger: grail_response]` `[factor_trigger: tarot_major_justice AND myth_grail]` `[role: 条件分支]` Grail initiation requires response—asking "What is meaning?" shows recognition of being part of process; without question, initiation cannot continue. → Initiation Sequence
- `[ns_78deg_385]` `[trigger: free_will_lesson]` `[factor_trigger: tarot_major_justice AND principle_free_will]` `[role: 总结]` Most important Tarot lesson: how little we exercise freedom; free will exists but we don't know how to use it; must understand causes within ourselves. → Free Will Reality
- `[ns_78deg_134]` `[trigger: magician_priestess_unity]` `[factor_trigger: unity_magician_priestess]` `[role: 总结]` Justice = Magician + High Priestess (1+2=11)—action and wisdom inseparably intertwined; the sword cannot cut without the scales' vision. → English Paraphrase

**完整中文诠释**:
**正义**=**责任**、**理解**、**觉知回应**——接受我们通过行动创造自己。**Waite调换**（回顾）：**传统**：正义=8，力量=11；**Waite/金色黎明**：正义=11，力量=8；**理由**：启蒙序列需力量在先（开始勇气），然后正义（对愿景回应）。**数字11**：加为2（女祭司），但1（魔术师）的更高版本和21（世界）的较低版本；大阿卡纳中心：精确中点（22张牌的第11张），过去与未来间平衡点。**图像元素**（RWS牌）：带帷幕**双柱间人物**=呼应女祭司，但主动非被动；**无蒙眼**（不同于法律Justitia）=必须**看见真理**以灵性前进；**剑向上指**=智慧穿透假象、决心、双刃选择；**平衡天平**=过去与未来完美均衡，非在时间中而在视野中；**红袍**=行动、激情（魔术师品质）；**黄冠/背景**=心智力量、思考生命；**紫帷幕**=内在智慧；**雌雄同体外观**=阳性/阴性原则统一；**一脚外、一脚藏**=在静止与行动间悬停。**哲学意义**："责任≠控制"：**它意味着**：每个事件帮助**形成你的性格**；你通过行动**创造自己**；过往行动成为**你的一部分**（不可撤销）；未来自我被**现在采取的行动**形成；生命要求对每个事件**回应**（非道德要求，只是事实）。**它不意味着**：**非**：对外在世界的隐形控制（如意念摧毁房屋）；**非**：道德评判或责备；**非**：控制浩瀚奇异宇宙中发生之事；理解包括**接受**物质存在的限制。"自由悖论"：通过接受责任，我们**悖论性地从过去解放**；如佛陀忆起所有前世：**唯觉知觉察解放**；否则，持续**重复过往行为**；自我面具**控制我们**只要我们不承认自己锻造了它。**行动vs运动**："第一线幻象"：混淆**做事情**与**行动**；主动原则=无理解的无意义运动；从事件被推向事件如同**机器**（真正被动）。"真正行动"：源于**理解**；带来生命的**意义与价值**；第二线目的：不是放弃行动而是**唤醒**它。**魔术师+女祭司统一**："完整综合"：**数字**：11加为2（女祭司）；**视觉**：双柱间女子（女祭司）穿红袍、一臂上/下（魔术师）；**真理**：行动源于自我认知；智慧源于行动；**不可分割地结合**如同：阴/阳蛇缠绕（昆达里尼、赫密士节杖）；DNA双螺旋。"智慧需要思考"：非自发；必须**思考生命**以理解；但思考无处可去若无**清晰真理视野**。**启蒙序列**："模式"（所有启蒙遵循）：1.**力量（8）**：成为新手的勇气，向无意识开放通道；2.**隐者（9）**：指导、冥想、接受性；3.**轮（10）**：戏剧性展示教派奥秘之愿景；4.**正义（11）**：**候选者必须回应**←关键时刻！"圣杯启蒙例子"：展示愿景：圣杯行列、受伤国王、随从符号；**需要回应**：发问"何意义？"或"圣杯服务谁？"；无提问/回应=**启蒙无法继续**；发问显示**认识自己是过程一部分**，对结果负责。"心理平行"：轮=你生命愿景（事件、你是谁、你造就了什么）；正义=通过责任**理解**该愿景。**自由意志现实检验**："常见错误"：塔罗解读显示灾难可能；人说"我的自由意志允许我改变它"；继续前进，结果正如预测；**"自由意志"被用作托辞**以忽视有效投射。"真理"：自由意志**当然存在**；但**我们不知如何使用**；预见结果不够；必须**理解为何它来临**；必须**处理我们内在的因**；**塔罗最重要教训**：我们多么少地行使自由。


---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 11: Justice"
    factor_refs: list = ['tarot_major_justice', 'tarot_number_11', 'principle_self_creation', 'symbol_wisdom_sword', 'principle_response_required', 'principle_responsibility_distinction']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_card_11__justice_001_L1",
    )
    version: str = "1.0.0"
