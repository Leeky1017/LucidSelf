"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042180
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
    semantic_id="smth_v1.0.0_洛书点数与五行方位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 洛书点数与五行方位(SemanticEntry):
    """
    - **原文（source_text）**：
  夫洛马出书之初，有一白点六黑点在背，近尾；七白点二黑点在背，近洛书之图头；三白点八黑点在背之左，九白点四黑点在背之右；五白点十黑点在背之中。大挠定之一...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫洛马出书之初，有一白点六黑点在背，近尾；七白点二黑点在背，近洛书之图头；三白点八黑点在背之左，九白点四黑点在背之右；五白点十黑点在背之中。大挠定之一六在下，合于北，生水亥子属焉；二七在上，合于南，生火巳午属焉；三八在左，合于东，生木寅卯属焉；四九在右，合于西，生金申酉属焉；五十在中，合于中，生土辰戌丑未属焉。四维也，斯地之气重浊焉。

- **分字分词释义**：
  - **洛马出书**：传说洛水之神以神龟负书而出，即所谓「洛书」。
  - **一六、二七、三八、四九、五十**：奇偶配对的点数组合，用以标示方位与五行根数。
  - **背、头、左、右、中**：以神龟之身为图，分别对应北、南、东、西、中五方。
  - **四维之气重浊**：四隅为土气所聚之处，较为凝重浑浊。

- **规范化释义（primary_lang_explained）**：
  本段描述洛书在神龟背上的点数分布：一六居下为北方之水，二七居上为南方之火，三八居左为东方之木，四九居右为西方之金，五十居中为中央之土。通过奇偶相配的点数，把五行根数与方位严密对应起来。所谓「四维之气重浊」，是说四隅之地土气较重，用以完成中央土对四方的统摄。

- **完整对等诠释（secondary_lang_full）**：
  The Luo River Diagram describes the distribution of paired numbers on the divine turtle's back: one-six positioned below represents Northern Water, two-seven above for Southern Fire, three-eight on the left for Eastern Wood, four-nine on the right for Western Metal, and five-ten in the center for Central Earth. Through these odd-even paired numbers, the root numerology of Five Elements is strictly correlated with cardinal directions. The phrase "four corners heavy and turbid" indicates that the four diagonal positions carry denser Earth qi, completing the central Earth's governance over the four directions. This system establishes the foundational coordinate framework for destiny analysis, encoding orientation-element relationships through numerology rather than arbitrary mystical arithmetic.

- **核心要点**：
  - 洛书点数并非单纯的数字游戏，而是用一组有序的数列编码「方位—五行—阴阳」的整体结构。
  - 一六水、二七火、三八木、四九金、五十土，为后世术数中「河洛数理」与旺衰判断的根本对应。
  - 命局中若论「数与方位」，实质上皆在沿用这一套河洛数与五行方位的对应框架。

- **详细解说**：
  1) 在传统命理阅读中，可将「洛书点数」视作干支方位与五行分布的底层坐标系：先定一六水、二七火、三八木、四九金、五十土的方位，再映射到命盘的年、月、日、时；
  2) 在现代建模中，可把洛书九宫抽象为一个 3×3 网格，将不同方位上的五行强弱、事件权重映射到此网格中；
  3) 分析命盘时，若有明显的「某一宫过强」或「某一宫为空」现象，可用洛书坐标来解释该方位在现实生活中的重点或缺失（如事业、居住环境、健康部位）；
  4) 在系统实现上，可将「洛书方位—五行—干支」做成独立的映射表，供解释层按需调用，而不与具体推命规则耦合。

- 反例与边界：
  - 不应将洛书点数当作神秘算术，认为「数字本身」即可决定吉凶，而忽略其只是方位与五行的编码方式；
  - 不宜把后世各种「数字风水」完全等同于河洛本义，混淆了原始数理与民间演绎；
  - 在工程中，若把洛书映射硬编码进所有规则，而不留出方位建模的扩展层，将来调整坐标系或接入真实空间数据会非常困难；
  - 反过来，完全抛弃河洛坐标，只在一维上看「木火土金水多少」，会丢失「同一五行在不同方位、不同宫位作用不同」这一关键信息。

- 小例（示意）：
  - 某命盘水气集中于一六宫与北方方位，对应现实中长期居于寒湿环境、职业又与信息流通（水）有关，系统可用「洛书水势偏北」来解释其思维偏冷静、行动偏保守；
  - 在工程试验中，将用户行为按「九宫方位」聚类，与实际地理或社交网络结构对照，可检验「洛书型」坐标是否比简单的东西南北划分更有解释力。

- **校勘与字词辨析**：
  - 「洛马出书」一作「洛水出书」「洛龟负书」，此处据底本存「马」字，当作洛神所乘之马、代指洛水神迹解。
  - **English**：
    - Stem-branch combinations explained with modern terminology; classical poetic imagery preserved with practical interpretation."""
    normalized_text_zh: str = """"""
    subject: str = "洛书点数与五行方位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_洛书点数与五行方位_001_L1",
    )
    version: str = "1.0.0"
