"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339273
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
    semantic_id="smth_v1.0.0_六己日甲子时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日甲子时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时甲子，明官暗印有声名。身强官旺宜高贵，破害刑冲又不情。
  己日甲子时，明官暗印。己用甲为官，癸为财，辛为食。子上有明甲暗癸，生辛，己土长生。见甲为...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时甲子，明官暗印有声名。身强官旺宜高贵，破害刑冲又不情。
  己日甲子时，明官暗印。己用甲为官，癸为财，辛为食。子上有明甲暗癸，生辛，己土长生。见甲为明官，癸为暗财，辛为暗食。若身旺、通月气，行木火运，贵。忌见庚辛，伤官七煞，刑冲破害。

- 分字分词释义：
  - **明官暗印**：甲子时，甲木透出为己土正官（明官）；子中癸水生甲木，且癸为己土偏财，子水又是辛金食神长生之地（原文“暗印”恐有误或指代不同，通常子中癸为财，但子为辛金长生，辛能生癸，癸生甲，辗转相生）。另解：子水为印绶之源（水生木，木生火印），或指水为财，财旺生官。古注多有歧义，此处依“明甲暗癸”解。
  - **身强官旺**：日主己土得地得势，甲木官星亦旺。
  - **破害刑冲**：指地支出现午冲子、未穿子、卯刑子等情况，破坏时支子水。

- **规范化释义（primary_lang_explained）**：
  六己日出生于甲子时，甲木透干为正官，子水藏癸为偏财，财官相生，有名声。若己土日主身强，且官星得令旺相，主高贵。但若地支见刑冲破害（如午冲子），则官星根基受损，反主无情或吉中藏凶。
  具体而言，己日甲子时，甲木为明官，子中癸水为暗财，子又是辛金食神的长生之地（辛金能生财）。若日主身旺，通月气（如生于四季土月或火月），行木火运助身助官，主大贵。最忌庚辛金透出克甲木（伤官见官），或地支子水受刑冲破害。
  - **English**：
    - Annual fortune (大运) terminology explained; timing indicators treated as influence periods rather than fixed events.


- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Jia-Zi Hour":

  - Jia Wood Direct Official at Zi is revealed; Gui Water Indirect Wealth hidden in Zi branch—forming "revealed official hidden wealth" with mutual generation.
  - If Ji Earth Day Master is strong with Official star in season, indicates high nobility and fame.
  - If branches show punishment-clash-break-harm (like Wu clashing Zi), Official's foundation is damaged—turns auspicious into mixed fortune.
  - Key requirements: strong body passing monthly qi, traveling Wood-Fire luck supporting self and official; taboo Geng-Xin Metal hurting official or Zi branch receiving clashes.

- 核心要点：
  - **时上正官格**：甲己合，甲为正官，坐子水财地，财官双美。
  - **身旺为要**：官星虽好，需日主身强方能胜任；身弱则官重压身。
  - **忌伤官刑冲**：庚辛金克甲，午冲子，皆为破格。

- 详细解说：
  己日甲子时，名为“明官暗印”（或暗财），格局清纯。甲木正官坐子水财地，财来生官，官星有力。子水又是天乙贵人（己鼠猴乡），故带贵气。若己土生于巳午月，印绶生身，或辰戌丑未月，比劫帮身，日主健旺，再行东方木运或南方火运，官印相生，必主富贵。若生于申酉月，伤官食神旺，克制甲木；或生于亥子月，财多身弱，则需火土运帮身。

- 校勘与字词辨析：
  - **“暗印”**：原文“明官暗印”，子中藏癸水，癸为己土偏财，非印。印为丙丁火。此处“暗印”可能指癸水生甲木，甲木能生丙火印绶（辗转相生），或古本传抄之误，实指“暗财”。后文解释“见甲为明官，癸为暗财”，可见实指财。
  - **“辛为食”**：子为辛金长生之地，故云“生辛”。
  - **English**：
    - Annual fortune (大运) terminology explained; timing indicators treated as influence periods rather than fixed events.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_001]` `[trigger: 明官暗印]` `[factor_trigger: mingguan_anyin AND you_shengming]` `[role: 主干]` 六己日生时甲子，明官暗印有声名。 → 《三命通会》卷九#六己日甲子时
  - `[ns_smth_09_002]` `[trigger: 身强官旺]` `[factor_trigger: shenqiang_guanwang AND yi_gaogui]` `[role: 主干依赖]` 身强官旺宜高贵，破害刑冲又不情。 → 《三命通会》卷九#六己日甲子时
  - `[ns_smth_09_003]` `[trigger: 财官相生]` `[factor_trigger: caiguan_xiangsheng AND da_gui]` `[role: 条件分支]` 若身旺、通月气，行木火运，贵。 → 《三命通会》卷九#六己日甲子时
  - `[ns_smth_09_004]` `[trigger: 忌伤官刑冲]` `[factor_trigger: ji_shangguan_xingchong AND poguan]` `[role: 总结]` 忌见庚辛，伤官七煞，刑冲破害。 → 《三命通会》卷九#六己日甲子时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日甲子时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_252', 'bazi_semantic', 'bazi_relation_zhenguan_2', 'bazi_semantic', 'bazi_state_factor_253', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_factor_111', 'bazi_semantic', 'source_ref', 'rel_smth_09_001', 'mingguan_ancai', 'rel_smth_09_002', 'shenwang_tongyueqi', 'rel_smth_09_003', 'pohai_xingchong', 'evi_smth_09_001', 'mingguan_ancai', 'rule_mingguan1', 'evi_smth_09_002', 'shenwang_tongyueqi', 'rule_shenqiang_guanwang', 'evi_smth_09_003', 'pohai_xingchong', 'rule_pohai1', 'map_smth_09_001', 'map_smth_09_002']
    
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
        l1_anchor="smth_v1.0.0_六己日甲子时_001_L1",
    )
    version: str = "1.0.0"
