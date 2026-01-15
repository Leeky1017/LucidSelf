"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699392
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
    semantic_id="zw_v1.0.0_乐谷之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 乐谷之命(SemanticEntry):
    """
    - 分字分词释义：

  - **贪武同行**：贪狼与武曲同行于命宫或三方，主财武双兼。
  - **左右同宫**：左辅右彼同守命宫，主贵人扶持。
  - **权禄生逢**：生年即逢权星与禄星同会，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **贪武同行**：贪狼与武曲同行于命宫或三方，主财武双兼。
  - **左右同宫**：左辅右彼同守命宫，主贵人扶持。
  - **权禄生逢**：生年即逢权星与禄星同会，主权禄双美。
  - **三方四正羊陀**：命宫三方四正同时见擎羊与陀罗，主声名进退不稳。
  - **破哭劫耗**：破军、天哭、地劫、大耗等凶星聚集，主耗损悲哭。
  - **太岁入命冲照**：太岁星入命宫并与本命形成冲照，激活所有潜在凶象。
  - **阴男水二局**：乐谷命盘的五行局数，水二局主智慧机敏。

- **原文（source_text）**：  
  乐谷之命。阴男水二局。贪武同行，左右同宫，权禄生逢俱吉，柰遇三方四正，俱见羊陀，却空进退声名。大限游于太岁之地，破哭劫耗，流羊、流陀迭并，太岁入命，亦忌冲照，是以死也。

- **规范化释义（primary_lang_explained）**：  
  乐谷命属阴男水二局，贪武同行、左右同宫、权禄生逢俱吉。然三方四正俱见羊陀，声名进退有虚。大限游于太岁之地，破哭劫耗、流羊流陀迭并，太岁入命又忌冲照，故死。

- **完整对等诠释（secondary_lang_full）**：  
  Yue Gu's Yin male Water Second chart has Tan‑Wu same path, Left‑Right same palace, Authority‑Salary at birth—all auspicious. But triplicity‑four‑cardinal all see Blade‑Tuo, fame advances‑retreats uncertain. Major travels to Tai Sui position; Po‑Crying‑Robbery‑Depletion; transiting Blade‑Tuo converge; Tai Sui enters Life with clash. Death.

- **核心要点**：  
  1. 贪武同行、左右同宫、权禄生逢俱吉。  
  2. 三方四正俱见羊陀，声名有虚。  
  3. 大限太岁之地、流羊流陀迭并、太岁冲照，为死亡应期。

- **叙事素材（narrative_snippets）**：
  - **贪武左右**："贪武同行，左右同宫，权禄生逢俱吉"，乐谷命主原局权禄双美、文武皆备。
  - **声名进退**："柰遇三方四正，俱见羊陀，却空进退声名"，三方四正羊陀遍布，使其声望时高时低、难以稳固。
  - **太岁冲命**："大限游于太岁之地，破哭劫耗，流羊、流陀迭并，太岁入命，亦忌冲照，是以死也"，太岁入命配羊陀迭并，为一生凶险最高的年份。
  - **现代应用**：对外在光鲜、内里多是非的命局而言，遇太岁入命且羊陀迭并之年，应避免过度曝光与高调操作，以免在聚光灯下暴露所有破绽。"""
    normalized_text_zh: str = """"""
    subject: str = "乐谷之命"
    factor_refs: list = ['pattern_tanwu_tongxing', 'pattern_zuoyou_tonggong', 'malefic_sanfang_yangtuo', 'timing_liuyang_liutuo', 'timing_taisui_ruminng', 'malefic_pokujihao']
    
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
        l1_anchor="zw_v1.0.0_乐谷之命_001_L1",
    )
    version: str = "1.0.0"
