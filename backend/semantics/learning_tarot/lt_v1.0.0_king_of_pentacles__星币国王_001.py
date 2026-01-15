"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008726
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
    semantic_id="lt_v1.0.0_king_of_pentacles__星币国王_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KingOfPentacles星币国王(SemanticEntry):
    """
    **Keywords**: Enterprising • Adept • Reliable • Supporting • Steady

**English Paraphrase**: **King ...
    """
    
    original_text: str = """**Keywords**: Enterprising • Adept • Reliable • Supporting • Steady

**English Paraphrase**: **King of Pentacles** represents practical leadership—enterprising, adept, reliable, supporting, steady.

**Complete Chinese Interpretation**: **星币国王**代表实践领导力——有进取心、熟练、可靠、支持、稳定。

**Narrative Snippets**:
- `[ns_ltt_127]` `[trigger: king_pentacles]` `[factor_trigger: tarot_king_pentacles AND tarot_prosperity]` `[role: 主干]` King of Pentacles has built empire through patient accumulation: wealth as crystallized competence, success as proof of reliable judgment; his authority comes from demonstrated results rather than inherited position or theoretical knowledge."""
    normalized_text_zh: str = """"""
    subject: str = "King of Pentacles (星币国王)"
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
        l1_anchor="lt_v1.0.0_king_of_pentacles__星币国王_001_L1",
    )
    version: str = "1.0.0"
