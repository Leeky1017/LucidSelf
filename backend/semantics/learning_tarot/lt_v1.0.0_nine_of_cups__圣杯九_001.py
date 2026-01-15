"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008365
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
    semantic_id="lt_v1.0.0_nine_of_cups__圣杯九_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class NineOfCups圣杯九(SemanticEntry):
    """
    **Source Text** (Lines 6018-6074): Keywords: Wish Fulfillment • Satisfaction • Sensual Pleasure

**E...
    """
    
    original_text: str = """**Source Text** (Lines 6018-6074): Keywords: Wish Fulfillment • Satisfaction • Sensual Pleasure

**English Paraphrase**: **Nine of Cups** represents "wish fulfillment"—getting what you want, satisfaction, enjoying pleasures.

**Complete Chinese Interpretation**: **圣杯九**代表"愿望实现"——得到你想要的、满足、享受快乐。

**Core Points**: Nine of Cups = wish fulfillment, satisfaction, pleasure; Getting your heart's desire; Contentment

**Narrative Snippets**:
- `[ns_ltt_090]` `[trigger: nine_cups]` `[factor_trigger: tarot_nine_cups AND tarot_satisfaction]` `[role: 主干]` Nine of Cups shows the satisfied figure before displayed cups: the 'wish card' indicates emotional desires coming true; genuine contentment rather than craving—though its shadow asks whether the wish was truly worth wanting."""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Cups (圣杯九)"
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
        l1_anchor="lt_v1.0.0_nine_of_cups__圣杯九_001_L1",
    )
    version: str = "1.0.0"
