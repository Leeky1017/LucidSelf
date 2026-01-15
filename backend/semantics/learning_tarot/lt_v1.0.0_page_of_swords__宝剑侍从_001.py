"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008661
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
    semantic_id="lt_v1.0.0_page_of_swords__宝剑侍从_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class PageOfSwords宝剑侍从(SemanticEntry):
    """
    **Keywords**: Use Your Mind • Be Truthful • Be Just • Have Fortitude

**English Paraphrase**: **Page...
    """
    
    original_text: str = """**Keywords**: Use Your Mind • Be Truthful • Be Just • Have Fortitude

**English Paraphrase**: **Page of Swords** represents youthful mental sharpness—using the mind, being truthful, just, and having fortitude.

**Complete Chinese Interpretation**: **宝剑侍从**代表年轻的思维敏锐——运用头脑、真实、公正、有毅力。

**Narrative Snippets**:
- `[ns_ltt_120]` `[trigger: page_swords]` `[factor_trigger: tarot_page_swords AND tarot_truth]` `[role: 主干]` Page of Swords wields intellect with the enthusiasm of discovery: curious, vigilant, sometimes tactlessly honest; the mind beginning to differentiate truth from falsehood, developing critical faculties that may wound before learning restraint."""
    normalized_text_zh: str = """"""
    subject: str = "Page of Swords (宝剑侍从)"
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
        l1_anchor="lt_v1.0.0_page_of_swords__宝剑侍从_001_L1",
    )
    version: str = "1.0.0"
