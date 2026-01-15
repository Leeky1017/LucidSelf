"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.009085
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
    semantic_id="lt_v1.0.0_introduction_to_jill_s_reading_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class IntroductionToJillSReading(SemanticEntry):
    """
    **Source Text** (Lines 9132-9141): Jill's tale is a series of three readings over the course of a ye...
    """
    
    original_text: str = """**Source Text** (Lines 9132-9141): Jill's tale is a series of three readings over the course of a year. These readings illustrate how the tarot can reflect developments over time.

**English Paraphrase**: Jill's tale demonstrates how "every reading is a snapshot of a given moment. As events unfold, the snapshots change, but there is a common thread that connects them."

**Complete Chinese Interpretation**: Jill的故事展示了"每次解读都是某一时刻的快照。随着事件展开，快照会改变，但有一条共同的线索连接它们。"

**Key Teaching Points**:
- Readings reflect developments over time
- Each reading = snapshot of a given moment
- Common thread connects multiple readings
- Repeat cards show enduring energies"""
    normalized_text_zh: str = """"""
    subject: str = "Introduction to Jill's Readings"
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
        l1_anchor="lt_v1.0.0_introduction_to_jill_s_reading_001_L1",
    )
    version: str = "1.0.0"
