"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157662
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
    semantic_id="smth_v1.0.0_六丁日己酉时断_伤官见财与身旺用财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日己酉时断伤官见财与身旺用财(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日己酉时断。

  六丁日生时己酉，伤官见财喜身强；月通身旺财官旺，不贵即富福禄长。丁日己酉时，伤官见财，己土伤官，辛金正财，酉上辛旺己长生，若通身旺月...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日己酉时断。

  六丁日生时己酉，伤官见财喜身强；月通身旺财官旺，不贵即富福禄长。丁日己酉时，伤官见财，己土伤官，辛金正财，酉上辛旺己长生，若通身旺月，伤官生财，财官双美，大贵。身弱财旺，平常。

  丁丑日己酉时，巳酉丑月，合财，大富。寅午戌月，身旺，大贵。

  丁卯日己酉时，卯酉相冲，伤妻害子。春身旺，贵。秋财旺，富。

  丁巳日己酉时，巳酉半合，贵。春身旺，大贵。秋财旺，富。

  丁未日己酉时，酉未暗合，春身旺，贵。秋财旺，富。

  丁酉日己酉时，两酉自刑，伤妻害子。春身旺，贵。秋财旺，富。

  丁亥日己酉时，春身旺，行金水运，贵。秋财旺，行南运，富。

  丁日己酉时上逢，伤官生财喜身强；月通身旺财官旺，不贵即富福禄长。丁日己酉时准，伤官生财相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **伤官见财**：己土伤官见辛金正财，伤官生财。
  - **伤官生财**：伤官生助财星，形成良性结构。
  - **身旺用财**：日主身旺方能驾驭财星为用。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，己酉时」：

  - 己土伤官在酉为长生，辛金正财在酉为建禄，形成「伤官生财」的结构；
  - 若通身旺月，伤官生财、财官双美，大贵；身弱财旺，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Ji-You Hour":

  - Ji Earth Hurting Official at You is at long life; Xin Metal Direct Wealth at You is at establishment—forming "hurting-official generating wealth."
  - If connected with strong-body month, hurting-official generating wealth with wealth-official double beauty achieves great nobility; if body is weak with prosperous wealth, outcomes remain ordinary.

- 核心要点：

  - 本格以「伤官生财」为核心，结构优良。
  - 伤官忌见官，但喜见财。
  - 身旺是关键。

- 详细解说：

  1. **伤官生财的优势**  
     - 己土伤官生助辛金正财；  
     - 伤官忌官喜财，形成良性结构。

  2. **身旺的必要性**  
     - 身旺方能用财，身弱财旺反凶；  
     - 需要月令通火木之气。

- 校勘与字词辨析：

  - 「福禄长」形容福禄长久。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_181]` `[trigger: 伤官见财]` `[factor_trigger: shangguan_jiancai AND xi_shenqiang]` `[role: 主干]` 六丁日生时己酉，伤官见财喜身强。 → 《三命通会》卷八#六丁日己酉时
  - `[ns_smth_08_182]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄长。 → 《三命通会》卷八#六丁日己酉时
  - `[ns_smth_08_183]` `[trigger: 身弱财旺]` `[factor_trigger: shenruo_caiwang AND ping_chang]` `[role: 条件分支]` 身弱财旺，平常。 → 《三命通会》卷八#六丁日己酉时
  - `[ns_smth_08_184]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六丁日己酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日己酉时断：伤官见财与身旺用财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'bazi_relation_shangguan_6', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_136', 'shangguan_shengcai', 'rel_smth_08_137', 'shangguan_jiancai', 'rel_smth_08_138', 'tongshenwang_yue', 'evi_smth_08_136', 'shangguan_shengcai', 'rule_shengcai2', 'evi_smth_08_137', 'shangguan_jiancai', 'rule_jiancai', 'evi_smth_08_138', 'shenwang_yongcai', 'rule_yongcai3', 'map_smth_08_091', 'map_smth_08_092']
    
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
        l1_anchor="smth_v1.0.0_六丁日己酉时断_伤官见财与身旺用财_001_L1",
    )
    version: str = "1.0.0"
