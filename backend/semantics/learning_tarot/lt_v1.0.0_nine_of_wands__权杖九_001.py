"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008266
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
    semantic_id="lt_v1.0.0_nine_of_wands__权杖九_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class NineOfWands权杖九(SemanticEntry):
    """
    **Source Text** (Lines 5443-5499): Keywords: Defensiveness • Perseverance • Stamina

**English Parap...
    """
    
    original_text: str = """**Source Text** (Lines 5443-5499): Keywords: Defensiveness • Perseverance • Stamina

**English Paraphrase**: **Nine of Wands** represents "perseverance"—being wounded but continuing, having stamina, defending despite exhaustion.

**Complete Chinese Interpretation**: **权杖九**代表"坚持不懈"——受伤但继续前进、有耐力、尽管疲惫仍在防守。

**Core Points**: Nine of Wands = defensiveness, perseverance, stamina; Wounded but continuing; Last stand

**Narrative Snippets**:
- `[ns_ltt_080]` `[trigger: nine_wands]` `[factor_trigger: tarot_nine_wands]` `[role: 主干]` Nine of Wands represents perseverance despite being wounded. → L5443-5455"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Wands (权杖九)"
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
        l1_anchor="lt_v1.0.0_nine_of_wands__权杖九_001_L1",
    )
    version: str = "1.0.0"
