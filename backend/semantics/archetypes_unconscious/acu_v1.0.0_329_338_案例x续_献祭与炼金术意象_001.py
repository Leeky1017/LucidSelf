"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552802
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
    semantic_id="acu_v1.0.0_329_338_案例x续_献祭与炼金术意象_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 329338案例x续献祭与炼金术意象(SemanticEntry):
    """
    **原文** (§329-338, 行5461-5530):

> [329] v. There now follows a sacrifice of sheep, during which a ga...
    """
    
    original_text: str = """**原文** (§329-338, 行5461-5530):

> [329] v. There now follows a sacrifice of sheep, during which a game of ball is likewise played with the sacrificial animal...
>
> [330] vi. After that X comes to a den of snakes, and the snakes wind all round her.
>
> [331] vii. In a den of snakes beneath the sea there is a divine woman, asleep...
>
> [333] viii. As X emerged from the depths and saw the light again, she experienced a kind of illumination: white flames played about her head as she walked through waving fields of grain.

**英文释义（主语言）**:

**v. 羊献祭**：
献祭羊，同时用牺牲动物玩球游戏。参与者用牺牲血涂抹自己，之后在搏动的血中沐浴。X随后转化为一株植物。

**vi. 蛇穴**：
X来到蛇穴，蛇缠绕在她全身。

**vii. 海底蛇穴中的神圣女性**：
海底蛇穴中有一位沉睡的神圣女性（画中她比其他人大得多）。她穿着血红色衣服，只遮住下半身。她皮肤黝黑，嘴唇丰满红润，似乎有极大的身体力量。她亲吻X（显然处于少女角色），并将她作为礼物交给站在旁边的许多男人。这个**地母女神**是许多现代幻想中出现的典型**大地母亲**。

**viii. 光明与启示**：
X从深处浮出重见光明时，经历了一种**启示**：当她穿过摇曳的麦田时，白色火焰在她头上舞动。

随着这幅画面，母亲篇章结束。虽然没有任何已知神话被重复的丝毫痕迹，母题及其联系对我们来说从神话中都很熟悉。这些图像自发呈现，不基于任何有意识的知识。

**荣格自己的梦**：
荣格描述了自己多年前的一个梦：攀登一座大山，到达以为是山顶的地方却发现自己站在高原边缘，真正的山峰在远处。夜色降临，他在对面黑暗的山坡上看到一条带有金属光泽的溪流流下，两条道路像蛇一样蜿蜒而上，一条向左，一条向右。山顶右边有一家旅馆。溪流在左下方流淌，有一座桥横跨其上。

不久后他在一本晦涩的炼金术论著中发现了以下"寓言"。Gerard Dorn描述了"世界的漫游，我们称之为错误之路"和"真理之路"。左边有工业和医院，右边有智慧的溪流。

**完整中文诠释（次语言）**:

案例X的幻象系列继续深入无意识领域：羊献祭和血浴代表原始仪式的内化；蛇穴象征进入无意识深处；海底神圣女性是地母原型的显现；最后的光明和麦田中的白火是启示和精神觉醒的象征。

荣格用自己的梦作为例子，说明即使是看似"个人"的梦意象，经分析后也会显示其原型本质。他的山和溪流梦与16世纪炼金术士Gerard Dorn的寓言惊人相似，虽然荣格做梦时对这本书一无所知。这证明了原型意象可以跨越时代和个人不断再现。

**核心要点**:
- 羊献祭+血浴 = 原始仪式内化
- 蛇穴 = 进入无意识深处
- 海底神圣女性 = 地母原型
- 光明+白火+麦田 = 启示和精神觉醒
- 母亲篇章结束 = 完成无意识下降
- 荣格自己的梦 = 原型跨时代再现的证据
- 炼金术寓言的平行 = 无意识知识的验证

**叙事片段**:
- `[ns_cw9i_V_331_001]` `[trigger: earth_mother]` `[factor_trigger: jung_chthonic_goddess]` `[role: 主干]` 海底蛇穴神圣女性=地母原型——皮肤黝黑、红唇、巨大力量。→ §331-332
- `[ns_cw9i_V_333_001]` `[trigger: illumination]` `[factor_trigger: jung_light AND jung_grain]` `[role: 主干依赖]` 光明与麦田=启示——白火在头上舞动，母亲篇章结束。→ §333-334"""
    normalized_text_zh: str = """"""
    subject: str = "§329-338 案例X续：献祭与炼金术意象"
    factor_refs: list = ['engine_id', 'sacrifice_blood', 'psych_semantic', 'snake_den', 'psych_semantic', 'earth_mother', 'psych_semantic', 'illumination', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_329_338_案例x续_献祭与炼金术意象_001_L1",
    )
    version: str = "1.0.0"
