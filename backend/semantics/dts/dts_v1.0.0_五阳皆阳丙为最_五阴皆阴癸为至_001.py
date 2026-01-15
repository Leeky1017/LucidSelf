"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932721
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
    semantic_id="dts_v1.0.0_五阳皆阳丙为最_五阴皆阴癸为至_001",
    book_id="dts",
    engine_id="bazi"
)
class 五阳皆阳丙为最五阴皆阴癸为至(SemanticEntry):
    """
    - 原文（source_text）：
  五阳皆阳丙为最，五阴皆阴癸为至.

- 原注（原文注解）：
  　　甲，丙，戊，庚，壬，为阳，独丙火禀阳之精，而为阳中之阳.
  
  　　乙，丁，己，辛，癸...
    """
    
    original_text: str = """- 原文（source_text）：
  五阳皆阳丙为最，五阴皆阴癸为至.

- 原注（原文注解）：
  　　甲，丙，戊，庚，壬，为阳，独丙火禀阳之精，而为阳中之阳.
  
  　　乙，丁，己，辛，癸，为阴，独癸水禀阴之精，而为阴中之阴.

- 分字分词释义：
  - 五阳：甲、丙、戊、庚、壬.
  - 最：至盛、阳中之阳.
  - 五阴：乙、丁、己、辛、癸.

- 规范化释义（primary_lang_explained）：
  五阳干中，丙火为阳之极；五阴干中，癸水为阴之纯。此言性类之纲，示判干性之极点坐标.

- **次语种完整诠释（secondary_lang_full）**：  
  Among the Five Yang stems (Jia, Bing, Wu, Geng, Ren), Bing Fire represents the extreme of yang—yang within yang (Yang Zhong Zhi Yang). Among the Five Yin stems (Yi, Ding, Ji, Xin, Gui), Gui Water embodies the ultimate yin—yin within yin (Yin Zhong Zhi Yin). These two establish the polar coordinates of a stem polarity axis for measuring the overall yin-yang balance of any chart. Bing epitomizes brightness, outward radiation, and manifest expression; Gui epitomizes moistening subtlety, inward concealment, and latent transformation. Each of the Ten Heavenly Stems occupies a specific position on this axis, with varying distances from the poles indicating degrees of yang vigor or yin receptivity. Proper destiny analysis requires assessing where the Day Master and overall configuration sit on this axis, then determining appropriate regulatory strategies—softening excessive yang with cooling moisture, or activating deficient yin through flow and transformation—to prevent imbalance from extreme concentration at either pole without counterbalance.

- **核心要点**：
  - 五阳干：甲丙戊庚壬；五阴干：乙丁己辛癸
  - 丙火为阳中之阳，象征光明、外放、显性
  - 癸水为阴中之阴，象征润下、内藏、隐性
  - 丙癸构成阴阳轴的两个极点坐标
  - 十天干在此轴上各有位置，既有阴阳方向，也有强弱远近之分
  - 判断命局整体阴阳偏颇与调剂方向的基准参照

- **详细解说**：
  本条建立天干阴阳轴的极点坐标系。十天干分为两组：五阳干（甲丙戊庚壬）与五阴干（乙丁己辛癸）。在阳干中，丙火为"阳中之阳"，禀阳之精，光明外放；在阴干中，癸水为"阴中之阴"，禀阴之精，润下内藏。以丙、癸为两极，可构建一条阴阳轴，衡量命局整体的阴阳偏颇程度。实占时，先判断日主在阴阳轴上的位置（近丙极、近癸极或中性），再结合格局用神判断是否需要调剂——阳极过燥则需水木润化，阴极过郁则需火土激活。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_019]` `[trigger: 阴阳定位]` `[factor_trigger: tiangan_polarity_axis]` `[role: 主干]` 五阳干中丙火为阳之极，五阴干中癸水为阴之纯，此为判干性的极点坐标。 → 《滴天髓·通天论》#第7条
  - `[ns_dts_020]` `[trigger: 阳极过燥]` `[factor_trigger: bing_huo_pole]` `[role: 条件分支]` 命局若偏近丙极而燥烈无制，宜以水木润化，使阳不焚枯。 → 《滴天髓·通天论》#第7条
  - `[ns_dts_021]` `[trigger: 阴极过郁]` `[factor_trigger: gui_shui_pole]` `[role: 条件分支]` 命局若偏近癸极而阴沉无激，宜以火土激活，使阴不凝滞。 → 《滴天髓·通天论》#第7条
  - `[ns_dts_109]` `[trigger: 阴阳轴构建]` `[factor_trigger: tiangan_polarity_axis]` `[role: 主干依赖]` 以丙火与癸水为两极，可构建十天干在其上的阴阳轴，用以衡量整体偏阳或偏阴。 → 《滴天髓·通天论》#第7条
  - `[ns_dts_110]` `[trigger: 调剂路径]` `[factor_trigger: yinyang_adjustment]` `[role: 总结]` 实占先判日主在阴阳轴上的位置，再配合格局用神决定是减火增水还是减水增火。 → 《滴天髓·通天论》#第7条"""
    normalized_text_zh: str = """"""
    subject: str = "五阳皆阳丙为最，五阴皆阴癸为至."
    factor_refs: list = ['wuyang_group', 'wuyin_group', 'bing_huo_pole', 'gui_shui_pole', 'tiangan_bing', 'tiangan_gui']
    
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
        l1_anchor="dts_v1.0.0_五阳皆阳丙为最_五阴皆阴癸为至_001_L1",
    )
    version: str = "1.0.0"
