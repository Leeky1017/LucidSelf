"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899782
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
    semantic_id="zy_v1.0.0_履卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 履卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  履：履虎尾，不咥人，亨。

  【彖传】
  《彖》曰：“履”，柔履刚也。
  说而应乎乾，是以“履虎尾，不咥人，亨”。
  刚中正，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  履：履虎尾，不咥人，亨。

  【彖传】
  《彖》曰：“履”，柔履刚也。
  说而应乎乾，是以“履虎尾，不咥人，亨”。
  刚中正，履帝位而不疚，光明也。

  【象传】
  《象》曰：上天下泽，履；君子以辨上下，定民志。

  【爻辞】
  初九，素履，往，无咎。
  九二，履道坦坦，幽人贞吉。
  六三，眇能视，跛能履，履虎尾咥人，凶；武人为于大君。
  九四，履虎尾，诉诉，终吉。
  九五，夬履，贞厉。
  上九，视履考祥，其旋元吉。

- 分字分词释义：

  - 履：踏、行走，引申为行为方式与行事路径。
  - 履虎尾：踩在老虎尾巴上，比喻身处极险之境。
  - 咥（dié）人：咬人。
  - 柔履刚：以柔顺之道行于刚强之上。
  - 说而应乎乾：以和悦之态回应乾刚之道。
  - 刚中正：阳刚处中且得正位。
  - 履帝位而不疚：居皇帝之位而行事无愧于心。
  - 上天下泽：上为天，下为泽，象征尊卑有序、上下分明。
  - 素履：朴素之履，按本来简朴的方式行事。
  - 履道坦坦：行于平坦大道，比喻正道光明、无所隐曲。
  - 幽人：幽居之人，或指不显于世而守道者。
  - 眇能视：一目失明而仍能看见，能力有限。
  - 跛能履：足跛而仍能行走，行动受限。
  - 武人为于大君：武人以刚强之志效力于君王。
  - 诉诉：惴惴不安、战战兢兢之状。
  - 夬履：决断而行，果决之履。
  - 视履考祥：观察自己的行履，并考察吉凶祸福。
  - 其旋元吉：回旋归返时得大吉。

- **规范化释义（primary_lang_explained）**：

  履卦讲的是“在险境中如何踏准分寸”的问题。卦辞“履虎尾，不咥人，亨”描写一种极端情形：已经踩到虎尾，本应被咬，却得以通达无害；关键在于行履之道是否合宜。彖传以“柔履刚”“说而应乎乾”说明：以柔顺、和悦的态度，行于刚强的环境之上，并与乾道中正相应，才有可能化险为夷；九五刚中正，“履帝位而不疚”，是理想的统治者形象：身居高位而不失谦敬与自省。

  六爻具体呈现不同层次的行履之道：初九“素履，往，无咎”主张以朴素本真的方式行事，不装饰、不逞强，反而可以无咎；九二“履道坦坦，幽人贞吉”则强调处中之人安守平坦之道，即使身处幽隐，只要守贞便吉。六三“眇能视，跛能履，履虎尾咥人，凶；武人为于大君”是全卦的警钟：能力有限却处于危险位置，既要视又要履，终至“咥人之凶”；惟其志刚，尚可为大君之武人，提示在不适当位上的刚猛，既有危险也有用武之地。九四“履虎尾，诉诉，终吉”表现出在险境中战战兢兢、如履薄冰的态度，最终可得吉利。九五“夬履”则把焦点放在“决断”上：有时仅靠谨慎不足以应对局势，需要在守正的前提下做出果断选择，但“贞厉”说明这种决断伴随风险，必须不断自守。上九“视履考祥，其旋元吉”强调回顾与调适的重要性：在经历一段行动之后，停下来审视自己的行履，并根据所见吉凶做出调整，“其旋元吉”提示这种循环中的反思本身就是吉祥之源。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Lü, "Treading" or "Conduct", is about how to maintain proper measure and hierarchical awareness when passing through necessary risks. The Judgment "Lü: treading on the tiger's tail, it does not bite the person, success" uses the vivid metaphor of treading on a tiger's tail to illustrate that even in highly dangerous situations, if one acts with propriety and maintains proper boundaries, one can pass through without disaster. The Image "heaven above, lake below, Lü; the noble person thereby distinguishes above and below and settles the people's aspirations" points to the hexagram's core issue: in a structure where heaven is above and lake below, there must be clear distinctions between superior and inferior positions to avoid transgression; the noble person must first clarify hierarchical order before discussing action, preventing rash behavior in chaotic structures.

- 核心要点：

  - 履卦不是教人远离一切风险，而是教人如何在必经的风险中保持分寸与层级意识。
  - 卦象“上天下泽”要求君子“辨上下、定民志”：先厘清秩序，再谈行动，防止在混乱结构中贸然行事。
  - 六爻从“素履”“坦坦”“眇跛之险”“履虎尾诉诉”“夬履”“视履考祥”构成一条从朴素守道到自我检验的行为路径。
  - 在命理与解梦情境中，履卦往往指向“临界风险”“权力关系”“角色与能力不匹配”等主题，关键在于认清自身位置与能力边界。

- 详细解说：

  卦象上乾下兑：天在上、泽在下，尊卑分明而又有交流。兑为悦，乾为刚，组合出“以悦应刚”的局面：下位以和悦之态承接上位的刚健，形成一种既有秩序又有弹性的结构。履卦因此强调的不是一味顺从，而是在尊重结构的前提下，以柔顺与审慎来行使行动自由。

  初九“素履”代表尚未卷入复杂局势前的简单行履：只要按照本心、本分去做，无需过多技巧即可无咎。九二“履道坦坦，幽人贞吉”表明即便不显于世，只要行于坦荡之道，仍可安然；这对于那些处于边缘或隐退状态的人，是一种肯定。六三则呈现出“能力与位次不匹配”的危险：一目失明、足跛之人却在履虎尾，这种状态本身便预示凶险；只有当其刚猛之志被正确安放于“武人为于大君”的角色时，凶象才可能转化为某种必要的防卫力量。

  九四同样履虎尾，但以“诉诉”形容其心态：惶恐而不轻举妄动，最终可得吉利。九五“夬履”则把焦点放在“决断”上：有时仅靠谨慎不足以应对局势，需要在守正的前提下做出果断选择，但“贞厉”说明这种决断伴随风险，必须不断自守。上九“视履考祥，其旋元吉”强调回顾与调适的重要性：在经历一段行动之后，停下来审视自己的行履，并根据所见吉凶做出调整，“其旋元吉”提示这种循环中的反思本身就是吉祥之源。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "履卦（䷉）"
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
        l1_anchor="zy_v1.0.0_履卦_001_L1",
    )
    version: str = "1.0.0"
