"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309977
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
    semantic_id="pit_v1.0.0_jupiter_conjunct_moon__流年木星合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterConjunctMoon流年木星合本命(SemanticEntry):
    """
    > Emotional expansion and optimism. Feel generous and magnanimous. Good for family, domestic matters...
    """
    
    original_text: str = """> Emotional expansion and optimism. Feel generous and magnanimous. Good for family, domestic matters. May overeat or overindulge emotionally. Home improvements. Protected feeling.

**Narrative Snippets**:
- `[ns_pit_ju018]` `[trigger: transit_jupiter_conjunct_natal_moon]` `[factor_trigger: astro_transit_jupiter CONJUNCT natal_moon]` `[role: 主干]` Emotional expansion. Good for family. Watch overindulgence. → PIT Ch9 Jupiter☌Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Conjunct Moon (流年木星合本命月亮)"
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
        l1_anchor="pit_v1.0.0_jupiter_conjunct_moon__流年木星合本命_001_L1",
    )
    version: str = "1.0.0"
