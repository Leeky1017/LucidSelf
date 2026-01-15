"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008892
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
    semantic_id="lt_v1.0.0_lesson_17__reversed_cards__逆位牌_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson17ReversedCards逆位牌(SemanticEntry):
    """
    **Source Text** (Lines 1791-1874): When card is reversed, energy is not fully developed. May be in e...
    """
    
    original_text: str = """**Source Text** (Lines 1791-1874): When card is reversed, energy is not fully developed. May be in early stages, losing power, incomplete, or unavailable.

**English Paraphrase**: **Reversed cards** show energy "not fully developed. It may be in its early stages, or losing power. It may be incomplete or unavailable." Upright = energy freely manifesting. Reversed = same energy present but at lower level. Proportion of reversed cards also matters: many reversed = energies low, situation not clearly defined, change likely.

**Complete Chinese Interpretation**: **逆位牌**显示能量"未充分发展。它可能处于早期阶段，或正在失去力量。它可能是不完整的或不可用的。"正位=能量自由显现。逆位=相同能量存在但处于较低水平。逆位牌的比例也很重要：许多逆位=能量低，情况不明确，变化可能。

**Reversed Card Theory**:
- **Upright**: Energy free to manifest, qualities available and active
- **Reversed**: Energy not fully developed—early stages, losing power, incomplete, unavailable

**Four Reversed Interpretations**:
1. **Blocked energy**: Something holding back the quality
2. **Reduced level**: Same energy but less intense
3. **Conscious lowering needed**: Hint to reduce that energy
4. **Twist in interpretation**: e.g., Emperor reversed = authority figure toppled

**Proportion Reading**: Many reversed = energies low, situation undefined, change likely

**Narrative Snippets**:
- `[ns_ltt_150]` `[trigger: reversed_theory]` `[factor_trigger: tarot_reversed]` `[role: 主干]` Reversed = energy not fully developed, in early stages, or losing power. → L1805-1809
- `[ns_ltt_151]` `[trigger: reversed_proportion]` `[factor_trigger: tarot_reversed]` `[role: 辅助]` Many reversed cards = low energy, undefined situation, change likely. → L1862-1867"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 17: Reversed Cards (逆位牌)"
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
        l1_anchor="lt_v1.0.0_lesson_17__reversed_cards__逆位牌_001_L1",
    )
    version: str = "1.0.0"
