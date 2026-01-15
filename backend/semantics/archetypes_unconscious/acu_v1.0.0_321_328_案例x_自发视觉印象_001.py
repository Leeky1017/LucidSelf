"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552784
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
    semantic_id="acu_v1.0.0_321_328_案例x_自发视觉印象_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 321328案例x自发视觉印象(SemanticEntry):
    """
    **原文** (§321-328, 行5408-5459):

> [321] i. "I saw a white bird with outstretched wings. It alighted ...
    """
    
    original_text: str = """**原文** (§321-328, 行5408-5459):

> [321] i. "I saw a white bird with outstretched wings. It alighted on the figure of a woman, clad in blue, who sat there like an antique statue. The bird perched on her hand, and in it she held a grain of wheat. The bird took it in its beak and flew into the sky again."
>
> [323] ii. A bull lifts a child up from the ground and carries it to the antique statue of a woman. A naked young girl with a wreath of flowers in her hair appears, riding on a white bull...
>
> [325] iii. "I saw a golden pig on a pedestal. Beast-like beings danced round it in a circle..."
>
> [327] iv. "I saw a beautiful youth with golden cymbals, dancing and leaping in joy and abandonment..."

**英文释义（主语言）**:

**案例X的四个幻象**：

**i. 白鸟与蓝衣女神**：
白鸟降落在一个穿蓝衣的女性形象上，她像古代雕像一样坐着。鸟停在她手上，她手中握着一粒麦子。鸟用喙衔走麦子，再次飞向天空。X为此画了一幅画：蓝衣、古朴简单的"母亲"形象，站在白色大理石基座上，大乳房强调其母性。

**ii. 公牛与孩童**：
公牛从地上举起孩童，带到古代女性雕像前。一个头戴花环的裸体少女出现，骑在白牛上。她拿起孩子像球一样抛向空中又接住。白牛载着两人去神庙。少女在这里以**欧罗巴**的形式出现。球类游戏与孩童是某种秘密仪式的母题，总与"儿童献祭"有关。

**iii. 金猪与仪式**：
金猪在基座上，兽形存在围绕它跳圆圈舞。挖一个洞在地上，发现水。一个金马车上的男人出现，跳入洞中前后摇摆像跳舞。X与他同步摇摆。他突然跳出洞，强暴她，使她怀孕。X与少女同一，少女也常以青年形式出现——**阿尼姆斯形象**，女性中男性元素的化身。青年和少女共同形成**配对**或**合一**，象征整体性的本质。

**iv. 金钹青年**：
美丽的青年拿着金钹，欢乐地跳舞。最后他倒在地上，脸埋入花中。然后他沉入一位非常老的母亲的怀中。过一会他起来跳入水中，像海豚一样嬉戏。跳过峡谷时青年跌入深渊。X一人继续，来到河边，白色海马带着金船等候她。在这个场景中X就是青年；因此他后来消失，留她作为故事的唯一女主角。她是"非常老的母亲"的孩子，也是海豚，是失落在峡谷中的青年，是显然被波塞冬期待的新娘。

**完整中文诠释（次语言）**:

案例X是一位中年女性，通过积极想象产生了一系列自发视觉印象。这些例子与梦的区别仅在于其更好的形式——内容是被清醒意识而非梦中意识感知的。

四个幻象展现了科瑞原型的多重面向：白鸟与麦子象征精神性的母亲形象；公牛与孩童涉及秘密仪式和儿童献祭母题；金猪仪式展现了阿尼姆斯的整合与受孕象征；金钹青年代表女性内在的男性成分的转化与消失。

母题的独特重叠和位移与神话变体中的情况大致相同。这印证了荣格关于原型普遍存在于人类心灵前意识构成中的理论。

**核心要点**:
- 案例X = 中年女性的积极想象系列
- 白鸟+麦子+蓝衣女神 = 母亲原型
- 公牛+孩童+球游戏 = 儿童献祭仪式母题
- 金猪+洞+受孕 = 阿尼姆斯整合
- 青年+少女 = 配对/合一 = 整体性象征
- 青年消失 = 阿尼姆斯整合后女性成为唯一主角
- 母题重叠位移 ≈ 神话变体

**叙事片段**:
- `[ns_cw9i_V_321_001]` `[trigger: case_x]` `[factor_trigger: jung_active_imagination AND jung_kore]` `[role: 主干]` 案例X白鸟幻象——麦子、蓝衣女神、母亲原型。→ §321-322
- `[ns_cw9i_V_323_001]` `[trigger: bull_child]` `[factor_trigger: jung_europa AND jung_sacrifice]` `[role: 主干依赖]` 公牛与孩童——欧罗巴形式、球游戏与儿童献祭母题。→ §323-324
- `[ns_cw9i_V_326_001]` `[trigger: syzygy]` `[factor_trigger: jung_animus AND jung_wholeness]` `[role: 主干依赖]` 青年与少女=配对/合一——阿尼姆斯整合象征整体性。→ §326"""
    normalized_text_zh: str = """"""
    subject: str = "§321-328 案例X：自发视觉印象"
    factor_refs: list = ['engine_id', 'white_bird', 'psych_semantic', 'wheat', 'psych_semantic', 'animus', 'psych_semantic', 'syzygy_coniunctio', 'psych_semantic', 'child_sacrifice', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_321_328_案例x_自发视觉印象_001_L1",
    )
    version: str = "1.0.0"
