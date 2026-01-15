"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206943
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
    semantic_id="pit_v1.0.0_uranus_conjunct_sun__流年天王星合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusConjunctSun流年天王星合本命太(SemanticEntry):
    """
    > Powerful urge for freedom and self-expression. May make radical changes. Break from past. Exciting...
    """
    
    original_text: str = """> Powerful urge for freedom and self-expression. May make radical changes. Break from past. Exciting but potentially disruptive. New sense of identity possible. Don't act rashly—channel constructively.

**Narrative Snippets**:
- `[ns_pit_ur013]` `[trigger: transit_uranus_conjunct_natal_sun]` `[factor_trigger: astro_transit_uranus CONJUNCT natal_sun]` `[role: 主干]` Powerful freedom urge. Radical changes. New identity. Channel constructively. → PIT Ch11 Uranus☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus Conjunct Sun (流年天王星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_uranus_conjunct_sun__流年天王星合本命太_001_L1",
    )
    version: str = "1.0.0"
