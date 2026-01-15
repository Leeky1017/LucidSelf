"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994309
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
    semantic_id="pt_v1.0.0_chapter_1__the_four_card_patte_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Chapter1TheFourCardPatte(SemanticEntry):
    """
    ### Unity and Duality - The Diamond Pattern

#### Key Term Analysis

| Term | Definition | Significa...
    """
    
    original_text: str = """### Unity and Duality - The Diamond Pattern

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Diamond Pattern | 4 key cards | Structural map |
| Fool (0) | Infinite potential | Journey start |
| Magician/Priestess | 1+2 duality | Core polarity |
| World (21) | Integration | Journey end |

**Source Text**: Through its long history the Major Arcana has attracted a great many interpretations. Today, we tend to look upon the trumps as a psychological process, showing us passing through different stages of existence to reach a state of full development — unity with the world around us, or liberation from weakness, confusion, and fear. To get an understanding of it as a whole we need look at only four cards: the Fool, the Magician, the High Priestess, and the World, arranged in a diamond pattern.

**English Paraphrase**:

The **22 Major Arcana cards** form a **psychological journey** from fragmentation to wholeness. The entire journey can be understood through **four archetypal cards** in a diamond pattern:

```
           0 - The Fool
          /           \
    1 - Magician    2 - High Priestess
          \           /
          21 - The World
```

**Key Observations**:

**Motion vs. Stillness**:
- **Fool (0) and World (21)**: Both show **dancing, joyful figures** in motion
- **Magician (1) and High Priestess (2)**: **Stationary, fixed** positions
- All other trumps (3-20): Staged as "still photographs" — **fixed states of existence**

**Journey Arc**:
- **Fool**: Rushes forward, **richly clothed**, about to leap from high distant country into lower world
- **World**: Naked, suspended in **victory wreath**, paradoxically **outside** material universe

**Numerological Significance**:
- **0 (Fool)**: Not a number, but **absence** of number = **infinite potentiality**. All things remain possible because no form has been taken.
- **1 (Magician)**: First **odd** number = **unity, spirit, masculine**
- **2 (High Priestess)**: First **even** number = **duality, matter, feminine**
- **21 (World)**: **Combines 2 + 1** = synthesis of opposites, **unity achieved through integration**

**Symbolic Postures**:
- **Magician**: Raises **wand** (phallic symbol) to heaven = masculine, active, spiritual aspiration
- **High Priestess**: Sits between **two pillars** (vaginal symbol) = feminine, receptive, duality
- **World**: Female dancer holds **two wands** (hermaphroditic, integrated polarity)

**The Journey's Meaning**:
1. **Start (Fool)**: Innocent, unformed potential, clothed in ego/persona
2. **Separation (1 & 2)**: Consciousness splits into opposites (masculine/feminine, spirit/matter, active/passive)
3. **Integration (World)**: Return to unity, but now **conscious** — naked (ego-less), dancing (liberated), complete

**完整中文诠释**:
22张大阿卡纳构成一条从分裂到完整的**心理旅程**，可通过**四张原型卡牌**的菱形模式理解全貌：愚者（0）位于顶端，魔术师（1）和女祭司（2）分列两侧，世界（21）位于底端。**运动与静止**：愚者和世界都显示**舞动、喜悦的运动人物**；魔术师和女祭司则是**静止、固定的姿态**；其他主牌（3-20）如静态照片，代表固定的存在状态。**旅程弧线**：愚者奔跑向前，**衣着华丽**，即将从高远之地跃入低处世界；世界则**赤裸**，悬浮于**胜利花环**中，悖论性地置于物质宇宙**之外**。**数字意义**：0（愚者）不是数字而是数字的**缺席**=**无限潜能**，一切皆有可能因尚未取形；1（魔术师）是第一个**奇数**=**统一、灵性、阳性**；2（女祭司）是第一个**偶数**=**二元、物质、阴性**；21（世界）**结合2+1**=对立的综合，通过整合达成的统一。**象征姿态**：魔术师举起**权杖**（阳具符号）指天=阳性、主动、灵性渴望；女祭司坐于**两柱之间**（阴道符号）=阴性、接受、二元性；世界的女舞者持有**两根权杖**（雌雄同体，整合的极性）。**旅程含义**：起点（愚者）天真无邪、未成形的潜能、被自我/人格掩盖；分离（1和2）意识分裂为对立面（阳性/阴性、灵/质、主动/被动）；整合（世界）回归统一，但现在是**有意识的**——赤裸（无自我）、舞动（解放）、完整。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's diamond pattern: Fool(0)=potential, Magician(1)+Priestess(2)=duality, World(21)=integration. Psychological journey from fragmentation to wholeness.
- **中文**: Pollack的菱形模式:愚者(0)=潜能，魔术师(1)+女祭司(2)=二元，世界(21)=整合。从分裂到完整的心理旅程。

**Narrative Snippets**:
- `[ns_78deg_017]` `[trigger: diamond_pattern]` `[factor_trigger: tarot_four_cards AND tarot_archetype]` `[role: 主干]` The entire journey can be understood through four archetypal cards in a diamond pattern: Fool(0), Magician(1), Priestess(2), World(21). → English Paraphrase
- `[ns_78deg_018]` `[trigger: zero_infinite]` `[factor_trigger: tarot_fool AND tarot_potentiality]` `[role: 主干]` 0 (Fool) is not a number but absence of number = infinite potentiality; all things remain possible because no form has been taken. → Source Text
- `[ns_78deg_019]` `[trigger: journey_meaning]` `[factor_trigger: tarot_journey AND tarot_integration AND framework_fools_journey]` `[role: 总结]` Start (Fool): innocent potential. Separation (1&2): consciousness splits into opposites. Integration (World): return to unity, now conscious. → English Paraphrase
- `[ns_78deg_420]` `[trigger: motion_stillness]` `[factor_trigger: tarot_diamond AND principle_motion_stillness]` `[role: 条件分支]` Fool and World show dancing, joyful figures in motion; Magician and Priestess are stationary—other trumps fixed as still photographs between the two poles. → Key Observations
- `[ns_78deg_421]` `[trigger: numerology_synthesis]` `[factor_trigger: tarot_world AND number_21]` `[role: 条件分支]` World (21) combines 2+1—synthesis of opposites, unity achieved through integration; female dancer holds two wands showing hermaphroditic completion. → Numerological Significance
- `[ns_78deg_422]` `[trigger: symbolic_postures]` `[factor_trigger: tarot_magician AND tarot_priestess]` `[role: 条件分支]` Magician raises wand to heaven (masculine, active, spiritual aspiration); Priestess sits between two pillars (feminine, receptive, duality)—polarity requiring integration. → Symbolic Postures
- `[ns_78deg_464]` `[trigger: fool_world_dance]` `[factor_trigger: tarot_fool AND tarot_world AND symbol_dance]` `[role: 条件分支]` Both Fool and World show dancing, joyful figures—the journey begins and ends in motion, unlike the fixed states between; the dance is freedom, the poses are learning. → Motion Observation
- `[ns_78deg_465]` `[trigger: clothed_naked]` `[factor_trigger: tarot_fool AND tarot_world AND symbol_clothing]` `[role: 条件分支]` Fool richly clothed (ego/persona intact), World naked (ego-less liberation)—the journey strips away what we thought was self to reveal true essence. → Journey Arc
- `[ns_78deg_491]` `[trigger: odd_even_polarity]` `[factor_trigger: tarot_magician AND tarot_priestess AND principle_polarity]` `[role: 条件分支]` First odd number (1/Magician) = unity, spirit, masculine; first even number (2/Priestess) = duality, matter, feminine—the primal split that the journey must heal. → Numerological Significance

---

### The Pillars of Duality

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Two Pillars | Boaz & Jachin | Duality symbol |
| Threshold | Liminal space | Initiation |
| Balance | Opposites tension | Equilibrium |
| Recurring Motif | Throughout Major | Structural pattern |

**Source Text**: The High Priestess sits between two pillars, a vaginal symbol as well as a symbol of duality. These two pillars appear again and again in the Major Arcana, in such obvious places as the temple in the Hierophant, and in more subtle ways, like the two lovers on card 6, or the two sphinxes harnessed to the Chariot.

**English Paraphrase**:

The **two pillars** are a recurring **archetypal motif** throughout the Major Arcana, representing:

**Primary Symbolism**:
- **Duality**: All opposites (masculine/feminine, light/dark, active/passive, conscious/unconscious)
- **Threshold**: Standing between pillars = liminality, initiation, passage between worlds
- **Balance**: The tension and equilibrium between opposites

**Appearances in Major Arcana**:
1. **High Priestess (II)**: Sits **between** black and white pillars (B and J, Boaz and Jachin from Solomon's Temple)
2. **Hierophant (V)**: **Two pillars** frame the temple entrance (institutional duality)
3. **Lovers (VI)**: **Two figures** (man and woman, Adam and Eve)
4. **Chariot (VII)**: **Two sphinxes** (one black, one white) harnessed to chariot
5. **Justice (XI)**: Implied through **two sides** of scales
6. **Moon (XVIII)**: **Two towers** flanking the path
7. **Others**: Subtle dual imagery throughout (e.g., Devil's two captives)

**Psychological Meaning**:
- **Pre-integration**: Opposites experienced as **conflict** or **separation**
- **Path to wholeness**: Must **acknowledge and balance** both poles
- **World (XXI)**: Pillars transcended — dancer **integrates** duality within single figure

**Qabalistic Connection**:
- Pillars of **Mercy (right)** and **Severity (left)** on Tree of Life
- **Middle Pillar** = path of equilibrium, balance, integration

**完整中文诠释**:
**两根柱子**是贯穿大阿卡纳的反复出现的**原型母题**，象征着：**二元性**（所有对立面：阳性/阴性、光/暗、主动/被动、意识/无意识）；**门槛**（站在柱子之间=过渡状态、启蒙、在世界间的通道）；**平衡**（对立面之间的张力与均衡）。**在大阿卡纳中的出现**：女祭司（II）坐在黑白柱子**之间**（B和J，所罗门圣殿的Boaz和Jachin）；教皇（V）**两根柱子**框定圣殿入口（制度性二元）；恋人（VI）**两个人物**（男人和女人，亚当和夏娃）；战车（VII）**两只斯芬克斯**（一黑一白）系于战车；正义（XI）通过天平的**两侧**暗示；月亮（XVIII）**两座塔**夹住道路；其他牌中也有微妙的双重意象（如恶魔的两个俘虏）。**心理意义**：整合前的阶段，对立面被体验为**冲突**或**分离**；通往完整的路径必须**承认并平衡**两极；世界（XXI）超越了柱子——舞者在单一人物中**整合**了二元性。**卡巴拉联系**：生命之树上**慈悲之柱**（右）和**严厉之柱**（左）；**中柱**=均衡、平衡、整合之路。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's Two Pillars: recurring duality motif. Appears in Priestess, Hierophant, Lovers, Chariot, Justice, Moon. Qabalah: Mercy/Severity pillars. World transcends.
- **中文**: Pollack的两柱:反复出现的二元母题。出现于女祭司、教皇、恋人、战车、正义、月亮。卡巴拉:慈悲/严厉柱。世界超越。

**Narrative Snippets**:
- `[ns_78deg_020]` `[trigger: two_pillars]` `[factor_trigger: tarot_pillars AND tarot_duality]` `[role: 主干]` The two pillars appear again and again in the Major Arcana—a vaginal symbol as well as a symbol of duality. → Source Text
- `[ns_78deg_021]` `[trigger: pillar_appearances]` `[factor_trigger: tarot_pillars AND tarot_major_arcana]` `[role: 条件分支]` Pillars appear in: Priestess (B&J), Hierophant (temple), Lovers (two figures), Chariot (sphinxes), Moon (towers). → English Paraphrase
- `[ns_78deg_022]` `[trigger: world_transcends]` `[factor_trigger: tarot_world AND tarot_transcendence]` `[role: 总结]` World (XXI): pillars transcended—dancer integrates duality within single figure, both wands in one person. → English Paraphrase
- `[ns_78deg_423]` `[trigger: threshold_symbol]` `[factor_trigger: tarot_pillars AND principle_threshold]` `[role: 条件分支]` Standing between pillars = liminality, initiation, passage between worlds; threshold space where transformation becomes possible. → Primary Symbolism
- `[ns_78deg_424]` `[trigger: qabalah_pillars]` `[factor_trigger: tarot_pillars AND kabbalah_tree]` `[role: 条件分支]` Qabalistic connection: Pillars of Mercy (right) and Severity (left) on Tree of Life; Middle Pillar = path of equilibrium and integration. → Qabalistic Connection
- `[ns_78deg_425]` `[trigger: pre_integration]` `[factor_trigger: tarot_pillars AND state_separation]` `[role: 条件分支]` Before integration, opposites experienced as conflict or separation; path to wholeness requires acknowledging and balancing both poles. → Psychological Meaning
- `[ns_78deg_466]` `[trigger: boaz_jachin]` `[factor_trigger: tarot_pillars AND symbol_solomons_temple]` `[role: 条件分支]` Black and white pillars B and J (Boaz and Jachin) from Solomon's Temple—duality at the threshold of sacred space; one must pass between opposites to enter wisdom. → Symbolic Reference
- `[ns_78deg_467]` `[trigger: recurring_motif]` `[factor_trigger: tarot_pillars AND principle_structural_pattern]` `[role: 条件分支]` Pillars recur throughout Major Arcana as structural pattern—Tarot uses visual repetition to reinforce the universal law of duality requiring integration. → Structural Observation
- `[ns_78deg_492]` `[trigger: balance_tension]` `[factor_trigger: tarot_pillars AND principle_equilibrium]` `[role: 条件分支]` Balance requires tension between opposites—not eliminating one pole but holding both in creative equilibrium; the space between pillars is where transformation occurs. → Psychological Meaning

---"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter 1: The Four Card Pattern"
    factor_refs: list = []
    
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
        l1_anchor="pt_v1.0.0_chapter_1__the_four_card_patte_001_L1",
    )
    version: str = "1.0.0"
