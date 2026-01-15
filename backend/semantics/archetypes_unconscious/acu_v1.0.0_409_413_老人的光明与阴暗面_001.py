"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498251
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
    semantic_id="acu_v1.0.0_409_413_老人的光明与阴暗面_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 409413老人的光明与阴暗面(SemanticEntry):
    """
    **原文** (§409-413, 行6315-6380):

> [409] In certain primitive fairytales, the illuminating quality of...
    """
    
    original_text: str = """**原文** (§409-413, 行6315-6380):

> [409] In certain primitive fairytales, the illuminating quality of our archetype is expressed by the fact that the old man is identified with the sun. He brings a firebrand with him which he uses for roasting a pumpkin...
>
> [413] Just as all archetypes have a positive, favourable, bright side that points upwards, so also they have one that points downwards, partly negative and unfavourable, partly chthonic, but for the rest merely neutral. To this the spirit archetype is no exception.

**英文释义（主语言）**:

**老人与火/太阳的关联**：
在某些原始童话中，老人原型的**启明性质**通过将老人与太阳认同来表达。他带来一支火把用于烤南瓜。精神也有火焰面向——如旧约语言和五旬节奇迹所示。

**老人的道德考验**：
除了聪明、智慧和洞察，老人还因其**道德品质**而著名；更重要的是，他甚至**考验他人的道德品质**，使其礼物取决于这种考验。爱沙尼亚童话中的继女正是因为她的善良和服从而获得老人的金银奖赏。

**老人与上帝的联系**：
优越而乐于助人的老人形象引诱人将他与上帝联系起来。德国童话中的小灰胡子老人正是上帝本人，因为他"不能再继续看着魔鬼每晚制造的恶作剧"。

**原型的阴暗面**：
正如所有原型都有指向上方的正面、有利、光明的一面，它们也有指向下方的一面——部分是负面和不利的，部分是地下的(chthonic)，其余只是中性的。精神原型也不例外。老人的侏儒形式本身就暗示一种**限制**，暗示从地下世界冒出的**自然植被精灵**。

**老人的残缺**：
在一个巴尔干童话中，老人失去了一只眼睛——被翼状精灵Vili挖出。他因此失去了部分视力——即洞察力和启示——给了魔性的黑暗世界。这让人想起**奥西里斯失眼**（看到黑猪/邪恶兄弟Set时）或**沃坦献眼**（在米米尔泉边）。

**西伯利亚童话中的半边老人**：
西伯利亚童话中出现独腿、独手、独眼的灰胡子，用铁杖唤醒死人。故事名为"半边老人"——他的残缺表明他只由一半组成。另一半是看不见的，但以**谋杀者**的形状出现，寻求英雄的生命。最终英雄杀死了他持续的谋杀者，同时也杀死了半边老人——两个受害者的同一性由此揭示。因此老人可能是**他自己的对立面**——既是**生命赐予者**也是**死亡制造者**——"ad utrumque peritus"（精于两者），正如对赫尔墨斯的描述。

**完整中文诠释（次语言）**:

本节揭示精神原型的歧义性。老人可以被认同为太阳，具有启明性质，但也可以是残缺的、阴暗的、甚至邪恶的。

老人的火与太阳关联表明精神的启明功能。他考验他人的道德品质，使奖赏取决于考验。他可能与上帝认同——在德国童话中他就是上帝本人。

但精神原型也有阴暗面。老人可能失去一只眼睛（像奥西里斯或沃坦），表明他的洞察力部分被黑暗世界夺走。"半边老人"的故事最清楚地揭示了这一点：老人是他自己的对立面——既是生命赐予者也是死亡制造者，既是助人者也是谋杀者。这就是原型的根本歧义性。

**核心要点**:
- 老人与太阳/火 = 启明性质
- 老人考验道德品质 = 奖赏取决于考验
- 老人可被认同为上帝
- 原型有光明面和阴暗面
- 老人残缺（失眼）= 部分洞察力失于黑暗
- 半边老人 = 老人是自己的对立面
- 生命赐予者 = 死亡制造者
- "ad utrumque peritus" = 精于两者（如赫尔墨斯）

**叙事片段**:
- `[ns_cw9i_VI_409_001]` `[trigger: old_man_sun]` `[factor_trigger: jung_spirit AND jung_fire]` `[role: 主干]` 老人与太阳/火=启明性质——精神的火焰面向。→ §409
- `[ns_cw9i_VI_413_001]` `[trigger: archetype_dark_side]` `[factor_trigger: jung_spirit AND jung_shadow]` `[role: 主干]` 原型有光明面和阴暗面——老人可能是自己的对立面，既赐生也予死。→ §413"""
    normalized_text_zh: str = """"""
    subject: str = "§409-413 老人的光明与阴暗面"
    factor_refs: list = ['engine_id', 'fire_sun', 'psych_semantic', 'moral_test', 'psych_semantic', 'ambiguity', 'psych_semantic', 'osiris_wotan', 'psych_semantic', 'unity_of_opposites', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_409_413_老人的光明与阴暗面_001_L1",
    )
    version: str = "1.0.0"
