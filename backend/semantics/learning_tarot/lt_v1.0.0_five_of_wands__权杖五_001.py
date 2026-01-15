"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008223
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
    semantic_id="lt_v1.0.0_five_of_wands__权杖五_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FiveOfWands权杖五(SemanticEntry):
    """
    **Source Text** (Lines 5215-5271): Keywords: Disagreement • Competition • Hassles

**English Paraphr...
    """
    
    original_text: str = """**Source Text** (Lines 5215-5271): Keywords: Disagreement • Competition • Hassles

**English Paraphrase**: **Five of Wands** represents "disagreement and competition"—clashing interests, petty hassles, struggling against others.

**Complete Chinese Interpretation**: **权杖五**代表"分歧和竞争"——利益冲突、琐碎麻烦、与他人斗争。

**Core Points**: Five of Wands = disagreement, competition, hassles; Clashing interests; Conflict energy

**Narrative Snippets**:
- `[ns_ltt_076]` `[trigger: five_wands]` `[factor_trigger: tarot_five_wands AND tarot_conflict]` `[role: 主干]` Five of Wands shows creative friction: the clash is more sparring than warfare—each combatant tests ideas against others; competition sharpens skills when not taken personally, though it can degenerate into petty hassle if ego dominates."""
    normalized_text_zh: str = """"""
    subject: str = "Five of Wands (权杖五)"
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
        l1_anchor="lt_v1.0.0_five_of_wands__权杖五_001_L1",
    )
    version: str = "1.0.0"
