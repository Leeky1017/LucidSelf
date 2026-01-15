"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309762
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
    semantic_id="pit_v1.0.0_jupiter_in_the_fourth_house__木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheFourthHouse木(SemanticEntry):
    """
    **Source Text** (Lines 10259-10295):
> Seek inner peace and security. Improve all areas of innermost...
    """
    
    original_text: str = """**Source Text** (Lines 10259-10295):
> Seek inner peace and security. Improve all areas of innermost life—home, personal life, family, past, inner self. May purchase real estate or new home, or improve present home. Good time to invest in real estate. Supports domestic life, problems cleared up. Feel generous to family, they respond same. Relationship with parents good. Time to concentrate on personal life rather than getting ahead. Put down roots, gain sense of belonging. Increased inner confidence. Handle truths about yourself you're normally reluctant to face.

**English Paraphrase**: Seek inner peace. Improve home, family, inner life. May buy/improve real estate. Domestic life supported. Good with family and parents. Time for personal life, put down roots. Increased inner confidence. Face inner truths.

**Complete Chinese Interpretation**: 寻求内心平静。改善家庭、内在生活。可能购买/改善房产。家庭生活受支持。与家人和父母关系好。个人生活的时间，扎根。增加内心信心。面对内在真相。

**Narrative Snippets**:
- `[ns_pit_ju004]` `[trigger: jupiter_transit_house_4]` `[factor_trigger: astro_transit_jupiter AND astro_house_4]` `[role: 主干]` Seek inner peace. Good for home and family. Put down roots. Inner confidence. → PIT Ch9 Jupiter-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Fourth House (木星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_fourth_house__木_001_L1",
    )
    version: str = "1.0.0"
