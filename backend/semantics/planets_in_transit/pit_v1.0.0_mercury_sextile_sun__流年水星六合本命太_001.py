"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280856
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
    semantic_id="pit_v1.0.0_mercury_sextile_sun__流年水星六合本命太_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercurySextileSun流年水星六合本命太(SemanticEntry):
    """
    > Busy but mentally stimulating day. Mind sharp, alive, ready for experiences. Great curiosity. Tele...
    """
    
    original_text: str = """> Busy but mentally stimulating day. Mind sharp, alive, ready for experiences. Great curiosity. Telephone never seems to stop ringing. Let people know where you stand—honesty commands respect. Good for group discussions and reporting. May travel more than usual.

**Narrative Snippets**:
- `[ns_pit_me016]` `[trigger: transit_mercury_sextile_natal_sun]` `[factor_trigger: astro_transit_mercury SEXTILE natal_sun]` `[role: 主干]` Busy, stimulating. Mind sharp with great curiosity. Good for group discussions. → PIT Ch6 Mercury⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Sextile Sun (流年水星六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_mercury_sextile_sun__流年水星六合本命太_001_L1",
    )
    version: str = "1.0.0"
