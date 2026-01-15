"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535901
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
    semantic_id="acu_v1.0.0_286_童子从冲突中涌现_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 286童子从冲突中涌现(SemanticEntry):
    """
    **原文** (¶286, 行4794-4802):

> [286] Out of this situation the "child" emerges as a symbolic content,...
    """
    
    original_text: str = """**原文** (¶286, 行4794-4802):

> [286] Out of this situation the "child" emerges as a symbolic content, manifestly separated or even isolated from its background (the mother), but sometimes including the mother in its perilous situation, threatened on the one hand by the negative attitude of the conscious mind and on the other by the horror vacui of the unconscious, which is quite ready to swallow up all its progeny, since it produces them only in play, and destruction is an inescapable part of its play. Nothing in all the world welcomes this new birth, although it is the most precious fruit of Mother Nature herself, the most pregnant with the future, signifying a higher stage of self-realization. That is why Nature, the world of the instincts, takes the "child" under its wing: it is nourished or protected by animals.

**英文释义（主语言）**:

**童子从情境中涌现**：
"童子"从这种情境中作为象征内容涌现，明显与其背景（母亲）分离甚至隔离，但有时包括母亲在其危险境遇中。

**双重威胁**：
- 一方面受意识心智的负面态度威胁
- 另一方面受无意识的"空虚恐惧"(horror vacui)威胁——无意识完全准备好吞噬其所有后代，因为它只是在游戏中产生它们，而毁灭是其游戏不可逃避的部分

**无人欢迎的诞生**：
世界上没有任何东西欢迎这个新诞生，尽管它是大自然母亲自己最珍贵的果实，最充满未来，意味着**更高阶段的自我实现**。

**自然的保护**：
因此，自然——本能的世界——将"童子"置于羽翼之下：它被动物哺育或保护。

**完整中文诠释（次语言）**:

**童子从冲突情境中涌现**：
"童子"从这种情境中作为象征内容涌现，明显与其背景（母亲）分离甚至隔离，但有时包括母亲在其危险境遇中。

**童子面临的双重威胁**：
童子一方面受意识心智的负面态度威胁，另一方面受无意识的"空虚恐惧"(horror vacui)威胁。无意识完全准备好吞噬其所有后代，因为它只是在游戏中产生它们，而毁灭是其游戏不可逃避的部分。

**新诞生的孤独**：
世界上没有任何东西欢迎这个新诞生，尽管它是大自然母亲自己最珍贵的果实，最充满未来，意味着**更高阶段的自我实现**。

**自然/本能的保护功能**：
这就是为什么自然——本能的世界——将"童子"置于羽翼之下：它被动物哺育或保护。这解释了为什么许多英雄/童神被动物抚养（如罗慕路斯和雷穆斯被母狼抚养）。

**核心要点**:
- 童子从冲突情境中作为象征内容涌现
- 与母亲/背景分离或隔离
- 双重威胁：意识的负面态度 + 无意识的"空虚恐惧"
- 无意识在游戏中产生并毁灭其后代
- 新诞生无人欢迎，却是最珍贵的果实
- 意味着更高阶段的自我实现
- 自然/本能保护童子——被动物哺育

**叙事片段**:
- `[ns_cw9i_IV_286_001]` `[trigger: child_emergence]` `[factor_trigger: jung_child_archetype AND jung_conflict]` `[role: 主干]` 童子从冲突情境中涌现——受意识负面态度和无意识"空虚恐惧"双重威胁。→ ¶286
- `[ns_cw9i_IV_286_002]` `[trigger: animal_protection]` `[factor_trigger: jung_child_archetype AND jung_instinct]` `[role: 主干依赖]` 自然/本能将童子置于羽翼之下——被动物哺育或保护。→ ¶286"""
    normalized_text_zh: str = """"""
    subject: str = "¶286 童子从冲突中涌现"
    factor_refs: list = ['engine_id', 'horror_vacui', 'psych_semantic', 'higher_self_realization', 'psych_semantic', 'animal_protection', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_286_童子从冲突中涌现_001_L1",
    )
    version: str = "1.0.0"
