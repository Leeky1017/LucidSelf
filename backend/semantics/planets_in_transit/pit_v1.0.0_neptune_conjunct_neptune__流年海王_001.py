"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.273168
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
    semantic_id="pit_v1.0.0_neptune_conjunct_neptune__流年海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneConjunctNeptune流年海王(SemanticEntry):
    """
    > Neptune Return (~165 years). Almost no one experiences this. Complete spiritual cycle if lived.

*...
    """
    
    original_text: str = """> Neptune Return (~165 years). Almost no one experiences this. Complete spiritual cycle if lived.

**Narrative Snippets**:
- `[ns_pit_ne053]` `[trigger: transit_neptune_conjunct_natal_neptune]` `[factor_trigger: astro_transit_neptune CONJUNCT natal_neptune]` `[role: 主干]` Neptune Return (~165 years). Complete spiritual cycle. → PIT Ch12 Neptune☌Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune Conjunct Neptune (流年海王星合本命海王星)"
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
        l1_anchor="pit_v1.0.0_neptune_conjunct_neptune__流年海王_001_L1",
    )
    version: str = "1.0.0"
