"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008625
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
    semantic_id="lt_v1.0.0_page_of_cups__圣杯侍从_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class PageOfCups圣杯侍从(SemanticEntry):
    """
    **Keywords**: Be Emotional • Be Intuitive • Be Intimate • Be Loving

**English Paraphrase**: **Page ...
    """
    
    original_text: str = """**Keywords**: Be Emotional • Be Intuitive • Be Intimate • Be Loving

**English Paraphrase**: **Page of Cups** represents youthful emotional sensitivity—being intuitive, intimate, loving.

**Complete Chinese Interpretation**: **圣杯侍从**代表年轻的情感敏感性——直觉、亲密、有爱。

**Narrative Snippets**:
- `[ns_ltt_116]` `[trigger: page_cups]` `[factor_trigger: tarot_page_cups AND tarot_intuition]` `[role: 主干]` Page of Cups gazes at the fish emerging from the cup with wonder rather than fear: openness to emotional and psychic impressions, willingness to receive messages from the unconscious; the beginning of intuitive development before defenses harden."""
    normalized_text_zh: str = """"""
    subject: str = "Page of Cups (圣杯侍从)"
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
        l1_anchor="lt_v1.0.0_page_of_cups__圣杯侍从_001_L1",
    )
    version: str = "1.0.0"
