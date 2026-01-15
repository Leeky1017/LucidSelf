"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301546
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
    semantic_id="pit_v1.0.0_moon_conjunct_neptune__流年月亮合本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctNeptune流年月亮合本命(SemanticEntry):
    """
    > Highly sensitive and impressionable. Imagination and intuition strong. May feel confused or dreamy...
    """
    
    original_text: str = """> Highly sensitive and impressionable. Imagination and intuition strong. May feel confused or dreamy. Good for creative and spiritual activities. Avoid deception. Compassion heightened.

**Narrative Snippets**:
- `[ns_pit_m066]` `[trigger: transit_moon_conjunct_natal_neptune]` `[factor_trigger: astro_transit_moon CONJUNCT natal_neptune]` `[role: 主干]` Highly sensitive and impressionable. Imagination strong. Good for creative and spiritual. → PIT Ch5 Moon☌Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Neptune (流年月亮合本命海王星)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_neptune__流年月亮合本命_001_L1",
    )
    version: str = "1.0.0"
