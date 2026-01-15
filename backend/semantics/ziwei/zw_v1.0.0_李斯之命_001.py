"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699236
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
    semantic_id="zw_v1.0.0_李斯之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 李斯之命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右同宫**：左辅右彼同在一宫，主辅佐之力。
  - **日己月酉并明**：太阳在己宫、太阴在酉宫皆明，主文明显达。
  - **权禄加会**：化权化禄同会命宫，主富...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右同宫**：左辅右彼同在一宫，主辅佐之力。
  - **日己月酉并明**：太阳在己宫、太阴在酉宫皆明，主文明显达。
  - **权禄加会**：化权化禄同会命宫，主富贵。
  - **丧门白虎冲命**：流年丧门白虎冲照命宫，主凶事。
  - **富贵之命**：左右日月权禄格局的主要效应。
  - **见凶**：太岁丧门白虎冲命的最终结局。
  - **阳男土五局**：李斯命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  李斯之命。阳男土五局。左右同宫，日已月酉并明，权禄加会，为富贵之命。太岁丧门、白虎冲命限，是以见凶。

- **规范化释义（primary_lang_explained）**：  
  李斯命属阳男土五局，左右同宫、日巳月酉并明、权禄加会，主富贵之命。然太岁丧门、白虎冲命限，故见凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Li Si's Yang male Earth Fifth chart has Left‑Right same palace, Sun in Si Moon in You both bright, Authority‑Salary converge—wealth and honour. Tai Sui with Mourning Gate and White Tiger clash Life period. Hence death.

- **核心要点**：  
  1. 左右同宫、日月并明、权禄加会，主富贵。  
  2. 太岁丧门白虎冲命限，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **富贵之命**："左右同宫，日已月酉并明，权禄加会，为富贵之命"，李斯命主位高权重、富贵显赫。
  - **丧门白虎**："太岁丧门、白虎冲命限，是以见凶"，丧门配白虎冲命，为刑戮、狱祸之典型星象组合。
  - **现代应用**：掌权者在丧门白虎冲命的年份，应极力避免卷入政治清算与重大司法案件，谨言慎行，以免富贵反成祸源。"""
    normalized_text_zh: str = """"""
    subject: str = "李斯之命"
    factor_refs: list = ['pattern_riyuebingming', 'star_baihuchongming', 'star_sangmenchongxian', 'source_ref', 'rel_lisi_001', 'pattern_zuoyouquanlu', 'rel_lisi_002', 'star_sangmenbaihu', 'evi_lisi_001', 'star_sangmenbaihu', 'rule_sangmenbaihu', 'concept_sun_moon', 'concept_white_tiger']
    
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
        l1_anchor="zw_v1.0.0_李斯之命_001_L1",
    )
    version: str = "1.0.0"
