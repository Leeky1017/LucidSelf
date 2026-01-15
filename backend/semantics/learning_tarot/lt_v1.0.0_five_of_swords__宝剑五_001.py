"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008422
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
    semantic_id="lt_v1.0.0_five_of_swords__宝剑五_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FiveOfSwords宝剑五(SemanticEntry):
    """
    **Source Text** (Lines 6365-6421): Keywords: Self-Interest • Discord • Open Dishonor

**English Para...
    """
    
    original_text: str = """**Source Text** (Lines 6365-6421): Keywords: Self-Interest • Discord • Open Dishonor

**English Paraphrase**: **Five of Swords** represents "self-interest at others' expense"—discord, winning but losing respect, dishonor.

**Complete Chinese Interpretation**: **宝剑五**代表"以牺牲他人为代价的自私"——不和、获胜但失去尊重、不名誉。

**Core Points**: Five of Swords = self-interest, discord, dishonor; Hollow victory; Ethical compromise

**Narrative Snippets**:
- `[ns_ltt_096]` `[trigger: five_swords]` `[factor_trigger: tarot_five_swords]` `[role: 主干]` Five of Swords represents hollow victory through self-interest. → L6365-6375"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Swords (宝剑五)"
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
        l1_anchor="lt_v1.0.0_five_of_swords__宝剑五_001_L1",
    )
    version: str = "1.0.0"
