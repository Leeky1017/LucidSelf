"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157769
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
    semantic_id="smth_v1.0.0_六戊日庚申时断_食神生财与财星长生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日庚申时断食神生财与财星长生(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日庚申时断。

  六戊日生时庚申，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。戊日庚申时，食神生财，庚金食神，壬水偏财，申上庚旺壬长生，若通身旺月...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日庚申时断。

  六戊日生时庚申，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。戊日庚申时，食神生财，庚金食神，壬水偏财，申上庚旺壬长生，若通身旺月，食神生财，大富。身弱财旺，平常。

  戊子日庚申时，申子半合，财旺。春印旺，贵。夏身旺，吉。秋财旺，富。

  戊寅日庚申时，寅申相冲，伤妻害子。春印旺，贵。秋财旺，行南运，富。

  戊辰日庚申时，申子辰月，合财，大富。寅午戌月，身旺，大贵。

  戊午日庚申时，春印旺，贵。夏身旺，吉。秋财旺，富。

  戊申日庚申时，两申相并，食神太旺。春印旺，贵。秋财旺，富。

  戊戌日庚申时，春印旺，贵。夏身旺，吉。秋财旺，富。辰戌丑未月，大贵。

  戊日庚申时上逢，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。戊日庚申时准，食神生财相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **食神生财**：庚金食神生助壬水偏财，形成良性循环。
  - **财星长生**：壬水偏财在申为长生，财源有根。
  - **身旺用财**：日主身旺方能驾驭财星为用。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，庚申时」：

  - 庚金食神在申为建禄，壬水偏财在申为长生，形成「食神生财」的结构；
  - 若通身旺月，食神生财，大富；身弱财旺，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Geng-Shen Hour":

  - Geng Metal Food God at Shen is at establishment; Ren Water Indirect Wealth at Shen is at longevity—forming "food-god generating wealth."
  - If connected with strong-body month, food-god generating wealth achieves great riches; if body is weak with prosperous wealth, outcomes remain ordinary.

- 核心要点：

  - 本格以「食神生财」为核心，结构优良。
  - 身旺是关键，方能驾驭财星。
  - 财星长生有根，财源稳定。

- 详细解说：

  1. **食神生财的优势**  
     - 庚金食神生助壬水偏财；  
     - 形成食神生财的良性循环。

  2. **财星长生的特点**  
     - 壬水偏财在申为长生，财源有根；  
     - 财源稳定，利于积累财富。

- 校勘与字词辨析：

  - 「福禄昌」形容福禄兴旺。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_225]` `[trigger: 食神生财]` `[factor_trigger: shishen_shengcai AND xi_shenqiang]` `[role: 主干]` 六戊日生时庚申，食神生财喜身强。 → 《三命通会》卷八#六戊日庚申时
  - `[ns_smth_08_226]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄昌。 → 《三命通会》卷八#六戊日庚申时
  - `[ns_smth_08_227]` `[trigger: 身弱财旺]` `[factor_trigger: shenruo_caiwang AND ping_chang]` `[role: 条件分支]` 身弱财旺，平常。 → 《三命通会》卷八#六戊日庚申时
  - `[ns_smth_08_228]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六戊日庚申时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日庚申时断：食神生财与财星长生"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_shishen_9', 'bazi_semantic', 'bazi_relation_factor_96', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_169', 'shishen_shengcai', 'rel_smth_08_170', 'caixing_changsheng', 'rel_smth_08_171', 'tongshenwang_yue', 'evi_smth_08_169', 'shishen_shengcai', 'rule_shengcai3', 'evi_smth_08_170', 'caixing_changsheng', 'rule_changsheng', 'evi_smth_08_171', 'shenwang_yongcai', 'rule_yongcai5', 'map_smth_08_113', 'map_smth_08_114']
    
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
        l1_anchor="smth_v1.0.0_六戊日庚申时断_食神生财与财星长生_001_L1",
    )
    version: str = "1.0.0"
