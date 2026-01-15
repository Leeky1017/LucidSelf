"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008634
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
    semantic_id="lt_v1.0.0_knight_of_cups__圣杯骑士_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KnightOfCups圣杯骑士(SemanticEntry):
    """
    **Keywords**: Romantic • Imaginative • Sensitive • Refined / Overemotional • Fanciful • Temperamenta...
    """
    
    original_text: str = """**Keywords**: Romantic • Imaginative • Sensitive • Refined / Overemotional • Fanciful • Temperamental

**English Paraphrase**: **Knight of Cups** represents romantic quest—imaginative, sensitive, refined. Shadow: overemotional, fanciful.

**Complete Chinese Interpretation**: **圣杯骑士**代表浪漫追求——富有想象力、敏感、精致。阴影面：过度情绪化、异想天开。

**Narrative Snippets**:
- `[ns_ltt_117]` `[trigger: knight_cups]` `[factor_trigger: tarot_knight_cups AND tarot_romance]` `[role: 主干]` Knight of Cups follows the heart's calling with poetic sensitivity: the romantic quester seeking beauty, meaning, and emotional connection; his danger is losing himself in fantasy, preferring the dream to the sometimes disappointing reality of actual relationship."""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Cups (圣杯骑士)"
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
        l1_anchor="lt_v1.0.0_knight_of_cups__圣杯骑士_001_L1",
    )
    version: str = "1.0.0"
