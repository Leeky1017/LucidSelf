"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699301
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
    semantic_id="zw_v1.0.0_刘伶之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 刘伶之命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右同垣**：左辅右彼同在命宫，主贵格。
  - **坐贵向贵**：命宫坐贵又向贵人，主极贵。
  - **生处带空**：生时带天空，如半天折翅，福禄不全。
  - ...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右同垣**：左辅右彼同在命宫，主贵格。
  - **坐贵向贵**：命宫坐贵又向贵人，主极贵。
  - **生处带空**：生时带天空，如半天折翅，福禄不全。
  - **身宫怯劫**：身宫有地劫无正曜，主身体受损。
  - **劫空会挠**：地劫天空会聚而挠，主凶亡。
  - **半天折翅**：比喻贵格有空，难以全展其才。
  - **阳男水二局**：刘伶命盘的五行局数，水二局主智慧放荡。

- **原文（source_text）**：  
  刘伶之命。阳男水二局。虽有左右同垣，坐贵向贵之局，生处带空，犹如半天折翅。且身宫怯劫，并无正曜。卅二岁，大限行巳宫，小限亦到巳，太岁相冲，劫空正会挠，故死子。其年。

- **规范化释义（primary_lang_explained）**：  
  刘伶命属阳男水二局，左右同垣、坐贵向贵，然生处带空如半天折翅，身宫怯劫无正曜。三十二岁大小限皆到巳，太岁相冲，劫空正会挠，故死于其年。

- **完整对等诠释（secondary_lang_full）**：  
  Liu Ling's Yang male Water Second chart has Left‑Right same court, sitting‑facing noble. But birth with Void—like broken wing mid‑sky. Body palace fears Robbery, no main star. At 32 both periods at Si, Tai Sui clashes, Robbery‑Void directly obstruct. Death that year.

- **核心要点**：  
  1. 左右同垣、坐贵向贵，然生处带空。  
  2. 身宫怯劫无正曜。  
  3. 大小限到巳、太岁冲、劫空会挠，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **半天折翅**："虽有左右同垣，坐贵向贵之局，生处带空，犹如半天折翅"，刘伶命局示意贵格有空，难以全展其才。
  - **身宫怯劫**："且身宫怯劫，并无正曜"，身宫地劫无正曜，使身体与行动力常受牵制。
  - **巳地会挠**："卅二岁，大限行巳宫，小限亦到巳，太岁相冲，劫空正会挠"，大小限同到巳宫又被劫空会挠，为命终时刻。
  - **现代应用**：有“半天折翅”倾向的命局，在重要年份避免自我消耗型生活方式（酗酒、过度放纵等），以免加重本就脆弱的身心结构。"""
    normalized_text_zh: str = """"""
    subject: str = "刘伶之命"
    factor_refs: list = ['metaphor_bantianzhezhi', 'pattern_shengongqiejie', 'pattern_jiekonghuinao', 'source_ref', 'rel_liuling_001', 'pattern_zuoyouguige', 'rel_liuling_002', 'metaphor_bantianzhezhi', 'rel_liuling_003', 'pattern_jiekonghuinao', 'evi_liuling_001', 'pattern_jiekonghuinao', 'rule_jiekong_huinao', 'concept_broken_wing', 'concept_body_robbery']
    
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
        l1_anchor="zw_v1.0.0_刘伶之命_001_L1",
    )
    version: str = "1.0.0"
