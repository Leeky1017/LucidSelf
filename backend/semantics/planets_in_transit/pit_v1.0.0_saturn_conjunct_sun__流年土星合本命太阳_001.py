"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318532
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
    semantic_id="pit_v1.0.0_saturn_conjunct_sun__流年土星合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnConjunctSun流年土星合本命太阳(SemanticEntry):
    """
    > Can bring both fulfillment and difficulty. 14 years ago at opposition made new beginnings—now resu...
    """
    
    original_text: str = """> Can bring both fulfillment and difficulty. 14 years ago at opposition made new beginnings—now results. Either successful climax or realize failure. Time of tremendous responsibility and hard work. Even success limits freedom. Be patient, concentrate on tasks. Don't take on new projects not connected to current work.

**Narrative Snippets**:
- `[ns_pit_sa013]` `[trigger: transit_saturn_conjunct_natal_sun]` `[factor_trigger: astro_transit_saturn CONJUNCT natal_sun]` `[role: 主干]` Results of 14-year cycle. Tremendous responsibility. Success or realize failure. → PIT Ch10 Saturn☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Conjunct Sun (流年土星合本命太阳)"
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
        l1_anchor="pit_v1.0.0_saturn_conjunct_sun__流年土星合本命太阳_001_L1",
    )
    version: str = "1.0.0"
