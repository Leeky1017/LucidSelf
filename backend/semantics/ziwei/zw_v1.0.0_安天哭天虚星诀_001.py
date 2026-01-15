"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654211
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
    semantic_id="zw_v1.0.0_安天哭天虚星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天哭天虚星诀(SemanticEntry):
    """
    **主题**：论本生年支安天哭天虚。

#### 原文（断句）：

天哭天虚起午宫，午宫起子两分踪。哭逆巳兮虚顺未，数到生年便居中。

#### 分字分词释义：

- **天哭**：杂曜之一，主悲伤、...
    """
    
    original_text: str = """**主题**：论本生年支安天哭天虚。

#### 原文（断句）：

天哭天虚起午宫，午宫起子两分踪。哭逆巳兮虚顺未，数到生年便居中。

#### 分字分词释义：

- **天哭**：杂曜之一，主悲伤、哭泣、丧事。
- **天虚**：杂曜之一，主虚空、落空、幻灭。
- **起午宫**：以午宫为基准点。
- **午宫起子**：午宫代表子年。
- **两分踪**：天哭、天虚分别向两个方向计算。
- **哭逆巳**：天哭从巳宫逆时针数。
- **虚顺未**：天虚从未宫顺时针数。
- **数到生年便居中**：数到命主生年地支的位置安放。

#### 安星规则：

- 午宫起子年
- **天哭**：从巳宫逆数至生年
- **天虚**：从未宫顺数至生年

#### 规范化释义（primary_lang_explained）：

天哭、天虚是一对与悲伤、空虚相关的杂曜，两星都以生年地支为锚点，在午宫起子年之后，一逆一顺地分布在十二支上。歌诀“午宫起子两分踪，哭逆巳兮虚顺未”所示，是先在午宫标记子年起点，再将悲泣之星天哭自巳宫逆数、生年止步，将空虚之星天虚自未宫顺行、生年收尾，好像在岁支周围画出一对“哀伤与虚无的交叉路口”。

实务中，天哭、天虚多不单独用来判断凶灾，而是标记在哪些宫位更容易出现哭泣送别、情绪低落与落空感等课题：落在父母、田宅等宫，往往对应家庭中的丧事、照顾或离散经验；落在命宫、福德宫，则强调命主对悲伤、空虚主题格外敏感，需要更主动学习情绪调节与心理复原力。当它们与丧门、白虎等凶煞同会时，才会把“悲伤与虚空”的象征推向更具事件性的层级。

#### 完整对等诠释（secondary_lang_full·19天哭天虚）：

Tianku and Tianxu operate as a paired system of sorrow and emptiness. Both are anchored by the earthly branch of the birth year, but the technique first sets a reference at Wu, treats it as the seat of Zi year, and then sends the two stars off in opposite directions: Tianku is counted backward from Si, Tianxu forward from Wei, both landing on the native’s year branch. The result is that the chart carries two sensitive points where the story of grief and the story of hollowness tend to gather.

Interpretively, these stars do not by themselves decree tragedy. Instead, they show where the person is more exposed to experiences of farewell, mourning, anticlimax or inner depletion. When Tianku or Tianxu fall into parental and property houses, the themes often involve family separations, caring for elders or repeatedly moving house with a sense of loss. When they touch the Life or Fortune palaces, they describe a temperament that feels sadness and meaninglessness more keenly than most. Only when they combine with heavier malefics such as Sangmen and Baihu do they move from psychological weather into concrete events like funerals, medical crises or periods of harsh emotional collapse.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天哭 | Tianku | 午宫起子巳逆数主悲泣丧事 | From Si backward grief sorrow | star_tianku | existing |
| 天虚 | Tianxu | 午宫起子未顺数主空虚 | From Wei forward hollowness vacancy | star_tianxu | existing |
| 午宫起子年 | Wu-Anchored Year | 以午宫视为子年起点 | Wu as anchor for Zi year | principle_wugongqizinian | existing |
| 哭虚一逆一顺 | One-Reverse-One-Forward | 天哭逆行天虚顺行对向 | Tianku backward Tianxu forward | algo_kuxuyinishun | new_candidate |

#### 详细解说：

天哭与天虚是紫微斗数杂曜系统中与情绪相关的一对星曜，天哭主悲伤哭泣，天虚主虚空幻灭，二者都依据生年地支定位。

**算法原理**：
- 以午宫为子年的参照点
- 天哭从巳宫逆时针数到生年地支
- 天虚从未宫顺时针数到生年地支
- 二星一逆一顺，形成对向分布

**天哭与天虚的象征意义**：
- **天哭**：主悲伤、哭泣、丧事、送别。入相关宫位时，容易遇到让人哭泣的事件。
- **天虚**：主虚空、落空、幻灭、不实。入相关宫位时，容易遇到期望落空的情况。

**重要格局**：
- **哭虚入命**：主人情绪敏感，容易悲观，需要学习情绪管理
- **哭虚入父母宫**：与家人有分离、送别的经历
- **哭虚逢丧门白虎**：主丧事、丧亲，是实际的凶事指标

**现代应用**：
天哭天虚在现代可用于评估情绪敏感度与心理韧性。入命的人需要特别注意心理健康的维护。

#### 校勘与字词辨析（bilingual）：

- **"天哭"**：哭泣之星，主悲伤送别。英文："Tianku, Weeping Star"。
- **"天虚"**：虚空之星，主幻灭落空。英文："Tianxu, Void Star"。
- **"午宫起子"**：以午宫作为子年的参照点。英文："Wu palace as the anchor for Zi year"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天哭天虚起午宫，哭逆巳兮虚顺未，数到生年便安之，悲欢离合皆有期。"此诀描述天哭天虚的定位方法与情绪象征。
- **悲欢相对**：古人认为天哭主"有形之悲"（如丧事），天虚主"无形之空"（如期望落空），二者相对而生。
- **现代应用**：天哭天虚在现代心理学语境中可理解为"悲伤敏感度"与"虚无倾向"的指标。入命或福德宫的人，可能需要更多的心理支持与情绪调节训练。"""
    normalized_text_zh: str = """"""
    subject: str = "安天哭天虚星诀"
    factor_refs: list = ['source_ref', 'rel_kuxu_001', 'principle_wugongqizinian', 'rel_kuxu_002', 'principle_wugongqizinian', 'rel_kuxu_003', 'star_tianku', 'evi_kuxu_001', 'star_tianku', 'rule_tianku_dingwei', 'evi_kuxu_002', 'star_tianxu', 'rule_tianxu_dingwei', 'concept_grief_star', 'concept_void_star']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_安天哭天虚星诀_001_L1",
    )
    version: str = "1.0.0"
