"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288339
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
    semantic_id="pit_v1.0.0_mars_square_mars__流年火星刑本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsSquareMars流年火星刑本命火星(SemanticEntry):
    """
    > Energy blocked or tested. Frustration and conflict. Actions challenged. Need constructive outlets....
    """
    
    original_text: str = """> Energy blocked or tested. Frustration and conflict. Actions challenged. Need constructive outlets.

**Narrative Snippets**:
- `[ns_pit_ma035]` `[trigger: transit_mars_square_natal_mars]` `[factor_trigger: astro_transit_mars SQUARE natal_mars]` `[role: 主干]` Energy blocked or tested. Frustration. Need constructive outlets. → PIT Ch8 Mars□Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Square Mars (流年火星刑本命火星)"
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
        l1_anchor="pit_v1.0.0_mars_square_mars__流年火星刑本命火星_001_L1",
    )
    version: str = "1.0.0"
