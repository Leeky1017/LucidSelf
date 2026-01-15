"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237698
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
    semantic_id="ap_v1.0.0_entry_1__three_epochs_of_thoug_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1ThreeEpochsOfThoug(SemanticEntry):
    """
    **Source Text** (Lines 1560-1729):
> Can Astrology Ever Become an Empirical Science? Astrology, the ...
    """
    
    original_text: str = """**Source Text** (Lines 1560-1729):
> Can Astrology Ever Become an Empirical Science? Astrology, the algebra of life. Such a statement demands explanation...
>
> [Sir James Jeans in The New Background of Science:] "Reviewing the history of man's efforts to understand the workings of the external world, we may distinguish three broad epochs, the nature of which may be suggested by the words animistic, mechanical and mathematical...
>
> "The animistic period was characterized by the error of supposing that the course of nature was governed by the whims and passions of living beings more or less like man himself...
>
> "It was not until the time of Galileo that science turned from cosmology to mechanics... Pieces of matter were supposed to exert 'forces' on one another...
>
> "Mechanism, with its implications, has dropped out of the scheme of science... We are beginning to see that man had freed himself from the anthropomorphic error of imagining that the workings of nature could be compared to those of his own whims and caprices (animism), only to fall headlong into the second anthropomorphic error of imagining that they could be compared to the workings of his own muscles, and sinews (mechanism)."
>
> It is easy to see how the three stages of knowledge which Jeans mentions (animistic, mechanical and mathematical) correspond to the three stages of astrological thought discussed in our preceding chapter. The "mechanism" of science is not basically different from the "vitalism" of astrology; the "push and pull" of the former corresponds in terms of material activity to the "yang and yin" principles of vital operations.
>
> The third stage of thought is called by Jeans "mathematical." The main feature of it is that pure mathematical speculation is seen to fit perfectly the results of ever more complex and refined experiments; in fact it often precedes experiments...
>
> This distinction is capital. For by defining astrology as the algebra of life, we place it in the category of mathematical thought—and not in that of empirical sciences.

**Key Term Analysis**:
- **Three epochs (Jeans)**: `animistic → mechanical → mathematical` / `science's evolution` / `parallels astrology`
- **Animistic error**: `whims and passions` / `personifying nature` / `anthropomorphic`
- **Mechanical error**: `push and pull` / `muscular projection` / `second anthropomorphism`
- **Mathematical stage**: `pure thought fits nature` / `symbolic relations` / `ordering complexity`
- **Mechanism = Vitalism parallel**: `push/pull = yang/yin` / `tangible dualism` / `force-based`
- **Astrology as mathematical**: `not empirical science` / `category distinction` / `form vs content`

**English Paraphrase (Primary Language)**:
Rudhyar opens Chapter 1 by citing Sir James Jeans's three epochs of scientific thought: animistic (personifying nature), mechanical (push-and-pull forces), and mathematical (pure relational thought). He demonstrates a striking parallel with astrological evolution: animistic, vitalistic, algebraic.

The crucial insight: mechanism and vitalism are structurally equivalent—both involve tangible dualism (push/pull, yang/yin). Both represent anthropomorphic projection (onto muscles and sinews, or onto reproductive polarity). The mathematical stage transcends both by recognizing that pure relational symbols can order the complexity of phenomena without projecting human characteristics.

This leads to Rudhyar's fundamental claim: by defining astrology as "the algebra of life," he places it in the category of mathematical thought—not empirical science. Astrology provides form, not content; it integrates, not predicts through causal mechanism. This distinction is "capital"—it changes everything about how astrology should be understood and practiced.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar在第一章开头引用Sir James Jeans的科学思想三阶段：泛灵论（人格化自然）、机械论（推拉力量）、数学论（纯关系思维）。他展示了与占星学演变的惊人平行：泛灵论、生机论、代数论。

关键洞见：机械论与生机论在结构上是等价的——两者都涉及有形的二元（推/拉、阴/阳）。两者都代表拟人投射（到肌肉和肌腱，或到生殖极性）。数学阶段通过承认纯关系符号可以在不投射人类特征的情况下排序现象的复杂性，从而超越了两者。

这导致了Rudhyar的根本主张：通过将占星学定义为"生命的代数"，他将其置于数学思维——而非经验科学——的范畴。占星学提供形式，而非内容；它整合，而非通过因果机制预测。这一区分是"根本性的"——它改变了占星学应该如何被理解和实践的一切。

**Core Points**:
- Jeans's three epochs: animistic → mechanical → mathematical
- Parallel to astrology: animistic → vitalistic → algebraic
- Both animism and mechanism are anthropomorphic errors
- Mechanism (push/pull) structurally equivalent to vitalism (yang/yin)
- Mathematical stage: pure symbolic relations order phenomena
- Astrology defined as algebra of life = mathematical thought
- Placed in category of form-giving, not empirical science
- Capital distinction for understanding astrology's nature
- Symbols correlate without causal projection

**Narrative Snippets**:
- `[ns_aop_057]` `[trigger: three_epochs]` `[factor_trigger: astro_three_epochs AND astro_animistic AND astro_animistic_stage AND astro_three_epochs_struct]` `[role: 主干]` Jeans identifies three epochs: animistic, mechanical, mathematical—parallel to astrology's animistic, vitalistic, algebraic stages. → Source Text L1574-1577, L1645-1647
- `[ns_aop_058]` `[trigger: mechanism_vitalism]` `[factor_trigger: mechanism AND vitalism AND astro_mech_vital_func AND astro_post_anthropo]` `[role: 主干依赖]` Mechanism (push/pull) not basically different from vitalism (yang/yin)—both tangible dualism, anthropomorphic projection. → Source Text L1647-1656
- `[ns_aop_059]` `[trigger: mathematical_stage]` `[factor_trigger: astro_math_stage AND astro_creative_synth AND astro_math_placement]` `[role: 条件分支]` Mathematical stage: pure thought fits nature, symbolic relations order complexity—transcends anthropomorphism. → Source Text L1658-1669
- `[ns_aop_060]` `[trigger: astrology_mathematical]` `[factor_trigger: mathematical_thought AND astro_math_par_struct]` `[role: 总结]` By defining astrology as algebra of life, we place it in mathematical thought category—not empirical sciences. Capital distinction. → Source Text L1727-1729

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's use of Jeans (a mainstream physicist) lends credibility to his argument. The parallel he draws between scientific and astrological evolution is original and philosophically significant.
- **中文**: Rudhyar使用Jeans（一位主流物理学家）增强了其论证的可信度。他在科学与占星学演变之间的平行比较是原创且具有哲学意义的。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Three Epochs of Thought—Jeans's Framework"
    factor_refs: list = ['astro_three_epochs', 'astro_mech_vital', 'astro_math_category', 'astro_capital_distinction']
    
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
        l1_anchor="ap_v1.0.0_entry_1__three_epochs_of_thoug_001_L1",
    )
    version: str = "1.0.0"
