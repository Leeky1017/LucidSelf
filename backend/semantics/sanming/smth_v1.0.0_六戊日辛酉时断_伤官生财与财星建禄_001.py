"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157778
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
    semantic_id="smth_v1.0.0_六戊日辛酉时断_伤官生财与财星建禄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日辛酉时断伤官生财与财星建禄(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日辛酉时断。

  六戊日生时辛酉，伤官生财喜身强；月通身旺财官旺，不贵即富福禄长。戊日辛酉时，伤官生财，辛金伤官，癸水正财，酉上辛旺癸长生，若通身旺月...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日辛酉时断。

  六戊日生时辛酉，伤官生财喜身强；月通身旺财官旺，不贵即富福禄长。戊日辛酉时，伤官生财，辛金伤官，癸水正财，酉上辛旺癸长生，若通身旺月，伤官生财，大富。身弱财旺，平常。

  戊子日辛酉时，子酉相破，伤妻害子。春印旺，贵。秋财旺，富。

  戊寅日辛酉时，寅酉暗合，春印旺，贵。秋财旺，行南运，富。

  戊辰日辛酉时，春印旺，贵。夏身旺，吉。巳酉丑月，合财，大富。

  戊午日辛酉时，午酉相破，伤妻害子。春印旺，贵。秋财旺，富。

  戊申日辛酉时，申酉相并，伤官太旺。春印旺，贵。秋财旺，富。

  戊戌日辛酉时，酉戌暗合，春印旺，贵。秋财旺，富。辰戌丑未月，大贵。

  戊日辛酉时上逢，伤官生财喜身强；月通身旺财官旺，不贵即富福禄长。戊日辛酉时准，伤官生财相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **伤官生财**：辛金伤官生助癸水正财，形成良性结构。
  - **财星建禄**：辛金伤官在酉为建禄，伤官有力。
  - **身旺用财**：日主身旺方能驾驭财星为用。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，辛酉时」：

  - 辛金伤官在酉为建禄，癸水正财在酉为长生，形成「伤官生财」的结构；
  - 若通身旺月，伤官生财，大富；身弱财旺，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Xin-You Hour":

  - Xin Metal Hurting Official at You is at establishment; Gui Water Direct Wealth at You is at longevity—forming "hurting-official generating wealth."
  - If connected with strong-body month, hurting-official generating wealth achieves great riches; if body is weak with prosperous wealth, outcomes remain ordinary.

- 核心要点：

  - 本格以「伤官生财」为核心，结构优良。
  - 伤官忌见官，但喜见财。
  - 身旺是关键。

- 详细解说：

  1. **伤官生财的优势**  
     - 辛金伤官生助癸水正财；  
     - 伤官忌官喜财，形成良性结构。

  2. **身旺的必要性**  
     - 身旺方能用财，身弱财旺反凶；  
     - 需要月令通火土之气。

- 校勘与字词辨析：

  - 「福禄长」形容福禄长久。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_229]` `[trigger: 伤官生财]` `[factor_trigger: shangguan_shengcai AND xi_shenqiang]` `[role: 主干]` 六戊日生时辛酉，伤官生财喜身强。 → 《三命通会》卷八#六戊日辛酉时
  - `[ns_smth_08_230]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄长。 → 《三命通会》卷八#六戊日辛酉时
  - `[ns_smth_08_231]` `[trigger: 身弱财旺]` `[factor_trigger: shenruo_caiwang AND ping_chang]` `[role: 条件分支]` 身弱财旺，平常。 → 《三命通会》卷八#六戊日辛酉时
  - `[ns_smth_08_232]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六戊日辛酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日辛酉时断：伤官生财与财星建禄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'bazi_relation_factor_97', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_172', 'shangguan_shengcai', 'rel_smth_08_173', 'caixing_jianlu', 'rel_smth_08_174', 'tongshenwang_yue', 'evi_smth_08_172', 'shangguan_shengcai', 'rule_shengcai4', 'evi_smth_08_173', 'caixing_jianlu', 'rule_jianlu2', 'evi_smth_08_174', 'shenwang_yongcai', 'rule_yongcai6', 'map_smth_08_115', 'map_smth_08_116']
    
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
        l1_anchor="smth_v1.0.0_六戊日辛酉时断_伤官生财与财星建禄_001_L1",
    )
    version: str = "1.0.0"
