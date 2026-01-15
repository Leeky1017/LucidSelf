"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.519918
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
    semantic_id="acu_v1.0.0_第一节_x小姐案例与积极想象起源___525_528_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第一节X小姐案例与积极想象起源525528(SemanticEntry):
    """
    **原文** (¶525-528, 行8091-8148):

> [525] 在1920年代，我在美国认识了一位受过学术教育的女士——我们称她为X小姐——她研究心理学已有九年...她与阿尼姆斯(女性...
    """
    
    original_text: str = """**原文** (¶525-528, 行8091-8148):

> [525] 在1920年代，我在美国认识了一位受过学术教育的女士——我们称她为X小姐——她研究心理学已有九年...她与阿尼姆斯(女性中一切男性因素的人格化)的无意识等价物生活在一起...
>
> [527] 这幅画首先展示了她被囚禁的状态...心理学上，这种状态意味着被困在无意识中。她与母亲的关系不足，留下了某些黑暗的、需要发展的东西。
>
> [528] 由于X小姐自己发现了我长期使用的积极想象方法，我能够从画面指示的那一点开始处理问题：她被困在无意识中，期望从我这个巫师那里得到魔法帮助。

**英文释义**: 

X小姐案例展示个体化的开始：55岁学术女性，与阿尼姆斯生活（正面父亲情结），来苏黎世。她在丹麦（母亲的国家）时自发地想画画。第一幅画：困在岩石中、半身在地下，期望巫师(荣格)用魔杖解放。心理意义：困在无意识中，与母亲关系不足留下黑暗需发展。她自己发现了积极想象法。

**完整中文诠释**:

X小姐案例是个体化过程的经典案例研究：

**背景**：
- 55岁美国学术女性，研究心理学九年
- 与阿尼姆斯（无意识男性人格）生活——正面父亲情结
- 与母亲关系不佳——斯堪的纳维亚血统（母系）

**触发点**：
- 访问丹麦（母亲的国家）——唤起绘画冲动
- 绘画时出现幻想意象：自己半身困在岩石中
- 期望魔法师（荣格）用魔杖解放

**心理意义**：
- 困在岩石中 = 被困在无意识中
- 与母亲关系不足 = 黑暗的、需要发展的东西
- 她自己发现了积极想象法

**核心要点**:
- X小姐案例展示个体化的开始
- 阿尼姆斯与正面父亲情结相关
- 母亲国家的访问激发无意识内容
- 被困岩石 = 被困无意识 = 母亲关系未解决
- 积极想象法的自发发现

**叙事片段**:
- `[ns_cw9i_IX_001]` `[trigger: 个体化案例]` `[factor_trigger: jung_individuation AND jung_animus]` `[role: 主干]` X小姐与阿尼姆斯生活，访问母亲国家激发绘画——第一幅画显示被困岩石，期望魔法解放。→ ¶525-527"""
    normalized_text_zh: str = """"""
    subject: str = "第一节：X小姐案例与积极想象起源 (¶525-528)"
    factor_refs: list = ['animus_father_complex', 'mother_relation', 'stuck_in_unconscious', 'active_imagination']
    
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
        l1_anchor="acu_v1.0.0_第一节_x小姐案例与积极想象起源___525_528_001_L1",
    )
    version: str = "1.0.0"
