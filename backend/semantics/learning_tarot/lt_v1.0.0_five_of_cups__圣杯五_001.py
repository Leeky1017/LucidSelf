"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008326
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
    semantic_id="lt_v1.0.0_five_of_cups__圣杯五_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class FiveOfCups圣杯五(SemanticEntry):
    """
    **Source Text** (Lines 5790-5846): Keywords: Loss • Bereavement • Regret

**English Paraphrase**: **...
    """
    
    original_text: str = """**Source Text** (Lines 5790-5846): Keywords: Loss • Bereavement • Regret

**English Paraphrase**: **Five of Cups** represents "loss"—grief, bereavement, focusing on what's gone while missing what remains.

**Complete Chinese Interpretation**: **圣杯五**代表"失去"——悲伤、丧亲之痛、专注于失去的而忽视剩余的。

**Core Points**: Five of Cups = loss, bereavement, regret; Grieving; Focusing on the negative

**Narrative Snippets**:
- `[ns_ltt_086]` `[trigger: five_cups]` `[factor_trigger: tarot_five_cups AND tarot_grief]` `[role: 主干]` Five of Cups shows the figure mourning three spilled cups while two full ones stand behind unnoticed: grief naturally focuses on loss, but recovery begins when attention shifts to what remains; the card does not deny pain but suggests perspective."""
    normalized_text_zh: str = """"""
    subject: str = "Five of Cups (圣杯五)"
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
        l1_anchor="lt_v1.0.0_five_of_cups__圣杯五_001_L1",
    )
    version: str = "1.0.0"
