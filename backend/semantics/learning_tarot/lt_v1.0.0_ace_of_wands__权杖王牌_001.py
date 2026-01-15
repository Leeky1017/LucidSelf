"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008184
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
    semantic_id="lt_v1.0.0_ace_of_wands__权杖王牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AceOfWands权杖王牌(SemanticEntry):
    """
    **Source Text** (Lines 4982-5043): Keywords: Creative Force • Enthusiasm • Confidence • Courage

**E...
    """
    
    original_text: str = """**Source Text** (Lines 4982-5043): Keywords: Creative Force • Enthusiasm • Confidence • Courage

**English Paraphrase**: **Ace of Wands** is "a symbol of possibility in the area of creativity, excitement, adventure, courage, and personal power." When you see this Ace, "be daring and brave—sometimes you have to risk to get what you want."

**Complete Chinese Interpretation**: **权杖王牌**是"在创造力、兴奋、冒险、勇气和个人力量领域的可能性象征"。当你看到这张王牌时，"要勇敢大胆——有时你必须冒险才能得到你想要的。"

**Core Points**: Ace of Wands = creative force, enthusiasm, confidence, courage; Seed of bold enthusiasm; Time of passion beginning

**Narrative Snippets**:
- `[ns_ltt_071]` `[trigger: ace_wands]` `[factor_trigger: tarot_ace_wands]` `[role: 主干]` Ace of Wands shows a seed of bold enthusiasm has been planted. → L5030-5031
- `[ns_ltt_072]` `[trigger: ace_wands_action]` `[factor_trigger: tarot_ace_wands AND tarot_action]` `[role: 主干依赖]` Be daring and brave—sometimes you have to risk to get what you want. → L5036-5037"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Wands (权杖王牌)"
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
        l1_anchor="lt_v1.0.0_ace_of_wands__权杖王牌_001_L1",
    )
    version: str = "1.0.0"
