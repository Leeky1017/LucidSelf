"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.281350
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
    semantic_id="pit_v1.0.0_mercury_sextile_pluto__流年水星六合本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercurySextilePluto流年水星六合本(SemanticEntry):
    """
    > Constructive deep thinking. Good for research, psychology, clearing mental clutter. Influence thro...
    """
    
    original_text: str = """> Constructive deep thinking. Good for research, psychology, clearing mental clutter. Influence through words. Persuasive communication.

**Narrative Snippets**:
- `[ns_pit_me061]` `[trigger: transit_mercury_sextile_natal_pluto]` `[factor_trigger: astro_transit_mercury SEXTILE natal_pluto]` `[role: 主干]` Constructive deep thinking. Good for research. Persuasive communication. → PIT Ch6 Mercury⚹Pluto"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Sextile Pluto (流年水星六合本命冥王星)"
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
        l1_anchor="pit_v1.0.0_mercury_sextile_pluto__流年水星六合本_001_L1",
    )
    version: str = "1.0.0"
