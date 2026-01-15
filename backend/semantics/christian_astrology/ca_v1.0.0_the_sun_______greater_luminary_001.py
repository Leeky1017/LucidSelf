"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156323
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
    semantic_id="ca_v1.0.0_the_sun_______greater_luminary_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TheSunGreaterLuminary(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 69-71): "The Sun is placed in the middle of all Planets, called ...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 69-71): "The Sun is placed in the middle of all Planets, called the Heart of Heaven, Eye of the World. He is hot, dry, fiery. The Sun signifies kings, rulers, fathers, nobles."

#### English Paraphrase (Primary Language)

**Sun** = **vitality, identity, authority, consciousness**. Heart of Heaven.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (life-giving) |
| Moisture | Dry (defining) |
| Symbolism | Heart of Heaven, Eye of World |
| People | Kings, fathers, nobles |
| Body | Heart, brain, eyes, vital spirit |

#### Complete Chinese Interpretation (Secondary Language)

**太阳** = **生命力、身份、权威、意识**。天之心。热燥火性。象征国王、父亲、贵族。主心脏、大脑、眼睛、生命精气。

**Narrative Snippets**:
- `[ns_lilly_sun_001]` `[trigger: sun_nature]` `[factor_trigger: astro_planet_sun AND astro_vitality_identity AND astro_luminary AND astro_vitality_authority]` `[role: 主干]` The Sun is Heart of Heaven, Eye of World—vitality and authority. → CA I #Sun"""
    normalized_text_zh: str = """"""
    subject: str = "The Sun (☉) - Greater Luminary"
    factor_refs: list = ['luminary', 'vital_spirit']
    
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
        l1_anchor="ca_v1.0.0_the_sun_______greater_luminary_001_L1",
    )
    version: str = "1.0.0"
