"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238237
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
    semantic_id="ap_v1.0.0_entry_3__part_of_fortune___moo_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3PartOfFortuneMoo(SemanticEntry):
    """
    **Source Text** (Lines 10262-10398):
> The "Ascendants" of Planets: This often confusing subject... ...
    """
    
    original_text: str = """**Source Text** (Lines 10262-10398):
> The "Ascendants" of Planets: This often confusing subject... can be readily understood if we re-state in a slightly different manner ideas often repeated in this book...
>
> This point has been used for a long time in astrology under the name Pars Fortuna: the Part of Fortune. It is found by adding the longitudes of Ascendant and Moon, and subtracting from the sum the longitude of the Sun...
>
> The Part of Fortune represents a man's congenital activity, as a merely conscious ego—and discounting all his deeper intuitions and unconscious or super-conscious motives.

**Key Term Analysis**:
- **Ascendant of Moon**: `Part of Fortune` / `Pars Fortuna` / `ASC + Moon - Sun`
- **Part of Fortune meaning**: `congenital activity as conscious ego` / `spontaneous personal reactions` / `happiness, wealth`
- **Sun-Ascendant relation**: `Sun = integrating force` / `Ascendant = unique individual expression`
- **Medieval interpretation**: `wealth` / `happiness` / `best self-expression`

**English Paraphrase (Primary Language)**:
Part of Fortune = "Ascendant of the Moon" = ASC + Moon - Sun.

It represents "congenital activity as a merely conscious ego, discounting deeper intuitions and unconscious motives." Shows "that department of life in which the native expresses himself to best advantage."

Medieval meaning: wealth, happiness. Modern: spontaneous personal reactions, social cooperation.

**Complete Chinese Interpretation (Secondary Language)**:
福点 = "月亮的上升点" = ASC + 月亮 - 太阳。

它代表"仅作为意识自我的先天活动，不考虑更深层的直觉和无意识动机。"显示"原住民最能发挥优势表达自己的生活领域。"

中世纪意义：财富、幸福。现代：自发的个人反应、社会合作。

**Narrative Snippets**:
- `[ns_aop_191]` `[trigger: part_fortune]` `[factor_trigger: astro_pars_fortuna AND astro_part_fortune]` `[role: 主干]` Part of Fortune = ASC + Moon - Sun; congenital activity as conscious ego. → L10351-10366
- `[ns_aop_192]` `[trigger: fortune_meaning]` `[factor_trigger: astro_fortune_interpretation]` `[role: 总结]` Part of Fortune: best self-expression, happiness, spontaneous personal reactions. → L10368-10386"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Part of Fortune - Moon's Ascendant"
    factor_refs: list = ['part_fortune', 'pars_fortuna']
    
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
        l1_anchor="ap_v1.0.0_entry_3__part_of_fortune___moo_001_L1",
    )
    version: str = "1.0.0"
