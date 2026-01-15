"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899877
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
    semantic_id="zy_v1.0.0_观卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 观卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  观：盥而不荐，有孚颙若。

  【彖传】
  《彖》曰：“大观在上，顺而巽，中正以观天下。‘观，盥而不荐，有孚颙若’，下观而化也。观天...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  观：盥而不荐，有孚颙若。

  【彖传】
  《彖》曰：“大观在上，顺而巽，中正以观天下。‘观，盥而不荐，有孚颙若’，下观而化也。观天之神道，而四时不忒；圣人以神道设教，而天下服矣。”

  【象传】
  《象》曰：风行地上，观；先王以省方观民设教。

  【爻辞】
  初六，童观，小人无咎，君子吝。
  六二，𬮭观，利女贞。
  六三，观我生，进退。
  六四，观国之光，利用宾于王。
  九五，观我生，君子无咎。
  上九，观其生，君子无咎。

- 分字分词释义：

  - **观**：观看、观察、瞻仰，既指下观上、仰观，也指上观下、察民情，更可引申为自我观照。
  - **盥而不荐**：盥，洗手、沐浴净身；荐，进献祭品。只观祭前的沐浴之礼而不需看到献祭，强调重在内心虔敬而非外在隆重。
  - **有孚颙若**：内怀诚信之“孚”，外现庄严可仰之神色，“颙若”形容肃敬庄重的仪态。
  - **大观在上，顺而巽，中正以观天下**：在位者具有宏大视野，又能柔顺谦巽，以中正之心观天下，不以私意偏视。
  - **风行地上**：风在地上流行，悄然而遍，象征教化之风通过“观”而广泛渗透。
  - **童观 / 𬮭观**：童观如孩童见物，浅陋而不自知；𬮭观为暗中窥视，只适于“女贞”情境，象征内敛谨慎。
  - **观我生 / 观其生 / 观国之光**：分别是观自身生命、观他人生命、观国家文明与德光，是三种不同层次的“观”。

- **规范化释义（primary_lang_explained）**：

  观卦讨论的是“以何种方式看世界与看自己”。卦辞“观：盥而不荐，有孚颙若”以祭祀为喻：真正重要的不是是否参与到最后的献祭，而是祭前能否洗净身心、怀抱诚信、神色庄严——只要内心有孚，则即便只是“观礼”，也能与神道相通。

  彖传指出：“大观在上，顺而巽，中正以观天下”，说明在位者若能以宽广视野、谦巽态度和中正之心来观察天下，则其所行之教化会自然深入人心；“下观而化”则提示：下位者通过观摩上位者的仪态与行事风格，也能被潜移默化地影响。“观天之神道，而四时不忒；圣人以神道设教，而天下服矣”更是把“观”提升到观天道以设教化的高度。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Guan, "Contemplation" or "Viewing", addresses the importance of observation, both being observed by others and observing the world with care. The Judgment states "Guan: the ablution has been made, but not yet the offering; there is sincerity and reverence", pointing to a solemn, preparatory stage where one's example and bearing matter more than overt action.

- 核心要点：

  - 观卦的核心是**观与被观的关系**：上观下、下观上、观己、观人、观国，最终都指向“观我生”的自省。
  - 卦辞强调**内在诚敬重于外在仪式**，这是“观礼”得其真义的关键。
  - 爻辞从童观、𬮭观到观我生、观国之光、观其生，构成一条从幼稚观察到成熟观照的进阶路径。

- 详细解说：

  卦象为风行地上：风虽无形，却能通过树木与尘埃的反应被“看见”，正如观卦所言的“神道设教”——不可见的道通过可见的现象为人所体会。与临卦相比，临重在“如何临下”，观重在“如何看与被看”：前者偏向权力姿态，后者偏向认知与自省。

  爻辞中，“童观，小人无咎，君子吝”说明初级的观只适合尚未承担大责的人；“𬮭观，利女贞”则肯定在某些内向、隐蔽的情境中，暗中细察是合宜的；“观我生”出现两次，强调无论身处何位，自观自身的生命轨迹、言行得失，才是避免大错的根本；“观国之光”则让人从一个国家的礼乐制度、公共空间与文化气象中，看到其真正的文明程度；“观其生”则提醒人们从他人的生活状态中看见其志向与道路。"""
    normalized_text_zh: str = """"""
    subject: str = "观卦（䷓）"
    factor_refs: list = ['zhouyi_gua_guan']
    
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
        l1_anchor="zy_v1.0.0_观卦_001_L1",
    )
    version: str = "1.0.0"
