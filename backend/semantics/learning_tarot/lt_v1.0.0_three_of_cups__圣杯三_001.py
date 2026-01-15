"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008306
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
    semantic_id="lt_v1.0.0_three_of_cups__圣杯三_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class ThreeOfCups圣杯三(SemanticEntry):
    """
    **Source Text** (Lines 5676-5732): Keywords: Exuberance • Friendship • Community

**English Paraphra...
    """
    
    original_text: str = """**Source Text** (Lines 5676-5732): Keywords: Exuberance • Friendship • Community

**English Paraphrase**: **Three of Cups** represents "friendship and community"—celebrating with others, group harmony, shared joy.

**Complete Chinese Interpretation**: **圣杯三**代表"友谊和社区"——与他人庆祝、群体和谐、共同的喜悦。

**Core Points**: Three of Cups = exuberance, friendship, community; Celebrating together; Group joy

**Narrative Snippets**:
- `[ns_ltt_084]` `[trigger: three_cups]` `[factor_trigger: tarot_three_cups]` `[role: 主干]` Three of Cups represents friendship and community celebration. → L5676-5685"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Cups (圣杯三)"
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
        l1_anchor="lt_v1.0.0_three_of_cups__圣杯三_001_L1",
    )
    version: str = "1.0.0"
