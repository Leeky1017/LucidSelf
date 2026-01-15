"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.259520
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
    semantic_id="pit_v1.0.0_venus_sextile_jupiter__流年金星六合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusSextileJupiter流年金星六合本(SemanticEntry):
    """
    > Pleasant and optimistic. Social and financial opportunities. Good for travel, education, legal. Ge...
    """
    
    original_text: str = """> Pleasant and optimistic. Social and financial opportunities. Good for travel, education, legal. Generosity flows.

**Narrative Snippets**:
- `[ns_pit_ve039]` `[trigger: transit_venus_sextile_natal_jupiter]` `[factor_trigger: astro_transit_venus SEXTILE natal_jupiter]` `[role: 主干]` Pleasant and optimistic. Social and financial opportunities. → PIT Ch7 Venus⚹Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Venus Sextile Jupiter (流年金星六合本命木星)"
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
        l1_anchor="pit_v1.0.0_venus_sextile_jupiter__流年金星六合本_001_L1",
    )
    version: str = "1.0.0"
