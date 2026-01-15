"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157591
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
    semantic_id="smth_v1.0.0_六丁日壬寅时断_官印相生与长生得地_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日壬寅时断官印相生与长生得地(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日壬寅时断。

  六丁日生时壬寅，官印长生最为真；月气通根身旺相，文章显达贵超群。丁日壬寅时，官印长生，丁用壬为官，甲为印，寅上甲禄壬长生，壬合丁，若...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日壬寅时断。

  六丁日生时壬寅，官印长生最为真；月气通根身旺相，文章显达贵超群。丁日壬寅时，官印长生，丁用壬为官，甲为印，寅上甲禄壬长生，壬合丁，若通身旺月，官印两旺，文章显达，大贵。不通月气，平常。

  丁丑日壬寅时，丑刑寅，刑伤妻子。春身旺，吉。夏平，秋富，冬贵。卯未年月，大贵。

  丁卯日壬寅时，身强印旺，科甲有望。春大贵。夏平，秋富，冬官旺，俱吉。

  丁巳日壬寅时，巳寅刑，伤妻害子。春贵，夏平，秋富，冬吉。子申辰年月，官旺，大贵。

  丁未日壬寅时，寅午戌月，身旺，大贵。亥卯未月，印旺，贵。申子辰月，官旺，吉。

  丁酉日壬寅时，春身旺，行西北运，贵。秋财旺，行南运，富。亥卯未、申子辰年月，大贵。

  丁亥日壬寅时，亥卯未月，印旺，大贵。申子辰月，官旺，贵。巳酉丑月，财旺，富。

  丁日壬寅时上逢，官星印绶两相逢；柱中身旺通月气，定主文章贵显隆。丁日壬寅时准，官印长生得地。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **官印长生**：壬水正官在寅为长生，甲木正印在寅为建禄，官印皆得长生。
  - **壬合丁**：壬水与丁火相合，官合日主，有情。
  - **文章显达**：主文学才华出众，适合科举仕途。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，壬寅时」：

  - 壬水正官在寅为长生，甲木正印在寅为建禄，形成「官印长生」的结构；
  - 壬水与丁火相合，官合日主，有情；若通身旺月，官印两旺，文章显达，大贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Ren-Yin Hour":

  - Ren Water Direct Official at Yin is at long life; Jia Wood Direct Seal at Yin is at establishment—forming "official-seal at longevity."
  - Ren Water combines with Ding Fire, official joining day-master affectionately; if connected with strong-body month, official-seal both prosperous, literary prominence achieved, great nobility.

- 核心要点：

  - 本格以「官印长生」为核心，结构优良。
  - 官印相生，壬丁相合，主文学仕途。
  - 身旺月气是关键。

- 详细解说：

  1. **官印长生的优势**  
     - 壬水正官在寅为长生，官星有力；  
     - 甲木正印在寅为建禄，印星有根。

  2. **壬丁相合的特点**  
     - 壬水与丁火相合，官合日主；  
     - 有情有义，主贵人扶持、仕途顺利。

- 校勘与字词辨析：

  - 「科甲有望」指科举登第有希望。
  - 「贵显隆」形容显贵兴隆。
  - **English**：
    - Describes flourishing nobility and prosperity.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_153]` `[trigger: 官印长生]` `[factor_trigger: guanyin_changsheng AND zui_wei_zhen]` `[role: 主干]` 六丁日生时壬寅，官印长生最为真。 → 《三命通会》卷八#六丁日壬寅时
  - `[ns_smth_08_154]` `[trigger: 月气通根]` `[factor_trigger: yueqi_tonggen AND wenzhang_xianda]` `[role: 主干依赖]` 月气通根身旺相，文章显达贵超群。 → 《三命通会》卷八#六丁日壬寅时
  - `[ns_smth_08_155]` `[trigger: 壬合丁]` `[factor_trigger: ren_he_ding AND guanyin_liang_wang]` `[role: 条件分支]` 壬合丁，若通身旺月，官印两旺，大贵。 → 《三命通会》卷八#六丁日壬寅时
  - `[ns_smth_08_156]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六丁日壬寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日壬寅时断：官印相生与长生得地"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_187', 'bazi_semantic', 'bazi_relation_ren_ding', 'bazi_semantic', 'bazi_state_factor_208', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_115', 'guanyin_changsheng', 'rel_smth_08_116', 'rending_xianghe', 'rel_smth_08_117', 'tongshenwang_yue', 'evi_smth_08_115', 'guanyin_changsheng', 'rule_changsheng', 'evi_smth_08_116', 'rending_xianghe', 'rule_xianghe', 'evi_smth_08_117', 'wenzhang_xianda', 'rule_xianda', 'map_smth_08_077', 'map_smth_08_078']
    
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
        l1_anchor="smth_v1.0.0_六丁日壬寅时断_官印相生与长生得地_001_L1",
    )
    version: str = "1.0.0"
