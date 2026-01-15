"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899888
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
    semantic_id="zy_v1.0.0_噬嗑卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 噬嗑卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  噬嗑：亨，利用狱。

  【彖传】
  《彖》曰：“颐中有物，曰噬嗑。噬嗑而亨，刚柔分，动而明，雷电合而章。柔得中而上行，虽不当位，利...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  噬嗑：亨，利用狱。

  【彖传】
  《彖》曰：“颐中有物，曰噬嗑。噬嗑而亨，刚柔分，动而明，雷电合而章。柔得中而上行，虽不当位，利用狱也。”

  【象传】
  《象》曰：雷电，噬嗑；先王以明罚𠡠法。

  【爻辞】
  初九，屦校灭趾，无咎。
  九二，噬肤，灭鼻，无咎。
  六三，噬腊肉，遇毒；小吝，无咎。
  九四，噬乾胏，得金矢；利艰贞，吉。
  六五，噬乾肉，得黄金；贞厉，无咎。
  上九，何校灭耳，凶。

- 分字分词释义：

  - **噬嗑**：噬，咬合；嗑，合闭。颐中有物，必须咬断才能通过，比喻在有阻碍、有案件时，通过明辨与决断打通。
  - **利用狱**：有利于处理刑狱、判案，强调在法律与惩戒层面“噬而合之”的功能。
  - **刚柔分，动而明，雷电合而章**：刚柔分明，在动荡之中仍保持光明，雷电交作，使是非昭彰。
  - **柔得中而上行**：六五阴爻居中而上行，象征在处理刑狱时柔中带刚，能持中道。
  - **屦校 / 何校**：校为刑具；屦校是足镣，何校是戴于颈肩的枷锁。
  - **噬肤、噬腊肉、噬乾胏、噬乾肉**：从咬皮肤、小肉到腊肉、带骨干肉、干肉，象征处理问题由浅入深、由易到难的层次。
  - **金矢 / 黄金**：从干肉中咬出金箭与黄金，比喻在艰难剖析中得到关键证据或公正之利器。

- **规范化释义（primary_lang_explained）**：

  噬嗑卦讲“在有阻碍时如何通过咬合、断决，使事理显明”，尤其指向刑狱与律法层面的实践。卦辞“噬嗑：亨，利用狱”指出：当口中有物、道路受阻时，需要果断“咬断”障碍，才能亨通；在繁杂案情之中，通过分辨与决断，咬碎虚伪，咬出真相，便是“利用狱”。

  彖传以卦象说明：震为雷、离为火，雷电交作，有动有明，使隐藏之事得以暴露；“刚柔分”意味着法律、执行者与当事人各安其位，不可混淆；“柔得中而上行”则说明执法者应柔中带刚、居中行事，虽未必位位尽善，仍要尽量合乎时宜。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Shi He, "Biting Through", represents situations where an obstruction must be removed by decisive action, like biting through something blocking the mouth. The Judgment, "Shi He: success; it is favorable to use legal proceedings", indicates that when something blocks unity or progress, one must act with clarity and justice to break through.

- 核心要点：

  - 噬嗑卦聚焦于**处理阻碍与判明是非**，在司法、规则执行、冲突裁决等场景尤为贴切。
  - 卦象“雷电合而章”强调：在动荡压力之中，必须以清明、分明的原则行事，使是非彰显。
  - 六爻呈现从轻罚到重罚、从浅伤到深伤的序列，为观察“如何逐步加重而不滥用刑罚”提供了象例。

- 详细解说：

  卦序上，噬嗑承接观卦：观重在“看清”，噬嗑重在“咬断”。当单纯的“观”不足以解决问题时，必须在规则与裁决层面做出行动，这便引出“噬嗑而亨”。

  爻辞中的图像非常具体：足镣、颈枷、腊肉、干肉……一方面描绘了逐步加重的刑罚与审讯强度；另一方面也提醒人们警惕“何校灭耳”的危险——当刑具过重、惩罚过度时，不仅伤人之身，也会毁坏自身的“耳”，即听纳意见与辨别是非的能力。

  从心理层面看，噬嗑也可以理解为“自我审判”的象征：在剔除旧习与阴影时，需要一定程度的“咬断”，但若过度苛责自我，就会走向“灭耳”的自伤状态。如何在严明与慈悲之间取得平衡，是噬嗑卦留给后人长期思考的命题。"""
    normalized_text_zh: str = """"""
    subject: str = "噬嗑卦（䷔）"
    factor_refs: list = ['zhouyi_gua_shihe']
    
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
        l1_anchor="zy_v1.0.0_噬嗑卦_001_L1",
    )
    version: str = "1.0.0"
