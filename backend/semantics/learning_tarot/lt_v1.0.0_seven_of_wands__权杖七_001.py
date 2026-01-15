"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008245
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
    semantic_id="lt_v1.0.0_seven_of_wands__权杖七_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SevenOfWands权杖七(SemanticEntry):
    """
    **Source Text** (Lines 5329-5385): Keywords: Aggression • Defiance • Conviction

**English Paraphras...
    """
    
    original_text: str = """**Source Text** (Lines 5329-5385): Keywords: Aggression • Defiance • Conviction

**English Paraphrase**: **Seven of Wands** represents "standing your ground"—aggression, defiance, maintaining your position against opposition.

**Complete Chinese Interpretation**: **权杖七**代表"坚守立场"——进攻、反抗、在反对面前维持你的位置。

**Core Points**: Seven of Wands = aggression, defiance, conviction; Standing ground; Defending position

**Narrative Snippets**:
- `[ns_ltt_078]` `[trigger: seven_wands]` `[factor_trigger: tarot_seven_wands]` `[role: 主干]` Seven of Wands represents standing your ground against opposition. → L5329-5340"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Wands (权杖七)"
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
        l1_anchor="lt_v1.0.0_seven_of_wands__权杖七_001_L1",
    )
    version: str = "1.0.0"
