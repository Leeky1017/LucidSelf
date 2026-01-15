"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620075
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
    semantic_id="qtbj_v1.0.0_3__六月乙木_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3六月乙木未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月乙木，木性且寒，柱多金水，丙火为尊。支成水局，乙得无伤。癸水透干，大富大贵。无癸定作常人，运不行北，困苦一生。
  凡五六月乙木，气退枯焦，用癸水...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月乙木，木性且寒，柱多金水，丙火为尊。支成水局，乙得无伤。癸水透干，大富大贵。无癸定作常人，运不行北，困苦一生。
  凡五六月乙木，气退枯焦，用癸水切忌戊己杂乱，则为下格。
  或甲木高透，制伏土神名为去浊留清，可许俊秀。土多乏甲秀气脱空，庸人而已。
  或丙癸两透，加以甲透制戊，选拔定然。若不见丙癸，只有丁火，亦属常人，有壬、可充衣食。
  或柱中无水，又无比劫出干﹐乃为弃命从才，富大贵小，能招贤德之妻。从才格以火为妻，土为子。
  或一派戊土出干，不见比肩，名为才多身弱，终为富屋贫人。
  或丙辛化水，嫖赌破家，终非承受之儿。
  或一派乙木，不见丙癸，名为乱臣无主劳碌奔波，又加支多辛金，僧道之辈。

- **分字分词释义**：
  - **木性且寒**：木性尚且寒冷 / 三伏生寒 / 需丙
  - **乙得无伤**：乙木没有受伤 / 水局保护 / 吉象
  - **气退枯焦**：气势退却枯槁焦燥 / 五六月特征 / 需水
  - **去浊留清**：去除浊气保留清气 / 甲制土 / 格清
  - **秀气脱空**：秀气落空 / 土多无甲 / 庸人
  - **弃命从才**：放弃自身从属财星 / 变格 / 无水无比
  - **富屋贫人**：住在富人房子里的穷人 / 财多身弱 / 虚名
  - **乱臣无主**：混乱的臣子没有君主 / 乙多无丙癸 / 劳碌

- **规范化释义（primary_lang_explained）**：
  六月（未月）的乙木，木性尚且寒冷（三伏生寒？此处疑指阴气生或金水多时），如果柱中金水多，以丙火为至尊（解寒）。如果地支合成水局，乙木没有受伤。此时癸水透干，大富大贵。如果没有癸水，定作常人，如果大运不走北方水地，一生困苦。
  凡是五六月的乙木，气退枯焦，用癸水切忌戊己土杂乱（土克水），否则为下格。
  如果甲木高透，制伏土神（戊己），这叫“去浊留清”，可以许诺俊秀。如果土多而缺乏甲木，秀气脱空，只是庸人而已。
  如果丙癸两透，加上甲木透出制戊，选拔（科举）是一定的。如果不见丙癸，只有丁火，也属常人，有壬水，可以充裕衣食。
  如果柱中无水，又无比劫出干，这叫“弃命从财”，富大贵小，能招贤德的妻子。
  如果一派戊土出干，不见比肩（甲乙），这叫“财多身弱”，终究是富屋贫人。
  如果丙辛化水（丙辛合化水在未月难成，除非局象特殊），主嫖赌破家，终非能承受家业的儿子。
  如果一派乙木，不见丙癸，这叫“乱臣无主”（无君臣），劳碌奔波，若加上地支多辛金（七杀），是僧道之辈。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 6th Month (Goat Month): Wood nature is somewhat cold (due to Yin growth or Metal/Water presence). If pillars have much Metal/Water, Bing Fire is supreme. If branches form a Water frame, Yi is uninjured. If Gui is revealed, it is great wealth and nobility. Without Gui, one is ordinary; if Luck does not go North, one suffers for life.
  Generally for Yi in 5th/6th Months, Qi retreats and is scorched. Using Gui Water strictly avoids Wu/Ji Earth mixing in; otherwise, it is a lower pattern.
  If Jia Wood is highly revealed to control the Earth Spirit (Wu/Ji), it is called "Removing Turbidity Keeping Clarity", promising talent. If Earth is abundant and lacks Jia, elegance is hollow, merely a mediocre person.
  If Bing and Gui are both revealed, plus Jia to control Wu, Civil Service is certain. Without Bing/Gui, having only Ding makes one ordinary; having Ren provides enough for food and clothing.
  If pillars have no Water and no Parallel/Rob Wealth revealed, it is "Abandon Life Follow Wealth"; great wealth but small nobility, obtaining a virtuous wife.
  If a mass of Wu Earth is revealed without Parallel Shoulders, it is "Abundant Wealth Weak Body", ending as a "Rich House Poor Man".
  If Bing and Xin transform into Water (rare/conditional), one ruins the family through prostitution and gambling.
  If a mass of Yi Wood appears without Bing/Gui, it is "Rebellious Ministers without a Ruler", denoting toil and wandering. Adding abundant Xin Metal in branches makes one a monk or Taoist.

- **核心要点**：
  - **去浊留清**：土旺（浊）需甲木（清）制土护水。
  - **弃命从财**：土多无印比，从财。
  - **乱臣无主**：比劫多而无丙癸（无用神），劳碌。
  - **丙辛化水**：未月乃燥土，化水难，若强合往往心性不稳（嫖赌）。
  未月是木的墓库，气最弱。
  - 关键在于“润”（癸）和“疏”（甲）。
  - 未土燥，无水则木枯。癸水最重要，但怕土克，所以甲木制土护水（去浊留清）是贵格的关键。
  - "乱臣无主"形容一堆乙木（乱臣）没有丙火（君）和癸水（臣）来引导，只能瞎忙。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_191]` `[trigger: 未月乙木]` `[factor_trigger: month_wei AND tiangan_yi AND (metal_excess OR water_excess) AND tiangan_bing]` `[role: 主干]` 六月乙木，木性且寒，柱多金水，丙火为尊。 → 《穷通宝鉴·三夏乙木》#8.3
  - `[ns_qttbj_192]` `[trigger: 甲木去浊]` `[factor_trigger: month_wei AND tiangan_yi AND tiangan_jia AND earth_excessive AND jia_controls_earth]` `[role: 主干依赖]` 甲木高透，制伏土神名为去浊留清，可许俊秀。 → 《穷通宝鉴·三夏乙木》#8.3
  - `[ns_qttbj_193]` `[trigger: 富屋贫人]` `[factor_trigger: month_wei AND tiangan_yi AND wu_excessive AND NOT shishen_parallel]` `[role: 例外处理]` 一派戊土出干，不见比肩，名为才多身弱，终为富屋贫人。 → 《穷通宝鉴·三夏乙木》#8.3
  - `[ns_qttbj_194]` `[trigger: 乱臣无主]` `[factor_trigger: month_wei AND tiangan_yi AND yi_multiple AND NOT tiangan_bing AND NOT tiangan_gui]` `[role: 例外处理]` 一派乙木，不见丙癸，名为乱臣无主劳碌奔波。 → 《穷通宝鉴·三夏乙木》#8.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 六月乙木（未月）"
    factor_refs: list = ['rebellious_ministers', 'ruin_family_via_vice']
    
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
        l1_anchor="qtbj_v1.0.0_3__六月乙木_未月_001_L1",
    )
    version: str = "1.0.0"
