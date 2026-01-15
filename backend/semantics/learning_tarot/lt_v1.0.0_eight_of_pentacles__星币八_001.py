"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008551
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
    semantic_id="lt_v1.0.0_eight_of_pentacles__星币八_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class EightOfPentacles星币八(SemanticEntry):
    """
    **Source Text** (Lines 7111-7167): Keywords: Diligence • Knowledge • Detail

**English Paraphrase**:...
    """
    
    original_text: str = """**Source Text** (Lines 7111-7167): Keywords: Diligence • Knowledge • Detail

**English Paraphrase**: **Eight of Pentacles** represents "diligent work"—skill development, attention to detail, learning through practice.

**Complete Chinese Interpretation**: **星币八**代表"勤奋工作"——技能发展、注重细节、通过实践学习。

**Core Points**: Eight of Pentacles = diligence, knowledge, detail; Skill development; Dedicated practice

**Narrative Snippets**:
- `[ns_ltt_109]` `[trigger: eight_pentacles]` `[factor_trigger: tarot_eight_pentacles]` `[role: 主干]` Eight of Pentacles represents diligent skill development. → L7111-7120"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Pentacles (星币八)"
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
        l1_anchor="lt_v1.0.0_eight_of_pentacles__星币八_001_L1",
    )
    version: str = "1.0.0"
