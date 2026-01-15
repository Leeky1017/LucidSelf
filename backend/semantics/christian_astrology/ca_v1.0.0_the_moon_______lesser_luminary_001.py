"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156356
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
    semantic_id="ca_v1.0.0_the_moon_______lesser_luminary_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TheMoonLesserLuminary(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 80-83): "The Moon is cold, moist, phlegmatick. She is the swifte...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 80-83): "The Moon is cold, moist, phlegmatick. She is the swiftest of all Planets. The Moon signifies queens, mothers, common people, travelers, fishermen, sailors."

#### English Paraphrase (Primary Language)

**Moon** = **emotions, instincts, change, the public**. Lesser Luminary. Swiftest planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (receptive, reflective) |
| Moisture | Moist (flowing, changeable) |
| Temperament | Phlegmatic |
| People | Queens, mothers, common people, sailors |
| Body | Brain, stomach, breasts, left eye |

#### Complete Chinese Interpretation (Secondary Language)

**月亮** = **情感、本能、变化、公众**。小发光体。最快行星。寒湿粘液质。象征王后、母亲、平民、水手。主大脑、胃、乳房、左眼。

**Narrative Snippets**:
- `[ns_lilly_moon_001]` `[trigger: moon_nature]` `[factor_trigger: astro_planet_moon AND astro_emotions_public]` `[role: 主干]` The Moon is cold, moist, swiftest—emotions, instincts, the public. → CA I #Moon"""
    normalized_text_zh: str = """"""
    subject: str = "The Moon (☽) - Lesser Luminary"
    factor_refs: list = ['moon_luminary', 'temperament_phlegmatic']
    
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
        l1_anchor="ca_v1.0.0_the_moon_______lesser_luminary_001_L1",
    )
    version: str = "1.0.0"
