"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206839
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
    semantic_id="pit_v1.0.0_uranus_in_the_ninth_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheNinthHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14700-14736):
> Opportunity to greatly expand awareness and gain insights nev...
    """
    
    original_text: str = """**Source Text** (Lines 14700-14736):
> Opportunity to greatly expand awareness and gain insights never had before—must keep open mind. Otherwise only upset by what Uranus reveals. If flexible, simply points out new ways of seeing world. If identified with particular viewpoint, feel threatened and resist. That is response of social reactionary. Many events notify you that some aspect of thinking is wrong—not invalidated, must adjust. If flexible, attracted to new stimulating ways of thinking—science, technology, new techniques, astrology, radical solutions to social problems. Not especially dangerous for traveling—more likely travel or relocation will revolutionize life. Accidents happen because violent energy inhibited. Because connection with law, avoid legal encounters now.

**English Paraphrase**: Expand awareness—keep open mind. Events show thinking needs adjustment. Flexible: attracted to new thinking—science, technology, astrology. Travel may revolutionize life. Avoid legal encounters.

**Complete Chinese Interpretation**: 扩展意识——保持开放心态。事件显示思维需要调整。灵活：被新思维吸引——科学、技术、占星。旅行可能彻底改变生活。避免法律纠纷。

**Narrative Snippets**:
- `[ns_pit_ur009]` `[trigger: uranus_transit_house_9]` `[factor_trigger: astro_transit_uranus AND astro_house_9]` `[role: 主干]` Expand awareness—open mind. Attracted to new thinking. Travel may revolutionize. Avoid legal issues. → PIT Ch11 Uranus-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Ninth House (天王星过境第九宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_ninth_house__天王星_001_L1",
    )
    version: str = "1.0.0"
