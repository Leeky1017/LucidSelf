"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008026
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
    semantic_id="lt_v1.0.0_the_lovers__恋人_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheLovers恋人(SemanticEntry):
    """
    **Source Text** (Lines 3850-3920): Keywords: Relationship • Sexuality • Personal Beliefs • Values

*...
    """
    
    original_text: str = """**Source Text** (Lines 3850-3920): Keywords: Relationship • Sexuality • Personal Beliefs • Values

**English Paraphrase**: **The Lovers (Card 6)** represents "the attractive force that draws any two entities together"—people, ideas, events, movements. It also stands for personal value choices and moral crossroads.

**Complete Chinese Interpretation**: **恋人（第6号牌）**代表"将任何两个实体吸引在一起的力量"——人、想法、事件、运动。它也代表个人价值选择和道德十字路口。

**Core Points**: Card 6 = relationship, sexuality, personal beliefs, values; Counterpoint to Hierophant; Love/union + moral crossroads

**Narrative Snippets**:
- `[ns_ltt_039]` `[trigger: lovers_card]` `[factor_trigger: tarot_lovers]` `[role: 主干]` The Lovers represents the attractive force that draws any two entities together. → L3909-3911
- `[ns_ltt_040]` `[trigger: lovers_values]` `[factor_trigger: tarot_lovers AND tarot_decision]` `[role: 主干依赖]` The Lovers can indicate a moral or ethical crossroads. → L3916-3917"""
    normalized_text_zh: str = """"""
    subject: str = "The Lovers (恋人)"
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
        l1_anchor="lt_v1.0.0_the_lovers__恋人_001_L1",
    )
    version: str = "1.0.0"
