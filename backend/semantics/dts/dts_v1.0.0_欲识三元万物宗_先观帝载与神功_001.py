"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932630
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
    semantic_id="dts_v1.0.0_欲识三元万物宗_先观帝载与神功_001",
    book_id="dts",
    engine_id="bazi"
)
class 欲识三元万物宗先观帝载与神功(SemanticEntry):
    """
    - 原文（source_text）：
  欲识三元万物宗，先观帝载与神功。

- 原注（原文注解）：
  　　天有阴阳，故春木，夏火，秋金，冬水，季土。得时而显其神功，命中天地元之理，悉本于此，日干为...
    """
    
    original_text: str = """- 原文（source_text）：
  欲识三元万物宗，先观帝载与神功。

- 原注（原文注解）：
  　　天有阴阳，故春木，夏火，秋金，冬水，季土。得时而显其神功，命中天地元之理，悉本于此，日干为天元，地支为地元，支中所为人元。

- 分字分词释义：
  - 欲：将要、想要。
  - 识：认识、辨识、洞见其本源。
  - 三元：有两层常见指向。
    1) 天元、地元、人元（天地人三才之元）。
    2) 年元、月元、日元（历法纲纪的三纲，亦可扩“四柱”含时）。
  - 万物：世间万类事物、气机与人事。
  - 宗：宗旨、根本、总纲。
  - 先：先行、优先顺序。
  - 观：观察、审视、体会其运行。
  - 帝：天帝、天道之主宰，亦借指“天”。
  - 载：承载、运载、运行之轨（历法与时序的承载）。
  - 与：和、以及。
  - 神：神妙之机、不可见之用，造化之妙。
  - 功：功用、作为、效能（四时运化之功）。

- 规范化释义（primary_lang_explained）：
  想要认识三元（天地人、或年月日）所统摄的万事万物之根本，必须先观察“天”的运行承载（历法、节令、岁时）以及造化运作的功用（四时升降、寒燥温凉、阴阳消长）。先观天道纲纪，再入格局细论。

- **次语种完整诠释（secondary_lang_full）**：  
  To recognize the Three Foundations (Sanyuan: Heaven-Earth-Human or Year-Month-Day) as the root principle governing all phenomena, one must first observe the Imperial Mandate (Dizai: the celestial calendar cycles and seasonal nodes) and the Divine Workings (Shengong: the transformative functions of four seasons—spring Wood, summer Fire, autumn Metal, winter Water, and transitional Earth). Only by establishing this overarching celestial-temporal framework can one accurately descend into specific pattern analysis and mundane affairs. Without anchoring judgment to Dizai and Shengong, interpretations become fragmented and lack coherence with the grand ordering principle.

- **核心要点**：
  - 三元（天地人或年月日）是命理体系的总纲架构
  - 帝载指历法、节令、岁时的运转轨道，是时间轴承载面
  - 神功指四时造化的具体作用，是气机显现的方式
  - 先观天道纲纪，再入格局细论，此为论命总序
  - 不可离时令独言日主强弱，否则失"帝载与神功"的总纲
  - 历算法度必须精准，节气分界错误将导致根本性偏差

- **详细解说**：
  本条为《滴天髓》开篇总纲，确立命理分析的根本框架。"三元"指天元（日干为主体）、地元（地支为环境）、人元（藏干为作用），构成纵横三层结构。"帝载"喻天道运行之轨道，即历法节令的时序系统，是气机运行的时间坐标；"神功"指四时五行的造化功用，春生夏长秋收冬藏，是气机在具体时空中的显现方式。论命必先明此总纲：先定时令纲领（以月令为提纲），次观日主与当令气机的关系（得令或失令），再看干支配合（生克制化、通关泄化），最后裁取用神喜忌。若不先观"帝载与神功"，直接论格局喜忌，则如无根之木，判断必偏。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_001]` `[trigger: 论命起手]` `[factor_trigger: dizai_shengong]` `[role: 主干]` 欲断命先观月令，月令为帝载之首，定当令与失令。 → 《滴天髓·通天论》#第1条
  - `[ns_dts_002]` `[trigger: 节气交界]` `[factor_trigger: calendar_precision_boundary]` `[role: 条件分支]` 节气交界不明时，须以真太阳时精准校历，否则帝载错位全盘皆误。 → 《滴天髓·通天论》#第1条
  - `[ns_dts_003]` `[trigger: 三元定位]` `[factor_trigger: sanyuan_frame]` `[role: 主干依赖]` 天元日干为主体，地元支局为环境，人元藏干为作用，三者缺一不可。 → 《滴天髓·通天论》#第1条
  - `[ns_dts_097]` `[trigger: 论命法序]` `[factor_trigger: dizai_shengong]` `[role: 主干依赖]` 论命须先定时令纲领，再观日主与当令气机，最后裁取用神喜忌。 → 《滴天髓·通天论》#第1条
  - `[ns_dts_098]` `[trigger: 忽略帝载后果]` `[factor_trigger: dizai_shengong]` `[role: 总结]` 若不先观帝载与神功，直断格局喜忌，如无根之木，判断必偏。 → 《滴天髓·通天论》#第1条"""
    normalized_text_zh: str = """"""
    subject: str = "欲识三元万物宗，先观帝载与神功。"
    factor_refs: list = ['sanyuan_frame', 'dizai_shengong', 'shengong_function', 'tianyuan_layer', 'diyuan_layer', 'renyuan_layer']
    
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
        l1_anchor="dts_v1.0.0_欲识三元万物宗_先观帝载与神功_001_L1",
    )
    version: str = "1.0.0"
