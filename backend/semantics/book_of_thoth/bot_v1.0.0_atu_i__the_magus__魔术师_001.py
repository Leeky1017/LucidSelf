"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044548
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
    semantic_id="bot_v1.0.0_atu_i__the_magus__魔术师_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuITheMagus魔术师(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Beth (ב) | Hebrew letter "House" | Container for spirit |
| Mercury/Hermes | Planet of communication | Messenger archetype |
| Logos | Creative Word | Manifestation through speech |
| Cynocephalus Ape | Thoth's companion | Mimicry vs understanding |

**Source Text**:
> "It is the figure of the Magus of the Taro; in his right arm the torch of the flames blazing upwards; in his left, the cup of poison, a cataract into Hell. And upon his head the evil talisman, blasphemy and blasphemy and blasphemy, in the form of a circle... This is the mill in which the Universal Substance, which is ether, was ground down into matter... He is the first of the Aeons." (Book of Thoth, The Magus - The Lord of Illusion)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Beth (ב, value 2) - "House"
- **Path**: Connects Kether (Crown) to Binah (Understanding) - The 12th Path
- **Planet**: Mercury ☿
- **Element**: Air (intellectual realm)

**English Paraphrase**:
The Magus is the archetypal **Messenger** and **Juggler** of cosmic forces, embodying Mercury/Hermes who mediates between the divine source (Kether) and the formative realm (Binah). He is conscious will manifesting through trained skill and technique. The card depicts him dynamically surrounded by the four elemental weapons (Wand, Cup, Sword, Disk) which float freely, signifying effortless mastery rather than forceful grasping. The **Caduceus** with its twin serpents represents the reconciliation of opposites—active and passive, life and death, healing and poison. Below him crouches the **Cynocephalus Ape** (companion of Thoth), symbolizing mimicry and the distortion of truth through language. The Magus is titled "The Lord of Illusion" because he creates the manifested world through the Word (Logos), yet this creation is itself an illusion compared to the absolute silence of the Fool.

**完整中文诠释**:
魔术师（The Magus）是宇宙力量的原型**信使**与**戏法师**，体现了水星/赫尔墨斯（Mercury/Hermes）在神圣源头（Kether，至高王冠）与形成领域（Binah，理解之母）之间的中介角色。他代表着通过训练有素的技巧与技术而显化的**意识意志**。卡牌将他描绘为一个动态的人物，被四件元素武器（权杖、圣杯、宝剑、圆盘）环绕——这些武器自由漂浮，象征着轻松自如的掌控而非强力的抓握。**商神杖**（Caduceus）及其双蛇代表了对立面的和解——主动与被动、生与死、治疗与毒药。在他下方蹲伏着**狗头猿**（Cynocephalus Ape，图特神的伴侣），象征着模仿以及通过语言对真理的扭曲。魔术师被称为"幻象之主"（The Lord of Illusion），因为他通过"道"（Logos，创世之言）创造了显化的世界，然而与愚者的绝对静默相比，这个被创造的世界本身就是一种幻象。

**Core Points**:
- **Conscious Manifestation**: Focused will transforming potential into form
- **Communication**: The Word (Logos) as the creative force structuring reality
- **Fluid Mastery**: Effortless command over the four elements through skill
- **Sacred Illusion**: Recognition that manifested reality is a magical construct

**Detailed Explanation**:
Beth (House) represents the container or vessel that spirit inhabits. The Magus balances the "Torch of Flames" (active Yang principle, will) with the "Cup of Poison" (passive Yin principle, love/death), demonstrating the union of opposites required for creation. His gesture embodies "As above, so below" - the Hermetic axiom of correspondence. The floating tools indicate that mastery comes not from forceful control but from alignment with natural law. The Ape beneath serves as a warning: words can either transmit truth or distort it through mimicry without understanding.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Magus is titled "Lord of Illusion" emphasizing the constructed nature of manifested reality. The floating elemental weapons (vs RWS's table-bound tools) show effortless mastery. The Ape warns against mimicry without understanding. Beth (House) indicates spirit dwelling in form.
- **中文**: Crowley的魔术师被称为"幻象之主"强调显化现实的构建性质。漂浮的元素武器（对比RWS桌上固定的工具）显示轻松掌控。狗头猴警告不要没有理解的模仿。Beth（房屋）表示灵住在形式中。

**Narrative Snippets**:
- `[ns_thoth_031]` `[trigger: magus_lord_illusion]` `[factor_trigger: tarot_magus AND tarot_illusion]` `[role: 主干]` The Magus is titled 'The Lord of Illusion' because he creates the manifested world through the Word (Logos), yet this creation is itself an illusion. → English Paraphrase
- `[ns_thoth_032]` `[trigger: floating_tools]` `[factor_trigger: tarot_tools AND tarot_mastery]` `[role: 主干依赖]` The four elemental weapons float freely—signifying effortless mastery rather than forceful grasping. → English Paraphrase
- `[ns_thoth_033]` `[trigger: caduceus]` `[factor_trigger: tarot_caduceus AND tarot_reconciliation]` `[role: 主干依赖]` The Caduceus with twin serpents represents the reconciliation of opposites—active and passive, life and death, healing and poison. → English Paraphrase
- `[ns_thoth_034]` `[trigger: cynocephalus_ape]` `[factor_trigger: tarot_ape AND tarot_mimicry]` `[role: 例外处理]` The Ape beneath serves as a warning: words can either transmit truth or distort it through mimicry without understanding. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU I: The Magus (魔术师)"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_atu_i__the_magus__魔术师_001_L1",
    )
    version: str = "1.0.0"
