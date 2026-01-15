"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009074
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
    semantic_id="lt_v1.0.0_appendix_d__court_card_rank_pa_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class AppendixDCourtCardRankPa(SemanticEntry):
    """
    **Summary**: When two court card ranks appear, they create specific dynamics.

**King/King**: Two ma...
    """
    
    original_text: str = """**Summary**: When two court card ranks appear, they create specific dynamics.

**King/King**: Two mature, different aspects; masculine focus doubled
**Queen/Queen**: Equal partners; feminine focus doubled
**King/Queen**: Man/Woman, Outer/Inner, Direct/Indirect
**King-Queen/Knight**: Adult/Teen, Moderate/Immoderate, Cautious/Adventurous
**King-Queen/Page**: Adult/Child, Serious/Lighthearted, Responsible/Carefree
**Knight/Knight**: Two extreme opposing sides of self
**Knight/Page**: Drastic/Mild, Obsessive/Easygoing

**Narrative Snippets**:
- `[ns_ltt_167]` `[trigger: rank_pairs]` `[factor_trigger: tarot_court_pairs]` `[role: 主干]` Court rank pairs create dynamics: King/Queen = masculine/feminine, etc. → Appendix D"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix D: Court Card Rank Pair Meanings (宫廷牌等级配对含义)"
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
        l1_anchor="lt_v1.0.0_appendix_d__court_card_rank_pa_001_L1",
    )
    version: str = "1.0.0"
