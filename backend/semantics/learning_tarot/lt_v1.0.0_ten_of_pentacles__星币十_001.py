"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008570
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
    semantic_id="lt_v1.0.0_ten_of_pentacles__星币十_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TenOfPentacles星币十(SemanticEntry):
    """
    **Source Text** (Lines 7225-7281): Keywords: Affluence • Permanence • Convention

**English Paraphra...
    """
    
    original_text: str = """**Source Text** (Lines 7225-7281): Keywords: Affluence • Permanence • Convention

**English Paraphrase**: **Ten of Pentacles** represents "affluence and legacy"—wealth, family security, tradition, established prosperity.

**Complete Chinese Interpretation**: **星币十**代表"富裕和遗产"——财富、家庭安全、传统、已建立的繁荣。

**Core Points**: Ten of Pentacles = affluence, permanence, convention; Family wealth; Lasting prosperity

**Narrative Snippets**:
- `[ns_ltt_111]` `[trigger: ten_pentacles]` `[factor_trigger: tarot_ten_pentacles]` `[role: 主干]` Ten of Pentacles represents affluence and family legacy. → L7225-7235"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Pentacles (星币十)"
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
        l1_anchor="lt_v1.0.0_ten_of_pentacles__星币十_001_L1",
    )
    version: str = "1.0.0"
