"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997252
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
    semantic_id="dts_v1.0.0_阴乘阴位阴气盛_还须道路光亨_001",
    book_id="dts",
    engine_id="bazi"
)
class 阴乘阴位阴气盛还须道路光亨(SemanticEntry):
    """
    - **原文（source_text）**：
  阴乘阴位阴气盛，还须道路光亨。

- 原注（原文注解）：
 　　六阴之位，独未酉亥为阴方，乃阴位之纯，五阴居之，其盛无比，其行运宜阳明光亨之地。

-...
    """
    
    original_text: str = """- **原文（source_text）**：
  阴乘阴位阴气盛，还须道路光亨。

- 原注（原文注解）：
 　　六阴之位，独未酉亥为阴方，乃阴位之纯，五阴居之，其盛无比，其行运宜阳明光亨之地。

- 分字分词释义：
  - 阴乘阴位：阴干阴支相得其位.
  - 光亨：光明而亨通.

- **规范化释义（primary_lang_explained）**：
  阴干坐纯阴之支而阴气极盛，本性偏向内敛深藏。若行运之路幽闭不通，则易积郁停滞；唯有趋向光明开阔、人来人往之方，方能以阳明之气开启深阴，使其由藏而用、由暗而显.

- **次语种完整诠释（secondary_lang_full）**:  
  When a yin stem sits on a pure yin branch, yin qi becomes extremely concentrated and tends to turn inward, hidden and still. Such a configuration is rich in depth but easily drifts toward seclusion, over‑protection or stagnation if it lacks bright, open routes into the world. The life path therefore needs environments and movements that are well lit, public and accessible: roads where people, information and opportunities flow, so that what has been cultivated in the dark can meet sunlight. In this way, extreme yin is opened by appropriate yang: what was closed and withdrawn can be transformed into visible contribution, and the chart avoids sinking into isolation or excessive heaviness.

- **核心要点**：
  - 阴乘阴位阴气极盛，本身偏向深藏内敛，不宜再增一层幽闭.
  - 行运之路宜往阳明光亨、道路开阔之地，以路通、人通来疏导阴盛.
  - 若再行幽暗闭塞之方，则易陷封闭孤立与停滞，难以见到实际出路.

- **详细解说**：
  阴乘阴位之局，好比人在深处、暗处长期用功：一方面蕴藏着厚积的能量与经验，另一方面也容易形成对外界的防御与躲避。阴气愈盛，愈倾向于以退缩、隐居、自我封闭来回应世界；若环境又是幽暗逼仄、人迹罕至，便更加剧这种封闭，久而久之形成郁结与停滞.

  因此经文强调“还须道路光亨”：不是否定阴乘阴位本身，而是提醒必须以阳明之路来调节——行运所至之地宜光明开阔、人气交流、资讯流动，使深阴得以被阳气引出，原本潜藏的力量得以进入现实舞台.断此条时，一要看阴乘阴位是否极盛，二要看行运道路是光亨还是幽闭，三要评估命主是否愿意从暗处走向光处.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_085]` `[trigger: 命局形成阴乘阴位且阴气极盛]` `[factor_trigger: yin_on_yin_position_pattern & yin_intensity_level=极盛]` `[role: 主干]` 阴乘阴位而阴气极盛者，多主才情深藏不露，若所处环境又偏幽闭，则易见郁滞与自我封锁. → 《滴天髓·地支论》#阴乘阴位阴气盛
  - `[ns_dts_086]` `[trigger: 阴乘阴位行运临阳明光亨之地]` `[factor_trigger: yin_on_yin_position_pattern & path_brightness_level=光亨开阔]` `[role: 主干依赖]` 阴局行运至阳明光亨之方，往往应在走出暗处、登上舞台、结识人群之际，原本深藏之力开始发挥作用. → 《滴天髓·地支论》#阴乘阴位阴气盛
  - `[ns_dts_087]` `[trigger: 阴乘阴位行运仍入幽闭阴方]` `[factor_trigger: yin_on_yin_position_pattern & yin_stagnation_risk=on]` `[role: 条件分支]` 阴乘阴位再行幽暗闭塞之地，多见闭门思虑、自困于局，须防因长久不见天日而生身心郁疾. → 《滴天髓·地支论》#阴乘阴位阴气盛
  - `[ns_dts_153]` `[trigger: 阴极无光路]` `[factor_trigger: yin_on_yin_position_pattern & path_brightness_level=幽暗]` `[role: 例外处理]` 阴乘阴位而行运无阳明光亨，深阴久闭终成郁结之疾. → 《滴天髓·地支论》#阴乘阴位阴气盛
  - `[ns_dts_154]` `[trigger: 阴阳互济总则]` `[factor_trigger: yin_on_yin_position_pattern & path_brightness_level]` `[role: 总结]` 阴乘阴位贵在深藏，行运贵在光亨，阴极需阳启方能化幽为明. → 《滴天髓·地支论》#阴乘阴位阴气盛

 - **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "阴乘阴位阴气盛，还须道路光亨。"
    factor_refs: list = ['yincheng_yinwei', 'yinqi_sheng', 'daolu_guangheng', 'guangheng', 'youbi', 'yangming_kaiqi']
    
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
        l1_anchor="dts_v1.0.0_阴乘阴位阴气盛_还须道路光亨_001_L1",
    )
    version: str = "1.0.0"
