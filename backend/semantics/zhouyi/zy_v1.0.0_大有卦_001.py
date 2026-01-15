"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899821
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
    semantic_id="zy_v1.0.0_大有卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 大有卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  大有：元亨。

  【彖传】
  《彖》曰：“大有”，柔得尊位大中，而上下应之，曰大有。
  其德刚健而文明，应乎天而时行，是以元亨。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  大有：元亨。

  【彖传】
  《彖》曰：“大有”，柔得尊位大中，而上下应之，曰大有。
  其德刚健而文明，应乎天而时行，是以元亨。

  【象传】
  《象》曰：火在天上，“大有”；君子以遏恶扬善，顺天休命。

  【爻辞】
  初九，无交害，匪咎，艰则无咎。
  九二，大车以载，有攸往，无咎。
  九三，公用亨于天子，小人弗克。
  九四，匪其彭，无咎。
  六五，厥孚交如，威如，吉。
  上九，自天祐之，吉无不利。

- 分字分词释义：

  - 大有：大有所获、大有其德，既指物质丰盛，也指德位兼备。
  - 元亨：元为始、为大，亨为通达，合指根本通达的大吉之象。
  - 柔得尊位大中：柔爻居尊位而得中，如六五处上卦之中，又应上下。
  - 应乎天而时行：顺应天道，因时而动，而非恣意妄为。
  - 遏恶扬善：抑制邪恶，彰显善行，是大有之世君子应有的用力方向。
  - 无交害：无相互侵害之交往，或不与有害之交往相混。
  - 大车以载：以大车承载，象征承载之力足够，可以远行。
  - 公用亨于天子：以公器、公共礼仪奉享于天子，非私人宴乐。
  - 匪其彭：不以盛大炫耀自满。
  - 厥孚交如，威如：既有诚信交往，又具应有之威仪。

- **规范化释义（primary_lang_explained）**：

  大有卦描写的是“拥有丰盛资源与声望的状态”。卦辞只用“元亨”二字，说明这种大有并非局部幸运，而是根基深厚、时运相合的通达之象。彖传指出：阴柔之爻处尊位而得其中，又上下相应；德性上则刚健而文明，顺应天道按时而行，因此而大吉。

  在这种局面中，君子之责不在继续索取，而在“遏恶扬善，顺天休命”：通过节制与教化，使大有成为天下共享的福分，而非个体独占之利。六爻则从不同角色描绘如何在大有之时保持不失：初九“无交害，匪咎，艰则无咎”先以谨慎交往为底线；九二“大车以载，有攸往，无咎”强调承载有度、方向明确；九三“公用亨于天子，小人弗克”表明大有之礼属于公器，小人无法胜任。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Da You, "Great Possession", portrays a state in which one holds abundant resources, influence, and recognition. The Judgment simply says, "Da You: great success", indicating that this is not a narrow or accidental stroke of luck but a condition in which deep roots, personal virtue, and the timing of Heaven all align. The Tuan explains that a gentle Yin line occupies the honored central position and is responded to above and below; at the same time, the overall virtue is both strong and civilized, acting in accordance with Heaven and moving at the proper time. For this reason, Da You brings great and far-reaching success.

  In such a situation, the noble person’s duty is not to keep accumulating more but to "restrain evil and exalt good, following Heaven’s gracious mandate". Abundance is to be stewarded, not hoarded. The lines show how different roles should conduct themselves in times of great possession: the first line, "no harmful entanglement in relationships; not a fault; if one remains cautious, there is no blame", lays down careful association as the basic safeguard at the onset of abundance. The second line, "a great carriage to carry; there is a destination; no blame", emphasizes having both sufficient capacity and a clear direction. The third line, "using public offerings to honor the Son of Heaven; the petty person is not capable", makes clear that the rituals and offerings of Da You are public, not private; small-minded people cannot properly handle what belongs to the whole.

  The fourth line, "not his own swelling; no blame", warns those near the top not to exult in greatness as if it were their personal inflation; by refusing to make a show of their largeness, they remain safe. The fifth line, "his trust is interwoven; his dignity is awe-inspiring; good fortune", reveals the core of leadership in Da You: relationships woven together by real trust, coupled with appropriate dignity and authority. The top line, "from Heaven it is blessed; good fortune; nothing is not favorable", shows Da You at its peak: when one’s possession and position are truly in harmony with the mandate of Heaven, support comes unforced from above. Yet even here the implication remains that this blessing is not self-generated; it arrives "from Heaven", and forgetting this quickly turns blessing into hubris.

- 核心要点：

  - 大有卦的重点不在“如何得有”，而在“有之后如何用有”：顺天之时而动、以公义节制丰盛。
  - 六五“厥孚交如，威如，吉”提示：居尊位者以诚信交往、内怀威仪，才能使大有不致流于骄奢。
  - 上九“自天祐之，吉无不利”强调：真正的大有来自德与时的契合，而非仅靠人力累积。

-  详细解说：

  卦象上乾下离：火在天上，光照万物而无所不及，是“大有”的象征。与同人相邻，一重在“如何与人同”，一重在“资源丰盛时如何用之”。若大有而不谦，则易盈而招损；大有能谦，则能长久。

  初九忌“交害”：在丰盛将起之初，先要远离有害之交，知艰而能守，则可无咎。九二以“大车以载”象征载道而行，其贵在“有攸往”：有明确之志，不为空载。九三“公用亨于天子，小人弗克”，说明在大有之时，祭祀与礼乐最能体现格局，小人若以私心参与，反成祸端。

  九四近上而不居尊，故“匪其彭，无咎”：不以盛大为自夸，反得安全。六五为全卦枢纽，“厥孚交如，威如，吉”揭示领导者应在信与威之间保持平衡；上九则是大有之极，“自天祐之”说明此时人事已至所能，仍须以天命为终极根基，避免以己力为全功。"""
    normalized_text_zh: str = """"""
    subject: str = "大有卦（䷍）"
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
        l1_anchor="zy_v1.0.0_大有卦_001_L1",
    )
    version: str = "1.0.0"
