"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238032
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
    semantic_id="ap_v1.0.0_entry_2__astrology_of_the_indi_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2AstrologyOfTheIndi(SemanticEntry):
    """
    **Source Text** (Lines 6632-6687):
> 1. ASTROLOGY OF THE INDIVIDUAL: This includes especially the as...
    """
    
    original_text: str = """**Source Text** (Lines 6632-6687):
> 1. ASTROLOGY OF THE INDIVIDUAL: This includes especially the astrology of the individual human being (natal astrology) and the astrology of the individual situation (horary astrology)...
>
> "Natal astrology," in the strictest sense of the term, refers to individual birth-moments. It demands as a prerequisite absolute accuracy in the knowledge of the moment of the "first breath"...
>
> Such a true natal astrology is therefore based essentially on psychological understanding. It deals with subjective interpretation of objective facts. It is a system of creative life-interpretation and creative symbolism applied to an individual personality.

**Key Term Analysis**:
- **Natal astrology**: `individual birth-moments` / `first breath accuracy required` / `house framework = individual selfhood`
- **Horary astrology**: `individual situation` / `chart for question time` / `personal equation of astrologer`
- **Psychological basis**: `subjective interpretation of objective facts` / `creative life-interpretation`

**English Paraphrase (Primary Language)**:
**Astrology of the Individual** includes natal (individual birth) and horary (individual situation). Natal astrology requires precise "first breath" time to establish the house framework—"the very frame-work of the native's individual selfhood and unique destiny."

True natal astrology is "based essentially on psychological understanding... a system of creative life-interpretation and creative symbolism applied to an individual personality."

**Complete Chinese Interpretation (Secondary Language)**:
**个体占星学**包括本命（个体出生）和卜卦（个体情境）。本命占星需要精确的"第一口呼吸"时间来建立宫位框架——"命主个体自性和独特命运的框架本身。"

真正的本命占星"本质上基于心理学理解……一个应用于个体人格的创造性生命诠释和创造性符号学系统。"

**Narrative Snippets**:
- `[ns_aop_147]` `[trigger: natal_astrology]` `[factor_trigger: astro_natal AND astro_horary_func AND astro_natal_func]` `[role: 主干]` Natal astrology: individual birth, first breath, house framework = individual selfhood. → L6657-6674
- `[ns_aop_148]` `[trigger: psychological_basis]` `[factor_trigger: astro_psychological]` `[role: 总结]` True natal astrology based on psychological understanding, creative life-interpretation. → L6676-6687"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Astrology of the Individual—Natal and Horary"
    factor_refs: list = ['astro_natal', 'astro_horary']
    
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
        l1_anchor="ap_v1.0.0_entry_2__astrology_of_the_indi_001_L1",
    )
    version: str = "1.0.0"
