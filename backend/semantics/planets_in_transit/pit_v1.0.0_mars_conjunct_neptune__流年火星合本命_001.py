"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288583
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
    semantic_id="pit_v1.0.0_mars_conjunct_neptune__流年火星合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsConjunctNeptune流年火星合本命(SemanticEntry):
    """
    > Energy confused or inspired. Actions may be unclear. Good for spiritual/creative action. Avoid dec...
    """
    
    original_text: str = """> Energy confused or inspired. Actions may be unclear. Good for spiritual/creative action. Avoid deception. Low physical energy possible.

**Narrative Snippets**:
- `[ns_pit_ma053]` `[trigger: transit_mars_conjunct_natal_neptune]` `[factor_trigger: astro_transit_mars CONJUNCT natal_neptune]` `[role: 主干]` Energy confused or inspired. Good for creative action. Avoid deception. → PIT Ch8 Mars☌Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Conjunct Neptune (流年火星合本命海王星)"
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
        l1_anchor="pit_v1.0.0_mars_conjunct_neptune__流年火星合本命_001_L1",
    )
    version: str = "1.0.0"
