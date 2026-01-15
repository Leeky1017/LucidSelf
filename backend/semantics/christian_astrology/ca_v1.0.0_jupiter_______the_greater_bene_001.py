"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156298
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
    semantic_id="ca_v1.0.0_jupiter_______the_greater_bene_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class JupiterTheGreaterBene(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 61-64): "Jupiter is placed betwixt Saturn and Mars, the greatest...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 61-64): "Jupiter is placed betwixt Saturn and Mars, the greatest of all Planets in body. He is hot, moist, sanguine. Jupiter signifies religious men, judges, counsellors, senators, bishops, priests, lawyers."

#### English Paraphrase (Primary Language)

**Jupiter** = **expansion, wisdom, fortune, growth**. 12-year orbit.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (expands, warms) |
| Moisture | Moist (connects, nurtures) |
| Temperament | Sanguine |
| People | Judges, priests, lawyers, scholars |
| Body | Liver, arteries, lungs |

#### Complete Chinese Interpretation (Secondary Language)

**木星** = **扩张、智慧、好运、成长**。12年轨道。热湿多血质。象征法官、神父、律师、学者。主肝脏、动脉、肺。

**Narrative Snippets**:
- `[ns_lilly_jup_001]` `[trigger: jupiter_nature]` `[factor_trigger: astro_planet_jupiter AND astro_fortune_expansion AND astro_benefic]` `[role: 主干]` Jupiter is hot, moist, sanguine—Greater Benefic of expansion and fortune. → CA I #Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter (♃) - The Greater Benefic"
    factor_refs: list = ['jupiter_benefic', 'temperament_sanguine']
    
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
        l1_anchor="ca_v1.0.0_jupiter_______the_greater_bene_001_L1",
    )
    version: str = "1.0.0"
