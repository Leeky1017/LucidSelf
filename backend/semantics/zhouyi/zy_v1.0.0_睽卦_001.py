"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919304
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
    semantic_id="zy_v1.0.0_睽卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 睽卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  睽：小事吉。

  【彖传】
  《彖》曰：睽，火动而上，泽动而下；二女同居，其志不同行。说而丽乎明，柔进而上行，得中而应乎刚，是以小...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  睽：小事吉。

  【彖传】
  《彖》曰：睽，火动而上，泽动而下；二女同居，其志不同行。说而丽乎明，柔进而上行，得中而应乎刚，是以小事吉。天地睽而其事同也，男女睽而其志通也，万物睽而其事类也；睽之时用大矣哉！

  【象传】
  《象》曰：上火下泽，睽；君子以同而异。

  【爻辞】
  初九，悔亡；丧马，勿逐，自复；见恶人，无咎。
  九二，遇主于巷，无咎。
  六三，见舆曳，其牛掣，其人天且劓，无初有终。
  九四，睽孤，遇元夫，交孚，厉无咎。
  六五，悔亡；厥宗噬肤，往何咎？
  上九，睽孤，见豕负涂，载鬼一车；先张之弧，后说之弧；匪寇，婚媾；往遇雨则吉。

- 分字分词释义：

  - **睽**：乖离、不合；视线相背。卦名指“表面相背、内有相通”的局面。
  - **小事吉**：在睽离之时，适宜处理小事，而不宜图大事。
  - **火动而上，泽动而下**：离火向上、兑泽向下，各行其道，象征上下相背。
  - **二女同居，其志不同行**：同处一室、志向不同，用以比喻人际或系统中的分歧与偏差。
  - **说而丽乎明**：内心向往欢乐，而又依附于光明；表示在分歧中仍可寻求共同的光明基础。
  - **同而异**：求大同而容小异，既不抹杀差异，也不放弃共识。
  - **悔亡；丧马，勿逐，自复**：不必为一时损失过度追逐，顺其自然，自有回返。
  - **见舆曳，其牛掣，其人天且劓**：目睹车被拖曳、牛被牵扯、驾车人受重刑，象征错位与严重偏差的后果。
  - **睽孤**：因观点或处境不同而陷入孤立状态。
  - **豕负涂，载鬼一车**：满身泥污的猪、载满“鬼魅”的车，象征极度丑恶、怪异之相。

- **规范化释义（primary_lang_explained）**：

  睽卦讨论的是“分歧与误解之中，如何保留共同之道”。卦辞“睽：小事吉。”提示：在彼此相背、沟通困难的时期，宜从小事做起，积累信任，不宜强行推动大事。

  彖传通过“火上泽下”的卦象与“二女同居，其志不同行”的比喻指出：睽是客观存在的结构——各行其道、各有所求，而非单纯的道德问题。然而，“说而丽乎明，柔进而上行，得中而应乎刚”，说明在分歧中仍可能通过向明、向中的一方逐渐进取，与刚强者相互呼应，从而实现小事之吉。天地、男女、万物看似睽离，但在各自职责与类属上又具有深层同构，因此“睽之时用大矣哉”。

  象传“君子以同而异”给出实践路径：君子在睽离之世不强求表面一致，而是先求“同”——找出共同底线；同时也承认并保留“异”，让差异有其可容之地。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Kui (Opposition) addresses 背离与分殊. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 睽卦核心是**“在分歧中经营共识，在孤立中保持通道”**。
  - “小事吉”提醒：在高度睽离的场域，先从小小的合作、微小的善意着手，而非企图一举化解所有对立。
  - 爻辞从“丧马勿逐，自复”到“睽孤遇元夫、交孚”再到“遇雨则吉”，逐层展示从误解走向重逢的过程。

- 详细解说：

  卦象上离下兑：火在上、泽在下，彼此相背；同时，上为明，下为悦，仍有共同基础——光明与愉悦的追求。睽并非彻底断绝，而是暂时的视线不合。

  初九“悔亡；丧马，勿逐，自复；见恶人，无咎”说明在睽离之初，面对损失与“恶人”不必急于追逐或决裂，而是暂避锋芒，允许事物自然回归。九二“遇主于巷，无咎”展示：即便在狭窄巷中，也可能偶然相遇主宰，象征在局促环境中仍有机会恢复联系。

  六三“见舆曳，其牛掣，其人天且劓，无初有终”则描绘睽离极端化的场景：制度与行为严重失衡，连驾车之人都受重刑；然而“无初有终”提示仍有翻转的余地。九四“睽孤，遇元夫，交孚，厉无咎”说明孤立之人若遇到有德的“元夫”，建立深度信任，即便有险也可无咎。

  六五“悔亡；厥宗噬肤，往何咎？”用“宗族咬肤”的亲密隐喻暗示：在更深的血缘与共同体层面，仍有互相支持的空间，只要前往相会，又有何咎？上九“睽孤，见豕负涂，载鬼一车；先张之弧，后说之弧；匪寇，婚媾；往遇雨则吉”则将睽离的极限画面推向高潮：起初一切看似极恶、怪诞，甚至让人紧张到张弓以备战；但最终发现那并非寇仇，而是婚媾之旅，待“遇雨”——象征情绪和疑虑被洗涤之后，疑云消散，转而为吉。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_344]` `[trigger: 卦=睽 AND 卦辞=小事吉]` `[factor_trigger: zhouyi_gua_kui AND zhouyi_guaci]` `[role: 主干]` 睽，小事吉：乖离之时，小事尚可成。 → 《周易·睽卦·卦辞》
  - `[ns_zhouyi_345]` `[trigger: 卦=睽 AND 彖传]` `[factor_trigger: zhouyi_gua_kui AND zhouyi_tuan AND zhouyi_guili_chengdu]` `[role: 主干依赖]` 火动而上，泽动而下。 → 《周易·睽卦·彖传》
  - `[ns_zhouyi_346]` `[trigger: 卦=睽 AND 象传=上火下泽]` `[factor_trigger: zhouyi_gua_kui AND zhouyi_xiang]` `[role: 主干依赖]` 上火下泽，睽；君子以同而异：火泽相违，和而不同。 → 《周易·睽卦·象传》
  - `[ns_zhouyi_347]` `[trigger: 卦=睽 AND 初九=悔亡丧马勿逐]` `[factor_trigger: zhouyi_gua_kui]` `[role: 条件分支]` 悔亡，丧马勿逐：失马不追，自复来归。 → 《周易·睽卦·爻辞》
  - `[ns_zhouyi_348]` `[trigger: 卦=睽 AND 九二=遇主于巷]` `[factor_trigger: zhouyi_gua_kui]` `[role: 条件分支]` 遇主于巷，无咎：在小巷偶遇，亦可相合。 → 《周易·睽卦·爻辞》
  - `[ns_zhouyi_349]` `[trigger: 卦=睽 AND 六三=见舆曳]` `[factor_trigger: zhouyi_gua_kui]` `[role: 例外处理]` 见舆曳，其牛掣：车被拖曳，牛被牵制。 → 《周易·睽卦·爻辞》
  - `[ns_zhouyi_350]` `[trigger: 卦=睽 AND 九四=睽孤遇元夫]` `[factor_trigger: zhouyi_gua_kui]` `[role: 条件分支]` 睽孤，遇元夫：孤立之中，遇贤人相助。 → 《周易·睽卦·爻辞》
  - `[ns_zhouyi_351]` `[trigger: 卦=睽 AND 六五=悔亡厥宗噬肤]` `[factor_trigger: zhouyi_gua_kui]` `[role: 主干依赖]` 悔亡，厥宗噬肤：与宗族相合，如食美肤。 → 《周易·睽卦·爻辞》
  - `[ns_zhouyi_352]` `[trigger: 卦=睽 AND 上九=睽孤见豕负涂]` `[factor_trigger: zhouyi_gua_kui]` `[role: 总结]` 睽孤，见豕负涂：极度孤立，所见皆疑。 → 《周易·睽卦·爻辞》
  - **中文**：
  - 卦辞"睽：小事吉"依通行王弼本；"睽"为乖离、背离，上离下兑，二女同居而志不同行。
  - "上火下泽"谓离火向上、兑泽向下，性质相反，象征乖离对立。
  - "以同而异"谓君子在睽离之时，求大同而存小异，和而不同。
  - "丧马勿逐，自复"谓失马不必追逐，待其自归，比喻不强求即可复合。
  - "见豕负涂，载鬼一车"之"豕负涂"谓猪背负泥土，初见以为怪异；"载鬼一车"谓以为车中满载鬼怪，皆为疑心误判之象。
  - "遇雨则吉"谓阴阳相济如遇雨，睽极而合，疑虑尽消。
  - **English**: Based on Wang Bi commentary edition. "睽" means opposition/separation. "上火下泽" shows fire and lake moving apart. "豕负涂/载鬼" describe misjudgments from suspicion. "遇雨" indicates reconciliation of opposites."""
    normalized_text_zh: str = """"""
    subject: str = "睽卦（䷥）"
    factor_refs: list = ['zhouyi_gua_038', 'symbol_two_daughters_proposal', 'symbol_pig_mud_proposal', 'principle_rain_fortune_proposal', 'principle_small_matters_proposal']
    
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
        l1_anchor="zy_v1.0.0_睽卦_001_L1",
    )
    version: str = "1.0.0"
