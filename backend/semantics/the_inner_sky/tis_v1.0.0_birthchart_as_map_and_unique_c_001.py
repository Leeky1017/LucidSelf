"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134353
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
    semantic_id="tis_v1.0.0_birthchart_as_map_and_unique_c_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class BirthchartAsMapAndUniqueC(SemanticEntry):
    """
    **Source Text**:
A birthchart is a unique arrangement of astrology’s primary elements: signs, houses...
    """
    
    original_text: str = """**Source Text**:
A birthchart is a unique arrangement of astrology’s primary elements: signs, houses, and planets. Even though there are only about three dozen words in astrology’s vocabulary, when we add the laws of grammar and syntax they combine in nearly endless ways. A birthchart is a particular combination, taken to represent the individual.
Physically, a birthchart is simply a map. It shows the way the sun, moon, and planets were arranged in the sky at the moment a person was born.
...
Yet the birthchart is only a map of the sky. Such a simple thing. Its symbolism does not arise out of the pet theories of any man or woman. It stands beyond personal prejudices, beyond the mythologies of any culture. Its foundation is far deeper, far more primal. Astrology is rooted in nature, just as we are.

**Key Term Analysis**:
- `primary elements`: the basic symbolic building blocks—signs, houses, and planets.
- `unique arrangement`: the specific combination of those elements that represents one individual.
- `map of the sky`: the chart as a two‑dimensional diagram of celestial positions at birth.
- `rooted in nature`: the claim that astrological symbolism is grounded in natural cycles, not private theories.

**English Paraphrase (Primary Language)**:
Forrest defines a birthchart as a unique arrangement of astrology’s primary elements: signs, houses, and planets. Although the symbolic vocabulary is small—only about three dozen "words"—the rules of grammar and syntax allow nearly infinite combinations. Each chart is one such combination, taken as a symbolic representation of a particular person. This moves us away from the idea of fixed types and toward a language model: we are not twelve signs, but countless "sentences" built from the same basic alphabet.

On the physical level, a birthchart is simply a map that records how the sun, moon, and planets were arranged in the sky at the moment of birth. Its lines and glyphs are just a diagram. Yet its symbolic power does not come from anyone’s personal theory or cultural myth; it comes from the underlying patterns of nature—cycles of light and darkness, orbital relationships, and the way these cycles intersect with human experience. The chart, then, is both very simple (a sky map) and very deep (a compact picture of how an individual is woven into natural rhythms).

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 对命盘的定义，从一开始就强调「组合」与「语言」的视角。命盘是占星三大基本要素——星座、宫位与行星——的一种独特排列。虽然整套符号系统的「词汇」其实只有三十多个，但一旦引入语法与句法规则，这些词可以组合出几乎无穷多种句子。每一张命盘，就是其中一条只属于某个个体的「句子」，而不是把人粗暴地塞进十二个固定类型里的标签表。

在物理层面上，命盘只是一张图：它记录了一个人在出生那一刻，太阳、月亮与诸行星在天空中的相对位置。这些线条与符号本身并不神秘。然而，它所承载的象征意义，并不是某个占星师个人理论或某个文化神话的产物，而是扎根于自然本身——光与暗的周期、行星绕行的节奏，以及这些节奏如何与人类经验交织。换句话说，命盘一方面极其朴素（只是天空的平面地图），另一方面又极其深刻（是一幅浓缩了「某个人如何嵌入自然节律」的图像）。

**Core Points**:
- A birthchart is a unique combination of signs, houses, and planets.
- The astrological vocabulary is small, but grammar and syntax create near‑infinite variations.
- Physically, the chart is a two‑dimensional map of the sky at birth.
- Symbolically, it is rooted in natural patterns rather than personal or cultural theories.

**Detailed Explanation**:
This definition anchors the entire system in both structure and humility. By emphasizing a limited vocabulary with rich combinatorics, Forrest explains how astrology can speak precisely about individuals without multiplying symbols endlessly. The "map" metaphor clarifies that the chart is descriptive, not causal: it depicts configurations that correlate with psychological patterns, but it does not mechanically cause them. Describing astrology as rooted in nature situates it alongside other nature‑based sciences and arts, even as its focus remains symbolic.

The distinction between physical map and symbolic meaning also protects against superstition. Anyone can, in principle, verify the astronomical positions on a chart. What makes the map meaningful is the long, collective observation of how these natural cycles resonate with human life. In practice, this means that calibration work must keep both levels in view: we must be precise about what the chart literally shows, and equally precise about how we derive symbolic interpretations from those natural facts.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The phrase "only a map of the sky" is preserved to underline the modesty of the physical object, while the language of "primary elements" and "grammar and syntax" is expanded slightly to connect with earlier chapters on vocabulary. The claim that astrology is "rooted in nature" is highlighted because it contrasts with views that see astrology as purely cultural.
- **中文**：译文中特意强化了「有限词汇 × 无限组合」的语言学比喻，以呼应本书整体「占星 = 一门语言」的框架。"rooted in nature" 译为「扎根于自然」，并用「自然节律与人类经验的交织」来展开，避免被误解为某种抽象的「天意」。对「only a map」则处理为「一方面极其朴素、另一方面极其深刻」的对比，以符合中文的修辞习惯。

**Narrative Snippets**:
- `[ns_innersky_058]` `[trigger: chart_definition]` `[factor_trigger: astro_chart AND astro_individual]` `[role: 主干]` A birthchart is a unique arrangement of signs, houses, and planets—a particular combination representing the individual. → Source Text
- `[ns_innersky_059]` `[trigger: vocabulary_size]` `[factor_trigger: astro_language AND astro_combination]` `[role: 主干依赖]` Only about three dozen words in astrology's vocabulary, but grammar and syntax combine them in nearly endless ways. → Source Text
- `[ns_innersky_060]` `[trigger: physical_chart]` `[factor_trigger: astro_chart AND astro_celestial]` `[role: 条件分支]` Physically, a birthchart is simply a map showing how the celestial bodies were arranged at the moment of birth. → Source Text
- `[ns_innersky_061]` `[trigger: nature_basis]` `[factor_trigger: astro_symbol AND astro_nature]` `[role: 总结]` Astrology's symbolism does not arise from personal theories—it is rooted in nature, just as we are. → Source Text
- `[ns_innersky_062]` `[trigger: beyond_culture]` `[factor_trigger: astro_chart AND astro_universal]` `[role: 主干]` The chart stands beyond personal prejudices, beyond the mythologies of any culture—its foundation is far more primal. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Birthchart as Map and Unique Combination of Elements"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_birthchart_as_map_and_unique_c_001_L1",
    )
    version: str = "1.0.0"
