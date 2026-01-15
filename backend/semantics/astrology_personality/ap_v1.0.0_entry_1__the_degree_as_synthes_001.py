"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238255
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
    semantic_id="ap_v1.0.0_entry_1__the_degree_as_synthes_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1TheDegreeAsSynthes(SemanticEntry):
    """
    **Source Text** (Lines 10500-10556):
> Degrees of the Zodiac and the "Sabian" Symbols: The Degree is...
    """
    
    original_text: str = """**Source Text** (Lines 10500-10556):
> Degrees of the Zodiac and the "Sabian" Symbols: The Degree is not merely a subdivision of the zodiacal sign, or of the whole zodiac. It stands, as an astrological element, alone and in a position of supreme (though little understood) significance...
>
> For in the Degree come to a point of synthesis the two motions of the Earth—and, symbolically, the two great principles of all life: collective and individual, universal and particular. In the Degree we witness the operation of the creative within an individual personality, or a particular situation.

**Key Term Analysis**:
- **Degree significance**: `not mere subdivision` / `supreme significance` / `most mysterious element`
- **Two motions synthesis**: `orbital (collective)` + `axial (individual)` = `Degree`
- **Day as cycle**: `waking to sleep` / `conscious to unconscious` / `integration function`
- **Creative operation**: `reconciles opposites` / `meaning revealed through symbols`

**English Paraphrase (Primary Language)**:
The Degree = "most mysterious element in astrology," NOT merely subdivision but synthesis of Earth's two motions:
- **Orbital** (collective, universal)
- **Axial** (individual, particular)

"In the Degree we witness the operation of the creative within an individual personality." The Degree = space covered in orbital motion during one complete axial rotation. "Here 'meaning' stands revealed—for whosoever knows how to read symbols."

**Complete Chinese Interpretation (Secondary Language)**:
度数 = "占星学中最神秘的元素"，不仅仅是细分，而是地球两种运动的综合：
- **轨道运动**（集体、普遍）
- **轴向运动**（个体、特殊）

"在度数中，我们见证创造性在个体人格中的运作。"度数 = 在一次完整轴向旋转期间轨道运动覆盖的空间。"在这里，'意义'显现——对于知道如何阅读符号的人。"

**Narrative Snippets**:
- `[ns_aop_195]` `[trigger: degree_synthesis]` `[factor_trigger: astro_degree_nature AND astro_degree]` `[role: 主干]` Degree = synthesis of orbital (collective) + axial (individual); most mysterious element. → L10504-10529
- `[ns_aop_196]` `[trigger: degree_creative]` `[factor_trigger: astro_degree_meaning AND astro_degree AND astro_sabian]` `[role: 总结]` Degree = creative operation within personality; meaning revealed through symbols. → L10531-10548"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: The Degree as Synthesis of Two Motions"
    factor_refs: list = ['degree_zodiac', 'sabian_symbols']
    
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
        l1_anchor="ap_v1.0.0_entry_1__the_degree_as_synthes_001_L1",
    )
    version: str = "1.0.0"
