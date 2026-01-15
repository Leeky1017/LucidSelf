"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157620
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
    semantic_id="smth_v1.0.0_六丁日乙巳时断_日禄归时与印绶帝旺_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日乙巳时断日禄归时与印绶帝旺(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日乙巳时断。

  六丁日生时乙巳，日禄归时印帝旺；柱无财官来混杂，定主文章富贵昌。丁日乙巳时，日禄归时，丁火禄在巳，乙木印星在巳为帝旺，印禄归垣，主文...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日乙巳时断。

  六丁日生时乙巳，日禄归时印帝旺；柱无财官来混杂，定主文章富贵昌。丁日乙巳时，日禄归时，丁火禄在巳，乙木印星在巳为帝旺，印禄归垣，主文章秀发。若无财官冲破，大贵。有财官，平常。

  丁丑日乙巳时，丑刑巳，刑伤妻子。春身旺，贵。夏平，秋富，冬吉。

  丁卯日乙巳时，身旺印旺，科名有望。春大贵。夏行金水运，贵。

  丁巳日乙巳时，两巳自刑，伤妻害子。春贵，夏平，秋富，冬吉。

  丁未日乙巳时，寅午戌月，身旺，大贵。亥卯未月，印旺，贵。

  丁酉日乙巳时，巳酉半合，春身旺，贵。秋财旺，行南运，富。

  丁亥日乙巳时，亥巳相冲，伤妻害子。春身旺，贵。冬官旺，行南运，贵。

  丁日乙巳时上逢，日禄归时印帝旺；柱无财官来混杂，定主文章富贵昌。丁日乙巳时准，印禄归垣相逢。若无财官福无边，定主荣华富贵。

- 分字分词释义：

  - **日禄归时**：丁火禄在巳，时支为巳，禄位归时。
  - **印绶帝旺**：乙木偏印在巳为帝旺，印星极旺。
  - **印禄归垣**：印星与日主禄位同在一处，主文章秀发。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，乙巳时」：

  - 丁火禄在巳，时支为巳，形成「日禄归时」格；乙木偏印在巳为帝旺，印星极旺；
  - 若柱无财官冲破，则文章秀发，大贵；有财官混杂，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Yi-Si Hour":

  - Ding Fire's fortune is at Si, hour-branch is Si, forming "Day Fortune Returns to Hour"; Yi Wood Indirect Seal at Si is at emperor-prosperity—seal star extremely strong.
  - If the chart lacks wealth-official clash-breaks, this indicates literary elegance and great nobility; with wealth-official mixing, outcomes remain ordinary.

- 核心要点：

  - 本格以「日禄归时」与「印帝旺」为核心，结构优良。
  - 印禄归垣，主文学才华。
  - 最忌财官混杂。

- 详细解说：

  1. **日禄归时的优势**  
     - 丁火禄在巳，时支为巳，禄位归时；  
     - 主晚年福禄丰厚，子孙有靠。

  2. **印帝旺的加持**  
     - 乙木偏印在巳为帝旺，印星极旺；  
     - 印生身，主文学才华、学业有成。

- 校勘与字词辨析：

  - 「文章秀发」形容文学才华出众。
  - 「富贵昌」形容富贵兴旺。
  - **English**：
    - Describes flourishing wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_165]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND yin_diwang]` `[role: 主干]` 六丁日生时乙巳，日禄归时印帝旺。 → 《三命通会》卷八#六丁日乙巳时
  - `[ns_smth_08_166]` `[trigger: 无财官混]` `[factor_trigger: wu_caiguan_hun AND wenzhang_fugui]` `[role: 主干依赖]` 柱无财官来混杂，定主文章富贵昌。 → 《三命通会》卷八#六丁日乙巳时
  - `[ns_smth_08_167]` `[trigger: 印禄归垣]` `[factor_trigger: yinlu_guiyuan AND wenzhang_xiufa]` `[role: 条件分支]` 印禄归垣，主文章秀发。 → 《三命通会》卷八#六丁日乙巳时
  - `[ns_smth_08_168]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND wu_caiguan_fu]` `[role: 总结]` 若无财官福无边，定主荣华富贵。 → 《三命通会》卷八#六丁日乙巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日乙巳时断：日禄归时与印绶帝旺"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_factor_87', 'bazi_semantic', 'bazi_state_factor_194', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_62', 'bazi_semantic', 'source_ref', 'rel_smth_08_124', 'rilu_guishi', 'rel_smth_08_125', 'yinxu_diwang', 'rel_smth_08_126', 'wucaiguan_hun', 'evi_smth_08_124', 'rilu_guishi', 'rule_rilu2', 'evi_smth_08_125', 'yinxu_diwang', 'rule_diwang2', 'evi_smth_08_126', 'yinlu_guiyuan', 'rule_guiyuan', 'map_smth_08_083', 'map_smth_08_084']
    
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
        l1_anchor="smth_v1.0.0_六丁日乙巳时断_日禄归时与印绶帝旺_001_L1",
    )
    version: str = "1.0.0"
