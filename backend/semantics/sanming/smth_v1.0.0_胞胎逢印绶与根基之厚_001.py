"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412734
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
    semantic_id="smth_v1.0.0_胞胎逢印绶与根基之厚_001",
    book_id="sanming",
    engine_id="bazi"
)
class 胞胎逢印绶与根基之厚(SemanticEntry):
    """
    - **原文（source_text）**：

  胞胎逢印绶：《经》云：胞胎逢印绶，禄享千锺。如庚寅、辛卯、丙申、乙酉等，日时月令逢印绶之地，主贵。《经》云：时日胞胎格，月通印绶，逢煞官印运助，职位...
    """
    
    original_text: str = """- **原文（source_text）**：

  胞胎逢印绶：《经》云：胞胎逢印绶，禄享千锺。如庚寅、辛卯、丙申、乙酉等，日时月令逢印绶之地，主贵。《经》云：时日胞胎格，月通印绶，逢煞官印运助，职位列三公。

- 分字分词释义：

  - **胞胎**：指日时或日月之间的生扶关系，如日主处于长生、养、胎等位。
  - **胞胎逢印绶**：在这些“初生阶段”的位置上，又遇见印星之地，象征根基深厚、资源充沛。

- **规范化释义（primary_lang_explained）**：

  胞胎逢印绶，着重强调“起点”与“根本”：

  - 出生环境、家庭支持、学历教育等方面，往往占据相对优势；
  - 在同等努力条件下，更容易获得职位与待遇。

- 核心要点：

  - 这是印绶格中偏重**起点与基础**的一个特例。
  - 真正能达“三公”之贵仍需行官印吉运，并有相匹配的时代与环境。

- 详细解说：

  在阅读此类条文时，需要避免“看到一句‘职位列三公’就直接套用”。更合理的做法是：

  - 将其理解为“在同辈中竞争起点较高、资源较厚”；
  - 再结合具体时代、行业与个人抉择，判断现实可达的层级。

- **校勘与字词辨析（双语）**：

  - “禄享千锺”“职位列三公”等语，本稿统归于古代对高官厚禄的夸饰写法，在白话中均以“职位优渥、待遇不薄”概括。
  - **English**：
    - Phrases like "salary of a thousand zhong" and "rank among the Three Dukes" are treated as classical hyperbole for high office; summarized in vernacular as "comfortable position, well compensated."

  - “弃祖基而自创别业”一语，本稿理解为事业路径的转向，而非简单的断绝家族关系。
  - **English**：
    - Not simply breaking family ties; nuanced interpretation provided.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_149]` `[trigger: 胞胎逢印]` `[factor_trigger: paotai_fengyin AND genji_houzhong]` `[role: 主干]` 胞胎逢印纶，禄享千锲。如庚寅、辛卯、丙申、乙酉等，日时月令逢印纶之地，主贵。 → 《三命通会》卷六#胞胎逢印纶
  - `[ns_smth_06_150]` `[trigger: 起点优越]` `[factor_trigger: tongban_qidian AND ziyuan_youshi]` `[role: 主干依赖]` 在同辈中竞争起点较高、资源较厚。 → 《三命通会》卷六#胞胎逢印纶
  - `[ns_smth_06_151]` `[trigger: 职位列三公]` `[factor_trigger: yuetong_yinshou AND guanyinyun]` `[role: 条件分支]` 时日胞胎格，月通印纶，逢煚官印运助，职位列三公。 → 《三命通会》卷六#胞胎逢印纶
  - `[ns_smth_06_152]` `[trigger: 根基之厚]` `[factor_trigger: chuusheng_huanjing AND jiating_zhichi]` `[role: 总结]` 胞胎逢印纶着重强调“起点”与“根本”。 → 《三命通会》卷六#胞胎逢印纶"""
    normalized_text_zh: str = """"""
    subject: str = "胞胎逢印绶与根基之厚"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_39', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_27', 'bazi_semantic', 'bazi_state_factor_29', 'bazi_semantic', 'bazi_condition_month_command_degree', 'bazi_semantic', 'bazi_condition_factor_200', 'bazi_semantic', 'source_ref', 'rel_smth_06_139', 'paotai_fengyinshou_presence', 'rel_smth_06_140', 'genji_shenhou', 'rel_smth_06_141', 'yueling_tongyin', 'evi_smth_06_139', 'paotai_fengyinshou_presence', 'rule_paotai', 'evi_smth_06_140', 'genji_shenhou', 'rule_genji', 'evi_smth_06_141', 'shaguanyin_yun', 'rule_shunyun', 'map_smth_06_093', 'map_smth_06_094']
    
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
        l1_anchor="smth_v1.0.0_胞胎逢印绶与根基之厚_001_L1",
    )
    version: str = "1.0.0"
