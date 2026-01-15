"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224454
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
    semantic_id="pit_v1.0.0_sun_square_jupiter__流年太阳刑本命木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareJupiter流年太阳刑本命木星(SemanticEntry):
    """
    **Source Text** (Lines 2734-2753):
> Extremely useful square—gives energy to get ahead, provided you...
    """
    
    original_text: str = """**Source Text** (Lines 2734-2753):
> Extremely useful square—gives energy to get ahead, provided you are disciplined and avoid excess. Difficulty: spurs you to do more than you can handle, projects beyond your energy or resources. But same tendency can lift you to attempt and succeed at tasks you wouldn't usually consider. Depends on whether you're naturally cautious or overoptimistic. Can make you generous or extravagant. Watch self-righteousness—be compassionate instead.

**English Paraphrase**: Useful square—energy to get ahead if disciplined. Difficulty: overextension. But can lift you to succeed at tasks you wouldn't consider. Depends on natural tendency (cautious vs overoptimistic). Generous or extravagant. Avoid self-righteousness—be compassionate.

**Complete Chinese Interpretation**: 有用的刑相——如果有纪律则有能量前进。困难：过度扩张。但可以提升你成功完成通常不会考虑的任务。取决于自然倾向（谨慎vs过度乐观）。慷慨或挥霍。避免自以为是——要有同情心。

**Narrative Snippets**:
- `[ns_pit_094]` `[trigger: transit_sun_square_natal_jupiter]` `[factor_trigger: astro_transit_sun SQUARE natal_jupiter]` `[role: 主干]` Useful square—energy to get ahead if disciplined. Can lift you to succeed at tasks you wouldn't consider. → PIT Ch4 Sun□Jupiter
- `[ns_pit_095]` `[trigger: transit_sun_square_natal_jupiter]` `[factor_trigger: astro_transit_sun SQUARE natal_jupiter]` `[role: 条件分支]` Difficulty: overextension. Avoid self-righteousness—be compassionate. → PIT Ch4 Sun□Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Jupiter (流年太阳刑本命木星)"
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
        l1_anchor="pit_v1.0.0_sun_square_jupiter__流年太阳刑本命木星_001_L1",
    )
    version: str = "1.0.0"
