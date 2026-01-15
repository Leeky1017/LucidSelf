"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272765
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
    semantic_id="pit_v1.0.0_neptune_opposition_sun__流年海王星冲_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneOppositionSun流年海王星冲(SemanticEntry):
    """
    > Others may deceive or confuse you about who you are. May feel undermined. Good for seeing ego illu...
    """
    
    original_text: str = """> Others may deceive or confuse you about who you are. May feel undermined. Good for seeing ego illusions. Relationships may be confusing.

**Narrative Snippets**:
- `[ns_pit_ne017]` `[trigger: transit_neptune_opposition_natal_sun]` `[factor_trigger: astro_transit_neptune OPPOSITION natal_sun]` `[role: 主干]` Others may deceive or confuse. See ego illusions. Relationships confusing. → PIT Ch12 Neptune☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Opposition Sun (流年海王星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_neptune_opposition_sun__流年海王星冲_001_L1",
    )
    version: str = "1.0.0"
