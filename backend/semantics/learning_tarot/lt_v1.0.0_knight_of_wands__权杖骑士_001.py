"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008592
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
    semantic_id="lt_v1.0.0_knight_of_wands__权杖骑士_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KnightOfWands权杖骑士(SemanticEntry):
    """
    **Keywords**: Charming • Self-Confident • Daring • Adventurous / Superficial • Cocky • Foolhardy • R...
    """
    
    original_text: str = """**Keywords**: Charming • Self-Confident • Daring • Adventurous / Superficial • Cocky • Foolhardy • Restless

**English Paraphrase**: **Knight of Wands** represents action with confidence—charming, daring, adventurous. Shadow: superficial, cocky, foolhardy.

**Complete Chinese Interpretation**: **权杖骑士**代表自信的行动——迷人、大胆、冒险。阴影面：肤浅、自大、鲁莽。

**Narrative Snippets**:
- `[ns_ltt_113]` `[trigger: knight_wands]` `[factor_trigger: tarot_knight_wands AND tarot_action]` `[role: 主干]` Knight of Wands charges forward with infectious confidence: action precedes thought, charm opens doors that planning cannot; the danger lies in scattering energy across too many adventures, leaving none completed."""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Wands (权杖骑士)"
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
        l1_anchor="lt_v1.0.0_knight_of_wands__权杖骑士_001_L1",
    )
    version: str = "1.0.0"
