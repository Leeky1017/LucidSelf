"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008355
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
    semantic_id="lt_v1.0.0_eight_of_cups__圣杯八_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class EightOfCups圣杯八(SemanticEntry):
    """
    **Source Text** (Lines 5961-6017): Keywords: Deeper Meaning • Moving On • Weariness

**English Parap...
    """
    
    original_text: str = """**Source Text** (Lines 5961-6017): Keywords: Deeper Meaning • Moving On • Weariness

**English Paraphrase**: **Eight of Cups** represents "moving on"—seeking deeper meaning, leaving behind the familiar, spiritual quest.

**Complete Chinese Interpretation**: **圣杯八**代表"继续前进"——寻求更深的意义、离开熟悉的、灵性追求。

**Core Points**: Eight of Cups = deeper meaning, moving on, weariness; Spiritual quest; Leaving behind

**Narrative Snippets**:
- `[ns_ltt_089]` `[trigger: eight_cups]` `[factor_trigger: tarot_eight_cups]` `[role: 主干]` Eight of Cups represents moving on to seek deeper meaning. → L5961-5970"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Cups (圣杯八)"
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
        l1_anchor="lt_v1.0.0_eight_of_cups__圣杯八_001_L1",
    )
    version: str = "1.0.0"
