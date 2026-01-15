"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899732
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
    semantic_id="zy_v1.0.0_需卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 需卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  需：有孚，光亨，贞吉。利涉大川。

  【爻辞】
  初九，需于郊，利用恒，无咎。
  九二，需于沙，小有言，终吉。
  九三，需于泥...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  需：有孚，光亨，贞吉。利涉大川。

  【爻辞】
  初九，需于郊，利用恒，无咎。
  九二，需于沙，小有言，终吉。
  九三，需于泥，致寇至。
  六四，需于血，出自穴。
  九五，需于酒食，贞吉。
  上六，入于穴，有不速之客三人来；敬之，终吉。

  【彖传】
  《彖》曰：需，须也；险在前也。
  刚健而不陷，其义不困穷矣。
  “需，有孚，光亨，贞吉”，位乎天位，以正中也。
  “利涉大川”，往有功也。

  【象传】
  《象》曰：云上于天，需；君子以饮食宴乐。

- 分字分词释义：

  - 需：卦名，本义为等待、须臾，引申为在险势未解之前须待其时。
  - 有孚：内有诚信与信任，可为根基。
  - 光亨：光明通达，发展顺畅。
  - 贞吉：守正而吉，强调不妄动、不妄变。
  - 利涉大川：利于渡过大河，比喻适时而行，能越过重大险阻。
  - 需于郊：在郊外等待，离险地尚远，形势较为宽缓。
  - 利用恒：利于保持恒久不变的态度和原则。
  - 需于沙：在沙地等待，局势较前收紧，尚有议论与波折。
  - 小有言：有少量非议或口舌之事。
  - 需于泥：在泥泞之地等待，行动受阻，易招祸患。
  - 致寇至：招致强盗来到，比喻因处境不慎或行为不当引来外患。
  - 需于血：在血地等待，近乎伤害与杀伐之境。
  - 出自穴：从穴中出来，象征脱离险境。
  - 需于酒食：在酒食之间等待，比喻安心处中、养精蓄锐。
  - 不速之客：未曾预期而来的客人，比喻突如其来的机会或挑战。
  - 敬之，终吉：以恭敬之心对待，即可终得吉利。
  - 云上于天：上卦为坎之云气，下卦为乾之天，云在天上，未雨而云聚，象“待雨之时局”。
  - 饮食宴乐：在等待期间，君子以饮食宴乐自处，表示外不躁进、内不自扰。

- **规范化释义（primary_lang_explained）**：

  需卦所描绘的是“在险之前的等待之道”：前方有险（坎在前），自身刚健（乾在后），此时若能内守诚信、光明中正，则可在适当的时机渡过大川。卦辞说“有孚，光亨，贞吉”，说明等待并非消极，而是基于内在诚信与光明前景的主动选择；“利涉大川”则强调，等待的目的在于择机一举跨越大险，而非无限期拖延。

  六爻具体呈现等待位置与态度的差异：初九“需于郊，利用恒，无咎”，位处卦下之始，离险地尚远，只要持守恒常之道，不妄动便无灾；九二“需于沙，小有言，终吉”，逼近险地边缘，难免有口舌与质疑，但只要居中守正，终可吉；九三“需于泥，致寇至”，已经陷入泥泞，若仍不知谨慎，容易招致外寇，是“因需不当而致祸”的典型；六四“需于血，出自穴”，身近血地，却有机会从穴中脱身，象征在极险之中仍有转圜，只要把握脱离时机；九五“需于酒食，贞吉”代表身居尊位却能安然处中，在饮酒进食中从容等待，不失中正；上六“入于穴，有不速之客三人来；敬之，终吉”，则说明在退守穴中时，会有意外贵客或机缘造访，只要以敬相待，最后仍可吉利。

  彖传以“需，须也；险在前也。刚健而不陷，其义不困穷矣”总括需卦：局势有险，但若以前卦之刚健自持而不轻进，则可不至于困穷。云在天上而未雨，是“需”的外在图景；君子在此阶段“以饮食宴乐”，并非沉迷享乐，而是借有序的生活与仪式感稳定人心，不被未知之险搅乱。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xu, "Waiting", addresses the way of waiting when danger lies ahead: danger is in front, firmness and strength are behind, so now is not the time to rashly advance but to choose the right moment to act. The Judgment's "having sincerity, brilliant success, steadfastness brings good fortune; it is favorable to cross the great water" indicates that waiting must be built on sincerity and a bright prospect, with correctness as the condition; only then can great rivers be crossed when the time comes. The Image "clouds above heaven, Xu; the noble person thereby drinks, eats, and takes ease" reminds that in the waiting stage, one should use orderly life and a sense of ritual to stabilize people's hearts, not be disturbed by the unknown danger.

- 核心要点：

  - 需卦强调“在险之前的等待之道”：前方有险，后承刚健，此时不宜贸然前行，而应择时而动。
  - 卦辞中的“有孚，光亨，贞吉”说明等待必须建立在诚信与光明的前景上，并以守正为条件。
  - 六爻从郊、沙、泥、血、酒食、穴等不同环境，展示等待位置与风险程度的渐变，提醒人分辨“可守”“可进”“当退”“宜敬”。
  - 需卦的实践要点在于：看清险势所在、守中蓄势、善待不速之机缘，而非因焦躁或恐惧而乱动。

- 详细解说：

  在卦序上，需承蒙而来：蒙卦讲“启蒙与教化”，需卦则转入“在外部环境尚不明朗时，如何安排自己的节奏”。乾为天，坎为险，二者相叠构成需卦：下乾在内，象征内在刚健有力；上坎在外，象征前路险阻、情况多变。这种组合决定了需卦不是单纯的“被困于险中”，而是“在险势尚未直接压身之时主动选择等待”。

  卦辞中的“有孚”表明等待的根基在于信：信自己、信同伴、信大势仍有可为；“光亨”则指虽然暂时不行，但前景可期；“贞吉”提醒人在等待期不可因外界波动而改变根本原则。若只是因为胆怯而拖延，而非基于信与正，那便不是需卦之道。

  从爻位来看，需卦展示了接近险势的渐进过程：初九远在郊外，可以宽松地观望；九二已步入沙地，脚步开始受限，难免受到议论与误解，但守中则终吉；九三陷于泥中，代表已深入问题现场，若仍不调整策略，便是“自致寇至”；六四“需于血，出自穴”表明形势已危及性命，惟有从隐处脱出才是正道。九五在酒食中守贞，看似安逸，实则象征居尊位者在等待期内以中正之德安抚人心、整顿后勤。上六则把注意力转移到“如何对待突如其来的客人”上：不速之客三人来，若以敬相待，最终仍吉；这提醒在等待过程中，要对“意外机缘”保持开放与敬重，而不是一味拒斥或轻率迎合。

  象传以“云上于天，需；君子以饮食宴乐”点出需卦的生活面向：在云聚未雨的时刻，君子通过适度的饮食宴乐维持秩序与节律，而非任由焦虑扩散。对于命理与解梦场景，这意味着当卦象指向需时，往往是“暂缓大动作、稳住日常、养精蓄锐”的时段，重点在调节节奏、培养信念，而非追求立即突破。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "需卦（䷄）"
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
        l1_anchor="zy_v1.0.0_需卦_001_L1",
    )
    version: str = "1.0.0"
