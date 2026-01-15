"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339789
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
    semantic_id="smth_v1.0.0_六壬日丁未时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日丁未时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时丁未，夫化妻从格局奇。若是局中通水木，发财发福两相宜。
  壬日丁未时，夫从妻化，壬合丁，未上同木局，贵。若月通木局，有倚托者发财，不通，但有资助，...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时丁未，夫化妻从格局奇。若是局中通水木，发财发福两相宜。
  壬日丁未时，夫从妻化，壬合丁，未上同木局，贵。若月通木局，有倚托者发财，不通，但有资助，因妻致富。

- 分字分词释义：
  - **夫从妻化**：壬（阳水）合丁（阴火），化木。丁为妻，壬为夫（相对于丁而言，或指阳干为夫）。此处指化木格。
  - **未上同木局**：未为木库，亥卯未合木。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于丁未时，丁壬相合化木。未为木库。若生于木旺之月（寅卯），或地支成木局，化气成格，主贵。若有倚托（身旺）且通木局，发财。若不通木局，但有其他资助，主因妻致富（丁为财）。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Ding-Wei Hour":

  - Husband transforms wife follows pattern marvelous—Ren combines Ding transforming into Wood; Wei is Wood treasury.
  - If pattern inside connects Water-Wood, developing wealth developing fortune both suitable.
  - Ren combines Ding; Wei above same Wood bureau, noble; if month connects Wood bureau with support, developing wealth; not connecting but has assistance, rich due to wife.
  - Key: Transformation pattern requires Wood prosperous month; non-transformation normal Wealth pattern also auspicious.

- 核心要点：
  - **化木格**：丁壬化木，喜木旺月。
  - **正财合身**：丁壬合。
  - **官库**：未为官库（己土）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_173]` `[trigger: 夫化妻从]` `[factor_trigger: fuhua_qicong AND geju_qi]` `[role: 主干]` 六壬日生时丁未，夫化妻从格局奇。 → 《三命通会》卷九#六壬日丁未时
  - `[ns_smth_09_174]` `[trigger: 通水木]` `[factor_trigger: tong_shuimu AND facai_fafu]` `[role: 主干依赖]` 若是局中通水木，发财发福两相宜。 → 《三命通会》卷九#六壬日丁未时
  - `[ns_smth_09_175]` `[trigger: 丁壬化木]` `[factor_trigger: dingren_huamu AND wei_muku]` `[role: 条件分支]` 壬合丁，未上同木局，贵。 → 《三命通会》卷九#六壬日丁未时
  - `[ns_smth_09_176]` `[trigger: 因妻致富]` `[factor_trigger: yinqi_zhifu AND butong_zizhu]` `[role: 总结]` 若月通木局，有倚托者发财，不通，但有资助，因妻致富。 → 《三命通会》卷九#六壬日丁未时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日丁未时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_ding_ren_wood', 'bazi_semantic', 'bazi_relation_zhengcai', 'bazi_semantic', 'bazi_state_factor_339', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_wood', 'bazi_semantic', 'source_ref', 'rel_smth_09_130', 'dingren_huamu', 'rel_smth_09_131', 'dingren_huamu', 'rel_smth_09_132', 'zhengcai_heshen', 'evi_smth_09_130', 'dingren_huamu', 'rule_dingren_huamu1', 'evi_smth_09_131', 'facai_fafu', 'rule_facai_fafu_dingwei1', 'evi_smth_09_132', 'yinqi_zhifu', 'rule_yinqi_zhifu1', 'map_smth_09_087', 'map_smth_09_088']
    
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
        l1_anchor="smth_v1.0.0_六壬日丁未时_001_L1",
    )
    version: str = "1.0.0"
