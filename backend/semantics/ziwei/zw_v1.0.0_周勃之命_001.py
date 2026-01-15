"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699383
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
    semantic_id="zw_v1.0.0_周勃之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 周勃之命(SemanticEntry):
    """
    - 分字分词释义：

  - **太阴天同居子**：太阴天同同守子宫，为福星聚会的上等命格。
  - **丙丁人富贵忠良**：丙丁年生人逢此格，主富贵忠良。
  - **权禄生逢**：生年即逢权星与禄...
    """
    
    original_text: str = """- 分字分词释义：

  - **太阴天同居子**：太阴天同同守子宫，为福星聚会的上等命格。
  - **丙丁人富贵忠良**：丙丁年生人逢此格，主富贵忠良。
  - **权禄生逢**：生年即逢权星与禄星同会，主出将入相。
  - **大限巳宫逢陀罗**：大限行至巳宫又逢陀罗，主凶险。
  - **巳生忌本身临**：巳年生人大限行至巳宫，形成生年与限运重叠之忌。
  - **地劫天哭作挠**：地劫天哭同会，主基础被侵蚀与悲哭之事。
  - **阴男木三局**：周勃命盘的五行局数，木三局主生发忠勇。

- **原文（source_text）**：  
  周勃之命。阴男木三局。太阴天同，居子守命，丙丁人富贵忠良，权禄生逢入将出相之命。大限到于巳宫，又逢陀罗，且已生人切忌本身临，又太岁地劫天哭星作挠，是以凶也。

- **规范化释义（primary_lang_explained）**：  
  周勃命属阴男木三局，太阴天同居子守命，丙丁人主富贵忠良，权禄生逢为出将入相之命。大限到巳宫逢陀罗，巳生人切忌本身临，太岁地劫天哭作挠，故凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zhou Bo's Yin male Wood Third chart has Taiyin‑Tiantong at Zi guarding Life—bing‑ding natives rich, loyal. Authority‑Salary at birth, general‑minister destiny. Major at Si meets Tuo; Si natives should avoid; Tai Sui with Robbery‑Crying obstruct. Death.

- **核心要点**：  
  1. 太阴天同居子，丙丁人富贵忠良。  
  2. 权禄生逢，出将入相。  
  3. 大限巳宫陀罗、巳生忌本身临、地劫天哭，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **忠良之将**："太阴天同，居子守命，丙丁人富贵忠良，权禄生逢入将出相之命"，周勃命主以忠勇之姿，出将入相、安社稷。
  - **巳宫凶限**："大限到于巳宫，又逢陀罗"，巳宫逢陀罗象征功成之后仍有潜在危机。
  - **地劫天哭**："且已生人切忌本身临，又太岁地劫天哭星作挠，是以凶也"，地劫天哭加生年忌临，为兵权功过被清算之象。
  - **现代应用**：居功至伟的武将或高管，在陀罗加地劫天哭之年的权力交接期，应学会急流勇退，避免被卷入"秋后算账"。"""
    normalized_text_zh: str = """"""
    subject: str = "周勃之命"
    factor_refs: list = ['pattern_taiyintiantongzi', 'pattern_quanlu_shengfeng', 'timing_sigong_tuoluo', 'malefic_dijie_tianku', 'taboo_sisheng_benshenlin']
    
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
        l1_anchor="zw_v1.0.0_周勃之命_001_L1",
    )
    version: str = "1.0.0"
