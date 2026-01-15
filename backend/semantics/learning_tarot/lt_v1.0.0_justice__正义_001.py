"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008076
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
    semantic_id="lt_v1.0.0_justice__正义_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Justice正义(SemanticEntry):
    """
    **Source Text** (Lines 4187-4256): Keywords: Justice • Responsibility • Decision • Cause and Effect
...
    """
    
    original_text: str = """**Source Text** (Lines 4187-4256): Keywords: Justice • Responsibility • Decision • Cause and Effect

**English Paraphrase**: **Justice (Card 11)** represents "the understanding that life is ultimately fair and just"—universal order through karma, where causes return as effects.

**Complete Chinese Interpretation**: **正义（第11号牌）**代表"对生命最终是公平和公正的理解"——通过因果的宇宙秩序，原因作为结果返回。

**Core Points**: Card 11 = justice, responsibility, decision, karma; Universal order through karma; Causes return as effects

**Narrative Snippets**:
- `[ns_ltt_049]` `[trigger: justice_card]` `[factor_trigger: tarot_justice AND tarot_karma]` `[role: 主干]` Justice embodies cosmic law: every action generates consequences that return to the actor; the sword cuts through illusion while the scales weigh deeds with perfect impartiality—no external judge is needed. → L4238-4243
- `[ns_ltt_050]` `[trigger: justice_responsibility]` `[factor_trigger: tarot_justice AND tarot_decision]` `[role: 主干依赖]` Justice demands honest self-assessment: what have you contributed to your current situation? The card calls for taking responsibility rather than blaming external circumstances. → L4250-4252"""
    normalized_text_zh: str = """"""
    subject: str = "Justice (正义)"
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
        l1_anchor="lt_v1.0.0_justice__正义_001_L1",
    )
    version: str = "1.0.0"
