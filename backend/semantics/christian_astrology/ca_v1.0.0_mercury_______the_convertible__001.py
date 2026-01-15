"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156346
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
    semantic_id="ca_v1.0.0_mercury_______the_convertible__001",
    book_id="christian_astrology",
    engine_id="astro"
)
class MercuryTheConvertible(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 76-79): "Mercury is the least of all Planets. He is convertible:...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 76-79): "Mercury is the least of all Planets. He is convertible: with good Planets good, with evil Planets evil. Mercury signifies ambassadors, secretaries, astrologers, merchants, mathematicians, poets."

#### English Paraphrase (Primary Language)

**Mercury** = **communication, intellect, commerce, adaptability**. Neutral/convertible.

| Attribute | Value |
|-----------|-------|
| Nature | Variable (takes on aspect partners' nature) |
| Temperament | Mixed |
| People | Secretaries, merchants, astrologers, poets |
| Body | Brain, tongue, hands, nerves |

#### Complete Chinese Interpretation (Secondary Language)

**水星** = **沟通、智识、商业、适应性**。中性/可转换。性质可变（随相位伙伴性质）。象征秘书、商人、占星师、诗人。主大脑、舌头、双手、神经系统。

**Narrative Snippets**:
- `[ns_lilly_merc_001]` `[trigger: mercury_nature]` `[factor_trigger: astro_planet_mercury AND astro_communication_intellect]` `[role: 主干]` Mercury is convertible—good with benefics, evil with malefics. → CA I #Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury (☿) - The Convertible One"
    factor_refs: list = ['mercury_convertible', 'neutral_planet']
    
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
        l1_anchor="ca_v1.0.0_mercury_______the_convertible__001_L1",
    )
    version: str = "1.0.0"
