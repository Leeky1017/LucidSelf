"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699128
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
    semantic_id="zw_v1.0.0_孙膑之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孙膑之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府朝垣格**：紫微天府拱照命宫的极贵格局。
  - **科权禄三方会合**：化科化权化禄三方会合命宫，主终身富贵。
  - **文昌武曲守命**：文星武星同守命宫，...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府朝垣格**：紫微天府拱照命宫的极贵格局。
  - **科权禄三方会合**：化科化权化禄三方会合命宫，主终身富贵。
  - **文昌武曲守命**：文星武星同守命宫，主文武兼资。
  - **大限天罗**：大限入天罗宫，为晚年凶限。
  - **小限流年相冲**：小限与流年宫位相冲，放大凶象。
  - **终身富贵**：紫府科权禄格局的主要效应。
  - **阳男金四局**：孙膑命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  孙膑之命。阳男金四局。此为紫府朝垣格，左右拱照科权禄三方会合，文昌、武曲守命，兼资文武终身富贵之论。七十五岁，大限入天罗，小限在子，与流年戊午相冲，故凶。

- **规范化释义（primary_lang_explained）**：  
  孙膑命属阳男金四局，紫府朝垣格，左右拱照、科权禄三方会合，文昌武曲守命，主文武兼资、终身富贵。七十五岁大限入天罗，小限在子与流年戊午相冲，凶象叠加而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Sun Bin's Yang male Metal Fourth chart forms Ziwei‑Tianfu Facing Court. Left‑Right flank, Academic‑Authority‑Salary converge triplicity. Wenchang and Wuqu guard Life—dual civil‑martial talents, lifelong wealth. At 75 major enters Heaven Net, minor at Zi clashes wu‑wu year. Malefics cause death.

- **核心要点**：  
  1. 紫府朝垣、左右拱照、科权禄三方会合，主终身富贵。  
  2. 文昌武曲守命，主文武兼资。  
  3. 大限天罗、小限与流年相冲，为晚年寿终应期。

- **叙事素材（narrative_snippets）**：
  - **文武富贵**："紫府朝垣，左右拱照，文昌、武曲守命"，孙膑命主文武兼资、终身富贵。
  - **天罗晚限**："七十五岁，大限入天罗"，提示晚年天罗为人生高危限运节点。
  - **小限冲年**："小限在子，与流年戊午相冲"，小限与流年相冲放大凶象，应事多在行军、决策与身体机能上。
  - **现代应用**：身处高压行业或决策岗位者，在晚年遇到天罗加岁限冲照组合时，更需关注血压、心脑血管与突发事故风险。"""
    normalized_text_zh: str = """"""
    subject: str = "孙膑之命"
    factor_refs: list = ['star_wenchangwuqu', 'pattern_kequanlu', 'pattern_xiaoxianchong', 'source_ref', 'rel_sunbin_001', 'pattern_zifuchaoyuan', 'rel_sunbin_002', 'star_wenchangwuqu', 'rel_sunbin_003', 'pattern_tianluo', 'evi_sunbin_001', 'pattern_tianluo', 'rule_tianluo_chong', 'concept_civil_martial', 'concept_heaven_net']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_孙膑之命_001_L1",
    )
    version: str = "1.0.0"
