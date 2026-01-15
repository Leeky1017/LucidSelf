"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523716
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
    semantic_id="zpzq_v1.0.0_合化之义_以十干阴阳相配而成_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 合化之义以十干阴阳相配而成(SemanticEntry):
    """
    - **原文（source_text）**：
  合化之义，以十干阴阳相配而成。河图之数，以一二三四五配六七八十，先天之道也。故始于太阴之水，而终于冲气之土，以气而语其生之序也。盖未有五行之先，必先有...
    """
    
    original_text: str = """- **原文（source_text）**：
  合化之义，以十干阴阳相配而成。河图之数，以一二三四五配六七八十，先天之道也。故始于太阴之水，而终于冲气之土，以气而语其生之序也。盖未有五行之先，必先有阴阳老少，而后冲气，故生以土。终之既有五行，则万物又生于土，而水火木金，亦寄质焉，故以土先之。是以甲己相合之始，则化为土；土则生金，故乙庚化金次之；金生水，故丙辛化水又次之；水生木，故丁壬化木又次之；木生火，故戊癸化火又次之，而五行遍焉。先之以土，相生之序，自然如此，此十干合化之义也。

- 原注（原文注解）：
  　　本段先从“先天河图”与阴阳老少之序讲起，说明十干合化并不是随意配对，而是顺着先天数理与后天五行相生的秩序展开：
  - 阴阳老少先于五行；
  - 冲气成土，以土为先；
  - 再由土生金、金生水、水生木、木生火，织成十干五对的合化架构。

- 分字分词释义：
  - 合化之义：十干两两相合而化气成某一行的道理。
  - 以十干阴阳相配而成：以阴阳相对的两干配对，如甲己、乙庚、丙辛、丁壬、戊癸。
  - 河图之数：河图中一二三四五配六七八九十的数理结构，象征先天阴阳五行之布列。
  - 太阴之水：先天水气之始源，偏阴柔收敛的一端。
  - 冲气之土：阴阳老少与四行互相冲激所凝成的中和之土。
  - 生以土：在先天气机角度，土为冲气所结，是五行生发的起点。
  - 万物又生于土：在后天生长角度，万物仰赖土以生长与承载。
  - 甲己化土、乙庚化金、丙辛化水、丁壬化木、戊癸化火：十干五对合化对应五行的次序。

- **规范化释义（primary_lang_explained）**：
  十干合化，不是任意说“两个天干合成某行”，而是有一整套先天数理和后天生化的秩序作为基础。先从河图的数说起：一二三四五与六七八九十的配对，象征着先天阴阳数的组合。未有五行之先，必先有阴阳老少与“冲气”：阴阳老少相互冲激，凝结为土，所以“生以土”；等到五行体系成立之后，万物从土中萌生，而水、火、木、金也都寄托其形质于土上，所以“万物又生于土”。因此，在十干配合中，以甲己相合化土为始：既合两干之阴阳，又顺着“土生金、金生水、水生木、木生火”的次序往下排：甲己化土，乙庚化金，丙辛化水，丁壬化木，戊癸化火，五行由是遍布全局。这是“十干合化”的根本逻辑，不是杂乱无章的配对表。

- **完整对等诠释（secondary_lang_full）**：  
  This section clarifies that stem combination and transformation is not an arbitrary game of pairing any two stems and calling them a new element. The ten stems are arranged into five yin–yang pairs – Jia with Ji, Yi with Geng, Bing with Xin, Ding with Ren, and Wu with Gui – and these pairs follow a deeper numerical pattern known from the Hetu diagram. Before the Five Elements are named, there must first be yin and yang in their elder and younger phases whose interactions condense into Earth; from the standpoint of primordial qi, Earth is therefore the starting point of generation. After the fivefold system is established, all living things again depend on Earth as their ground, and the concrete substance of Water, Fire, Wood and Metal is also lodged in Earth. For this reason the combination sequence begins with Jia–Ji transforming into Earth. Following the path of mutual generation, Earth then gives rise to Metal, so Yi–Geng are said to transform into Metal; Metal gives Water, so Bing–Xin transform into Water; Water gives Wood, so Ding–Ren transform into Wood; Wood gives Fire, so Wu–Gui transform into Fire. In this way the five elements are fully covered, and the route from combination to transformation mirrors the structure of qi itself rather than a random list of convenient pairings.

- 详细解说：
  - 十干合化的次序是“土起、土终”的闭环，与“土居中以承载生化”的大结构相呼应。
  - 先讲“阴阳老少”和“冲气”后讲五行，意味着合化的本源在于气机结构，而不仅是五行名称。
  - 由双干合一行，再顺行相生，形成“从合到化，从化到生”的一条路径，为后文论“配合性情”打基础。

- 核心要点：
  - 十干合化有严格次序：甲己→土→金→水→木→火。
  - 土是先天冲气所结，也是后天万物所生，故为合化之始与枢纽。
  - 认清这条合化路径，是理解“合去用神/合来用神”“从化从格”等概念的前提。

- 应用推演：
  1) 识别命局中是否出现经典合化组合（甲己、乙庚、丙辛、丁壬、戊癸）。
  2) 判断该合是否具备“化”的条件（时令、根气、从众、不被破坏等）。
  3) 若真能化，再顺着“土→金→水→木→火”的链路，看其后续影响到哪些用神与格局。

- 反例与边界：
  - 只要见甲己同柱或同局，就武断说“必化土”，不问时令、根气与是否有他神干扰，是误用合化论。
  - 仅记“甲己化土”等口诀，而不清楚其“先有冲气土、后有土生五行”的背景，会在复杂命局中失准。

- 小例（示意）：
  - 甲己并见于辰戌等土旺之地，又值土旺时令，且局中多金少木，此时“甲己化土”用来成土金格局，多有其效；若木旺火炽，并无土根，此时甲己难谈真化，只能当作合而不化。

- 校勘与字词辨析：
  - “故始于太阴之水，而终于冲气之土，以气而语其生之序也”：此处“始于太阴之水”与“终于冲气之土”，皆站在“先天气机”角度言，不宜与后天五行相生顺序混淆。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_193]` `[trigger: 因成得败]` `[factor_trigger: geju_bencheng AND yizi_po_zhi AND result=bai]` `[role: 主干]` 格局本成，一字破之则败。 → 《子平真诠·论用神因成得败因败得成》#因成得败
  - `[ns_zpzy_194]` `[trigger: 成败转化]` `[factor_trigger: (yincheng_debai OR yinbai_decheng) AND yunlu_fenqi]` `[role: 主干]` 因成得败、因败得成，运路分歧。 → 《子平真诠·论用神因成得败因败得成》#转化
  - `[ns_zpzy_195]` `[trigger: 因败得成]` `[factor_trigger: geju_benbai AND yunzhong_dejiu AND result=cheng]` `[role: 主干]` 格局本败，运中得救则成。 → 《子平真诠·论用神因成得败因败得成》#因败得成
  - `[ns_zpzy_196]` `[trigger: 成败循环]` `[factor_trigger: chengbai_xiangyin AND fei_yiding_zhi_ju]` `[role: 主干]` 成败相因，非一定之局。 → 《子平真诠·论用神因成得败因败得成》#循环
  - `[ns_zpzy_197]` `[trigger: 会局之力]` `[factor_trigger: (sanhui OR sanhe) AND liliang_beizeng]` `[role: 主干]` 三会三合，力量倍增。 → 《子平真诠》#上卷
  - `[ns_zpzy_198]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_199]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_200]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_201]` `[trigger: 身弱从势]` `[factor_trigger: shenruo_wuyi AND cong_qi_wangshi]` `[role: 主干]` 身弱无依，从其旺势。 → 《子平真诠》#上卷
  - `[ns_zpzy_202]` `[trigger: 印绶护身]` `[factor_trigger: yinshou_hushen AND huasha_weiquan]` `[role: 主干]` 印绶护身，化煞为权。 → 《子平真诠》#上卷
  - `[ns_zpzy_203]` `[trigger: 相神得用]` `[factor_trigger: xiangshen_deyong AND fuge_yougong]` `[role: 主干]` 相神得用，辅格有功。 → 《子平真诠》#上卷
  - `[ns_zpzy_204]` `[trigger: 时柱归宿]` `[factor_trigger: pillar=shi AND role=guisu_zixi]` `[role: 例外处理]` 时柱归宿，子息之宫。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "合化之义，以十干阴阳相配而成"
    factor_refs: list = ['he', 'hehua', 'heshen', 'huachu_zhixing', 'conghua', 'chongqi_chengtu']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_合化之义_以十干阴阳相配而成_001_L1",
    )
    version: str = "1.0.0"
