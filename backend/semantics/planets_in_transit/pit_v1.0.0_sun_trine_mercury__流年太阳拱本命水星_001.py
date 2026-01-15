"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224238
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
    semantic_id="pit_v1.0.0_sun_trine_mercury__流年太阳拱本命水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineMercury流年太阳拱本命水星(SemanticEntry):
    """
    **Source Text** (Lines 2367-2385):
> Under this transit you can increase your understanding of yours...
    """
    
    original_text: str = """**Source Text** (Lines 2367-2385):
> Under this transit you can increase your understanding of yourself and your goals, as well as of others and their goals. Your mind is functioning clearly now. You are aware that your thinking and ideas have made an impact on others. This is a good time for all kinds of studying and learning. Your mind is relatively tranquil, making this a good time to look over your general situation. Excellent for beginning a trip for recreational or business purposes.

**English Paraphrase**: Increase understanding of self, others, and goals. Mind functions clearly; aware of your impact on others. Good for studying and learning. Mind tranquil—review general situation. Excellent for starting trips.

**Complete Chinese Interpretation**: 增加对自己、他人和目标的理解。头脑运作清晰；意识到你对他人的影响。适合学习。头脑平静——审视总体情况。开始旅行极好。

**Narrative Snippets**:
- `[ns_pit_070]` `[trigger: transit_sun_trine_natal_mercury]` `[factor_trigger: astro_transit_sun TRINE natal_mercury]` `[role: 主干]` Increase understanding of yourself and your goals—mind functioning clearly, aware of your impact on others. → PIT Ch4 Sun△Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Mercury (流年太阳拱本命水星)"
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
        l1_anchor="pit_v1.0.0_sun_trine_mercury__流年太阳拱本命水星_001_L1",
    )
    version: str = "1.0.0"
