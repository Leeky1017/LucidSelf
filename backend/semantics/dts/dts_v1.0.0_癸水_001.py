"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.009030
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
    semantic_id="dts_v1.0.0_癸水_001",
    book_id="dts",
    engine_id="bazi"
)
class 癸水(SemanticEntry):
    """
    - 原文（source_text）：
  癸水至弱，达于天津，龙德而运，功化斯神，不畏火土，不论庚辛，合戊见火，化火乃真。

- 原注（原文注解）：
  　　癸乃纯阴而至弱，然上达天津，凡柱中有甲乙寅...
    """
    
    original_text: str = """- 原文（source_text）：
  癸水至弱，达于天津，龙德而运，功化斯神，不畏火土，不论庚辛，合戊见火，化火乃真。

- 原注（原文注解）：
  　　癸乃纯阴而至弱，然上达天津，凡柱中有甲乙寅卯，皆能运用水汽，生木制火，润土养金，如龙能运水，火土虽多不畏，至于庚辛，则不赖其生，亦不忌其多，惟合戊化火，必通火根，乃为真也。

- 分字分词释义：
  - 癸：阴水，至弱之水，如雨露雾气。
  - 至弱：十干中最柔弱者，细微渗透。
  - 达于天津：上接天河之津渡，象征灵性通天。
  - 龙德而运：如龙行云布雨，借木气运化水汽。
  - 功化斯神：化育之功精微入神，细致渗透。
  - 不畏火土：自有独特生存之道，不循常规生克。
  - 不论庚辛：不赖金生，亦不忌金多。
  - 合戊见火：癸戊相合化火，须有丙丁火根方为真化。

- 规范化释义（primary_lang_explained）：
  癸水为十干中最柔弱者，如雨露雾气，细微而能渗透万物。其特点在于"至弱而通天"：虽弱却能上达天津，借木气运化水汽如龙行云布雨，化育之功精微入神。癸水的生存之道与众不同：有木承运则能生木制火、润土养金，故"不畏火土"；自有灵性通道，不依赖金生亦不忌金多，故"不论庚辛"。癸戊相合化火是癸水成格的关键：必须有丙丁真火根支撑，方为真化有成，否则为虚化耗散。

- **次语种完整诠释（secondary_lang_full）**：  
  Gui Water is the most yin and subtle among all stems—the image of dew, mist, and fine rain rather than rivers or oceans. Its nature is "weakest yet reaching heaven" (Zhi Ruo Da Yu Tianjin): though appearing the most delicate, Gui connects to the celestial ford where heavenly water and earthly moisture meet, possessing a spiritual channel that transcends ordinary strength metrics. Gui's operational principle is "dragon virtue in motion" (Longde Er Yun): like a dragon that moves clouds and brings rain, Gui requires Wood (Jia-Yi, Yin-Mao) to carry and direct its moisture. With proper wood support, Gui can generate wood to control fire, moisten earth to nurture metal—accomplishing transformation through subtle penetration rather than direct force. This explains why Gui "does not fear fire or earth" and "does not depend on metal": its unique pathway bypasses conventional generating-controlling cycles. The critical formation is Gui-Wu combination transforming to Fire: this transformation is genuine only when supported by real Bing-Ding fire roots in the chart. Without such roots, the combination becomes hollow exhaustion rather than productive transformation—the difference between "divine transformation" and "empty dissipation."

- **核心要点**：
  - 癸为阴水，至弱之水，如雨露雾气
  - 达于天津：上接天河，灵性通天
  - 龙德而运：借木气运化水汽，如龙布雨
  - 功化斯神：化育之功精微入神
  - 不畏火土：有木承运则不循常规生克
  - 不论庚辛：不赖金生亦不忌金多
  - 合戊见火化火乃真：癸戊合化须有真火根

- **详细解说**：
  癸水为阴水之代表，为十干中最柔弱者，如雨露雾气，细微而能渗透万物。与壬水的"汪洋刚中"形成对照，癸水的精髓在于"至弱而通天"——虽是最弱之水，却能上达天津，拥有独特的灵性通道。癸水的运化之道在于"龙德"：需借甲乙寅卯等木气承运水汽，如龙行云布雨，方能发挥"功化斯神"的精微化育之功。有木承运时，癸水能生木制火、润土养金，故"不畏火土"；癸水自有灵性出路，不依赖金生亦不忌金多，故"不论庚辛"。癸戊相合化火是癸水成格的关键：必须有丙丁真火根支撑，方为"真化"有成；若无火根，则为"虚化"耗散，反成无功之合。判断癸水命局时，关键看木气承运与戊合真假。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_052]` `[trigger: 日主=癸水]` `[factor_trigger: tiangan_gui]` `[role: 主干]` 癸水至弱达于天津，如雨露雾气，灵性通天而功化斯神。 → 《滴天髓·天干论》#癸水
  - `[ns_dts_053]` `[trigger: 癸水见甲乙寅卯]` `[factor_trigger: gui_wood_carrier]` `[role: 主干依赖]` 癸水得木承运如龙布雨，能生木制火润土养金。 → 《滴天髓·天干论》#癸水
  - `[ns_dts_054]` `[trigger: 癸戊相合]` `[factor_trigger: gui_wu_transformation]` `[role: 条件分支]` 癸戊合化火，须有丙丁真火根方为真化，否则虚化耗散。 → 《滴天髓·天干论》#癸水
  - `[ns_dts_131]` `[trigger: 癸水不畏火土]` `[factor_trigger: gui_independence]` `[role: 例外处理]` 癸水有木承运则不畏火土，不循常规生克之理。 → 《滴天髓·天干论》#癸水
  - `[ns_dts_132]` `[trigger: 癸水不论庚辛]` `[factor_trigger: gui_independence]` `[role: 总结]` 癸水自有灵性通道，不赖金生亦不忌金多，故不论庚辛。 → 《滴天髓·天干论》#癸水"""
    normalized_text_zh: str = """"""
    subject: str = "癸水"
    factor_refs: list = ['gui_zhiruo', 'tiangan_gui_tianjin', 'gui_longde_yun', 'gui_gonghua_sishen', 'gui_buwei_huotu', 'gui_hewu_huozhihen']
    
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
        l1_anchor="dts_v1.0.0_癸水_001_L1",
    )
    version: str = "1.0.0"
