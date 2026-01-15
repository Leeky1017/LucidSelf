"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919535
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
    semantic_id="zy_v1.0.0_涣卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 涣卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  涣：亨。王假有庙，利涉大川，利贞。

  【彖传】
  《彖》曰：“涣亨，刚来而不穷，柔得位乎外而上同。王假有庙，王乃在中也。利涉大川...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  涣：亨。王假有庙，利涉大川，利贞。

  【彖传】
  《彖》曰：“涣亨，刚来而不穷，柔得位乎外而上同。王假有庙，王乃在中也。利涉大川，乘木有功也。”

  【象传】
  《象》曰：风行水上，涣；先王以享于帝，立庙。

  【爻辞】
  初六，用拯马壮，吉。
  九二，涣奔其机，悔亡。
  六三，涣其躬，无悔。
  六四，涣其群，元吉；涣有丘，匪夷所思。
  九五，涣汗其大号，涣王居，无咎。
  上九，涣其血，去逖出，无咎。

- 分字分词释义：

  - **涣**：本义为水流散开，引申为涣散、消解、疏通，在卦中多指“涣散中寻求重新凝聚”的过程。
  - **王假有庙**：“假”作“至、临”；王至宗庙而祭，在祖宗之“庙”中重新凝聚人心与秩序。
  - **利涉大川**：有利于渡过大河，比喻在涣散不安的局势中跨越重大危险。
  - **风行水上**：上巽为风，下坎为水，风吹水面，水波涣散，是涣之象，既有散开，也有重新流动的含义。
  - **用拯马壮**：以强壮之马施救，比喻在涣散之初用有力的行动援助他人。
  - **奔其机**：“机”可解为枢机、要害之处，“涣奔其机”指在涣散时迅速奔赴关键点以挽回局势。
  - **涣其躬**：使自身的执著与局限涣散、松解，象征在大局面前先放下自我。
  - **涣其群，涣有丘**：使群体由涣散中重新聚集于一“丘”，象征在分散状态中形成新的集中点。
  - **汗其大号**：汗如雨下，大号所出，比喻以庄严号令、宣告于众，疏导集体情绪。
  - **去逖出**：“逖”为远，指远离危险之地，脱离血光之灾。

- **规范化释义（primary_lang_explained）**：

  涣卦描写的是在“涣散与疏离”的局面下，如何重新凝聚与渡险。卦辞说：“涣：亨。王假有庙，利涉大川，利贞。”——在涣散之际，若君王能亲临宗庙、归依祖宗与制度之中轴，便有望亨通；以此为中心来组织力量，可以利于涉过大川般的险境，并利于在变动中保持正道。

  彖传指出：涣之所以“亨”，在于“刚来而不穷，柔得位乎外而上同”——阳刚之气来到内位而不至困穷，柔顺之爻在外位与中正之刚相合；王假有庙，则象征君主居中不失，成为重新凝聚的枢纽。利涉大川，则需“乘木有功”——借合适的工具和制度（如舟木）而渡险，而非徒凭一腔热血。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Huan (Dispersion) addresses 离散涣解. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 涣卦核心是**“在涣散中重建中心、化散为通”**。
  - 宗庙与“大号”代表在价值与制度层面重新确认共同基点。
  - 各爻通过“拯马壮”“涣其躬”“涣其群”“涣其血”等象，展示从局部救援到个人松绑、群体再聚与远离危险的多重路径。

- 详细解说：

  卦象为上巽下坎：风行水上、水波涣散，若无中心则漫无边际；然而水的流动也意味着可以“由散而通”，关键在于有否“庙”与“丘”这样的聚焦点。先王“以享于帝，立庙”，通过建立宗庙，将天命、祖训与现实政治汇聚于一处，使涣散的人心有可依托之所。

  初六“用拯马壮，吉。”处涣之始，宜以强健之资源援救危困者，如用壮马拉人出险；行动及时而有力，则可得吉。九二“涣奔其机，悔亡。”则强调在涣散局势中迅速奔赴关键枢机：若能抓住“机”，则先前踌躇之悔可亡。

  六三“涣其躬，无悔。”提示：在更深一层，需要“涣其躬”——不再只护卫自我小圈，愿意让个人之身融入更大局势之流动，如此可免后悔。六四“涣其群，元吉；涣有丘，匪夷所思。”则描绘了一种“从散到聚”的转折：群体一度涣散，但在新的“丘”——新的高地或中心之下重新聚合，此一局面在旁人看来或许难以理解，却是“元吉”的结构性转化。

  九五“涣汗其大号，涣王居，无咎。”表现的是君王位上的涣：通过发布重大号令、公开表达立场，如汗出般尽情疏发，使聚散有度；“涣王居”意味着王位本身也在涣散的流中重新被确认与安置，因此可以无咎。上九“涣其血，去逖出，无咎。”则是涣卦末尾的“远离危险”：将血光之象（杀戮、仇怨）从自身中涣散出去，远离其所聚集之地，转入更远处，由此得以无咎。


#### L2 语义提取

- **主题**：离散涣解，如何在此情境中顺应天道、把握时机、实现人生目标。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_533]` `[trigger: 卦=涣 AND 卦辞=亨王假有庙]` `[factor_trigger: zhouyi_gua_huan AND zhouyi_guaci AND zhouyi_juji_chengdu]` `[role: 主干]` 涣，亨；王假有庙，利涉大川：涣散之时，王以宗庙聚心。 → 《周易·涣卦·卦辞》
  - `[ns_zhouyi_534]` `[trigger: 卦=涣 AND 彖传]` `[factor_trigger: zhouyi_gua_huan AND zhouyi_tuan AND zhouyi_huansan_chengdu]` `[role: 主干依赖]` 亨。刚来而不穷。 → 《周易·涣卦·彖传》
  - `[ns_zhouyi_535]` `[trigger: 卦=涣 AND 象传=风行水上]` `[factor_trigger: zhouyi_gua_huan AND zhouyi_xiang]` `[role: 主干依赖]` 风行水上，涣；先王以享于帝立庙：风行水上，涣散成波。 → 《周易·涣卦·象传》
  - `[ns_zhouyi_536]` `[trigger: 卦=涣 AND 初六=用拯马壮吉]` `[factor_trigger: zhouyi_gua_huan]` `[role: 条件分支]` 用拯马壮，吉：以壮马拯救涣散。 → 《周易·涣卦·爻辞》
  - `[ns_zhouyi_537]` `[trigger: 卦=涣 AND 九二=涣奔其机]` `[factor_trigger: zhouyi_gua_huan]` `[role: 条件分支]` 涣奔其机，悔亡：奔走于机要之处。 → 《周易·涣卦·爻辞》
  - `[ns_zhouyi_538]` `[trigger: 卦=涣 AND 六三=涣其躬]` `[factor_trigger: zhouyi_gua_huan]` `[role: 条件分支]` 涣其躬，无悔：涣散自身之私。 → 《周易·涣卦·爻辞》
  - `[ns_zhouyi_539]` `[trigger: 卦=涣 AND 六四=涣其群]` `[factor_trigger: zhouyi_gua_huan]` `[role: 主干依赖]` 涣其群，元吉：涣散朋党，大为吉祥。 → 《周易·涣卦·爻辞》
  - `[ns_zhouyi_540]` `[trigger: 卦=涣 AND 九五=涣汗其大号]` `[factor_trigger: zhouyi_gua_huan]` `[role: 主干依赖]` 涣汗其大号，涣王居：如汗之出，号令天下。 → 《周易·涣卦·爻辞》
  - `[ns_zhouyi_541]` `[trigger: 卦=涣 AND 上九=涣其血去逖出]` `[factor_trigger: zhouyi_gua_huan]` `[role: 总结]` 涣其血，去逖出：涣散血腥，远离灾祸。 → 《周易·涣卦·爻辞》
  - **中文**：
  - 卦辞"涣：亨。王假有庙，利涉大川，利贞"依通行王弼本；"涣"为离散、涣散，王者以宗庙凝聚人心而化涣为聚。
  - "风行水上"谓巽风在坎水之上，风吹水面成涟漪，象征涣散之状。
  - "用拯马壮"中"拯"释为救援，以壮马拯救涣散之局。
  - "涣奔其机"之"机"或释为几案、或释为机要，奔于机要之处以应涣。
  - "涣其躬"谓涣散自身之私欲；"涣其群"谓涣散朋党私结，皆为正面之涣。
  - "涣汗其大号"以汗喻号令，汗出则不可复收，号令天下亦当如此决绝不回。
  - **English**: Based on Wang Bi commentary edition. "涣" means dispersion. "王假有庙" shows king unifying through ancestral temple. "风行水上" depicts wind on water creating ripples. "涣汗" likens royal decree to sweat—once issued, cannot be recalled."""
    normalized_text_zh: str = """"""
    subject: str = "涣卦（䷺）"
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
        l1_anchor="zy_v1.0.0_涣卦_001_L1",
    )
    version: str = "1.0.0"
