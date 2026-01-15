"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162853
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
    semantic_id="tb_v1.0.0_the_new_moon_of_the_year__chap_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheNewMoonOfTheYearChap(SemanticEntry):
    """
    **Source Text**:
> The new moon which immediately precedes the Sun's entrance into Aries is particul...
    """
    
    original_text: str = """**Source Text**:
> The new moon which immediately precedes the Sun's entrance into Aries is particularly to be observed... for from it may be prognosticated the general atmospheric constitution of the whole year.

**English Paraphrase (Primary Language)**:
The **Aries ingress** (Sun entering Aries at vernal equinox) and the **preceding new moon** are used to forecast the year's general weather. The planetary configurations at this lunation indicate the atmospheric conditions for the coming year—temperature, moisture, winds, storms.

**Complete Chinese Interpretation (Secondary Language)**:
**白羊座入境**（太阳在春分进入白羊座）和**之前的新月**用于预测全年的一般天气。此朔望的行星配置指示来年的大气条件——温度、湿度、风、暴风雨。

**Core Points**:
- New moon before Aries ingress = year's weather indicator
- Sun's Aries entry marks the astrological new year
- Planetary configurations indicate temperature, moisture, winds

**Narrative Snippets**:
- `[ns_tetra_ii008]` `[trigger: aries_ingress]` `[factor_trigger: astro_sun_ingress_aries]` `[role: 主干]` The new moon preceding Sun's Aries entry indicates the year's general atmospheric constitution. → Source Text II.11"""
    normalized_text_zh: str = """"""
    subject: str = "The New Moon of the Year (Chapter XI)"
    factor_refs: list = ['aries_ingress']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_the_new_moon_of_the_year__chap_001_L1",
    )
    version: str = "1.0.0"
