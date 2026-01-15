"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309734
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
    semantic_id="pit_v1.0.0_jupiter_in_the_second_house__木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheSecondHouse木(SemanticEntry):
    """
    **Source Text** (Lines 10192-10223):
> Traditionally associated with making money. Actualizing whate...
    """
    
    original_text: str = """**Source Text** (Lines 10192-10223):
> Traditionally associated with making money. Actualizing whatever you value. If money, that's where you increase; if spiritual values, increase there. Important to understand how you use resources—may get more but potential for mismanagement. Look at overall goals honestly. Make necessary changes to attain goals. Not call for asceticism—expensive purchases okay if you really want them. Material resources can be comfort. Learn about yourself through handling possessions. Good time to invest.

**English Paraphrase**: May make money. Actualize what you value. Understand resource use—may get more but watch mismanagement. Look at goals honestly. Make changes to attain them. Okay to buy if really wanted. Good time to invest.

**Complete Chinese Interpretation**: 可能赚钱。实现你看重的。理解资源使用——可能得到更多但注意管理不善。诚实看待目标。做出改变以达成。如果真的想要可以购买。投资的好时机。

**Narrative Snippets**:
- `[ns_pit_ju002]` `[trigger: jupiter_transit_house_2]` `[factor_trigger: astro_transit_jupiter AND astro_house_2]` `[role: 主干]` May increase wealth. Actualize values. Good for investment but watch mismanagement. → PIT Ch9 Jupiter-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Second House (木星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_second_house__木_001_L1",
    )
    version: str = "1.0.0"
