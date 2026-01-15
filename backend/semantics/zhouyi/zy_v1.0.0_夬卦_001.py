"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919378
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
    semantic_id="zy_v1.0.0_夬卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 夬卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  夬：扬于王庭，孚号有厉；告自邑，不利即戎；利有攸往。

  【彖传】
  《彖》曰：“夬，决也，刚决柔也。健而说，决而和。扬于王庭，柔...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  夬：扬于王庭，孚号有厉；告自邑，不利即戎；利有攸往。

  【彖传】
  《彖》曰：“夬，决也，刚决柔也。健而说，决而和。扬于王庭，柔乘五刚也。孚号有厉，其危乃光也。告自邑，不利即戎，所尚乃穷也。利有攸往，刚长乃终也。”

  【象传】
  《象》曰：泽上于天，夬；君子以施禄及下，居德则忌。

  【爻辞】
  初九，壮于前趾，往不胜为咎。
  九二，惕号，莫夜有戎，勿恤。
  九三，壮于頄，有凶。君子夬夬，独行，遇雨若濡，有愠，无咎。
  九四，臀无肤，其行次且。牵羊悔亡，闻言不信。
  九五，苋陆夬夬，中行，无咎。
  上六，无号，终有凶。

- 分字分词释义：

  - **夬**：本义为决、决断，有“决水决堤”“决去阴柔”之象，卦名取阳刚决去残余阴柔之意。
  - **扬于王庭**：在王庭公开宣示，象征在最高、公正的场域之中作出决断，而非私下暗行。
  - **孚号有厉**：以真诚之心发出疾呼、号令，过程中有危险、有压力，但其“危”反使正道之光更为彰显。
  - **告自邑，不利即戎**：先在本邑、本域内告示和整饬，而不宜立刻发动战争；提示决断之前要有充分的宣示与内部整顿。
  - **利有攸往**：在完成必要宣告与整顿之后，才有利于前往执行决断之事。
  - **泽上于天**：下乾为天，上兑为泽，泽气上腾至天，成“泽上于天”之象，喻内有刚健、外有喜悦，决断虽烈而不失其和。
  - **施禄及下**：把俸禄、恩惠施予下民，表示决断的结果要落实到具体民生，而非只停留在权力层面。
  - **惕号，莫夜有戎，勿恤**：惕然警觉而呼号，是因为夜半有兵戎之警，但只要决断得当，就无需过度忧惧。
  - **壮于頄**：頄为面颊骨，形容阳刚之气上冲于面，若仅是逞强之“壮”，反为有凶之兆。
  - **夬夬**：果决坚断之貌，强调决断时的决绝与不回避。
  - **牵羊悔亡**：以绳牵羊，比喻在决断中采取柔和牵引的方式，能够消解悔恨。
  - **苋陆夬夬**：苋陆为野草，易生易败，象征若不节制的决断易生偏激；“中行无咎”提示在中道中实施决断方可无咎。
  - **无号，终有凶**：完全不发出号令、不作必要沟通，固然免一时之险，却因失时失机而终致大凶。

- **规范化释义（primary_lang_explained）**：

  夬卦与前一卦益卦相承。《序卦》曰：“益而不已必决，故受之以夬。”——当“益”的过程失去节制，就会发展到必须“决断”的地步。卦辞说：“夬：扬于王庭，孚号有厉；告自邑，不利即戎；利有攸往。”强调的是在大势已成、阳刚已长之时，如何以合宜方式清除残余阴柔、解决积累已久的结构问题。

  “扬于王庭”说明一切决断要在公开、公正的场域中进行，而非密室操作；“孚号有厉”点明，真正有诚意的号令，必然伴随风险与压力，这恰恰是其价值所在。“告自邑，不利即戎”提醒：先在本地宣告、整顿，修正自身结构，再谈对外行动；不可因内部尚未理顺就急于“即戎”。只有完成这套程序，“利有攸往”的前行才真正具备道义与现实基础。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Guai (Breakthrough) addresses 决断与突破. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 夬卦的核心是**“阳刚已长之时，如何以公开、公正且有限度的方式作出决断”**。
  - 决断不仅是“去柔”的动作，还包含“施禄及下”的责任：决断之后必须让多数人真正受益。
  - 爻辞呈现了从“初始逞强的危险”、“警觉夜戎”、“君子独行之夬夬”、“以牵羊化悔”、“中行无咎”到“终无号而有凶”的一整套决断光谱。

- 详细解说：

  卦象为上兑下乾：乾为天、刚健，兑为泽、为悦，内刚而外悦，形成“健而说，决而和”的结构。五阳在下，一阴在上，被五阳群阳所决，是“刚决柔”的局面。与损、益偏重在“损益调节”不同，夬卦聚焦在“时机已至时的最终决断”。

  初九“壮于前趾，往不胜为咎”提示：在决断刚刚起步时，若只凭脚趾之勇、逞一时之壮，贸然前往，反而不胜而有咎。九二“惕号，莫夜有戎，勿恤”则把这种决断放在实际危局中：夜半有兵戎惊扰，需要警觉呼号，但若其位得中、应时而行，则可“勿恤”。

  九三“壮于頄，有凶。君子夬夬，独行，遇雨若濡，有愠，无咎”进一步区分“暴烈之壮”与“君子之决”。前者是面骨高突、怒容满面，难免有凶；后者则是君子在无人支持时仍能独自按义决断，虽会“遇雨若濡，有愠”——过程辛苦、心中不免郁闷，却不至于有咎。九四“臀无肤，其行次且。牵羊悔亡，闻言不信”则指出：身处中层，当两边拉扯、坐立难安之时，若能以“牵羊”式的温和牵引来处理下层力量，便可消弭悔恨；若只一味不信善言，则难免拖泥带水。

  九五“苋陆夬夬，中行，无咎”强调，“夬夬”之决不可脱离“中行”：决断若像苋陆野草，生长过快、枯败也快，则易陷偏激；唯有居中而行，才不致有咎。上六“无号，终有凶”作为对照：当阴柔处于顶部，若因惧怕风险而干脆“不号”、不发出任何号令，似可一时避险，最终却导致积弊难返，酿成更大之凶。



- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_389]` `[trigger: 卦=夬 AND 卦辞=扬于王庭]` `[factor_trigger: zhouyi_gua_guai AND zhouyi_guaci]` `[role: 主干]` 夬，扬于王庭，孚号有厉：决断之时，当公开昭示。 → 《周易·夬卦·卦辞》
  - `[ns_zhouyi_390]` `[trigger: 卦=夬 AND 彖传]` `[factor_trigger: zhouyi_gua_guai AND zhouyi_tuan AND zhouyi_jueduan_chengdu]` `[role: 主干依赖]` 决也。刚决柔也。健而说。 → 《周易·夬卦·彖传》
  - `[ns_zhouyi_391]` `[trigger: 卦=夬 AND 象传=泽上于天]` `[factor_trigger: zhouyi_gua_guai AND zhouyi_xiang]` `[role: 主干依赖]` 泽上于天，夬；君子以施禄及下：如泽升于天，施惠于下。 → 《周易·夬卦·象传》
  - `[ns_zhouyi_392]` `[trigger: 卦=夬 AND 初九=壮于前趾]` `[factor_trigger: zhouyi_gua_guai]` `[role: 条件分支]` 壮于前趾，往不胜：力壮于趾，前往难胜。 → 《周易·夬卦·爻辞》
  - `[ns_zhouyi_393]` `[trigger: 卦=夬 AND 九二=惕号]` `[factor_trigger: zhouyi_gua_guai]` `[role: 条件分支]` 惕号，莫夜有戎，勿恤：警惕呼号，夜有戎兵亦勿忧。 → 《周易·夬卦·爻辞》
  - `[ns_zhouyi_394]` `[trigger: 卦=夬 AND 九三=壮于頄]` `[factor_trigger: zhouyi_gua_guai]` `[role: 条件分支]` 壮于頄，有凶：力壮于颧骨，独断则凶。 → 《周易·夬卦·爻辞》
  - `[ns_zhouyi_395]` `[trigger: 卦=夬 AND 九四=臀无肤]` `[factor_trigger: zhouyi_gua_guai]` `[role: 条件分支]` 臀无肤，其行次且：臀部无肉，行动不便。 → 《周易·夬卦·爻辞》
  - `[ns_zhouyi_396]` `[trigger: 卦=夬 AND 九五=苋陆夬夬]` `[factor_trigger: zhouyi_gua_guai]` `[role: 主干依赖]` 苋陆夬夬，中行无咎：如除苋陆之草，行于中道。 → 《周易·夬卦·爻辞》
  - `[ns_zhouyi_397]` `[trigger: 卦=夬 AND 上六=无号终有凶]` `[factor_trigger: zhouyi_gua_guai]` `[role: 总结]` 无号，终有凶：不呼号警示，终遭凶咎。 → 《周易·夬卦·爻辞》
  - **中文**：
  - 卦辞"夬：扬于王庭，孚号有厉；告自邑，不利即戎；利有攸往"依通行王弼本；"夬"为决断，五阳决一阴。
  - "泽上于天"谓兑泽升于乾天之上，水汽上升将决为雨，象征阳刚即将决去阴柔。
  - "扬于王庭"谓公开于朝廷宣示，光明正大而非暗中行事。
  - "孚号有厉"谓以诚信发号，虽有危厉但可无咎。
  - "壮于頄"之"頄"为颧骨，壮于颧骨喻独断面目可憎之象。
  - "苋陆夬夬"之"苋陆"为野草，夬夬然果决除之，示中行无咎。
  - **English**: Based on Wang Bi commentary edition. "夬" means breakthrough/decision—five yangs removing one yin. "扬于王庭" requires open declaration. "頄" is cheekbone—obstinate appearance. "苋陆" is a weed to be decisively removed."""
    normalized_text_zh: str = """"""
    subject: str = "夬卦（䷪）"
    factor_refs: list = ['zhouyi_gua_043', 'principle_proclaim_court_proposal', 'principle_firm_resolves_yielding_proposal', 'principle_sincere_call_danger_proposal', 'principle_not_favor_arms_proposal']
    
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
        l1_anchor="zy_v1.0.0_夬卦_001_L1",
    )
    version: str = "1.0.0"
