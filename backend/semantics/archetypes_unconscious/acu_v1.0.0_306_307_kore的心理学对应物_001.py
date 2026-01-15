"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552517
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
    semantic_id="acu_v1.0.0_306_307_kore的心理学对应物_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 306307Kore的心理学对应物(SemanticEntry):
    """
    **原文** (§306-307, 行5173-5188):

> [306] Not only is the figure of Demeter and the Kore in its threef...
    """
    
    original_text: str = """**原文** (§306-307, 行5173-5188):

> [306] Not only is the figure of Demeter and the Kore in its threefold aspect as maiden, mother, and Hecate not unknown to the psychology of the unconscious, it is even something of a practical problem. The "Kore" has her psychological counterpart in those archetypes which I have called the self or supraordinate personality on the one hand, and the anima on the other.
>
> [307] The psychologist has to contend with the same difficulties as the mythologist when an exact definition or clear and concise information is demanded of him. The picture is concrete, clear, and subject to no misunderstandings only when it is seen in its habitual context.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Kore (科瑞) | 少女 | 阿尼玛/自性 | 得墨忒耳神话 |
| Demeter (得墨忒耳) | 谷物女神 | 大母神 | 母女神话 |
| Hecate (赫卡忒) | 冥界女神 | 暗面/老妪 | 三相女神 |
| Supraordinate personality | 超位人格 | 自性 | 整体性 |

**英文释义（主语言）**:

**得墨忒耳-科瑞的三相**：
得墨忒耳和科瑞的形象以其三重面向——**少女、母亲和赫卡忒**——对无意识心理学来说并非陌生，甚至是一个实际问题。

**Kore的心理学对应物**：
"Kore"在心理学上对应两个原型：
- **自性或超位人格**
- **阿尼玛**

**定义的困难**：
心理学家与神话学家面临同样的困难——当被要求给出精确定义或清晰简明的信息时。图像只有在其习惯性语境中才是具体的、清晰的、不会误解的。

**完整中文诠释（次语言）**:

**得墨忒耳-科瑞神话的心理学意义**：
得墨忒耳和科瑞的形象以其三重面向——少女、母亲和赫卡忒——对无意识心理学来说并非陌生，甚至是一个实际问题。这个神话形象在临床实践中经常出现。

**Kore的双重心理学对应**：
"Kore"在心理学上对应两个原型：一方面是**自性或超位人格**，另一方面是**阿尼玛**。为解释这些对大多数读者不熟悉的形象，荣格需要先做一些一般性说明。

**定义原型的困难**：
心理学家与神话学家面临同样的困难——当被要求给出精确定义或清晰简明的信息时。图像只有在其习惯性语境中才是具体的、清晰的、不会误解的。以这种形式，它告诉我们它所包含的一切。但一旦试图抽象出图像的"真正本质"，整个事情就变得模糊不清。

**核心要点**:
- 得墨忒耳-科瑞 = 三相女神（少女、母亲、赫卡忒）
- Kore的心理学对应：自性/超位人格 + 阿尼玛
- 原型不能简单定义——需在语境中理解
- 抽象"真正本质"会使原型变得模糊

**叙事片段**:
- `[ns_cw9i_V_306_001]` `[trigger: kore_archetype]` `[factor_trigger: jung_kore AND jung_anima AND jung_self]` `[role: 主干]` Kore的心理学对应：自性/超位人格+阿尼玛——三相女神是无意识心理学的实际问题。→ §306
- `[ns_cw9i_V_307_001]` `[trigger: definition_difficulty]` `[factor_trigger: jung_archetype AND jung_context]` `[role: 主干依赖]` 原型只在习惯性语境中清晰——抽象本质会使之模糊，需让其保持有机整体。→ §307"""
    normalized_text_zh: str = """"""
    subject: str = "§306-307 Kore的心理学对应物"
    factor_refs: list = ['engine_id', 'kore', 'psych_semantic', 'kore_self', 'psych_semantic', 'kore_anima', 'psych_semantic', 'context_dependent', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_306_307_kore的心理学对应物_001_L1",
    )
    version: str = "1.0.0"
