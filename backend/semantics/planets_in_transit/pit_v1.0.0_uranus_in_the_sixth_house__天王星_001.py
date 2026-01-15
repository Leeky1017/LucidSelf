"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206678
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
    semantic_id="pit_v1.0.0_uranus_in_the_sixth_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheSixthHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14596-14628):
> New attitude toward work and new relationship with it. Seek f...
    """
    
    original_text: str = """**Source Text** (Lines 14596-14628):
> New attitude toward work and new relationship with it. Seek freedom from excessive demands. Common: change of job (not profession), changes giving more freedom, revolt against oppressive duties. Not happy with what you feel you have to do. Proper response: make changes in areas too binding. Break free and find new kinds of work and service allowing greater freedom. Wildly rebellious response probably too destructive. Look for new responsibilities with different challenges. May encounter new techniques—computers, electronics. Deal with challenges consciously. Don't repress tension—if repressed, expressed physically as health problem. Sixth house is body's physical efficiency. If don't make changes consciously, body will force them. Heart trouble, accidents, nerve problems, need for operation are typical.

**English Paraphrase**: New work attitude. Seek freedom. May change job. Break from oppressive duties. Look for new challenges. May encounter technology. Don't repress—body will express as health problem if changes not made consciously.

**Complete Chinese Interpretation**: 新的工作态度。寻求自由。可能换工作。摆脱压迫性职责。寻找新挑战。可能遇到技术。不要压抑——如果不有意识地做出改变，身体会表达为健康问题。

**Narrative Snippets**:
- `[ns_pit_ur006]` `[trigger: uranus_transit_house_6]` `[factor_trigger: astro_transit_uranus AND astro_house_6]` `[role: 主干]` New work attitude. Seek freedom. Don't repress—health problems if changes not made. → PIT Ch11 Uranus-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Sixth House (天王星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_sixth_house__天王星_001_L1",
    )
    version: str = "1.0.0"
