"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412786
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
    semantic_id="smth_v1.0.0_伤官与才气之偏锋_001",
    book_id="sanming",
    engine_id="bazi"
)
class 伤官与才气之偏锋(SemanticEntry):
    """
    - **原文（source_text）**：

  论伤官：伤官者，我生彼之谓，乃甲见丁、乙见丙之类。甲用辛为官，丁火乘旺，盗我之气，克制辛金，使不辅甲为贵，故名伤官。伤官格务要伤尽，方作贵看。元有官...
    """
    
    original_text: str = """- **原文（source_text）**：

  论伤官：伤官者，我生彼之谓，乃甲见丁、乙见丙之类。甲用辛为官，丁火乘旺，盗我之气，克制辛金，使不辅甲为贵，故名伤官。伤官格务要伤尽，方作贵看。元有官星，伤之则重。《经》云：“伤官见官，祸患百端”是也。伤官虽凶，乃我所生，自家之物，伤尽则能生财，财旺则能生官，造化展转有情。如月令在伤官，四柱作合结局，皆在伤位，无冲无破，不见一点官星，谓之伤尽。又有月支伤官、时上伤官，四柱无官星，亦谓伤尽。更身旺、财旺或印旺，名标金榜，一品贵人。此格主多材艺，傲物气高，心险无忌惮，多谋少遂，弄巧成拙，常以天下之人不如己，而人亦惮之恶之。伤官无财主贫穷，盖生财气者即食神伤官，盗财气者即七煞官星，所以伤官要见财，不要见官。假如甲生午月，木不南奔，身势太柔，岂可再逢金制？金能盗土之气，所以不要见官。既无官星，而柱却无一点财可恃，虽聪明机巧，不过虚名虚利。《经》云：“伤官无财可倚，虽巧必贫”是也。

- 分字分词释义：

  - **伤官**：日主所生之气，对官星形成“伤害”，既象征才华外放，也象征对权威的挑战。
  - **伤官见官，祸患百端**：在以官为用的格局中，伤官若直接冲克官星，易生是非与冲突。
  - **伤尽则贵**：若全局无官，伤官纯粹、生财有力，则反能以才华与创造力成就贵格。

- **规范化释义（primary_lang_explained）**：

  伤官格可凶可贵：

  - 若结构得宜、伤尽而又生财，常见才华横溢、敢言敢行之人；

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_169]` `[trigger: 伤官定义]` `[factor_trigger: shangguan_presence AND keguan_zhixing]` `[role: 主干]` 伤官者，我生彼之谓，乃甲见丁、乙见丙之类。 → 《三命通会》卷六#论伤官
  - `[ns_smth_06_170]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_jianguan AND huohuan_baiduan]` `[role: 主干依赖]` 伤官见官，祸患百端。 → 《三命通会》卷六#论伤官
  - `[ns_smth_06_171]` `[trigger: 伤尽则贵]` `[factor_trigger: shangjin_wuguan AND shengcai_weigui]` `[role: 条件分支]` 伤官格务要伤尽，方作贵看。 → 《三命通会》卷六#论伤官
  - `[ns_smth_06_172]` `[trigger: 才气偏锋]` `[factor_trigger: duocaiyi AND aowu_qigao]` `[role: 总结]` 此格主多材艺，傲物气高，心险无忌惮。 → 《三命通会》卷六#论伤官"""
    normalized_text_zh: str = """"""
    subject: str = "伤官与才气之偏锋"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_shangguan', 'bazi_semantic', 'bazi_state_shangguan_9', 'bazi_semantic', 'bazi_condition_factor_206', 'bazi_semantic', 'bazi_state_factor_348', 'bazi_semantic', 'source_ref', 'rel_smth_06_154', 'shangguan_ge', 'rel_smth_06_155', 'shangguan_jianguan', 'rel_smth_06_156', 'caihua_hengyi', 'evi_smth_06_154', 'shangguan_ge', 'rule_shangguan', 'evi_smth_06_155', 'shangguan_jianguan', 'rule_jianguan', 'evi_smth_06_156', 'caihua_hengyi', 'rule_caiyi', 'map_smth_06_103', 'map_smth_06_104']
    
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
        l1_anchor="smth_v1.0.0_伤官与才气之偏锋_001_L1",
    )
    version: str = "1.0.0"
