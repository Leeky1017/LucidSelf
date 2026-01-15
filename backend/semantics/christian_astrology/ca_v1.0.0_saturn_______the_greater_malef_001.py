"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156284
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
    semantic_id="ca_v1.0.0_saturn_______the_greater_malef_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class SaturnTheGreaterMalef(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 57-60): "Saturn is the supremest of all Planets; is placed betwi...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 57-60): "Saturn is the supremest of all Planets; is placed betwixt Jupiter and the Firmament. He is cold, dry, earthy, melancholy. Saturn governs old men, grandfathers, monks, husbandmen, miners, day laborers."

#### English Paraphrase (Primary Language)

**Saturn** = **limitation, structure, time, maturation**. 30-year orbit = slowest planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Cold (contracts, restricts) |
| Moisture | Dry (hardens, isolates) |
| Temperament | Melancholic |
| People | Old men, monks, farmers, miners |
| Body | Bones, teeth, knees, spleen |

#### Complete Chinese Interpretation (Secondary Language)

**土星** = **限制、结构、时间、成熟**。30年轨道周期=最慢行星。寒燥忧郁质。象征老人、僧侣、农夫、矿工。主骨骼、牙齿、膝盖、脾脏。

**Narrative Snippets**:
- `[ns_lilly_sat_001]` `[trigger: saturn_nature]` `[factor_trigger: astro_planet_saturn AND astro_limitation_delay AND astro_limitation_structure]` `[role: 主干]` Saturn is cold, dry, melancholy—Greater Malefic of limitation and time. → CA I #Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn (♄) - The Greater Malefic"
    factor_refs: list = ['saturn_malefic', 'temperament_melancholy']
    
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
        l1_anchor="ca_v1.0.0_saturn_______the_greater_malef_001_L1",
    )
    version: str = "1.0.0"
