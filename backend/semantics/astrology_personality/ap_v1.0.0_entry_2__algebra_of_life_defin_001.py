"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237711
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
    semantic_id="ap_v1.0.0_entry_2__algebra_of_life_defin_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2AlgebraOfLifeDefin(SemanticEntry):
    """
    **Source Text** (Lines 1731-1757):
> The word "algebra" comes from an Arabian word "al-jebr" which m...
    """
    
    original_text: str = """**Source Text** (Lines 1731-1757):
> The word "algebra" comes from an Arabian word "al-jebr" which means: the reduction of parts to a whole. The word "jabara," from which it is derived signifies: to bind together (Webster). Algebra has therefore as its basic function the binding together, or correlating, or integrating of elements into a formulated whole...
>
> Two important points stand out in such a definition. First, mathematics is seen as a "science of pure correlation" (Bertrand Russell). Second, what it correlates are "quantities or magnitudes and operations." Algebra is a branch of mathematics, but besides correlating quantities it also deals with a category of conventional symbols which can be made to represent any element considered or the relations between any groups of elements.
>
> According to our conception, astrology is a kind of algebra, inasmuch as it deals with symbolic elements (planets, stars, segments of geocentric space, astrological Parts, Nodes, progressed positions, etc.) which it "binds together" into a formula describing a living whole: the native. However, these symbolic elements do not belong to the realm of quantity. They represent, on the contrary, universal life-qualities. Astrology is thus a kind of algebra of qualities; and these qualities are not mere sensorial qualities (such as white, blue, thick, heavy, painful, etc.), but qualities which refer to... psychological and super-psychological planes.

**Key Term Analysis**:
- **Al-jebr etymology**: `reduction of parts to whole` / `jabara = bind together` / `Arabic origin`
- **Algebra's function**: `correlating` / `integrating` / `formulated whole`
- **Science of pure correlation**: `Bertrand Russell` / `no content, only relations` / `mathematical essence`
- **Algebra of qualities**: `not quantities` / `universal life-qualities` / `Rudhyar's innovation`
- **Symbolic elements**: `planets, stars, Parts, Nodes` / `bound together` / `describing native`
- **Psychological/super-psychological**: `not sensorial` / `inner nature` / `life-processes`

**English Paraphrase (Primary Language)**:
Rudhyar elaborates the "algebra of life" definition. Algebra (from Arabic "al-jebr") means "reduction of parts to a whole" or "binding together." Mathematics is a "science of pure correlation" (Russell)—it correlates quantities and operations through conventional symbols.

Astrology parallels this: it binds symbolic elements (planets, signs, houses, aspects, Parts, Nodes) into a formula describing a living whole—the native. The critical difference: astrology deals with qualities, not quantities. Mathematical algebra correlates numbers; astrological algebra correlates "universal life-qualities."

These qualities are not sensorial (colors, textures) but psychological and super-psychological—referring to inner processes, life-meanings, archetypal functions. This is Rudhyar's philosophical innovation: positioning astrology as a qualitative formal system that integrates the person's life-pattern into meaningful order.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar详细阐述了"生命的代数"定义。代数（来自阿拉伯语"al-jebr"）意为"将部分还原为整体"或"绑定在一起"。数学是"纯相关的科学"（Russell）——它通过常规符号关联数量和运算。

占星学与此平行：它将符号元素（行星、星座、宫位、相位、阿拉伯点、交点）绑定为描述活生生整体——命主——的公式。关键区别：占星学处理的是质而非量。数学代数关联数字；占星代数关联"普遍生命品质"。

这些品质不是感官的（颜色、质地）而是心理和超心理的——指向内在过程、生命意义、原型功能。这是Rudhyar的哲学创新：将占星学定位为一种质性形式系统，将人的生命模式整合为有意义的秩序。

**Core Points**:
- Al-jebr = "reduction of parts to whole," "binding together"
- Mathematics = science of pure correlation (Russell)
- Algebra correlates through conventional symbols
- Astrology = algebra binding symbolic elements into formula
- Describes living whole: the native
- Critical difference: qualities not quantities
- Universal life-qualities, not sensorial
- Psychological and super-psychological planes
- Rudhyar's innovation: qualitative formal system

**Narrative Snippets**:
- `[ns_aop_061]` `[trigger: al_jebr_etymology]` `[factor_trigger: astro_al_jebr AND astro_aljebr_struct]` `[role: 主干]` Al-jebr means "reduction of parts to whole," jabara = "bind together"—algebra's basic function is integrating elements into formulated whole. → Source Text L1731-1735
- `[ns_aop_062]` `[trigger: pure_correlation]` `[factor_trigger: astro_pure_correlation AND astro_pure_corr]` `[role: 主干依赖]` Mathematics is "science of pure correlation" (Russell)—algebra correlates through conventional symbols representing any elements. → Source Text L1741-1746
- `[ns_aop_063]` `[trigger: qualities_not_quantities]` `[factor_trigger: astro_qualities AND astro_quality_alg]` `[role: 条件分支]` Astrology's symbolic elements don't belong to quantity realm—represent universal life-qualities. → Source Text L1750-1754
- `[ns_aop_064]` `[trigger: psychological_qualities]` `[factor_trigger: astro_psych_qualities AND astro_life_qual_domain]` `[role: 总结]` These qualities are psychological and super-psychological, not mere sensorial—refer to inner life-processes. → Source Text L1754-1757

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: "Algebra of qualities" is Rudhyar's distinctive contribution, distinguishing his approach from both fortune-telling and purely psychological astrology. It grounds astrology in formal, not causal, relations.
- **中文**: "质的代数"是Rudhyar的独特贡献，使其方法与算命和纯心理占星学都区分开来。它将占星学建立在形式关系而非因果关系上。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Algebra of Life—Definition and Qualities"
    factor_refs: list = ['astro_al_jebr_func', 'astro_pure_correlation', 'astro_quality_algebra', 'astro_life_qualities']
    
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
        l1_anchor="ap_v1.0.0_entry_2__algebra_of_life_defin_001_L1",
    )
    version: str = "1.0.0"
