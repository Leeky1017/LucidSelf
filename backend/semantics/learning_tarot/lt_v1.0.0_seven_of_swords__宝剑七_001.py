"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008442
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
    semantic_id="lt_v1.0.0_seven_of_swords__宝剑七_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SevenOfSwords宝剑七(SemanticEntry):
    """
    **Source Text** (Lines 6479-6535): Keywords: Running Away • Lone-Wolf Style • Hidden Dishonor

**Eng...
    """
    
    original_text: str = """**Source Text** (Lines 6479-6535): Keywords: Running Away • Lone-Wolf Style • Hidden Dishonor

**English Paraphrase**: **Seven of Swords** represents "acting alone"—going it alone, stealth, avoiding confrontation, possibly deception.

**Complete Chinese Interpretation**: **宝剑七**代表"独自行动"——单独行动、隐秘、避免对抗、可能的欺骗。

**Core Points**: Seven of Swords = running away, lone-wolf, hidden dishonor; Stealth action; Going alone

**Narrative Snippets**:
- `[ns_ltt_098]` `[trigger: seven_swords]` `[factor_trigger: tarot_seven_swords]` `[role: 主干]` Seven of Swords represents acting alone or stealthily. → L6479-6490"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Swords (宝剑七)"
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
        l1_anchor="lt_v1.0.0_seven_of_swords__宝剑七_001_L1",
    )
    version: str = "1.0.0"
