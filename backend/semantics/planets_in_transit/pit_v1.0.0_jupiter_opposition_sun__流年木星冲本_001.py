"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309967
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
    semantic_id="pit_v1.0.0_jupiter_opposition_sun__流年木星冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterOppositionSun流年木星冲本(SemanticEntry):
    """
    > Others bring opportunities but may overextend through them. Check promises. Others may expect too ...
    """
    
    original_text: str = """> Others bring opportunities but may overextend through them. Check promises. Others may expect too much. Good for seeing your expansive patterns. Balance enthusiasm with realism.

**Narrative Snippets**:
- `[ns_pit_ju017]` `[trigger: transit_jupiter_opposition_natal_sun]` `[factor_trigger: astro_transit_jupiter OPPOSITION natal_sun]` `[role: 主干]` Others bring opportunities. Watch overextension. Balance enthusiasm. → PIT Ch9 Jupiter☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Opposition Sun (流年木星冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_jupiter_opposition_sun__流年木星冲本_001_L1",
    )
    version: str = "1.0.0"
