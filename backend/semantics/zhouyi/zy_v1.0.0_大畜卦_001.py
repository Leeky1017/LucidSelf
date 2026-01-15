"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899932
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
    semantic_id="zy_v1.0.0_大畜卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 大畜卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  大畜：利贞；不家食，吉；利涉大川。

  【彖传】
  《彖》曰：“大畜，刚健笃实，𪸩光日新其德；刚上而尚贤，能止健，大正也。‘不家食...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  大畜：利贞；不家食，吉；利涉大川。

  【彖传】
  《彖》曰：“大畜，刚健笃实，𪸩光日新其德；刚上而尚贤，能止健，大正也。‘不家食，吉’，养贤也。‘利涉大川’，应乎天也。”

  【象传】
  《象》曰：天在山中，大畜；君子以多识前言往行，以畜其德。

  【爻辞】
  初九，有厉，利已。
  九二，舆说輹。
  九三，良马逐，利艰贞；曰闲舆卫，利有攸往。
  六四，童牛之牿，元吉。
  六五，豮豕之牙，吉。
  上九，何天之衢，亨。

- 分字分词释义：

  - **大畜**：大规模的蓄养与积聚，既指物质资源，也指德行、人才与经验的积累。
  - **利贞**：利于守正而蓄，不宜躁动妄用。
  - **不家食，吉**：不让贤者只在家中吃饭，意为使有德有才者不闲置在家，而被举用于外；亦可理解为“所食不局于一家”。
  - **利涉大川**：有利于渡大河，比喻在大风险、大跨越中能安然通过。
  - **刚健笃实，𪸩光日新其德**：阳刚而又笃厚真实，光辉日新，德性不断增益。
  - **能止健，大正也**：能以艮之止节制乾之健，使刚健不至于横冲直撞，成为“大正之道”。
  - **舆说輹**：车轴脱落，比喻行动受阻，需要暂停整备。
  - **良马逐，曰闲舆卫**：良马奔驰、练习车马与卫护之技，比喻在蓄养阶段练兵习艺。
  - **童牛之牿**：给小牛加横木以防冲撞，比喻及早设限，使力量受控。
  - **豮豕之牙**：阉猪之牙，象征对凶猛之性加以节制。
  - **何天之衢**：通达天路的大道，比喻与天道相应而大道亨通之境。

- **规范化释义（primary_lang_explained）**：

  大畜卦讲“如何在强盛之时蓄养而不滥用”，同时兼顾“养贤”与“渡险”。卦辞云：“大畜：利贞；不家食，吉；利涉大川。”——说明此时宜于积聚而守正，不宜轻率消耗；贤者不应闲居家中，而应被举用、被养成；在这样的蓄养结构下，面对“大川”般的险境也有条件安全渡过。

  彖传指出：下乾上艮，刚健而笃实，如天之气蓄于山中，“𪸩光日新其德”形容光明与德行不断更新；上九居艮之上，尚贤而能止健，使乾之过刚受到节制。“不家食，吉”，意在养贤——贤才不应困于小家，而应被国家社会所用；“利涉大川”则因为此种结构顺应天道，面对重大风险时，既有力量又有节制。

  象传“天在山中，大畜；君子以多识前言往行，以畜其德”把“大畜”落到学习与记忆上：天在山中，好比伟大的道德能量储存在坚实结构内部；君子通过广泛记忆前贤的言行，以此蓄养自己的德性，而非空谈。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Da Xu, "Great Accumulation" or "Taming Power", describes the ability to restrain and accumulate great strength, both inner virtue and external resources, in preparation for significant action. The Judgment, "Da Xu: favorable to be steadfast; not eating at home brings good fortune; it is favorable to cross the great water", indicates that this accumulated strength should eventually be put to use in the wider world.

- 核心要点：

  - 大畜卦的核心是**“有力而能蓄，有才而不滥”**：在强盛期重积累、重训练，而非只求立刻释放。
  - 爻辞展示了从“有厉，利已”的自我克制，到“良马逐”“童牛之牿”“豮豕之牙”的训练与节制，再到“何天之衢”的大路亨通的过程。
  - “不家食，吉”提供了一个重要的人才观：贤才不应仅为一姓一家所独占，而应被更大系统所承载。

- 详细解说：
  从卦象看，下乾为天，上艮为山，是“天在山中”的图景：大能量被坚实的结构所收纳，形成“可蓄而不泄”的状态。与无妄相比，无妄重在“顺天而不妄为”，大畜则重在“在顺天的前提下，如何蓄积与节制能力”。

  爻序层面，初九“有厉，利已”是起点：处在初始之阳，既有冲劲，也有危险，故宜自止以避免犯灾；九二“舆说輹”提示：系统进入积累期，车輪脱落，需修整而暂缓进发；九三“良马逐，利艰贞；曰闲舆卫，利有攸往”说明：在艰难中训练良马与防卫之技，虽喘息不易，却为后续前行打基础。

  六四"童牛之牿，元吉"与六五"豮豕之牙，吉"从"限制潜在危险"谈起：对尚未完全成形的力量（童牛）与潜在凶暴（豮豕）及时加以约束，是大畜阶段的智慧；最后上九"何天之衢，亨"，则呈现当蓄养与节制都到位之后，与天道相通、大道亨行的状态。"""
    normalized_text_zh: str = """"""
    subject: str = "大畜卦（䷙）"
    factor_refs: list = ['zhouyi_gua_daxu']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_大畜卦_001_L1",
    )
    version: str = "1.0.0"
