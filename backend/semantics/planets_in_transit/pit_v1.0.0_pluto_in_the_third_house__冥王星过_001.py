"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237925
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
    semantic_id="pit_v1.0.0_pluto_in_the_third_house__冥王星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheThirdHouse冥王星过(SemanticEntry):
    """
    **Source Text** (Lines 18821-18854):
> Everyday contacts and communications take on heavier tone. El...
    """
    
    original_text: str = """**Source Text** (Lines 18821-18854):
> Everyday contacts and communications take on heavier tone. Elements normally taken for granted—neighbors, relatives, daily business—now fraught with significance. Forced to examine day-to-day actions as never before. Great changes triggered by circumstances in immediate environment. Situations contended with for years may reach crisis point—beginning of deep psychological change and inner regeneration continuing many years. Examine everyday beliefs—ideas held true without question may be undermining life in subtle way. Not good to take anything for granted—repressed psychological tensions will surface. Difficult to keep problems buried. Acute self-questioning. Don't assume wrong about everything. Not taking for granted doesn't mean wrong—just became so used they no longer register. To be aware is to experience. Don't settle for superficial explanations—get close to inner workings. May become interested in psychology, yoga, occult studies. Changes of scene and short trips may trigger important far-reaching changes.

**English Paraphrase**: Everyday contacts take on heavy significance. Crisis points reached. Beginning of deep psychological change. Examine beliefs—repressed tensions surface. Acute self-questioning. Seek inner workings. May study psychology, yoga, occult. Short trips trigger changes.

**Complete Chinese Interpretation**: 日常接触变得意义重大。到达危机点。深层心理变化的开始。审视信念——压抑的紧张浮出水面。深刻的自我质疑。寻求内在运作。可能学习心理学、瑜伽、神秘学。短途旅行触发变化。

**Narrative Snippets**:
- `[ns_pit_pl003]` `[trigger: pluto_transit_house_3]` `[factor_trigger: astro_transit_pluto AND astro_house_3]` `[role: 主干]` Everyday contacts significant. Crisis points. Deep psychological change begins. Self-questioning. → PIT Ch13 Pluto-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Third House (冥王星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_third_house__冥王星过_001_L1",
    )
    version: str = "1.0.0"
