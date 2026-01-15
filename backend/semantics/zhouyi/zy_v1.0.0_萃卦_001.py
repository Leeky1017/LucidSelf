"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919400
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
    semantic_id="zy_v1.0.0_萃卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 萃卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  萃：亨。王假有庙，利见大人，亨。利有攸往，利建侯。

  【彖传】
  《彖》曰：“萃，聚也。顺以说，刚中而应，故聚也。王假有庙，致孝...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  萃：亨。王假有庙，利见大人，亨。利有攸往，利建侯。

  【彖传】
  《彖》曰：“萃，聚也。顺以说，刚中而应，故聚也。王假有庙，致孝享也。利见大人，亨，聚以正也。利有攸往，利建侯，行师，众之所聚也。”

  【象传】
  《象》曰：泽上于地，萃；君子以除戎器，戒不虞。

  【爻辞】
  初六，有孚不终，乃乱乃萃；若号，一握为笑，勿恤，往无咎。
  六二，引吉，无咎，孚乃利用禴。
  六三，萃如，嗟如，无攸利；往无咎，小吝。
  九四，大吉，无咎。
  九五，萃有位，无咎；匪孚，元永贞，悔亡。
  上六，赍咨涕洟，无咎。

- 分字分词释义：

  - **萃**：聚集、汇聚之意，卦取众多之气、众人之心聚合于一点的局面。
  - **王假有庙**：君王亲临宗庙，行祭祀之礼，以聚合宗庙之“神气”与宗族之“人心”。
  - **利见大人，亨**：有利于见到“大人”（有德有位者），通过正当之聚使事业亨通，而非依靠私党之聚。
  - **利有攸往，利建侯**：在“聚”已成形之时，有利于按礼制建立诸侯、布置地方秩序，使聚集转化为稳定结构。
  - **泽上于地**：上兑为泽，下坤为地，泽水积于地上，象征众流所聚，易成“盈溢”，需加以治理与防备。
  - **除戎器，戒不虞**：修治兵器以备不测，提醒在“盛聚”之时要预防潜在冲突，而非沉迷于当下的繁华。
  - **有孚不终，乃乱乃萃**：起初有诚信，却不能坚持到底，便会先乱后聚，聚中带乱。
  - **若号，一握为笑，勿恤，往无咎**：在混乱中以号哭聚众，一旦握手言和便转为欢笑，说明及时开放沟通可化解纷乱。
  - **利用禴**：适宜用简约的小祭（禴祭）来维系聚集，而不必事事大张旗鼓。
  - **萃如，嗟如**：聚而叹息，表面有人群，内心却感到空虚或不安。
  - **赍咨涕洟**：携带忧虑、咨嗟而泣，鼻涕眼泪俱下，象征在聚散交界处的情绪宣泄。

- **规范化释义（primary_lang_explained）**：

  萃卦讲“众聚之道”。《序卦》曰：“物相遇而后聚，故受之以萃。”——在姤卦“相遇”之后，随之而来的就是如何聚集人与资源的问题。卦辞“萃：亨。王假有庙，利见大人，亨。利有攸往，利建侯。”把聚焦点放在“以宗庙之礼聚心，以大人之德聚人，以制度建侯聚势”三层上。

  彖传指出：萃之所以能“聚”，在于“顺以说，刚中而应”：坤顺在下，兑悦在上，内顺而外说，使人愿意自发靠拢；又有刚爻居中得位，与上下相应，因此聚而不乱。君王“假有庙”，是以孝道为核心，让聚集有其精神中心；“利见大人，亨”，是以正道之人作为聚集的轴心；“利建侯，行师”，则是把聚集的力量通过行政与军事结构化，使之成为秩序而非乌合之众。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Cui (Gathering) addresses 聚合会萃. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 萃卦的核心是**“在盛聚之时，如何以礼、德、制三者维持秩序并防范风险”**。
  - 真正的“萃”，不是人数越多越好，而是要聚到“有庙”“有大人”“有制度”的中心上。
  - 爻辞表现了从“有孚不终的乱聚”“简约之禴祭”“聚中叹息”“位得而大吉”“有位无孚需永贞”，到“涕洟而无咎”的全程聚散图景。

- 详细解说：

  卦象为上兑下坤：坤为地、为顺，兑为泽、为悦。地之上有泽，水聚其上，象征下民顺聚于上层，形成充盈的局面。与损、益偏重资源流动不同，萃偏重“状态上的聚集”和“治理聚集的方式”。

  初六“有孚不终，乃乱乃萃；若号，一握为笑，勿恤，往无咎”揭示了聚集初期的典型风险：初有诚信，未能坚持到底，便引发叛乱与混萃。但只要有人挺身而出“号”之，公开表达与沟通，握手言和后便可由哭转笑，前往则无咎——关键在于及时修复信任。六二“引吉，无咎，孚乃利用禴”进一步强调“简祭”与“引而不迫”：以适度的礼仪引导人心，保持诚信，比堆砌盛大场面更重要。

  六三“萃如，嗟如，无攸利；往无咎，小吝”显示的是“人虽聚而心不安”的状态：场面热闹，叹息却多，若勉强推进未必有利；但适当前行，至少可以免于大祸，只是略有可惜。九四“大吉，无咎”说明当阳刚之力介入、居于适中之位时，能为萃局提供稳固骨干，使大吉而无咎。九五“萃有位，无咎；匪孚，元永贞，悔亡”则点明：聚之中心必须“有位”且“永贞”，如果一时缺乏信任，可通过长期守贞来化解悔恨。

  上六“赍咨涕洟，无咎”收束全卦：在聚局即将散开或结构变换之际，难免有忧思与悲伤，但只要在此时避免激烈动作，让情绪得以宣泄反而无咎——这是对“盛聚之后”的一种温和过渡。


#### L2 语义提取

- **主题**：聚合会萃，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_407]` `[trigger: 卦=萃 AND 卦辞=亨王假有庙]` `[factor_trigger: zhouyi_gua_cui AND zhouyi_guaci]` `[role: 主干]` 萃，亨；王假有庙：聚会之道，王以宗庙聚众。 → 《周易·萃卦·卦辞》
  - `[ns_zhouyi_408]` `[trigger: 卦=萃 AND 彖传]` `[factor_trigger: zhouyi_gua_cui AND zhouyi_tuan AND zhouyi_juji_chengdu]` `[role: 主干依赖]` 聚也。顺以说，刚中而应。 → 《周易·萃卦·彖传》
  - `[ns_zhouyi_409]` `[trigger: 卦=萃 AND 象传=泽上于地]` `[factor_trigger: zhouyi_gua_cui AND zhouyi_xiang]` `[role: 主干依赖]` 泽上于地，萃；君子以除戎器戒不虞：萃聚之时，备戎防患。 → 《周易·萃卦·象传》
  - `[ns_zhouyi_410]` `[trigger: 卦=萃 AND 初六=有孚不终]` `[factor_trigger: zhouyi_gua_cui]` `[role: 条件分支]` 有孚不终，乃乱乃萃：诚信不持终，则乱而后萃。 → 《周易·萃卦·爻辞》
  - `[ns_zhouyi_411]` `[trigger: 卦=萃 AND 六二=引吉无咎]` `[factor_trigger: zhouyi_gua_cui]` `[role: 条件分支]` 引吉，无咎：引导而吉，无所咎责。 → 《周易·萃卦·爻辞》
  - `[ns_zhouyi_412]` `[trigger: 卦=萃 AND 六三=萃如嗟如]` `[factor_trigger: zhouyi_gua_cui]` `[role: 条件分支]` 萃如嗟如，无攸利：聚而叹息，无所利也。 → 《周易·萃卦·爻辞》
  - `[ns_zhouyi_413]` `[trigger: 卦=萃 AND 九四=大吉无咎]` `[factor_trigger: zhouyi_gua_cui]` `[role: 主干依赖]` 大吉，无咎：大为吉祥，无所咎责。 → 《周易·萃卦·爻辞》
  - `[ns_zhouyi_414]` `[trigger: 卦=萃 AND 九五=萃有位]` `[factor_trigger: zhouyi_gua_cui]` `[role: 主干依赖]` 萃有位，无咎：聚于正位，无所咎责。 → 《周易·萃卦·爻辞》
  - `[ns_zhouyi_415]` `[trigger: 卦=萃 AND 上六=齎咨涕洟]` `[factor_trigger: zhouyi_gua_cui]` `[role: 总结]` 齎咨涕洟，无咎：悲泣涕泪，无所咎责。 → 《周易·萃卦·爻辞》
  - **中文**：
  - 卦辞"萃：亨。王假有庙，利见大人，亨。利有攸往，利建侯"依通行王弼本；"萃"为聚集，兑泽在上、坤地在下。
  - "泽上于地"谓兑泽高于坤地，水聚于地上，象征众人萃聚。
  - "除戎器，戒不虞"谓萃聚之时，当修治兵器、戒备不测，聚则易生乱。
  - "王假有庙"之"假"释为至、临，王者以宗庙凝聚人心，致孝享之诚。
  - "若号，一握为笑"谓初聚或有纷扰，呼号之后握手言欢。
  - "齎咨涕洟"之"齎咨"为嗟叹，"涕洟"为涕泪，上六萃极而悲，终无咎。
  - **English**: Based on Wang Bi commentary edition. "萃" means gathering. "泽上于地" shows water gathering on earth. "除戎器" advises preparing weapons during assembly. "王假有庙" emphasizes ruler gathering through temple. "齎咨涕洟" describes sighing and weeping at the end."""
    normalized_text_zh: str = """"""
    subject: str = "萃卦（䷬）"
    factor_refs: list = ['zhouyi_gua_045', 'principle_king_temple_proposal', 'method_great_sacrifice_proposal', 'principle_gathering_position_proposal', 'principle_firm_center_responds_proposal']
    
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
        l1_anchor="zy_v1.0.0_萃卦_001_L1",
    )
    version: str = "1.0.0"
