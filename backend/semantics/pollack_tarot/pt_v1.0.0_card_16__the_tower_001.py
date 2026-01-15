"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994600
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
    semantic_id="pt_v1.0.0_card_16__the_tower_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card16TheTower(SemanticEntry):
    """
    ### Breakthrough, Liberation, Shattering Illusions

#### Key Term Analysis

| Term | Definition | Si...
    """
    
    original_text: str = """### Breakthrough, Liberation, Shattering Illusions

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 16 | 1+6=7 | Chariot destroyed |
| Lightning | Divine not angry | Grace (yod drops) |
| Dam Metaphor | Jung's consciousness | Blocks unconscious |
| Veil Torn | Temple opened | Deep liberation |

**Source Text**: The Devil is God's shadow. By embracing the Devil we set the psyche on a violent course leading to the explosion of the Tower. Jung described consciousness as a dam blocking free flow of the river of the unconscious. Temperance acts as a kind of sluice, letting the waters through at a controlled rate. The Tower blows away the dam completely, releasing the locked up energy as a flood. The veil across the temple is the conscious personality, protecting us from life itself.

**English Paraphrase**:

**The Tower** = **Violent Liberation**, **Shattering Consciousness**, **Divine Destruction** — explosion that frees repressed energy, breaks illusions.

**Core Symbolism**:
- **Number 16**: 1+6=7 (Chariot) — ego structure destroyed vs. Chariot's ego triumph
- **Tower/House**: God's House or Devil's House (both names used)

**Visual Elements** (Rider-Waite-Smith):
- **Lightning bolt** from sky striking tower
- **Crown blown off top** = gold crown of ego/materialism
- **Two figures falling** = people thrown from false security
- **Drops of fire shaped like yod** (Hebrew letter) = first letter of God's name = **grace not anger**
- **Grey stone tower** = prison of narrow materialism
- **Black background** = chaos, destruction
- **Flames/explosions** = energy released violently

**Dual Interpretations**:

**1. Moral/Surface Meaning**:

**Tower = materialist conception** of universe:
- Life based on wealth, fame, physical pleasure
- Ignoring introspection and spiritual beauty
- **Prison raised around oneself** (grey, rock-bound, gold crown)

**Lightning = destruction**:
- Comes to life based on purely materialist principles
- **But**: Not outside force — derives from **psychological principles**
- Pressure builds as unconscious strains at bonds
- Dreams disturbed, arguments, depression
- If repressed further → **unconscious explodes**

**External disasters**:
- Friends/family turn against you
- Work collapses
- Violence swirls around
- **Mystery**: Bad luck comes in clusters
- **Truth**: Problems result from long neglected/mishandled situations
- Strike at moment we become vulnerable
- **Coincidence** shows life contains more than visible

**2. Esoteric/Deep Meaning**:

**If Devil = release of repressed energy**:
- Tower = **illusion shattered** is consciousness itself
- **Veil of the temple torn open** (not just materialism destroyed)

**Jung's metaphor**:
- Consciousness = **dam blocking** unconscious river's free flow
- **Temperance** = sluice (controlled rate)
- **Tower** = **dam blown away** (flood released)

**Why necessary?**

**No other way** to:
- Finally go beyond barrier of consciousness
- Break free from what separates life into opposites
- Break free from what cuts us off from pure energy within

**Veil across temple** = conscious personality:
- **Protects us** from life itself
- Mystics/shamans testify: **Eternity all around us**, blinding, overwhelming
- Unprepared mind cannot encompass such power
- Consciousness = **protective barrier**

**But**:
- To reach unity with life, **veil must be torn**
- Requires **violent breakthrough**
- Tower = necessary destruction for liberation

**Yod Drops** (Hebrew letter):
- Shaped like drops of fire falling
- **First letter of God's name** (YHVH)
- Not anger but **grace**
- Universe/human mind **will not allow** us stay imprisoned forever
- If cannot free peacefully → **forces of life arrange explosion**

**Not Enjoyable**:
- Don't enjoy painful experiences that shake us loose
- Can't see beneficial ends from such means
- **Process doesn't always result in freedom**
- Often series of disasters **cripples** once-strong personality
- **Point**: Given no other outlets, unconscious will erupt
- Can use experience to find better balance

**Devil's House = God's House**:

**Deeper meaning**:
- Hebrew: "Snake" = same numerical value as "Messiah"
- **Devil is God's shadow**
- Person seeking unity **must bring out repressed energy** (Devil)
- But endangers Temperance's calm/balance
- **Violent course** = necessary price

**Narrative Snippets**:
- `[ns_78deg_173]` `[trigger: tower_major]` `[factor_trigger: tarot_major_tower AND sequence_devil_tower AND state_breakthrough AND tarot_number_16 AND symbol_lightning_tower AND state_veil_torn]` `[role: 主干]` Tower represents violent breakthrough shattering consciousness dam—not punishment but grace; universe refuses to let us remain imprisoned forever. → English Paraphrase
- `[ns_78deg_174]` `[trigger: mars_aries_ruler]` `[factor_trigger: planet_mars, sign_aries]` `[role: 主干依赖]` Mars and Aries rule Tower—violent action, sudden force, fire element of explosive transformation; the lightning strike. → English Paraphrase
- `[ns_78deg_339]` `[trigger: dam_metaphor]` `[factor_trigger: tarot_major_tower AND symbol_dam]` `[role: 主干依赖]` Jung's dam metaphor: consciousness blocks unconscious river; Temperance = sluice (controlled rate), Tower = dam blown away releasing flood of locked-up energy. → Source Text
- `[ns_78deg_340]` `[trigger: yod_drops_grace]` `[factor_trigger: tarot_major_tower AND symbol_yod]` `[role: 条件分支]` Drops of fire shaped like yod (first letter of YHVH)—not anger but grace; universe arranges explosion if we cannot free ourselves peacefully. → Yod Drops
- `[ns_78deg_341]` `[trigger: tower_crown]` `[factor_trigger: tarot_major_tower AND symbol_crown]` `[role: 条件分支]` Crown blown off top—gold crown of ego/materialism; grey stone tower as prison of narrow materialism; two figures falling from false security. → Visual Elements
- `[ns_78deg_342]` `[trigger: veil_temple]` `[factor_trigger: tarot_major_tower AND principle_liberation]` `[role: 条件分支]` Veil across temple = conscious personality protecting us from overwhelming eternity; to reach unity with life, veil must be violently torn. → Esoteric Meaning
- `[ns_78deg_343]` `[trigger: devil_god_shadow]` `[factor_trigger: tarot_major_tower AND tarot_major_devil]` `[role: 条件分支]` Devil is God's shadow—Hebrew "Snake" = same numerical value as "Messiah"; person seeking unity must bring out repressed energy (Devil) triggering Tower. → Devil's House = God's House
- `[ns_78deg_344]` `[trigger: tower_necessity]` `[factor_trigger: tarot_major_tower AND principle_necessary_destruction]` `[role: 总结]` Tower = necessary destruction for liberation; no other way to go beyond consciousness barrier, break free from what separates life into opposites. → Why Necessary
- `[ns_78deg_507]` `[trigger: grey_stone_prison]` `[factor_trigger: tarot_major_tower AND symbol_grey_tower]` `[role: 条件分支]` Grey stone tower as prison we built—walls of narrow materialism, gold crown of ego; comfortable captivity we mistake for security until lightning reveals the truth. → Visual Elements

**完整中文诠释**:
**高塔**=**暴力解放**、**粉碎意识**、**神圣毁灭**——爆炸释放压抑能量、打破幻觉。**数字16**：1+6=7（战车）——自我结构被摧毁vs战车自我胜利；塔/屋：上帝之屋或恶魔之屋（两名皆用）。**图像元素**（RWS牌）：天空**闪电**击塔；顶部**王冠飞落**=自我/物质主义金冠；**两人坠落**=从虚假安全被抛；**火滴Yod形**（希伯来字母）=上帝名首字母=**恩典非怒**；**灰石塔**=狭隘物质主义监狱；**黑背景**=混乱、毁灭；**火焰/爆炸**=能量暴力释放。**双重诠释**："1.道德/表面意义"："塔=物质主义宇宙观"：基于财富、名声、身体愉悦的生命；忽视内省与灵性之美；**围己升起的监狱**（灰、岩缚、金冠）。"闪电=毁灭"：来临于纯物质原则基础的生命；**但**：非外力——源自**心理原则**；随无意识紧绷枷锁压力累积；梦受扰、争执、抑郁；若进一步压抑→**无意识爆炸**。"外在灾难"：朋友/家人反目；工作崩塌；暴力环绕；**谜**：厄运成串；**真相**：问题源自长期疏忽/错处情境；在我们变脆弱时刻击中；**巧合**显示生命包含超可见之物。"2.深奥/深层意义"："若恶魔=释放压抑能量"：塔=**被粉碎的幻觉即意识本身**；**圣殿幕帘撕开**（非仅物质主义被毁）。"荣格比喻"：意识=**堵塞**无意识河流自由流动之坝；**节制**=水闸（控制速率）；**塔**=**炸坝**（洪流释放）。"为何必要？"："无他途**以：最终超越意识屏障**；从将生命分为对立面之物解放；从切断我们与内在纯能量之物解放。"圣殿幕帘**=有意识人格：**保护我们**免于生命本身；神秘家/萨满证：**永恒环绕我们**，炫目、压倒；未备之心无法包容此力量；意识=**保护屏障**。**但**：达与生命合一，**幕帘必须撕裂**；需要**暴力突破**；塔=解放必要之毁灭。**Yod滴**（希伯来字母）：火滴形落下；**上帝名（YHVH）首字母**；非怒而是**恩典**；宇宙/人类心智**不允许**我们永远被囚；若无法和平释放→**生命之力安排爆炸**。**非享受**：不享受震松我们的痛苦经验；无法从此手段见有益目的；**过程不总带来自由**；常是一系列灾难**致残**曾强壮人格；**要点**：无其他出口，无意识将爆发；可用经验找到更好平衡。**恶魔屋=上帝屋**："更深意义"：希伯来："蛇"=与"弥赛亚"数值相同；**恶魔乃上帝之影**；寻求合一之人**必须引出压抑能量**（恶魔）；但危及节制平静/平衡；**暴力路程**=必须撒裂。"""
    normalized_text_zh: str = """"""
    subject: str = "Card 16: The Tower"
    factor_refs: list = ['tarot_major_tower', 'tarot_number_16', 'metaphor_dam', 'symbol_yod_grace', 'state_veil_torn', 'state_breakthrough']
    
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
        l1_anchor="pt_v1.0.0_card_16__the_tower_001_L1",
    )
    version: str = "1.0.0"
