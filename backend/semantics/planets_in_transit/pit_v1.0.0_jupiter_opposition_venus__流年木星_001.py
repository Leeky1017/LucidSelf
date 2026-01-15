"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.310165
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
    semantic_id="pit_v1.0.0_jupiter_opposition_venus__流年木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterOppositionVenus流年木星(SemanticEntry):
    """
    > Others bring love/financial opportunities but watch overextension. Social or financial excess poss...
    """
    
    original_text: str = """> Others bring love/financial opportunities but watch overextension. Social or financial excess possible. Balance generosity.

**Narrative Snippets**:
- `[ns_pit_ju032]` `[trigger: transit_jupiter_opposition_natal_venus]` `[factor_trigger: astro_transit_jupiter OPPOSITION natal_venus]` `[role: 主干]` Others bring opportunities. Watch overextension. Balance. → PIT Ch9 Jupiter☍Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Opposition Venus (流年木星冲本命金星)"
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
        l1_anchor="pit_v1.0.0_jupiter_opposition_venus__流年木星_001_L1",
    )
    version: str = "1.0.0"
