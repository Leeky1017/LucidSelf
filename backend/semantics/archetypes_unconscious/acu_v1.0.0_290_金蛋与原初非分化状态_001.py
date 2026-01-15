"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535942
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
    semantic_id="acu_v1.0.0_290_金蛋与原初非分化状态_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 290金蛋与原初非分化状态(SemanticEntry):
    """
    **原文** (¶290, 行4903-4927):

> [290] The phenomenology of the "child's" birth always points back to a...
    """
    
    original_text: str = """**原文** (¶290, 行4903-4927):

> [290] The phenomenology of the "child's" birth always points back to an original psychological state of non-recognition, i.e., of darkness or twilight, of non-differentiation between subject and object, of unconscious identity of man and the universe. This phase of non-differentiation produces the golden egg, which is both man and universe and yet neither, but an irrational third...
>
> "Fantasies" are the natural expressions of the life of the unconscious... In the last analysis the human body, too, is built of the stuff of the world, the very stuff wherein fantasies become visible; indeed, without it they could not be experienced at all.

**英文释义（主语言）**:

**童子诞生的原初背景**：
"童子"诞生的现象学总是指向一种**原初心理状态**：
- 非认识状态
- 黑暗或黄昏
- 主客体之间的非分化
- 人与宇宙的无意识同一

**金蛋的象征**：
这个非分化阶段产生**金蛋**——既是人也是宇宙，但又两者都不是，而是**非理性的第三物**。

**幻想的现实性**：
幻想是无意识生活的自然表达。医学心理学知道"仅仅是"幻想可以导致多么可怕的身体功能紊乱和多么毁灭性的心理后果。

**身体与幻想的关系**：
人体也是由世界的材料构成的——正是在这种材料中幻想变得可见；没有它，幻想根本无法被体验。

**完整中文诠释（次语言）**:

**童子诞生指向原初非分化状态**：
"童子"诞生的现象学总是指向一种原初心理状态：非认识状态，即黑暗或黄昏，主客体之间的非分化，人与宇宙的无意识同一。

**金蛋作为非理性第三物**：
这个非分化阶段产生**金蛋**——既是人也是宇宙，但又两者都不是，而是一个非理性的第三物。

**原始意识与分化意识的不同视角**：
对原始人的黄昏意识而言，这个蛋似乎是从广阔世界的子宫中产生的，因此是宇宙的、客观的、外部的事件。另一方面，对分化意识而言，这个蛋显然只是心灵抛出的象征——或更糟的——一种空想推测，因此"只不过是"一种原始幻想，没有任何"现实性"。

**现代医学心理学的立场**：
然而，当代医学心理学对这些"幻想"有不同看法。它太清楚"仅仅是"幻想可以导致多么可怕的身体功能紊乱和多么毁灭性的心理后果。幻想是无意识生活的自然表达。

**身体与世界的同质性**：
最终分析中，人体也是由世界的材料构成的——正是在这种材料中幻想变得可见；没有它，幻想根本无法被体验。

**核心要点**:
- 童子诞生指向原初非分化状态
- 原初状态：黑暗/黄昏、主客不分、人与宇宙同一
- 金蛋 = 非理性第三物（既是人也是宇宙，又都不是）
- 幻想是无意识的自然表达，有真实心理生理后果
- 人体由世界材料构成——幻想通过身体变得可见

**叙事片段**:
- `[ns_cw9i_IV_290_001]` `[trigger: golden_egg]` `[factor_trigger: jung_child_archetype AND jung_non_differentiation]` `[role: 主干]` 童子诞生指向原初非分化状态——金蛋既是人也是宇宙，又都不是，是非理性第三物。→ ¶290
- `[ns_cw9i_IV_290_002]` `[trigger: fantasy_reality]` `[factor_trigger: jung_fantasy AND jung_body]` `[role: 主干依赖]` 幻想是无意识的自然表达，有真实心理生理后果——人体由世界材料构成，幻想通过身体变得可见。→ ¶290"""
    normalized_text_zh: str = """"""
    subject: str = "¶290 金蛋与原初非分化状态"
    factor_refs: list = ['engine_id', 'non_differentiation', 'psych_semantic', 'golden_egg', 'psych_semantic', 'fantasy_reality', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_290_金蛋与原初非分化状态_001_L1",
    )
    version: str = "1.0.0"
