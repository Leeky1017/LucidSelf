"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620124
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
    semantic_id="qtbj_v1.0.0_2__十一月乙木_子月_与冬至后_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一月乙木子月与冬至后(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月乙木，花木寒冻，一阳来复，喜用丙火解冻，则花木有向阳之意，不宜用癸以冻花木，故耑用丙火。
  有一二点丙火出干，无癸制者，可许科甲。即丙藏支内，...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月乙木，花木寒冻，一阳来复，喜用丙火解冻，则花木有向阳之意，不宜用癸以冻花木，故耑用丙火。
  有一二点丙火出干，无癸制者，可许科甲。即丙藏支内，亦有选拔恩封，得此不贵，必因风水薄。或壬癸出干，有戊制，可作能人，即丙在支内，亦是俊秀。若壬透无戊，贫贱之人。
  支成水局，干透壬癸，丙丁全无，虽有戊制，贫乏到老，运至南方，稍有衣食。
  丁火有亦如无，丁乃灯烛之火，岂能解严寒之冻。设无丙丁，戊土多见，金水奔流，下贱。或有戊己无火，亦属常人，但不至下贱。
  或一派丁火，大奸大诈之徒。如无甲引丁，孤鳏到老。丁火见甲，必主麟趾振振，芝兰绑膝。
  乙木生于冬至之后，坐下木局，得丙透干者，富贵之造。即丁出干，亦有衣禄，须忌癸制丁。
  乙木生于冬月，己土透干，又有丙透，大富贵之造。

- **分字分词释义**：
  - **花木寒冻**：花草树木寒冷冻结 / 子月特征 / 极寒
  - **一阳来复**：一阳开始复生 / 冬至节气 / 转暖
  - **向阳之意**：面向太阳的意愿 / 喜丙 / 生机
  - **冻花木**：冻结花木 / 癸水大忌 / 凶象
  - **灯烛之火**：灯烛的微弱火光 / 丁火 / 力弱
  - **严寒之冻**：严寒的冰冻 / 子月 / 难解
  - **大奸大诈**：极其奸诈 / 丁火多无甲 / 凶象
  - **麟趾振振**：子孙昌盛 / 丁见甲 / 吉象
  - **芝兰绑膝**：子孙贤德 / 丁见甲 / 吉象

- **规范化释义（primary_lang_explained）**：
  十一月（子月）的乙木，花木寒冷冻结，一阳（冬至）开始复生，喜欢用丙火解冻，这样花木就有向阳的意思，不宜用癸水来冻结花木，所以专用丙火。
  有一两点丙火透出天干，没有癸水克制的人，可以许诺科甲。即使丙火藏在地支内，也有选拔恩封的功名，如果这样还不贵，必定是因为风水薄。如果壬癸水透出，有戊土制约，可以做能人，此时即使丙火在支内，也是俊秀之才。如果壬水透出没有戊土，是贫贱之人。
  地支合成水局，天干透出壬癸水，丙丁火全无，虽有戊土制水，也是贫乏到老，大运到了南方火地，才稍有衣食。
  丁火虽然有，但也像没有一样，丁火是灯烛之火，怎能解开严寒的冰冻？假设没有丙丁火，戊土多见，而金水奔流，是下贱之命。如果有戊己土而无火，也属常人，但不至于下贱。
  如果一派丁火（无丙），是大奸大诈之徒。如果无甲木引生丁火，孤寡到老。丁火见到甲木，必主子孙昌盛（麟趾振振）。
  乙木生于冬至之后，坐下木局（如日支卯或合成局），得到丙火透干，是富贵之造。即使丁火出干，也有衣禄，但必须忌讳癸水制丁。
  乙木生于冬月，己土透干，又有丙火透出，是大富贵之造。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 11th Month (Rat Month): Flowers and trees are frozen. One Yang returns (Winter Solstice). It delights in using Bing Fire to unfreeze, giving the wood an intention to face the Sun. It is not suitable to use Gui Water to freeze the wood further; thus exclusively use Bing Fire.
  If one or two points of Bing are revealed without Gui to control them, Civil Service is promised. Even if Bing is hidden in branches, there is selection and honors; if not noble, it must be due to poor Feng Shui. If Ren/Gui are revealed and Wu controls them, one can be a capable person; even with Bing in branches, one is elegant. If Ren is revealed without Wu, one is poor and lowly.
  If branches form a Water frame, Ren/Gui revealed, and absolutely no Bing/Ding, even with Wu controlling, one is poor until old age; when Luck reaches the South, there is slight food and clothing.
  Ding Fire, even if present, is like nothing; Ding is lamp fire, how can it unfreeze severe cold? If there is no Bing/Ding, and Wu Earth is seen frequently, but Metal/Water rush, it is lowly. If there is Wu/Ji but no Fire, it is ordinary but not lowly.
  If there is a mass of Ding Fire, one is a great treacherous deceiver. Without Jia to ignite Ding, one is lonely until old age. If Ding sees Jia, it implies flourishing offspring.
  Yi Wood born after Winter Solstice, sitting on a Wood frame, with Bing revealed, is a structure of wealth and nobility. Even if Ding is revealed, there is sustenance, but one must avoid Gui controlling Ding.
  Yi Wood born in Winter Month, with Ji revealed and Bing also revealed, is a structure of great wealth and nobility.

- **核心要点**：
  - **专用丙火**：寒木向阳，非丙不暖。
  - **丁火无力**：灯烛难解冻，除非有甲引丁。
  - **忌癸水**：冻花木。
  - **冬至后**：一阳复始，气机转暖，丙火更具功效。

- **详细解说**：
  子月乙木，关键在于“解冻”。
  - 丙火太阳是唯一解药。
  - 丁火力微，且子月癸水当令，丁火易伤。但若有甲木（藤萝系甲）生丁，则丁火有源，主子孙贤。
  - "大奸大诈"：指丁火虽多但无甲引、无丙照，阴火由于寒湿环境而变得阴暗诡诈。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_208]` `[trigger: 子月乙木]` `[factor_trigger: month_zi AND tiangan_yi AND tiangan_bing AND likes_bing_unfreeze]` `[role: 主干]` 十一月乙木，花木寒冻，一阳来复，喜用丙火解冻，故耑用丙火。 → 《穷通宝鉴·三冬乙木》#10.2
  - `[ns_qttbj_209]` `[trigger: 灯烛之火]` `[factor_trigger: month_zi AND tiangan_yi AND tiangan_ding AND NOT tiangan_bing AND ding_fire_weak]` `[role: 主干依赖]` 丁火有亦如无，丁乃灯烛之火，岂能解严寒之冻。 → 《穷通宝鉴·三冬乙木》#10.2
  - `[ns_qttbj_210]` `[trigger: 大奸大诈]` `[factor_trigger: month_zi AND tiangan_yi AND ding_multiple AND NOT tiangan_jia AND NOT tiangan_bing]` `[role: 例外处理]` 一派丁火，大奸大诈之徒。如无甲引丁，孤鳏到老。 → 《穷通宝鉴·三冬乙木》#10.2
  - `[ns_qttbj_211]` `[trigger: 麟趾振振]` `[factor_trigger: month_zi AND tiangan_yi AND tiangan_ding AND tiangan_jia AND flourishing_offspring]` `[role: 条件分支]` 丁火见甲，必主麟趾振振，芝兰绕膝。 → 《穷通宝鉴·三冬乙木》#10.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一月乙木（子月）与冬至后"
    factor_refs: list = ['one_yang_returns', 'spring_cold_valley', 'flourishing_offspring']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__十一月乙木_子月_与冬至后_001_L1",
    )
    version: str = "1.0.0"
