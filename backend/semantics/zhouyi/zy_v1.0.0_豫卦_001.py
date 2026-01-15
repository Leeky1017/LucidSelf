"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899840
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
    semantic_id="zy_v1.0.0_豫卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 豫卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  豫：利建侯，行师。

  【彖传】
  《彖》曰：豫，刚应而志行，顺以动，豫。
  豫，顺以动，故天地如之，而况建侯行师乎？
  天地...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  豫：利建侯，行师。

  【彖传】
  《彖》曰：豫，刚应而志行，顺以动，豫。
  豫，顺以动，故天地如之，而况建侯行师乎？
  天地以顺动，故日月不过，而四时不忒；
  圣人以顺动，则刑罚清而民服，豫之时义大矣哉。

  【象传】
  《象》曰：雷出地奋，豫；先王以作乐崇德，殷荐之上帝，以配祖考。

  【爻辞】
  初六，鸣豫，凶。
  六二，介于石，不终日，贞吉。
  六三，盱豫，悔；迟有悔。
  九四，由豫，大有得，勿疑，朋盍簪。
  六五，贞疾，恒不死。
  上六，冥豫，成，有渝，无咎。

- 分字分词释义：

  - 豫：喜悦、安乐，亦有预备之意，本卦重在“顺势而乐”。
  - 利建侯，行师：有利于封建诸侯、出兵行师，提示豫乐之时正是大规模制度建设与军事行动的良机。
  - 刚应而志行：阳刚之爻得正应，志向得以实行。
  - 顺以动：顺势而动，不逆时机与人心。
  - 雷出地奋：雷自地中奋发，象征气机鼓动、万物欣欣向荣。
  - 作乐崇德：制作音乐以崇尚德行，而非单纯娱乐。
  - 鸣豫：高声宣扬快乐，乐在表面。
  - 介于石：如刻于石上般坚贞，不易动摇。
  - 盱豫：仰视而乐，带有轻浮、好高骛远之意。
  - 朋盍簪：朋友如发丝聚于簪下，比喻群贤聚集、合力成事。
  - 冥豫：沉迷于快乐而不自觉，陷于昏冥之豫。

- **规范化释义（primary_lang_explained）**：

  豫卦谈的是“如何在顺势与欢乐中保持分寸”。卦辞“豫：利建侯，行师”指出：在豫乐之时，适合确立诸侯、进行军政行动——因为人心顺、气机畅，更易于推行制度。但彖传紧接着强调：豫之所以可贵，在于“顺以动”：天地顺势而运，日月四时不差；圣人顺势而行，刑罚清明、民心服从，豫因此成为承载大事业的时机，而非只供享乐的节日。

  象传“雷出地奋”描绘春雷勃发、万物振动的景象，先王因而“作乐崇德”，用音乐礼仪来承载与调和这种集体情绪，使欢乐有所归依，而不至于流于放纵。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Yu, "Enthusiasm" or "Joy", is about how to maintain proper measure in following the flow and enjoying success. The Judgment, "Yu: it is favorable to establish feudal lords and to set armies in motion", indicates that in times of joyful momentum, it is appropriate to confirm vassals and undertake military or political actions—because when hearts are aligned and energy flows smoothly, institutions are easier to establish. Yet the Tuan immediately stresses that the value of Yu lies in "moving in accord with the flow": Heaven and Earth move in accord, so the sun and moon do not overstep and the four seasons do not err; the sage moves in accord, so punishments are clear and the people submit. Yu is thus a season for great undertakings, not merely a holiday for indulgence.

  The Image, "thunder coming forth from the earth with vigor", evokes the scene of spring thunder bursting forth and all things stirring. The ancient kings, observing this, "made music to honor virtue, offering it abundantly to the High God and pairing it with the ancestors". Music and ritual serve to channel and harmonize this collective emotional surge, so that joy has a proper home and does not descend into license.

  The six lines show a spectrum from shallow joy to deep joy, from vigilance to intoxication: the first line, "proclaiming joy; misfortune", opens by warning that announcing pleasure at the very start, without any actual foundation, leads to danger. The second line, "firm as stone, not lasting the whole day; steadfast and auspicious", is crucial: even in joyful times, one holds steadfast as stone and does not indulge beyond a single day, ending celebrations in good time—thus remaining fortunate. The third line, "looking up in joy; regret; delay brings regret", criticizes frivolous ambition and a pleasure-seeking gaze that refuses to self-correct, bringing lifelong regret.

  The fourth line, "from Yu great gain is obtained; do not doubt; friends gather like hair at the hairpin", shows that when one moves with the joyful momentum in full confidence and gathers allies effectively, great rewards follow. The fifth line, "steadfast as if ill; constantly does not die", echoes a similar phrase from Qian: even amid joy and favorable conditions, one must maintain a kind of vigilant "illness"—a self-guarding wariness—to avoid downfall. The top line, "dark joy; it is accomplished; there is change; no blame", offers the ultimate warning: if one has already sunk into dark intoxication with joy, only changing course can prevent disaster; otherwise, joy pushed to its extreme turns into sorrow.

- 核心要点：

  - 豫卦的核心是“顺势而乐”，乐必须有德、有度，有所预备。
  - 豫之适用场景是大规模制度与军政行为的推进期，强调“在乐时立制”。
  - 六爻从“鸣豫”“介于石”“盱豫”“由豫大有得”“贞疾恒不死”“冥豫成，有渝无咎”呈现了从浅乐到深乐、从警觉到沉迷的不同状态。

- 详细解说：

  卦象上震下坤：雷在地中，动而不离其本。与谦卦相连：谦谈有而能下，豫谈顺而能乐。若有而不谦，则盈；顺而不戒，则冥豫。

  初六“鸣豫，凶”开宗明义地指出：一开始就高声宣扬快乐，而无实际根基，必致凶险。六二“介于石，不终日，贞吉”则是豫卦中非常重要的一爻：在乐时仍能保持如石般坚贞，并且“不过终日”——不过度沉溺，适时收束，故得贞吉。六三“盱豫，悔；迟有悔”批评的是好高骛远、迟迟不改之乐，终生悔恨。

  九四“由豫，大有得，勿疑，朋盍簪”说明当顺势而乐时，若能坚定不疑，善用同志之力，就能“大有得”；六五“贞疾，恒不死”在谦卦中已有相似表达，这里强调即使处于欢乐、顺境之中，仍要像得病一样警醒自守，才能不致灭亡。上六“冥豫成，有渝，无咎”则给出终极提醒：若已沉迷于豫，唯有改变（渝）才可免咎，否则豫极则变，乐极生悲。"""
    normalized_text_zh: str = """"""
    subject: str = "豫卦（䷏）"
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
        l1_anchor="zy_v1.0.0_豫卦_001_L1",
    )
    version: str = "1.0.0"
