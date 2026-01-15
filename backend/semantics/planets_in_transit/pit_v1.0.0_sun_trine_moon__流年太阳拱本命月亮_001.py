"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224183
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
    semantic_id="pit_v1.0.0_sun_trine_moon__流年太阳拱本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineMoon流年太阳拱本命月亮(SemanticEntry):
    """
    **Source Text** (Lines 2235-2263):
> Like the sextile, the trine transit is a time of inner peace an...
    """
    
    original_text: str = """**Source Text** (Lines 2235-2263):
> Like the sextile, the trine transit is a time of inner peace and balance. You have the serenity to look into yourself and come to a deeper understanding of what you want, what you need and how to get it.
> 
> Since this is a time of balance, study your personal life and find out what you need to do to correct any misunderstandings. Today you are able to make the compromises necessary to getting along with others. Friendships and love relationships that start under this transit will have important consequences for your future.

**English Paraphrase**: Inner peace and balance; serenity to understand wants, needs, and methods. Study personal life, correct misunderstandings. Able to make necessary compromises. Relationships started now have important future consequences.

**Complete Chinese Interpretation**: 内心平和与平衡；宁静地理解想要、需要和方法。研究个人生活，纠正误解。能够做出必要的妥协。现在开始的关系对未来有重要影响。

**Narrative Snippets**:
- `[ns_pit_061]` `[trigger: transit_sun_trine_natal_moon]` `[factor_trigger: astro_transit_sun TRINE natal_moon]` `[role: 主干]` Inner peace and balance—serenity to understand what you want, need, and how to get it. → PIT Ch4 Sun△Moon
- `[ns_pit_062]` `[trigger: transit_sun_trine_natal_moon]` `[factor_trigger: astro_transit_sun TRINE natal_moon]` `[role: 主干依赖]` Make necessary compromises. Relationships started now have important future consequences. → PIT Ch4 Sun△Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Moon (流年太阳拱本命月亮)"
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
        l1_anchor="pit_v1.0.0_sun_trine_moon__流年太阳拱本命月亮_001_L1",
    )
    version: str = "1.0.0"
