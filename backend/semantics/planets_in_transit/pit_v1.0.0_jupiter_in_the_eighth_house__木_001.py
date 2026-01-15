"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309810
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
    semantic_id="pit_v1.0.0_jupiter_in_the_eighth_house__木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheEighthHouse木(SemanticEntry):
    """
    **Source Text** (Lines 10382-10401):
> Traditionally indicates inheritance, but based on correct pri...
    """
    
    original_text: str = """**Source Text** (Lines 10382-10401):
> Traditionally indicates inheritance, but based on correct principle: benefit from other people's resources. Good time to enter partnership pooling resources. Good time to request loan. Others more willing to help you out. Powerful but fortunate changes—any sweeping change for the best. Greater understanding of psychological patterns. If recent psychological stress, helps healing process. Can indicate religious/spiritual regeneration, "conversion experience." Benefit from studying occult and mystical literature.

**English Paraphrase**: May benefit from others' resources. Good for partnerships and loans. Fortunate changes. Understanding of psychological patterns. Healing. Possible spiritual regeneration. Good for occult/mystical study.

**Complete Chinese Interpretation**: 可能从他人资源中受益。适合合作和贷款。幸运的变化。理解心理模式。疗愈。可能的精神重生。适合神秘学研究。

**Narrative Snippets**:
- `[ns_pit_ju008]` `[trigger: jupiter_transit_house_8]` `[factor_trigger: astro_transit_jupiter AND astro_house_8]` `[role: 主干]` Benefit from others' resources. Good for loans. Fortunate changes. Psychological healing. → PIT Ch9 Jupiter-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Eighth House (木星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_eighth_house__木_001_L1",
    )
    version: str = "1.0.0"
