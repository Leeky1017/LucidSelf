"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318494
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
    semantic_id="pit_v1.0.0_saturn_in_the_tenth_house__土星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheTenthHouse土星过(SemanticEntry):
    """
    **Source Text** (Lines 12513-12545):
> Represents the harvest. Experience consequences of preparatio...
    """
    
    original_text: str = """**Source Text** (Lines 12513-12545):
> Represents the harvest. Experience consequences of preparations over last 20-24 years. If prepared well, results excellent; if not, basis of difficulties. Professional life—gain many responsibilities. If ever to be a leader, it will be now. If prefer not to lead, may be onerous but productive. Function with most complete sense of who you are. Greatest opportunity to make impression on world as individual. But can also be time of disaster—negative energies have consequences now. Nixon resigned during this transit. Dangerous if difficult aspects natally. Control results by preparing carefully, no shortcuts. May focus so much on external that overlook personal life—why 4H foundation was important 14 years ago. If prepared well, most rewarding time—you earned it.

**English Paraphrase**: The harvest. Consequences of 20-24 years preparation. If well prepared, excellent results. Greatest professional responsibilities. Leaders emerge now. Greatest opportunity for individual impact. Can be disaster if negatives activated. Prepare carefully, no shortcuts. Balance external focus with personal life.

**Complete Chinese Interpretation**: 收获期。20-24年准备的后果。如果准备充分，结果优秀。最大的职业责任。领导者现在出现。个人影响的最大机会。如果负面被激活可能是灾难。仔细准备，没有捷径。平衡外部焦点与个人生活。

**Narrative Snippets**:
- `[ns_pit_sa010]` `[trigger: saturn_transit_house_10]` `[factor_trigger: astro_transit_saturn AND astro_house_10]` `[role: 主干]` The harvest. Career peak. Greatest responsibility. Results depend on preparation. No shortcuts. → PIT Ch10 Saturn-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Tenth House (土星过境第十宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_tenth_house__土星过_001_L1",
    )
    version: str = "1.0.0"
