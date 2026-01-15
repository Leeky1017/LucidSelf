"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008172
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
    semantic_id="lt_v1.0.0_the_world__世界_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheWorld世界(SemanticEntry):
    """
    **Source Text** (Lines 4846-4914): Keywords: Integration • Accomplishment • Involvement • Fulfillmen...
    """
    
    original_text: str = """**Source Text** (Lines 4846-4914): Keywords: Integration • Accomplishment • Involvement • Fulfillment

**English Paraphrase**: **The World (Card 21)** represents "wholeness—the sense that everything is working together in harmony." It is "a very positive sign that you are in a position to realize your heart's desire."

**Complete Chinese Interpretation**: **世界（第21号牌）**代表"完整——一切和谐运作的感觉。"它是"一个非常积极的信号，表明你处于实现心愿的位置。"

**Core Points**: Card 21 = integration, accomplishment, involvement, fulfillment; Wholeness; Heart's desire realized

**Narrative Snippets**:
- `[ns_ltt_069]` `[trigger: world_card]` `[factor_trigger: tarot_world]` `[role: 主干]` The World represents wholeness—everything working together in harmony. → L4905-4906
- `[ns_ltt_070]` `[trigger: world_fulfillment]` `[factor_trigger: tarot_world AND tarot_success]` `[role: 主干依赖]` A very positive sign you are in position to realize your heart's desire. → L4910-4911"""
    normalized_text_zh: str = """"""
    subject: str = "The World (世界)"
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
        l1_anchor="lt_v1.0.0_the_world__世界_001_L1",
    )
    version: str = "1.0.0"
