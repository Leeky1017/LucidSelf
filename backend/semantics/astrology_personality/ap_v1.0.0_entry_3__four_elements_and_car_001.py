"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238139
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
    semantic_id="ap_v1.0.0_entry_3__four_elements_and_car_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3FourElementsAndCar(SemanticEntry):
    """
    **Source Text** (Lines 8235-8316):
> The Meaning and Classification of the Signs of the Zodiac: In a...
    """
    
    original_text: str = """**Source Text** (Lines 8235-8316):
> The Meaning and Classification of the Signs of the Zodiac: In ancient astrology... the equinoxes and solstices served most naturally to effect a division of the zodiac into four great quarters corresponding to the seasons...
>
> Fire (Aries) and Air (Libra) are expressions of momentum; Water (Cancer) and Earth (Capricorn) are expressions of life-qualities, or polarities...
>
> Fire (Aries) is motion toward objective manifestation... the primordial desire for manifestation, the thirst for life in a body: Tanha...
> Air (Libra) is motion toward subjective realization—the yearning for the God-within, the thirst for "Liberation"...

**Key Term Analysis**:
- **Four cardinal signs**: `Aries (spring equinox)` / `Cancer (summer solstice)` / `Libra (fall equinox)` / `Capricorn (winter solstice)`
- **Equinoxes = momentum**: `Fire (Aries) toward objective` / `Air (Libra) toward subjective`
- **Solstices = quality**: `Water (Cancer) purest Yang` / `Earth (Capricorn) purest Yin`
- **Tanha**: `Buddhist term` / `will to live as separate self`

**English Paraphrase (Primary Language)**:
The four cardinal signs mark equinoxes and solstices:
- **Equinoxes (momentum)**: Fire/Aries = motion toward objective manifestation (Tanha); Air/Libra = motion toward subjective realization (Liberation)
- **Solstices (quality)**: Water/Cancer = purest Yang, objective maturity; Earth/Capricorn = purest Yin, subjective maturity (Christ-birth within)

**Complete Chinese Interpretation (Secondary Language)**:
四个本位星座标记分至点：
- **分点（动量）**：火/白羊 = 朝向客观显现的运动（渴爱）；气/天秤 = 朝向主观实现的运动（解脱）
- **至点（品质）**：水/巨蟹 = 最纯阳，客观成熟；土/摩羯 = 最纯阴，主观成熟（内在基督诞生）

**Narrative Snippets**:
- `[ns_aop_169]` `[trigger: four_elements]` `[factor_trigger: astro_elements_four]` `[role: 主干]` Four elements: Fire/Air = momentum (equinoxes); Water/Earth = quality (solstices). → L8277-8286
- `[ns_aop_170]` `[trigger: aries_libra]` `[factor_trigger: astro_cardinal_axis AND astro_cardinal]` `[role: 主干依赖]` Aries = objective manifestation (Tanha); Libra = subjective realization (Liberation). → L8305-8316"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Four Elements and Cardinal Signs"
    factor_refs: list = ['elements_four', 'signs_cardinal']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_3__four_elements_and_car_001_L1",
    )
    version: str = "1.0.0"
