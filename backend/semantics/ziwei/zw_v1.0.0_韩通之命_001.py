"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699311
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
    semantic_id="zw_v1.0.0_韩通之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 韩通之命(SemanticEntry):
    """
    - 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗星，主富贵荣垂。
  - **紫府朝垣**：紫微天府拱照命宫，主终身福厚。
  - **尊居八佐**：左右昌曲齐会，象征辅佐天子、居高位。
...
    """
    
    original_text: str = """- 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗星，主富贵荣垂。
  - **紫府朝垣**：紫微天府拱照命宫，主终身福厚。
  - **尊居八佐**：左右昌曲齐会，象征辅佐天子、居高位。
  - **沉马**：大限到午为沉马，主行动受限。
  - **七杀重逢**：限运再遇七杀，主凶险。
  - **羊陀迭并**：擎羊陀罗齐聚，主凶亡。
  - **阳男水二局**：韩通命盘的五行局数，水二局主智慧武勇。

- **原文（source_text）**：  
  韩通之命。阳男水二局。七杀朝斗，富贵荣垂，紫府朝垣，终身福厚。左右昌曲加会，尊居八佐，八限到午，谓之沉马。太岁地网戊年，卯羊在午，流陀在辰，命垣七杀重逢，羊陀迭并，故死。

- **规范化释义（primary_lang_explained）**：  
  韩通命属阳男水二局，七杀朝斗、紫府朝垣，主富贵荣华、终身福厚。左右昌曲加会，尊居八佐。大限到午为沉马，太岁地网戊年，卯羊在午、流陀在辰，命垣七杀重逢、羊陀迭并，故死。

- **完整对等诠释（secondary_lang_full）**：  
  Han Tong's Yang male Water Second chart has Seven Killings Facing Dipper, Ziwei‑Tianfu Facing Court—wealth and lifelong blessings. Left‑Right Chang‑Qu converge, eight assistants. Major at Wu is Sinking Horse. Tai Sui in Earth Net wu year; Mao Blade at Wu, Tuo at Chen; Life meets Seven Killings again with Blade‑Tuo converge. Death.

- **核心要点**：  
  1. 七杀朝斗、紫府朝垣，主富贵福厚。  
  2. 大限沉马、太岁地网。  
  3. 七杀重逢、羊陀迭并，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **富贵福厚**："七杀朝斗，富贵荣垂，紫府朝垣，终身福厚"，韩通命主富贵显赫、享受终身福厚。
  - **尊居八佐**："左右昌曲加会，尊居八佐"，左右昌曲齐会，象征辅佐天子、居高位之臣。
  - **沉马羊陀**："八限到午，谓之沉马。太岁地网戊年，卯羊在午，流陀在辰，命垣七杀重逢，羊陀迭并，故死"，沉马加羊陀迭并，为寿终之险关。
  - **现代应用**：身处高位且终身顺遂的命局，在沉马加羊陀迭并之年尤须防范突发事故与权力斗争，宜收敛锋芒、减少冒进。"""
    normalized_text_zh: str = """"""
    subject: str = "韩通之命"
    factor_refs: list = ['pattern_qishachongfeng', 'pattern_chenma', 'pattern_yangtuodiebing', 'source_ref', 'rel_hantong_001', 'pattern_qishazifuge', 'rel_hantong_002', 'pattern_chenma', 'rel_hantong_003', 'pattern_yangtuodiebing', 'evi_hantong_001', 'pattern_yangtuodiebing', 'rule_chenma_yangtuo', 'concept_sinking_horse', 'concept_blade_tuo']
    
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
        l1_anchor="zw_v1.0.0_韩通之命_001_L1",
    )
    version: str = "1.0.0"
