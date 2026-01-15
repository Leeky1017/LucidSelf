"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280941
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
    semantic_id="pit_v1.0.0_mercury_opposition_moon__流年水星冲_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryOppositionMoon流年水星冲(SemanticEntry):
    """
    > Mind and emotions at cross purposes. Others' feelings may conflict with your thinking. Good for se...
    """
    
    original_text: str = """> Mind and emotions at cross purposes. Others' feelings may conflict with your thinking. Good for seeing how you communicate emotionally. May reveal relationship dynamics.

**Narrative Snippets**:
- `[ns_pit_me024]` `[trigger: transit_mercury_opposition_natal_moon]` `[factor_trigger: astro_transit_mercury OPPOSITION natal_moon]` `[role: 主干]` Mind and emotions cross purposes. See how you communicate emotionally. → PIT Ch6 Mercury☍Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Opposition Moon (流年水星冲本命月亮)"
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
        l1_anchor="pit_v1.0.0_mercury_opposition_moon__流年水星冲_001_L1",
    )
    version: str = "1.0.0"
