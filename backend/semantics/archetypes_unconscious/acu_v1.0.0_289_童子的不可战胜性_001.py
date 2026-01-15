"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535931
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
    semantic_id="acu_v1.0.0_289_童子的不可战胜性_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 289童子的不可战胜性(SemanticEntry):
    """
    **原文** (¶289, 行4850-4870):

> [289] It is a striking paradox in all child myths that the "child" is ...
    """
    
    original_text: str = """**原文** (¶289, 行4850-4870):

> [289] It is a striking paradox in all child myths that the "child" is on the one hand delivered helpless into the power of terrible enemies and in continual danger of extinction, while on the other he possesses powers far exceeding those of ordinary humanity. This is closely related to the psychological fact that though the child may be "insignificant," unknown, "a mere child," he is also divine. From the conscious standpoint we seem to be dealing with an insignificant content that has no releasing, let alone redeeming, character...
>
> The "child" is born out of the womb of the unconscious, begotten out of the depths of human nature, or rather out of living Nature herself. It is a personification of vital forces quite outside the limited range of our conscious mind; of ways and possibilities of which our one-sided conscious mind knows nothing; a wholeness which embraces the very depths of Nature. It represents the strongest, the most ineluctable urge in every being, namely the urge to realize itself.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Invincibility (不可战胜) | 无法战胜 | 童子的神性 | 悖论特征 |
| Urge to realize itself (自我实现冲动) | 实现自己的冲动 | 自然法则 | 个体化动力 |

**英文释义（主语言）**:

**童子神话的悖论**：
在所有童子神话中存在一个惊人的悖论：
- **一方面**："童子"无助地被交付给可怕敌人的力量，持续面临灭绝危险
- **另一方面**：他拥有远超普通人类的力量

**心理学事实的关联**：
虽然童子可能"微不足道"、未知、"只是个孩子"，但他也是**神圣的**。从意识的角度，我们似乎在处理一个没有释放、更不用说救赎特性的微不足道内容。

**神话强调的真相**：
神话强调事实并非如此，"童子"被赋予了超越的力量，尽管所有危险，将意外地渡过难关。

**童子的本质**：
- "童子"从无意识的子宫中诞生
- 从人性深处，或更确切地说，从活生生的自然本身孕育
- 是远超意识心智有限范围的**生命力量的人格化**
- 是我们片面意识心智一无所知的方式和可能性
- 是**拥抱自然最深处的整体性**
- 代表每个存在中**最强大、最不可逃避的冲动**——即**自我实现的冲动**

**完整中文诠释（次语言）**:

**童子神话的惊人悖论**：
在所有童子神话中存在一个惊人的悖论："童子"一方面无助地被交付给可怕敌人的力量，持续面临灭绝危险，另一方面他拥有远超普通人类的力量。

**与心理学事实的关联**：
这与一个心理学事实密切相关：虽然童子可能"微不足道"、未知、"只是个孩子"，但他也是神圣的。从意识的角度，我们似乎在处理一个没有释放、更不用说救赎特性的微不足道内容。意识心智困在其冲突情境中，交战力量似乎如此压倒性，以至于"童子"作为孤立内容与意识因素毫无关系。因此它很容易被忽视并落回无意识。

**神话的补偿性强调**：
然而，神话强调事实并非如此，"童子"被赋予了超越的力量，尽管所有危险，将意外地渡过难关。

**童子的深层本质**：
"童子"从无意识的子宫中诞生，从人性深处，或更确切地说，从活生生的自然本身孕育。它是远超意识心智有限范围的**生命力量的人格化**；是我们片面意识心智一无所知的方式和可能性；是**拥抱自然最深处的整体性**。

它代表每个存在中**最强大、最不可逃避的冲动**——即**自我实现的冲动**。可以说，它是无法做其他事情的能力的化身，配备了自然和本能的所有力量，而意识心智总是困在其假定的可以做其他事情的能力中。

**核心要点**:
- 童子神话的悖论：无助+危险 vs 超凡力量
- 童子微不足道却神圣
- 神话强调童子将意外渡过难关
- 童子从无意识/活生生的自然诞生
- 童子 = 生命力量的人格化
- 童子 = 拥抱自然深处的整体性
- 童子 = 自我实现冲动（最强大、不可逃避）

**叙事片段**:
- `[ns_cw9i_IV_289_001]` `[trigger: child_paradox]` `[factor_trigger: jung_child_archetype AND jung_invincibility]` `[role: 主干]` 童子神话悖论：无助+危险 vs 超凡力量——微不足道却神圣，将意外渡过难关。→ ¶289
- `[ns_cw9i_IV_289_002]` `[trigger: self_realization_urge]` `[factor_trigger: jung_child_archetype AND jung_self_realization]` `[role: 主干]` 童子代表最强大、最不可逃避的冲动——自我实现的冲动，是活生生自然的生命力量人格化。→ ¶289"""
    normalized_text_zh: str = """"""
    subject: str = "¶289 童子的不可战胜性"
    factor_refs: list = ['engine_id', 'helpless_powerful', 'psych_semantic', 'divine', 'psych_semantic', 'urge_to_realize', 'psych_semantic', 'vital_forces', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_289_童子的不可战胜性_001_L1",
    )
    version: str = "1.0.0"
