"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339753
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
    semantic_id="smth_v1.0.0_六壬日癸卯时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日癸卯时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时癸卯，引归死地势难安。劫财煞刃见伤鬼，倚托若无常命看。
  壬日癸卯时，身死刃生。壬以癸为刃，卯为暗乙，而伤官鬼。卯上癸生乙旺壬死，不通身旺月气，无...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时癸卯，引归死地势难安。劫财煞刃见伤鬼，倚托若无常命看。
  壬日癸卯时，身死刃生。壬以癸为刃，卯为暗乙，而伤官鬼。卯上癸生乙旺壬死，不通身旺月气，无救助及倚托者，夭贱。巳酉丑月，印旺无化者，性僻孤高虚诈，通身旺，见金气，行才运，贵。伤官伤尽，行南运，亦贵。

- 分字分词释义：
  - **身死刃生**：壬在卯为死地，癸（刃）在卯为长生。
  - **伤官鬼**：卯中乙木为伤官，伤官克官，故名伤官鬼（或指伤官为日主之泄气之鬼）。
  - **印旺无化**：印重身强，无财克印，或无食伤泄秀。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于癸卯时，日主入死地，羊刃癸水得长生，卯木伤官泄气。身弱泄重。若不通身旺月气，无印比救助，主夭贱。若生于巳酉丑金月，印旺生身，若无化解（无财坏印或食伤泄秀），性情孤高虚诈。若身旺见金，行财运，或伤官伤尽行火运，主贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Gui-Mao Hour":

  - Guide returning dead ground momentum difficult stabilize—Ren in Mao is Dead stage; Gui (Blade) in Mao is Long Life.
  - Robbing-Wealth Killing Blade sees Wounded Ghost; without support ordinary fate to see.
  - Body dead Blade born; Mao above Gui born Yi prosperous Ren dead; not connecting body prosperous monthly qi, no rescue or support, early death humble.
  - Key: Body weak draining heavy needs Seal-Parallel rescue; Wounded Officer wounded exhausted traveling South luck also noble.

- 核心要点：
  - **伤官羊刃**：癸水生乙木。
  - **身死**：壬死于卯。
  - **喜身旺**：忌身弱泄重。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_157]` `[trigger: 引归死地]` `[factor_trigger: yingui_sidi AND shi_nan_an]` `[role: 主干]` 六壬日生时癸卯，引归死地势难安。 → 《三命通会》卷九#六壬日癸卯时
  - `[ns_smth_09_158]` `[trigger: 劫财煞刃]` `[factor_trigger: jiecai_sharen AND shang_gui]` `[role: 主干依赖]` 劫财煞刃见伤鬼，倚托若无常命看。 → 《三命通会》卷九#六壬日癸卯时
  - `[ns_smth_09_159]` `[trigger: 身死刃生]` `[factor_trigger: shensi_rensheng AND siyou_chou_yue]` `[role: 条件分支]` 身死刃生，巳酉丑月，印旺无化者，性僻孤高虚诈。 → 《三命通会》卷九#六壬日癸卯时
  - `[ns_smth_09_160]` `[trigger: 通身旺贵]` `[factor_trigger: tong_shenwang_gui AND xing_nan_yun]` `[role: 总结]` 通身旺，见金气，行才运，贵。伤官伤尽，行南运，亦贵。 → 《三命通会》卷九#六壬日癸卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日癸卯时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_332', 'bazi_semantic', 'bazi_relation_shangguan_13', 'bazi_semantic', 'bazi_state_factor_333', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_metal_5', 'bazi_semantic', 'source_ref', 'rel_smth_09_118', 'shensi_ren_sheng', 'rel_smth_09_119', 'shensi_ren_sheng', 'rel_smth_09_120', 'tong_shenwang_yue_jianjin', 'evi_smth_09_118', 'shensi_ren_sheng', 'rule_shensi_ren_sheng1', 'evi_smth_09_119', 'yaojian', 'rule_yaojian_ren_ji1', 'evi_smth_09_120', 'tong_shenwang_yue_jianjin', 'rule_tong_shenwang_yue_jianjin1', 'map_smth_09_079', 'map_smth_09_080']
    
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
        l1_anchor="smth_v1.0.0_六壬日癸卯时_001_L1",
    )
    version: str = "1.0.0"
