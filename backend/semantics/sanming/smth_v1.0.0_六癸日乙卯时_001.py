"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339643
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
    semantic_id="smth_v1.0.0_六癸日乙卯时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日乙卯时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生乙卯时，长生之地遇食神。众无午酉兼辛巳，福寿双全禄位人。
  癸日乙卯时，食神干旺。癸以乙为学堂食神，卯上癸水长生，乙坐禄，柱中无己破辛夺，午酉刑冲，...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生乙卯时，长生之地遇食神。众无午酉兼辛巳，福寿双全禄位人。
  癸日乙卯时，食神干旺。癸以乙为学堂食神，卯上癸水长生，乙坐禄，柱中无己破辛夺，午酉刑冲，通月气，有倚托，主聪明有寿，居官食禄；若有己土，不贵。春月生，北运，显达。

- 分字分词释义：
  - **长生之地**：癸水长生在卯。
  - **食神干旺**：乙木食神透干，坐卯禄地，极旺。
  - **辛夺**：辛金（枭）夺食（乙）。
  - **己破**：己土（煞）破格（食神制煞？此处指己土混杂，或贪合）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于乙卯时，癸水长生在卯，乙木食神得禄，食神生旺。若柱中无己土七煞、辛金枭神、午酉刑冲，且通月气有倚托，主聪明长寿，富贵。若有己土，则减福。春月生（木旺），行北方水运（帮身），显达。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Yi-Mao Hour":

  - Long Life place encountering Eating God—Gui Water Long Life at Mao; Yi Wood Eating God at Mao is at Prosperity position.
  - If no Wu-You together with Xin-Si (Killing-clash-Owl), fortune-longevity complete Salary-position person.
  - If no Ji breaking Xin seizing, Wu-You punishing-clashing, connecting monthly qi with support, intelligent with longevity, holding office eating salary.
  - Key: Pure Eating God pattern fears Owl seizing and Killing breaking; spring birth north luck prominent.

- 核心要点：
  - **食神格**：乙卯纯食。
  - **长生**：身坐长生。
  - **忌枭煞**：忌辛己。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_205]` `[trigger: 长生食神]` `[factor_trigger: changsheng_shishen AND yu_shishen]` `[role: 主干]` 六癸日生乙卯时，长生之地遇食神。 → 《三命通会》卷九#六癸日乙卯时
  - `[ns_smth_09_206]` `[trigger: 无午酉辛巳]` `[factor_trigger: wu_wuyou_xinsi AND fushou_shuangquan]` `[role: 主干依赖]` 众无午酉兼辛巳，福寿双全禄位人。 → 《三命通会》卷九#六癸日乙卯时
  - `[ns_smth_09_207]` `[trigger: 食神干旺]` `[factor_trigger: shishen_ganwang AND congming_youshou]` `[role: 条件分支]` 食神干旺，癸以乙为学堂食神，卯上癸水长生，乙坐禄，主聪明有寿。 → 《三命通会》卷九#六癸日乙卯时
  - `[ns_smth_09_208]` `[trigger: 春月北运]` `[factor_trigger: chunyue_beiyun AND xianda]` `[role: 总结]` 若有己土，不贵。春月生，北运，显达。 → 《三命通会》卷九#六癸日乙卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日乙卯时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_shishen_8', 'bazi_semantic', 'bazi_state_factor_277', 'bazi_semantic', 'bazi_state_factor_313', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_ji_xin_wu_you', 'bazi_semantic', 'source_ref', 'rel_smth_09_154', 'shishen_ganwang', 'rel_smth_09_155', 'wu_ji_xin_wu_you', 'rel_smth_09_156', 'xin_duoshi', 'evi_smth_09_154', 'changsheng_zhidi', 'rule_changsheng_shishen1', 'evi_smth_09_155', 'fushou_shuangquan', 'rule_fushou_shuangquan1', 'evi_smth_09_156', 'jianfu_bugui', 'rule_jitu_poge1', 'map_smth_09_103', 'map_smth_09_104']
    
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
        l1_anchor="smth_v1.0.0_六癸日乙卯时_001_L1",
    )
    version: str = "1.0.0"
