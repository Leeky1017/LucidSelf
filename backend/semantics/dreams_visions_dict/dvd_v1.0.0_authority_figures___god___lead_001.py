"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414668
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
    semantic_id="dvd_v1.0.0_authority_figures___god___lead_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class AuthorityFiguresGodLead(SemanticEntry):
    """
    **English**: Father = God Father, Teacher = mentor, Boss = spiritual covering. Reveals how you relat...
    """
    
    original_text: str = """**English**: Father = God Father, Teacher = mentor, Boss = spiritual covering. Reveals how you relate to authority/God. Rebellion = rebellion against God.
**Chinese**: 父=天父、教师=导师、老板=灵性遮盖。揭示你如何与权威/神相关。反叛=反叛神。
**Core**: External relationship (not Jung's internal aspect). East: 权威=神/师(Christian) vs 自我面(Jung)"""
    normalized_text_zh: str = """"""
    subject: str = "Authority Figures - God & Leaders"
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
        l1_anchor="dvd_v1.0.0_authority_figures___god___lead_001_L1",
    )
    version: str = "1.0.0"
