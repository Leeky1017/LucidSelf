"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339408
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
    semantic_id="smth_v1.0.0_六己日甲戌时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日甲戌时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时甲戌，暗藏官印库中埋。若逢刑破开冲钥，高科及第福自来。
  己日甲戌时，明官暗印。己用甲为官，丁为印。戌上甲木养位，丁火入库。若柱逢刑冲，开库，生旺...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时甲戌，暗藏官印库中埋。若逢刑破开冲钥，高科及第福自来。
  己日甲戌时，明官暗印。己用甲为官，丁为印。戌上甲木养位，丁火入库。若柱逢刑冲，开库，生旺，贵；无刑冲，平常。

- 分字分词释义：
  - **暗藏官印**：戌中藏丁火（印）、戊土（劫）、辛金（食）。官星甲木透干（明官），印星丁火入库（暗印）。
  - **开冲钥**：戌为火库（印库），喜辰冲开，或刑开。

- **规范化释义（primary_lang_explained）**：
  六己日出生于甲戌时，甲木正官透出，丁火印绶藏于戌库。若有刑冲（如辰冲戌）开库，放出印绶，主高科及第（印主文书、功名）。若无刑冲，印星入库不开，则为平常之命。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Jia-Xu Hour":

  - Jia Wood Direct Official reveals; Ding Fire Seal hidden in Xu treasury—"official-seal buried in treasury."
  - If encountering punishment-break-clash to open treasury key, indicates high examination success and fortune arrives naturally.
  - Without clash-punishment, seal remains buried—ordinary fate.
  - Key: Treasury pattern requires opening; clash-punishment becomes key to unlock hidden fortune.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_041]` `[trigger: 暗藏官印]` `[factor_trigger: ancang_guanyin AND ku_zhong_mai]` `[role: 主干]` 六己日生时甲戌，暗藏官印库中埋。 → 《三命通会》卷九#六己日甲戌时
  - `[ns_smth_09_042]` `[trigger: 刑破开冲]` `[factor_trigger: xingpo_kaichong AND gaoke_jidi]` `[role: 主干依赖]` 若逢刑破开冲钥，高科及第福自来。 → 《三命通会》卷九#六己日甲戌时
  - `[ns_smth_09_043]` `[trigger: 库开生旺]` `[factor_trigger: kukai_shengwang AND gui]` `[role: 条件分支]` 若柱逢刑冲，开库，生旺，贵。 → 《三命通会》卷九#六己日甲戌时
  - `[ns_smth_09_044]` `[trigger: 无刑冲平常]` `[factor_trigger: wu_xingchong_pingchang AND yin_mai]` `[role: 总结]` 无刑冲，平常。 → 《三命通会》卷九#六己日甲戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日甲戌时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_266', 'bazi_semantic', 'bazi_relation_factor_114', 'bazi_semantic', 'bazi_state_factor_267', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_factor_119', 'bazi_semantic', 'source_ref', 'rel_smth_09_031', 'guanxing_zuoku', 'rel_smth_09_032', 'kaichong_yao', 'rel_smth_09_033', 'kaichong_yao', 'evi_smth_09_031', 'guanxing_zuoku', 'rule_guanxing_zuoku1', 'evi_smth_09_032', 'kaichong_yao', 'rule_kaichong_yao1', 'evi_smth_09_033', 'gaoke_jidi', 'rule_gaoke_jidi1', 'map_smth_09_021', 'map_smth_09_022']
    
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
        l1_anchor="smth_v1.0.0_六己日甲戌时_001_L1",
    )
    version: str = "1.0.0"
