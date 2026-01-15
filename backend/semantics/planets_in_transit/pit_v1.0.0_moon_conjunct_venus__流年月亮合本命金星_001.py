"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301267
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
    semantic_id="pit_v1.0.0_moon_conjunct_venus__流年月亮合本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctVenus流年月亮合本命金星(SemanticEntry):
    """
    > Feelings of love, affection, and appreciation for beauty are heightened. Excellent for socializing...
    """
    
    original_text: str = """> Feelings of love, affection, and appreciation for beauty are heightened. Excellent for socializing, romance, and enjoying pleasures. Feel attractive and attracted. Good for artistic activities and beautifying surroundings. Harmonious relations, especially with women.

**Narrative Snippets**:
- `[ns_pit_m041]` `[trigger: transit_moon_conjunct_natal_venus]` `[factor_trigger: astro_transit_moon CONJUNCT natal_venus]` `[role: 主干]` Love and affection heightened—excellent for socializing, romance, artistic activities. → PIT Ch5 Moon☌Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Venus (流年月亮合本命金星)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_venus__流年月亮合本命金星_001_L1",
    )
    version: str = "1.0.0"
