"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008679
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
    semantic_id="lt_v1.0.0_queen_of_swords__宝剑王后_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class QueenOfSwords宝剑王后(SemanticEntry):
    """
    **Keywords**: Honest • Astute • Forthright • Witty • Experienced

**English Paraphrase**: **Queen of...
    """
    
    original_text: str = """**Keywords**: Honest • Astute • Forthright • Witty • Experienced

**English Paraphrase**: **Queen of Swords** represents mature mental mastery—honest, astute, forthright, witty, experienced.

**Complete Chinese Interpretation**: **宝剑王后**代表成熟的思维掌控——诚实、精明、直率、机智、有经验。

**Narrative Snippets**:
- `[ns_ltt_122]` `[trigger: queen_swords]` `[factor_trigger: tarot_queen_swords AND tarot_discernment]` `[role: 主干]` Queen of Swords has earned her clarity through loss: experience has taught her what matters and what is pretense; her incisive perception cuts through sentimentality, offering truth even when it hurts—the wisdom of one who will not be fooled again."""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Swords (宝剑王后)"
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
        l1_anchor="lt_v1.0.0_queen_of_swords__宝剑王后_001_L1",
    )
    version: str = "1.0.0"
