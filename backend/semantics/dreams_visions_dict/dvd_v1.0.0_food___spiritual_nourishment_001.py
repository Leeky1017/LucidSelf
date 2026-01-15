"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414572
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
    semantic_id="dvd_v1.0.0_food___spiritual_nourishment_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class FoodSpiritualNourishment(SemanticEntry):
    """
    **English**: Word of God, teaching. Healthy = sound doctrine, junk = false teaching, meat = mature, ...
    """
    
    original_text: str = """**English**: Word of God, teaching. Healthy = sound doctrine, junk = false teaching, meat = mature, milk = basic. Eating = receiving, hunger = spiritual need.
**Chinese**: 神的话、教导。健康=纯正教义、垃圾=假教导、肉=成熟、奶=基本。吃=接受、饥饿=灵性需要。
**Core**: Bread of life (John 6:35), milk vs meat (Hebrews 5:12-14). East: 食物=滋养(共通) + 道(Christian)"""
    normalized_text_zh: str = """"""
    subject: str = "Food - Spiritual Nourishment"
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
        l1_anchor="dvd_v1.0.0_food___spiritual_nourishment_001_L1",
    )
    version: str = "1.0.0"
