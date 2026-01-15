"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535768
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
    semantic_id="acu_v1.0.0_273_童子母题代表集体心灵的童年方面_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 273童子母题代表集体心灵的童年方面(SemanticEntry):
    """
    **原文** (¶273, 行4596-4602):

> [273] Statements like "The child motif is a vestigial memory of one's ...
    """
    
    original_text: str = """**原文** (¶273, 行4596-4602):

> [273] Statements like "The child motif is a vestigial memory of one's own childhood" and similar explanations merely beg the question. But if, giving this proposition a slight twist, we were to say, "The child motif is a picture of certain forgotten things in our childhood," we are getting closer to the truth. Since, however, the archetype is always an image belonging to the whole human race and not merely to the individual, we might put it better this way: "The child motif represents the preconscious, childhood aspect of the collective psyche."

**英文释义（主语言）**:

**错误解释**："童子母题是个人童年的残余记忆"——只是回避问题。

**稍好的解释**："童子母题是我们童年中某些被遗忘事物的图像"——更接近真相。

**最佳表述**：由于原型总是属于整个人类而非仅仅个体的意象，更好的说法是：**"童子母题代表集体心灵的前意识、童年方面。"**

**完整中文诠释（次语言）**:

荣格在此批评和修正对童子母题的常见解释：

**错误解释**：
"童子母题是个人童年的残余记忆"——这种解释只是回避问题，没有真正解释任何东西。

**稍好的解释**：
如果我们稍微转换这个命题，说"童子母题是我们童年中某些被遗忘事物的图像"，就更接近真相。

**最佳表述**：
然而，由于原型总是属于整个人类而非仅仅个体的意象，我们可以更好地表述为：**"童子母题代表集体心灵的前意识、童年方面。"**

这个定义将童子母题从个人层面提升到集体层面，从个人记忆提升到人类共同的心理遗产。

**核心要点**:
- "童子=个人童年记忆"是错误解释
- "童子=被遗忘的童年事物"稍好
- 最佳定义：童子母题=集体心灵的前意识、童年方面
- 原型属于整个人类，非仅个体

**叙事片段**:
- `[ns_cw9i_IV_273_001]` `[trigger: child_collective]` `[factor_trigger: jung_child_archetype AND jung_collective_psyche]` `[role: 主干]` 童子母题代表集体心灵的前意识、童年方面——不是个人童年记忆，而是人类共同的心理遗产。→ ¶273"""
    normalized_text_zh: str = """"""
    subject: str = "¶273 童子母题代表集体心灵的童年方面"
    factor_refs: list = ['engine_id', 'collective_childhood', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_273_童子母题代表集体心灵的童年方面_001_L1",
    )
    version: str = "1.0.0"
