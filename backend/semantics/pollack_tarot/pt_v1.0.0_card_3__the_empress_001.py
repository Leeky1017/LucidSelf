"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994395
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
    semantic_id="pt_v1.0.0_card_3__the_empress_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card3TheEmpress(SemanticEntry):
    """
    ### Nature, Motherhood, and Passionate Life

#### Key Term Analysis

| Term | Definition | Significa...
    """
    
    original_text: str = """### Nature, Motherhood, and Passionate Life

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 3 | 1+2 synthesis | Child/creation |
| Great Mother | Underlying life principle | Nature archetype |
| Venus Symbol | Love, beauty, desire | Goddess energy |
| River Current | Life force/passion | Change + continuity |

**Source Text**: The Empress represents the more accessible, more benign aspects of the female archetype. She is motherhood, love, gentleness. At the same time she signifies sexuality, emotion and the female as mistress. Both motherhood and sex derive from feelings that are non-intellectual and basic to life. Passions rather than ideas. The High Priestess represented the mental side of the female archetype; her deep intuitive understanding. The Empress is pure emotion.

**English Paraphrase**:

**The Empress** = **Nature**, **Emotion**, **Sensuality** — the physical, passionate, life-giving principle.

**Core Symbolism**:
- **Number 3**: Synthesis of 1 + 2 (masculine + feminine) = **the child**, new creation
- **Triangle**: Harmony, stability, manifestation into physical reality

**Visual Elements** (Rider-Waite-Smith):
- **Voluptuous pregnant figure** = fertility, abundance, life-giving power
- **Shield with Venus symbol** (♀) = love, beauty, desire (Great Goddess)
- **Crown of 12 stars** = zodiac, universe as her domain
- **Necklace of 9 pearls** = nine planets (pre-Pluto discovery)
- **Field of grain** at feet = agriculture, harvest, material abundance (Corn Goddess/Demeter)
- **River flowing** from trees = **life force current**, passion, change within continuity
- **Six-pointed stars** on crown = two triangles (fire △ + water ▽) combined
- **Lush green forest** = untamed nature, growth, fertility
- **Red robe** = passion, blood, life
- **Cushioned throne** in nature = comfort, nurturing, grounded in earth

**Psychological Meaning**:

**Nature as Underlying Reality**:
- Empress = **natural world** created by union of Magician (energy) + High Priestess (potential)
- **Life's creation**: Lightning (Magician's fire) strikes primordial sea (High Priestess's water) = life emerges
- **Great Mother** = not the forms of nature but the **underlying principle of life**
- Wears **universe as jewelry** = nature encompasses all

**Emotion vs. Intellect**:
- High Priestess = **mental/intuitive** side of feminine
- Empress = **emotional/sensual** side of feminine
- **Pure emotion**: feelings, passions, non-intellectual experience
- **Direct experience** of world without labels or controls

**Motherhood and Sexuality**:
- **Mother**: Love, nurturing, protection, bonding
- **Mistress**: Sexuality, desire, pleasure, passion
- Both derive from **basic life feelings**, not rational thought
- **Unity of reproduction**: Child as product of union (number 3 = child of 1 & 2)

**The River Symbolism**:

Flowing water represents:
1. **Life force current** running beneath all separate forms
2. **Passion unrestrained** — when we surrender to feeling, we sense this current
3. **Change within continuity**: Water never same, yet always the same river (like human identity — cells die/renew, yet we remain ourselves)
4. **Death's inevitability**: River carries us forward through experience until we return to the sea of existence

**The Path to Enlightenment Through Sensuality**:

Pollack's radical claim: **Sensuality is the first step to enlightenment**

- "Until we learn to experience the outer world completely we cannot hope to transcend it"
- **Passion allows us to sense** (from deep inside, not intellectually) the **spirit that fills all existence**
- Many see religion as **escape from "impure" natural world** — this is an **illusion**
- Body and natural world are **realities that must be integrated, not denied**

**Buddhist example**: Prince Siddhartha (Gautama Buddha)
- Gods manipulated father to provide **every sensual satisfaction**
- Only **after completely experiencing sensuality** could he leave it behind
- Then joined ascetics (other extreme) — but enlightenment came only through **Middle Way**
- Buddha = World dancer holding both Magician and High Priestess lightly

**The Child Archetype**:
- Number 3 = **child born from 1 & 2**
- Child = **creature of nature**, unburdened by ego/personality
- **Directly experiences universe** without controls or labels
- **Tarot's goal**: Return us to this natural state of direct experience

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's Empress: Nature=underlying reality. Great Mother. Passion=life force river. Integrate body/nature, not transcend. Child archetype.
- **中文**: Pollack的皇后:自然=底层现实。大母神。激情=生命力河流。整合身体/自然,非超越。孩子原型。

**Narrative Snippets**:
- `[ns_78deg_035]` `[trigger: empress_emotion]` `[factor_trigger: tarot_empress AND tarot_emotion AND archetype_child]` `[role: 主干]` The Empress represents the more accessible, more benign aspects of the female archetype—motherhood, love, gentleness, sexuality, emotion. → Source Text
- `[ns_78deg_036]` `[trigger: high_priestess_vs_empress]` `[factor_trigger: tarot_high_priestess AND tarot_empress AND polarity_empress_emperor]` `[role: 主干]` The High Priestess represented the mental side of the female archetype; the Empress is pure emotion. → Source Text
- `[ns_78deg_037]` `[trigger: river_life_force]` `[factor_trigger: tarot_river AND tarot_life_force]` `[role: 条件分支]` The river represents the life force current running beneath all separate forms—when we surrender to feeling, we sense this current. → English Paraphrase
- `[ns_78deg_038]` `[trigger: sensuality_enlightenment]` `[factor_trigger: tarot_sensuality AND tarot_enlightenment]` `[role: 总结]` Sensuality is the first step to enlightenment—until we learn to experience the outer world completely we cannot hope to transcend it. → Source Text
- `[ns_78deg_088]` `[trigger: empress_major]` `[factor_trigger: tarot_major_empress AND tarot_number_3 AND state_pure_emotion AND symbol_grain_field]` `[role: 主干]` The Empress represents nature, emotion, sensuality—the physical, passionate, life-giving principle; the more accessible aspects of the female archetype. → Source Text
- `[ns_78deg_089]` `[trigger: venus_ruler]` `[factor_trigger: planet_venus]` `[role: 主干依赖]` Venus rules the Empress—shield bears Venus symbol (♀) representing love, beauty, desire; the Great Goddess in her earthly, accessible aspect. → English Paraphrase
- `[ns_78deg_090]` `[trigger: great_mother]` `[factor_trigger: archetype_great_mother]` `[role: 主干]` The Empress as Great Mother—not the forms of nature but the underlying principle of life itself; she wears the universe as jewelry. → English Paraphrase
- `[ns_78deg_091]` `[trigger: life_river_symbol]` `[factor_trigger: symbol_life_river]` `[role: 条件分支]` The flowing river represents life force current running beneath all separate forms—passion unrestrained; change within continuity. → English Paraphrase
- `[ns_78deg_092]` `[trigger: sensual_path]` `[factor_trigger: principle_sensual_path]` `[role: 总结]` Sensuality as the first step to enlightenment—body and nature as realities to be integrated, not denied; we must fully experience before we can transcend. → Source Text

**完整中文诠释**:
**皇后**=**自然**、**情感**、**感官性**——物质的、热情的、赋予生命的原则。**数字3**：1+2（阳性+阴性）的综合=**孩子**，新的创造；三角形：和谐、稳定、显化为物质现实。**图像元素**（RWS牌）：**丰满怀孕人物**=生育力、丰盛、赋予生命力量；**盾牌上金星符号**（♀）=爱、美、欲望（大女神）；**12星冠**=黄道，宇宙为其领域；**9珠项链**=九行星（冥王星发现前）；脚边**谷物田**=农业、收获、物质丰盛（谷物女神/德墨忒尔）；从树林流出的**河流**=**生命力洪流**，激情，连续性中的变化；冠上**六芒星**=两个三角形（火△+水▽）结合；**茂密绿色森林**=未驯服自然、生长、生育力；**红袍**=激情、血液、生命；大自然中**有垫座椅**=舒适、滋养、根植于大地。**心理意义**："自然作为底层现实"：皇后=魔术师（能量）与女祭司（潜能）结合创造的**自然世界**；**生命创造**：闪电（魔术师之火）击中原初之海（女祭司之水）=生命涌现；**大母神**=非自然的形式而是生命的**底层原则**；穿戴**宇宙为珠宝**=自然包容一切。**情感vs智力**：女祭司=女性的**心智/直觉**侧；皇后=女性的**情感/感官**侧；**纯粹情感**：感受、激情、非理智经验；**直接经验**世界，不加标签或控制。**母性与性**：**母亲**：爱、滋养、保护、结合；**情妇**：性、欲望、愉悦、激情；两者都源自**基本生命感受**，非理性思维；**繁殖的统一**：孩子为结合的产物（数字3=1和2之子）。**河流象征**：流水代表：1.**生命力洪流**运行于所有分离形式之下；2.**无拘激情**——当我们臣服于感受时，感知此洪流；3.**连续性中的变化**：水从不相同，但总是同一河流（如人类身份——细胞死亡/更新，我们仍是自己）；4.**死亡的不可避免**：河流载我们前行穿越经验，直至回归存在之海。**通过感官性的开悟之路**：Pollack的激进主张：**感官性是开悟的第一步**——"直到我们学会完全体验外在世界，才能期望超越它"；**激情让我们感知**（从深处，非理智地）**充满一切存在的灵**；许多人视宗教为**逃离"不洁"自然世界**——这是**幻觉**；身体与自然世界是**必须整合而非否认的现实**。**佛教例子**：悉达多王子（释迦牟尼）：神灵操纵父亲提供**一切感官满足**；只有在**完全体验感官性之后**才能离开它；然后加入苦行者（另一极端）——但开悟只通过**中道**；佛陀=世界牌舞者，轻持魔术师与女祭司。**孩子原型**：数字3=**从1和2诞生的孩子**；孩子=**自然之造物**，不为自我/人格所累；**直接体验宇宙**不加控制或标签；**塔罗目标**：返回我们至这种直接经验的自然状态。


---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 3: The Empress"
    factor_refs: list = ['tarot_major_empress', 'tarot_number_3', 'archetype_great_mother', 'symbol_life_river', 'planet_venus', 'principle_sensual_path', 'state_pure_emotion', 'archetype_child']
    
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
        l1_anchor="pt_v1.0.0_card_3__the_empress_001_L1",
    )
    version: str = "1.0.0"
