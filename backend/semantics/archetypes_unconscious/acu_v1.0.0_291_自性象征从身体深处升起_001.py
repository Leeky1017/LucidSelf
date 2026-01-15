"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535951
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
    semantic_id="acu_v1.0.0_291_自性象征从身体深处升起_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 291自性象征从身体深处升起(SemanticEntry):
    """
    **原文** (¶291, 行4929-4945):

> [291] The symbols of the self arise in the depths of the body and they...
    """
    
    original_text: str = """**原文** (¶291, 行4929-4945):

> [291] The symbols of the self arise in the depths of the body and they express its materiality every bit as much as the structure of the perceiving consciousness. The symbol is thus a living body, corpus et anima; hence the "child" is such an apt formula for the symbol. The uniqueness of the psyche can never enter wholly into reality, it can only be realized approximately...
>
> The more archaic and "deeper," that is the more physiological, the symbol is, the more collective and universal, the more "material" it is. The more abstract, differentiated, and specific it is, and the more its nature approximates to conscious uniqueness and individuality, the more it sloughs off its universal character.

**英文释义（主语言）**:

**自性象征的身体起源**：
自性象征从**身体深处**升起，既表达其物质性，也表达知觉意识的结构。

**象征 = 活的身体**：
象征因此是**活的身体，corpus et anima（身体和灵魂）**。因此"童子"是象征的恰当公式。

**心灵的独特性**：
心灵的独特性永远无法完全进入现实，只能近似实现，但它仍然是所有意识的绝对基础。

**心灵层次的深度特征**：
- 心灵越深的"层次"，随着它们退入黑暗，越失去个体独特性
- "更下面"，即接近自主功能系统时，它们变得越来越集体化
- 直到在身体的物质性中被普遍化和消灭
- 身体的碳只是碳。因此"在底层"心灵只是"世界"

**象征的深度-普遍性关系**：
- **越古老、越"深"（即越生理学）**的象征 → **越集体、越普遍、越"物质"**
- **越抽象、越分化、越特定**的象征 → **越接近意识的独特性和个体性** → **越脱落其普遍性**

**完整中文诠释（次语言）**:

**自性象征的身体起源**：
自性象征从**身体深处**升起，既表达其物质性，也表达知觉意识的结构。象征因此是**活的身体，corpus et anima（身体和灵魂）**。因此"童子"是象征的恰当公式。

**心灵独特性的局限**：
心灵的独特性永远无法完全进入现实，只能近似实现，但它仍然是所有意识的绝对基础。

**心灵深层的集体化**：
心灵越深的"层次"，随着它们退入黑暗，越失去个体独特性。"更下面"，即接近自主功能系统时，它们变得越来越集体化，直到在身体的物质性中被普遍化和消灭，即在化学物质中。身体的碳只是碳。因此"在底层"心灵只是"世界"。

**Kerényi的洞见**：
在这个意义上，荣格认为Kerényi完全正确：在象征中，世界本身在说话。

**象征的深度-普遍性关系**：
象征越古老、越"深"（即越生理学），就越集体、越普遍、越"物质"。象征越抽象、越分化、越特定，其本性越接近意识的独特性和个体性，就越脱落其普遍性。最终达到完全意识时，它有成为纯粹寓言的风险，不再超越意识理解的范围，因此暴露于各种理性主义的、因此不充分的解释尝试。

**核心要点**:
- 自性象征从身体深处升起
- 象征 = 活的身体 = corpus et anima
- "童子"是象征的恰当公式
- 心灵深层越深 → 越集体、普遍
- "在底层"心灵只是"世界"
- 在象征中世界本身在说话
- 越古老/深/生理学 → 越集体/普遍/物质
- 越抽象/分化/特定 → 越脱落普遍性

**叙事片段**:
- `[ns_cw9i_IV_291_001]` `[trigger: symbol_body]` `[factor_trigger: jung_self AND jung_body]` `[role: 主干]` 自性象征从身体深处升起——象征是活的身体(corpus et anima)，"童子"是象征的恰当公式。→ ¶291
- `[ns_cw9i_IV_291_002]` `[trigger: depth_universality]` `[factor_trigger: jung_symbol AND jung_collective]` `[role: 主干依赖]` 象征越古老/深/生理学→越集体/普遍/物质；越抽象/分化→越脱落普遍性。在底层心灵只是"世界"。→ ¶291"""
    normalized_text_zh: str = """"""
    subject: str = "¶291 自性象征从身体深处升起"
    factor_refs: list = ['engine_id', 'body_depths', 'psych_semantic', 'corpus_et_anima', 'psych_semantic', 'depth_universality', 'psych_semantic']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_291_自性象征从身体深处升起_001_L1",
    )
    version: str = "1.0.0"
