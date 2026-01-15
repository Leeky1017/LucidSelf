"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339736
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
    semantic_id="smth_v1.0.0_六壬日辛丑时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日辛丑时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时辛丑，下有官星上印绶。如通月气运西南，官印扶身人清秀。
  壬日辛丑时，官印得位。壬以己为官，辛为印，丑上金局，暗己得位，若通月气，为人清秀，禄贵安...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时辛丑，下有官星上印绶。如通月气运西南，官印扶身人清秀。
  壬日辛丑时，官印得位。壬以己为官，辛为印，丑上金局，暗己得位，若通月气，为人清秀，禄贵安稳；不通，主性僻诡谲。

- 分字分词释义：
  - **官印得位**：辛金印绶透干，丑中藏己土（官）、辛金（印）、癸水（劫）。丑为金库，印星有力。己土在丑为墓地，但也是旺地（土旺四季）。
  - **清秀**：官印相生，金白水清。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于辛丑时，辛金正印透出，丑中己土正官暗藏。官印相生，扶助日主。若通月气（身旺或官印旺），且行西南（火土金）运，主为人清秀，福禄安稳。若不通月气，身弱或官印无力，主性情怪僻诡谲。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Xin-Chou Hour":

  - Below has Official star above Seal—Xin Metal Direct Seal reveals; Chou hides Ji Earth (Official), Xin Metal (Seal).
  - If connecting monthly qi luck Southwest, Official-Seal support body person elegant refined.
  - Official-Seal gain position; if connecting monthly qi, person elegant refined, Salary-nobility stable; not connecting, rules nature eccentric deceitful.
  - Key: Official-Seal mutual generation pattern; requires monthly qi connection; Southwest luck (Fire-Earth-Metal) favorable.

- 核心要点：
  - **官印格**：辛透己藏。
  - **杂气财官**：丑中财官印。
  - **身旺**：喜身旺。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_149]` `[trigger: 下官上印]` `[factor_trigger: xiaguan_shangyin AND chou_yinku]` `[role: 主干]` 六壬日生时辛丑，下有官星上印纶。 → 《三命通会》卷九#六壬日辛丑时
  - `[ns_smth_09_150]` `[trigger: 通月气西南]` `[factor_trigger: tong_yueqi_xinan AND guanyin_fushen]` `[role: 主干依赖]` 如通月气运西南，官印扶身人清秀。 → 《三命通会》卷九#六壬日辛丑时
  - `[ns_smth_09_151]` `[trigger: 官印得位]` `[factor_trigger: guanyin_dewei AND qingxiu_lugui]` `[role: 条件分支]` 官印得位，若通月气，为人清秀，禄贵安稳。 → 《三命通会》卷九#六壬日辛丑时
  - `[ns_smth_09_152]` `[trigger: 不通性僻]` `[factor_trigger: butong_xingpi AND guijue]` `[role: 总结]` 不通，主性僻诡谲。 → 《三命通会》卷九#六壬日辛丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日辛丑时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_factor_329', 'bazi_semantic', 'bazi_state_factor_342', 'bazi_semantic', 'bazi_state_factor_330', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_factor_131', 'bazi_semantic', 'source_ref', 'rel_smth_09_112', 'guanyin_dewei', 'rel_smth_09_113', 'guanyin_dewei', 'rel_smth_09_114', 'tong_yueqi_xinan_yun', 'evi_smth_09_112', 'guanyin_dewei', 'rule_guanyin_dewei1', 'evi_smth_09_113', 'tong_yueqi_xinan_yun', 'rule_tong_yueqi_xinan_yun1', 'evi_smth_09_114', 'xingpi_guijue', 'rule_xingpi_guijue1', 'map_smth_09_075', 'map_smth_09_076']
    
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
        l1_anchor="smth_v1.0.0_六壬日辛丑时_001_L1",
    )
    version: str = "1.0.0"
