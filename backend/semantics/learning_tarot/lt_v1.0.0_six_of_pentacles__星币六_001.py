"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008532
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
    semantic_id="lt_v1.0.0_six_of_pentacles__星币六_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SixOfPentacles星币六(SemanticEntry):
    """
    **Source Text** (Lines 6997-7053): Keywords: Having/Not Having Resources • Knowledge • Power

**Engl...
    """
    
    original_text: str = """**Source Text** (Lines 6997-7053): Keywords: Having/Not Having Resources • Knowledge • Power

**English Paraphrase**: **Six of Pentacles** represents "having and sharing resources"—generosity, giving and receiving, power dynamics in exchange.

**Complete Chinese Interpretation**: **星币六**代表"拥有和分享资源"——慷慨、给予和接受、交换中的权力动态。

**Core Points**: Six of Pentacles = resources, knowledge, power; Generosity; Giving and receiving

**Narrative Snippets**:
- `[ns_ltt_107]` `[trigger: six_pentacles]` `[factor_trigger: tarot_six_pentacles]` `[role: 主干]` Six of Pentacles represents sharing resources and generosity. → L6997-7005"""
    normalized_text_zh: str = """"""
    subject: str = "Six of Pentacles (星币六)"
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
        l1_anchor="lt_v1.0.0_six_of_pentacles__星币六_001_L1",
    )
    version: str = "1.0.0"
