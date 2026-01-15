"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162895
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
    semantic_id="tb_v1.0.0_signification_of_meteors__chap_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class SignificationOfMeteorsChap(SemanticEntry):
    """
    **Source Text**:
> The signification of meteors, such as comets, shooting stars, and atmospheric phe...
    """
    
    original_text: str = """**Source Text**:
> The signification of meteors, such as comets, shooting stars, and atmospheric phenomena... comets indicate wars, hot and dry weather, mortality; their nature depends on their color and the sign in which they appear.

**English Paraphrase (Primary Language)**:
**Meteors and comets** serve as supplementary mundane indicators:
- **Comets**: Indicate wars, drought, mortality; nature depends on color (red=Mars, yellow=Saturn) and appearing sign
- **Shooting stars**: Indicate winds from the direction they travel
- **Halos, rainbows**: Indicate moisture or temperature changes

These phenomena modify or intensify eclipse-based predictions.

**Complete Chinese Interpretation (Secondary Language)**:
**流星和彗星**作为补充的世俗指示器：彗星指示战争、干旱、死亡；性质取决于颜色（红色=火星，黄色=土星）和出现的星座。流星指示从其移动方向来的风。光环、彩虹指示湿度或温度变化。

**Core Points**:
- Comets = wars, drought, mortality
- Comet nature from color and sign
- Shooting stars indicate wind direction
- Halos/rainbows indicate moisture changes

**Narrative Snippets**:
- `[ns_tetra_ii010]` `[trigger: meteors_comets]` `[factor_trigger: astro_comet_mundane]` `[role: 条件分支]` Comets indicate wars, drought, and mortality; their nature depends on color and appearing sign. → Source Text II.14
- `[ns_tetra_ii_me]` `[trigger: mundane_event]` `[factor_trigger: mundane_event]` `[role: 效果]` Mundane events indicated by comets and meteors: wars, drought, mortality, winds—supplementing eclipse predictions. → Source Text II.14"""
    normalized_text_zh: str = """"""
    subject: str = "Signification of Meteors (Chapter XIV)"
    factor_refs: list = ['comet_mundane']
    
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
        l1_anchor="tb_v1.0.0_signification_of_meteors__chap_001_L1",
    )
    version: str = "1.0.0"
