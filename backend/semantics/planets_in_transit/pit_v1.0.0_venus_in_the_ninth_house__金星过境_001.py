"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258815
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
    semantic_id="pit_v1.0.0_venus_in_the_ninth_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheNinthHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6958-6980):
> Through Venus encounter—love or beauty—have consciousness-expan...
    """
    
    original_text: str = """**Source Text** (Lines 6958-6980):
> Through Venus encounter—love or beauty—have consciousness-expanding experience. Good time for challenging art exhibit, different music concert. Can signify long, enjoyable pleasure trip. Benefit from trip to new place. Experience broadened through loved one. Attracted to new persons who are strange and different—foreigners, travelers, better educated. Usually easy and rewarding transit.

**English Paraphrase**: Consciousness-expanding through love/beauty. Good for new art, music. Favorable for travel to new places. Attracted to different, foreign people. Easy and rewarding.

**Complete Chinese Interpretation**: 通过爱/美扩展意识。适合新的艺术、音乐。有利于去新地方旅行。被不同的、外国人吸引。轻松而有回报。

**Narrative Snippets**:
- `[ns_pit_ve009]` `[trigger: venus_transit_house_9]` `[factor_trigger: astro_transit_venus AND astro_house_9]` `[role: 主干]` Consciousness-expanding through love/beauty. Good for travel. Attracted to different people. → PIT Ch7 Venus-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Ninth House (金星过境第九宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_ninth_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
