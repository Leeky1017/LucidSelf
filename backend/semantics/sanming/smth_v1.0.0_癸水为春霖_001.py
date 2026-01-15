"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042620
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
    semantic_id="smth_v1.0.0_癸水为春霖_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸水为春霖(SemanticEntry):
    """
    - **原文（source_text）**：
  癸水为春霖。癸水生卯月，号曰春霖，盖阴木得雨而发生也。然至申则死，七八月多干旱也。且卯前一位是辰，辰为龙宫，卯近龙宫而水生，龙一奋遂化为雨焉；卯为雷门...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸水为春霖。癸水生卯月，号曰春霖，盖阴木得雨而发生也。然至申则死，七八月多干旱也。且卯前一位是辰，辰为龙宫，卯近龙宫而水生，龙一奋遂化为雨焉；卯为雷门，雷一震而龙必兴焉，观此则癸水其春霖矣。如癸卯日透出己字者，有云行雨施之象，其人必有经济才也。春夏吉，秋冬不吉。

- **分字分词释义**：
  - **春霖**：连绵春雨，重在滋养与渗透。
  - **卯为雷门、辰为龙宫**：雷震龙兴，喻水化雨之机。
  - **云行雨施**：形容调度资源、普惠众生之象。

- **规范化释义（primary_lang_explained）**：
  癸水喻为春霖：生于卯月，适逢阴木萌发，连绵春雨最利其生。卯前之辰为龙宫，卯为雷门，雷震龙起则云行雨施，正是癸水化霖之象。至申则死，七八月多干旱，春霖之功告尽。癸卯日又透己土者，如云行雨施，有统筹资源、泽被众人的才干；多利春夏，不利秋冬。

- **完整对等诠释（secondary_lang_full）**：
  Gui Water is likened to long spring rains. Born in Mao month when yin Wood is sprouting, it does its best work as a gentle, continuous drizzle that soaks the soil and allows tender roots to take hold. Chen, the “dragon palace”, and Mao, the “gate of thunder”, describe the mechanism by which stored water and rising qi turn into clouds and then into life‑giving rain: when thunder stirs the dragon, Gui spreads out as cloud and falls as widespread moisture. By the time the qi has shifted to Shen and the seventh and eighth months, this function is exhausted and drought is more common. A Gui‑Mao day with Ji Earth visible shows the classic “cloud travelling and rain being dispensed” pattern, associated with the ability to allocate resources and extend benefit to many. Such charts favour spring and summer, when there is something to feed; in autumn and winter the same rain can become cold dampness or wasted effort. Interpreting Gui as spring rain thus highlights sustained support and provisioning rather than dramatic surges."""
    normalized_text_zh: str = """"""
    subject: str = "癸水为春霖"
    factor_refs: list = []
    
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
        l1_anchor="smth_v1.0.0_癸水为春霖_001_L1",
    )
    version: str = "1.0.0"
