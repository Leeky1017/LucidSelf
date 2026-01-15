"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318366
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
    semantic_id="pit_v1.0.0_saturn_in_the_first_house__土星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheFirstHouse土星过(SemanticEntry):
    """
    **Source Text** (Lines 12219-12253):
> New beginning of internal growth. Responsibilities heavy but ...
    """
    
    original_text: str = """**Source Text** (Lines 12219-12253):
> New beginning of internal growth. Responsibilities heavy but accomplishments may be great. Not good to start new long-range projects. Turn attention inward—just completed 14-year outward focus. Restructure yourself wherever necessary. Learn about yourself, not in others' terms. Time of introversion and introspection. May feel withdrawn and tired. Elaborate outer commitments may face trouble if distracting from inner work. Excellent for psychotherapy, human potential work, consciousness-raising. Unlearn incorrect ways of thinking about yourself.

**English Paraphrase**: New internal growth cycle. Heavy responsibilities. Don't start long-range projects. Turn inward. Restructure yourself. Learn who you are. Introspection required. May feel withdrawn. Excellent for therapy and consciousness work.

**Complete Chinese Interpretation**: 新的内在成长周期。沉重的责任。不要开始长期项目。向内转。重构自己。了解你是谁。需要内省。可能感到退缩。适合治疗和意识工作。

**Narrative Snippets**:
- `[ns_pit_sa001]` `[trigger: saturn_transit_house_1]` `[factor_trigger: astro_house_1 AND astro_identity_transformation]` `[role: 主干]` New internal growth cycle. Turn inward. Restructure yourself. Excellent for therapy. → PIT Ch10 Saturn-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the First House (土星过境第一宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_saturn_in_the_first_house__土星过_001_L1",
    )
    version: str = "1.0.0"
