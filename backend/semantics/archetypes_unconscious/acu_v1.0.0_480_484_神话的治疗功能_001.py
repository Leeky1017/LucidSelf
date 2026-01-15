"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.545110
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
    semantic_id="acu_v1.0.0_480_484_神话的治疗功能_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 480484神话的治疗功能(SemanticEntry):
    """
    **原文** (§480-484, 行7484-7545):

> [480] From this point of view we can see why the myth of the trick...
    """
    
    original_text: str = """**原文** (§480-484, 行7484-7545):

> [480] From this point of view we can see why the myth of the trickster was preserved and developed: like many other myths, it was supposed to have a therapeutic effect. It holds the earlier low intellectual and moral level before the eyes of the more highly developed individual, so that he shall not forget how things looked yesterday...
>
> [484] The fact is, that this old trichotomous hierarchy of psychic contents (hylic, psychic, and pneumatic) represents the polaristic structure of the psyche, which is the only immediate object of experience. The unity of our psychic nature lies in the middle, just as the living unity of the waterfall appears in the dynamic connection between above and below.

**英文释义（主语言）**:

**神话的治疗效果**：
骗术师神话被保存和发展，因为像许多其他神话一样，它被认为具有**治疗效果**。它将早期低级的智力和道德水平保持在更高发展个体的眼前，使他**不忘昨天的样子**。

**人对神话的矛盾态度**：
存在两种相反的倾向：一方面**渴望摆脱早期状态**，另一方面**不愿忘记它**。我们喜欢想象我们不理解的东西不会以任何方式帮助我们，但并非总是如此。

**神话对无意识的直接作用**：
由于其**神圣性**，神话直接作用于无意识，不管是否被理解。神话的反复讲述并未早已过时，这可由其有用性解释。

**心灵的极性结构**：
古老的心理内容三层等级（hylic质料性、psychic心灵性、pneumatic精神性）代表心灵的**极性结构**——这是唯一直接的经验对象。我们心灵本性的**统一**在中间，正如瀑布的活的统一出现在上下之间的动态联系中。

**完整中文诠释（次语言）**:

**神话的治疗功能**：
骗术师神话被保存和发展，因为像许多其他神话一样，它被认为具有治疗效果。它将早期低级的智力和道德水平保持在更高发展个体的眼前，使他不忘昨天的样子。

**矛盾的心理态度**：
解释相当困难，因为存在两种相反的倾向：一方面渴望摆脱早期状态，另一方面不愿忘记它。这种顽固的拒绝遗忘不是偶然的。最开明的人也会为孩子设立圣诞树而不知这习俗意味什么。

**心灵极性与神话体验**：
古老的心理内容三层等级（质料性、心灵性、精神性）代表心灵的极性结构——唯一直接的经验对象。我们心灵本性的统一在中间，正如瀑布的活的统一出现在上下之间的动态联系中。神话的活效果在更高意识欢庆其自由独立时被体验——面对神话形象的自主性，却无法逃离其迷恋而必须向压倒性印象致敬。

**核心要点**:
- 骗术师神话有治疗效果——使人不忘昨天
- 两种矛盾倾向：渴望摆脱+不愿忘记
- 神话因神圣性直接作用于无意识
- 心灵三层等级=极性结构
- 心灵统一在中间=上下动态联系
- 神话形象=自主人格，参与观察者心灵

**叙事片段**:
- `[ns_cw9i_VII_480_001]` `[trigger: therapeutic_myth]` `[factor_trigger: jung_trickster AND jung_therapy]` `[role: 主干]` 骗术师神话有治疗效果——使人不忘早期状态，两种矛盾倾向并存。→ §480
- `[ns_cw9i_VII_484_001]` `[trigger: psychic_polarity]` `[factor_trigger: jung_psyche AND jung_structure]` `[role: 主干依赖]` 心灵极性结构——统一在中间，神话形象作为自主人格直接作用于无意识。→ §484"""
    normalized_text_zh: str = """"""
    subject: str = "§480-484 神话的治疗功能"
    factor_refs: list = ['engine_id', 'therapeutic_effect', 'psych_semantic', 'contradictory_attitude', 'psych_semantic', 'polaristic_structure', 'psych_semantic', 'middle_unity', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_480_484_神话的治疗功能_001_L1",
    )
    version: str = "1.0.0"
