"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157671
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
    semantic_id="smth_v1.0.0_六丁日庚戌时断_财星入库与冲开发财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日庚戌时断财星入库与冲开发财(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日庚戌时断。

  六丁日生时庚戌，财星入库待冲逢；若逢辰字冲开库，定主财源广进通。丁日庚戌时，财星入库，庚金正财入戌库，若生辰月，辰戌相冲，冲开财库，...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日庚戌时断。

  六丁日生时庚戌，财星入库待冲逢；若逢辰字冲开库，定主财源广进通。丁日庚戌时，财星入库，庚金正财入戌库，若生辰月，辰戌相冲，冲开财库，大发财。辰戌丑未月，杂气财官，大贵。

  丁丑日庚戌时，春身旺，贵。夏平，秋富，冬吉。辰戌丑未年月，大贵。

  丁卯日庚戌时，卯戌合，春身旺，贵。秋财旺，行南运，富。

  丁巳日庚戌时，贵。寅午戌月，身旺，大贵。辰月冲库，大发。

  丁未日庚戌时，未戌刑，刑伤妻子。春身旺，贵。秋财旺，富。

  丁酉日庚戌时，酉戌暗合，春身旺，贵。秋财旺，富。

  丁亥日庚戌时，亥卯未月，印旺，大贵。辰月冲库，贵显。

  丁日庚戌时上逢，财星入库待冲逢；运行辰字冲开库，定主财源广进通。丁日庚戌时准，财星入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **财星入库**：庚金正财入戌库，财源有储藏。
  - **冲开发财**：辰冲戌，冲开财库，财源涌出。
  - **杂气财官**：辰戌丑未为杂气之地，财官藏于其中。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，庚戌时」：

  - 庚金正财入戌库，财源有储藏；若生辰月或柱有辰字，辰戌相冲，冲开财库，大发财；
  - 不冲则财源储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Geng-Xu Hour":

  - Geng Metal Direct Wealth enters Xu treasury; if born in Chen month or chart has Chen, Chen-Xu clash opens wealth treasury leading to great riches.
  - Without clash, wealth remains stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「财星入库」为核心，需冲开方能发用。
  - 冲开则财源广进，不冲则平常。
  - 杂气月生者更能发挥财库的价值。

- 详细解说：

  1. **财星入库的特点**  
     - 戌为金库，庚金正财入库有储藏；  
     - 需要辰冲或行运冲开，方能发挥。

  2. **冲开的重要性**  
     - 辰冲戌，冲开财库，财源涌出；  
     - 主财源广进、大发利市。

- 校勘与字词辨析：

  - 「财源广进通」形容财源广阔、畅通无阻。
  - 「发荣昌」形容发达兴旺。
  - **English**：
    - Describes prospering and flourishing.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_185]` `[trigger: 财星入库]` `[factor_trigger: caixing_ruku AND dai_chong_feng]` `[role: 主干]` 六丁日生时庚戌，财星入库待冲逢。 → 《三命通会》卷八#六丁日庚戌时
  - `[ns_smth_08_186]` `[trigger: 辰字冲库]` `[factor_trigger: chenzi_chongku AND caiyuan_guang]` `[role: 主干依赖]` 若逢辰字冲开库，定主财源广进通。 → 《三命通会》卷八#六丁日庚戌时
  - `[ns_smth_08_187]` `[trigger: 杂气财官]` `[factor_trigger: zaqi_caiguan AND da_gui]` `[role: 条件分支]` 辰戌丑未月，杂气财官，大贵。 → 《三命通会》卷八#六丁日庚戌时
  - `[ns_smth_08_188]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六丁日庚戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日庚戌时断：财星入库与冲开发财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_214', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'bazi_state_factor_215', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_139', 'caixing_ruku', 'rel_smth_08_140', 'chongkai_facai', 'rel_smth_08_141', 'youchong_youfa', 'evi_smth_08_139', 'caixing_ruku', 'rule_cairuku', 'evi_smth_08_140', 'chongkai_facai', 'rule_chongkai4', 'evi_smth_08_141', 'zaqi_caiguan', 'rule_zaqi2', 'map_smth_08_093', 'map_smth_08_094']
    
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
        l1_anchor="smth_v1.0.0_六丁日庚戌时断_财星入库与冲开发财_001_L1",
    )
    version: str = "1.0.0"
