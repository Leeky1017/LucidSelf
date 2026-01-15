"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008045
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
    semantic_id="lt_v1.0.0_strength__力量_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Strength力量(SemanticEntry):
    """
    **Source Text** (Lines 3991-4056): Keywords: Strength • Patience • Compassion • Soft Control

**Engl...
    """
    
    original_text: str = """**Source Text** (Lines 3991-4056): Keywords: Strength • Patience • Compassion • Soft Control

**English Paraphrase**: **Strength (Card 8)** represents "inner strength"—perseverance, courage, resolve, composure. Unlike Chariot's hard control, Strength achieves through "soft control."

**Complete Chinese Interpretation**: **力量（第8号牌）**代表"内在力量"——坚持、勇气、决心、镇定。不同于战车的硬控制，力量通过"软控制"达成。

**Core Points**: Card 8 = inner strength, patience, compassion, soft control; Contrast to Chariot; Strength of love

**Narrative Snippets**:
- `[ns_ltt_043]` `[trigger: strength_card]` `[factor_trigger: tarot_strength]` `[role: 主干]` Card 8 represents inner strength—perseverance, courage, resolve. → L4039-4042
- `[ns_ltt_044]` `[trigger: strength_soft]` `[factor_trigger: tarot_strength AND tarot_tarot_chariot]` `[role: 主干依赖]` Chariot controls through authority; Strength is more subtle, even loving. → L4048-4051"""
    normalized_text_zh: str = """"""
    subject: str = "Strength (力量)"
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
        l1_anchor="lt_v1.0.0_strength__力量_001_L1",
    )
    version: str = "1.0.0"
