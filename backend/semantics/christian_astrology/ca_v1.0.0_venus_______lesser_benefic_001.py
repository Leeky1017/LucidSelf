"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156334
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
    semantic_id="ca_v1.0.0_venus_______lesser_benefic_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class VenusLesserBenefic(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 72-75): "Venus is cold, moist, the lesser fortune. She is phlegm...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 72-75): "Venus is cold, moist, the lesser fortune. She is phlegmatick, temperate. Venus signifies women, mothers, musicians, painters, jewelers, lovers."

#### English Paraphrase (Primary Language)

**Venus** = **love, beauty, harmony, pleasure**. Lesser Benefic.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (receptive) |
| Moisture | Moist (connecting) |
| Temperament | Phlegmatic |
| People | Women, musicians, lovers, artists |
| Body | Throat, kidneys, veins, reproductive |

#### Complete Chinese Interpretation (Secondary Language)

**金星** = **爱、美、和谐、愉悦**。小吉星。寒湿粘液质。象征女性、音乐家、恋人、艺术家。主咽喉、肾脏、静脉、生殖系统。

**Narrative Snippets**:
- `[ns_lilly_venus_001]` `[trigger: venus_nature]` `[factor_trigger: astro_planet_venus AND astro_love_beauty]` `[role: 主干]` Venus is cold, moist—Lesser Benefic of love, beauty, harmony. → CA I #Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus (♀) - Lesser Benefic"
    factor_refs: list = ['venus_benefic', 'temperament_phlegmatic']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_venus_______lesser_benefic_001_L1",
    )
    version: str = "1.0.0"
