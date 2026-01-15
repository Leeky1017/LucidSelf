"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157610
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
    semantic_id="smth_v1.0.0_六丁日甲辰时断_印绶入库与冲开显贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日甲辰时断印绶入库与冲开显贵(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日甲辰时断。

  六丁日生时甲辰，印绶入库喜相亲；若逢戌字冲开库，定主文章显贵人。丁日甲辰时，印绶入库，甲木印星入辰库，若生戌月，辰戌相冲，冲开印库，...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日甲辰时断。

  六丁日生时甲辰，印绶入库喜相亲；若逢戌字冲开库，定主文章显贵人。丁日甲辰时，印绶入库，甲木印星入辰库，若生戌月，辰戌相冲，冲开印库，主文章显达。辰戌丑未月，杂气印绶，大贵。

  丁丑日甲辰时，春身旺，贵。夏平，秋富，冬吉。辰戌丑未年月，大贵。

  丁卯日甲辰时，身旺印旺，科名有望。春大贵。戌月冲库，行南运，大贵。

  丁巳日甲辰时，贵。春身旺，夏平，秋富，冬吉。

  丁未日甲辰时，春身旺，行西北运，贵。秋财旺，冬官旺，俱吉。

  丁酉日甲辰时，春身旺，贵。秋财旺，行南运，富。辰戌年月，冲库，大贵。

  丁亥日甲辰时，亥卯未月，印旺，大贵。戌月冲库，贵显。

  丁日甲辰时上逢，印绶入库待冲逢；运行戌字冲开库，定主文章贵显隆。丁日甲辰时准，印星入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **印绶入库**：甲木正印入辰库，印星有储藏。
  - **冲开显贵**：戌冲辰，冲开印库，印星得用，主文章显达。
  - **杂气印绶**：辰戌丑未为杂气之地，印绶藏于其中。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，甲辰时」：

  - 甲木正印入辰库，印星有储藏；若生戌月或柱有戌字，辰戌相冲，冲开印库，主文章显达；
  - 不冲则印星储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Jia-Chen Hour":

  - Jia Wood Direct Seal enters Chen treasury; if born in Xu month or chart has Xu, Chen-Xu clash opens seal treasury indicating literary prominence.
  - Without clash, seal star remains stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「印绶入库」为核心，需冲开方能发用。
  - 冲开则文章显达，不冲则平常。
  - 杂气月生者更能发挥印绶的作用。

- 详细解说：

  1. **印绶入库的特点**  
     - 辰为木库，甲木正印入库有储藏；  
     - 需要戌冲或行运冲开，方能发挥。

  2. **冲开的重要性**  
     - 戌冲辰，冲开印库，印星得用；  
     - 主文章显达、科举有成。

- 校勘与字词辨析：

  - 「待冲逢」形容印库等待冲开后方能发挥。
  - 「贵显隆」形容显贵兴隆。
  - **English**：
    - Describes flourishing nobility and prosperity.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_161]` `[trigger: 印绶入库]` `[factor_trigger: yinxu_ruku AND xi_xiangqin]` `[role: 主干]` 六丁日生时甲辰，印绶入库喜相亲。 → 《三命通会》卷八#六丁日甲辰时
  - `[ns_smth_08_162]` `[trigger: 戌字冲库]` `[factor_trigger: xuzi_chongku AND wenzhang_xian_gui]` `[role: 主干依赖]` 若逢戌字冲开库，定主文章显贵人。 → 《三命通会》卷八#六丁日甲辰时
  - `[ns_smth_08_163]` `[trigger: 杂气印绶]` `[factor_trigger: zaqi_yinxu AND da_gui]` `[role: 条件分支]` 辰戌丑未月，杂气印绶，大贵。 → 《三命通会》卷八#六丁日甲辰时
  - `[ns_smth_08_164]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六丁日甲辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日甲辰时断：印绶入库与冲开显贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_191', 'bazi_semantic', 'bazi_relation_factor_86', 'bazi_semantic', 'bazi_state_factor_192', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_121', 'yinxu_ruku', 'rel_smth_08_122', 'chongkai_xiangui', 'rel_smth_08_123', 'youchong_youfa', 'evi_smth_08_121', 'yinxu_ruku', 'rule_yinruku', 'evi_smth_08_122', 'chongkai_xiangui', 'rule_xiangui', 'evi_smth_08_123', 'zaqi_yinxu', 'rule_zaqi', 'map_smth_08_081', 'map_smth_08_082']
    
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
        l1_anchor="smth_v1.0.0_六丁日甲辰时断_印绶入库与冲开显贵_001_L1",
    )
    version: str = "1.0.0"
