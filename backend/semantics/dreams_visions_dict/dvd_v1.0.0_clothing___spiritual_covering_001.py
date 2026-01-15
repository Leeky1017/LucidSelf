"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414550
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
    semantic_id="dvd_v1.0.0_clothing___spiritual_covering_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class ClothingSpiritualCovering(SemanticEntry):
    """
    **English**: Spiritual covering, anointing. White = righteousness, Black = sin, Purple = royalty, Ro...
    """
    
    original_text: str = """**English**: Spiritual covering, anointing. White = righteousness, Black = sin, Purple = royalty, Robe = prophetic mantle. Naked = loss of covering.
**Chinese**: 灵性遮盖、膏抹。白=公义、黑=罪、紫=王权、袍=先知外袍。赤裸=失遮盖。
**Core**: Biblical garments (Isaiah 61:10, Revelation 7:9). East: 衣服=遮盖(Christian) vs 自我(Jung)"""
    normalized_text_zh: str = """"""
    subject: str = "Clothing - Spiritual Covering"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_clothing___spiritual_covering_001_L1",
    )
    version: str = "1.0.0"
