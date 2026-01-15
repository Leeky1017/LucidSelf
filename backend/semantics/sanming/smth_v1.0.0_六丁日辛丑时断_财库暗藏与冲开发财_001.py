"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157582
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
    semantic_id="smth_v1.0.0_六丁日辛丑时断_财库暗藏与冲开发财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日辛丑时断财库暗藏与冲开发财(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日辛丑时断。

  六丁日生时辛丑，财库星明有暗官；若逢冲破财官旺，不贵即富寿且安。丁日辛丑时，财库暗官，辛金财星入丑库，丑中有癸水暗官。若生未月，丑未...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日辛丑时断。

  六丁日生时辛丑，财库星明有暗官；若逢冲破财官旺，不贵即富寿且安。丁日辛丑时，财库暗官，辛金财星入丑库，丑中有癸水暗官。若生未月，丑未相冲，冲开财库，大发财。辰戌丑未月，杂气财官，大贵。

  丁丑日辛丑时，两丑自刑，伤妻害子。春夏身旺，吉。秋财旺，冬官旺，俱吉。

  丁卯日辛丑时，春身旺，行西北运，贵。秋财旺，行南运，富。子申辰年月，贵显。

  丁巳日辛丑时，贵。丑未月，冲库，大发。卯酉年月，亦吉。

  丁未日辛丑时，丑未相冲，冲开财库，大富。春夏，行西运，贵。秋冬，行南运，亦贵。

  丁酉日辛丑时，巳酉丑月，合财，大富。寅午戌月，身旺用财，大贵。

  丁亥日辛丑时，春夏吉。秋冬，水旺身弱，贫。亥卯未年月，印旺，贵。

  丁日时逢辛丑藏，财官入库待冲扬；运行未字财源广，不贵即富寿延长。丁日辛丑时位，财官暗库相藏。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **财库暗藏**：辛金正财入丑库，财源有储藏。
  - **暗官**：丑中癸水正官暗藏，官星隐秘。
  - **冲开发财**：未冲丑，冲开财库，财源涌出。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，辛丑时」：

  - 辛金正财入丑库，丑中又有癸水暗官，财官皆入库藏；
  - 若生未月或柱有未字，丑未相冲，冲开财库，大发财；
  - 不冲则财官储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Xin-Chou Hour":

  - Xin Metal Direct Wealth enters Chou treasury; Chou also contains hidden Gui Water Official—wealth-official both stored in treasury.
  - If born in Wei month or chart has Wei, Chou-Wei clash opens wealth treasury leading to great riches.
  - Without clash, wealth-official remain stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「财库暗藏」为核心，需冲开方能发用。
  - 冲开则大富大贵，不冲则平常。
  - 歌诀强调：运行未字财源广。

- 详细解说：

  1. **财库暗藏的特点**  
     - 丑为金库，辛金正财入库有储藏；  
     - 丑中癸水暗官，官星隐秘。

  2. **冲开的重要性**  
     - 未冲丑，冲开财库，财官涌出；  
     - 若不冲，则储而不发。

- 校勘与字词辨析：

  - 「待冲扬」形容财库等待冲开后方能发挥。
  - 「寿延长」指此格若配合得当，可享长寿。
  - **English**：
    - With proper configuration, longevity attainable.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_149]` `[trigger: 财库暗官]` `[factor_trigger: caiku_anguan AND xingming_you]` `[role: 主干]` 六丁日生时辛丑，财库星明有暗官。 → 《三命通会》卷八#六丁日辛丑时
  - `[ns_smth_08_150]` `[trigger: 冲破发财]` `[factor_trigger: chongpo_facai AND bugui_jifu]` `[role: 主干依赖]` 若逢冲破财官旺，不贵即富寿且安。 → 《三命通会》卷八#六丁日辛丑时
  - `[ns_smth_08_151]` `[trigger: 未字财广]` `[factor_trigger: weizi_caiguang AND ren_xing]` `[role: 条件分支]` 运行未字财源广。 → 《三命通会》卷八#六丁日辛丑时
  - `[ns_smth_08_152]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六丁日辛丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日辛丑时断：财库暗藏与冲开发财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_185', 'bazi_semantic', 'bazi_relation_factor_84', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_112', 'caiku_ancang', 'rel_smth_08_113', 'anguan', 'rel_smth_08_114', 'youchong_youfa', 'evi_smth_08_112', 'caiku_ancang', 'rule_caiku', 'evi_smth_08_113', 'anguan', 'rule_anguan', 'evi_smth_08_114', 'chongkai_facai', 'rule_chongkai2', 'map_smth_08_075', 'map_smth_08_076']
    
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
        l1_anchor="smth_v1.0.0_六丁日辛丑时断_财库暗藏与冲开发财_001_L1",
    )
    version: str = "1.0.0"
