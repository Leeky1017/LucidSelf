"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008055
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
    semantic_id="lt_v1.0.0_the_hermit__隐士_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheHermit隐士(SemanticEntry):
    """
    **Source Text** (Lines 4057-4120): Keywords: Introspection • Searching • Guidance • Solitude

**Engl...
    """
    
    original_text: str = """**Source Text** (Lines 4057-4120): Keywords: Introspection • Searching • Guidance • Solitude

**English Paraphrase**: **The Hermit (Card 9)** represents "the desire to turn away from society to focus on the inner world." He seeks answers within through quiet and solitude.

**Complete Chinese Interpretation**: **隐士（第9号牌）**代表"渴望从社会转身，专注于内在世界"。他通过安静和独处在内心寻找答案。

**Core Points**: Card 9 = introspection, searching, guidance, solitude; Focus on inner world; Answers within

**Narrative Snippets**:
- `[ns_ltt_045]` `[trigger: hermit_card]` `[factor_trigger: tarot_hermit AND tarot_introspection]` `[role: 主干]` The Hermit withdraws from external distractions to seek answers within; his lantern illuminates not outward paths but inner truth—guidance comes from self-knowledge, not external authorities. → L4103-4106
- `[ns_ltt_046]` `[trigger: hermit_solitude]` `[factor_trigger: tarot_hermit AND tarot_solitude]` `[role: 主干依赖]` The Hermit's solitude is purposeful, not escapist: he withdraws temporarily to gain perspective that crowds obscure, then returns with wisdom to share (the raised lantern). → L4114-4116"""
    normalized_text_zh: str = """"""
    subject: str = "The Hermit (隐士)"
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
        l1_anchor="lt_v1.0.0_the_hermit__隐士_001_L1",
    )
    version: str = "1.0.0"
