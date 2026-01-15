"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309785
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
    semantic_id="pit_v1.0.0_jupiter_in_the_sixth_house__木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheSixthHouse木星(SemanticEntry):
    """
    **Source Text** (Lines 10325-10349):
> Very good for any kind of work and fulfilling duties. Indicat...
    """
    
    original_text: str = """**Source Text** (Lines 10325-10349):
> Very good for any kind of work and fulfilling duties. Indicates good health with one exception. Demands of this house can conflict with personal growth—house of duty and service. But with Jupiter, progress precisely because of these matters. Work fulfilling and enjoyable, gives sense of purpose. Often improved job situation, better pay or opportunities. But not likely to advance to greater power—this is a period of work. Gain esteem of superiors and those under you. Excellent for health, but be careful of gaining weight. Avoid overindulgence.

**English Paraphrase**: Good for work and duties. Good health except weight gain. Work fulfilling and enjoyable. May improve job situation. Not promotion time but gain esteem. Watch weight and overindulgence.

**Complete Chinese Interpretation**: 适合工作和职责。健康好但注意体重增加。工作充实而愉快。可能改善工作状况。不是晋升时间但获得尊重。注意体重和过度放纵。

**Narrative Snippets**:
- `[ns_pit_ju006]` `[trigger: jupiter_transit_house_6]` `[factor_trigger: astro_transit_jupiter AND astro_house_6]` `[role: 主干]` Good for work. Health good but watch weight. Work fulfilling. Gain esteem. → PIT Ch9 Jupiter-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Sixth House (木星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_sixth_house__木星_001_L1",
    )
    version: str = "1.0.0"
