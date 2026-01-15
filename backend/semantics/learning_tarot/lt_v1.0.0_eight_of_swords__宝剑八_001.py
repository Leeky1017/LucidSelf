"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008451
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
    semantic_id="lt_v1.0.0_eight_of_swords__宝剑八_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class EightOfSwords宝剑八(SemanticEntry):
    """
    **Source Text** (Lines 6536-6592): Keywords: Restriction • Confusion • Powerlessness

**English Para...
    """
    
    original_text: str = """**Source Text** (Lines 6536-6592): Keywords: Restriction • Confusion • Powerlessness

**English Paraphrase**: **Eight of Swords** represents "feeling restricted"—trapped by circumstances, confusion, feeling powerless despite having options.

**Complete Chinese Interpretation**: **宝剑八**代表"感到受限"——被环境困住、困惑、尽管有选择仍感到无力。

**Core Points**: Eight of Swords = restriction, confusion, powerlessness; Feeling trapped; Mental prison

**Narrative Snippets**:
- `[ns_ltt_099]` `[trigger: eight_swords]` `[factor_trigger: tarot_eight_swords]` `[role: 主干]` Eight of Swords represents feeling trapped and restricted. → L6536-6545"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Swords (宝剑八)"
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
        l1_anchor="lt_v1.0.0_eight_of_swords__宝剑八_001_L1",
    )
    version: str = "1.0.0"
