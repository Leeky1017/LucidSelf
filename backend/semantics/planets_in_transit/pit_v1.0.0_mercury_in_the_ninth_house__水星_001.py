"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280799
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
    semantic_id="pit_v1.0.0_mercury_in_the_ninth_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheNinthHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 5167-5186):
> Good for study and education—intellectually eager for knowledge...
    """
    
    original_text: str = """**Source Text** (Lines 5167-5186):
> Good for study and education—intellectually eager for knowledge. Want larger view of life, how parts fit into whole. Foreign places, law, philosophy, higher knowledge attract attention. Good time to travel—curiosity makes it interesting. Expose yourself to different lifestyles. Good for conversation about abstract ideas. More tolerant of different opinions.

**English Paraphrase**: Good for study/education. Want larger view of life. Foreign, law, philosophy attract. Good for travel. Expose to different lifestyles. Talk about abstract ideas. More tolerant.

**Complete Chinese Interpretation**: 适合学习/教育。想要更大的人生视野。外国、法律、哲学吸引。适合旅行。接触不同生活方式。谈论抽象想法。更包容。

**Narrative Snippets**:
- `[ns_pit_me010]` `[trigger: mercury_transit_house_9]` `[factor_trigger: astro_transit_mercury AND astro_house_9]` `[role: 主干]` Good for study, education, travel. Want larger view. More tolerant of different opinions. → PIT Ch6 Mercury-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Ninth House (水星过境第九宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_ninth_house__水星_001_L1",
    )
    version: str = "1.0.0"
