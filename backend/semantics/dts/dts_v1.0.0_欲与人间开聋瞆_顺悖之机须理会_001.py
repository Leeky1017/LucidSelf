"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932693
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
    semantic_id="dts_v1.0.0_欲与人间开聋瞆_顺悖之机须理会_001",
    book_id="dts",
    engine_id="bazi"
)
class 欲与人间开聋瞆顺悖之机须理会(SemanticEntry):
    """
    - 原文（source_text）：
  欲与人间开聋瞆，顺悖之机须理会。

- 原注（原文注解）：
  　　不知命者如聋瞆，知命者于顺悖之机而能理会之，庶可以开之耳.

- 分字分词释义：
  - ...
    """
    
    original_text: str = """- 原文（source_text）：
  欲与人间开聋瞆，顺悖之机须理会。

- 原注（原文注解）：
  　　不知命者如聋瞆，知命者于顺悖之机而能理会之，庶可以开之耳.

- 分字分词释义：
  - 欲：欲要、希望.
  - 与：给予、启发.
  - 人间：世人、众人.
  - 开：开启、开悟.
  - 聋：听不见，比喻愚昧不达.
  - 瞆：目盲不明，比喻昧理.
  - 顺悖：顺应或违逆.
  - 之机：其中机括、关节点.
  - 须：必须.
  - 理会：明白、体认并掌握.

- 规范化释义（primary_lang_explained）：
  要启发世人从迷昧走向通达，必须让其真正理解顺与逆的关键处——何时顺、何时逆、逆当如何化、顺当如何持.

- **次语种完整诠释（secondary_lang_full）**：  
  To awaken people from confusion (Kai Long Kuai: opening the deaf and blind), one must help them truly comprehend the pivotal mechanisms (Ji) of accordance and contravention. These mechanisms are not static labels but dynamic thresholds determined by three factors: timing (seasonal mandate and cyclical phases), strength configuration (relative power of Day Master versus environmental forces), and relational sentiment (harmonious versus conflicting interactions among stems and branches). The pivotal moments occur where structure, timing, and choice intersect—these are the operational leverage points where slight adjustments can shift outcomes from inauspicious to auspicious or vice versa. The value of destiny analysis lies not in frightening people with fixed fate pronouncements, but in illuminating these actionable pivot-points and their operational sequences, enabling informed adjustment rather than passive resignation.

- **核心要点**：
  - 聋瞆喻不知命者的迷昧状态，理会指从迷昧到觉察的认知转化
  - 机指关键转折点，是结构-时机-选择三者交汇之处
  - 机在时令：顺悖随节令运岁变化而转，非永恒不变
  - 机在强弱：同一结构对身强者是机、对身弱者可能是压
  - 机在情义：生合有情则顺中有机，冲刑害深则悖中有险
  - 命理价值在于指出可调整的机位，而非静态的吉凶定论

- **详细解说**：
  本条强调"机"字的核心地位——命理的价值不在于恐吓人以吉凶，而在于指出"结构—时势—选择"三者交汇处的关键铰链。"机"有三层含义：机在时令（随节令、运岁、旺衰而转），机在强弱（同一五行对身强者是机、对身弱者是压），机在情义（生合有情则顺中有机，冲刑害深则悖中有险）。实占时，先点出关键机位（何支为枢、何干为钥），次示以法度（通关、制化、扶抑的优先顺序），再核以流年（观应期与力度）。顺悖非绝对，随岁运而变，逆要化、顺要持，皆须有度。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_010]` `[trigger: 命主不识机]` `[factor_trigger: ji_pivot_profile]` `[role: 主干]` 命主不识顺悖，如聋如瞆，纵遇良机亦不知用，逢险亦不知避。 → 《滴天髓·通天论》#第4条
  - `[ns_dts_011]` `[trigger: 运岁转换]` `[factor_trigger: ji_timing_pivot]` `[role: 条件分支]` 顺悖之机在运岁转换处显现时，宜预先指明，使命主有备无患。 → 《滴天髓·通天论》#第4条
  - `[ns_dts_012]` `[trigger: 机随势变]` `[factor_trigger: ji_pivot_profile]` `[role: 主干依赖]` 顺悖之机非静态，随时令强弱情义而变，须动态追踪而非一次定论。 → 《滴天髓·通天论》#第4条
  - `[ns_dts_103]` `[trigger: 三重机位]` `[factor_trigger: ji_trigger_conditions]` `[role: 主干依赖]` 顺悖之机兼具时令、强弱与情义三重含义，需同时评估方不失其枢纽。 → 《滴天髓·通天论》#第4条
  - `[ns_dts_104]` `[trigger: 实占用法]` `[factor_trigger: pivot_window_level]` `[role: 总结]` 实占时先点出关键机位，再示以通关制化次第，并配合流年验证应期与力度。 → 《滴天髓·通天论》#第4条"""
    normalized_text_zh: str = """"""
    subject: str = "欲与人间开聋瞆，顺悖之机须理会。"
    factor_refs: list = ['longkuai_state', 'ji_pivot_profile', 'lihui_awareness', 'ji_timing_pivot', 'ji_strength_pivot', 'ji_sentiment_pivot']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_欲与人间开聋瞆_顺悖之机须理会_001_L1",
    )
    version: str = "1.0.0"
