"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412879
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
    semantic_id="smth_v1.0.0_木火交辉与木火通明之局_001",
    book_id="sanming",
    engine_id="bazi"
)
class 木火交辉与木火通明之局(SemanticEntry):
    """
    - **原文（source_text）**：

  赋云：火明木秀，生春月以为荣。此象乃甲戌、甲午、甲寅、丙午、丙寅、丙戌等日，生春月或夏月，柱无金水伤坏，时上有木火。行木火运，木日火秀，行南方运，火...
    """
    
    original_text: str = """- **原文（source_text）**：

  赋云：火明木秀，生春月以为荣。此象乃甲戌、甲午、甲寅、丙午、丙寅、丙戌等日，生春月或夏月，柱无金水伤坏，时上有木火。行木火运，木日火秀，行南方运，火日木秀，行东方运，主清贵福厚，火日火秀，行东亦贵。如丙辰日生火旺月，行木火运亦可，但富而不贵，木秀无火，则不成局，以木火有通明之象故也。如：丁巳、甲辰、甲寅、丁卯；甲午、丙寅、丁卯、丙午；丁巳、甲辰、乙巳、丁亥。三命皆木火光辉，清贵之造。

- 分字分词释义：

  - **火明木秀**：火明指火光烈而不浊，木秀指木气生发而有文采；木火相映，成“通明光辉”之象。
  - **生春月以为荣**：春令木旺，木得其时而秀；夏月火旺，若木火相资，亦可成局。
  - **甲戌、甲午、甲寅、丙午、丙寅、丙戌等日**：列举木火交辉的典型日柱，或木日带火，或火日带木。
  - **柱无金水伤坏，时上有木火**：忌金水过重来伤木、熄火；时支若有木火，则格局更显光辉通明。
  - **木日火秀 / 火日木秀**：木日主若得火相生，则才华被点亮；火日主若得木相生，则火得源头，光明不绝。
  - **木秀无火，则不成局**：若只有木之生发而缺少火之照耀，则难成“木火交辉”的上格。

- **规范化释义（primary_lang_explained）**：

  木火交辉格，以“木火相生而成通明之象”为核心。甲木、丙火互为生扶：木为柴薪，火为光明；木盛而火得其材，则火光绵长而不熄；火旺而木得其护，则火不至于枯焦。原文以甲戌、甲午、甲寅、丙午、丙寅、丙戌等日为例，说明木日得火、火日得木时，若生于春夏、四柱又无金水重伤，则多主清贵福厚。

  行运上，木日主喜南方火运，使“火秀”以显木之用；火日主喜东方木运，使“木秀”以生火之明；火日若再行东方木运，亦可因木火互动而得贵。反之，若仅见木秀而无火照，则如枝叶繁茂而无光照耀，难以成就突出之名；若火旺而缺木，便如烈焰无薪，虽一时炽盛，却难以持久。

- 核心要点：

  - 以**木火相生、通明光辉**为主轴，典型组合多见于甲、丙等日柱。
  - 忌金水来重伤木、熄火，尤其金多克木、水多浇火之局。
  - 行运取木火为佳，东方木运、南方火运皆能增益其清贵之象。

- 详细解说：

  若从性格与人生路径角度看，木火交辉格的人往往具备：思路活跃（木）、表达热烈（火）、审美与创造力兼具的特质。由木之“生长”与火之“表现”结合而成的能量，适合流向教育、文化、艺术、传播等需要创意与表达的领域。

  然而，这种格局也有其隐忧：火过而木弱时，易流于躁急、虚张声势；木多而火弱时，则多为理想主义而缺乏执行力。故在判断时，需要细察：

  1. 木火之比重是否协调；
  2. 金水是否过多干扰，特别是金多折木、水多熄火；
  3. 行运是否维持或破坏木火通明之局。若行运有利，多见“清贵而不俗”的人生轨迹；若行运反向，则可能表现为情绪波动大、创作能量难以落地。

- **校勘与字词辨析（双语）**：

  - 原文“火明木秀，生春月以为荣”一句，本稿在释义中分解为“木旺为根、火明为用”，并在白话中以“通明之象”概括。
  - 文末所列三造示例，本稿仅以“木火光辉、清贵之造”概括其共性，不逐一推演具体命局。
  - “柱无金水伤坏，时上有木火”一句，本稿在详细解说中具体化为“忌金水过多、喜木火行运”的判断框架。
  - **English**：
    - Judgment framework for wood-fire fortune cycles established.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_205]` `[trigger: 木火交辉]` `[factor_trigger: muhuojiaohui_presence AND chunxia_muhuo]` `[role: 主干]` 火明木秀，生春月以为荣。 → 《三命通会》卷六#木火交辉
  - `[ns_smth_06_206]` `[trigger: 通明光辉]` `[factor_trigger: muhuo_tongming AND qinggui_fuhou]` `[role: 主干依赖]` 以木火有通明之象故也。 → 《三命通会》卷六#木火交辉
  - `[ns_smth_06_207]` `[trigger: 无金水伤]` `[factor_trigger: zhu_wu_jinshui AND cheng_ge]` `[role: 条件分支]` 柱无金水伤坏，时上有木火。 → 《三命通会》卷六#木火交辉
  - `[ns_smth_06_208]` `[trigger: 清贵福厚]` `[factor_trigger: muhuo_xingnan AND qinggui_fuhou]` `[role: 总结]` 主清贵福厚。 → 《三命通会》卷六#木火交辉"""
    normalized_text_zh: str = """"""
    subject: str = "木火交辉与木火通明之局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wood_fire_marker', 'bazi_semantic', 'bazi_structure_wood_fire_config', 'bazi_semantic', 'bazi_state_degree_35', 'bazi_semantic', 'bazi_state_factor_34', 'bazi_semantic', 'bazi_condition_metal_water_3', 'bazi_semantic', 'bazi_condition_factor_215', 'bazi_semantic', 'source_ref', 'rel_smth_06_181', 'muhuojiaohui_presence', 'rel_smth_06_182', 'tongming_chengdu', 'rel_smth_06_183', 'jinshui_shanghuai_risk', 'evi_smth_06_181', 'muhuojiaohui_presence', 'rule_muhuojiaohui', 'evi_smth_06_182', 'qinggui_fuhou', 'rule_qinggui', 'evi_smth_06_183', 'jinshui_shanghuai_risk', 'rule_jinshui', 'map_smth_06_121', 'map_smth_06_122']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_木火交辉与木火通明之局_001_L1",
    )
    version: str = "1.0.0"
