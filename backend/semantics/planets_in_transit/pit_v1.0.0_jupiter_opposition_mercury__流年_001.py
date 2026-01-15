"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310110
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
    semantic_id="pit_v1.0.0_jupiter_opposition_mercury__流年_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterOppositionMercury流年(SemanticEntry):
    """
    > Others expand your thinking. May challenge your beliefs. Good for learning from different perspect...
    """
    
    original_text: str = """> Others expand your thinking. May challenge your beliefs. Good for learning from different perspectives. Watch overconfidence in ideas.

**Narrative Snippets**:
- `[ns_pit_ju027]` `[trigger: transit_jupiter_opposition_natal_mercury]` `[factor_trigger: astro_transit_jupiter OPPOSITION natal_mercury]` `[role: 主干]` Others expand thinking. Learn from different perspectives. → PIT Ch9 Jupiter☍Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Opposition Mercury (流年木星冲本命水星)"
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
        l1_anchor="pit_v1.0.0_jupiter_opposition_mercury__流年_001_L1",
    )
    version: str = "1.0.0"
