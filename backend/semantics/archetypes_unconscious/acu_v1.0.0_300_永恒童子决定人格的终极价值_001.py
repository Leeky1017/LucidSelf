"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.536010
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
    semantic_id="acu_v1.0.0_300_永恒童子决定人格的终极价值_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 300永恒童子决定人格的终极价值(SemanticEntry):
    """
    **原文** (¶300, 行5094-5103):

> [300] Primitive man is no puzzle to himself. The question "What is man...
    """
    
    original_text: str = """**原文** (¶300, 行5094-5103):

> [300] Primitive man is no puzzle to himself. The question "What is man?" is the question that man has always kept until last... This experience has projected itself into the archetype of the child, which expresses man's wholeness. The "child" is all that is abandoned and exposed and at the same time divinely powerful; the insignificant, dubious beginning, and the triumphal end. The "eternal child" in man is an indescribable experience, an incongruity, a handicap, and a divine prerogative; an imponderable that determines the ultimate worth or worthlessness of a personality.

**英文释义（主语言）**:

**原始人与自我认识**：
原始人对自己不是谜。"人是什么？"是人总是留到最后的问题。原始人有太多心灵在意识之外，以至于外部心理体验对他比对我们更熟悉。

**意识被心理力量包围**：
被心理力量包围、支持或威胁或欺骗的意识，是人类古老的经验。这种经验已投射到**童子原型**中，表达**人的整体性**。

**童子的悖论定义**：
"童子"是所有被遗弃和暴露的，同时又是**神圣强大的**；是**微不足道、可疑的开端**，和**凯旋的终结**。

**永恒童子的本质**：
人内心的"永恒童子"是：
- 一种**不可描述的经验**
- 一种**不协调**
- 一种**障碍**
- 一种**神圣特权**
- 一种**决定人格终极价值或无价值的不可衡量者**

**完整中文诠释（次语言）**:

**原始人与现代人的差异**：
原始人对自己不是谜。"人是什么？"是人总是留到最后的问题。原始人有太多心灵在意识之外，以至于外部心理体验对他比对我们更熟悉。

**意识被心理力量包围的古老经验**：
被心理力量包围、支持或威胁或欺骗的意识，是人类古老的经验。这种经验已投射到**童子原型**中，表达**人的整体性**。

**童子的完整悖论定义**：
"童子"是所有被遗弃和暴露的，同时又是**神圣强大的**；是**微不足道、可疑的开端**，和**凯旋的终结**。

**永恒童子的深层意义**：
人内心的"永恒童子"是一种**不可描述的经验**，一种**不协调**，一种**障碍**，和一种**神圣特权**；一种**决定人格终极价值或无价值的不可衡量者**。

这是对童子原型的最终总结：它是人格中最关键却最难以捉摸的因素。

**核心要点**:
- 原始人对自己不是谜——有太多心灵在意识之外
- 被心理力量包围的意识=人类古老经验→投射为童子原型
- 童子原型表达人的整体性
- 童子=被遗弃+神圣强大
- 童子=微不足道开端+凯旋终结
- 永恒童子=不可描述经验+不协调+障碍+神圣特权
- 永恒童子=决定人格终极价值的不可衡量者

**叙事片段**:
- `[ns_cw9i_IV_300_001]` `[trigger: eternal_child]` `[factor_trigger: jung_child_archetype AND jung_personality]` `[role: 主干]` 永恒童子=不可描述经验+不协调+障碍+神圣特权——决定人格终极价值的不可衡量者。→ ¶300"""
    normalized_text_zh: str = """"""
    subject: str = "¶300 永恒童子决定人格的终极价值"
    factor_refs: list = ['engine_id', 'eternal_child', 'psych_semantic', 'abandoned_divine', 'psych_semantic', 'ultimate_worth', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_300_永恒童子决定人格的终极价值_001_L1",
    )
    version: str = "1.0.0"
