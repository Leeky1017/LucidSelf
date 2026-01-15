"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699095
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
    semantic_id="zw_v1.0.0_子产之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 子产之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府朝垣**：紫微天府拱照命宫的极贵格局。
  - **左辅文昌加会**：左辅与文昌同会命宫，主富贵名扬。
  - **沉马**：天马星陷落或行不利宫位，为晚年凶象。...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府朝垣**：紫微天府拱照命宫的极贵格局。
  - **左辅文昌加会**：左辅与文昌同会命宫，主富贵名扬。
  - **沉马**：天马星陷落或行不利宫位，为晚年凶象。
  - **地网逢忌**：限运入地网宫又逢化忌，诸凶叠加。
  - **君名题扬**：名誉远播、感动君王。
  - **一生富贵**：紫府朝垣格局的主要效应。
  - **阴男金四局**：子产命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  子产之命。阴男金四局。紫府朝垣，左辅文昌加曾，一生富贵，君名题扬。大限沉马，小限六十四入地网逢忌，故凶而死。

- **规范化释义（primary_lang_explained）**：  
  子产命属阴男金四局，紫府朝垣、左辅文昌加会，主一生富贵名扬。然大限行沉马之地，小限六十四入地网逢忌，凶象叠加而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zi Chan's Yin male Metal Fourth chart forms Ziwei‑Tianfu Facing Court with Left Assistant and Wenchang—lifelong wealth and fame. Major period in Sinking Horse; minor at 64 enters Earth Net with taboo. Malefics converge, causing death.

- **核心要点**：  
  1. 紫府朝垣、左辅文昌加会，主富贵名扬。  
  2. 大限沉马、小限地网逢忌，为晚年凶象。  
  3. 六十四岁凶象叠加，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **富贵名扬**："紫府朝垣，左辅文昌加会，一生富贵君名题扬"，子产命主富贵名扬。
  - **沉马地网**："大限沉马，小限入地网逢忌"，晚年凶象叠加。
  - **现代应用**：富贵之命须关注晚年限运——沉马、地网逢忌为高危组合。"""
    normalized_text_zh: str = """"""
    subject: str = "子产之命"
    factor_refs: list = ['pattern_zifuchaoyuan', 'star_chenma', 'pattern_diwangji', 'source_ref', 'rel_zichan_001', 'pattern_zifuchaoyuan', 'rel_zichan_002', 'star_chenma', 'rel_zichan_003', 'pattern_diwangji', 'evi_zichan_001', 'pattern_diwangji', 'rule_chenma_diwang', 'concept_horse_debility', 'concept_earth_net']
    
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
        l1_anchor="zw_v1.0.0_子产之命_001_L1",
    )
    version: str = "1.0.0"
