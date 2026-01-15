"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.801308
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
    semantic_id="mlxj_v1.0.0_1_姤合总论_姤合类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1姤合总论姤合类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

梦与他人交合，主为人干蛊，小有悔，无大咎，厉，终吉。交接男子，主失财。与妇交者，凶。与男人交者吉。玩弄阴户者，主争詈之灾。阴阳相对，抵推不合，必有大难。抱怀...
    """
    
    original_text: str = """#### 原文（source_text）

梦与他人交合，主为人干蛊，小有悔，无大咎，厉，终吉。交接男子，主失财。与妇交者，凶。与男人交者吉。玩弄阴户者，主争詈之灾。阴阳相对，抵推不合，必有大难。抱怀不乱，主欢乐喜庆，和而不流，万物回春之兆。合入不终者，作事反复，谋利不成。联梦美女交搆，主祟厉，损精，宜正心以辟邪，则诸淫鬼远之而不能相侵。

#### 规范化释义（primary_lang_explained）

梦与他人交合，主为人干蛊（替人办事），小有悔恨，无大过错，虽有危险，终究吉利。

- 交接男子：主失财
- 与妇人交：凶
- 与男人交：吉
- 玩弄阴户：主争吵之灾
- 阴阳相对抵推不合：必有大难
- 抱怀不乱：主欢乐喜庆，和而不流，万物回春之兆
- 合入不终：作事反复，谋利不成
- 连续梦见美女交媾：主邪祟，损精气，宜正心辟邪

#### 完整对等诠释（secondary_lang_full）

Dreaming of intercourse with others signifies doing someone's bidding—minor regrets but no major fault, though dangerous, ultimately auspicious.

- Intercourse with a man: loss of wealth
- Intercourse with a woman: inauspicious
- Intercourse with a man (for women): auspicious
- Playing with private parts: quarrels and disputes
- Yin-yang opposition without union: great difficulty ahead
- Embracing without disorder: joy and celebration, harmony without excess, sign of all things reviving
- Union without completion: affairs reverse, profits fail
- Recurring dreams of beautiful women: demonic influence, depletes essence—rectify the heart to ward off evil

#### 核心要点

- 姤合梦=为人干蛊=替人办事
- **性别分化**：男交男失财，女交男吉，交妇凶
- 抱怀不乱=和谐之兆=万物回春
- 合入不终=有始无终=谋事不成
- 连梦美女=邪祟损精=需正心辟邪

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v10_001]` `[trigger: 人事梦象]` `[factor_trigger: bagua_yinyang AND dream_qingou AND taixing AND dream_lianjimeinv]` `[role: 人事类]` 八卦阴阳、亲耦、胎形、连梦美女等人事梦象。 → 《梦林玄解·卷十》#人事"""
    normalized_text_zh: str = """"""
    subject: str = "1 姤合总论（姤合类首条·完整精校）"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_姤合总论_姤合类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
