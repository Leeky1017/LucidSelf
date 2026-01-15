"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997243
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
    semantic_id="dts_v1.0.0_阳乘阳位阳气昌_最要行程安顿_001",
    book_id="dts",
    engine_id="bazi"
)
class 阳乘阳位阳气昌最要行程安顿(SemanticEntry):
    """
    - **原文（source_text）**：
  阳乘阳位阳气昌，最要行程安顿.


- 原注（原文注解）：
  　　六阳之位，独子寅辰为阳方，乃阳位之纯，五阳居之，其旺无比，其行运最宜阴顺安顿之地....
    """
    
    original_text: str = """- **原文（source_text）**：
  阳乘阳位阳气昌，最要行程安顿.


- 原注（原文注解）：
  　　六阳之位，独子寅辰为阳方，乃阳位之纯，五阳居之，其旺无比，其行运最宜阴顺安顿之地.


- 分字分词释义：
  - 阳乘阳位：阳干阳支相得其位.
  - 阳气昌：阳气昌盛.
  - 行程安顿：行运所至，应求安顿之宜（阴顺处）.


- **规范化释义（primary_lang_explained）**：
  阳居阳位，势最昌盛.But行运所至，当以“安顿”为先，阴顺之地更能涵养其盛，不可躁进.

- **次语种完整诠释（secondary_lang_full）**:
  When yang stems occupy yang branch positions (such as Yin, Chen), yang energy reaches its peak. However, the key to long-term fortune lies in "settling" during transit periods. When moving through yin-natured environments, the strong yang energy can be properly nurtured and contained.

- **核心要点**：
  - 阳乘阳位主势大位正，但亦最怕过热与躁进.
  - 行运宜往阴顺安顿之地，以涵养、沉实既有之盛.
  - 若再入阳动险地，易因过刚过急而折损福力.
  - 断此条时，要把“位正”与“行缓”“阴顺”联成一体看.

- **详细解说**：
  阳干坐于寅、辰等阳方，本身就象征着站在前台、居于高位，气势昂扬、行动力强。一旦再逢岁运助旺，容易出现“人到山巅”的状态：外在机会、资源与能见度都被推向高点。这时若仍以加速、争抢、冒进为主调，就像在烈日之下再加柴火，短期看似更烈，长期却易因体力不支、人事反噬或环境承受不了而急转直下.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_082]` `[trigger: 命局形成阳乘阳位]` `[factor_trigger: yang_on_yang_position_pattern==阳乘阳 AND yang_intensity_level IN {极旺, 强} AND transit_dest_yinyang==阴静 AND settlement_priority==高]` `[role: 主干]` 阳乘阳位而阳气已昌，行运以阴顺安顿为上，不宜再求险捷猛进. → 《滴天髓·行运论》#阳乘阳位
  - `[ns_dts_083]` `[trigger: 阳乘阳位行运入阴静之乡]` `[factor_trigger: yang_on_yang_position_pattern==阳乘阳 AND yang_intensity_level IN {极旺, 强} AND transit_dest_yinyang==阴静 AND settlement_priority==高]` `[role: 主干依赖]` 阳局行运临阴柔安静之地，多主功成身稳，势不再躁而得以长久. → 《滴天髓·行运论》#阳乘阳位
  - `[ns_dts_084]` `[trigger: 阳乘阳位行运再入阳动险地]` `[factor_trigger: yang_on_yang_position_pattern==阳乘阳 AND yang_intensity_level IN {极旺, 强} AND transit_dest_yinyang==阳动]` `[role: 条件分支]` 阳乘阳位又逢阳动险地，易因过热过急而折损，须防"高处不胜寒". → 《滴天髓·行运论》#阳乘阳位
  - `[ns_dts_151]` `[trigger: 阳极无阴顺]` `[factor_trigger: yang_on_yang_position_pattern==阳乘阳 AND yang_intensity_level==极旺 AND transit_dest_yinyang!=阴静 AND settlement_priority!=高]` `[role: 例外处理]` 阳乘阳位而行运无阴顺涵养，易成烈火燎原终归灰烬. → 《滴天髓·行运论》#阳乘阳位
  - `[ns_dts_152]` `[trigger: 位正行缓总则]` `[factor_trigger: yang_on_yang_position_pattern==阳乘阳 AND settlement_priority==高 AND transit_dest_yinyang==阴静]` `[role: 总结]` 阳乘阳位贵在位正，行运贵在缓进，位正行缓方能长久. → 《滴天髓·行运论》#阳乘阳位

- **校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "阳乘阳位阳气昌，最要行程安顿."
    factor_refs: list = ['yangcheng_yangwei', 'yangqi_chang', 'xingcheng_andun', 'yinshun', 'hanyang', 'zaojin']
    
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
        l1_anchor="dts_v1.0.0_阳乘阳位阳气昌_最要行程安顿_001_L1",
    )
    version: str = "1.0.0"
