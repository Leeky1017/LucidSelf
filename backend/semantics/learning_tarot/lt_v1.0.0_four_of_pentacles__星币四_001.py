"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008512
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
    semantic_id="lt_v1.0.0_four_of_pentacles__星币四_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FourOfPentacles星币四(SemanticEntry):
    """
    **Source Text** (Lines 6883-6939): Keywords: Possessiveness • Control • Blocked Change

**English Pa...
    """
    
    original_text: str = """**Source Text** (Lines 6883-6939): Keywords: Possessiveness • Control • Blocked Change

**English Paraphrase**: **Four of Pentacles** represents "possessiveness"—holding on too tight, control, blocking change, security through rigidity.

**Complete Chinese Interpretation**: **星币四**代表"占有欲"——抓得太紧、控制、阻止变化、通过僵化获得安全。

**Core Points**: Four of Pentacles = possessiveness, control, blocked change; Holding too tight; Fear of loss

**Narrative Snippets**:
- `[ns_ltt_105]` `[trigger: four_pentacles]` `[factor_trigger: tarot_four_pentacles]` `[role: 主干]` Four of Pentacles represents possessiveness and blocked change. → L6883-6895"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Pentacles (星币四)"
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
        l1_anchor="lt_v1.0.0_four_of_pentacles__星币四_001_L1",
    )
    version: str = "1.0.0"
