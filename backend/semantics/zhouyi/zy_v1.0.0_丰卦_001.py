"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919499
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
    semantic_id="zy_v1.0.0_丰卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 丰卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  丰，亨。王假之，勿忧，宜日中。

  【彖传】
  《彖》曰：“丰，大也。明以动，故丰。王假之，尚大也。勿忧，宜日中，宜照天下也。日中...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  丰，亨。王假之，勿忧，宜日中。

  【彖传】
  《彖》曰：“丰，大也。明以动，故丰。王假之，尚大也。勿忧，宜日中，宜照天下也。日中则昃，月盈则食；天地盈虚，与时消息，而况人于人乎？况于鬼神乎？”

  【象传】
  《象》曰：雷电皆至，丰；君子以折狱致刑。

  【爻辞】
  初九，遇其配主，虽旬无咎，往有尚。
  六二，丰其蔀，日中见斗；往得疑疾，有孚发若，吉。
  九三，丰其沛，日中见沬；折其右肱，无咎。
  九四，丰其蔀，日中见斗；遇其夷主，吉。
  六五，来章，有庆誉，吉。
  上九，丰其屋，蔀其家，闚其户，阒其无人，三岁不觌，凶。

- 分字分词释义：

  - **丰**：本义为大、盛，引申为资源、声势、光明等方面的充盈和高涨。
  - **王假之**：“假”作“至、临”解，王亲临其事或其时，象征在丰盛局面中由上位者主持与节制。
  - **宜日中**：以“日中”为最盛之时，既指适宜在光明、公正的时段行事，又暗含“日中则昃”的盛极而衰之理。
  - **雷电皆至**：下震为雷，上离为火电，雷电同至，象征局势张扬、变化迅猛、影响广远。
  - **蔀**：遮蔽之具，如帷幕、屋檐；“丰其蔀”“蔀其家”皆指遮蔽过厚，以致光明不达内里。
  - **日中见斗 / 见沬**：正午而见星斗、见水沫之影，比喻盛极之时已现反常征兆，暗示将入衰境。
  - **配主 / 夷主**：配主为与己相配之主；夷主可解作同类、平辈之主，皆指是否遇到相称而可依持的对象。
  - **来章，有庆誉**：“章”指文章、文采或昭彰之德，“来章”即美名来临，由此带来庆贺与声誉。
  - **闚其户，阒其无人，三岁不觌**：“闚”为从缝隙窥视，“阒”为寂静无声，“觌”为相见，整体形容外观丰盛、实则门内空虚、久不相见之状。

- **规范化释义（primary_lang_explained）**：

  丰卦讨论的是“在极盛与高张时如何自处”。卦辞云：“丰，亨。王假之，勿忧，宜日中。”——丰盛之时，若有合宜的主持与节制，则可以通达而不致忧患；关键在于把握“日中”的尺度：既借光明与鼎盛之便，又不忘盛极必衰的节律。

  彖传以“明以动”点出丰象的根本：离为明，震为动，光明而又行动，故为“丰”；然而紧接着便提醒“日中则昃，月盈则食”，天地盈虚本有常理，人及人事亦然。丰卦因此既不否定丰盛本身，也不鼓励沉醉不醒，而是要求在丰盛中自觉节制，使丰不至于倾覆。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Feng (Abundance) addresses 丰盛显大. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - **丰卦聚焦“盛时之道”**：强调在资源、声名、光明都处于高峰时，须以节制与警觉自处。
  - **“日中则昃”是整卦的时间背景**：丰并非恒久状态，而是短暂高点，因此“勿忧，宜日中”更像是“在盛中行事、在盛中思衰”。
  - **各爻通过“丰其屋、丰其蔀”等象，展示从内实外虚到外盛内空的演变**：提醒人分辨丰的内涵与外形。

- 详细解说：

  丰卦卦象上离下震：震为雷、为动，离为火、为明，雷电交作，光明四布，是典型的“显赫之象”。与前卦旅之“在外漂泊”不同，丰描写的是身处中心、光明照临的状态：王者亲临，众目所视，一举一动都代表某种“丰盛的秩序”。

  初九“遇其配主，虽旬无咎，往有尚。”描写丰始之际的良好相遇：得其配主，即找到相称的主事者或合作方，即便在一个“旬期”内尚未见大效，也不会有咎，反而有可称道之处。“丰”的开端，贵在遇对人，而非一开始就求极大之功。

  六二、九四一再提到“丰其蔀，日中见斗”：当遮蔽太厚之时，纵使日中之光本应最明，仍反常地看到斗星，象征体制与结构遮蔽了应有的光明，导致在繁华表象之下积累阴影。六二处下体中位，“往得疑疾，有孚发若，吉。”说明一旦意识到“疑疾”——结构性病症，并以诚信坦陈、主动“发若”揭示问题，仍可转吉；九四则“遇其夷主，吉”，提示在更高一层找到同类之主，可以协力拨云见日。

  九三“丰其沛，日中见沬；折其右肱，无咎。”则展示另一种风险：表面上盛大丰盈（丰其沛），却在关键部位（右臂）受损，只要懂得收手，不再逞强，尚可“无咎”。六五“来章，有庆誉，吉。”代表在尊位者若以真实文采与德行来主持丰局，则赞誉与庆典顺势而来，此时的丰是真实之丰，而非空架子。

  上六“丰其屋，蔀其家，闚其户，阒其无人，三岁不觌，凶。”则是对“空壳丰盛”的极端描写：屋宇宏伟、遮蔽严密，外观似极盛，然门内寂寥，无人可见，长期失去真正的往来，终归于凶。此爻提醒，当丰演变为只剩外观、关系实质断裂之时，已不是调整即可化解的小病，而是结构性危机。


#### L2 语义提取

- **主题**：丰盛显大，如何在此情境中顺应天道、把握时机、实现人生目标。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_497]` `[trigger: 卦=丰 AND 卦辞=亨王假之]` `[factor_trigger: zhouyi_gua_feng AND zhouyi_guaci]` `[role: 主干]` 丰，亨；王假之，勿忧，宜日中：丰盛之时，王临之而勿忧。 → 《周易·丰卦·卦辞》
  - `[ns_zhouyi_498]` `[trigger: 卦=丰 AND 彖传]` `[factor_trigger: zhouyi_gua_feng AND zhouyi_tuan]` `[role: 主干依赖]` 大也。明以动，故丰。 → 《周易·丰卦·彖传》
  - `[ns_zhouyi_499]` `[trigger: 卦=丰 AND 象传=雷电皆至]` `[factor_trigger: zhouyi_gua_feng AND zhouyi_xiang]` `[role: 主干依赖]` 雷电皆至，丰；君子以折狱致刑：雷电并作，明断狱刑。 → 《周易·丰卦·象传》
  - `[ns_zhouyi_500]` `[trigger: 卦=丰 AND 初九=遇其配主]` `[factor_trigger: zhouyi_gua_feng]` `[role: 条件分支]` 遇其配主，虽旬无咎：遇合适之主，十日无咎。 → 《周易·丰卦·爻辞》
  - `[ns_zhouyi_501]` `[trigger: 卦=丰 AND 六二=丰其蔀]` `[factor_trigger: zhouyi_gua_feng]` `[role: 条件分支]` 丰其蔀，日中见斗：帷幕遮日，日中见斗。 → 《周易·丰卦·爻辞》
  - `[ns_zhouyi_502]` `[trigger: 卦=丰 AND 九三=丰其沛]` `[factor_trigger: zhouyi_gua_feng]` `[role: 例外处理]` 丰其沛，日中见沫：繁盛之极，日中见星。 → 《周易·丰卦·爻辞》
  - `[ns_zhouyi_503]` `[trigger: 卦=丰 AND 九四=丰其蔀日中见斗]` `[factor_trigger: zhouyi_gua_feng]` `[role: 条件分支]` 丰其蔀，日中见斗，遇其夷主：帷幕遮蔽，遇平等之主。 → 《周易·丰卦·爻辞》
  - `[ns_zhouyi_504]` `[trigger: 卦=丰 AND 六五=来章有庆誉]` `[factor_trigger: zhouyi_gua_feng]` `[role: 主干依赖]` 来章，有庆誉，吉：文采来临，庆誉齐至。 → 《周易·丰卦·爻辞》
  - `[ns_zhouyi_505]` `[trigger: 卦=丰 AND 上六=丰其屋蔀其家]` `[factor_trigger: zhouyi_gua_feng]` `[role: 总结]` 丰其屋，蔀其家：屋大而家遮蔽，孤立无援。 → 《周易·丰卦·爻辞》
  - **中文**：
  - 卦辞"丰：亨。王假之，勿忧，宜日中"依通行王弼本；"假"训为至、临，王者临于丰盛之世。
  - "日中则昃，月盈则食"为彖传警语，谓日正中必偏西、月满必亏，天地盈虚与时消息，警示盛极必衰。
  - "丰其蔀"之"蔀"释为帷幕、遮蔽物；"日中见斗"谓正午却能见北斗，比喻盛世反见衰象。
  - "丰其沛"之"沛"一说为旗帜，一说为幡幔；"日中见沬"之"沬"为小星，象征更深的遮蔽。
  - "来章"之"章"释为文采、光彩；"有庆誉"谓吉庆与美誉齐至。
  - "蔀其家"谓以帷幕遮蔽其家，自我封闭而孤立无援。
  - **English**: Based on Wang Bi commentary edition. "假" means arrive/approach. "日中则昃" warns of peak-to-decline cycle. "蔀" means curtain/covering. "日中见斗/沬" indicates seeing stars at noon—darkness in prosperity. "来章" means arriving brilliance."""
    normalized_text_zh: str = """"""
    subject: str = "丰卦（䷶）"
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
        l1_anchor="zy_v1.0.0_丰卦_001_L1",
    )
    version: str = "1.0.0"
