"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238246
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
    semantic_id="ap_v1.0.0_entry_4__general_theory_of_ast_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4GeneralTheoryOfAst(SemanticEntry):
    """
    **Source Text** (Lines 10400-10478):
> The General Theory of Astrological "Parts": The "Ascendants" ...
    """
    
    original_text: str = """**Source Text** (Lines 10400-10478):
> The General Theory of Astrological "Parts": The "Ascendants" of the planets are determined by calculating the "arcs" (or differences of longitude) between the Sun and the planets, and by adding the value of these arcs to the longitude of the actual Ascendant...
>
> A Part is the distance between two planets, referred for its significance to the Ascendant. The Ascendant is the point of individual awareness...
>
> The astrology of Parts is indeed a kind of "group-algebra" working out nearly endless correlations and permutations between the original elements of the birth-formula.

**Key Term Analysis**:
- **Parts theory**: `distance between two planets` / `referred to Ascendant` / `individual awareness point`
- **Arc calculation**: `longitude difference` / `added to Ascendant`
- **Eight possible points**: `two directions (clockwise/counter)` / `four angles (ASC/MC/DSC/IC)`
- **Parts as algebra**: `correlations, permutations` / `infinite complexity` / `nerve tracts analogy`

**English Paraphrase (Primary Language)**:
Parts = "distance between two planets, referred to the Ascendant" (point of individual awareness).

For each planet pair: distance can be measured in two directions, and referred to four angles = 8 possible points per pair.

"The astrology of Parts is indeed a kind of 'group-algebra' working out nearly endless correlations and permutations." It approximates "the infinite variety of life-connections" like nerve tracts in the body.

**Complete Chinese Interpretation (Secondary Language)**:
Parts = "两颗行星之间的距离，参照上升点"（个体意识点）。

对于每对行星：距离可以在两个方向上测量，并参照四个角度 = 每对8个可能的点。

"Parts的占星学确实是一种'群代数'，计算出原始出生公式元素之间几乎无穷无尽的相关性和排列组合。"它近似于"生命连接的无限多样性"，如身体中的神经束。

**Narrative Snippets**:
- `[ns_aop_193]` `[trigger: parts_theory]` `[factor_trigger: astro_parts_general AND astro_parts]` `[role: 主干]` Parts = distance between planets referred to Ascendant; point of individual awareness. → L10423-10432
- `[ns_aop_194]` `[trigger: parts_algebra]` `[factor_trigger: astro_parts_complexity]` `[role: 总结]` Parts as "group-algebra": 8 points per pair, nearly endless correlations of birth-formula. → L10464-10478"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: General Theory of Astrological Parts"
    factor_refs: list = ['parts_theory', 'part_imaging']
    
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
        l1_anchor="ap_v1.0.0_entry_4__general_theory_of_ast_001_L1",
    )
    version: str = "1.0.0"
