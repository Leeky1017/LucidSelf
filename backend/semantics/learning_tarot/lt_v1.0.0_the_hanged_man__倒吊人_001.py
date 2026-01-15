"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008087
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
    semantic_id="lt_v1.0.0_the_hanged_man__倒吊人_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheHangedMan倒吊人(SemanticEntry):
    """
    **Source Text** (Lines 4257-4328): Keywords: Letting Go • Reversal • Suspension • Sacrifice

**Engli...
    """
    
    original_text: str = """**Source Text** (Lines 4257-4328): Keywords: Letting Go • Reversal • Suspension • Sacrifice

**English Paraphrase**: **The Hanged Man (Card 12)** is "most mysterious"—paradoxical truths: "We 'control' by letting go, 'win' by surrendering, 'move forward' by standing still."

**Complete Chinese Interpretation**: **倒吊人（第12号牌）**是"最神秘的"——悖论真理："我们通过放手来'控制'，通过投降来'获胜'，通过静止来'前进'。"

**Core Points**: Card 12 = letting go, reversal, suspension, sacrifice; Paradoxical truths; Control by releasing

**Narrative Snippets**:
- `[ns_ltt_051]` `[trigger: hanged_man_card]` `[factor_trigger: tarot_hanged_man]` `[role: 主干]` The Hanged Man symbolizes paradox—truths hidden in opposites. → L4312-4317
- `[ns_ltt_052]` `[trigger: hanged_man_paradox]` `[factor_trigger: tarot_hanged_man AND tarot_paradox]` `[role: 主干依赖]` We control by letting go, win by surrendering, move forward by standing still. → L4318-4323"""
    normalized_text_zh: str = """"""
    subject: str = "The Hanged Man (倒吊人)"
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
        l1_anchor="lt_v1.0.0_the_hanged_man__倒吊人_001_L1",
    )
    version: str = "1.0.0"
