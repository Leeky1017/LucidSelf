"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008847
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
    semantic_id="lt_v1.0.0_lesson_13__aces__王牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson13Aces王牌(SemanticEntry):
    """
    **Source Text** (Lines 1320-1372): Each Ace represents qualities of suit in purest form. Aces are po...
    """
    
    original_text: str = """**Source Text** (Lines 1320-1372): Each Ace represents qualities of suit in purest form. Aces are portals between realms of major and minor arcanas.

**English Paraphrase**: Each **Ace** "represents the qualities of its suit in their purest form" and "stands out from other cards as if in a circle of its own light." Aces are "portals between the realms of the major and minor arcanas. They allow powerful but impersonal forces to come into your life."

**Complete Chinese Interpretation**: 每张**王牌**"以最纯粹的形式代表其花色的品质"，并"从其他牌中脱颖而出，仿佛在自己的光圈中。"王牌是"大小阿卡纳领域之间的门户。它们允许强大但非个人化的力量进入你的生活。"

**The Four Aces**:
- **Ace of Wands**: Gift of creativity, enthusiasm, courage, confidence
- **Ace of Cups**: Gift of emotion, intuition, intimacy, love
- **Ace of Swords**: Gift of mental clarity, truth, justice, fortitude
- **Ace of Pentacles**: Gift of prosperity, practicality, security, manifestation

**Ace = Portals**: "Allow powerful but impersonal forces to come into your life"
**Ace = Seed of Possibility**: "Will grow given your attention and care"
**Ace = Window of Opportunity**: "Pay attention so you don't miss it"

**Narrative Snippets**:
- `[ns_ltt_143]` `[trigger: aces_portals]` `[factor_trigger: tarot_aces]` `[role: 主干]` Aces are portals between major and minor arcanas, allowing powerful forces in. → L1355-1358
- `[ns_ltt_144]` `[trigger: aces_gifts]` `[factor_trigger: tarot_aces AND tarot_potential]` `[role: 辅助]` Each Ace presents a gift from the mysterious source: the hand emerging from clouds offers raw elemental potential; whether Fire, Water, Air, or Earth, the gift is both opportunity and responsibility—potential requires cultivation."""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 13: Aces (王牌)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_lesson_13__aces__王牌_001_L1",
    )
    version: str = "1.0.0"
