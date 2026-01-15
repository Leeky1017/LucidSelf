"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412619
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
    semantic_id="smth_v1.0.0_岁带正马与祖业承继_001",
    book_id="sanming",
    engine_id="bazi"
)
class 岁带正马与祖业承继(SemanticEntry):
    """
    - **原文（source_text）**：

  岁带正马：如甲日午年己，乙日巳年戊，喜忌与月干正财同。若岁带正马，生辰戌丑未月或夏令月中，己土旺相，不犯刑冲分夺，日干乘旺，主受祖业丰厚。若生寅卯月...
    """
    
    original_text: str = """- **原文（source_text）**：

  岁带正马：如甲日午年己，乙日巳年戊，喜忌与月干正财同。若岁带正马，生辰戌丑未月或夏令月中，己土旺相，不犯刑冲分夺，日干乘旺，主受祖业丰厚。若生寅卯月令，柱中更带比肩，或遇运行伤劫之地，必主贫困。

- 分字分词释义：

  - **岁带正马**：以流年干支（岁支）上见正财所临之驿马，例如甲日逢午年己、乙日逢巳年戊等。
  - **喜忌与月干正财同**：判断利害的原则与月令上正财格相似，仍重身强、财得地、不被分夺。
  - **生辰戌丑未月或夏令月中，己土旺相**：在辰戌丑未或夏季土旺之时，土财得令、驿马有根。
  - **不犯刑冲分夺**：忌再见刑冲、比劫来分马上之财，破坏其承继之象。

- **规范化释义（primary_lang_explained）**：

  岁带正马，主要谈的是“流年之马”与正财相连时，对祖业与外来资源的影响。若甲日在某年逢午年己、乙日逢巳年戊等，岁支所临之马与正财同来，且又恰在己土旺相之辰戌丑未月或夏令，则往往意味着：

  - 家族既有一定基础（祖业、田产、旧有资源）；
  - 当年有机会“骑马承财”，承接或放大既有资源。

  若反之，岁马落在寅卯等比劫旺地，又兼行伤劫之运，则马成“奔波之马”、财成“分争之财”，反而主耗损与贫困。

- 核心要点：

  - 岁带正马偏重于**年度机缘与祖业承接**，不是长期结构，而是流年触发。
  - 关键在土财是否旺相、有根，以及是否免于刑冲与比劫分夺。
  - 身弱者得印比扶持，则承继之象较吉；身强而再逢比劫，则易成“争产”与“破家”。

- 详细解说：

  从结构上看，岁带正马可视作“在年度层面，把财星与驿马叠加”的一种状态：马主动、主迁移、主变化；财主资源与资产。当二者同来时，人往往在那一年有明显的资源移动——例如继承、置业、迁居、扩大经营等。

  若命局本就以财为用、身能胜任，则这样的流年往往是“顺风借马之年”；若命局财多身弱，又行比劫、伤劫之地，则同样的组合反而对应“被迫应对家产变动、债务重组”等事件。故判断时需将岁运、原局与家世背景一并参看。

- **校勘与字词辨析（双语）**：

  - 本节原文极为简练，仅以“喜忌与月干正财同”一句带过，本稿在释义与白话中按卷内正财格的原则加以展开。
  - 例中“甲日午年己、乙日巳年戊”等语，本稿不逐一换算纳音与马星，只就“岁支为马、干支合成正财”的大原则说明。
  - **English**:
    - General principle explanation of "transforming into direct wealth" is provided.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_105]` `[trigger: 岁带正马]` `[factor_trigger: nianzhu_zhengcai AND yima_weizhi]` `[role: 主干]` 岁带正马，如甲日午年己，乙日巳年戊，喜忌与月干正财同。 → 《三命通会》卷六#岁带正马
  - `[ns_smth_06_106]` `[trigger: 祖业丰厚]` `[factor_trigger: jitu_wangxiang AND bu_xingchong]` `[role: 主干依赖]` 生辰戌丑未月或夏令月中，己土旺相，不犯刑冲分夺，主受祖业丰厚。 → 《三命通会》卷六#岁带正马
  - `[ns_smth_06_107]` `[trigger: 比肩贫困]` `[factor_trigger: yinmao_yueling AND bijian_shangjie]` `[role: 条件分支]` 若生寅卯月令，柱中更带比肩，或遇运行伤劫之地，必主贫困。 → 《三命通会》卷六#岁带正马
  - `[ns_smth_06_108]` `[trigger: 岁马承财]` `[factor_trigger: suidai_zhengma AND zuye_chengji]` `[role: 总结]` 当年有机会骑马承财，承接或放大既有资源。 → 《三命通会》卷六#岁带正马"""
    normalized_text_zh: str = """"""
    subject: str = "岁带正马与祖业承继"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_30', 'bazi_semantic', 'bazi_structure_year_pillar_zhengcai_combo', 'bazi_semantic', 'bazi_state_month_command_degree_1', 'bazi_semantic', 'bazi_state_degree_17', 'bazi_semantic', 'bazi_condition_factor_182', 'bazi_semantic', 'bazi_condition_bijian_1', 'bazi_semantic', 'source_ref', 'rel_smth_06_106', 'suidai_zhengma_presence', 'rel_smth_06_107', 'yueling_caidi', 'rel_smth_06_108', 'xingchong_fenduo_risk', 'evi_smth_06_106', 'suidai_zhengma_presence', 'rule_suidai', 'evi_smth_06_107', 'yueling_caidi', 'rule_yueling', 'evi_smth_06_108', 'bijian_shangjie_risk', 'rule_pinkun', 'map_smth_06_071', 'map_smth_06_072']
    
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
        l1_anchor="smth_v1.0.0_岁带正马与祖业承继_001_L1",
    )
    version: str = "1.0.0"
