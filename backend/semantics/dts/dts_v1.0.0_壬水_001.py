"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.009013
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
    semantic_id="dts_v1.0.0_壬水_001",
    book_id="dts",
    engine_id="bazi"
)
class 壬水(SemanticEntry):
    """
    - 原文（source_text）：
  壬水汪洋，能泄金气，刚中之德，周流不滞，通根透癸，冲天奔地，化则有情，从则相济。

- 原注（原文注解）：
  　　壬乃癸水之源，有分有合，运行不息，为百川，...
    """
    
    original_text: str = """- 原文（source_text）：
  壬水汪洋，能泄金气，刚中之德，周流不滞，通根透癸，冲天奔地，化则有情，从则相济。

- 原注（原文注解）：
  　　壬乃癸水之源，有分有合，运行不息，为百川，亦为雨露，不可岐而二之，壬水能泄西方金气，其德刚中而又周流不滞，若遇申子辰，而又透癸，则其势不可遏也，合丁化木，又生丁火，可谓有情，能制丙火，不夺丁之爱，故为夫义而为君仁，生于九夏，则巳午未中土之气，得壬水薰蒸而成雨露，故虽从火土，未尝不相济也。

- 分字分词释义：
  - 壬：阳水，汪洋大水，如江河湖海。
  - 汪洋：广阔深远，水势浩大。
  - 能泄金气：水能泄金之锐气，金水相生。
  - 刚中之德：外柔内刚，刚健而居中。
  - 周流不滞：循环流动，不停滞不淤塞。
  - 通根透癸：地支有申子辰水局，天干透出癸水。
  - 冲天奔地：水势浩大，不可遏制。
  - 化则有情：壬丁合化木，木又生丁火，有情有义。
  - 从则相济：从火土之势时，能以水润之，相济为用。

- 规范化释义（primary_lang_explained）：
  壬水如江河汪洋，水势浩大而周流不滞。其特点在于"刚中有德"：能泄金之锐气使金更清，自身刚健而不偏激，循环流动而不淤塞。壬水若通根于申子辰并透癸水，则势如冲天奔地，不可阻遏。壬丁相合化木，木又生丁火，此为"化则有情"；壬水能制丙火而不夺丁火之爱，此为"夫义君仁"。即使在夏月从火土之势，壬水仍能以水润火土，相济为用而非完全臣服。

- **次语种完整诠释（secondary_lang_full）**：  
  Ren Water is the image of vast oceans, great rivers, and boundless lakes—expansive, deep, and constantly flowing. Its nature embodies "virtue within firmness" (Gang Zhong Zhi De): though appearing soft as water, it possesses inner strength and central balance. Ren excels at draining Metal's sharpness, making Metal clearer and more refined through the generating cycle. Its circulation never stagnates—it flows continuously, adapting to terrain while maintaining momentum. When Ren has roots in Shen-Zi-Chen water frame and Gui Water emerges in the stems, its power becomes unstoppable, "rushing to heaven and racing across earth." The Ren-Ding combination demonstrates sophisticated relationship dynamics: Ren combines with Ding to transform into Wood, and this Wood then generates Ding Fire—a cycle of mutual benefit that exemplifies "transformation with affection" (Hua Ze You Qing). Ren can control Bing Fire without stealing Ding Fire's love, acting as both righteous husband and benevolent ruler. Even when apparently following Fire-Earth dominance in summer, Ren Water provides crucial moisture that allows the fire-earth system to function productively—"following yet mutually assisting" (Cong Ze Xiang Ji) rather than mere submission.

- **核心要点**：
  - 壬为阳水，如江河汪洋，水势浩大
  - 刚中之德：外柔内刚，刚健居中
  - 能泄金气：金水相生，泄金之锐
  - 周流不滞：循环流动，不停滞淤塞
  - 通根透癸冲天奔地：申子辰透癸则势不可遏
  - 化则有情：壬丁合化木生丁火，有情有义
  - 从则相济：从火土势时仍能润济为用

- **详细解说**：
  壬水为阳水之代表，如江河湖海，汪洋广阔而周流不滞。其精髓在于"刚中有德"——虽为水却内蕴刚健之气，不是软弱无力而是柔中带刚。壬水能泄金之锐气，使金更清秀；自身循环流动，顺势而行却不淤塞。当壬水通根于申子辰水局并透出癸水时，水势浩大如冲天奔地，不可阻遏——此时为壬水最强盛之态。壬丁相合化木是命理中的佳配：木又能生丁火，形成"化则有情"的良性循环；壬水能制丙火而不夺丁火之爱，体现"夫义君仁"的高级关系处理。即使在夏月火土当令，壬水"从"其势时仍能发挥润济作用，使火土不至于燥烈——这便是"从则相济"的深意。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_049]` `[trigger: 日主=壬水]` `[factor_trigger: tiangan_ren]` `[role: 主干]` 壬水如江河汪洋，刚中有德，周流不滞而势大力强. → 《滴天髓·天干论》#壬水
  - `[ns_dts_050]` `[trigger: 壬水通根透癸]` `[factor_trigger: ren_root_gui]` `[role: 主干依赖]` 壬水通根申子辰透癸，冲天奔地势不可遏. → 《滴天髓·天干论》#壬水
  - `[ns_dts_051]` `[trigger: 壬丁相合]` `[factor_trigger: ren_ding_combination]` `[role: 条件分支]` 壬丁合化木，木又生丁火，化则有情，夫义君仁. → 《滴天髓·天干论》#壬水
  - `[ns_dts_129]` `[trigger: 壬水从火土]` `[factor_trigger: ren_following]` `[role: 例外处理]` 夏月壬水从火土势，仍能润济为用，非全然臣服. → 《滴天髓·天干论》#壬水
  - `[ns_dts_130]` `[trigger: 壬水泄金]` `[factor_trigger: ren_metal_drainage]` `[role: 总结]` 壬水能泄金之锐气，金水相生使金更清秀. → 《滴天髓·天干论》#壬水"""
    normalized_text_zh: str = """"""
    subject: str = "壬水"
    factor_refs: list = ['ren_wangyang', 'tiangan_ren_gangzhong', 'ren_zhouliu_buzhi', 'ren_chongtian_bendi', 'ren_huaze_youqing', 'ren_congze_xiangji']
    
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
        l1_anchor="dts_v1.0.0_壬水_001_L1",
    )
    version: str = "1.0.0"
