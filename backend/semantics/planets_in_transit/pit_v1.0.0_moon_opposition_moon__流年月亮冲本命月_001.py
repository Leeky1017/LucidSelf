"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301210
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
    semantic_id="pit_v1.0.0_moon_opposition_moon__流年月亮冲本命月_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonOppositionMoon流年月亮冲本命月(SemanticEntry):
    """
    > Emotional culmination—full Moon of your lunar cycle. Maximum tension between your needs and others...
    """
    
    original_text: str = """> Emotional culmination—full Moon of your lunar cycle. Maximum tension between your needs and others' needs. Relations with women and family at critical point. Time to see your emotional patterns clearly.

**Narrative Snippets**:
- `[ns_pit_m035]` `[trigger: transit_moon_opposition_natal_moon]` `[factor_trigger: astro_transit_moon OPPOSITION natal_moon]` `[role: 主干]` Emotional culmination—full Moon of lunar cycle. Maximum tension between your needs and others'. → PIT Ch5 Moon☍Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Opposition Moon (流年月亮冲本命月亮)"
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
        l1_anchor="pit_v1.0.0_moon_opposition_moon__流年月亮冲本命月_001_L1",
    )
    version: str = "1.0.0"
