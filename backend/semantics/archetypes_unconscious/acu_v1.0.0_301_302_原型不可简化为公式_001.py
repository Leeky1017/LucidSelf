"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.536022
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
    semantic_id="acu_v1.0.0_301_302_原型不可简化为公式_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 301302原型不可简化为公式(SemanticEntry):
    """
    **原文** (¶301-302, 行5107-5131):

> [301] I am aware that a psychological commentary on the child arch...
    """
    
    original_text: str = """**原文** (¶301-302, 行5107-5131):

> [301] I am aware that a psychological commentary on the child archetype without detailed documentation must remain a mere sketch... No archetype can be reduced to a simple formula. It is a vessel which we can never empty, and never fill. It has a potential existence only, and when it takes shape in matter it is no longer what it was. It persists throughout the ages and requires interpreting ever anew. The archetypes are the imperishable elements of the unconscious, but they change their shape continually.
>
> [302] It is a well-nigh hopeless undertaking to tear a single archetype out of the living tissue of the psyche; but despite their interwovenness they do form units of meaning that can be apprehended intuitively. Psychology, as one of the many expressions of psychic life, operates with ideas which in their turn are derived from archetypal structures and thus generate a somewhat more abstract kind of myth.

**英文释义（主语言）**:

**心理学评论的局限**：
荣格承认，没有详细文献的童子原型心理学评论只能是一个素描。由于这对心理学家是处女地，主要努力是标出原型提出的问题的可能范围。

**原型的流动性**：
在这个领域，清晰的区分和严格的表述是不可能的，因为某种**流动的相互渗透属于所有原型的本性**。它们最多只能被粗略地界定。它们的**活的意义**更多来自作为整体的呈现，而非单一表述。

**原型不可简化为公式**：
**没有原型可以简化为简单公式。** 它是一个我们永远无法倒空也永远无法填满的**容器**。它只有**潜在存在**，当它在物质中成形时就不再是它原来的样子。它**贯穿各个时代**，需要不断重新诠释。

**原型的本质**：
原型是无意识的**不朽元素**，但它们**不断改变形状**。

**从心灵活组织中撕出原型的困难**：
从心灵的活组织中撕出单一原型几乎是无望的努力；但尽管它们相互交织，它们确实形成可以直觉把握的**意义单元**。

**心理学作为现代神话**：
心理学作为心理生活的众多表达之一，使用源自原型结构的观念，因此产生**一种更抽象的神话**。

**完整中文诠释（次语言）**:

**原型的流动本性**：
清晰的区分和严格的表述在这个领域是不可能的，因为某种**流动的相互渗透属于所有原型的本性**。它们最多只能被粗略地界定。它们的**活的意义**更多来自作为整体的呈现，而非单一表述。每一次更清晰地聚焦它们的尝试都会立即受到惩罚——意义的不可触及核心失去其光辉。

**原型不可简化**：
**没有原型可以简化为简单公式。** 它是一个我们永远无法倒空也永远无法填满的**容器**。它只有**潜在存在**，当它在物质中成形时就不再是它原来的样子。它**贯穿各个时代**，需要不断重新诠释。原型是无意识的**不朽元素**，但它们**不断改变形状**。

**撕出原型的困难与可能**：
从心灵的活组织中撕出单一原型几乎是无望的努力；但尽管它们相互交织，它们确实形成可以直觉把握的**意义单元**。心理学作为心理生活的众多表达之一，使用源自原型结构的观念，因此产生**一种更抽象的神话**。心理学因此将神话的古老语言翻译成现代神话语——当然尚未被认可——构成"科学"神话的一个元素。

**核心要点**:
- 原型有流动的相互渗透本性
- 原型最多只能被粗略界定
- 原型的活的意义来自整体呈现
- 没有原型可简化为简单公式
- 原型 = 永远倒不空填不满的容器
- 原型只有潜在存在，成形时就变了
- 原型贯穿时代，需不断重新诠释
- 原型 = 不朽元素，但不断改变形状
- 原型形成可直觉把握的意义单元
- 心理学 = 产生更抽象神话的现代语言

**叙事片段**:
- `[ns_cw9i_IV_301_001]` `[trigger: archetype_irreducible]` `[factor_trigger: jung_archetype]` `[role: 主干]` 没有原型可简化为公式——是永远倒不空填不满的容器，只有潜在存在，需不断重新诠释。→ ¶301
- `[ns_cw9i_IV_302_001]` `[trigger: psychology_myth]` `[factor_trigger: jung_psychology AND jung_myth]` `[role: 主干依赖]` 心理学使用源自原型结构的观念——产生一种更抽象的神话，是科学神话的元素。→ ¶302"""
    normalized_text_zh: str = """"""
    subject: str = "¶301-302 原型不可简化为公式"
    factor_refs: list = ['engine_id', 'fluid_interpenetration', 'psych_semantic', 'irreducible', 'psych_semantic', 'imperishable_changing', 'psych_semantic', 'psychology_as_myth', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_301_302_原型不可简化为公式_001_L1",
    )
    version: str = "1.0.0"
