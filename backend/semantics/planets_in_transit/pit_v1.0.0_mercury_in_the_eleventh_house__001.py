"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280823
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
    semantic_id="pit_v1.0.0_mercury_in_the_eleventh_house__001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheEleventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 5213-5230):
> Think about goals and expectations in life. Examine ideals—how ...
    """
    
    original_text: str = """**Source Text** (Lines 5213-5230):
> Think about goals and expectations in life. Examine ideals—how well have they served you. Are goals really your own or adopted from others. House of group ideals and your position in groups. More verbal and intellectual exchanges with friends. Talking with friends helps reach objective viewpoint. May encounter younger people in circle of friends.

**English Paraphrase**: Think about goals and ideals. Are they yours or adopted? Examine group position. More exchanges with friends. Friends help objectivity. May meet younger people.

**Complete Chinese Interpretation**: 思考目标和理想。是你自己的还是采纳的？检视群体地位。与朋友更多交流。朋友帮助客观。可能遇到年轻人。

**Narrative Snippets**:
- `[ns_pit_me012]` `[trigger: mercury_transit_house_11]` `[factor_trigger: astro_transit_mercury AND astro_house_11]` `[role: 主干]` Think about goals—are they yours? More exchanges with friends help objectivity. → PIT Ch6 Mercury-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Eleventh House (水星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_eleventh_house__001_L1",
    )
    version: str = "1.0.0"
