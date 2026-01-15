"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919389
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
    semantic_id="zy_v1.0.0_姤卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 姤卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  姤：女壮，勿用取女。

  【彖传】
  《彖》曰：“姤，遇也，柔遇刚也。勿用取女，不可与长也。天地相遇，品物咸章也。刚遇中正，天下大...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  姤：女壮，勿用取女。

  【彖传】
  《彖》曰：“姤，遇也，柔遇刚也。勿用取女，不可与长也。天地相遇，品物咸章也。刚遇中正，天下大行也。姤之时义大矣哉！”

  【象传】
  《象》曰：天下有风，姤；后以施命诰四方。

  【爻辞】
  初六，系于金柅，贞吉；有攸往，见凶，羸豕孚踟躅。
  九二，包有鱼，无咎，不利宾。
  九三，臀无肤，其行次且，厉，无大咎。
  九四，包无鱼，起凶。
  九五，以杞包瓜，含章，有陨自天。
  上九，姤其角，吝，无咎。

- 分字分词释义：

  - **姤**：本义为遇、相逢，卦取“阴遇阳”之象，特指在并未充分准备的情形下的邂逅相遇。
  - **女壮，勿用取女**：女子强壮，或指年、势、性情之强盛，不宜娶为正妻。并非贬抑女性，而是提示阴阳失衡、结构难以长久。
  - **柔遇刚也**：一阴在上，遇下体诸阳，为“柔遇刚”；既是机会，也是风险。
  - **不可与长也**：这种相遇不宜长久维系，如果当作恒久结构，就会积累问题。
  - **天下有风**：下乾为天，上巽为风，风行天下，象征命令与影响扩散至四方。
  - **施命诰四方**：君主在“遇时”颁布号令、诰命，善用机缘，使之化为秩序而非混乱。
  - **系于金柅**：金柅为车闸，比喻以坚固装置牵系、遏止车轮，象征在初遇之时要先自制约束。
  - **羸豕孚踟躅**：瘦猪被绑而仍踟躇不安，示意欲望虽受约束，内心仍动荡需再加节制。
  - **包有鱼 / 包无鱼**：“包”为包裹、器皿，鱼多指欲望或利益。“有鱼”尚有实，“无鱼”则空虚、徒具其名。
  - **含章，有陨自天**：内含文采德行，终有“陨自天”的外来变故，提示偶然性的机缘与打击。
  - **姤其角**：在“角”处相遇，取“触角、尖端”之象，象征在矛盾尖锐处遭遇，虽有可叹但终无大咎。

- **规范化释义（primary_lang_explained）**：

  姤卦承接夬卦的“决断之后必有遇”。《序卦》曰：“决必有遇，故受之以姤。”当系统完成一次“夬”的大决之后，新的相遇、新的因缘便随之而来。但这种“遇”往往带有偶然性、突发性，以及结构上的不对称。

  卦辞“姤：女壮，勿用取女”用婚嫁之象说明：当一方已经“过壮”，不论年龄、地位还是性情，都可能与另一方形成失衡结构。此时若勉强成婚，难以“与长”，即难以长久稳定。彖传以“柔遇刚”“天地相遇，品物咸章”扩展这一点——相遇本身是天地运行的一部分，可使品类彰显、万物归位，但若在“柔遇刚”的结构中不察阴阳之度，就会埋下隐患。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Gou (Encounter) addresses 不期而遇. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 姤卦的核心是**“偶然相遇中的结构失衡与自我节制”**。
  - 它既提醒“遇”的珍贵，也提醒“不可与长”的限度：不是所有邂逅都要强行固化为长期结构。
  - 爻辞从“初遇先系、谨慎前行”，到“有鱼/无鱼”的得失，对应于在机会与欲望面前的取舍与节制。

- 详细解说：

  卦象为上巽下乾：乾为天、为健，巽为风、为入。风行天下，入乎万物，正是“遇”的外在景象；而内在则是“刚健”在下，承接来自上的柔风。与夬卦“泽上于天”的决断不同，姤卦更像是决断后迎来的种种新接触与机缘。

  初六“系于金柅，贞吉；有攸往，见凶，羸豕孚踟躅”提示：在初遇阶段必须“先系后行”，先把“车轮”紧紧刹住，守住贞正才吉；若急于“有攸往”，则易见凶险。羸猪被捆仍踟躇不安，犹如欲望尚未真正安定，需要时间与更深的约束。

  九二“包有鱼，无咎，不利宾”说明：内中有实（有鱼），自己享用则无咎，但尚不宜对外“待宾”，提示在资源尚未稳定前勿急于扩张分享。九三“臀无肤，其行次且，厉，无大咎”则展现因迟疑与磨擦带来的痛感：在行动层面已经磨损、步伐蹒跚，却仍有机会止损，不至大祸。

  九四“包无鱼，起凶”转为警示：若一味维持空壳结构，“包”中已无“鱼”，再行推进则起凶。九五“以杞包瓜，含章，有陨自天”强调另一种状况：虽处中位而内含文采，但外在局势的突变（“陨自天”）仍可能打断原本的轨迹，提醒在“遇”的结构中要接受不可控的因素。上九“姤其角，吝，无咎”作为收束：在局势末端再遇冲突尖角，虽有可叹，终能无咎——只要不再逞强延续不当结构。


#### L2 语义提取

- **主题**：不期而遇，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_398]` `[trigger: 卦=姤 AND 卦辞=女壮勿用取女]` `[factor_trigger: zhouyi_gua_gou AND zhouyi_guaci]` `[role: 主干]` 姤，女壮，勿用取女：阴气初生，须防女壮。 → 《周易·姤卦·卦辞》
  - `[ns_zhouyi_399]` `[trigger: 卦=姤 AND 彖传]` `[factor_trigger: zhouyi_gua_gou AND zhouyi_tuan AND zhouyi_xiangyu_chengdu]` `[role: 主干依赖]` 遇也。柔遇刚也。 → 《周易·姤卦·彖传》
  - `[ns_zhouyi_400]` `[trigger: 卦=姤 AND 象传=天下有风]` `[factor_trigger: zhouyi_gua_gou AND zhouyi_xiang]` `[role: 主干依赖]` 天下有风，姤；后以施命诰四方：风行天下，传布号令。 → 《周易·姤卦·象传》
  - `[ns_zhouyi_401]` `[trigger: 卦=姤 AND 初六=系于金柅]` `[factor_trigger: zhouyi_gua_gou]` `[role: 条件分支]` 系于金柅，贞吉：系于金闸，守正则吉。 → 《周易·姤卦·爻辞》
  - `[ns_zhouyi_402]` `[trigger: 卦=姤 AND 九二=包有鱼]` `[factor_trigger: zhouyi_gua_gou]` `[role: 条件分支]` 包有鱼，无咎，不利宾：厨中有鱼，不宜待客。 → 《周易·姤卦·爻辞》
  - `[ns_zhouyi_403]` `[trigger: 卦=姤 AND 九三=臀无肤]` `[factor_trigger: zhouyi_gua_gou]` `[role: 条件分支]` 臀无肤，其行次且：行动不便，进退维艰。 → 《周易·姤卦·爻辞》
  - `[ns_zhouyi_404]` `[trigger: 卦=姤 AND 九四=包无鱼]` `[factor_trigger: zhouyi_gua_gou]` `[role: 条件分支]` 包无鱼，起凶：厨中无鱼，将起凶咎。 → 《周易·姤卦·爻辞》
  - `[ns_zhouyi_405]` `[trigger: 卦=姤 AND 九五=以杞包瓜]` `[factor_trigger: zhouyi_gua_gou]` `[role: 主干依赖]` 以杞包瓜，含章，有陨自天：杞木包瓜，含德而待天佑。 → 《周易·姤卦·爻辞》
  - `[ns_zhouyi_406]` `[trigger: 卦=姤 AND 上九=姤其角]` `[factor_trigger: zhouyi_gua_gou]` `[role: 总结]` 姤其角，吝，无咎：遇于角落，虽吝而无咎。 → 《周易·姤卦·爻辞》
  - **中文**：
  - 卦辞"姤：女壮，勿用取女"依通行王弼本；"姤"为遇、相遇，一阴遇五阳，与夬卦相对。
  - "天下有风"谓巽风在乾天之下，风行天下，象征号令传布四方。
  - "女壮，勿用取女"谓阴气初生而壮，如此之女不可取，恐不可与久处。
  - "系于金柅"之"柅"为刹车之具，系于金柅而止其进，守正则吉。
  - "包有鱼/包无鱼"以厨包有无鱼喻遇合之有无，有鱼则无咎，无鱼则凶。
  - "以杞包瓜"之"杞"为杞柳，以杞木包裹瓜果，象征含章守德而待天佑。
  - **English**: Based on Wang Bi commentary edition. "姤" means encounter—one yin meeting five yangs. "女壮" warns of strong yin not suitable for marriage. "金柅" is a brake. "包有鱼/无鱼" uses fish as metaphor for encounter. "杞包瓜" symbolizes patient virtue."""
    normalized_text_zh: str = """"""
    subject: str = "姤卦（䷫）"
    factor_refs: list = ['zhouyi_gua_044', 'principle_yielding_meets_firm_proposal', 'principle_woman_strong_not_marry_proposal', 'symbol_wrapped_fish_proposal', 'method_tied_metal_brake_proposal']
    
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
        l1_anchor="zy_v1.0.0_姤卦_001_L1",
    )
    version: str = "1.0.0"
