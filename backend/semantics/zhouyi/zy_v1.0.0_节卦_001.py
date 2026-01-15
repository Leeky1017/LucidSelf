"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919544
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
    semantic_id="zy_v1.0.0_节卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 节卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  节：亨。苦节不可贞。

  【彖传】
  《彖》曰：“节亨，刚柔分而刚得中。‘苦节不可贞，其道穷也。’说以行险，当位以节，中正以通。天...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  节：亨。苦节不可贞。

  【彖传】
  《彖》曰：“节亨，刚柔分而刚得中。‘苦节不可贞，其道穷也。’说以行险，当位以节，中正以通。天地节而四时成，节以制度，不伤财，不害民。”

  【象传】
  《象》曰：泽上有水，节；君子以制数度，议德行。

  【爻辞】
  初九，不出户庭，无咎。
  九二，不出门庭，凶。
  六三，不节若，则嗟若；无咎。
  六四，安节，亨。
  九五，甘节，吉；往有尚。
  上九，苦节，贞凶，悔亡。

- 分字分词释义：

  - **节**：节制、节律、制度之“节”，既指限制，也指划分与调配。
  - **节：亨。苦节不可贞。**：有度的节制可以导致亨通；过于苦涩、僵硬的节制则难以长久守正。
  - **刚柔分而刚得中**：阳刚与阴柔各得其分，而居中的为刚爻，象征以中正之刚来主持节制。
  - **说以行险，当位以节，中正以通**：以兑之说悦面对坎险，在合适位置上施行节制，以中正之道实现通达。
  - **泽上有水**：上兑为泽，下坎为水，水在泽上，水量有限而须节，象征资源需有度分配。
  - **不出户庭 / 不出门庭**：在初、二位分别控制活动范围，表现节制的不同层次与其吉凶差别。
  - **不节若，则嗟若**：若不知节制，则必有叹息与后悔，提示节制之必要。
  - **安节 / 甘节 / 苦节**：对“节”的三种心态：安然守节、甘心守节、苦涩守节，对应不同的吉凶走向。

- **规范化释义（primary_lang_explained）**：

  节卦关心的是“如何设定恰当的边界与节制”。卦辞说：“节：亨。苦节不可贞。”——说明合理的节制有助于亨通，但若节制过苦、过苛，就难以长久保持正道，终将走向穷途。

  彖传指出：“节亨，刚柔分而刚得中”，节之所以能致亨，在于刚柔有分而不混乱，由居中的刚爻主持，这样的节制既不过度，也不失守。“说以行险，当位以节，中正以通”进一步说明：在险中行事，需要以悦、以说来缓冲紧张，同时在合适的位置上施行节制，使中正之道得以通行。天地因为有节，四季才能成序；人间制度通过节制资源与行为，方能“不伤财，不害民”。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jie (Limitation) addresses 节制有度. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 节卦核心是**“有度的节制，而非一味收缩”**。
  - “苦节不可贞”提供了对过度 austerity 的明确否定：节必须兼顾人情与长久性。
  - 爻辞通过“不出户庭 / 不出门庭”“安节 / 甘节 / 苦节”等对照，展示节制从过轻到过重、从适度到失衡的谱系。

- 详细解说：

  卦象为上兑下坎：坎为水、为险，兑为泽、为悦，水在泽中，若无节制易溢为患；若善用边界，则既能蓄水又不致成灾。君子“以制数度，议德行”：一方面通过“数度”——法律和制度层面的量化标准来约束行为，另一方面通过“议德行”在德性上加以讨论与校正，使节制不仅是外在强制，也是内在认同。

  初九“不出户庭，无咎。”刻画节制的起点：只要暂时不出自家门庭，就可免于祸咎；这里的节多半是因时制宜的谨慎。九二“不出门庭，凶。”则警示：当环境与角色已经变化时，若仍沿用同样的封闭方式，就从“谨慎”变为“闭塞”，因而为凶。

  六三“不节若，则嗟若；无咎。”呈现另一侧面：若完全不懂节制，到头来必生叹息；然而及时反省还来得及，故“无咎”。六四“安节，亨。”则是理想状态之一：以安然之心守节，不勉强自己也不放纵，因而亨通。九五“甘节，吉；往有尚。”进一步说明：若能发自内心地“甘于节制”，节不再只是外在束缚，而成为自愿选择，那么不仅吉，而且“往有尚”——在前行之路上更有可称道之处。

  上六“苦节，贞凶，悔亡。”则总结全卦：若节制走向苦涩、僵硬，即便自以为守贞，终究凶险。然而“悔亡”也提示，当走到极端苦节之时，已经没有更多后悔空间，反而需要整体回到对“节”的重新理解上，不能再以加倍紧缩来弥补错误。


#### L2 语义提取

- **主题**：节制有度，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：
  - **象征**：泽上有水、苦节不可贞、安节亨、不出户庭无咎。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_542]` `[trigger: 卦=节 AND 卦辞=亨苦节不可贞]` `[factor_trigger: zhouyi_gua_jie2 AND zhouyi_guaci]` `[role: 主干]` 节，亨；苦节不可贞：节制有度，过苦则不可守。 → 《周易·节卦·卦辞》
  - `[ns_zhouyi_543]` `[trigger: 卦=节 AND 彖传]` `[factor_trigger: zhouyi_gua_jie AND zhouyi_tuan AND zhouyi_bianjie_yishi]` `[role: 主干依赖]` 亨。刚柔分而刚得中。 → 《周易·节卦·彖传》
  - `[ns_zhouyi_544]` `[trigger: 卦=节 AND 象传=泽上有水]` `[factor_trigger: zhouyi_gua_jie2 AND zhouyi_xiang]` `[role: 主干依赖]` 泽上有水，节；君子以制数度议德行：泽蓄有度，制定规矩。 → 《周易·节卦·象传》
  - `[ns_zhouyi_545]` `[trigger: 卦=节 AND 初九=不出户庭]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 条件分支]` 不出户庭，无咎：守于门户之内。 → 《周易·节卦·爻辞》
  - `[ns_zhouyi_546]` `[trigger: 卦=节 AND 九二=不出门庭凶]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 例外处理]` 不出门庭，凶：过于自守，反失时机。 → 《周易·节卦·爻辞》
  - `[ns_zhouyi_547]` `[trigger: 卦=节 AND 六三=不节若]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 例外处理]` 不节若，则嗟若：不知节制，终有嗟叹。 → 《周易·节卦·爻辞》
  - `[ns_zhouyi_548]` `[trigger: 卦=节 AND 六四=安节亨]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 条件分支]` 安节，亨：安于节制，自然亨通。 → 《周易·节卦·爻辞》
  - `[ns_zhouyi_549]` `[trigger: 卦=节 AND 九五=甘节吉]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 主干依赖]` 甘节，吉：甘于节制，大为吉祥。 → 《周易·节卦·爻辞》
  - `[ns_zhouyi_550]` `[trigger: 卦=节 AND 上六=苦节贞凶]` `[factor_trigger: zhouyi_gua_jie2]` `[role: 总结]` 苦节，贞凶，悔亡：过苦之节，守正亦凶。 → 《周易·节卦·爻辞》
  - **中文**：卦辞"节：亨"强调通达；"苦节不可贞"警示过度节制。
  - **English**: "节亨" emphasizes success. "苦节不可贞" warns against excessive limitation."""
    normalized_text_zh: str = """"""
    subject: str = "节卦（䷻）"
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_节卦_001_L1",
    )
    version: str = "1.0.0"
