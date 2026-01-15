"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237576
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
    semantic_id="ap_v1.0.0_preface_to_the_1991_edition__a_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PrefaceToThe1991EditionA(SemanticEntry):
    """
    **Source Text** (Lines 387-451):
> The book you are now holding was described on its flyleaf in 1936...
    """
    
    original_text: str = """**Source Text** (Lines 387-451):
> The book you are now holding was described on its flyleaf in 1936 by Paul Clancy as "the greatest step forward in Astrology since the time of Ptolemy." That was no jovial publisher's hype. The influence of this book, often unacknowledged, has been all pervasive, consciously and unconsciously shaping the way most thinking astrologers view astrology today...
>
> Perhaps the central importance of this book is the very clear insight Rudhyar presents of the fundamental nature of astrology, and the importance he therefore places on an understanding of its symbolic and formal basis. Rudhyar's vision of astrology as "the algebra of life" whose goal is the "alchemy of personality," reveals astrology to be primarily, not as so often portrayed as a traditional body of empirical knowledge, but as a system of symbolic logic, based on first principles, which we can employ for understanding the underlying order and significance of the processes of Nature...
>
> Rudhyar's definition of astrology as "the algebra of life" is no casual image. Rudhyar is never casual. He is deliberately identifying astrology with mathematical thought as opposed to empirical knowledge. Rudhyar points out that algebra comes from the Arabic word "al-jebr" meaning the reduction of parts to a whole. "Jabara" in fact means to bind together, and the function of algebra is the binding together, correlating or integrating of elements into a formulated whole...
>
> Rudhyar's emphasis is a crucial one, for whilst no-one, including Rudhyar himself, would deny the importance and value of observation and empirical studies, we have to be clear that astrology teaches about what Aristotle would have called the formal or "informing" causes of things, and not as does most of modern science, about their material causes.

**Key Term Analysis**:
- **Algebra of life**: `al-jebr = reduction to whole` / `binding together elements` / `symbolic integration`
- **Formal causes (Aristotle)**: `informing principles` / `not material causes` / `pattern/form`
- **Symbolic logic**: `first principles` / `not empirical data` / `understanding order`
- **System of symbolic logic**: `astrology's true nature` / `formal not material` / `meaning-making`
- **Greatest step since Ptolemy**: `Paul Clancy's assessment` / `historical significance` / `1936 evaluation`

**English Paraphrase (Primary Language)**:
Charles Harvey's 1991 Preface analyzes the book's revolutionary contribution. He cites Paul Clancy's 1936 assessment—"the greatest step forward since Ptolemy"—and affirms its accuracy. The book's central insight is Rudhyar's understanding of astrology's fundamental nature as symbolic logic, not empirical science.

The phrase "algebra of life" is carefully chosen: "algebra" derives from Arabic "al-jebr" meaning "reduction of parts to a whole" or "binding together." Astrology, like algebra, integrates symbolic elements (planets, signs, houses) into a coherent formula describing a living whole. But where algebra deals with quantities, astrology deals with qualities—life-qualities, universal processes from physical to spiritual.

Harvey invokes Aristotle's distinction between formal and material causes. Modern science focuses on material causes (what things are made of, physical mechanisms). Astrology addresses formal causes—the patterns, principles, and "informing" structures that give meaning and order. This is not a deficiency but a different epistemological domain. Empirical studies have value, but they cannot capture astrology's essential function as symbolic language for understanding life's underlying order.

**Complete Chinese Interpretation (Secondary Language)**:
Charles Harvey的1991年前言分析了本书的革命性贡献。他引用Paul Clancy 1936年的评价——"自托勒密以来占星学最伟大的进步"——并确认其准确性。本书的核心洞见是Rudhyar对占星学作为符号逻辑而非经验科学的根本性质的理解。

"生命的代数"这个短语是精心选择的："algebra"源自阿拉伯语"al-jebr"，意为"将部分还原为整体"或"绑定在一起"。占星学如同代数，将符号元素（行星、星座、宫位）整合为描述活生生整体的连贯公式。但代数处理的是数量，占星学处理的是质量——生命质量、从物质到精神层面的普世过程。

Harvey援引亚里士多德对形式因和质料因的区分。现代科学关注质料因（事物由什么构成、物理机制）。占星学处理形式因——赋予意义和秩序的模式、原则和"形成性"结构。这不是缺陷而是不同的认识论领域。经验研究有其价值，但无法捕捉占星学作为理解生命底层秩序的符号语言的本质功能。

**Core Points**:
- "Greatest step since Ptolemy" (Clancy 1936) - book's historical significance
- Astrology as symbolic logic, not empirical science
- "Algebra of life" - al-jebr = binding parts into whole
- Symbolic elements integrate into formula for living whole
- Algebra deals with quantities; astrology with qualities
- Aristotle's formal vs material causes distinction
- Astrology teaches formal/informing causes
- Modern science teaches material causes
- Different epistemological domains, not inferior/superior

**Detailed Explanation**:
Harvey's analysis illuminates Rudhyar's epistemological sophistication. By positioning astrology alongside algebra (mathematical, formal, logical) rather than physics (empirical, material, experimental), Rudhyar rescues astrology from the impossible task of proving itself by scientific methods designed for a different domain. The Aristotelian distinction is crucial: asking "does astrology work?" is like asking "does algebra work?"—it's a category error. Algebra works as a formal system for relating quantities; astrology works as a symbolic system for relating life-qualities.

This explains why empirical tests of astrology often fail: they seek material-cause correlations (statistical links between planetary positions and measurable outcomes) when astrology actually operates through formal-cause symbolism (meaningful patterns revealing underlying order). The Gauquelin research, for instance, found statistical correlations—but these capture only a thin slice of what astrology actually does.

**Narrative Snippets**:
- `[ns_aop_018]` `[trigger: algebra_of_life]` `[factor_trigger: algebra AND astro_algebra_life AND astro_algebra_def AND astro_algebra_framework]` `[role: 主干]` "Algebra of life" comes from al-jebr meaning binding parts into whole—astrology integrates symbolic elements into formula for living totality. → Source Text L417-429
- `[ns_aop_019]` `[trigger: formal_causes]` `[factor_trigger: formal_causes AND material_causes AND astro_content_free AND astro_formal_operation AND astro_epistemic_domain]` `[role: 主干依赖]` Astrology teaches about Aristotle's formal or "informing" causes, not material causes as modern science does. → Source Text L435-437
- `[ns_aop_020]` `[trigger: symbolic_logic]` `[factor_trigger: astro_symbolic_logic AND astro_abstract_order]` `[role: 条件分支]` Astrology is a system of symbolic logic based on first principles for understanding Nature's underlying order. → Source Text L411-415
- `[ns_aop_021]` `[trigger: quality_not_quantity]` `[factor_trigger: qualities AND quantities AND astro_quality_focus]` `[role: 总结]` Where algebra deals with quantities, astrology deals with qualities—universal life processes from physical to spiritual. → Source Text L427-429

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Harvey's 1991 Preface provides the most sophisticated philosophical analysis of Rudhyar's contribution. The Aristotelian framework (formal vs material causes) clarifies why scientific testing often misses astrology's point.
- **中文**: Harvey 1991年前言提供了对Rudhyar贡献最精深的哲学分析。亚里士多德框架（形式因vs质料因）阐明了为什么科学测试常常误解占星学的要点。"""
    normalized_text_zh: str = """"""
    subject: str = "Preface to the 1991 Edition: Algebra of Life and Formal Causes"
    factor_refs: list = ['astro_algebra_life', 'phil_formal_causes', 'phil_material_causes', 'astro_symbolic_logic', 'astro_al_jebr']
    
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
        l1_anchor="ap_v1.0.0_preface_to_the_1991_edition__a_001_L1",
    )
    version: str = "1.0.0"
