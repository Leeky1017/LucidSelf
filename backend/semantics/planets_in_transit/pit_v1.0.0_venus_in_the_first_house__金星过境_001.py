"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258584
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
    semantic_id="pit_v1.0.0_venus_in_the_first_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheFirstHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6814-6831):
> Venus influences your whole manner of expressing yourself. Grea...
    """
    
    original_text: str = """**Source Text** (Lines 6814-6831):
> Venus influences your whole manner of expressing yourself. Great desire to relate to others, willing to make personal compromises. Feel rather unaggressive, may not defend your own rights. Work out compromise or evade contest. Project warmth and social agreeableness. Good time to make peace among others. Good time to have fun with friends, vacation, do what you enjoy. May attract other people due to Yin action of Venus.

**English Paraphrase**: Desire to relate, willing to compromise. Unaggressive, may not defend rights. Project warmth, make peace. Good for fun, vacation. Attract people naturally.

**Complete Chinese Interpretation**: 渴望与人建立关系，愿意妥协。不具攻击性，可能不会捍卫权利。展现温暖，促进和平。适合娱乐、度假。自然吸引他人。

**Narrative Snippets**:
- `[ns_pit_ve001]` `[trigger: venus_transit_house_1]` `[factor_trigger: astro_transit_venus AND astro_house_1]` `[role: 主干]` Desire to relate, willing to compromise. Project warmth, attract people naturally. → PIT Ch7 Venus-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the First House (金星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_first_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
