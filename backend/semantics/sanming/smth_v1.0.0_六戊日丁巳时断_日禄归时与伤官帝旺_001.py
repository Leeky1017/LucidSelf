"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157739
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
    semantic_id="smth_v1.0.0_六戊日丁巳时断_日禄归时与伤官帝旺_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日丁巳时断日禄归时与伤官帝旺(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日丁巳时断。

  六戊日生时丁巳，日禄归时伤官旺；柱无官煞来混杂，定主文章富贵昌。戊日丁巳时，日禄归时，戊土禄在巳，丁火伤官在巳为帝旺，伤官禄旺。若无...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日丁巳时断。

  六戊日生时丁巳，日禄归时伤官旺；柱无官煞来混杂，定主文章富贵昌。戊日丁巳时，日禄归时，戊土禄在巳，丁火伤官在巳为帝旺，伤官禄旺。若无官煞冲破，大贵。有官煞，平常。

  戊子日丁巳时，子巳暗合，春印旺，贵。夏身旺，吉。

  戊寅日丁巳时，寅巳刑，刑伤妻子。春印旺，贵。夏身旺，吉。

  戊辰日丁巳时，春印旺，贵。夏身旺，吉。辰戌丑未月，杂气伤官，大贵。

  戊午日丁巳时，午巳相并，伤官太旺。春印旺，贵。夏身旺，吉。

  戊申日丁巳时，巳申合，合伤官。春印旺，贵。秋财旺，富。

  戊戌日丁巳时，春印旺，贵。夏身旺，吉。辰戌丑未月，大贵。

  戊日丁巳时上逢，日禄归时伤官旺；柱无官煞来混杂，定主文章富贵昌。戊日丁巳时准，伤官禄旺相逢。若无官煞福无边，定主荣华富贵。

- 分字分词释义：

  - **日禄归时**：戊土禄在巳，时支为巳，禄位归时。
  - **伤官帝旺**：丁火伤官在巳为帝旺，伤官极旺。
  - **伤官禄旺**：伤官与日主禄位同在一处，主聪明才华。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，丁巳时」：

  - 戊土禄在巳，时支为巳，形成「日禄归时」格；丁火伤官在巳为帝旺，伤官极旺；
  - 若柱无官煞冲破，则文章秀发，大贵；有官煞混杂，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Ding-Si Hour":

  - Wu Earth's fortune is at Si, hour-branch is Si—forming "Day Fortune Returns to Hour"; Ding Fire Hurting Official at Si is at emperor-prosperity—hurting-official extremely strong.
  - If chart lacks official-killing interference, literary elegance achieves great nobility; with official-killing mixed, outcomes remain ordinary.

- 核心要点：

  - 本格以「日禄归时」与「伤官帝旺」为核心，结构优良。
  - 伤官禄旺，主聪明才华。
  - 最忌官煞混杂。

- 详细解说：

  1. **日禄归时的优势**  
     - 戊土禄在巳，时支为巳，禄位归时；  
     - 主晚年福禄丰厚，子孙有靠。

  2. **伤官帝旺的特点**  
     - 丁火伤官在巳为帝旺，伤官极旺；  
     - 伤官主聪明才华、创意表达。

- 校勘与字词辨析：

  - 「富贵昌」形容富贵兴旺。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_213]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND shangguan_wang]` `[role: 主干]` 六戊日生时丁巳，日禄归时伤官旺。 → 《三命通会》卷八#六戊日丁巳时
  - `[ns_smth_08_214]` `[trigger: 无官煞混]` `[factor_trigger: wu_guansha_hun AND wenzhang_fugui]` `[role: 主干依赖]` 柱无官煞来混杂，定主文章富贵昌。 → 《三命通会》卷八#六戊日丁巳时
  - `[ns_smth_08_215]` `[trigger: 伤官禄旺]` `[factor_trigger: shangguan_luwang AND congming_caihua]` `[role: 条件分支]` 伤官禄旺，主聪明才华。 → 《三命通会》卷八#六戊日丁巳时
  - `[ns_smth_08_216]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND wu_guansha_fu]` `[role: 总结]` 若无官煞福无边，定主荣华富贵。 → 《三命通会》卷八#六戊日丁巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日丁巳时断：日禄归时与伤官帝旺"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_shangguan_7', 'bazi_semantic', 'bazi_state_shangguan_7', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_74', 'bazi_semantic', 'source_ref', 'rel_smth_08_160', 'rilu_guishi', 'rel_smth_08_161', 'shangguan_diwang', 'rel_smth_08_162', 'wuguansha_hunza', 'evi_smth_08_160', 'rilu_guishi', 'rule_rilu3', 'evi_smth_08_161', 'shangguan_diwang', 'rule_diwang5', 'evi_smth_08_162', 'shangguan_luwang', 'rule_luwang', 'map_smth_08_107', 'map_smth_08_108']
    
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
        l1_anchor="smth_v1.0.0_六戊日丁巳时断_日禄归时与伤官帝旺_001_L1",
    )
    version: str = "1.0.0"
