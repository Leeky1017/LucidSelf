"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280888
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
    semantic_id="pit_v1.0.0_mercury_opposition_sun__流年水星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryOppositionSun流年水星冲本(SemanticEntry):
    """
    > Increases flow of communication but can indicate ego conflicts expressed verbally. High-energy tra...
    """
    
    original_text: str = """> Increases flow of communication but can indicate ego conflicts expressed verbally. High-energy transit—be careful. May feel urgent message to deliver. Others may be strongly opposed. Compromise may be necessary via third party. Communications clear though not harmonious. Use time to understand positions.

**Narrative Snippets**:
- `[ns_pit_me019]` `[trigger: transit_mercury_opposition_natal_sun]` `[factor_trigger: astro_transit_mercury OPPOSITION natal_sun]` `[role: 主干]` Increases communication but ego conflicts possible. Clear but not harmonious. → PIT Ch6 Mercury☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Opposition Sun (流年水星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_mercury_opposition_sun__流年水星冲本_001_L1",
    )
    version: str = "1.0.0"
