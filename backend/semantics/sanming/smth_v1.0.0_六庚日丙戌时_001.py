"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339487
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
    semantic_id="smth_v1.0.0_六庚日丙戌时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日丙戌时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时丙戌，金火持争事不详。身旺月通印绶吉，不通无救祸难当。
  庚日丙戌时，金火持争。庚以丙为鬼，丙火、戊土合局，金无气。若通身旺印，卯月有救助者，贵；...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时丙戌，金火持争事不详。身旺月通印绶吉，不通无救祸难当。
  庚日丙戌时，金火持争。庚以丙为鬼，丙火、戊土合局，金无气。若通身旺印，卯月有救助者，贵；反是平常或夭贱。运通亦吉。庚属大肠，若丙丁旺甚，主痔漏、脏毒、脓血之灾。

- 分字分词释义：
  - **金火持争**：戌为火库，丙火透干，火旺克金。
  - **事不详**：吉凶难测，多主不吉。
  - **丙戊合局**：戌中藏戊、丁、辛。丙火生戊土，火土相生（或指寅午戌合火）。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于丙戌时，丙火七煞透出，坐戌火库，火旺攻身。若日主身旺，或月通印绶（土），化煞生身，主吉。若身弱无救，七煞攻身，主灾祸。庚属大肠，火克金，防痔漏脓血之疾。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Bing-Xu Hour":

  - Metal-Fire hold struggle, matters unclear—Bing Fire Seven-Killing sits on Xu Fire treasury attacking Geng.
  - If body prosperous month connects Seal auspicious; without connection no rescue disaster difficult to bear.
  - If body weak without rescue, killing attacks body bringing disasters; Geng rules large intestine, excessive Fire indicates hemorrhoids, viscera poison, pus-blood calamities.
  - Key: Killing-Seal mutual generation transforms killing; strong body handles killing, weak body receives disaster.

- 核心要点：
  - **时上七煞**：丙火坐库，煞旺。
  - **煞印相生**：戌中戊土印绶化煞。
  - **身旺为贵**：身弱畏煞。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_089]` `[trigger: 金火持争]` `[factor_trigger: jinhuo_chizheng AND shi_buxiang]` `[role: 主干]` 六庚日生时丙戌，金火持争事不详。 → 《三命通会》卷九#六庚日丙戌时
  - `[ns_smth_09_090]` `[trigger: 身旺印绶吉]` `[factor_trigger: shenwang_yinshou_ji AND butong_huo_nandang]` `[role: 主干依赖]` 身旺月通印绶吉，不通无救祸难当。 → 《三命通会》卷九#六庚日丙戌时
  - `[ns_smth_09_091]` `[trigger: 通身旺印月]` `[factor_trigger: tong_shenwang_yinyue AND gui]` `[role: 条件分支]` 若通身旺印，卯月有救助者，贵。 → 《三命通会》卷九#六庚日丙戌时
  - `[ns_smth_09_092]` `[trigger: 痔漏脏毒]` `[factor_trigger: zhilou_zangdu AND bingren_shenbing]` `[role: 总结]` 庚属大肠，若丙丁旺甚，主痔漏、脏毒、脓血之灾。 → 《三命通会》卷九#六庚日丙戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日丙戌时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_metal_fire_3', 'bazi_semantic', 'bazi_relation_factor_121', 'bazi_semantic', 'bazi_state_factor_284', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_factor_125', 'bazi_semantic', 'source_ref', 'rel_smth_09_067', 'jinhua_chizheng', 'rel_smth_09_068', 'jinhua_chizheng', 'rel_smth_09_069', 'tong_shenwang_yinyue', 'evi_smth_09_067', 'jinhua_chizheng', 'rule_jinhua_chizheng1', 'evi_smth_09_068', 'tong_shenwang_yinyue', 'rule_shenwang_yinyue1', 'evi_smth_09_069', 'jinhua_chizheng', 'rule_wu_yin_wujiu1', 'map_smth_09_045', 'map_smth_09_046']
    
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
        l1_anchor="smth_v1.0.0_六庚日丙戌时_001_L1",
    )
    version: str = "1.0.0"
