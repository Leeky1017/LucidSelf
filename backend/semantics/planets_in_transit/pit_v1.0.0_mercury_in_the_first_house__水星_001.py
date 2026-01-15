"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280676
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
    semantic_id="pit_v1.0.0_mercury_in_the_first_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheFirstHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 4975-5001):
> Good time for expressing your point of view. You put a great de...
    """
    
    original_text: str = """**Source Text** (Lines 4975-5001):
> Good time for expressing your point of view. You put a great deal of yourself into whatever you say. Capacity to examine yourself with greater objectivity. Mind will be more active—keep it occupied with useful projects. Mind jumps from issue to issue rapidly. Mercury doesn't settle on any one issue for long—try to control this. May react with nervousness or anxiety if afflicted. Strong urge to travel short distances. Good time for negotiations or contract discussions.

**English Paraphrase**: Good for expressing your viewpoint authentically. Greater mental activity and self-examination capacity. Mind jumps rapidly—control this tendency. May feel nervous if afflicted. Urge to travel. Good for negotiations.

**Complete Chinese Interpretation**: 表达观点的好时机，真实地表达自己。心智活动增强，自我审视能力提高。思维跳跃迅速——控制这种倾向。如受刑可能感到紧张。有旅行冲动。适合谈判。

**Narrative Snippets**:
- `[ns_pit_me001]` `[trigger: mercury_transit_house_1]` `[factor_trigger: astro_transit_mercury AND astro_house_1]` `[role: 主干]` Good for expressing viewpoint authentically. Mind more active but jumps rapidly. → PIT Ch6 Mercury-1H
- `[ns_pit_me002]` `[trigger: mercury_transit_house_1]` `[factor_trigger: astro_transit_mercury AND astro_house_1]` `[role: 条件分支]` Good for negotiations. May feel nervous if afflicted. → PIT Ch6 Mercury-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the First House (水星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_first_house__水星_001_L1",
    )
    version: str = "1.0.0"
