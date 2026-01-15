"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008315
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
    semantic_id="lt_v1.0.0_four_of_cups__圣杯四_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FourOfCups圣杯四(SemanticEntry):
    """
    **Source Text** (Lines 5733-5789): Keywords: Self-Absorption • Apathy • Going Within

**English Para...
    """
    
    original_text: str = """**Source Text** (Lines 5733-5789): Keywords: Self-Absorption • Apathy • Going Within

**English Paraphrase**: **Four of Cups** represents "self-absorption"—being lost in thoughts, apathy, withdrawal, contemplating but not acting.

**Complete Chinese Interpretation**: **圣杯四**代表"自我沉溺"——迷失在思绪中、冷漠、退缩、沉思但不行动。

**Core Points**: Four of Cups = self-absorption, apathy, going within; Contemplative withdrawal; Missing opportunities

**Narrative Snippets**:
- `[ns_ltt_085]` `[trigger: four_cups]` `[factor_trigger: tarot_four_cups]` `[role: 主干]` Four of Cups represents self-absorption and contemplative withdrawal. → L5733-5745"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Cups (圣杯四)"
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
        l1_anchor="lt_v1.0.0_four_of_cups__圣杯四_001_L1",
    )
    version: str = "1.0.0"
