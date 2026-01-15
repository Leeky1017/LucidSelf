"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498286
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
    semantic_id="acu_v1.0.0_426_434_三与四的对立与心理功能_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 426434三与四的对立与心理功能(SemanticEntry):
    """
    **原文** (§426-434, 行6603-6790):

> [426] Between the three and the four there exists the primary oppo...
    """
    
    original_text: str = """**原文** (§426-434, 行6603-6790):

> [426] Between the three and the four there exists the primary opposition of male and female, but whereas fourness is a symbol of wholeness, threeness is not...
>
> [430] Turning now to quite another field, the realm of psychological experience, we know that three of the four functions of consciousness can become differentiated...
>
> [434] The archetype of the spirit in this, be it said, by no means primitive fairytale is expressed theriomorphically as a system of three functions which is subordinated to a unity...

**英文释义（主语言）**:

**三与四的对立**：
三与四之间存在**男与女的基本对立**。但四是**整体性**的象征，三则不是。根据炼金术，三表示**极性**——一个三元组总是预设另一个，正如高预设低、光预设暗、善预设恶。在能量术语中，极性意味着电位，而有电位就有电流、事件流动的可能，因为对立的张力追求平衡。

**Maria的公理**：
如果将四位一体想象为被对角线一分为二的正方形，就得到两个顶点指向相反方向的三角形。因此可以隐喻地说，如果四位一体象征的整体性被分成相等的两半，就产生两个对立的三元组。三可以从四推导出来。Maria的谜语公理是："从第三产生第一作为第四"——当第三产生第四时，它立刻产生统一。

**心理功能与三/四**：
转向心理经验领域：四种意识功能中有三种可以分化（即变得有意识），而另一种仍与母体——无意识——相连，被称为**劣势功能**。它是最英勇意识的阿喀琉斯之踵：强者在某处是弱的，聪明者在某处是愚蠢的，好人在某处是坏的。

**优势功能与辅助功能**：
实际上只有一种功能或多或少成功地分化，被称为**优势功能**或**主功能**，与外倾或内倾一起构成意识态度的类型。这个功能与一个或两个**部分分化的辅助功能**相关联。第四种**劣势功能**则被证明对我们的意志不可及——时而作为捉弄人的小鬼，时而作为机器神(deus ex machina)出现，但总是自行来去。

**童话揭示心理结构**：
童话以非凡的清晰度揭示了精神原型的本质**对立性**，同时展示了所有对立都指向**更高意识**这一伟大目标的令人困惑的游戏。年轻牧猪人从动物水平攀登到世界树顶端，在光的上界发现他被俘虏的阿尼玛——高贵的公主——象征着意识的上升。

**完整中文诠释（次语言）**:

本节是Essay VI最深刻的部分，将童话象征与心理学功能理论联系起来。

三与四的对立反映男女对立：四象征整体性，三象征极性。每个三元组预设其对立三元组。Maria的炼金术公理"从第三产生第一作为第四"意味着：当三产生四时产生统一。

这与心理功能理论完美对应：四种功能（思维、情感、感觉、直觉）中三种可分化，一种（劣势功能）仍在无意识中。劣势功能不受意志控制，时而作为小鬼，时而作为神明出现。

童话结构反映这一心理结构：英雄代表优势功能，邪恶猎人代表劣势功能，它们最终在英雄身上合一。四条腿的马战胜三条腿——整体性战胜残缺。公主（阿尼玛）代表无意识中不可完全同化的那部分。

**核心要点**:
- 三vs四 = 男vs女 = 极性vs整体
- 每个三元组预设其对立三元组
- Maria公理：三产生四时产生统一
- 四种心理功能：三可分化，一为劣势
- 劣势功能 = 阿喀琉斯之踵
- 劣势功能不受意志控制
- 英雄 = 优势功能，猎人 = 劣势功能
- 四条腿 > 三条腿 = 整体性战胜残缺
- 公主/阿尼玛 = 永不可完全同化的无意识

**叙事片段**:
- `[ns_cw9i_VI_426_001]` `[trigger: three_four]` `[factor_trigger: jung_quaternity AND jung_triad]` `[role: 主干]` 三vs四=极性vs整体——每个三元组预设其对立。→ §426
- `[ns_cw9i_VI_430_001]` `[trigger: functions]` `[factor_trigger: jung_consciousness AND jung_functions]` `[role: 主干]` 四种心理功能——三可分化，一为劣势，阿喀琉斯之踵。→ §430
- `[ns_cw9i_VI_434_001]` `[trigger: hero_hunter]` `[factor_trigger: jung_superior AND jung_inferior]` `[role: 主干依赖]` 英雄=优势功能，猎人=劣势功能——最终合一。→ §434"""
    normalized_text_zh: str = """"""
    subject: str = "§426-434 三与四的对立与心理功能"
    factor_refs: list = ['engine_id', 'three_vs_four', 'psych_semantic', 'axiom_of_maria', 'psych_semantic', 'four_functions', 'psych_semantic', 'inferior_function', 'psych_semantic', 'hero_superior', 'psych_semantic', 'hunter_inferior', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_426_434_三与四的对立与心理功能_001_L1",
    )
    version: str = "1.0.0"
