"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.287902
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
    semantic_id="pit_v1.0.0_mars_in_the_first_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheFirstHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8272-8293):
> Time of great activity, work hard to further your own interests...
    """
    
    original_text: str = """**Source Text** (Lines 8272-8293):
> Time of great activity, work hard to further your own interests and assert yourself. Chance to show the world what you can do. Come on with more vigor than usual. If insensitive to others, can be difficult for all relationships. Better to work independently. More of a fighter for your own rights. Physical energy level quite high. Should be positive time of upbeat independent activity.

**English Paraphrase**: Great activity, assert yourself. Show what you can do. Work independently if possible. Fighter for your rights. High physical energy. Positive independent activity.

**Complete Chinese Interpretation**: 活动量大，展示自己。展现你能做什么。如果可能独立工作。为你的权利而战。高度体能。积极独立的活动。

**Narrative Snippets**:
- `[ns_pit_ma001]` `[trigger: mars_transit_house_1]` `[factor_trigger: astro_transit_mars AND astro_house_1]` `[role: 主干]` Great activity, assert yourself. High physical energy. Positive independent activity. → PIT Ch8 Mars-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the First House (火星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_first_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
