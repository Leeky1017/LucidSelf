"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008670
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
    semantic_id="lt_v1.0.0_knight_of_swords__宝剑骑士_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KnightOfSwords宝剑骑士(SemanticEntry):
    """
    **Keywords**: Direct • Authoritative • Incisive • Knowledgeable / Blunt • Overbearing • Cutting • Op...
    """
    
    original_text: str = """**Keywords**: Direct • Authoritative • Incisive • Knowledgeable / Blunt • Overbearing • Cutting • Opinionated

**English Paraphrase**: **Knight of Swords** represents direct mental action—authoritative, incisive, knowledgeable. Shadow: blunt, overbearing.

**Complete Chinese Interpretation**: **宝剑骑士**代表直接的思维行动——权威、敏锐、博学。阴影面：直率、专横。

**Narrative Snippets**:
- `[ns_ltt_121]` `[trigger: knight_swords]` `[factor_trigger: tarot_knight_swords AND tarot_action]` `[role: 主干]` Knight of Swords charges into intellectual battle with fierce directness: words as weapons, arguments as conquest; effective against confusion but potentially destructive to relationship—truth without mercy can be more harmful than diplomatic silence."""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Swords (宝剑骑士)"
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
        l1_anchor="lt_v1.0.0_knight_of_swords__宝剑骑士_001_L1",
    )
    version: str = "1.0.0"
