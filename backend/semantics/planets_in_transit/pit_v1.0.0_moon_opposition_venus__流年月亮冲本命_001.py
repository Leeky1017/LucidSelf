"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301304
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
    semantic_id="pit_v1.0.0_moon_opposition_venus__流年月亮冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionVenus流年月亮冲本命(SemanticEntry):
    """
    > Relationships in focus—may see clearly what you need vs what you have. Emotional needs may conflic...
    """
    
    original_text: str = """> Relationships in focus—may see clearly what you need vs what you have. Emotional needs may conflict with partner's needs. Good for understanding relationship dynamics. May feel unfulfilled.

**Narrative Snippets**:
- `[ns_pit_m045]` `[trigger: transit_moon_opposition_natal_venus]` `[factor_trigger: astro_transit_moon OPPOSITION natal_venus]` `[role: 主干]` Relationships in focus—emotional needs may conflict with partner's. Understanding dynamics. → PIT Ch5 Moon☍Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Venus (流年月亮冲本命金星)"
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
        l1_anchor="pit_v1.0.0_moon_opposition_venus__流年月亮冲本命_001_L1",
    )
    version: str = "1.0.0"
