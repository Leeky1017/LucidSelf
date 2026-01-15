"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008474
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
    semantic_id="lt_v1.0.0_ten_of_swords__宝剑十_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TenOfSwords宝剑十(SemanticEntry):
    """
    **Source Text** (Lines 6650-6706): Keywords: Bottoming Out • Victim Mentality • Martyrdom

**English...
    """
    
    original_text: str = """**Source Text** (Lines 6650-6706): Keywords: Bottoming Out • Victim Mentality • Martyrdom

**English Paraphrase**: **Ten of Swords** represents "bottoming out"—hitting rock bottom, victim mentality, the darkest hour before dawn.

**Complete Chinese Interpretation**: **宝剑十**代表"触底"——跌入谷底、受害者心态、黎明前最黑暗的时刻。

**Core Points**: Ten of Swords = bottoming out, victim, martyrdom; Rock bottom; Darkest before dawn

**Narrative Snippets**:
- `[ns_ltt_101]` `[trigger: ten_swords]` `[factor_trigger: tarot_ten_swords]` `[role: 主干]` Ten of Swords represents hitting rock bottom—darkest before dawn. → L6650-6660"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Swords (宝剑十)"
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
        l1_anchor="lt_v1.0.0_ten_of_swords__宝剑十_001_L1",
    )
    version: str = "1.0.0"
