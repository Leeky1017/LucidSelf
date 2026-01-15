"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339347
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
    semantic_id="smth_v1.0.0_六己日戊辰时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日戊辰时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时戊辰，财库专官又助身。无破有制财官旺，富贵声扬显赫人。
  己日戊辰时，财库专官。己用甲为官，丙为印，寅上甲旺丙生。如果无破，通月气，身旺，贵；不通...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时戊辰，财库专官又助身。无破有制财官旺，富贵声扬显赫人。
  己日戊辰时，财库专官。己用甲为官，丙为印，寅上甲旺丙生。如果无破，通月气，身旺，贵；不通，只是富。忌见甲己，化土为暗鬼；申冲寅，无倚落魄。
  己日戊辰时，财库专官。己以壬癸为财，辰上入墓；甲为官，辰中专位。更有戊土助身。若通月气，身旺，财官有气，富贵；不通，只是平常，冬月，财旺，亦贵。

- 分字分词释义：
  - **财库**：辰为水库（壬癸水之墓库），水为己土之财，故辰为财库。
  - **专官**：原文称“甲为官，辰中专位”恐有误，辰中藏乙木（余气）、癸水（墓气）、戊土（本气），无甲木。可能指“辰中乙木七煞”或“辰合酉化金制煞”等，或“辰为甲木衰地”。古注“专位”一词多指临官帝旺，甲禄在寅，非辰。此处存疑，或指辰土能培木养官。另一解释：辰为湿土，能生金（食伤）生财，财旺自能生官。
  - **助身**：戊土透干劫财帮身，辰土比劫帮身。

- **规范化释义（primary_lang_explained）**：
  六己日出生于戊辰时，辰为财库，且戊土透出助身。若日主通月气身旺，且财官有气（如生于水木旺月），主富贵显赫。若不通月气，则为平常之命。若生于冬月水旺（财旺），亦可富贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Wu-Chen Hour":

  - Chen is Wealth treasury (Water tomb); Wu Earth Rob Wealth reveals aiding Day Master.
  - If passing monthly qi with strong body and prosperous wealth-official, indicates prominent nobility and fame.
  - Without monthly qi, ordinary fate; if born in winter with prosperous wealth, can still achieve riches.
  - Key: Rob Wealth helps body; Wealth treasury stores riches; body-wealth balance is essential.

- 核心要点：
  - **比劫帮身**：戊辰时，土旺帮身，身强能任财官。
  - **财库**：辰为财库，主富。
  - **官星**：辰虽非官星旺地，但湿土养木，利于官星生长。

- 详细解说：
  此格重在“身财两停”。己土卑湿，喜戊土帮扶（筑堤拦水）。戊辰时，身强财亦有库，基础稳固。若局中再见甲乙木（官煞）或壬癸水（财），则财官双美。辰戌丑未月生人，土气过重，宜见木疏土；亥子月生人，财旺，喜火土帮身。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_017]` `[trigger: 财库专官]` `[factor_trigger: caiku_zhuanguan AND zhu_shen]` `[role: 主干]` 六己日生时戊辰，财库专官又助身。 → 《三命通会》卷九#六己日戊辰时
  - `[ns_smth_09_018]` `[trigger: 无破有制]` `[factor_trigger: wupo_youzhi AND caiguan_wang]` `[role: 主干依赖]` 无破有制财官旺，富贵声扬显赫人。 → 《三命通会》卷九#六己日戊辰时
  - `[ns_smth_09_019]` `[trigger: 通月财官]` `[factor_trigger: tongyue_caiguan AND fugui]` `[role: 条件分支]` 若通月气，身旺，财官有气，富贵。 → 《三命通会》卷九#六己日戊辰时
  - `[ns_smth_09_020]` `[trigger: 不通平常]` `[factor_trigger: butong_pingchang AND dongyue_gui]` `[role: 总结]` 不通，只是平常，冬月，财旺，亦贵。 → 《三命通会》卷九#六己日戊辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日戊辰时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_280', 'bazi_semantic', 'bazi_relation_factor_111', 'bazi_semantic', 'bazi_state_factor_259', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_120', 'bazi_semantic', 'source_ref', 'rel_smth_09_013', 'caiku', 'rel_smth_09_014', 'shenwang_tongyueqi', 'rel_smth_09_015', 'shencai_liangting', 'evi_smth_09_013', 'caiku', 'rule_caiku_zhushen1', 'evi_smth_09_014', 'shenwang_tongyueqi', 'rule_wupo_youzhi1', 'evi_smth_09_015', 'shencai_liangting', 'rule_fugui_shengyang1', 'map_smth_09_009', 'map_smth_09_010']
    
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
        l1_anchor="smth_v1.0.0_六己日戊辰时_001_L1",
    )
    version: str = "1.0.0"
