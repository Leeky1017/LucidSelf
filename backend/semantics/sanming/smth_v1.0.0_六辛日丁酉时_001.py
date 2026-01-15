"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339591
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
    semantic_id="smth_v1.0.0_六辛日丁酉时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日丁酉时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时丁酉，鬼破禄无祸百端。倚托身强方断吉，月通制伏是偏官。
  辛日丁酉时，火金持争。辛金酉上健旺，见丁为正鬼；酉上丁长生，破禄，不成其福，反复成败。身...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时丁酉，鬼破禄无祸百端。倚托身强方断吉，月通制伏是偏官。
  辛日丁酉时，火金持争。辛金酉上健旺，见丁为正鬼；酉上丁长生，破禄，不成其福，反复成败。身强通月气有制伏者，作偏官论；更行身旺运，贵。通金气无丁，身强，行南运，大贵。

- 分字分词释义：
  - **鬼破禄**：丁火（七煞/鬼）在酉长生，酉为辛金禄地，丁火克禄，故名鬼破禄。
  - **制伏**：食神制煞。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于丁酉时，丁火七煞透出，坐酉长生有力，克制日禄（酉），主反复成败，祸患百端。若日主身强，且月令有制伏（食伤），可作偏官格论，主贵。若无丁火透出，身强行南运（官煞），亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Ding-You Hour":

  - Ghost breaks Salary without, disasters hundred-fold—Ding Fire Seven-Killing at You is at Long Life position, attacking Xin's Salary (You).
  - With support body strong then judge auspicious; if month connects control-subdue, treat as Partial Official.
  - Fire-Metal hold struggle; Xin Metal healthy at You but Ding attacks Salary, reversals and failures; body strong with control, as Partial Official theory.
  - Key: Killing breaks Salary needs control (Eating God); body strong traveling South luck, great nobility.

- 核心要点：
  - **煞克禄**：丁克酉，忌。
  - **建禄**：辛禄在酉。
  - **制煞**：喜水制火。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_133]` `[trigger: 鬼破禄]` `[factor_trigger: guipo_lu AND huo_baidan]` `[role: 主干]` 六辛日生时丁酉，鬼破禄无祸百端。 → 《三命通会》卷九#六辛日丁酉时
  - `[ns_smth_09_134]` `[trigger: 身强方吉]` `[factor_trigger: shenqiang_fangji AND zhi_fu_pianguan]` `[role: 主干依赖]` 倚托身强方断吉，月通制伏是偏官。 → 《三命通会》卷九#六辛日丁酉时
  - `[ns_smth_09_135]` `[trigger: 火金持争]` `[factor_trigger: huojin_chizheng AND fanfu_chengbai]` `[role: 条件分支]` 火金持争，酉上丁长生，破禄，反复成败。 → 《三命通会》卷九#六辛日丁酉时
  - `[ns_smth_09_136]` `[trigger: 身旺行南运]` `[factor_trigger: shenwang_xing_nanyun AND dagui]` `[role: 总结]` 通金气无丁，身强，行南运，大贵。 → 《三命通会》卷九#六辛日丁酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日丁酉时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_301', 'bazi_semantic', 'bazi_relation_fire_metal_1', 'bazi_semantic', 'bazi_state_factor_302', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_129', 'bazi_semantic', 'source_ref', 'rel_smth_09_100', 'guipo_lu', 'rel_smth_09_101', 'guipo_lu', 'rel_smth_09_102', 'shenqiang_youzhi_fu', 'evi_smth_09_100', 'guipo_lu', 'rule_guipo_lu1', 'evi_smth_09_101', 'shenqiang_youzhi_fu', 'rule_shenqiang_youzhi_fu1', 'evi_smth_09_102', 'pianguan_ge', 'rule_pianguan_ge1', 'map_smth_09_067', 'map_smth_09_068']
    
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
        l1_anchor="smth_v1.0.0_六辛日丁酉时_001_L1",
    )
    version: str = "1.0.0"
