"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008652
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
    semantic_id="lt_v1.0.0_king_of_cups__圣杯国王_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class KingOfCups圣杯国王(SemanticEntry):
    """
    **Keywords**: Wise • Calm • Diplomatic • Caring • Tolerant

**English Paraphrase**: **King of Cups**...
    """
    
    original_text: str = """**Keywords**: Wise • Calm • Diplomatic • Caring • Tolerant

**English Paraphrase**: **King of Cups** represents emotional leadership—wise, calm, diplomatic, caring, tolerant.

**Complete Chinese Interpretation**: **圣杯国王**代表情感领导力——智慧、冷静、外交、关怀、宽容。

**Narrative Snippets**:
- `[ns_ltt_119]` `[trigger: king_cups]` `[factor_trigger: tarot_king_cups AND tarot_wisdom]` `[role: 主干]` King of Cups navigates emotional currents without being swept away: he feels deeply but responds wisely; his throne floats on turbulent waters yet remains stable—the integration of emotional depth with mature judgment that makes genuine compassion possible."""
    normalized_text_zh: str = """"""
    subject: str = "King of Cups (圣杯国王)"
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
        l1_anchor="lt_v1.0.0_king_of_cups__圣杯国王_001_L1",
    )
    version: str = "1.0.0"
