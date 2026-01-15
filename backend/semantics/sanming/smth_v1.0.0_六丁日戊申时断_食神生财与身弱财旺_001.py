"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157652
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
    semantic_id="smth_v1.0.0_六丁日戊申时断_食神生财与身弱财旺_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日戊申时断食神生财与身弱财旺(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日戊申时断。

  六丁日生时戊申，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。丁日戊申时，食神生财，戊土食神，庚金偏财，申上庚旺戊长生，若通身旺月...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日戊申时断。

  六丁日生时戊申，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。丁日戊申时，食神生财，戊土食神，庚金偏财，申上庚旺戊长生，若通身旺月，食神生财，财官双美，大贵。身弱财旺，平常。

  丁丑日戊申时，巳酉丑月，合财，大富。寅午戌月，身旺用财，大贵。

  丁卯日戊申时，春身旺，行西北运，贵。秋财旺，行南运，富。

  丁巳日戊申时，巳申合，贵。春身旺，大贵。秋财旺，富。

  丁未日戊申时，春身旺，行西北运，贵。秋财旺，富。辰戌丑未月，大贵。

  丁酉日戊申时，巳酉丑月，合财，大富。寅午戌月，身旺，大贵。

  丁亥日戊申时，亥卯未月，印旺，大贵。申子辰月，官旺，贵。

  丁日戊申时上逢，食神生财喜身强；月通身旺财官旺，不贵即富福禄昌。丁日戊申时准，食神生财相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **食神生财**：戊土食神生助庚金偏财，形成食神生财的结构。
  - **身弱财旺**：日主身弱而财星太旺，难以驾驭财星。
  - **财官双美**：财星与官星同旺，形成富贵的结构。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，戊申时」：

  - 戊土食神在申为长生，庚金偏财在申为建禄，形成「食神生财」的结构；
  - 若通身旺月，食神生财、财官双美，大贵；身弱财旺，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Wu-Shen Hour":

  - Wu Earth Food God at Shen is at long life; Geng Metal Indirect Wealth at Shen is at establishment—forming "food-god generating wealth."
  - If connected with strong-body month, food-god generating wealth with wealth-official double beauty achieves great nobility; if body is weak with prosperous wealth, outcomes remain ordinary.

- 核心要点：

  - 本格以「食神生财」为核心，结构优良。
  - 身旺是关键，方能驾驭财星。
  - 歌诀强调：身旺财官旺，不贵即富。

- 详细解说：

  1. **食神生财的优势**  
     - 戊土食神生助庚金偏财；  
     - 形成食神生财的良性循环。

  2. **身旺的必要性**  
     - 丁火在申为长生（有说为病地），需看月令配合；  
     - 身旺方能用财，身弱财旺反凶。

- 校勘与字词辨析：

  - 「福禄昌」形容福禄兴旺。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_177]` `[trigger: 食神生财]` `[factor_trigger: shishen_shengcai AND xi_shenqiang]` `[role: 主干]` 六丁日生时戊申，食神生财喜身强。 → 《三命通会》卷八#六丁日戊申时
  - `[ns_smth_08_178]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄昌。 → 《三命通会》卷八#六丁日戊申时
  - `[ns_smth_08_179]` `[trigger: 身弱财旺]` `[factor_trigger: shenruo_caiwang AND ping_chang]` `[role: 条件分支]` 身弱财旺，平常。 → 《三命通会》卷八#六丁日戊申时
  - `[ns_smth_08_180]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六丁日戊申时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日戊申时断：食神生财与身弱财旺"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_shishen_9', 'bazi_semantic', 'bazi_relation_factor_89', 'bazi_semantic', 'bazi_state_factor_264', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_133', 'shishen_shengcai', 'rel_smth_08_134', 'shishen_shengcai', 'rel_smth_08_135', 'tongshenwang_yue', 'evi_smth_08_133', 'shishen_shengcai', 'rule_shengcai', 'evi_smth_08_134', 'shenruo_caiwang', 'rule_shenruo', 'evi_smth_08_135', 'caiguan_shuangmei', 'rule_shuangmei2', 'map_smth_08_089', 'map_smth_08_090']
    
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
        l1_anchor="smth_v1.0.0_六丁日戊申时断_食神生财与身弱财旺_001_L1",
    )
    version: str = "1.0.0"
