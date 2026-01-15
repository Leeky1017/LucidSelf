"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223857
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
    semantic_id="pit_v1.0.0_sun_in_the_eighth_house__太阳过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheEighthHouse太阳过境第(SemanticEntry):
    """
    **Source Text** (Lines 1853-1881):
> You will consciously direct your attention to the subtler aspec...
    """
    
    original_text: str = """**Source Text** (Lines 1853-1881):
> You will consciously direct your attention to the subtler aspects of your psyche, your feelings and emotions and your general psychological health. Strong psychological compulsions may surface, leading to behavior that you do not understand. These compulsions can force considerable changes in your life.
> 
> With this transit you will have a strong desire to experience life on a feeling level. Each time this transit occurs, you will undergo a significant psychological transformation. Traditionally this is the house of death, usually meaning the death of some aspect of yourself.
> 
> On the material plane, this transit can be a time of great concern about finances or resources held jointly with another person.

**English Paraphrase**: Direct attention to subtler psychic aspects—feelings, emotions, psychological health. Compulsions may surface, forcing considerable changes. Desire to experience life on feeling level. Each transit brings psychological transformation. "Death" usually means transformation, not physical death. Joint finances become concern.

**Complete Chinese Interpretation**: 将注意力指向更微妙的心理层面——感受、情绪、心理健康。强迫可能浮现，迫使重大改变。渴望在感受层面体验生活。每次此行运都带来心理转化。"死亡"通常意味着转化而非真正死亡。共同财务成为关注点。

**Narrative Snippets**:
- `[ns_pit_034]` `[trigger: sun_transit_house_8]` `[factor_trigger: astro_transit_sun AND astro_house_8]` `[role: 主干]` Direct attention to subtler aspects of your psyche—strong psychological compulsions may surface. → PIT Ch4 Sun-8H
- `[ns_pit_035]` `[trigger: sun_transit_house_8]` `[factor_trigger: astro_transit_sun AND astro_house_8]` `[role: 主干依赖]` Each time this transit occurs, you undergo significant psychological transformation—the house of death means death of some aspect of yourself. → PIT Ch4 Sun-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Eighth House (太阳过境第八宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_eighth_house__太阳过境第_001_L1",
    )
    version: str = "1.0.0"
