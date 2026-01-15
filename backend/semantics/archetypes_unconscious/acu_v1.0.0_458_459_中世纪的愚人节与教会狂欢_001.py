"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.545070
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
    semantic_id="acu_v1.0.0_458_459_中世纪的愚人节与教会狂欢_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 458459中世纪的愚人节与教会狂欢(SemanticEntry):
    """
    **原文** (§458-459, 行7164-7196):

> It is just this transformation of the meaningless into the meaning...
    """
    
    original_text: str = """**原文** (§458-459, 行7164-7196):

> It is just this transformation of the meaningless into the meaningful that reveals the trickster's compensatory relation to the "saint." In the early Middle Ages, this led to some strange ecclesiastical customs based on memories of the ancient saturnalia...
>
> [459] It is not surprising that this veritable witches' sabbath was uncommonly popular, and that it required considerable time and effort to free the Church from this pagan heritage.

**英文释义（主语言）**:

**骗术师与圣人的补偿关系**：
正是这种**无意义转化为有意义**的过程揭示了骗术师与"圣人"的**补偿关系**。

**中世纪教会习俗**：
在中世纪早期，这导致一些基于古代农神节记忆的奇特教会习俗。大多在基督诞生后的几天——即新年——庆祝，有唱歌和跳舞：
- 祭司、低级神职人员、儿童和副执事的**tripudia（舞蹈）**在教堂举行
- 在诸圣婴孩日选举**儿童主教**(episcopus puerorum)，穿上主教服
- 在喧闹的欢庆中访问大主教宫殿，从窗口赐予主教祝福

**愚人节的堕落**：
到12世纪末，副执事的舞蹈堕落为真正的**愚人节**(festum stultorum)。1198年的报告说，在巴黎圣母院的割礼节上，"如此多的可憎之事和可耻行为"被犯下，圣地被"不仅是下流笑话，甚至是流血"所亵渎。

**教廷的谴责**：
教皇英诺森三世徒劳地谴责"使神职人员成为笑柄的笑话和疯狂"以及"他们戏剧表演的无耻狂热"。250年后（1444年），巴黎神学院致所有法国主教的信仍在谴责这些节日，在那里"甚至祭司和神职人员选举大主教或主教或教皇，称他为愚人教皇"。

**完整中文诠释（次语言）**:

**骗术师与圣人的互补**：
正是这种无意义转化为有意义的过程揭示了骗术师与"圣人"的补偿关系。这个关系导致中世纪早期一些基于古代农神节记忆的奇特教会习俗。

**愚人节的仪式**：
节日大多在基督诞生后的几天庆祝，有唱歌和跳舞。祭司、神职人员、儿童的舞蹈在教堂举行。选举儿童主教，穿上主教服，在喧闹中访问大主教宫殿赐予祝福。同样的事情发生在其他祭司等级的舞蹈中。

**愚人节的堕落与持续**：
到12世纪末，副执事的舞蹈堕落为真正的愚人节。在神圣仪式中间，戴着怪诞面具、装扮成女人、狮子和小丑的化装者表演舞蹈，在唱诗班唱下流歌曲，在祭坛角落吃油腻食物，玩骰子游戏，烧用旧鞋皮做的臭香，在整个教堂跑跳。这真正的女巫安息日异常流行，教会花费相当长的时间和努力才摆脱这一异教遗产。

**核心要点**:
- 骗术师与圣人 = 补偿关系
- 无意义→有意义 = 骗术师功能
- 中世纪愚人节 = 古代农神节的教会版
- 儿童主教、愚人教皇 = 等级颠倒仪式
- 教堂中的舞蹈、下流行为、化装 = 骗术师表现
- 教会花长时间摆脱这一异教遗产

**叙事片段**:
- `[ns_cw9i_VII_458_002]` `[trigger: trickster_saint]` `[factor_trigger: jung_trickster AND jung_saint]` `[role: 主干]` 骗术师与圣人=补偿关系——无意义转化为有意义揭示这一关系。→ §458
- `[ns_cw9i_VII_459_001]` `[trigger: fools_feast]` `[factor_trigger: jung_trickster AND jung_church]` `[role: 主干依赖]` 中世纪愚人节=古代农神节的教会版——等级颠倒、下流行为、化装舞蹈。→ §459"""
    normalized_text_zh: str = """"""
    subject: str = "§458-459 中世纪的愚人节与教会狂欢"
    factor_refs: list = ['engine_id', 'trickster_saint_compensation', 'psych_semantic', 'festum_stultorum', 'psych_semantic', 'episcopus_puerorum', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_458_459_中世纪的愚人节与教会狂欢_001_L1",
    )
    version: str = "1.0.0"
