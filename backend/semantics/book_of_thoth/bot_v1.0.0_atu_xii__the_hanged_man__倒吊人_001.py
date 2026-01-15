"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044661
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
    semantic_id="bot_v1.0.0_atu_xii__the_hanged_man__倒吊人_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXiiTheHangedMan倒吊人(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Mem (מ) | Hebrew letter "Water" | Dissolution element |
| Dying God | Osiris/Christ/Attis | Death-rebirth cycle |
| Ankh | Egyptian life symbol | Life through death |
| Nigredo | Alchemical blackening | Ego dissolution stage |

**Source Text**:
> "This is the card of the Dying God... The figure is suspended from an Ankh (the symbol of life)... He is immersed in water (Mem = water)... Below him is the abyss with a writhing serpent, representing the transformative power of the descent... This is baptism, the voluntary descent of the spirit into the waters of manifestation to be reborn." (Book of Thoth, The Hanged Man)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Mem (מ, value 40) - "Water"
- **Path**: Connects Geburah (Severity) to Hod (Splendor) - The 23rd Path
- **Element**: Water (dissolution, baptism, transformation)
- **Mythological**: The Dying God (Osiris, Christ, Attis)

**English Paraphrase**:
The Hanged Man represents the archetype of **voluntary sacrifice and spiritual surrender**. He is the Dying God suspended from the Ankh (symbol of life), immersed in water (Mem) representing the descent of spirit into matter. This is not passive suffering but **active redemption through sacrifice**—the necessary death that precedes rebirth. The serpent below symbolizes transformation through dissolution. The figure hangs upside-down, representing a **complete reversal of perspective**: what seemed up is down, what seemed important becomes trivial, the ego must die for the higher self to emerge. This is the alchemical stage of dissolution (Nigredo) and the mystical baptism where the initiate voluntarily descends into the waters of manifestation to be transformed and reborn.

**完整中文诠释**:
倒吊人代表着**自愿牺牲与灵性臣服**的原型。他是悬挂于Ankh（生命符号）上的垂死之神，浸没于水中（Mem），象征着灵性降入物质。这不是被动的受苦，而是**通过牺牲主动救赎**——重生前必需的死亡。下方的蛇象征着通过溶解实现的转化。人物倒悬，代表着**视角的彻底反转**：曾经向上的现在向下，曾经重要的变得琐碎，自我必须死去以让更高的自我浮现。这是炼金术的溶解阶段（黑化期）和神秘洗礼，启蒙者自愿降入显化之水以被转化和重生。

**Core Points**:
- **Voluntary Sacrifice**: Active choice to surrender ego for spiritual transformation
- **Dying God Formula**: Death as necessary stage before resurrection
- **Perspective Reversal**: Complete inversion of worldview through dissolution
- **Water Baptism**: Spirit descending into matter to be reborn

**Detailed Explanation**:
The path from Geburah (Mars, severity) to Hod (Mercury, intellect) shows how forceful transformation leads to new understanding. The Hanged Man's suspension is not punishment but initiation—the voluntary acceptance of dissolution. The Ankh from which he hangs represents that life comes through this death. The water (Mem) is both womb and tomb, the medium of transformation. This card embodies the mystery teachings of the Dying God found in Osiris, Christ, and Dionysus—the divine principle that must descend, be torn apart, and rise again transformed.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Hanged Man embodies the Dying God mystery (Osiris/Christ/Attis). Suspension from Ankh shows life through death. Mem (Water) represents dissolution and baptism. The inverted perspective symbolizes ego death. Harris depicts voluntary surrender, not punishment.
- **中文**: Crowley的倒吊人体现垂死之神奥秘（奥西里斯/基督/阿提斯）。悬挂于Ankh显示通过死亡获得生命。Mem（水）代表溶解和洗礼。倒转视角象征自我死亡。Harris描绘自愿臣服而非惩罚。

**Narrative Snippets**:
- `[ns_thoth_067]` `[trigger: hanged_man_dying_god]` `[factor_trigger: tarot_hanged_man AND tarot_dying_god]` `[role: 主干]` The Hanged Man is the card of the Dying God—Osiris, Christ, Attis—the divine principle that descends, is torn apart, and rises transformed. → English Paraphrase
- `[ns_thoth_068]` `[trigger: voluntary_sacrifice]` `[factor_trigger: tarot_sacrifice AND tarot_redemption]` `[role: 主干依赖]` This is not passive suffering but active redemption through sacrifice—the necessary death that precedes rebirth. → English Paraphrase
- `[ns_thoth_069]` `[trigger: mem_water_baptism]` `[factor_trigger: tarot_mem AND tarot_baptism]` `[role: 主干依赖]` Mem (Water) is the medium of transformation: baptism where the initiate voluntarily descends into the waters of manifestation to be reborn. → English Paraphrase
- `[ns_thoth_070]` `[trigger: perspective_reversal]` `[factor_trigger: tarot_reversal AND tarot_ego_death]` `[role: 总结]` Hanging upside-down represents a complete reversal of perspective: the ego must die for the higher self to emerge. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XII: The Hanged Man (倒吊人)"
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
        l1_anchor="bot_v1.0.0_atu_xii__the_hanged_man__倒吊人_001_L1",
    )
    version: str = "1.0.0"
