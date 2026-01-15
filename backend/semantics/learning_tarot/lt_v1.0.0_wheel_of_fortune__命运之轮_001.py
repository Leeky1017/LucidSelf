"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008066
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
    semantic_id="lt_v1.0.0_wheel_of_fortune__命运之轮_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class WheelOfFortune命运之轮(SemanticEntry):
    """
    **Source Text** (Lines 4121-4186): Keywords: Destiny • Turning Point • Movement • Personal Vision

*...
    """
    
    original_text: str = """**Source Text** (Lines 4121-4186): Keywords: Destiny • Turning Point • Movement • Personal Vision

**English Paraphrase**: **Wheel of Fortune (Card 10)** is unique—no human focal point. Its center is above the realm of man, where destinies are woven together. "When the Wheel arrives, life speeds up."

**Complete Chinese Interpretation**: **命运之轮（第10号牌）**是独特的——没有人物焦点。它的中心在人类领域之上，命运在那里被编织在一起。"当命运之轮到来时，生活加速。"

**Core Points**: Card 10 = destiny, turning point, movement, personal vision; Above realm of man; Life speeds up

**Narrative Snippets**:
- `[ns_ltt_047]` `[trigger: wheel_card]` `[factor_trigger: tarot_wheel]` `[role: 主干]` The Wheel is one of few cards without a human focal point—above the realm of man. → L4171-4175
- `[ns_ltt_048]` `[trigger: wheel_movement]` `[factor_trigger: tarot_wheel AND tarot_change]` `[role: 主干依赖]` When the Wheel arrives, life speeds up—caught in a cyclone. → L4184-4186"""
    normalized_text_zh: str = """"""
    subject: str = "Wheel of Fortune (命运之轮)"
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
        l1_anchor="lt_v1.0.0_wheel_of_fortune__命运之轮_001_L1",
    )
    version: str = "1.0.0"
