"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224001
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
    semantic_id="pit_v1.0.0_sun_square_sun__流年太阳刑本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareSun流年太阳刑本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 2041-2066):
> This transit occurs roughly three months after and three months...
    """
    
    original_text: str = """**Source Text** (Lines 2041-2066):
> This transit occurs roughly three months after and three months before your birthday. In both cases it is a transit of challenge and crisis. You should watch for circumstances that will test you and the validity of whatever you are doing.
> 
> Very often this crisis occurs in the form of persons who are working at cross-purposes to your efforts. On the square three months after your birthday, challenges may occur in connection with building something up. On the square three months before, you will be challenged in completing projects and reaping rewards.

**English Paraphrase**: Occurs ~3 months before/after birthday. Transit of challenge and crisis; watch for testing circumstances. Crisis often through persons at cross-purposes. Post-birthday square: challenges in building up. Pre-birthday square: challenges in completing and reaping rewards.

**Complete Chinese Interpretation**: 发生在生日前后约三个月。挑战和危机的行运；注意测试性情况。危机常通过目的相悖的人出现。生日后刑相：建设中的挑战。生日前刑相：完成和收获中的挑战。

**Narrative Snippets**:
- `[ns_pit_049]` `[trigger: transit_sun_square_natal_sun]` `[factor_trigger: astro_transit_sun SQUARE natal_sun]` `[role: 主干]` A transit of challenge and crisis—watch for circumstances that test you and the validity of what you're doing. → PIT Ch4 Sun□Sun
- `[ns_pit_050]` `[trigger: transit_sun_square_natal_sun]` `[factor_trigger: astro_transit_sun SQUARE natal_sun]` `[role: 条件分支]` Crisis often through persons at cross-purposes. Three months after: building challenges. Three months before: completion challenges. → PIT Ch4 Sun□Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Sun (流年太阳刑本命太阳)"
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
        l1_anchor="pit_v1.0.0_sun_square_sun__流年太阳刑本命太阳_001_L1",
    )
    version: str = "1.0.0"
