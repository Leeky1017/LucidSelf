"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899915
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
    semantic_id="zy_v1.0.0_复卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 复卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  复：亨。出入无疾，朋来无咎；反复其道，七日来复。利有攸往。

  【彖传】
  《彖》曰：“复，亨。刚反。动而以顺行，是以‘出入无疾，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  复：亨。出入无疾，朋来无咎；反复其道，七日来复。利有攸往。

  【彖传】
  《彖》曰：“复，亨。刚反。动而以顺行，是以‘出入无疾，朋来无咎’。‘反复其道，七日来复’，天行也。‘利有攸往’，刚长也。复，其见天地之心乎！”

  【象传】
  《象》曰：雷在地中，复；先王以至日闭关，商旅不行，后不省方。

  【爻辞】
  初九，不远复，无祇悔，元吉。
  六二，休复，吉。
  六三，频复，厉，无咎。
  六四，中行独复。
  六五，敦复，无悔。
  上九，迷复，凶，有灾眚。用行师，终有大败；以其国，君凶；至于十年不克征。

- 分字分词释义：

  - **复**：返回、回归、恢复正道之意，既指路径上的返程，也指心性与秩序的回归。
  - **刚反**：阳刚之气自下而返，象征正向力量从衰极中回升。
  - **出入无疾，朋来无咎**：往来之间不再有疾病与阻碍，朋友归来亦无灾咎，体现回归后的和畅状态。
  - **反复其道，七日来复**：道路在往返反复之中呈现；“七日”象征一小周期，暗合节律与轮回。
  - **雷在地中**：震为雷居于坤地之中，象征阳气隐伏于内、待机而发。
  - **至日闭关**：至日多指冬至；闭关、商旅不行、后不省方，象征在恢复阶段暂缓外动，专注内修与蓄势。
  - **不远复 / 休复 / 频复 / 中行独复 / 敦复 / 迷复**：分别表现回归的距离、质量、频率、方式、厚度与迷失程度，是“复”的多种状态。

- **规范化释义（primary_lang_explained）**：

  复卦紧承剥卦，是“剥极而复”的回转：在阳气几乎被剥尽之后，一缕新的阳刚从下而返，带来恢复与再生的契机。卦辞云：“复：亨。出入无疾，朋来无咎；反复其道，七日来复。利有攸往。”这说明复并非简单的“回头”，而是在周期性的往返之后重新回到正道，因此出入顺畅、朋类归来，并且重新具备“利有攸往”的前进条件。

  彖传把“复”视为“天地之心”：天地运转不可能只剥不复；当衰极之时，必有反转契机。“动而以顺行”意味着这股回归力量不是逆势硬推，而是在顺应时机中自然回升；“反复其道，七日来复，天行也”则强调这一回转具有节律性与周期性，可视作理解时间结构与恢复过程的基础模型。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Fu, "Return", marks the turning point after decay when yang energy returns and renewal begins. The Judgment, "Fu: success; coming and going without illness; friends come without blame; returning on one's own path; in seven days comes the return, favorable to have somewhere to go", celebrates the natural cycle of return and restoration.

- 核心要点：

  - 复卦呈现的是**从衰极到回升的第一个转折点**，强调“及时回头”与“周期回归”。
  - 卦辞中的“出入无疾，朋来无咎”描绘了复后的状态：关系修复、往来顺畅，是衡量复是否成功的重要指标。
  - 各爻刻画不同类型的“复”：从“不远复”“休复”到“频复”“中行独复”“敦复”“迷复”，可据以观察一个系统或个体复原的质量与路径。

- 详细解说：

  卦象为雷在地中：雷动藏于地内，如同新阳潜萌于深处。与剥卦的“山附于地”形成明显对照：剥时层次被抹平、阳刚被削弱；复时则是由内而外的重新激活。

  爻辞提供了一个“复的光谱”：
  - 初九“不远复”，是最理想的状态——偏离不远，觉察即返，故“无祇悔，元吉”；
  - 六二“休复”，是安稳、恬然的复归，不再折腾；
  - 六三“频复”，反复折返，虽危险但终能无大错；
  - 六四“中行独复”，是在众人未复时，自己先行回归中道；
  - 六五“敦复”，以敦厚之心一以贯之，使复归扎实而不浮躁；
  - 上六“迷复”则是完全迷失复路，仍欲用兵、图强，结果“终有大败”“至于十年不克征”。

  从个人成长看，复卦提醒人们：偏离与犯错几乎不可避免，关键在于“离道多远、多久回头、如何回头”。不远复与敦复，代表高质量的复原；频复与迷复，则分别对应“反复横跳的调整”与“在错误路径上越走越远”。"""
    normalized_text_zh: str = """"""
    subject: str = "复卦（䷗）"
    factor_refs: list = ['zhouyi_gua_fu']
    
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
        l1_anchor="zy_v1.0.0_复卦_001_L1",
    )
    version: str = "1.0.0"
