"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333672
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
    semantic_id="ah_v1.0.0_monotheistic_vs_pantheistic_co_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class MonotheisticVsPantheisticCo(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Monotheistic | Sun as on...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Monotheistic | Sun as one God | Tropical basis |
| Pantheistic | Multiple hierarchies | Sidereal basis |
| Soul Avenues | Twelve paths | Individual journey |
| Theological Foundation | Cosmology choice | Deeper meaning |

#### Source Text

"In the monotheistic framework, the Sun represents the one God, and Earth's orbit defines twelve soul avenues through which the individual relates to divine unity. In the pantheistic framework, the twelve constellations represent multiple creative hierarchies, and the Sun serves merely as a lens or window through which galactic energies reach Earth. This is a fundamental philosophical and theological difference underlying the sidereal-tropical debate."

#### English Paraphrase (Primary Language)

The zodiac debate ultimately rests on theological foundations. Monotheistic astrology treats the Sun as singular divine source, with Earth's orbital cycle defining twelve archetypal modes of relating to this one divinity—twelve "soul avenues" for individual spiritual development. Pantheistic astrology treats the twelve constellations as multiple cosmic hierarchies, each channeling distinct galactic energies, with the Sun functioning as intermediary lens rather than source—the true power resides in the stellar collectives. These represent fundamentally incompatible cosmologies: one sees reality as dialogue between individual soul and unified divine source; the other sees reality as complex weaving of multiple divine powers accessed through celestial hierarchies.

#### Complete Chinese Interpretation (Secondary Language)

**一神论宇宙观**(Monotheistic)视太阳为唯一神圣源头，十二星座代表灵魂发展的十二条道路，通过太阳的独一神性显化。这支持回归星座系统，因为太阳季节节奏(春分/夏至/秋分/冬至)定义十二分。**泛神论宇宙观**(Pantheistic)视十二星群为独立的神性层级或创造性等级，从银河中心向下层叠能量。太阳只是透镜或传递中介，不是唯一源头。这支持恒星星座系统，因为实际星群配置才是能量源。Rudhyar倾向一神论/回归系统，认为它更适合现代个体化意识——个人与神圣的直接关系(通过太阳)，而非通过多层宇宙等级。这是深刻的灵性哲学选择，非仅技术问题。

#### Core Points

- **Monotheistic**: Sun = one God, twelve soul avenues, individual-divine dialogue
- **Pantheistic**: Twelve constellations = divine hierarchies, Sun = lens only
- **Theological foundation**: Underlying sidereal-tropical choice
- **Individual vs collective**: Personal soul path vs cosmic hierarchy participation

#### Narrative Snippets

- `[ns_rudhyar_theology_001]` `[trigger: monotheistic_astrology]` `[factor_trigger: House_Philosophy_12H_7 AND individuality]` `[role: 主干]` Monotheistic astrology treats the Sun as singular divine source, with twelve signs representing twelve "soul avenues" for individual spiritual development in dialogue with one divinity. → The Astrological Houses Theology
- `[ns_rudhyar_theology_002]` `[trigger: pantheistic_astrology]` `[factor_trigger: transformation AND other_selves]` `[role: 主干依赖]` Pantheistic astrology treats twelve constellations as multiple cosmic hierarchies, each channeling distinct galactic energies, with Sun functioning as intermediary lens rather than source. → The Astrological Houses Theology
- `[ns_rudhyar_theology_003]` `[trigger: cosmology_choice]` `[factor_trigger: partnership AND inadequacy]` `[role: 总结]` These represent fundamentally incompatible cosmologies: individual soul-divine dialogue (monotheistic/tropical) vs complex weaving of multiple divine powers through stellar hierarchies (pantheistic/sidereal). → The Astrological Houses Theology"""
    normalized_text_zh: str = """"""
    subject: str = "Monotheistic vs Pantheistic Cosmology"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_monotheistic_vs_pantheistic_co_001_L1",
    )
    version: str = "1.0.0"
