"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280877
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
    semantic_id="pit_v1.0.0_mercury_trine_sun__流年水星拱本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryTrineSun流年水星拱本命太阳(SemanticEntry):
    """
    > Favorable for mental work and communication. Mind unusually clear, know what you want. Can state y...
    """
    
    original_text: str = """> Favorable for mental work and communication. Mind unusually clear, know what you want. Can state your case forcefully. Good for paperwork, letters, phone calls. Good for group discussions and negotiations. Good for organizing. Great curiosity for new studies.

**Narrative Snippets**:
- `[ns_pit_me018]` `[trigger: transit_mercury_trine_natal_sun]` `[factor_trigger: astro_transit_mercury TRINE natal_sun]` `[role: 主干]` Favorable for mental work. Mind clear, state case forcefully. Good for organizing. → PIT Ch6 Mercury△Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury Trine Sun (流年水星拱本命太阳)"
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
        l1_anchor="pit_v1.0.0_mercury_trine_sun__流年水星拱本命太阳_001_L1",
    )
    version: str = "1.0.0"
