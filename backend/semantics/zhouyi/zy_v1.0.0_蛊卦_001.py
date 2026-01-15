"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899859
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
    semantic_id="zy_v1.0.0_蛊卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 蛊卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  蛊：元亨，利涉大川。先甲三日，后甲三日。

  【彖传】
  《彖》曰：“蛊，刚上而柔下，巽而止蛊。蛊，元亨而天下治也。利涉大川，往有...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  蛊：元亨，利涉大川。先甲三日，后甲三日。

  【彖传】
  《彖》曰：“蛊，刚上而柔下，巽而止蛊。蛊，元亨而天下治也。利涉大川，往有事也。先甲三日，后甲三日，终则有始，天行也。”

  【象传】
  《象》曰：山下有风，蛊；君子以振民育德。

  【爻辞】
  初六，干父之蛊，有子考，无咎，厉终吉。
  九二，干母之蛊，不可贞。
  九三，干父之蛊，小有悔，无大咎。
  六四，裕父之蛊，往见吝。
  六五，干父之蛊，用誉。
  上九，不事王侯，高尚其事。

- 分字分词释义：

  - **蛊**：本义为腐败、败坏之事，引申为“整弊治乱”“修治积弊”的时局。
  - **元亨，利涉大川**：匡正积弊可以带来根本通达，并且有力气“涉大川”——承担大风险、大工程。
  - **刚上而柔下**：阳刚在上、阴柔在下，上层有力、下层顺应，为整弊提供条件。
  - **巽而止蛊**：以巽顺之道而“止”蛊，强调整治要有度、有节，而非粗暴推翻一切。
  - **先甲三日，后甲三日**：以“甲日”为一轮起点，前三日为终局、后三日为新始，象征终结旧弊、开启新局的循环节律。
  - **干父之蛊 / 干母之蛊**：干，有干预、担当之义；指主动承担起匡正父母（上一代）遗留弊端的责任。
  - **裕父之蛊**：裕，有宽纵、姑息之意；指对上一代的弊端加以掩饰、放任。
  - **用誉**：以誉终之，最终获得赞誉。
  - **不事王侯，高尚其事**：不去侍奉王侯，自守其道，以洁身自好为高。

- **规范化释义（primary_lang_explained）**：

  蛊卦讨论的是“如何面对与整治已经积累的败坏与弊端”。卦辞“蛊：元亨，利涉大川。先甲三日，后甲三日”，一方面指出正面整治积弊可以带来根本性的通达与进步，并有能力承担大工程与大风险；另一方面又通过“先甲三日，后甲三日”强调：整弊并非一蹴而就，而是处在终结旧局与开启新局之间的循环节点上——先有终，再有始。

  彖传以“刚上而柔下，巽而止蛊”说明，整治蛊弊需要上位者的刚健决断，也需要下层的顺从配合，更需要在“巽顺”中“止”而有度，不是以暴易暴。象传“山下有风，蛊；君子以振民育德”：山下有风，既有稳定的大地之形，又有流动之风，象征在稳固结构中发动清新的变风；君子观此，以振作民心、培养德行为本，而不只是技术性的改革。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Gu, "Decay" or "Work on What Has Been Spoiled", confronts situations where things have gone wrong, structures have rotted, and active repair is needed. The Judgment states "Gu: great success; it is favorable to cross the great water; before the starting point three days, after the starting point three days", meaning that decay can be turned into success through deliberate effort, careful timing, and sustained vigilance.

- 核心要点：

  - 蛊卦聚焦于**面对既成问题时的修治态度**：不是逃避、也不是粗暴翻案，而是有度地“振民育德”。
  - 卦辞中的“先甲三日，后甲三日”提示要有**时间与周期观**：整弊是阶段性的，需要预备旧局终结，也要预备新局生发。
  - 六爻围绕“干父/干母/裕父之蛊”展开，对承担责任与袒护纵容给出鲜明对比，最终以“不事王侯，高尚其事”收束于价值选择。

- 详细解说：

  卦象上艮下巽：山下有风，风在山下回旋，象征在稳固结构内部进行修整。与前一卦随相比，随强调“因时而动”，蛊则是“因时而治”——在时机成熟之时，启动对积弊的整理。卦辞的“利涉大川”呼应前文多卦所言的“涉大川”，暗示整弊本身就是一种渡险：若能在危机点上修治，便能为后续发展打通道路。

  爻辞自下而上，描绘了整治家族或系统性问题的不同水平：初六“干父之蛊，有子考，无咎，厉终吉”，强调子辈主动承担父辈的过失，虽有危险，终能得吉并保全父名；九二“干母之蛊，不可贞”，则指出对“母之蛊”的处理不宜固执不变，需要通权达变；九三再次“干父之蛊，小有悔，无大咎”，说明行动难免有瑕疵，但只要方向正确，终不致大害。

  六四“裕父之蛊，往见吝”则是反面教材：对上一代的弊病加以纵容与粉饰，表面是孝、实则害之，结果只会招致可叹之局；六五“干父之蛊，用誉”将“干父”提升到理想境界——不仅整治弊端，还能承继与发扬父辈的德行，从而获得社会的赞誉；上九“不事王侯，高尚其事”，则将“整蛊”的议题推至价值选择的层面：在权力与名位之外，仍有一条“高尚其事”的路可行，象征在大局已不可为时，选择自守其道、不与浊流同流合污。"""
    normalized_text_zh: str = """"""
    subject: str = "蛊卦（䷑）"
    factor_refs: list = ['zhouyi_gua_gu']
    
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
        l1_anchor="zy_v1.0.0_蛊卦_001_L1",
    )
    version: str = "1.0.0"
