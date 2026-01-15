"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919574
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
    semantic_id="zy_v1.0.0_既济卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 既济卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  既济：亨，小，利贞，初吉终乱。

  【彖传】
  《彖》曰：“既济亨，小者亨也。利贞，刚柔正而位当也。初吉，柔得中也；终止则乱，其道...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  既济：亨，小，利贞，初吉终乱。

  【彖传】
  《彖》曰：“既济亨，小者亨也。利贞，刚柔正而位当也。初吉，柔得中也；终止则乱，其道穷也。”

  【象传】
  《象》曰：水在火上，既济；君子以思患而豫防之。

  【爻辞】
  初九，曳其轮，濡其尾，无咎。
  六二，妇丧其茀，勿逐，七日得。
  九三，高宗伐鬼方，三年克之，小人勿用。
  六四，𦈡有衣袽，终日戒。
  九五，东邻杀牛，不如西邻之礿祭，实受其福。
  上六，濡其首，厉。

- 分字分词释义：

  - **既济**：已经渡过、已经成就之意；卦名指“事情已然告一段落、表面完成”的状态。
  - **亨，小，利贞，初吉终乱**：可以亨通，但属“小亨”；有利于守正；开头吉利，结局却易乱，提醒“成而未终”的风险。
  - **水在火上**：上坎为水，下离为火，水在火上，象征表面秩序已成、阴阳错综而暂时协调，但上下结构内含隐忧。
  - **曳其轮，濡其尾**：拖住车轮、打湿尾巴，比喻在已经可行的情势中仍稍作拖延、保守，以避免冒进之祸。
  - **妇丧其茀**：妇女丢失发饰或礼冠上的蔽饰，“茀”为遮蔽之物，比喻失去外在装饰而仍可复得。
  - **高宗伐鬼方，三年克之**：指殷高宗远征鬼方的战争故事，用以说明“既济之功往往伴随长期劳苦”，并警惕勿用小人。
  - **𦈡有衣袽，终日戒**：华美的衣服终将破旧，提醒在盛装背后仍要终日戒备，防范潜在败坏。
  - **东邻杀牛，不如西邻之礿祭**：盛大祭祀不如适时简祭，强调在既济状态中“贵在诚与时”，而非形式之大。
  - **濡其首，厉**：头部被湿，象征在高位处失于节制，易致危险与败局。

- **规范化释义（primary_lang_explained）**：

  既济卦讨论的是“事情已经完成表面阶段之后，如何防止走向败坏”。卦辞曰：“既济：亨，小，利贞，初吉终乱。”——已经渡河、已经成事，可以亨通，但主要是“小亨”；有利于坚守正道；开端吉利，若不知道收束与防微，终局易乱。

  彖传说明：既济之所以“亨”，在于“刚柔正而位当”——阳刚与阴柔各在其位、守其中正；但“初吉”只是因为柔爻得中，长久却难免“终止则乱，其道穷也”。既济之道因此不是庆祝功成，而是及时思患、防患于未然。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Ji Ji (After Completion) addresses 功成既济. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 既济卦核心是**“功成之时，最需防乱”**：在事情已经过河之后，更要警觉潜伏的逆转。
  - “小亨”与“初吉终乱”共同限定了既济的尺度与时间性：不要把一时成功视为永久秩序。
  - 各爻通过“曳其轮”“丧其茀”“三年克鬼方”“衣袽终日戒”“东邻杀牛 / 西邻礿祭”“濡其首厉”等象，展开从保守谨慎到劳苦得胜、从华饰将敝到节制祭祀、从慎终不渝到过度放纵的连续图景。

- 详细解说：

  卦象水在火上：水本可灭火，但今在其上，反倒形成一种“表面稳定、内里紧张”的结构——火气向上升，水气下压，需微妙平衡。君子因此“以思患而豫防之”：在既济之时，即要思考“尚未发生的祸患”，并预先布置防线，而非沉浸在成功叙事中。

  初九“曳其轮，濡其尾，无咎。”表现的是在既济之初的克制：宁可拖慢车轮、沾湿衣尾，也不贸然猛进；这种稍显笨拙的保守，恰恰使之“无咎”。六二“妇丧其茀，勿逐，七日得。”描写在已成局面中，对外饰损失采取“不急于追回”的态度：只要内在秩序仍在，中道自然会使所失复得。

  九三“高宗伐鬼方，三年克之，小人勿用。”提醒既济之功往往来之不易：经历长期战争与消耗，胜利之后更不能任用小人，以免成果被腐蚀。六四“𦈡有衣袽，终日戒。”指出：已然华丽的外表必有朽敝之时，因此在既济状态中要有“终日戒”的心态，随时警觉自身结构的老化与漏洞。

  九五“东邻杀牛，不如西邻之礿祭，实受其福。”则将既济之道落实为祭祀与制度：此时更关键的，是以适时、诚挚的小礼取代铺张的大典；实受其福在于“时”和“诚”，不是规模。上六“濡其首，厉。”总括全卦：当处于顶点仍不知节制，如在水火既济中仍纵情上冲，最终头部沾湿、局面失控，进入危险之境。


#### L2 语义提取

- **主题**：功成既济，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_569]` `[trigger: 卦=既济 AND 卦辞=亨小利贞]` `[factor_trigger: zhouyi_gua_jiji AND zhouyi_guaci]` `[role: 主干]` 既济，亨小，利贞：事已成，小利守正。 → 《周易·既济卦·卦辞》
  - `[ns_zhouyi_570]` `[trigger: 卦=既济 AND 彖传]` `[factor_trigger: zhouyi_gua_jiji AND zhouyi_tuan]` `[role: 主干依赖]` 亨小。柔得中也。 → 《周易·既济卦·彖传》
  - `[ns_zhouyi_571]` `[trigger: 卦=既济 AND 象传=水在火上]` `[factor_trigger: zhouyi_gua_jiji AND zhouyi_xiang]` `[role: 主干依赖]` 水在火上，既济；君子以思患而预防之：水火既济，思患预防。 → 《周易·既济卦·象传》
  - `[ns_zhouyi_572]` `[trigger: 卦=既济 AND 初九=曳其轮]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 条件分支]` 曳其轮，濡其尾：拖曳车轮，沾湿尾巴。 → 《周易·既济卦·爻辞》
  - `[ns_zhouyi_573]` `[trigger: 卦=既济 AND 六二=妇丧其茀]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 条件分支]` 妇丧其茀，勿逐：妇人失车帷，勿追逐。 → 《周易·既济卦·爻辞》
  - `[ns_zhouyi_574]` `[trigger: 卦=既济 AND 九三=高宗伐鬼方]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 主干依赖]` 高宗伐鬼方，三年克之：征伐远方，三年乃克。 → 《周易·既济卦·爻辞》
  - `[ns_zhouyi_575]` `[trigger: 卦=既济 AND 六四=繻有衣袽]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 例外处理]` 繻有衣袽，终日戒：有破衣备用，终日警戒。 → 《周易·既济卦·爻辞》
  - `[ns_zhouyi_576]` `[trigger: 卦=既济 AND 九五=东邻杀牛]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 主干依赖]` 东邻杀牛，不如西邻之禴祭：厚祭不如薄祭之诚。 → 《周易·既济卦·爻辞》
  - `[ns_zhouyi_577]` `[trigger: 卦=既济 AND 上六=濡其首]` `[factor_trigger: zhouyi_gua_jiji]` `[role: 总结]` 濡其首，厉：沾湿其首，危厉之象。 → 《周易·既济卦·爻辞》
  - **中文**：
  - 卦辞"既济：亨，小，利贞，初吉终乱"依通行王弼本；"既济"谓事已成济，"小"修饰"亨"，非大亨而是小亨。
  - "水在火上"谓坎水在离火之上，水火相济而相制，表面秩序已成，但内含"终乱"之隐忧。
  - "曳其轮，濡其尾"以渡水为喻，拖曳车轮、沾湿尾巴，谨慎行事可无咎。
  - "妇丧其茀"之"茀"释为车帷或首饰；"勿逐，七日得"谓勿急躁追求，七日自得。
  - "高宗伐鬼方"引殷商史事，高宗即武丁，鬼方为远方蛮族，三年乃克，示功业虽成仍需谨慎。
  - "东邻杀牛，不如西邻之禴祭"对比厚祭与薄祭，诚意胜于形式，"实受其福"谓实在受福。
  - **English**: Based on Wang Bi commentary edition. "既济" means already completed. "水在火上" shows water-fire balance but inherent instability. "高宗伐鬼方" is historical allusion to King Wu Ding. "东邻/西邻" contrasts form vs sincerity in sacrifice."""
    normalized_text_zh: str = """"""
    subject: str = "既济卦（䷾）"
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
        l1_anchor="zy_v1.0.0_既济卦_001_L1",
    )
    version: str = "1.0.0"
