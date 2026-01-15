"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044684
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
    semantic_id="bot_v1.0.0_atu_xvii__the_star__星星_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXviiTheStar星星(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Heh (ה) | Hebrew letter "Window" | Divine light entry |
| Nuit | Star goddess | Infinite space |
| Aquarius | Water-bearer sign | Universal vision |
| Seven-pointed Star | Venus/sacred feminine | Spiritual love |

**Source Text**:
> "This is the card of meditation and of the spiritual life... The naked figure of Nuit, the star goddess, pours water upon the earth from two cups... One stream flows upon herself, representing eternal renewal; the other upon the earth, representing the crystallization of spirit into form... The seven-pointed star of Venus dominates the sky... This is the pure spiritual light, cool and detached." (Book of Thoth, The Star)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Heh (ה, value 5) - "Window"  
- **Path**: Connects Chokmah (Wisdom) to Tiphareth (Beauty) - The 15th Path (second Heh)
- **Zodiac**: Aquarius ♒ (The Water-Bearer)
- **Element**: Air (intellectual, detached, universal)

**English Paraphrase**:
The Star represents **hope, inspiration, and connection to cosmic order**. The goddess Nuit (infinite space) pours life-giving water from two vessels: one stream flows back upon herself (eternal self-renewal), the other onto the earth (spirit crystallizing into matter). The **Window** (Heh) symbolizes the opening through which divine light enters consciousness—not the blinding sun but the cool, guiding starlight that illuminates without burning. The **seven-pointed star** (Venus/Babalon, the sacred feminine) dominates the sky, representing spiritual love and beauty. Aquarius brings detached vision and universal perspective, seeing patterns in the cosmic whole. This is trust in the process, faith that the universe is fundamentally benevolent and ordered.

**完整中文诠释**:
星星代表着**希望、灵感与宇宙秩序的连接**。女神Nuit（无限空间）从两个容器中倾倒赋予生命的水：一股水流回流到她自己身上（永恒的自我更新），另一股流到地上（灵性结晶为物质）。**窗户**（Heh）象征着神圣之光进入意识的开口——不是炽烈的太阳而是清凉的、引导性的星光，照亮而不灼烧。**七角星**（金星/巴巴隆，神圣女性）主导着天空，代表灵性之爱与美。水瓶座带来超然的视野与普世的视角，看见宇宙整体中的模式。这是对过程的信任，相信宇宙根本上是仁慈且有序的。

**Core Points**:
- **Dual Pouring**: Self-renewal and earthly manifestation in balance
- **Cool Starlight**: Guidance without force, inspiration without heat
- **Window to Divine**: Heh as opening for cosmic consciousness
- **Aquarian Vision**: Universal perspective, detached clarity

**Detailed Explanation**:
The path from Chokmah (creative wisdom) to Tiphareth (harmonized self) shows how cosmic inspiration descends to human consciousness. The Star follows the Tower—after destruction comes renewal and hope. Nuit's dual pouring represents the mystical truth that spirit must both renew itself eternally and manifest in matter. The seven-pointed star (Venus) contrasts with the six-pointed star (solar) of other cards, emphasizing the receptive, feminine aspect of spiritual illumination.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Star depicts Nuit (Thelemic goddess) pouring dual streams. Heh (Window) allows divine light entry. Seven-pointed Venus star emphasizes sacred feminine. Aquarius brings detached universal vision. Card follows Tower—hope after destruction.
- **中文**: Crowley的星星描绘Nuit（泰勒玛女神）倒出双流。Heh（窗户）允许神圣之光进入。七角金星强调神圣女性。水瓶座带来超然普世视野。此牌紧随塔——毁灭后的希望。

**Narrative Snippets**:
- `[ns_thoth_075]` `[trigger: star_hope_renewal]` `[factor_trigger: tarot_star AND tarot_hope]` `[role: 主干]` The Star represents hope, inspiration, and connection to cosmic order—trust that the universe is fundamentally benevolent and ordered. → English Paraphrase
- `[ns_thoth_076]` `[trigger: nuit_dual_pouring]` `[factor_trigger: tarot_nuit AND tarot_renewal]` `[role: 主干依赖]` Nuit pours from two cups: one stream flows upon herself (eternal renewal), the other upon the earth (spirit crystallizing into form). → English Paraphrase
- `[ns_thoth_077]` `[trigger: heh_window]` `[factor_trigger: tarot_heh AND tarot_illumination]` `[role: 主干依赖]` Heh (Window) symbolizes the opening through which divine light enters consciousness—cool starlight that guides without burning. → English Paraphrase
- `[ns_thoth_078]` `[trigger: seven_pointed_star]` `[factor_trigger: tarot_venus AND tarot_spiritual_love]` `[role: 总结]` The seven-pointed star of Venus dominates the sky, representing spiritual love and the sacred feminine aspect of illumination. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XVII: The Star (星星)"
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
        l1_anchor="bot_v1.0.0_atu_xvii__the_star__星星_001_L1",
    )
    version: str = "1.0.0"
