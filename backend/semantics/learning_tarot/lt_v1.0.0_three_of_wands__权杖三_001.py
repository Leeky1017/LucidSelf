"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008203
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
    semantic_id="lt_v1.0.0_three_of_wands__权杖三_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class ThreeOfWands权杖三(SemanticEntry):
    """
    **Source Text** (Lines 5101-5157): Keywords: Exploration • Foresight • Leadership

**English Paraphr...
    """
    
    original_text: str = """**Source Text** (Lines 5101-5157): Keywords: Exploration • Foresight • Leadership

**English Paraphrase**: **Three of Wands** represents "looking ahead to see what's coming"—exploration, foresight, visionary leadership.

**Complete Chinese Interpretation**: **权杖三**代表"展望未来"——探索、远见、有远见的领导力。

**Core Points**: Three of Wands = exploration, foresight, leadership; Looking ahead; Expanding horizons

**Narrative Snippets**:
- `[ns_ltt_074]` `[trigger: three_wands]` `[factor_trigger: tarot_three_wands]` `[role: 主干]` Three of Wands represents exploration and foresight—looking ahead. → L5101-5110"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Wands (权杖三)"
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
        l1_anchor="lt_v1.0.0_three_of_wands__权杖三_001_L1",
    )
    version: str = "1.0.0"
