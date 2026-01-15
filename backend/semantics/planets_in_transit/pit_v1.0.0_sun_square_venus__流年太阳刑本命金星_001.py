"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224282
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
    semantic_id="pit_v1.0.0_sun_square_venus__流年太阳刑本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareVenus流年太阳刑本命金星(SemanticEntry):
    """
    **Source Text** (Lines 2465-2489):
> Not a typical square—usually quite pleasant. Dynamic influence ...
    """
    
    original_text: str = """**Source Text** (Lines 2465-2489):
> Not a typical square—usually quite pleasant. Dynamic influence makes you actively seek pleasure, beauty, love, harmony. Probably not aggressive—prefer to take it easy. Positive: feeling loving and affectionate, possible new love or creative work. Negative: excessive self-gratification or at loved one's expense. Can reveal hidden relationship strains. Avoid spending on foolish whims. Watch passivity—sitting and waiting for things to come to you.

**English Paraphrase**: Not typical square—usually pleasant. Actively seek pleasure, beauty, love. Not aggressive—take it easy. Positive: loving feelings, new love possible, creative work. Negative: excess or at loved one's expense. Reveals hidden strains. Avoid foolish spending. Watch passivity.

**Complete Chinese Interpretation**: 不是典型刑相——通常愉快。积极寻求快乐、美、爱。不好斗——放松。正面：充满爱的感觉，可能有新恋情，创意工作。负面：过度或以牺牲所爱之人为代价。揭示隐藏的紧张。避免愚蠢的花费。注意被动性。

**Narrative Snippets**:
- `[ns_pit_076]` `[trigger: transit_sun_square_natal_venus]` `[factor_trigger: astro_transit_sun SQUARE natal_venus]` `[role: 主干]` Not typical square—usually pleasant. Actively seek pleasure, beauty, love. Feeling loving, creative. → PIT Ch4 Sun□Venus
- `[ns_pit_077]` `[trigger: transit_sun_square_natal_venus]` `[factor_trigger: astro_transit_sun SQUARE natal_venus]` `[role: 条件分支]` Negative: excessive self-gratification. Can reveal hidden relationship strains. Avoid foolish spending and passivity. → PIT Ch4 Sun□Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Venus (流年太阳刑本命金星)"
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
        l1_anchor="pit_v1.0.0_sun_square_venus__流年太阳刑本命金星_001_L1",
    )
    version: str = "1.0.0"
