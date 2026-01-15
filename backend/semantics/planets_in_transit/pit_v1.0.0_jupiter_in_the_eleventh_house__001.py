"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309891
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
    semantic_id="pit_v1.0.0_jupiter_in_the_eleventh_house__001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheEleventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 10460-10478):
> Hopes, ideals and wishes for future play important role. Frie...
    """
    
    original_text: str = """**Source Text** (Lines 10460-10478):
> Hopes, ideals and wishes for future play important role. Friends may be of considerable benefit. More involved in group activities—understand importance of group goals. Not time to go it alone. Need to be with many people. Friends more supportive, may make many new friends. Help them also—not one-way street. More than usually idealistic—want to improve world. Want to translate into broad social reform or changes affecting you and friends. Not a time to be selfish—if improvements don't affect others, won't be meaningful or long-lasting.

**English Paraphrase**: Hopes and ideals important. Friends beneficial. Group activities favored. Make new friends. Idealistic—want to improve world. Changes should affect others to be meaningful.

**Complete Chinese Interpretation**: 希望和理想重要。朋友有益。群体活动受青睐。结交新朋友。理想主义——想要改善世界。改变应该影响他人才有意义。

**Narrative Snippets**:
- `[ns_pit_ju011]` `[trigger: jupiter_transit_house_11]` `[factor_trigger: astro_transit_jupiter AND astro_house_11]` `[role: 主干]` Friends beneficial. Group activities. Idealistic—improve world through collective action. → PIT Ch9 Jupiter-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Eleventh House (木星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_eleventh_house__001_L1",
    )
    version: str = "1.0.0"
