"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008125
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
    semantic_id="lt_v1.0.0_the_tower__塔_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheTower塔(SemanticEntry):
    """
    **Source Text** (Lines 4530-4587): Keywords: Sudden Change • Downfall • Release • Revelation

**Engl...
    """
    
    original_text: str = """**Source Text** (Lines 4530-4587): Keywords: Sudden Change • Downfall • Release • Revelation

**English Paraphrase**: **The Tower (Card 16)** represents "sudden, dramatic upheaval or reversal in fortune"—quick and explosive change. "Sudden crises are life's way of telling you to wake up."

**Complete Chinese Interpretation**: **塔（第16号牌）**代表"突然、戏剧性的动荡或命运逆转"——快速和爆炸性的变化。"突然的危机是生活告诉你要觉醒的方式。"

**Core Points**: Card 16 = sudden change, downfall, release, revelation; Wake-up call; Response matters

**Narrative Snippets**:
- `[ns_ltt_059]` `[trigger: tower_card]` `[factor_trigger: tarot_tower AND tarot_upheaval]` `[role: 主干]` The Tower shatters structures built on false foundations: the lightning strikes what was already unstable; the fall is not punishment but liberation from prisons we didn't know we inhabited—revelation through destruction. → L4574-4576
- `[ns_ltt_060]` `[trigger: tower_wakeup]` `[factor_trigger: tarot_tower AND tarot_revelation]` `[role: 主干依赖]` The Tower's crisis forces confrontation with denied truths: what we refused to see is made undeniable; the ego's defenses collapse, and authentic reality breaks through—painful but ultimately freeing. → L4579-4582"""
    normalized_text_zh: str = """"""
    subject: str = "The Tower (塔)"
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
        l1_anchor="lt_v1.0.0_the_tower__塔_001_L1",
    )
    version: str = "1.0.0"
