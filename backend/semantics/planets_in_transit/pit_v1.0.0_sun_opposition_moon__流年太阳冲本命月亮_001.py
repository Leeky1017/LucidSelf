"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224195
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
    semantic_id="pit_v1.0.0_sun_opposition_moon__流年太阳冲本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionMoon流年太阳冲本命月亮(SemanticEntry):
    """
    **Source Text** (Lines 2264-2291):
> This may be a tense day, but it is an important one. Events tod...
    """
    
    original_text: str = """**Source Text** (Lines 2264-2291):
> This may be a tense day, but it is an important one. Events today may show how well you cope with daily and routine aspects of your life.
> 
> You will probably encounter tension between your personal needs and your public/professional duties. You may feel pulled in two different directions. Your emotional nature will come out in one way or another. If you have been in touch with your feelings, you will go through the day with a feeling of complete unity.

**English Paraphrase**: Tense but important day; events show coping ability. Tension between personal needs and public/professional duties. Feel pulled in two directions. Emotional nature will emerge. If in touch with feelings, feel complete unity; if not, day becomes very tense.

**Complete Chinese Interpretation**: 紧张但重要的一天；事件显示应对能力。个人需求与公共/职业责任之间的紧张。感觉被拉向两个方向。情感本性会浮现。如果接触感受，感到完全统一；如果没有，一天变得非常紧张。

**Narrative Snippets**:
- `[ns_pit_063]` `[trigger: transit_sun_opposition_natal_moon]` `[factor_trigger: astro_transit_sun OPPOSITION natal_moon]` `[role: 主干]` Tense but important day—tension between personal needs and public/professional duties. → PIT Ch4 Sun☍Moon
- `[ns_pit_064]` `[trigger: transit_sun_opposition_natal_moon]` `[factor_trigger: astro_transit_sun OPPOSITION natal_moon]` `[role: 条件分支]` Emotional nature will emerge. If in touch with feelings: complete unity. If not: very tense. → PIT Ch4 Sun☍Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Moon (流年太阳冲本命月亮)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_moon__流年太阳冲本命月亮_001_L1",
    )
    version: str = "1.0.0"
