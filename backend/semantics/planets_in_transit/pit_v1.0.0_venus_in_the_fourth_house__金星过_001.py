"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258698
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
    semantic_id="pit_v1.0.0_venus_in_the_fourth_house__金星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheFourthHouse金星过(SemanticEntry):
    """
    **Source Text** (Lines 6868-6883):
> Usually peaceful time, enjoy quiet hours at home. Feel amiable ...
    """
    
    original_text: str = """**Source Text** (Lines 6868-6883):
> Usually peaceful time, enjoy quiet hours at home. Feel amiable in quiet way. Relations with parents good. Good time to experience closeness and warmth of family. Redecorating often undertaken—want home elegant or light. Sensitive and in tune with inner feelings. Avoid lavish spending. Fourth house influences digestive tract—may overindulge in food/drink.

**English Paraphrase**: Peaceful time at home. Amiable, good with parents. Family warmth. Redecorating urge. In tune with feelings. Avoid lavish spending. Watch digestive overindulgence.

**Complete Chinese Interpretation**: 在家的平静时光。和蔼可亲，与父母关系好。家庭温暖。重新装修的冲动。与感受协调。避免奢侈消费。注意消化过度放纵。

**Narrative Snippets**:
- `[ns_pit_ve004]` `[trigger: venus_transit_house_4]` `[factor_trigger: astro_transit_venus AND astro_house_4]` `[role: 主干]` Peaceful time at home. Family warmth. Redecorating urge. → PIT Ch7 Venus-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Fourth House (金星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_fourth_house__金星过_001_L1",
    )
    version: str = "1.0.0"
