"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339772
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
    semantic_id="smth_v1.0.0_六壬日乙巳时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日乙巳时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时乙巳，身绝有财不聚财。进神暗鬼来相克，透己相刑是祸胎。
  壬日乙巳时，财旺身绝。壬用丙为财，戊为鬼，庚为倒食。巳上有乙木为伤官，丙戊健旺，庚金长生...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时乙巳，身绝有财不聚财。进神暗鬼来相克，透己相刑是祸胎。
  壬日乙巳时，财旺身绝。壬用丙为财，戊为鬼，庚为倒食。巳上有乙木为伤官，丙戊健旺，庚金长生，壬水气绝，柱有己官，祸患百端，傲物夸高。若不通身旺月无救助者，贫；有倚托，通旺，或行身旺运，皆吉。

- 分字分词释义：
  - **身绝**：壬水在巳为绝地。
  - **财旺**：巳中丙火（财）临官，戊土（煞）临官。
  - **进神**：古法神煞，甲子、甲午、己卯、己酉等为进神。此处乙巳非进神。可能指“乙木伤官生财，财生煞，煞攻身”的递进关系。或指乙木为进气之木？
  - **暗鬼**：巳中戊土七煞。
  - **透己相刑**：若天干透己土（官），官煞混杂，且伤官见官，主祸。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于乙巳时，巳中财官煞皆旺，日主壬水绝地。乙木伤官生财，财生煞，克身重。若天干再透己土正官，混杂且受乙木克，祸患百端，性格傲慢。若日主不通月气，身弱无助，主贫。若身旺有倚托，或行身旺运，可任财官，吉。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Yi-Si Hour":

  - Body extinct has Wealth not gather Wealth—Ren Water in Si is Extinct stage; Si contains Bing-Wu (Wealth-Killing) both prosperous.
  - Advance-spirit dark ghost comes mutually attacking; revealing Ji mutual punishment is disaster embryo.
  - Wealth prosperous body extinct; Yi Wood Wounded Officer generates Wealth generates Killing; if pillars have Ji Official, disasters hundred-fold, arrogant boastful.
  - Key: Body weak needs support; not connecting body prosperous month, poor; with support traveling body prosperous luck, auspicious.

- 核心要点：
  - **伤官生财**：乙生丙。
  - **财生煞**：丙生戊。
  - **身绝**：壬绝于巳。
  - **喜身旺**：身弱从杀或贫。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_165]` `[trigger: 身绝有财]` `[factor_trigger: shenjue_youcai AND bu_jucai]` `[role: 主干]` 六壬日生时乙巳，身绝有财不聚财。 → 《三命通会》卷九#六壬日乙巳时
  - `[ns_smth_09_166]` `[trigger: 进神暗鬼]` `[factor_trigger: jinshen_angui AND xiang_ke]` `[role: 主干依赖]` 进神暗鬼来相克，透己相刑是祸胎。 → 《三命通会》卷九#六壬日乙巳时
  - `[ns_smth_09_167]` `[trigger: 财旺身绝]` `[factor_trigger: caiwang_shenjue AND awu_kuagao]` `[role: 条件分支]` 财旺身绝，柱有己官，祸患百端，傲物夸高。 → 《三命通会》卷九#六壬日乙巳时
  - `[ns_smth_09_168]` `[trigger: 有倚托吉]` `[factor_trigger: you_yituo_ji AND tongwang_xingyun]` `[role: 总结]` 若不通身旺月无救助者，贫；有倚托，通旺，或行身旺运，皆吉。 → 《三命通会》卷九#六壬日乙巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日乙巳时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_335', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'bazi_state_factor_336', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_132', 'bazi_semantic', 'source_ref', 'rel_smth_09_124', 'caiwang_shenjue', 'rel_smth_09_125', 'caiwang_shenjue', 'rel_smth_09_126', 'tong_shenwangyue_youtuo', 'evi_smth_09_124', 'caiwang_shenjue', 'rule_caiwang_shenjue1', 'evi_smth_09_125', 'huohuan_baiduan', 'rule_jinshen_angui_touji1', 'evi_smth_09_126', 'tong_shenwangyue_youtuo', 'rule_tong_shenwangyue_youtuo1', 'map_smth_09_083', 'map_smth_09_084']
    
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
        l1_anchor="smth_v1.0.0_六壬日乙巳时_001_L1",
    )
    version: str = "1.0.0"
