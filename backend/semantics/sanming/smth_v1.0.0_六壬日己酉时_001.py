"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339806
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
    semantic_id="smth_v1.0.0_六壬日己酉时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日己酉时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时己酉，明官暗印有扶持。月通身旺人清贵，犹恐恋花贪酒色。
  壬日己酉时，败处逢生。壬水酉上沐浴，辛为生气印绶，酉上辛金旺，用己为官，酉上有明己，若通...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时己酉，明官暗印有扶持。月通身旺人清贵，犹恐恋花贪酒色。
  壬日己酉时，败处逢生。壬水酉上沐浴，辛为生气印绶，酉上辛金旺，用己为官，酉上有明己，若通月气有倚托，行财官运，贵，反是，平常。但犯桃花坐命，风流人物，恋花贪酒。

- 分字分词释义：
  - **败处逢生**：酉为壬水沐浴（败地），但酉中辛金印绶生身。
  - **明官暗印**：己土官星透干（明官），酉中辛金印绶暗藏（暗印）。
  - **桃花坐命**：酉为壬水沐浴桃花（咸池）。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于己酉时，壬水在酉沐浴（败地），但得辛金正印生助。己土正官透出。若通月气且有倚托（身旺），行财官运，主清贵。但因沐浴桃花在时，恐风流好色，恋花贪酒。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Ji-You Hour":

  - Bright Official dark Seal has support—Ji Earth Proper Official reveals; You hides Xin Metal Direct Seal.
  - Month connecting body prosperous person pure-noble; still fear love-flower greedy wine-color.
  - Defeat place meets life; Ren Water in You Bath stage; Xin Metal Seal prosperous; if connecting monthly qi with support, traveling Wealth-Official luck, noble.
  - Key: Official-Seal mutual generation pattern; Bath Peach Blossom indicates romantic character.

- 核心要点：
  - **官印相生**：己土生酉金，酉金生壬水。
  - **沐浴桃花**：主风流。
  - **喜身旺**：败地需扶。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_181]` `[trigger: 明官暗印]` `[factor_trigger: mingguan_anyin AND you_fuchi]` `[role: 主干]` 六壬日生时己酉，明官暗印有扶持。 → 《三命通会》卷九#六壬日己酉时
  - `[ns_smth_09_182]` `[trigger: 月通身旺]` `[factor_trigger: yuetong_shenwang AND ren_qinggui]` `[role: 主干依赖]` 月通身旺人清贵，犹恐恋花贪酒色。 → 《三命通会》卷九#六壬日己酉时
  - `[ns_smth_09_183]` `[trigger: 败处逢生]` `[factor_trigger: baichu_fengsheng AND xin_yinwang]` `[role: 条件分支]` 败处逢生，酉上辛金旺，用己为官。 → 《三命通会》卷九#六壬日己酉时
  - `[ns_smth_09_184]` `[trigger: 桃花坐命]` `[factor_trigger: taohua_zuoming AND fengliu_renwu]` `[role: 总结]` 但犯桃花坐命，风流人物，恋花贪酒。 → 《三命通会》卷九#六壬日己酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日己酉时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_342', 'bazi_semantic', 'bazi_relation_factor_136', 'bazi_semantic', 'bazi_state_taohua', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_133', 'bazi_semantic', 'source_ref', 'rel_smth_09_136', 'guanyin_xiangsheng', 'rel_smth_09_137', 'guanyin_xiangsheng', 'rel_smth_09_138', 'taohua_fengliu', 'evi_smth_09_136', 'guanyin_xiangsheng', 'rule_guanyin_xiangsheng_jiyou1', 'evi_smth_09_137', 'qinggui', 'rule_shenwang_qinggui1', 'evi_smth_09_138', 'lianhua_tanjiu', 'rule_taohua_fengliu1', 'map_smth_09_091', 'map_smth_09_092']
    
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
        l1_anchor="smth_v1.0.0_六壬日己酉时_001_L1",
    )
    version: str = "1.0.0"
