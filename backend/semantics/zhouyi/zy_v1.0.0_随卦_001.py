"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899849
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
    semantic_id="zy_v1.0.0_随卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 随卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  随：元亨，利贞，无咎。

  【彖传】
  《彖》曰：“随，刚来而下柔，动而说，随，大亨，贞无咎，而天下随时，随时之义大矣哉！”

 ...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  随：元亨，利贞，无咎。

  【彖传】
  《彖》曰：“随，刚来而下柔，动而说，随，大亨，贞无咎，而天下随时，随时之义大矣哉！”

  【象传】
  《象》曰：泽中有雷，随；君子以向晦入宴息。

  【爻辞】
  初九，官有渝，贞吉，出门交有功。
  六二，系小子，失丈夫。
  六三，系丈夫，失小子。随有求得，利居贞。
  九四，随有获，贞凶。有孚在道，以明，何咎！
  九五，孚于嘉，吉。
  上六，拘系之，乃从，维之，王用亨于西山。

- 分字分词释义：

  - **随**：随从、顺随、顺时而动之意，本卦重在“因时而随”，非盲从。
  - **元亨，利贞，无咎**：根本通达，又利于坚守正道，因此可免大咎。
  - **刚来而下柔**：阳刚之气来到而居于阴柔之下，象征有力者愿意下行、随顺而不专断。
  - **动而说**：在行动中使人心悦服，“说”作悦，象征以顺势而非强逼来推动变化。
  - **随时**：随顺时势、因时制宜，而非拘泥成见。
  - **官有渝**：官职、职分有更易、有变动。
  - **系小子 / 系丈夫**：系，系念、牵系；小子指下属、子弟，丈夫指正配或正道所系之人。
  - **随有求得**：顺势而随，有所追求则可有所获得。
  - **随有获，贞凶**：一味跟随他人求获，哪怕自以为守正，也可能走向凶险。
  - **有孚在道，以明**：内有诚信而安于正道，以光明的方式行事。
  - **拘系之，乃从，维之**：先拘束、系缚，再使之随行，用绳索维系，比喻用外在力量强制其随从。

- **规范化释义（primary_lang_explained）**：

  随卦谈“如何正确地随从与顺势”。卦辞“随：元亨，利贞，无咎”指出，随从若建立在顺应时势、坚守正道之上，则可以大吉大利而免于大过。彖传从卦象结构入手：“刚来而下柔，动而说”，说明阳刚下来居于阴柔之下，以行动感人而非强压于人，这是“随”的理想状态；更进一步提出“天下随时”，强调真正的随不是随人、随欲，而是随“时”——顺应整体情势与节律。

  象传以“泽中有雷”形容随之象：泽中有雷，动于安处，如同君子随日色渐暗而入室休息，起居有节，不逆天时。各爻则具体呈现随从中的取舍：初九“官有渝，贞吉”，是职分变动但仍守正而得吉；六二、六三则分别表现“执着于小子而失丈夫”“执着于丈夫而失小子”的两种偏执选择，提示随从时不可贪多，必须有所舍取；九四“随有获，贞凶”则警惕为获利而随人，即便自称守正，也可能走向凶险；九五“孚于嘉，吉”说明随从善人、随从可嘉之德；上六则是被拘系而随，随已失其自发。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Sui, "Following", addresses how one chooses whom or what to follow, and how to follow correctly. The Judgment, "Sui: great success; favorable to be steadfast; no blame", indicates that if one follows rightly, success will follow naturally, but this requires steadfastness and correct discernment. The Tuan explains that "following" arises when firmness comes below and gentleness moves above, and when there is joy within and movement without; thus one follows the time and the great is realized.

- 核心要点：

  - 随卦的“随”，重在**随时随道**，不是逢人就随、逢势就趋，必须以元亨利贞为前提。
  - 随的实践离不开**舍与取**：不同位置要决定“系小子”还是“系丈夫”，不可能两面兼顾。
  - 随可以是出于内心诚信之“有孚在道”，也可以是被外力“拘系之”的被迫之随，两者在结果与风险上截然不同。

- 详细解说：

  卦象上兑下震：震为雷，兑为泽，雷行泽中，象征在相对安乐、柔顺的环境中出现变动与振奋。与前一卦豫相比，豫谈“顺势而乐”，随则更强调“顺势而行”；与更前面的比、同人相比，比重亲比，同人重同道，而随则强调在关系与时势之间作出动态选择。

  初九“官有渝，贞吉，出门交有功”，是随卦中最典型的“因变而随”：官职、角色有变化，只要方向仍顺乎正道，便能在对外交往中有所成就。六二、六三则构成一对：前者“系小子，失丈夫”，着眼于眼前的小关系，失去真正值得依托的大关系；后者则调转为“系丈夫，失小子”，重心放在大处，与原则之人相系，而舍弃次要之交往——从义理上看，这是更接近正随的选择。

  九四“随有获，贞凶。有孚在道，以明，何咎！”看似矛盾：随从他人而有所得，按理守正应吉，却被判为“贞凶”。关键在于“随有获”的动机与路径：若随从只是为了获利，虽口称守贞，实则心不在道，必有凶险；唯有“有孚在道，以明”，即内心诚信而安于正道，以透明光明的方式行事，方能免咎。九五、上六则给出了“随善”与“被迫之随”的对比：前者“孚于嘉”，随的是可嘉之人、可嘉之道；后者则是被拘系、被绳索牵引的随，象征失去主体性的从众。


  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "随卦（䷐）"
    factor_refs: list = ['zhouyi_gua_sui']
    
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
        l1_anchor="zy_v1.0.0_随卦_001_L1",
    )
    version: str = "1.0.0"
