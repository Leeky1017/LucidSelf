"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008213
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
    semantic_id="lt_v1.0.0_four_of_wands__权杖四_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FourOfWands权杖四(SemanticEntry):
    """
    **Source Text** (Lines 5158-5214): Keywords: Celebration • Freedom • Excitement

**English Paraphras...
    """
    
    original_text: str = """**Source Text** (Lines 5158-5214): Keywords: Celebration • Freedom • Excitement

**English Paraphrase**: **Four of Wands** represents "celebration"—special occasions, ceremony, freedom, excitement.

**Complete Chinese Interpretation**: **权杖四**代表"庆祝"——特殊场合、仪式、自由、兴奋。

**Core Points**: Four of Wands = celebration, freedom, excitement; Special occasions; Joy and community

**Narrative Snippets**:
- `[ns_ltt_075]` `[trigger: four_wands]` `[factor_trigger: tarot_four_wands AND tarot_celebration]` `[role: 主干]` Four of Wands marks the completion of a foundation: the bower of celebration indicates that initial structure is in place—now joy can be expressed because security has been established; community gathers to honor what has been built."""
    normalized_text_zh: str = """"""
    subject: str = "Four of Wands (权杖四)"
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
        l1_anchor="lt_v1.0.0_four_of_wands__权杖四_001_L1",
    )
    version: str = "1.0.0"
