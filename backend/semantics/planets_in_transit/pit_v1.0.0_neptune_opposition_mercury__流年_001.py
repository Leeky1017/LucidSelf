"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272868
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
    semantic_id="pit_v1.0.0_neptune_opposition_mercury__流年_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneOppositionMercury流年(SemanticEntry):
    """
    > Others may confuse or deceive in communication. Misunderstandings from others. Good for seeing com...
    """
    
    original_text: str = """> Others may confuse or deceive in communication. Misunderstandings from others. Good for seeing communication illusions.

**Narrative Snippets**:
- `[ns_pit_ne027]` `[trigger: transit_neptune_opposition_natal_mercury]` `[factor_trigger: astro_transit_neptune OPPOSITION natal_mercury]` `[role: 主干]` Others confuse in communication. Misunderstandings. See illusions. → PIT Ch12 Neptune☍Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Opposition Mercury (流年海王星冲本命水星)"
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
        l1_anchor="pit_v1.0.0_neptune_opposition_mercury__流年_001_L1",
    )
    version: str = "1.0.0"
