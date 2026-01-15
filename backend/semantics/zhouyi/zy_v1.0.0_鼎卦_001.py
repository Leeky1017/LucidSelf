"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919452
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
    semantic_id="zy_v1.0.0_鼎卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 鼎卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  鼎，元吉，亨。

  【彖传】
  《彖》曰：“鼎，象也。以木巽火，亨饪也。圣人亨以享上帝，而大亨以养圣贤。巽而耳目聪明，柔进而上行，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  鼎，元吉，亨。

  【彖传】
  《彖》曰：“鼎，象也。以木巽火，亨饪也。圣人亨以享上帝，而大亨以养圣贤。巽而耳目聪明，柔进而上行，得中而应乎刚，是以元亨。”

  【象传】
  《象》曰：木上有火，鼎；君子以正位凝命。

  【爻辞】
  初六，鼎颠趾，利出否，得妾以其子，无咎。
  九二，鼎有实，我仇有疾，不我能即，吉。
  九三，鼎耳革，其行塞，雉膏不食。方雨，亏悔，终吉。
  九四，鼎折足，覆公餗，其形渥，凶。
  六五，鼎黄耳金铉，利贞。
  上九，鼎玉铉，大吉，无不利。

- 分字分词释义：

  - **鼎**：本为烹饪和祭祀的大型器皿，在古代逐渐成为权力、律法与秩序的象征；卦中由“取新、立新”之意，引申出制度与价值的重建。
  - **元吉，亨**：在鼎卦所代表的“取新立新”阶段，只要方式得当，即可获得大吉与通达。
  - **以木巽火，亨饪也**：下巽为木，上离为火，以木入火而烹饪，比喻以合宜手段推动内部转化，使原材料化为可供奉、可共享之食。
  - **正位凝命**：君子端正自身位置，使“天命”与人间职分在鼎这一重器上得以凝聚和承载。
  - **鼎颠趾**：鼎足向上翻转，比喻颠覆常态以倾倒陈积之物，为后续清理与更新做准备。
  - **利出否**：“否”为浊秽之物，从鼎中倒出污物以去旧更新，象征先清除积弊再谈立新。
  - **鼎有实**：鼎中充满可食之物，比喻制度与器具已经承载起真实内容，而非空器。
  - **鼎耳革，其行塞**：鼎耳改变、倾斜，提携不便，以致行进受阻，象征提携机制失灵，导致“雉膏不食”。
  - **公餗，其形渥**：“餗”指供祭之粥羹，“覆公餗”是把公家的祭品翻覆倾洒，“其形渥”则形容染污、狼狈的样子，喻权责失当导致公共事务受损。
  - **黄耳金铉 / 玉铉**：“耳”为鼎上两侧可系系绳之处，“铉”为贯耳以举鼎之横木或金属横梁；“黄耳金铉”与“玉铉”一组，象征在尊贵、稳固的提携结构中运作鼎事。
  - **我仇有疾，不我能即**：对手或对立面虽有疾病或缺陷，却一时无法接近我，表示在鼎有实之时，外患难以侵扰。
  - **方雨，亏悔，终吉**：雨势方起，悔恨渐消，虽一度停滞，终能转为吉利，暗示在调整提携机制后，鼎仍可重新运作。

- **规范化释义（primary_lang_explained）**：

  鼎卦继革卦而来，重点不在“破旧”本身，而在“立新”——如何把已经准备好的材料化为可供奉、可共享的成果。卦辞简练地说：“鼎，元吉，亨。”——在鼎象之时，若能善用此器，便能成就大吉与通达。

  彖传指出：鼎是“以木巽火，亨饪也”的器物象征：下卦巽为木，上卦离为火，木入火中，鼎中之物得以烹饪成熟。圣人以鼎烹祭，以致敬于上帝；又以鼎养圣贤，使道脉得以延续。鼎之所以“元亨”，在于“巽而耳目聪明，柔进而上行，得中而应乎刚”：既有柔顺上行之态，又有中正刚健之实，承上启下，载道而行。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Ding (Cauldron) addresses 鼎新革故. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 鼎卦的核心是**“在重器中完成从原料到供奉的转化”**：立新、养贤、承命三者合一。
  - 先“颠趾出否”，再“有实可食”：去旧与取新相辅相成，缺一不可。
  - 鼎的成败高度依赖“耳”“铉”之结构：提携方式是否稳固、公器是否被翻覆，决定了鼎能否成为真正的承载之器。

- 详细解说：

  卦象为上离下巽：离为火、为明，巽为木、为入，木入火中，火在木上，是典型的烹饪之象。与革卦“泽中有火”的冲突结构不同，鼎重在把已经被革新后的诸多要素置于一器之中，经过火候与时间的锤炼，化为可以奉献与共享的成果。

  初六“鼎颠趾，利出否，得妾以其子，无咎。”描绘的是“倒鼎出渣”的动作：先让鼎足朝天，把积累在鼎底的污物倾倒出来，如此虽有一时颠覆，却能“利出否”而不留后患；“得妾以其子”则暗示，虽出身不高，但有实际承载与延续之功，因此终无大咎。九二“鼎有实，我仇有疾，不我能即，吉。”则显示鼎中已装满实物，己方内部充实稳健，即便外有“仇”患，也因自身有实而难以侵扰，是为“吉”。

  九三“鼎耳革，其行塞，雉膏不食。方雨，亏悔，终吉。”提醒：当鼎耳结构失衡、提携之道受阻时，即使鼎中有“雉膏”那样精美的食物，也无法顺利供人享用；然而“方雨”象征润泽将至，“亏悔”则表示经由反省与调整，仍可转危为安，最终复归于吉。九四“鼎折足，覆公餗，其形渥，凶。”则是负面高峰：鼎足折断、公家祭品覆地，形象狼狈，是制度性失败对公共领域的直接伤害。

  六五“鼎黄耳金铉，利贞。”展示鼎在尊位时的理想状态：黄耳象征中和，金铉象征坚固的承载结构，鼎得以安稳提举，利于长久守贞。上九“鼎玉铉，大吉，无不利。”则将鼎之状态推至极致：铉由金进为玉，既坚且美，象征在最高层次上，承载与奉献的机制已经臻于完善，此时鼎不再只是炊具，更成为凝聚命运、统摄秩序的宗器，因此“大吉，无不利”。



- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_452]` `[trigger: 卦=鼎 AND 卦辞=元吉亨]` `[factor_trigger: zhouyi_gua_ding AND zhouyi_guaci]` `[role: 主干]` 鼎，元吉，亨：鼎为重器，象征大吉亨通。 → 《周易·鼎卦·卦辞》
  - `[ns_zhouyi_453]` `[trigger: 卦=鼎 AND 彖传]` `[factor_trigger: zhouyi_gua_ding AND zhouyi_tuan]` `[role: 主干依赖]` 象也。以木巽火。 → 《周易·鼎卦·彖传》
  - `[ns_zhouyi_454]` `[trigger: 卦=鼎 AND 象传=木上有火]` `[factor_trigger: zhouyi_gua_ding AND zhouyi_xiang]` `[role: 主干依赖]` 木上有火，鼎；君子以正位凝命：如鼎烹物，正位凝命。 → 《周易·鼎卦·象传》
  - `[ns_zhouyi_455]` `[trigger: 卦=鼎 AND 初六=鼎颠趾]` `[factor_trigger: zhouyi_gua_ding]` `[role: 条件分支]` 鼎颠趾，利出否：鼎足翻覆，利于去旧。 → 《周易·鼎卦·爻辞》
  - `[ns_zhouyi_456]` `[trigger: 卦=鼎 AND 九二=鼎有实]` `[factor_trigger: zhouyi_gua_ding]` `[role: 条件分支]` 鼎有实，我仇有疾：鼎中有物，仇敌有疾。 → 《周易·鼎卦·爻辞》
  - `[ns_zhouyi_457]` `[trigger: 卦=鼎 AND 九三=鼎耳革]` `[factor_trigger: zhouyi_gua_ding]` `[role: 例外处理]` 鼎耳革，其行塞：鼎耳脱落，难以举行。 → 《周易·鼎卦·爻辞》
  - `[ns_zhouyi_458]` `[trigger: 卦=鼎 AND 九四=鼎折足]` `[factor_trigger: zhouyi_gua_ding]` `[role: 例外处理]` 鼎折足，覆公餗：鼎足折断，倾覆所烹。 → 《周易·鼎卦·爻辞》
  - `[ns_zhouyi_459]` `[trigger: 卦=鼎 AND 六五=鼎黄耳金铉]` `[factor_trigger: zhouyi_gua_ding]` `[role: 主干依赖]` 鼎黄耳金铉，利贞：黄金鼎耳，守正则利。 → 《周易·鼎卦·爻辞》
  - `[ns_zhouyi_460]` `[trigger: 卦=鼎 AND 上九=鼎玉铉]` `[factor_trigger: zhouyi_gua_ding]` `[role: 总结]` 鼎玉铉，大吉，无不利：玉制鼎铉，大吉无不利。 → 《周易·鼎卦·爻辞》
  - **中文**：
  - 卦辞"鼎：元吉，亨"依通行王弼本；"元吉"在前表示根本之吉，"亨"为通达，合为鼎新之大吉象。
  - "以木巽火，亨饪也"中"亨饪"即烹饪，以巽木入离火，比喻制度文明化育万物。
  - "正位凝命"一语，"凝"释为凝聚、承载，君子端正其位而使天命凝定于此。
  - "鼎颠趾"之"颠"释为翻倒，"利出否"意为利于倾出渣滓，去旧迎新。
  - "覆公餗"之"餗"为鼎中之食，鼎折足则倾覆食物，象征制度败坏、养贤不成。
  - "黄耳金铉/玉铉"分别以金、玉形容鼎耳与鼎铉，由金至玉，象征品质提升。
  - **English**: Based on Wang Bi commentary edition. "亨饪" means cooking/transformation through proper means. "正位凝命" indicates stabilizing mandate through proper positioning. "颠趾/折足/覆餗" describe various failures of the vessel. "金铉/玉铉" progression symbolizes refinement."""
    normalized_text_zh: str = """"""
    subject: str = "鼎卦（䷱）"
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
        l1_anchor="zy_v1.0.0_鼎卦_001_L1",
    )
    version: str = "1.0.0"
