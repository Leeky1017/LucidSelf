"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134326
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
    semantic_id="tis_v1.0.0_the_holy_trinity__signs__house_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TheHolyTrinitySignsHouse(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Holy Trinity | Signs, houses, planets as three symbol systems | Foundational structure |
| Signs | Identity patterns, psychological framework | HOW/WHY dimension |
| Houses | Arenas of life, fields of activity | WHERE dimension |
| Planets | Psychological functions, parts of mind | WHAT dimension |

**Source Text**:
Signs, houses, and planets. Three distinct systems of symbols. Three vocabularies. Together they form astrology's holy trinity. Each serves a distinct purpose. Each answers a distinct set of questions. Without all three, astrology could not exist. Lacking one, it could have breadth and height, but no depth.
In broad terms, signs are identity, while houses are the arena within which identity operates. Signs provide the psychological framework, the needs and fears, the attitudes and biases, with which we attack the houses. Houses indicate problems and issues. They represent tasks we must face.
Planets are the third dimension of astrological symbolism. They represent the actual structure of the mind. Each one symbolizes a particular psychological function: intellect; emotions; self-imagery; the impulse toward intimacy.

**English Paraphrase (Primary Language)**:
Forrest introduces astrology's **three-symbol grammar**: signs, houses, and planets. Each system answers a different type of question, and together they create the depth necessary for meaningful interpretation.

**Signs** represent psychological identity—the internal patterns of needs, fears, attitudes, and biases that shape how we engage with life. They describe processes occurring within the mind: learning courage, developing sensitivity, cultivating awareness of others' needs.

**Houses** represent external arenas—the concrete theaters of life where identity operates. One house symbolizes career, another intimate relationships, a third material circumstances. Even houses that seem internal (like the unconscious mind) still represent something "outside" personality that must be encountered.

**Planets** represent the actual structure of the psyche—distinct psychological functions like intellect (Mercury), emotions (Moon), self-image, or the impulse toward intimacy (Venus). Together, the planets form a map of the human mind, analogous to Freud's ego/id/superego model but with more differentiated components.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 在本章引入占星学的**三套符号语法**：星座、宫位、行星。每套系统回答不同类型的问题，三者结合才能产生有意义解读所需的深度。

**星座**代表心理身份——塑造我们如何与生活互动的内在模式，包括需求、恐惧、态度和偏见。它们描述心灵内部发生的过程：学习勇气、发展敏感度、培养对他人需求的觉察。

**宫位**代表外在舞台——身份运作的具体生活领域。一个宫位象征事业，另一个象征亲密关系，第三个象征物质境况。即使是看似内在的宫位（如无意识）也仍然代表人格"之外"必须面对的事物。

**行星**代表心灵的实际结构——不同的心理功能，如智力（水星）、情感（月亮）、自我意象或亲密冲动（金星）。所有行星合在一起形成一幅人类心智地图，类似弗洛伊德的自我/本我/超我模型，但组件分化更精细。

**Core Points**:
- Signs, houses, and planets form astrology's essential three-system grammar
- Signs = identity/HOW (psychological processes within)
- Houses = arena/WHERE (external life theaters)
- Planets = function/WHAT (parts of the psyche)
- All three required for depth; missing one = flat interpretation

**Detailed Explanation**:
This chapter establishes the grammatical foundation for all subsequent interpretation. Forrest's innovation is framing the three systems not as arbitrary collections of meanings but as answers to fundamentally different questions. This what/how-why/where structure becomes the engine's primary parsing logic: identify which planetary function is involved, understand its sign-driven motivation and style, then locate the house arena where it manifests.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Forrest's "holy trinity" metaphor emphasizes that all three systems are equally essential—none is primary. The Freud comparison (ego/id/superego paralleled to planetary map) positions astrology within a psychological rather than predictive framework.
- **中文**: "神圣三位一体"隐喻强调三套系统同等重要——没有哪一个是主导。弗洛伊德比较（行星地图类比自我/本我/超我）将占星定位于心理学而非预测框架中。

**Narrative Snippets**:
- `[ns_innersky_043]` `[trigger: symbol_system_intro]` `[factor_trigger: astro_symbol AND astro_trinity AND three_symbol_grammar]` `[role: 主干]` Signs, houses, and planets form astrology's holy trinity—each answers a distinct set of questions. → Source Text
- `[ns_innersky_044]` `[trigger: sign_definition]` `[factor_trigger: astro_sign AND astro_identity AND sign_howwhy_dimension]` `[role: 主干依赖]` Signs are identity—the psychological framework of needs, fears, attitudes, and biases with which we attack life. → Source Text
- `[ns_innersky_045]` `[trigger: house_definition]` `[factor_trigger: astro_house AND astro_arena AND house_where_dimension]` `[role: 条件分支]` Houses indicate problems and issues—they represent tasks we must face in specific arenas of life. → Source Text
- `[ns_innersky_046]` `[trigger: planet_definition]` `[factor_trigger: astro_planet AND astro_function AND planet_what_dimension]` `[role: 总结]` Planets represent the actual structure of the mind—each symbolizes a particular psychological function. → Source Text
- `[ns_innersky_047]` `[trigger: three_dimensions]` `[factor_trigger: astro_synthesis AND astro_depth AND interpretation_sequence]` `[role: 主干]` Without all three systems, astrology could not exist; lacking one, it could have breadth and height, but no depth. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "The Holy Trinity: Signs, Houses, and Planets"
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
        l1_anchor="tis_v1.0.0_the_holy_trinity__signs__house_001_L1",
    )
    version: str = "1.0.0"
