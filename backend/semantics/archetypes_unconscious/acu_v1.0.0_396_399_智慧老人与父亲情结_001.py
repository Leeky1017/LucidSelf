"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498211
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
    semantic_id="acu_v1.0.0_396_399_智慧老人与父亲情结_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 396399智慧老人与父亲情结(SemanticEntry):
    """
    **原文** (§396-399, 行6058-6134):

> [396] The psychic manifestations of the spirit indicate at once th...
    """
    
    original_text: str = """**原文** (§396-399, 行6058-6134):

> [396] The psychic manifestations of the spirit indicate at once that they are of an archetypal nature—in other words, the phenomenon we call spirit depends on the existence of an autonomous primordial image which is universally present in the preconscious makeup of the human psyche...
>
> [398] The figure of the wise old man can appear so plastically, not only in dreams but also in visionary meditation (or what we call "active imagination"), that, as is sometimes apparently the case in India, it takes over the role of a guru...

**英文释义（主语言）**:

**精神的原型本质**：
精神的心理显现立即表明它们具有**原型本质**——换言之，我们称为精神的现象依赖于一个**自主的原初意象**的存在，这个意象普遍存在于人类心灵的**前意识构成**中。

**父亲情结的精神性**：
某种父亲情结具有"精神"性质，因为父亲意象产生陈述、行动、倾向、冲动、意见等，人们很难否认其"精神"属性。在梦中，总是从父亲形象发出**决定性的信念、禁令和智慧忠告**。

**精神的形象化**：
精神最常显现为**智慧老人**的形象。有时角色由"真正的"精灵扮演，即死者的鬼魂，或更罕见地，由怪诞的侏儒形象或会说话的动物扮演。

**智慧老人的出现时机**：
精神原型以人、妖精或动物形式总是在需要**洞察、理解、好建议、决心、计划**等但靠自己资源无法调动时出现。原型补偿这种精神缺失状态。

**完整中文诠释（次语言）**:

**精神的原型依据**：
精神的心理显现立即表明它们具有原型本质——我们称为精神的现象依赖于一个自主的原初意象的存在，这个意象普遍存在于人类心灵的前意识构成中。荣格最初是在研究病人的梦时遇到这个问题的。

**父亲情结与精神**：
某种父亲情结具有"精神"性质。在男性中，正面的父亲情结常产生对权威的轻信和对精神教条和价值的服从倾向；在女性中，它诱发最活跃的精神志向和兴趣。在梦中，总是从父亲形象发出决定性的信念、禁令和智慧忠告。

**智慧老人的多种形式**：
精神最常显现为智慧老人的形象，象征精神因素。有时由死者的鬼魂或怪诞的侏儒或会说话的动物扮演。智慧老人在梦中以魔术师、医生、祭司、教授、祖父或任何拥有权威的人的面目出现。

**核心要点**:
- 精神具有原型本质——自主原初意象
- 父亲情结常具精神性质
- 梦中父亲形象发出决定性信念、禁令、智慧忠告
- 智慧老人 = 精神原型最常见形式
- 其他形式：鬼魂、侏儒、会说话动物
- 出现时机：需要洞察、理解、好建议但自己无法调动时

**叙事片段**:
- `[ns_cw9i_VI_396_001]` `[trigger: spirit_archetype]` `[factor_trigger: jung_spirit AND jung_wise_old_man]` `[role: 主干]` 精神具原型本质——智慧老人是最常见形式，在需要洞察理解但自己无法调动时出现。→ §396-398"""
    normalized_text_zh: str = """"""
    subject: str = "§396-399 智慧老人与父亲情结"
    factor_refs: list = ['engine_id', 'wise_old_man', 'psych_semantic', 'father_complex', 'psych_semantic', 'compensate_deficiency', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_396_399_智慧老人与父亲情结_001_L1",
    )
    version: str = "1.0.0"
