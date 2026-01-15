"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498264
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
    semantic_id="acu_v1.0.0_414_418_老人的邪恶面向_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 414418老人的邪恶面向(SemanticEntry):
    """
    **原文** (§414-418, 行6382-6460):

> [414] In these circumstances, whenever the "simple" and "kindly" o...
    """
    
    original_text: str = """**原文** (§414-418, 行6382-6460):

> [414] In these circumstances, whenever the "simple" and "kindly" old man appears, it is advisable for heuristic and other reasons to scrutinize the context with some care...
>
> [415] The old man, then, has an ambiguous elfin character—witness the extremely instructive figure of Merlin—seeming, in certain of his forms, to be good incarnate and in others an aspect of evil...
>
> [417] In another Balkan tale, there is a variant of our motif... The old man, appearing at first as a tree-numen, is obviously connected with the sister. He is a murderer... This amounts to saying that the sister is animus-possessed.

**英文释义（主语言）**:

**审慎考察老人形象**：
在这些情况下，每当"单纯"和"善良"的老人出现时，出于启发式和其他原因，最好仔细审查语境。例如在爱沙尼亚童话中，有嫌疑认为正好在场的乐于助人的老人事先悄悄偷走了牛，以便给他的保护对象一个逃跑的极好理由。

**老人的精灵歧义性**：
因此，老人具有**歧义的精灵性格**——以极具启发性的**梅林形象**为证——在某些形式中似乎是善的化身，在另一些形式中则是恶的面向。他还可以是邪恶的魔法师，出于纯粹的利己主义，为恶而作恶。

**西伯利亚童话中的邪恶精灵**：
西伯利亚童话中他是邪恶精灵，"头上有两个湖，湖中有两只鸭子在游泳"。他以人肉为食。"造物主"命令英雄去找狗，但英雄被困在暴风雪中，不得不在邪恶精灵的小屋中避难。而"造物主"的父亲被称为"自创者"——因为他创造了自己。虽然故事没有说老人引诱英雄进入小屋以满足饥饿，但可以推测是一种非常特殊的精神使狗们举行宴会然后逃跑，使英雄被困在暴风雪中，驱使他进入邪恶老人的怀抱。

**巴尔干童话中的阿尼姆斯附身**：
巴尔干童话中，老人首先以**树精**出现，显然与国王的姐妹有关。他是谋杀者。他被指控通过将一整座城市变成铁——即使之不动、僵硬、锁住——来施魔法于它。他还囚禁了国王的姐妹，不让她回到亲人身边。这等于说姐妹被**阿尼姆斯附身**。因此老人应被视为她的阿尼姆斯。

**神圣婚姻的向对立面转化**：
这个大胆的**向对立面转化**(enantiodromia)不仅意味着老人的年轻化和转化，还暗示善与恶之间的秘密内在关系，反之亦然。故事中原型参与个体化过程，最终以神圣婚姻(hieros gamos)暗示性地结束。

**完整中文诠释（次语言）**:

本节深入探讨老人形象的邪恶面向。当"单纯善良"的老人出现时，需要仔细审查语境——他可能事先设置了困境以便提供帮助。

老人的精灵性格是歧义的——梅林形象是最好的例证。他可以是善的化身，也可以是恶的面向，甚至可以是纯粹的邪恶魔法师。西伯利亚童话中的邪恶精灵以人肉为食，而"造物主"本身也参与了引导英雄进入陷阱的计划——这提出了神义论的棘手问题。

巴尔干童话中老人以树精出现，囚禁了国王的姐妹。这被解释为阿尼姆斯附身——老人是姐妹的阿尼姆斯。但故事最终以神圣婚姻结束，老人转化为年轻英俊的新郎——这个向对立面的转化暗示善恶之间的秘密内在关系。

**核心要点**:
- 审慎审查"善良老人"的语境
- 老人可能事先设置困境
- 老人 = 歧义的精灵性格（梅林为证）
- 老人可以是纯粹邪恶的魔法师
- "造物主"也可能参与邪恶计划
- 老人 = 女性的阿尼姆斯（阿尼姆斯附身）
- 向对立面转化(enantiodromia) = 老人年轻化
- 神圣婚姻(hieros gamos) = 个体化的结局
- 善恶之间存在秘密内在关系

**叙事片段**:
- `[ns_cw9i_VI_414_001]` `[trigger: scrutinize_context]` `[factor_trigger: jung_old_man AND jung_evil]` `[role: 主干]` 审慎审查"善良老人"语境——他可能事先设置困境。→ §414
- `[ns_cw9i_VI_415_001]` `[trigger: merlin]` `[factor_trigger: jung_spirit AND jung_ambiguity]` `[role: 主干依赖]` 老人=歧义精灵性格——梅林为证，善恶皆可。→ §415
- `[ns_cw9i_VI_417_001]` `[trigger: animus_possession]` `[factor_trigger: jung_old_man AND jung_animus]` `[role: 主干依赖]` 老人=女性的阿尼姆斯——阿尼姆斯附身导致囚禁。→ §417"""
    normalized_text_zh: str = """"""
    subject: str = "§414-418 老人的邪恶面向"
    factor_refs: list = ['engine_id', 'scrutinize', 'psych_semantic', 'merlin', 'psych_semantic', 'animus_possession', 'psych_semantic', 'enantiodromia', 'psych_semantic', 'hieros_gamos', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_414_418_老人的邪恶面向_001_L1",
    )
    version: str = "1.0.0"
