"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008708
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
    semantic_id="lt_v1.0.0_knight_of_pentacles__星币骑士_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KnightOfPentacles星币骑士(SemanticEntry):
    """
    **Keywords**: Unwavering • Cautious • Thorough • Realistic / Stubborn • Unadventurous • Obsessive • ...
    """
    
    original_text: str = """**Keywords**: Unwavering • Cautious • Thorough • Realistic / Stubborn • Unadventurous • Obsessive • Pessimistic

**English Paraphrase**: **Knight of Pentacles** represents steady practical action—unwavering, cautious, thorough. Shadow: stubborn, pessimistic.

**Complete Chinese Interpretation**: **星币骑士**代表稳定的实际行动——坚定、谨慎、彻底。阴影面：固执、悲观。

**Narrative Snippets**:
- `[ns_ltt_125]` `[trigger: knight_pentacles]` `[factor_trigger: tarot_knight_pentacles AND tarot_persistence]` `[role: 主干]` Knight of Pentacles alone among knights sits motionless on his horse: progress through steady persistence rather than dramatic action; the tortoise who beats the hare—his apparent slowness masks deep reliability and eventual success through sheer endurance."""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Pentacles (星币骑士)"
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
        l1_anchor="lt_v1.0.0_knight_of_pentacles__星币骑士_001_L1",
    )
    version: str = "1.0.0"
