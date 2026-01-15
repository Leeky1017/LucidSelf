"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008433
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
    semantic_id="lt_v1.0.0_six_of_swords__宝剑六_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SixOfSwords宝剑六(SemanticEntry):
    """
    **Source Text** (Lines 6422-6478): Keywords: The Blues • Recovery • Travel

**English Paraphrase**: ...
    """
    
    original_text: str = """**Source Text** (Lines 6422-6478): Keywords: The Blues • Recovery • Travel

**English Paraphrase**: **Six of Swords** represents "moving toward calmer waters"—leaving troubles behind, recovery through travel, gradual improvement.

**Complete Chinese Interpretation**: **宝剑六**代表"驶向更平静的水域"——离开烦恼、通过旅行恢复、逐渐改善。

**Core Points**: Six of Swords = the blues, recovery, travel; Moving on; Calmer waters ahead

**Narrative Snippets**:
- `[ns_ltt_097]` `[trigger: six_swords]` `[factor_trigger: tarot_six_swords AND tarot_transition]` `[role: 主干]` Six of Swords shows the ferryman guiding passengers from choppy to calm waters: transition away from difficulty through mental clarity; the journey is somber because what's left behind was painful, but direction is unmistakably toward relief."""
    normalized_text_zh: str = """"""
    subject: str = "Six of Swords (宝剑六)"
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
        l1_anchor="lt_v1.0.0_six_of_swords__宝剑六_001_L1",
    )
    version: str = "1.0.0"
