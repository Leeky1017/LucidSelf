"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288615
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
    semantic_id="pit_v1.0.0_mars_trine_neptune__流年火星拱本命海王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsTrineNeptune流年火星拱本命海王星(SemanticEntry):
    """
    > Beautiful inspired action. Creative and spiritual activities excel. Compassionate strength.

**Nar...
    """
    
    original_text: str = """> Beautiful inspired action. Creative and spiritual activities excel. Compassionate strength.

**Narrative Snippets**:
- `[ns_pit_ma056]` `[trigger: transit_mars_trine_natal_neptune]` `[factor_trigger: astro_transit_mars TRINE natal_neptune]` `[role: 主干]` Inspired action. Creative and spiritual activities excel. → PIT Ch8 Mars△Neptune"""
    normalized_text_zh: str = """"""
    subject: str = "Mars Trine Neptune (流年火星拱本命海王星)"
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
        l1_anchor="pit_v1.0.0_mars_trine_neptune__流年火星拱本命海王星_001_L1",
    )
    version: str = "1.0.0"
