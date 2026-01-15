"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919471
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
    semantic_id="zy_v1.0.0_艮卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 艮卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  艮，艮其背，不获其身，行其庭，不见其人，无咎。

  【彖传】
  《彖》曰：“艮，止也。时止则止，时行则行，动静不失其时，其道光明。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  艮，艮其背，不获其身，行其庭，不见其人，无咎。

  【彖传】
  《彖》曰：“艮，止也。时止则止，时行则行，动静不失其时，其道光明。艮其止，止其所也。上下敌应，不相与也，是以不获其身。行其庭，不见其人，无咎也。”

  【象传】
  《象》曰：兼山，艮；君子以思不出其位。

  【爻辞】
  初六，艮其趾，无咎，利永贞。
  六二，艮其腓，不拯其随，其心不快。
  九三，艮其限，列其夤，厉薰心。
  六四，艮其身，无咎。
  六五，艮其辅，言有序，悔亡。
  上九，敦艮，吉。

- 分字分词释义：

  - **艮**：本义为止、止息，引申为安止、稳重、自我节制。
  - **艮其背，不获其身**：止于人的背部，看不见自己的正面，象征自制与“止于身后”的隐忍，而非向外扩张。
  - **行其庭，不见其人，无咎**：在庭院中行走却不见其人，表示于外保持低调、不妄露锋芒，反而可以免咎。
  - **兼山**：上下皆为艮山，两山相叠、互不相让，比喻相持不动、各守其位。
  - **趾 / 腓 / 限 / 夤 / 辅**：分别指脚趾、小腿、小腹或腰部、脊背肌肉、颊骨，呈自下而上的身体部位次第，用以比喻不同层位的“止”。
  - **不拯其随**：拯，援救；随，随行之人或随带之物。指只顾自止而不能照顾随从，心中因此不快。
  - **列其夤，厉薰心**：背部肌肉紧绷成列，以至危厉之气熏灼内心，比喻过度压抑导致心中焦灼与不安。
  - **敦艮**：敦厚之艮，指坚实而厚重的安止之德。

- **规范化释义（primary_lang_explained）**：

  艮卦讨论的是“何时当止，以及如何安止”。卦辞：“艮，艮其背，不获其身，行其庭，不见其人，无咎。”——止在背部，看不到自身形貌；行走于庭院之中，看不见那个人，这是一种“自制而不张扬”的状态。关键不在于绝对静止，而在于在该停止的时候能够收住脚步，把注意力从外界收回到自身。

  彖传将艮概括为“止也”，但立刻加上一句“时止则止，时行则行，动静不失其时，其道光明。”——真正的止是顺时的止，不是一味不动。艮卦揭示的，是当外在环境已不适宜推进时，如何在自己的位置上安顿身心；“思不出其位”，既是避免越位，也是提醒在角色边界内下功夫。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Gen (Keeping Still) addresses 止静安定. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 艮卦核心是**“知止与安止”**：在动静之间辨时而行，在位置之内安顿其心。
  - 止的层次自下而上：从趾、腓到身、辅，对应从行动节制到言语、心念的约束。
  - 过度的抑止会“薰心”，因此艮并非鼓励无限制的压抑，而是强调“适度之止”。

- 详细解说：

  卦象上艮下艮，两山相叠，互不相让，是“兼山”的图景。与前卦震的“连雷”相比，一刚一动、一止一行，构成“动静相继”的一对：震后必有艮，事后必有静。

  初六“艮其趾，无咎，利永贞。”从最末端开始训练“止”：先学会停住脚步，不乱迈第一步，如此虽略显拘谨，却无过错，并有利于长久守正。六二“艮其腓，不拯其随，其心不快。”则提示另一种失衡：只管束缚自己的小腿，而不能照顾到随从与同伴，导致内心不舒畅——提醒止不应只顾自身而忘了整体。

  九三“艮其限，列其夤，厉薰心。”描绘的是过度克制的危险：腰部紧束、背肌成列，以至威厉之气熏灼内心，象征长期压抑导致心中焦灼与不安。六四“艮其身，无咎。”则回到平衡之止：止于全身的行动，不过度折磨心志，反而免于祸咎。

  六五“艮其辅，言有序，悔亡。”将艮之道推进到口舌层面：止于颊骨处，即节制言语，让话语有条有理、出有次序，如此可以避免因失言而后悔。上九“敦艮，吉。”作为总结：当艮之德厚重而不偏激，成为一种敦实、可靠的定力时，即是“敦艮”，自然为吉。


#### L2 语义提取

- **主题**：止静安定，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_470]` `[trigger: 卦=艮 AND 卦辞=艮其背不获其身]` `[factor_trigger: zhouyi_gua_gen AND zhouyi_guaci]` `[role: 主干]` 艮其背，不获其身，行其庭，不见其人：止于背，不见其身。 → 《周易·艮卦·卦辞》
  - `[ns_zhouyi_471]` `[trigger: 卦=艮 AND 彖传]` `[factor_trigger: zhouyi_gua_gen AND zhouyi_tuan AND zhouyi_zhizhi_chengdu]` `[role: 主干依赖]` 止也。时止则止，时行则行。 → 《周易·艮卦·彖传》
  - `[ns_zhouyi_472]` `[trigger: 卦=艮 AND 象传=兼山艮]` `[factor_trigger: zhouyi_gua_gen AND zhouyi_xiang]` `[role: 主干依赖]` 兼山，艮；君子以思不出其位：两山相止，君子止于其位。 → 《周易·艮卦·象传》
  - `[ns_zhouyi_473]` `[trigger: 卦=艮 AND 初六=艮其趾]` `[factor_trigger: zhouyi_gua_gen]` `[role: 条件分支]` 艮其趾，无咎：止于足趾，无所咎责。 → 《周易·艮卦·爻辞》
  - `[ns_zhouyi_474]` `[trigger: 卦=艮 AND 六二=艮其腓]` `[factor_trigger: zhouyi_gua_gen]` `[role: 条件分支]` 艮其腓，不拯其随：止于小腿，不能拯救所随之人。 → 《周易·艮卦·爻辞》
  - `[ns_zhouyi_475]` `[trigger: 卦=艮 AND 九三=艮其限]` `[factor_trigger: zhouyi_gua_gen]` `[role: 例外处理]` 艮其限，列其夤：止于腰际，脊背生裂。 → 《周易·艮卦·爻辞》
  - `[ns_zhouyi_476]` `[trigger: 卦=艮 AND 六四=艮其身]` `[factor_trigger: zhouyi_gua_gen]` `[role: 条件分支]` 艮其身，无咎：止于身体，无所咎责。 → 《周易·艮卦·爻辞》
  - `[ns_zhouyi_477]` `[trigger: 卦=艮 AND 六五=艮其辅]` `[factor_trigger: zhouyi_gua_gen]` `[role: 主干依赖]` 艮其辅，言有序：止于面颊，言语有序。 → 《周易·艮卦·爻辞》
  - `[ns_zhouyi_478]` `[trigger: 卦=艮 AND 上九=敦艮吉]` `[factor_trigger: zhouyi_gua_gen]` `[role: 总结]` 敦艮，吉：敦厚而止，大为吉祥。 → 《周易·艮卦·爻辞》
  - **中文**：
  - 卦辞"艮其背，不获其身，行其庭，不见其人，无咎"依通行王弼本；"艮其背"谓止于背，不见前身，无私欲之纷扰。
  - "兼山"之"兼"释为重叠、并列，上下皆艮，故曰"兼山"，如两山相峙而俱止。
  - "艮其趾/腓/限/身/辅"依次为足趾、小腿、腰脊、身体、面颊，由下而上展示"止"之不同层次。
  - "艮其限，列其夤"中"限"为腰际，"夤"为脊膂之肉；止于腰而不通上下，则脊背有裂之象。
  - "敦艮"之"敦"释为敦厚、笃实，厚重而止则吉。
  - **English**: Based on Wang Bi commentary edition. "艮其背" means stopping at the back without seeing the front—no selfish desires. "兼山" means doubled mountains. Body parts from 趾 to 辅 show levels of stillness. "敦艮" indicates substantial/grounded stopping."""
    normalized_text_zh: str = """"""
    subject: str = "艮卦（䷳）"
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
        l1_anchor="zy_v1.0.0_艮卦_001_L1",
    )
    version: str = "1.0.0"
