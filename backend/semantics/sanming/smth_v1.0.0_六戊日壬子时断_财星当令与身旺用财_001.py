"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157690
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
    semantic_id="smth_v1.0.0_六戊日壬子时断_财星当令与身旺用财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日壬子时断财星当令与身旺用财(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日壬子时断。

  六戊日生逢壬子，财星当令喜身强；月有倚托身旺相，定主财源广进昌。戊日壬子时，财星当令，戊以壬为偏财，子上壬旺，若通身旺月者，身强财旺...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日壬子时断。

  六戊日生逢壬子，财星当令喜身强；月有倚托身旺相，定主财源广进昌。戊日壬子时，财星当令，戊以壬为偏财，子上壬旺，若通身旺月者，身强财旺，大富。身弱财旺，平常。

  戊子日壬子时，两子相并，主孤独。辰戌丑未月，杂气财官，大贵。寅卯月，印旺，贵。

  戊寅日壬子时，寅为长生，身旺用财，大贵。申子辰月，财旺，富。巳午月，身旺，贵。

  戊辰日壬子时，申子辰月，合财，大富。寅午戌月，身旺，大贵。

  戊午日壬子时，子午相冲，伤妻害子。寅卯月，印旺，贵。申子辰月，财旺，富。

  戊申日壬子时，申子半合，财旺。春印旺，贵。夏身旺，吉。秋财旺，富。冬官旺，贵。

  戊戌日壬子时，春印旺，贵。夏身旺，吉。秋财旺，富。冬官旺，贵。辰戌丑未月，大贵。

  戊日壬子时上逢，财星当令喜身强；月通身旺财官旺，定主财源广进昌。戊日壬子时准，财星当令相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **财星当令**：壬水偏财在子为建禄，财星得令。
  - **身旺用财**：日主身旺方能驾驭财星为用。
  - **财源广进**：财运亨通，收入丰厚。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，壬子时」：

  - 壬水偏财在子为建禄，财星得令；若通身旺月，身强财旺，大富；
  - 身弱财旺，则难以驾驭，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Ren-Zi Hour":

  - Ren Water Indirect Wealth at Zi is at establishment—wealth star in season; if connected with strong-body month, body strong with prosperous wealth leads to great riches.
  - If body is weak with prosperous wealth, unable to control—ordinary livelihood.

- 核心要点：

  - 本格以「财星当令」为核心，财星有力。
  - 身旺是关键，方能驾驭财星。
  - 歌诀强调：身旺财官旺，定主财源广进。

- 详细解说：

  1. **财星当令的优势**  
     - 子上壬水偏财得禄，财星有力；  
     - 财源稳定，利于积累财富。

  2. **身旺的必要性**  
     - 戊土在子为胎地，需月令扶助；  
     - 身旺方能用财，身弱财旺反凶。

- 校勘与字词辨析：

  - 「财源广进昌」形容财源广阔、兴旺发达。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_193]` `[trigger: 财星当令]` `[factor_trigger: caixing_dangling AND xi_shenqiang]` `[role: 主干]` 六戊日生逢壬子，财星当令喜身强。 → 《三命通会》卷八#六戊日壬子时
  - `[ns_smth_08_194]` `[trigger: 身旺相]` `[factor_trigger: shenwang_xiang AND caiyuan_guangjin]` `[role: 主干依赖]` 月有倔托身旺相，定主财源广进昌。 → 《三命通会》卷八#六戊日壬子时
  - `[ns_smth_08_195]` `[trigger: 身弱财旺]` `[factor_trigger: shenruo_caiwang AND ping_chang]` `[role: 条件分支]` 身弱财旺，平常。 → 《三命通会》卷八#六戊日壬子时
  - `[ns_smth_08_196]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六戊日壬子时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日壬子时断：财星当令与身旺用财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_factor_203', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'bazi_state_factor_204', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_145', 'caixing_dangling', 'rel_smth_08_146', 'shenwang_yongcai', 'rel_smth_08_147', 'tongshenwang_yue', 'evi_smth_08_145', 'caixing_dangling', 'rule_dangling', 'evi_smth_08_146', 'shenwang_yongcai', 'rule_yongcai4', 'evi_smth_08_147', 'caiyuan_guangjin', 'rule_guangjin', 'map_smth_08_097', 'map_smth_08_098']
    
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
        l1_anchor="smth_v1.0.0_六戊日壬子时断_财星当令与身旺用财_001_L1",
    )
    version: str = "1.0.0"
