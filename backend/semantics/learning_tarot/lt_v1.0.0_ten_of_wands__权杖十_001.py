"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008276
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
    semantic_id="lt_v1.0.0_ten_of_wands__权杖十_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TenOfWands权杖十(SemanticEntry):
    """
    **Source Text** (Lines 5500-5556): Keywords: Overextending • Burdens • Struggle

**English Paraphras...
    """
    
    original_text: str = """**Source Text** (Lines 5500-5556): Keywords: Overextending • Burdens • Struggle

**English Paraphrase**: **Ten of Wands** represents "burdens"—overextending yourself, taking on too much, struggling under excessive responsibilities.

**Complete Chinese Interpretation**: **权杖十**代表"负担"——过度扩张、承担太多、在过度责任下挣扎。

**Core Points**: Ten of Wands = overextending, burdens, struggle; Too many responsibilities; Heavy load

**Narrative Snippets**:
- `[ns_ltt_081]` `[trigger: ten_wands]` `[factor_trigger: tarot_ten_wands AND tarot_burden]` `[role: 主干]` Ten of Wands shows creative energy pushed to exhaustion: carrying all ten wands alone because you don't trust others or can't say no; the burden is real but often self-imposed—consider which responsibilities truly require your personal attention."""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Wands (权杖十)"
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
        l1_anchor="lt_v1.0.0_ten_of_wands__权杖十_001_L1",
    )
    version: str = "1.0.0"
