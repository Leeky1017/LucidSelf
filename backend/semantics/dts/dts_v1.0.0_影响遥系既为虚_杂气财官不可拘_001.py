"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997378
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
    semantic_id="dts_v1.0.0_影响遥系既为虚_杂气财官不可拘_001",
    book_id="dts",
    engine_id="bazi"
)
class 影响遥系既为虚杂气财官不可拘(SemanticEntry):
    """
    - **原文（source_text）**：
  影响遥系既为虚，杂气财官不可拘。

- 原注（原文注解）：
  　　飞天合禄之类，固为影响遥系，而非格矣，如四季月生人，只当取土为格，不可言杂气财官，...
    """
    
    original_text: str = """- **原文（source_text）**：
  影响遥系既为虚，杂气财官不可拘。

- 原注（原文注解）：
  　　飞天合禄之类，固为影响遥系，而非格矣，如四季月生人，只当取土为格，不可言杂气财官，戊己日生于四季，当看人元透出天干者取格，不可概以杂气论之，至于建禄阳刃，亦当看月令透于天干者取格，若不合形象方局，又无格可言，只取用神，用神又无取，只得轻轻泛泛，看其大势，以皮面上断穷通，不可执其格也。

- 分字分词释义：
  - 影响遥系：飞天合禄、远隔相合等“牵连关系”，力量遥远而不真切。
  - 杂气财官：以四季土或支中杂藏之财官，泛安“杂气财官格”的做法。
  - 不可拘：不可拘泥于格名与遥系之象，而忘局中大势与用神实情。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 影响遥系 | Remote Influence | 飞天合禄等远隔关系 | Distant indirect connection | yingxiang_yaoxi | new_candidate |
| 杂气财官 | Mixed Season Wealth-Officer | 四季月杂气中之财官 | Wealth/Officer in seasonal earth | zaqi_caiguan | new_candidate |
| 不可拘 | Do Not Cling | 不可拘泥于格名 | Do not be rigid about labels | bukeju | new_candidate |
| 四季月 | Four Seasons Months | 辰戌丑未月 | Chen, Xu, Chou, Wei months | sijiyue | existing |
| 建禄阳刃 | Jianlu and Yangren | 建禄格与阳刃格 | Prosperous and Blade patterns | jianlu_yangren | existing |
| 无格 | No Pattern | 无真格可立 | Lacking distinct structure | wuge | new_candidate |

- **规范化释义（primary_lang_explained）**：
  飞天合禄等遥合只是“影响遥系”，不能作为立格的根基。四季月生人，应先取土为格；戊己日生于四季，更当看支中人元透出天干者立格，不可一概称为“杂气财官格”。建禄、阳刃之格，同样要看月令所藏之神是否透干。当形象、方局皆不成，且月令用事之神不透干以成格时，只能退而求其次：单取用神、看大势，“轻轻泛泛”断其穷通，而不可执着某个格名自欺。

- **次语种完整诠释（secondary_lang_full）**:  
  Remote-influence影响遥系 (飞天合禄) is虚 insubstantial; 杂气财官 mixed-season-officers不可拘 avoid-rigid-labeling: 真格 true-pattern requires近实 near-rooted月令透干 not遥合 remote-links—四季月 four-seasons先取土 prioritize-earth; 建禄阳刃 jianlu-yangren看透干 stem-manifestation not执格名 forcing-labels; 无格时 when-no-pattern退居用神+大势 yongshen-plus-trend avoiding伪格迷惑 pseudo-pattern-confusion."""
    normalized_text_zh: str = """"""
    subject: str = "影响遥系既为虚，杂气财官不可拘。"
    factor_refs: list = []
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_影响遥系既为虚_杂气财官不可拘_001_L1",
    )
    version: str = "1.0.0"
