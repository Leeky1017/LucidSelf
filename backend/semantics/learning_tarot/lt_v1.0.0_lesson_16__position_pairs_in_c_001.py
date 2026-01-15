"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008882
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
    semantic_id="lt_v1.0.0_lesson_16__position_pairs_in_c_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Lesson16PositionPairsInC(SemanticEntry):
    """
    **Source Text** (Lines 1572-1790): Celtic Cross contains many natural pairings. Position 1-2 is core...
    """
    
    original_text: str = """**Source Text** (Lines 1572-1790): Celtic Cross contains many natural pairings. Position 1-2 is core situation, 3-5 is consciousness levels, 4-6 is time, 7-8 is self/other, 5-10 is possible futures, 9 is wild card.

**English Paraphrase**: The **Celtic Cross** contains natural pairings: **Position 1-2** (Core Situation - collision or support), **Position 3-5** (Levels of Consciousness - real vs. expected feelings, deeper truth vs. surface), **Position 4-6** (Time - past moving away, future approaching), **Position 7-8** (Self and Other - you vs. environment/person), **Position 5-10** (Possible Futures - vision vs. projected outcome), **Position 9** (Wild Card - guidance, obstacle, or surprise).

**Complete Chinese Interpretation**: **凯尔特十字**包含自然配对：**位置1-2**（核心情境-碰撞或支持）、**位置3-5**（意识层次-真实vs预期感受，更深真相vs表面）、**位置4-6**（时间-过去远去，未来接近）、**位置7-8**（自我与他人-你vs环境/他人）、**位置5-10**（可能的未来-愿景vs预期结果）、**位置9**（万能牌-指导、障碍或惊喜）。

**Six Position Pairings**:
1. **Position 1-2** (Core Situation): Central issue + opposing/supporting factor
2. **Position 3-5** (Consciousness Levels): Unconscious (real) vs. conscious (expected)
3. **Position 4-6** (Time): Past (receding) vs. future (approaching)
4. **Position 7-8** (Self/Other): You vs. environment, another person, or group
5. **Position 5-10** (Possible Futures): Your vision vs. projected outcome
6. **Position 9** (Wild Card): Guidance, key obstacle, or surprise element

**Narrative Snippets**:
- `[ns_ltt_149]` `[trigger: position_pairs]` `[factor_trigger: tarot_celtic_cross]` `[role: 主干]` Six position pairings in Celtic Cross: 1-2, 3-5, 4-6, 7-8, 5-10, 9. → L1575-1790"""
    normalized_text_zh: str = """"""
    subject: str = "Lesson 16: Position Pairs in Celtic Cross (凯尔特十字位置配对)"
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
        l1_anchor="lt_v1.0.0_lesson_16__position_pairs_in_c_001_L1",
    )
    version: str = "1.0.0"
