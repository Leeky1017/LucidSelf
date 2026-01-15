"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919411
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
    semantic_id="zy_v1.0.0_升卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 升卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  升：元亨。用见大人，勿恤。南征吉。

  【彖传】
  《彖》曰：“柔以时升，巽而顺，刚中而应，是以大亨。用见大人，勿恤，有庆也。南征...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  升：元亨。用见大人，勿恤。南征吉。

  【彖传】
  《彖》曰：“柔以时升，巽而顺，刚中而应，是以大亨。用见大人，勿恤，有庆也。南征吉，志行也。”

  【象传】
  《象》曰：地中生木，升；君子以顺德，积小以高大。

  【爻辞】
  初六，允升，大吉。
  九二，孚乃利用禴，无咎。
  九三，升虚邑。
  六四，王用亨于岐山，吉，无咎。
  六五，贞吉，升阶。
  上六，冥升，利于不息之贞。

- 分字分词释义：

  - **升**：上升、提升之意，可指地位、德行、形势的渐进上行，不是跃迁而是循序上升。
  - **元亨**：大亨通，强调此时“升”的过程在整体上有助于系统通达，而非局部之利。
  - **用见大人，勿恤**：适宜在上升过程中求见大人（有德之上位者），若路径得当，无需过度忧惧阻碍。
  - **南征吉**：向南而行为吉；南为离明之方，象征向光明、文明之处进发，强调“升”要朝向更开明的方向。
  - **柔以时升，巽而顺**：以内在之柔顺配合时机而升，上下皆巽，说明升应以谦逊、顺势而为，而非硬冲。
  - **刚中而应**：九二居中为刚，与上位相应，说明升之中有坚实支点，不是空升。
  - **地中生木**：下巽为木，上坤为地，木生地中，自下而上破土而出，是“积累—突破—升高”的自然图景。
  - **顺德，积小以高大**：以顺和之德行事，从细微处一点点积累，最终成就高大之物事，是升之正道。
  - **允升**：上升合乎允当之理，非僭越、不逾矩。
  - **孚乃利用禴**：有诚信，方可用简约之禴祭而无咎，与萃卦六二同文，在此强调“升”过程中仍须节制仪节、重在诚意。
  - **升虚邑**：上升到空城、空邑，象征职位或局面升高却缺乏实质承载，需要警觉“虚升”。
  - **王用亨于岐山**：王在岐山行大祭，岐山为宗周发祥之地，象征在上升过程中回到根基、巩固源头。
  - **升阶**：一步步登阶而上，比喻按次第晋升，不逾越等级。
  - **冥升**：在昏暗中上升，方向虽向上，但光线不明，需依靠“不断守贞”来避免失足。

- **规范化释义（primary_lang_explained）**：

  升卦承萃卦而来。《序卦》曰：“萃聚而升不来也，故受之以升。”——当众流所聚之势已经形成，下一步便是由下而上、由低而高的“升”。这里的“升”不是单纯的升官加爵，而是一种在顺势与累积基础上的整体上行。

  卦辞“升：元亨。用见大人，勿恤。南征吉。”说明，在这种“升”的时势里，整体气运是元亨的，但个人该如何行动？关键在于：一是要“用见大人”——在上升途中主动与更高层次的德行与制度接轨，而非只在自身小圈子里打转；二是“勿恤”——只要路径与对象得当，无需过分忧惧；三是“南征吉”——上升的方向要朝向光明、启发与文明，而不是向黑暗之地扩张。

  彖传强调“柔以时升，巽而顺，刚中而应”：升的方式是柔顺的、把握时机的，而不是以蛮力冲撞；同时，又必须有“刚中而应”的支点——中位的阳刚之德，才能让升不致虚浮。象传“地中生木，升；君子以顺德，积小以高大”则进一步把“升”拉回到人格修养：真正的升并非一蹴而就，而是像树木在土中扎根、缓慢生长，通过日复一日的小积累，最终成其高大。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Sheng (Ascending) addresses 上升进取. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 升卦的核心是**“顺势而上的渐进之升”，重在根基与累积，而非跳级和冒进**。
  - 升需要“柔顺 + 中刚”：既要谦逊顺时，又要在中位保持坚实与原则。
  - 爻辞从“允升的大吉”“以禴祭守诚”“升而虚”“返本于岐山”“循阶而上”“冥中守贞”描绘了多种升的路径与偏差。

- 详细解说：

  卦象为上坤下巽：巽木在地中生长，向上穿出坤土，是“由内而外、由下而上”的渐进之象。与萃卦“泽上于地”的聚集状态相比，升卦更强调“聚之后如何向上生长”。

  初六“允升，大吉”象征在升势萌芽之初，若所行之升合乎允当（不僭、不速），虽位卑仍能大吉。九二“孚乃利用禴，无咎”与萃六二呼应：上升过程中，保持诚信，比铺张更重要；只要有“孚”，简祭亦可无咎，暗示升的本质在于道德与关系的稳固，而非表面工程。

  九三“升虚邑”则提出警告：当人升之过快，未及充实内容，就可能来到“空城”——名位高而实事少，或环境空洞。此时不必立即恐慌，但要意识到“虚升”的风险，开始补课。六四“王用亨于岐山，吉，无咎”表明：在更高层级的升中，需要回到“岐山”——自己的根基与发祥之地，通过大祭与整合资源来稳固上升基座。

  六五“贞吉，升阶”体现的是最理想的升：守贞而吉，按阶级次第而上，不越级、不抢位。上六“冥升，利于不息之贞”则总结全卦：当升至极点，反而容易进入“冥”——看不清方向的地带；此时唯一的依托是“不息之贞”：不断地守持正道与反省，而非停在自满的高处。


#### L2 语义提取

- **主题**：上升进取，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_416]` `[trigger: 卦=升 AND 卦辞=元亨用见大人]` `[factor_trigger: zhouyi_gua_sheng AND zhouyi_guaci]` `[role: 主干]` 升，元亨；用见大人，勿恤：上升之时，利见大人。 → 《周易·升卦·卦辞》
  - `[ns_zhouyi_417]` `[trigger: 卦=升 AND 彖传]` `[factor_trigger: zhouyi_gua_sheng AND zhouyi_tuan AND zhouyi_shangsheng_chengdu]` `[role: 主干依赖]` 柔以时升。 → 《周易·升卦·彖传》
  - `[ns_zhouyi_418]` `[trigger: 卦=升 AND 象传=地中生木]` `[factor_trigger: zhouyi_gua_sheng AND zhouyi_xiang]` `[role: 主干依赖]` 地中生木，升；君子以顺德积小以高大：如木自地升起。 → 《周易·升卦·象传》
  - `[ns_zhouyi_419]` `[trigger: 卦=升 AND 初六=允升大吉]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 条件分支]` 允升，大吉：诚信而升，大为吉祥。 → 《周易·升卦·爻辞》
  - `[ns_zhouyi_420]` `[trigger: 卦=升 AND 九二=孚乃利用禴]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 条件分支]` 孚乃利用禴，无咎：诚信则祭礼可简。 → 《周易·升卦·爻辞》
  - `[ns_zhouyi_421]` `[trigger: 卦=升 AND 九三=升虚邑]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 例外处理]` 升虚邑：升入空虚之邑，无所阻碍。 → 《周易·升卦·爻辞》
  - `[ns_zhouyi_422]` `[trigger: 卦=升 AND 六四=王用亨于岐山]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 主干依赖]` 王用亨于岐山，吉无咎：王于岐山祭享而吉。 → 《周易·升卦·爻辞》
  - `[ns_zhouyi_423]` `[trigger: 卦=升 AND 六五=贞吉升阶]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 主干依赖]` 贞吉，升阶：守正则吉，循阶而升。 → 《周易·升卦·爻辞》
  - `[ns_zhouyi_424]` `[trigger: 卦=升 AND 上六=冥升利于不息之贞]` `[factor_trigger: zhouyi_gua_sheng]` `[role: 总结]` 冥升，利于不息之贞：冥冥而升，须持续守正。 → 《周易·升卦·爻辞》
  - **中文**：
  - 卦辞"升：元亨。用见大人，勿恤。南征吉"依通行王弼本；"升"为上升，巽木在下、坤地在上。
  - "地中生木"谓巽木自坤地中生长而出，象征由卑而升、渐次长大。
  - "顺德，积小以高大"谓君子当顺势修德，积累小善以成大德，如树木渐高。
  - "南征吉"之"南"为离方，向阳而进，志行顺畅。
  - "升虚邑"谓升入空虚之邑，无所阻碍，进入顺畅。
  - "王用亨于岐山"引周文王祭享岐山之典故，"亨"为祭祀通达。
  - "冥升"谓昏冥而升，已至极点，须"利于不息之贞"，持续守正不懈。
  - **English**: Based on Wang Bi commentary edition. "升" means ascent. "地中生木" shows tree growing from earth—gradual rise. "积小以高大" advises accumulating small virtues. "岐山" is King Wen's historical allusion. "冥升" warns of blind ascent needing constant rectitude."""
    normalized_text_zh: str = """"""
    subject: str = "升卦（䷭）"
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
        l1_anchor="zy_v1.0.0_升卦_001_L1",
    )
    version: str = "1.0.0"
