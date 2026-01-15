"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152280
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
    semantic_id="ca_v1.0.0_physical_constitution_and_mann_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class PhysicalConstitutionAndMann(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 532-548): "Of the Complexion, temperament of the body, quality...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 532-548): "Of the Complexion, temperament of the body, quality of Planets and Signs. The Ascendant, its Lord, the Moon, and planets in the 1st house describe the body. For manners, consider Mercury, Moon, and the Lord of the Geniture."

#### English Paraphrase (Primary Language)

**Physical Appearance** determined by:
1. **Ascendant sign** (primary body type)
2. **Lord of Ascendant** (modifying factors)
3. **Planets in 1st house** (strong physical influence)
4. **Moon** (general constitution)

**Mental Qualities and Manners** determined by:
1. **Mercury** (intellect, speech, reasoning)
2. **Moon** (emotions, habits, instincts)
3. **Lord of Geniture** (overall character tone)

**Lord of Geniture** = the strongest planet in the chart by:
- Essential dignity
- Angular position
- Aspects from other planets
- Being almuten (most dignities at key points)

#### Complete Chinese Interpretation (Secondary Language)

**外貌**由以下因素决定：1. 上升星座（主要体型）；2. 上升守护星（修正因素）；3. 第一宫行星（强烈身体影响）；4. 月亮（整体体质）。**心理品质与性情**由以下因素决定：1. 水星（智力、言语、推理）；2. 月亮（情感、习惯、本能）；3. 命宫主星（整体性格基调）。**命宫主星**=星盘中最强的行星，通过：本质尊贵、角宫位置、其他行星相位、成为全能星（在关键点有最多尊贵）来判断。

**Narrative Snippets**:
- `[ns_lilly_temp_001]` `[trigger: appearance]` `[factor_trigger: astro_physical_appearance]` `[role: 主干]` Ascendant and its Lord describe the body; planets in 1st house strongly modify appearance. → CA III #Temperament
- `[ns_lilly_temp_002]` `[trigger: manners]` `[factor_trigger: astro_mental_character]` `[role: 主干依赖]` Mercury and Moon together describe the native's mental qualities and habitual behaviors. → CA III #Temperament
- `[ns_lilly_temp_003]` `[trigger: asc_sign]` `[factor_trigger: astro_ascendant_sign]` `[role: 主干依赖]` Ascendant sign determines primary body type and physical constitution. → English Paraphrase
- `[ns_lilly_temp_004]` `[trigger: asc_lord]` `[factor_trigger: astro_asc_lord]` `[role: 条件分支]` Lord of Ascendant modifies and refines physical appearance indications. → English Paraphrase
- `[ns_lilly_temp_005]` `[trigger: mercury_mind]` `[factor_trigger: astro_mercury]` `[role: 主干依赖]` Mercury signifies intellect, speech, and reasoning capacity. → English Paraphrase
- `[ns_lilly_temp_006]` `[trigger: moon_mind]` `[factor_trigger: astro_moon]` `[role: 条件分支]` Moon signifies emotions, habits, and instinctive behaviors. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Physical Constitution and Manners"
    factor_refs: list = ['lord_of_geniture', 'almuten', 'temperament']
    
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
        l1_anchor="ca_v1.0.0_physical_constitution_and_mann_001_L1",
    )
    version: str = "1.0.0"
