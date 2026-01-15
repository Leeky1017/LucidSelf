"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725727
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
    semantic_id="zw_v1.0.0_23_其他杂曜_空劫_天刑_天姚等_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 23其他杂曜空劫天刑天姚等(SemanticEntry):
    """
    - 原文（source_text）：

  问：天空地劫所主若何？

  希夷先生答曰：

  二星守身命，遇吉则吉，遇凶则凶。如四杀冲照，轻者下贱，重者六畜之命，僧道不正，女子婢妾，刑克孤独。大抵二...
    """
    
    original_text: str = """- 原文（source_text）：

  问：天空地劫所主若何？

  希夷先生答曰：

  二星守身命，遇吉则吉，遇凶则凶。如四杀冲照，轻者下贱，重者六畜之命，僧道不正，女子婢妾，刑克孤独。大抵二星俱不宜见，定主破财。二限逢之必凶。

  歌曰：

  劫空为害最愁人，才智英雄误一身。只好为僧并学术，堆金积玉也须贫。

- 分字分词释义：

  - **天空**：象征上层支持抽离、外界结构“空洞化”的星曜，常使原有依靠突然失去。
  - **地劫**：象征基础与根基被侵蚀的虚耗之星，主财物流失、根基动摇。
  - **劫空**：天空地劫并见或与四杀同度时的合称，强调“见利反失”的落空感。
  - **四杀冲照**：与羊陀火铃等杀星对冲或同宫，放大空劫的破坏力，易致品级低贱、六畜之命。
  - **为僧并学术**：通过出家或专注学问，将现实层面的破败转化为精神或知识的积累，是传统给出的主要化解路径。

- 规范化释义（primary_lang_explained）：

  天空、地劫在紫微斗数中，并不是单纯“再多一颗凶星”，而是标记一种“落空”与“虚耗”的结构：它们守在身命宫时，往往表现为才智不低、眼界不差，却总在关键处失手——机会来得不稳，刚要抓住就消散；财物看似丰厚，结算时却发现支出与损失远大于想象。原文所谓“遇吉则吉，遇凶则凶”，强调的是放大性：如果周围多为吉曜，空劫有时只像是一层“轻盈”的滤镜，让人更容易放下执着；但一旦与羊陀火铃等四杀冲照，就会把本来就偏凶的结构拖向更低处，出现“轻者下贱，重者六畜之命”的极端情形。

  经文特别提醒空劫对财物与人际支持的消耗：二星“不宜见”，多主破财与孤独，甚至把僧道、婢妾等边缘身份写入象意之中。另一方面，歌诀又点出唯一较为正向的出路——“只好为僧并学术”：当物质与世俗路径反复落空时，若能主动把重心移向修行、研究、教学或技艺本身，空劫所带来的“空”反而可能成为减轻业力牵绊、看清事物本相的契机。整体而言，天空地劫问的不是“会不会一无所有”，而是：在几乎注定有缺口、有流失的领域中，命主究竟是死守既有、越守越空，还是学会以更轻的姿态持有与放下。

- 完整对等诠释（secondary_lang_full）：

  In Ziwei Doushu, Tiankong and Dijie do not simply add more malefic weight; they mark zones where form fails to hold content, where effort and outcome repeatedly fall out of alignment. When these stars guard the Life palace, they often describe people who are intelligent and capable yet find that opportunities evaporate just as they seem within reach, or that wealth passes quickly through their hands. The phrase "when meeting the auspicious, they are auspicious; when meeting the inauspicious, they are inauspicious" highlights their amplifying nature: surrounded by benefics, they can manifest as a lightness or detachment from worldly burden; entangled with the Four Killings, they deepen decline into humiliation, exploitation or lives reduced to serving others’ needs.

  The text repeatedly links this pair to financial erosion and social isolation, culminating in the judgement that both stars "are best not seen". Yet the verse also suggests a way to inhabit such a configuration: "best to become a monk or devote oneself to study; even with heaps of gold, one must know poverty." Read symbolically, this points to paths where value is stored not in accumulation but in understanding—spiritual practice, scholarship, disciplined craft. In these domains, the same emptiness that undermines possession can loosen attachment and sharpen insight. Tiankong and Dijie thus map the parts of a life where conventional success is fragile and easily lost, while hinting that if one stops insisting on ownership, the void they open may function less as a curse and more as a clearing.

- 核心要点：

  1. **空劫放大**：二星守身命，遇吉则吉遇凶则凶，有明显放大周围格局的作用.
  2. **破财孤独**：大抵不宜见，主破财、品级低贱与人际支持薄弱.
  3. **四杀冲照**：与四杀冲照时，轻则下贱，重则“六畜之命”、刑克孤独.
  4. **才智落空**：劫空常使才智英雄误一身，用力甚多、成果却屡屡落空.
  5. **僧道学术出路**：传统认为以僧道、学术之路承接空劫，是较可行的化解方式.

- 叙事素材（narrative_snippets）：

  - **遇吉随吉**："二星守身命，遇吉则吉，遇凶则凶"，天空地劫不自成吉凶，而是放大所遇格局.
  - **破财品级**："大抵二星俱不宜见，定主破财……轻者下贱，重者六畜之命"，从经济到身份都易有降格之象.
  - **劫空误身**："劫空为害最愁人，才智英雄误一身"，常见才华不低却屡屡在关键处失手.
  - **四杀冲照**："如四杀冲照……僧道不正，女子婢妾，刑克孤独"，说明在凶星包围下易滑向边缘身份与孤立状态.
  - **僧道学术**："只好为僧并学术，堆金积玉也须贫"，把空劫引向修行或学术，是传统给出的主要出口.
  - **现代应用**：空劫可作为评估"投入—产出错位"的指标——提醒哪些领域适合轻装前行、少做重押注."""
    normalized_text_zh: str = """"""
    subject: str = "23 其他杂曜（空劫、天刑、天姚等）"
    factor_refs: list = ['star_tiankong', 'star_dijie', 'pattern_jiekong', 'pattern_sisha_chongzhao', 'strategy_sengdao_xueshu']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_23_其他杂曜_空劫_天刑_天姚等_001_L1",
    )
    version: str = "1.0.0"
