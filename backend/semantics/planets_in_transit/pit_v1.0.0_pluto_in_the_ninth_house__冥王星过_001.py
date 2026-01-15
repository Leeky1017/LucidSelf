"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238037
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
    semantic_id="pit_v1.0.0_pluto_in_the_ninth_house__冥王星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheNinthHouse冥王星过(SemanticEntry):
    """
    **Source Text** (Lines 19010-19045):
> Overall view of world will change considerably, often because...
    """
    
    original_text: str = """**Source Text** (Lines 19010-19045):
> Overall view of world will change considerably, often because of crises demonstrating invalidity of former views. At same time, ability to see and understand world in depth and wisdom in handling it will grow. No reason to fear—at worst maturing experience, at best transform you into far better human being. Strive to learn everything—knowledge will be extremely useful during Pluto transit of 10H which follows. Whatever your interests prior, will turn now to more profound subjects—relationship to people and universe, your role in general scheme. May turn to religion if it gives deep intimate experience. Pluto brings knowledge not through mind but through viscera—must be experience. Mystical and occult philosophies may attract. But remember experiences are extremely powerful—avoid becoming fanatically obsessed. Pluto tends to produce obsessions—may cram what you've learned down others' throats. Give others chance to keep own views. Since 9H concerned with larger social order, may become involved in group or movement wanting to transform society—probably not revolutionary, Pluto operates slowly and effectively. If difficult aspects, may cause troubles with law if not careful—if convinced of own righteousness, operate without considering others' ideas. Keep in mind context and appropriateness.

**English Paraphrase**: Worldview changes through crises. Wisdom and depth grow. Knowledge useful for 10H. Turn to profound subjects—religion, occult. Knowledge through visceral experience, not just mind. Avoid obsession. May join transformative movements. Watch for legal issues if self-righteous.

**Complete Chinese Interpretation**: 世界观通过危机改变。智慧和深度增长。知识对第十宫有用。转向深刻主题——宗教、神秘学。通过内在体验而非仅仅头脑获得知识。避免执念。可能加入变革运动。如果自以为是要注意法律问题。

**Narrative Snippets**:
- `[ns_pit_pl009]` `[trigger: pluto_transit_house_9]` `[factor_trigger: astro_transit_pluto AND astro_house_9]` `[role: 主干]` Worldview transforms. Wisdom grows. Seek profound subjects. Avoid obsession. → PIT Ch13 Pluto-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Ninth House (冥王星过境第九宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_pluto_in_the_ninth_house__冥王星过_001_L1",
    )
    version: str = "1.0.0"
