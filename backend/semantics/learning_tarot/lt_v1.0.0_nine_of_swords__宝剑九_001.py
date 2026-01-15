"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008461
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
    semantic_id="lt_v1.0.0_nine_of_swords__宝剑九_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class NineOfSwords宝剑九(SemanticEntry):
    """
    **Source Text** (Lines 6593-6649): Keywords: Worry • Guilt • Anguish

**English Paraphrase**: **Nine...
    """
    
    original_text: str = """**Source Text** (Lines 6593-6649): Keywords: Worry • Guilt • Anguish

**English Paraphrase**: **Nine of Swords** represents "worry and anguish"—nightmares, guilt, sleepless nights, mental torment.

**Complete Chinese Interpretation**: **宝剑九**代表"忧虑和痛苦"——噩梦、内疚、不眠之夜、精神折磨。

**Core Points**: Nine of Swords = worry, guilt, anguish; Sleepless nights; Mental torment

**Narrative Snippets**:
- `[ns_ltt_100]` `[trigger: nine_swords]` `[factor_trigger: tarot_nine_swords AND tarot_anxiety]` `[role: 主干]` Nine of Swords shows the figure sitting up in bed with hands covering face: the nightmare of anxious thoughts that torture in darkness; often the fear is worse than reality warrants—the swords hang above but do not touch."""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Swords (宝剑九)"
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
        l1_anchor="lt_v1.0.0_nine_of_swords__宝剑九_001_L1",
    )
    version: str = "1.0.0"
