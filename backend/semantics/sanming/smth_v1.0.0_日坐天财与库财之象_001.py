"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412691
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
    semantic_id="smth_v1.0.0_日坐天财与库财之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 日坐天财与库财之象(SemanticEntry):
    """
    - **原文（source_text）**：

  日坐天财：如戊己土克水为财，水墓辰是也。古歌云：年干克下是天财，克墓之乡正库开，财入库时多谷帛，家豪金物积成堆。如毕状元己巳、癸酉、庚辰、甲申是也。...
    """
    
    original_text: str = """- **原文（source_text）**：

  日坐天财：如戊己土克水为财，水墓辰是也。古歌云：年干克下是天财，克墓之乡正库开，财入库时多谷帛，家豪金物积成堆。如毕状元己巳、癸酉、庚辰、甲申是也。

- 分字分词释义：

  - **日坐天财**：日干在日支上直接坐库中之财，如戊己见辰水墓为财库。
  - **年干克下是天财**：年干克年支，年支为财库，象征先天或祖上的“库财”。
  - **克墓之乡正库开**：克到墓库之地，如同打开仓库，财入库而可积累。

- **规范化释义（primary_lang_explained）**：

  日坐天财，多主“库中有财”、基础稳厚。与一般流通之财不同，天财偏重于：

  - 祖上累积的资产或资源；
  - 需要特定契机（运程、职责）才能真正启动的大额资源。

  若命局有能力“开库而不泄库”，则此类配置常对应家道殷实、资产厚重；若反之，库被冲破、比劫重重，则易出现“家有资产但难以守成”的局面。

- 核心要点：

  - 日坐天财重在**库财与先天基础**，非即时流通之小利。
  - 需结合年柱、月柱与行运，判断“何时开库、如何开库”。
  - 忌重冲重劫、反复启用，以免“开一次、亏一次”。

- 详细解说：

  实占时，见日坐天财，不可立刻断人为“大富翁”，而应询问：

  - 是否有家族资产、产业或隐藏资源；
  - 本人是否具备管理与承接的能力；
  - 岁运是否在合宜的时间点触动此库。如果个人能力与行运不足，即便库中有物，也可能“看得到、用不到”，甚至因管理不善而招致纷争。

- **校勘与字词辨析（双语）**：

  - 原文举毕状元一造，本稿仅以“库财厚重、家豪金物”概括其象，不逐条推断科名与官阶。
  - **English**：
    - Examination ranks and official grades not inferred clause by clause.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_133]` `[trigger: 日坐天财]` `[factor_trigger: rizuo_caiku AND kucai_zhixiang]` `[role: 主干]` 日坐天财，如戊己土克水为财，水墓辰是也。 → 《三命通会》卷六#日坐天财
  - `[ns_smth_06_134]` `[trigger: 克墓库开]` `[factor_trigger: kemu_zhixiang AND zhengku_kai]` `[role: 主干依赖]` 年干克下是天财，克墓之乡正库开。 → 《三命通会》卷六#日坐天财
  - `[ns_smth_06_135]` `[trigger: 财入库]` `[factor_trigger: cai_ruku AND duogubo]` `[role: 条件分支]` 财入库时多谷帛，家豪金物积成堆。 → 《三命通会》卷六#日坐天财
  - `[ns_smth_06_136]` `[trigger: 库财厉厚]` `[factor_trigger: kucai_houzhong AND jichu_wenjian]` `[role: 总结]` 日坐天财重在库财与先天基础，非即时流通之小利。 → 《三命通会》卷六#日坐天财"""
    normalized_text_zh: str = """"""
    subject: str = "日坐天财与库财之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_35', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_23', 'bazi_semantic', 'bazi_state_degree_24', 'bazi_semantic', 'bazi_condition_factor_193', 'bazi_semantic', 'bazi_condition_factor_194', 'bazi_semantic', 'source_ref', 'rel_smth_06_127', 'rizuo_tiancai_presence', 'rel_smth_06_128', 'kukai_chengdu', 'rel_smth_06_129', 'niangan_kexia', 'evi_smth_06_127', 'rizuo_tiancai_presence', 'rule_zuoku', 'evi_smth_06_128', 'kukai_chengdu', 'rule_kukai', 'evi_smth_06_129', 'cairuku_chengdu', 'rule_ruku', 'map_smth_06_085', 'map_smth_06_086']
    
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
        l1_anchor="smth_v1.0.0_日坐天财与库财之象_001_L1",
    )
    version: str = "1.0.0"
