"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899792
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
    semantic_id="zy_v1.0.0_泰卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 泰卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  泰：小往，大来，吉，亨。

  【彖传】
  《彖》曰：泰，小往，大来，吉，亨。
  则是天地交，而万物通也；
  上下交，而其志同也...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  泰：小往，大来，吉，亨。

  【彖传】
  《彖》曰：泰，小往，大来，吉，亨。
  则是天地交，而万物通也；
  上下交，而其志同也。
  内阳而外阴，内健而外顺；
  内君子而外小人；
  君子道长，小人道消也。

  【象传】
  《象》曰：天地交，泰；
  后以财成天地之道，辅相天地之宜，以左右民。

  【爻辞】
  初九，拔茅茹，以其汇，征吉。
  九二，包荒；用冯河；不遐遗；朋亡，得尚于中行。
  九三，无平不陂，无往不复；艰贞，无咎；勿恤其孚，于食有福。
  六四，翩翩；不富以其邻，不戒以孚。
  六五，帝乙归妹，以祉元吉。
  上六，城复于隍，勿用师；自邑告命，贞吝。

- 分字分词释义：

  - 泰：卦名，有安泰、通泰之意，象天地交泰、上下通达之时。
  - 小往，大来：小者退去，大者来到，比喻小人退居、君子进用。
  - 天地交：乾坤相交，阴阳和合，万物得以通达。
  - 财成天地之道：成就、裁成天地之道，使其条理化、制度化。
  - 辅相天地之宜：辅佐、顺应天地间种种适宜的时机与条件。
  - 拔茅茹，以其汇：拔除茅草，连带其根系相牵，比喻提携类聚之势。
  - 包荒：包容荒秽，度量广博。
  - 用冯河：不借舟船徒涉大河，象征敢于担当大险。
  - 不遐遗：不遗远方之人，不舍边缘之才。
  - 朋亡：朋党消散，不以小团体利害为重。
  - 中行：中正之道，为行事准绳。
  - 无平不陂，无往不复：事物发展有消长往返之理。
  - 艰贞：在艰难中守贞。
  - 翩翩：轻捷飘动之状，暗示地位和财势有浮动。
  - 不富以其邻：不积富于己，而与邻人共之。
  - 不戒以孚：不用戒备而以诚信相待。
  - 帝乙归妹：商王帝乙嫁女，以婚姻联姻和亲。
  - 祉：福祉、吉庆。
  - 城复于隍：城墙倾倒坠入壕沟，比喻形势已危。
  - 勿用师：不可轻启战端。
  - 自邑告命：在本国城邑中自行宣布命令，以内修代外争。

- **规范化释义（primary_lang_explained）**：

  泰卦表现的是“天地人三层皆通”的盛世状态：天地阴阳相交，万物通达，上下沟通，志向相合。卦辞“小往，大来，吉，亨”说明：小人之道退缩，君子之道进用，整体局面安泰而通达。在结构上，内阳外阴、内健外顺、内君子外小人，形成“君子居中为体，小人在外为用”的格局，因此君子之道日盛，小人之道日衰。

  爻辞依次描绘泰势展开的不同层面：初九“拔茅茹，以其汇，征吉”，以拔茅连根之象表示提携同类、群贤并进，只要志在外行，其征伐与行动必吉；九二“包荒，用冯河，不遐遗，朋亡，得尚于中行”则强调在泰世中健者应具宽广胸怀，能包容荒秽、敢行险事、不遗远人、不结朋党，而是以中行为尚；九三“无平不陂，无往不复；艰贞，无咎；勿恤其孚，于食有福”提醒即使在安泰之世，亦须知万物有盛衰起伏，在艰难中守贞反而可无咎，诚信不必过度焦虑，福报自在人间日用之处。

  六四“翩翩；不富以其邻，不戒以孚”从阴位描绘一种不固守自富、乐于与邻共享的态度，以诚信代替戒备；六五“帝乙归妹，以祉元吉”则以王者嫁女为象，指示处于君位者通过正当联姻与制度安排，使天下得福而大吉；上六“城复于隍，勿用师；自邑告命，贞吝”则发出警告：即便在泰世的末尾，若失察则有“城复于隍”的危险，此时不宜用兵，只宜内省整饬，若固守不变则为“贞吝”，有失泰道本意。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Tai, "Peace" or "Great Harmony", depicts a time when Heaven and Earth, rulers and people, all communicate freely so that life flows smoothly. The Judgment, "Tai: the small goes, the great comes; good fortune; success", shows a movement in which petty influences retreat while noble forces advance, creating an overall state of stability and prosperity. Structurally, Yang is within and Yin is without; strength and initiative are at the center, while flexibility and receptivity are on the outside. Noble people are inside as the core, petty people are pushed to the periphery as functionaries. This inner configuration causes the Way of the noble to grow stronger while the Way of the petty declines.

  The lines describe how this flourishing situation unfolds and how it must be safeguarded. The first line, "pulling up the grasses, with their roots entangled; pursuing brings good fortune", shows that when one virtuous person is raised up, many of like nature are brought along, forming a band of worthies whose outward movement and campaigns naturally bring success. The second line—"embracing the wastelands; using the ford of the river; not neglecting those afar; parties disappear; gaining honor in the middle path"—portrays the ideal leader in a time of peace: broad-minded enough to tolerate what is rough and imperfect, daring to take on great risks, refusing to abandon people in distant or marginal positions, and dissolving factions in favor of an upright middle way. The third line reminds us, "there is no level ground without a slope, no going forth without return"; even in Tai there is constant rise and fall. To hold fast to correctness amid difficulty removes blame; one need not anxiously worry about whether others fully trust him, for true blessing is found in the everyday realm of food, livelihood, and shared life.

  The fourth line, "lightly fluttering; not enriching himself but his neighbors; no warnings, yet there is trust", shows a softer position that willingly shares wealth and replaces defensive vigilance with sincerity. The fifth line, "King Di Yi marries off his younger sister; by this blessing there is great good fortune", uses the image of a royal marriage to illustrate how the central authority, in a Tai situation, maintains order through proper alliances and ritual rather than brute force, spreading blessing to the whole realm. The top line, "the city wall falls back into the moat; do not use the army; announce commands within your own city; perseverance brings distress", is a stark warning: at the very end of Tai, if vigilance is lost, collapse appears. In such a moment, external military action only accelerates disaster; the true response is to reform one’s own city and policies from within. To cling stubbornly to the old pattern is itself blameworthy and marks the turning point toward the hexagram Pi, "Obstruction".

- 核心要点：

  - 泰卦的核心是“盛世中的通与戒”：一方面天地交泰、上下通达，君子之道长，小人之道消；另一方面在泰势接近极点时，已隐含否塞的种子，需要未雨绸缪。
  - 爻辞从“群贤并进（拔茅以其汇）”“广包无私（包荒、不遐遗、朋亡）”“知盛衰之理（无平不陂、无往不复）”到“共享与联姻（不富以其邻、帝乙归妹）”“末尾警戒（城复于隍）”构成一条泰势生成与反转的轨迹。
  - 在实际应用中，泰卦往往对应“上升期或高点阶段”，关键不在于再求扩张，而在于稳中有让、广纳贤才、消解潜在隐患。

- 详细解说：

  卦象上坤下乾：天在下、地在上，象征天地交而气机上下往来。与乾坤两卦相比，泰卦处于“天地定位既定之后”的运转阶段，是乾坤之德在社会与历史层面展开的具体形态。因此，泰卦一方面承续乾之刚健、坤之厚载，另一方面又引出后续否卦，形成“泰—否”互为表里的局。

  初九与九二代表泰势初起阶段的“君子集结”：拔茅而征，表明以少拔多、以一引群；包荒、不遗远人、朋亡，则是以公道与广纳代替狭隘与朋比。九三处于天地交界之处，其“无平不陂，无往不复”提醒即使在泰时也要记得盛衰之理，艰贞无咎，说明在顺境中保有艰苦自守的态度，才是长久之道。

  六四、六五则是阴柔在上得位的两种可能：六四以“不富以其邻，不戒以孚”表现出一种乐施与无防的风度，但若脱离整体结构可能有轻率之虞；六五“帝乙归妹”则标志中央之位用柔和方式维护秩序，通过婚姻与礼乐体系连通诸侯与民情，使泰势得以巩固。上六“城复于隍，勿用师；自邑告命，贞吝”则预示泰极将否：城墙倒塌、危险已显，此时再用外力（行师）只会加速崩坏，真正的应对是自上而下地调整制度与命令，但若仍以故态自守，则成为“吝”，进入否卦的路口。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "泰卦（䷊）"
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
        l1_anchor="zy_v1.0.0_泰卦_001_L1",
    )
    version: str = "1.0.0"
