"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008035
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
    semantic_id="lt_v1.0.0_the_chariot__战车_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheChariot战车(SemanticEntry):
    """
    **Source Text** (Lines 3921-3990): Keywords: Victory • Will • Self-Assertion • Hard Control

**Engli...
    """
    
    original_text: str = """**Source Text** (Lines 3921-3990): Keywords: Victory • Will • Self-Assertion • Hard Control

**English Paraphrase**: **The Chariot (Card 7)** represents "victories possible through willpower and self-mastery"—discipline, grit, determination, assertiveness. Hard control: firm and direct.

**Complete Chinese Interpretation**: **战车（第7号牌）**代表"通过意志力和自我掌控而可能获得的胜利"——纪律、坚韧、决心、自信。硬控制：坚定而直接。

**Core Points**: Card 7 = victory, will, self-assertion, hard control; Military strengths; Healthy ego knows what it wants

**Narrative Snippets**:
- `[ns_ltt_041]` `[trigger: chariot_card]` `[factor_trigger: tarot_chariot]` `[role: 主干]` The Chariot represents victories possible through willpower and self-mastery. → L3976-3979
- `[ns_ltt_042]` `[trigger: chariot_control]` `[factor_trigger: tarot_chariot AND tarot_control]` `[role: 主干依赖]` Hard control is firm and direct, backed by strong will. → L3985-3987"""
    normalized_text_zh: str = """"""
    subject: str = "The Chariot (战车)"
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
        l1_anchor="lt_v1.0.0_the_chariot__战车_001_L1",
    )
    version: str = "1.0.0"
