"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008115
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
    semantic_id="lt_v1.0.0_the_devil__恶魔_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheDevil恶魔(SemanticEntry):
    """
    **Source Text** (Lines 4459-4529): Keywords: Bondage • Materialism • Ignorance • Hopelessness

**Eng...
    """
    
    original_text: str = """**Source Text** (Lines 4459-4529): Keywords: Bondage • Materialism • Ignorance • Hopelessness

**English Paraphrase**: **The Devil (Card 15)** shows errors hiding truth—ignorance, materialism, hopelessness. "This card lets you know you are caught in an unhealthy, unproductive situation."

**Complete Chinese Interpretation**: **恶魔（第15号牌）**显示隐藏真相的错误——无知、物质主义、绝望。"这张牌让你知道你陷入了不健康、无效的情况。"

**Core Points**: Card 15 = bondage, materialism, ignorance; Errors hiding truth; Examine assumptions

**Narrative Snippets**:
- `[ns_ltt_057]` `[trigger: devil_card]` `[factor_trigger: tarot_devil AND tarot_bondage]` `[role: 主干]` The Devil represents self-imposed bondage: the chains around the figures' necks are loose enough to remove, but they don't notice—addiction, obsession, and materialism feel like external forces but are maintained by our own collusion. → L4515-4520
- `[ns_ltt_058]` `[trigger: devil_shadow]` `[factor_trigger: tarot_devil AND tarot_shadow]` `[role: 主干依赖]` The Devil is the shadow confrontation: denied desires, rejected impulses, and disowned aspects of self accumulate power in the unconscious; acknowledgment (not indulgence) begins liberation. → L4521-4529"""
    normalized_text_zh: str = """"""
    subject: str = "The Devil (恶魔)"
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
        l1_anchor="lt_v1.0.0_the_devil__恶魔_001_L1",
    )
    version: str = "1.0.0"
